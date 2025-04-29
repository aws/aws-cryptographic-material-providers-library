// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "Structure.dfy"
include "../../AwsCryptographicMaterialProviders/src/AwsArnParsing.dfy"
include "../../AwsCryptographicMaterialProviders/src/Keyrings/AwsKms/AwsKmsMrkMatchForDecrypt.dfy"
include "../../AwsCryptographicMaterialProviders/src/AwsArnParsing.dfy"
include "HierarchicalVersionUtils.dfy"
include "KmsArn.dfy"

module {:options "/functionSyntax:4" } KMSKeystoreOperations {
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import Seq
  import Types = AwsCryptographyKeyStoreTypes
  import DDB = ComAmazonawsDynamodbTypes
  import KMS = ComAmazonawsKmsTypes
  import HvUtils = HierarchicalVersionUtils
  import AtomicPrimitives
  import UTF8
  import Structure
  import opened AwsArnParsing
  import AwsKmsMrkMatchForDecrypt
  import KmsArn
  import ErrorMessages = KeyStoreErrorMessages
  import KmsUtils

  // TODO-HV-2-M4 : BKS Datatype for Crypto, Storage, KMS Tuple
  // TODO-HV-2-M4 : Move to a helper module
  /** Constrains the relationship of the Crypto & KMS client, 
    ensuring they a valid but their histories are separate.
    Also allows us to make claims about the Grant Tokens and kmsConfig. */
  datatype CryptoAndKms = CryptoAndKms(
    kmsConfig: Types.KMSConfiguration,
    kms: KmsUtils.keyManagerStrat,
    crypto: AtomicPrimitives.AtomicPrimitivesClient
  ) {
    ghost predicate ValidState()
    {
      && kms.ValidState()
      && HasKeyId(kmsConfig)
      && KmsArn.ValidKmsArn?(GetKeyId(kmsConfig))
      && kms.Modifies !! crypto.Modifies
      && crypto.ValidState()
    }
    ghost const Modifies := multiset(kms.Modifies) + multiset(crypto.Modifies)
  }

  type KmsError = e: Types.Error | (
        || e.ComAmazonawsKms?
        || e.KeyManagementException?
        || e.BranchKeyCiphertextException?
      ) witness *

  function replaceRegion(arn : KMS.KeyIdType, region : KMS.RegionType) : KMS.KeyIdType
  {
    var parsed := ParseAwsKmsArn(arn);
    if parsed.Failure? then
      arn
    else if !IsMultiRegionAwsKmsArn(parsed.value) then
      arn
    else
      var newArn := parsed.value.ToArnString(Some(region));
      if KMS.IsValid_KeyIdType(newArn) then
        newArn
      else
        arn
  }

  function GetArn(kmsConfiguration: Types.KMSConfiguration, discoverdArn : KMS.KeyIdType) : KMS.KeyIdType
  {
    match kmsConfiguration {
      case kmsKeyArn(arn) => arn
      case kmsMRKeyArn(arn) => arn
      case discovery(obj) =>  discoverdArn
      case mrDiscovery(region) =>  replaceRegion(discoverdArn, region.region)
    }
  }

  predicate AttemptKmsOperation?(kmsConfiguration: Types.KMSConfiguration, kmsArnInStorage: string)
    ensures AttemptKmsOperation?(kmsConfiguration, kmsArnInStorage) && HasKeyId(kmsConfiguration)
            ==> Compatible?(kmsConfiguration, kmsArnInStorage)
  {
    match kmsConfiguration
    case kmsKeyArn(arn) => (arn == kmsArnInStorage) && KmsArn.ValidKmsArn?(arn)
    case kmsMRKeyArn(arn) => MrkMatch(arn, kmsArnInStorage) && KmsArn.ValidKmsArn?(arn)
    case discovery(obj) => KmsArn.ValidKmsArn?(kmsArnInStorage)
    case mrDiscovery(obj) => KmsArn.ValidKmsArn?(kmsArnInStorage)
  }

  predicate Compatible?(kmsConfiguration: Types.KMSConfiguration, keyId : string)
    requires(HasKeyId(kmsConfiguration))
  {
    match kmsConfiguration
    case kmsKeyArn(arn) => (arn == keyId)
    case kmsMRKeyArn(arn) => MrkMatch(arn, keyId)
  }

  predicate OptCompatible?(kmsConfiguration: Types.KMSConfiguration, keyId : Option<string>)
    requires(HasKeyId(kmsConfiguration))
  {
    keyId.Some? && Compatible?(kmsConfiguration, keyId.value)
  }

  predicate MrkMatch(x : string, y : string)
  {
    var xArn := ParseAwsKmsArn(x);
    var yArn := ParseAwsKmsArn(y);
    if xArn.Failure? || yArn.Failure? then
      false
    else
      AwsKmsMrkMatchForDecrypt.AwsKmsMrkMatchForDecrypt(AwsKmsArnIdentifier(xArn.value), AwsKmsArnIdentifier(yArn.value))
  }

  predicate HasKeyId(kmsConfiguration: Types.KMSConfiguration)
  {
    kmsConfiguration.kmsKeyArn? || kmsConfiguration.kmsMRKeyArn?
  }

  function GetKeyId(kmsConfiguration: Types.KMSConfiguration) : KMS.KeyIdType
    requires HasKeyId(kmsConfiguration)
  {
    match kmsConfiguration
    case kmsKeyArn(arn) => arn
    case kmsMRKeyArn(arn) => arn
  }

  method GetPlaintextDataKeyViaGenerateDataKey(
    nameonly encryptionContext: map<string, string>,
    nameonly kmsConfiguration: Types.KMSConfiguration,
    nameonly keyManagerAndStorage: KmsUtils.KeyManagerAndStorage
  )
    returns (output: Result<seq<uint8>, Types.Error>)
    requires
      // TODO-HV2-DecryptEncrypt support Decrypt/Encrypt
      && keyManagerAndStorage.keyManagerStrat.kmsSimple?
      && keyManagerAndStorage.ValidState()
      && HasKeyId(kmsConfiguration)
      && KmsArn.ValidKmsArn?(GetKeyId(kmsConfiguration))
    modifies keyManagerAndStorage.Modifies
    ensures keyManagerAndStorage.ValidState()
    ensures output.Success?
            ==>
              && var kms := keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient;
              && |kms.History.GenerateDataKey| == |old(kms.History.GenerateDataKey)| + 1
              && old(kms.History.Encrypt) == kms.History.Encrypt
              && var kmsGenerateDataKeyEvent := Seq.Last(kms.History.GenerateDataKey);
              && var kmsKeyArn := GetKeyId(kmsConfiguration);
              && KMS.GenerateDataKeyRequest(
                   KeyId := kmsKeyArn,
                   NumberOfBytes := Some(32),
                   EncryptionContext := Some(branchKeyContext),
                   GrantTokens := Some(keyManagerAndStorage.keyManagerStrat.kmsSimple.grantTokens)
                 ) == kmsGenerateDataKeyEvent.input
              && kmsGenerateDataKeyEvent.output.Success?
              && kmsGenerateDataKeyEvent.output.value.Plaintext.Some?
              && |kmsGenerateDataKeyEvent.output.value.Plaintext.value| == 32
              && kmsGenerateDataKeyEvent.output.value.KeyId.Some?
              && kmsGenerateDataKeyEvent.output.value.KeyId.value == kmsKeyArn
              && kmsGenerateDataKeyEvent.output.value.Plaintext.value == output.value
  {
    var kmsKeyArn := GetKeyId(kmsConfiguration);
    var generateDataKeyInput := KMS.GenerateDataKeyRequest(
      KeyId := kmsKeyArn,
      NumberOfBytes := Some(32),
      EncryptionContext := Some(branchKeyContext),
      GrantTokens := Some(keyManagerAndStorage.keyManagerStrat.kmsSimple.grantTokens)
    );

    var generateDataKeyResponse? := keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.GenerateDataKey(
      generateDataKeyInput
    );

    var generateDataKeyResponse :- generateDataKeyResponse?
    .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));

    :- Need(
      && generateDataKeyResponse.Plaintext.Some?
      && |generateDataKeyResponse.Plaintext.value| == 32,
      Types.KeyManagementException(
        message := "Invalid response from AWS KMS GenerateDataKey: KMS response's Plaintext is invalid."
      )
    );
    :- Need(
      && generateDataKeyResponse.KeyId.Some?
      && generateDataKeyResponse.KeyId.value ==  kmsKeyArn,
      Types.KeyManagementException(
        message := "Invalid response from AWS KMS GenerateDataKey: KMS Key ID of response did not match request."
      )
    );

    output := Success(generateDataKeyResponse.Plaintext.value);
  }

  method GenerateKey(
    encryptionContext: Structure.BranchKeyContext,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  )
    returns (res: Result<KMS.GenerateDataKeyWithoutPlaintextResponse, KmsError>)
    requires kmsClient.ValidState()
    requires HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(GetKeyId(kmsConfiguration))
    requires AttemptKmsOperation?(kmsConfiguration, encryptionContext[Structure.KMS_FIELD])
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()
    ensures
      && |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 1
      && var kmsKeyArn := GetKeyId(kmsConfiguration);
      && KMS.GenerateDataKeyWithoutPlaintextRequest(
           KeyId := kmsKeyArn,
           EncryptionContext := Some(encryptionContext),
           KeySpec := None,
           NumberOfBytes := Some(32),
           GrantTokens := Some(grantTokens)
         )
         == Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).input
      && old(kmsClient.History.GenerateDataKeyWithoutPlaintext) < kmsClient.History.GenerateDataKeyWithoutPlaintext
      && old(kmsClient.History.ReEncrypt) == kmsClient.History.ReEncrypt

    ensures res.Success? ==>
              && res.value.KeyId.Some?
              && res.value.CiphertextBlob.Some?
              && KMS.IsValid_CiphertextType(res.value.CiphertextBlob.value)
              && var kmsOperationOutput := Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output;
              && kmsOperationOutput.Success?
              && kmsOperationOutput.value == res.value
  {
    var kmsKeyArn := GetKeyId(kmsConfiguration);
    var generatorRequest := KMS.GenerateDataKeyWithoutPlaintextRequest(
      KeyId := kmsKeyArn,
      EncryptionContext := Some(encryptionContext),
      KeySpec := None,
      NumberOfBytes := Some(32),
      GrantTokens := Some(grantTokens)
    );

    var maybeGenerateResponse := kmsClient.GenerateDataKeyWithoutPlaintext(generatorRequest);
    var generateResponse :- maybeGenerateResponse
    .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));

    :- Need(
      && generateResponse.KeyId.Some?,
      Types.KeyManagementException(
        message := "Invalid response from AWS KMS GenerateDataKey: Invalid Key Id")
    );

    :- Need(
      && generateResponse.CiphertextBlob.Some?
      && KMS.IsValid_CiphertextType(generateResponse.CiphertextBlob.value),
      Types.KeyManagementException(
        message := "Invalid response from AWS KMS GenerateDataKey: Invalid ciphertext")
    );

    return Success(generateResponse);
  }

  ghost predicate AttemptReEncrypt?(
    sourceEncryptionContext: Structure.BranchKeyContext,
    destinationEncryptionContext: Structure.BranchKeyContext
  )
    requires
      && Structure.BranchKeyContext?(sourceEncryptionContext)
      && Structure.BranchKeyContext?(destinationEncryptionContext)
  {
    // This is to validate the encryption context
    // Therefore no change is an OK transition
    || (destinationEncryptionContext == sourceEncryptionContext)

    // Creating an Active record from a Version is OK
    || (
         // This is the defining characteristic of a Version record.
         && Structure.BRANCH_KEY_TYPE_PREFIX < sourceEncryptionContext[Structure.TYPE_FIELD]
         && Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD !in sourceEncryptionContext
         && destinationEncryptionContext == Structure.ActiveBranchKeyEncryptionContext(sourceEncryptionContext)
       )

    // KMS_FIELD can change and any non-reserved encryption context
    || (
         && sourceEncryptionContext[Structure.BRANCH_KEY_IDENTIFIER_FIELD] == destinationEncryptionContext[Structure.BRANCH_KEY_IDENTIFIER_FIELD]
         && sourceEncryptionContext[Structure.TYPE_FIELD] == destinationEncryptionContext[Structure.TYPE_FIELD]
         && sourceEncryptionContext[Structure.KEY_CREATE_TIME] == destinationEncryptionContext[Structure.KEY_CREATE_TIME]
         && sourceEncryptionContext[Structure.HIERARCHY_VERSION] == destinationEncryptionContext[Structure.HIERARCHY_VERSION]
         && sourceEncryptionContext[Structure.TABLE_FIELD] == destinationEncryptionContext[Structure.TABLE_FIELD]
            // @seebees for AttemptReEncrypt?, I do not think we need the following IFF:
            // It would only apply to ACTIVE Items, which we never ReEncrypt.
            // No other Items have `version` as a member of their EC
         && (Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD in sourceEncryptionContext
             <==>
             && Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD in destinationEncryptionContext
             && sourceEncryptionContext[Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD] == destinationEncryptionContext[Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD]
            )
       )
  }

  method ReEncryptKey(
    ciphertext: seq<uint8>,
    sourceEncryptionContext: Structure.BranchKeyContext,
    destinationEncryptionContext: Structure.BranchKeyContext,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  )
    returns (res: Result<KMS.ReEncryptResponse, KmsError>)
    requires
      && Structure.BranchKeyContext?(sourceEncryptionContext)
      && Structure.BranchKeyContext?(destinationEncryptionContext)
    requires AttemptReEncrypt?(sourceEncryptionContext, destinationEncryptionContext)
    requires AttemptKmsOperation?(kmsConfiguration, destinationEncryptionContext[Structure.KMS_FIELD])
    requires HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(GetKeyId(kmsConfiguration))
    requires kmsClient.ValidState()
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()

    ensures
      res.Success?
      ==>
        && KMS.IsValid_CiphertextType(ciphertext)
        && |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 1
        && var kmsKeyArn := GetKeyId(kmsConfiguration);
        && KMS.ReEncryptRequest(
             CiphertextBlob := ciphertext,
             SourceEncryptionContext := Some(sourceEncryptionContext),
             SourceKeyId := Some(kmsKeyArn),
             DestinationKeyId := kmsKeyArn,
             DestinationEncryptionContext := Some(destinationEncryptionContext),
             SourceEncryptionAlgorithm := None,
             DestinationEncryptionAlgorithm := None,
             GrantTokens := Some(grantTokens)
           )
           == Seq.Last(kmsClient.History.ReEncrypt).input
        && old(kmsClient.History.ReEncrypt) < kmsClient.History.ReEncrypt
        && old(kmsClient.History.GenerateDataKeyWithoutPlaintext) == kmsClient.History.GenerateDataKeyWithoutPlaintext

    ensures
      res.Success? ==>
        && var kmsKeyArn := GetKeyId(kmsConfiguration);
        && res.value.CiphertextBlob.Some?
        && res.value.SourceKeyId.Some?
        && res.value.KeyId.Some?
        && res.value.SourceKeyId.value == kmsKeyArn
        && res.value.KeyId.value == kmsKeyArn
        && KMS.IsValid_CiphertextType(res.value.CiphertextBlob.value)
        && var kmsOperationOutput := Seq.Last(kmsClient.History.ReEncrypt).output;
        && kmsOperationOutput.Success?
        && kmsOperationOutput.value == res.value
  {
    :- Need(
      KMS.IsValid_CiphertextType(ciphertext),
      Types.KeyManagementException(
        message := "Invalid KMS ciphertext.")
    );

    var kmsKeyArn := GetKeyId(kmsConfiguration);
    var reEncryptRequest := KMS.ReEncryptRequest(
      CiphertextBlob := ciphertext,
      SourceEncryptionContext := Some(sourceEncryptionContext),
      SourceKeyId := Some(kmsKeyArn),
      DestinationKeyId := kmsKeyArn,
      DestinationEncryptionContext := Some(destinationEncryptionContext),
      SourceEncryptionAlgorithm := None,
      DestinationEncryptionAlgorithm := None,
      GrantTokens := Some(grantTokens)
    );

    var maybeReEncryptResponse := kmsClient.ReEncrypt(reEncryptRequest);
    var reEncryptResponse :- maybeReEncryptResponse
    .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));

    :- Need(
      && reEncryptResponse.SourceKeyId.Some?
      && reEncryptResponse.KeyId.Some?
      && reEncryptResponse.SourceKeyId.value == kmsKeyArn
      && reEncryptResponse.KeyId.value == kmsKeyArn,
      Types.KeyManagementException(
        message := "Invalid response from AWS KMS ReEncrypt: Invalid KMS Key Id")
    );

    :- Need(
      && reEncryptResponse.CiphertextBlob.Some?
      && KMS.IsValid_CiphertextType(reEncryptResponse.CiphertextBlob.value),
      Types.KeyManagementException(
        message := "Invalid response from AWS KMS ReEncrypt: Invalid ciphertext.")
    );

    return Success(reEncryptResponse);
  }

  // TODO-HV-2-M1: Add a Dafny test
  method EncryptKey(
    plaintext: KMS.PlaintextType,
    encryptionContext: Types.EncryptionContextString,
    kmsArnToStorage: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  )
    returns (res: Result<KMS.CiphertextType, KmsError>)
    requires kmsClient.ValidState()
    requires |plaintext| == 80 || |plaintext| == 32
    requires |plaintext| == 32 ==> (
                 && Structure.BranchKeyContext?(encryptionContext)
                 && encryptionContext[Structure.KMS_FIELD] == kmsArnToStorage
                 && encryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_1 )
    requires HasKeyId(kmsConfiguration) && GetKeyId(kmsConfiguration) == kmsArnToStorage && KmsArn.ValidKmsArn?(kmsArnToStorage)
    requires AttemptKmsOperation?(kmsConfiguration, kmsArnToStorage)
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()
    ensures
      res.Success?
      ==>
        && |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 1
        && kmsClient.History.GenerateDataKey == old(kmsClient.History.GenerateDataKey)
        && var kmsKeyArn := GetKeyId(kmsConfiguration);

        && var encryptInput := Seq.Last(kmsClient.History.Encrypt).input;
        && KMS.EncryptRequest(
             KeyId := kmsKeyArn,
             Plaintext := plaintext,
             EncryptionContext := Some(encryptionContext),
             GrantTokens := Some(grantTokens)
           ) == encryptInput

        && old(kmsClient.History.Encrypt) < kmsClient.History.Encrypt
        && var encryptResponse := Seq.Last(kmsClient.History.Encrypt).output;
        && encryptResponse.Success?
        && encryptResponse.value.CiphertextBlob.Some?
        && encryptResponse.value.KeyId.Some?
        && encryptResponse.value.KeyId.value == kmsKeyArn // kmsKeyArn
        && KMS.IsValid_CiphertextType(encryptResponse.value.CiphertextBlob.value)
        && encryptResponse.value.CiphertextBlob.value == res.value
  {
    var kmsKeyArn := GetKeyId(kmsConfiguration);
    var kmsEncryptRequest := KMS.EncryptRequest(
      KeyId := kmsKeyArn,
      Plaintext := plaintext,
      EncryptionContext := Some(encryptionContext),
      GrantTokens := Some(grantTokens)
    );

    var encryptResponse? := kmsClient.Encrypt(kmsEncryptRequest);
    var encryptResponse :- encryptResponse?
    .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));

    :- Need(
      && encryptResponse.CiphertextBlob.Some?
      && KMS.IsValid_CiphertextType(encryptResponse.CiphertextBlob.value),
      Types.KeyManagementException(
        message := "Invalid response from AWS KMS Encrypt: KMS response's Ciphertext is invalid."
      )
    );
    :- Need(
      && encryptResponse.KeyId.Some?
      && encryptResponse.KeyId.value ==  kmsKeyArn,
      Types.KeyManagementException(
        message := "Invalid response from AWS KMS Encrypt: KMS Key ID of response did not match request."
      )
    );
    return Success(encryptResponse.CiphertextBlob.value);
  }

  method VerifyViaDecryptEncryptKey(
    ciphertext: seq<uint8>,
    sourceEncryptionContext: Structure.BranchKeyContext,
    destinationEncryptionContext: Structure.BranchKeyContext,
    kmsConfiguration: Types.KMSConfiguration,
    decryptGrantTokens: KMS.GrantTokenList,
    decryptKmsClient: KMS.IKMSClient
  )
    returns (res: Result<KMS.DecryptResponse, KmsError>)
    requires
      && Structure.BranchKeyContext?(sourceEncryptionContext)
      && Structure.BranchKeyContext?(destinationEncryptionContext)
    requires AttemptReEncrypt?(sourceEncryptionContext, destinationEncryptionContext)
    requires AttemptKmsOperation?(kmsConfiguration, destinationEncryptionContext[Structure.KMS_FIELD])
    requires HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(GetKeyId(kmsConfiguration))
    requires decryptKmsClient.ValidState()
    modifies decryptKmsClient.Modifies
    ensures  decryptKmsClient.ValidState()

    ensures
      res.Success?
      ==>
        // Proof for success when we decrypt
        && KMS.IsValid_CiphertextType(ciphertext)
        && |decryptKmsClient.History.Decrypt| == |old(decryptKmsClient.History.Decrypt)| + 1
        && var decryptInput := Seq.Last(decryptKmsClient.History.Decrypt).input;
        && var decryptResponse := Seq.Last(decryptKmsClient.History.Decrypt).output;
        && var kmsKeyArn := GetKeyId(kmsConfiguration);
        && KMS.DecryptRequest(
             CiphertextBlob := ciphertext,
             EncryptionContext := Some(sourceEncryptionContext),
             GrantTokens := Some(decryptGrantTokens),
             KeyId := Some(kmsKeyArn)
           ) == decryptInput
        && var decryptResponse := Seq.Last(decryptKmsClient.History.Decrypt).output;
        && decryptResponse.Success? && decryptResponse.value.Plaintext.Some?
        && old(decryptKmsClient.History.Decrypt) < decryptKmsClient.History.Decrypt
        && decryptResponse.value == res.value
  {
    :- Need(
      KMS.IsValid_CiphertextType(ciphertext),
      Types.KeyManagementException(
        message := "Invalid KMS ciphertext.")
    );

    var kmsKeyArn := GetKeyId(kmsConfiguration);
    var kmsDecryptRequest := KMS.DecryptRequest(
      CiphertextBlob := ciphertext,
      EncryptionContext := Some(sourceEncryptionContext),
      GrantTokens := Some(decryptGrantTokens),
      KeyId := Some(kmsKeyArn)
    );

    var decryptResponse? := decryptKmsClient.Decrypt(kmsDecryptRequest);
    var decryptResponse :- decryptResponse?
    .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));

    :- Need(
      && decryptResponse.Plaintext.Some?
      && decryptResponse.KeyId.Some?
      && decryptResponse.KeyId.value == kmsKeyArn,
      Types.KeyManagementException(
        message := "Invalid response from AWS KMS Decrypt: Invalid KMS Key Id"
      ));

    return Success(decryptResponse);
  }

  method MutateViaDecryptEncryptOnInitializeMutation(
    ciphertext: seq<uint8>,
    sourceEncryptionContext: Structure.BranchKeyContext,
    destinationEncryptionContext: Structure.BranchKeyContext,
    sourceKmsArn: string,
    destinationKmsArn: string,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  )
    returns (res: Result<KMS.CiphertextType, KmsError>)
    requires
      && Structure.BranchKeyContext?(sourceEncryptionContext)
      && Structure.BranchKeyContext?(destinationEncryptionContext)
    requires AttemptReEncrypt?(sourceEncryptionContext, destinationEncryptionContext)
    requires KmsArn.ValidKmsArn?(sourceKmsArn) && KmsArn.ValidKmsArn?(destinationKmsArn)
    requires kmsClient.ValidState()
    modifies kmsClient.Modifies
    ensures  kmsClient.ValidState()
    ensures
      res.Success?
      ==>
        && KMS.IsValid_CiphertextType(ciphertext)
        && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1
        && var decryptInput := Seq.Last(kmsClient.History.Decrypt).input;
        && var decryptOutput := Seq.Last(kmsClient.History.Decrypt).output;
        && KMS.DecryptRequest(
             CiphertextBlob := ciphertext,
             EncryptionContext := Some(sourceEncryptionContext),
             GrantTokens := Some(grantTokens),
             KeyId := Some(sourceKmsArn)
           ) == decryptInput
        && decryptOutput.Success? && decryptOutput.value.Plaintext.Some? && decryptOutput.value.KeyId.Some?
        && decryptOutput.value.KeyId.value == sourceKmsArn
        && |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 1
        && var encryptInput := Seq.Last(kmsClient.History.Encrypt).input;
        && var encryptResponse := Seq.Last(kmsClient.History.Encrypt).output;
        && KMS.EncryptRequest(
             KeyId := destinationKmsArn,
             Plaintext := decryptOutput.value.Plaintext.value,
             EncryptionContext := Some(destinationEncryptionContext),
             GrantTokens := Some(grantTokens)
           ) == encryptInput
        && old(kmsClient.History.Encrypt) < kmsClient.History.Encrypt
        && encryptResponse.Success?
        && encryptResponse.value.CiphertextBlob.Some?
        && encryptResponse.value.KeyId.Some?
        && encryptResponse.value.KeyId.value ==  destinationKmsArn // kmsKeyArn
        && KMS.IsValid_CiphertextType(encryptResponse.value.CiphertextBlob.value)
        && encryptResponse.value.CiphertextBlob.value == res.value
  {
    :- Need(
      KMS.IsValid_CiphertextType(ciphertext),
      Types.KeyManagementException(
        message := "Invalid KMS ciphertext.")
    );

    var kmsDecryptRequest := KMS.DecryptRequest(
      CiphertextBlob := ciphertext,
      EncryptionContext := Some(sourceEncryptionContext),
      GrantTokens := Some(grantTokens),
      KeyId := Some(sourceKmsArn)
    );

    var decryptResponse? := kmsClient.Decrypt(kmsDecryptRequest);
    var decryptResponse :- decryptResponse?
    .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));

    :- Need(
      && decryptResponse.Plaintext.Some?
      && decryptResponse.KeyId.Some?
      && decryptResponse.KeyId.value == sourceKmsArn,
      Types.KeyManagementException(
        message := "Invalid response from AWS KMS Decrypt: Invalid KMS Key Id"
      ));

    var kmsEncryptRequest := KMS.EncryptRequest(
      KeyId := destinationKmsArn,
      Plaintext := decryptResponse.Plaintext.value,
      EncryptionContext := Some(destinationEncryptionContext),
      GrantTokens := Some(grantTokens)
    );

    var encryptResponse? := kmsClient.Encrypt(kmsEncryptRequest);
    var encryptResponse :- encryptResponse?
    .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));

    :- Need(
      && encryptResponse.CiphertextBlob.Some?
      && KMS.IsValid_CiphertextType(encryptResponse.CiphertextBlob.value)
      && encryptResponse.KeyId.Some?
      && encryptResponse.KeyId.value == destinationKmsArn,
      Types.KeyManagementException(
        message := "Invalid response from AWS KMS Encrypt: Invalid KMS Key Id"
      ));

    return Success(encryptResponse.CiphertextBlob.value);
  }

  method MutateViaReEncrypt(
    ciphertext: seq<uint8>,
    sourceEncryptionContext: Structure.BranchKeyContext,
    destinationEncryptionContext: Structure.BranchKeyContext,
    sourceKmsArn: string,
    destinationKmsArn: string,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  )
    returns (res: Result<KMS.CiphertextType, KmsError>)
    requires
      && Structure.BranchKeyContext?(sourceEncryptionContext)
      && Structure.BranchKeyContext?(destinationEncryptionContext)
    requires AttemptReEncrypt?(sourceEncryptionContext, destinationEncryptionContext)
    requires KmsArn.ValidKmsArn?(sourceKmsArn) && KmsArn.ValidKmsArn?(destinationKmsArn)
    // requires AttemptKmsOperation?(kmsConfiguration, destinationEncryptionContext[Structure.KMS_FIELD])
    // requires HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(GetKeyId(kmsConfiguration))
    requires kmsClient.ValidState()
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()

    ensures
      res.Success?
      ==>
        && KMS.IsValid_CiphertextType(ciphertext)
        && |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 1
           // && var kmsKeyArn := GetKeyId(kmsConfiguration);
        && KMS.ReEncryptRequest(
             CiphertextBlob := ciphertext,
             SourceEncryptionContext := Some(sourceEncryptionContext),
             // SourceKeyId := Some(kmsKeyArn),
             SourceKeyId := Some(sourceKmsArn),
             DestinationKeyId := destinationKmsArn,
             DestinationEncryptionContext := Some(destinationEncryptionContext),
             SourceEncryptionAlgorithm := None,
             DestinationEncryptionAlgorithm := None,
             GrantTokens := Some(grantTokens)
           )
           == Seq.Last(kmsClient.History.ReEncrypt).input
        && old(kmsClient.History.ReEncrypt) < kmsClient.History.ReEncrypt
    // Apply Mutation cannot have a history with GenerateDataKeyWithoutPlaintext in it
    // && old(kmsClient.History.GenerateDataKeyWithoutPlaintext) == kmsClient.History.GenerateDataKeyWithoutPlaintext

    ensures
      res.Success? ==>
        // && var kmsKeyArn := GetKeyId(kmsConfiguration);
        && var kmsOperationOutput := Seq.Last(kmsClient.History.ReEncrypt).output;
        && kmsOperationOutput.Success?
        && kmsOperationOutput.value.CiphertextBlob.Some?
        && kmsOperationOutput.value.SourceKeyId.Some?
        && kmsOperationOutput.value.KeyId.Some?
        && kmsOperationOutput.value.SourceKeyId.value == sourceKmsArn //kmsKeyArn
        && kmsOperationOutput.value.KeyId.value ==  destinationKmsArn // kmsKeyArn
        && KMS.IsValid_CiphertextType(kmsOperationOutput.value.CiphertextBlob.value)
        && kmsOperationOutput.value.CiphertextBlob.value == res.value
  {
    :- Need(
      KMS.IsValid_CiphertextType(ciphertext),
      Types.KeyManagementException(
        message := "Invalid KMS ciphertext.")
    );

    // var kmsKeyArn := GetKeyId(kmsConfiguration);
    var reEncryptRequest := KMS.ReEncryptRequest(
      CiphertextBlob := ciphertext,
      SourceEncryptionContext := Some(sourceEncryptionContext),
      SourceKeyId := Some(sourceKmsArn), //Some(kmsKeyArn),
      DestinationKeyId := destinationKmsArn,
      DestinationEncryptionContext := Some(destinationEncryptionContext),
      SourceEncryptionAlgorithm := None,
      DestinationEncryptionAlgorithm := None,
      GrantTokens := Some(grantTokens)
    );

    var reEncryptResponse? := kmsClient.ReEncrypt(reEncryptRequest);
    var reEncryptResponse :- reEncryptResponse?
    .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));

    :- Need(
      && reEncryptResponse.SourceKeyId.Some?
      && reEncryptResponse.SourceKeyId.value == sourceKmsArn,  //kmsKeyArn
      Types.KeyManagementException(
        message := "Invalid response from KMS ReEncrypt: Invalid Source Key Id")
    );
    :- Need(
      && reEncryptResponse.KeyId.Some?
      && reEncryptResponse.KeyId.value == destinationKmsArn, // kmsKeyArn,
      Types.KeyManagementException(
        message := "Invalid response from KMS ReEncrypt: Invalid Destination Key Id")
    );

    :- Need(
      && reEncryptResponse.CiphertextBlob.Some?
      && KMS.IsValid_CiphertextType(reEncryptResponse.CiphertextBlob.value),
      Types.KeyManagementException(
        message := "Invalid response from AWS KMS ReEncrypt: Invalid ciphertext.")
    );

    return Success(reEncryptResponse.CiphertextBlob.value);
  }

  method DecryptKeyForHv1(
    encryptedKey: Types.EncryptedHierarchicalKey,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  )
    returns (output: Result<KMS.DecryptResponse, KmsError>)
    requires Structure.EncryptedHierarchicalKeyFromStorage?(encryptedKey)

    requires KmsArn.ValidKmsArn?(encryptedKey.KmsArn)
    requires AttemptKmsOperation?(kmsConfiguration, encryptedKey.EncryptionContext[Structure.KMS_FIELD])

    requires kmsClient.ValidState()
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()

    ensures output.Success?
            ==>
              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1
              && AwsKmsBranchKeyDecryptionForHV1?(
                   encryptedKey,
                   kmsConfiguration,
                   grantTokens,
                   kmsClient,
                   Seq.Last(kmsClient.History.Decrypt)
                 )

    ensures output.Success?
            ==>
              && Seq.Last(kmsClient.History.Decrypt).output.Success?
              && output.value == Seq.Last(kmsClient.History.Decrypt).output.value
              && output.value.Plaintext.Some?
              && 32 == |output.value.Plaintext.value|
              && encryptedKey.EncryptionContext[Structure.HIERARCHY_VERSION]
                 == Structure.HIERARCHY_VERSION_VALUE_1
  {
    :- Need(
      && KmsArn.ValidKmsArn?(encryptedKey.KmsArn)
         // This check is overloaded.
         // It is incredibly unlikely that the the stored ciphertext
         // has dropped to 0 or exceeds the KMS limit.
         // So the error message is left unchanged.
      && KMS.IsValid_CiphertextType(encryptedKey.CiphertextBlob),
      Types.KeyManagementException( message := ErrorMessages.RETRIEVED_KEYSTORE_ITEM_INVALID_KMS_ARN)
    );

    var kmsKeyArn := GetArn(kmsConfiguration, encryptedKey.KmsArn);
    var maybeDecryptResponse := kmsClient.Decrypt(
      KMS.DecryptRequest(
        CiphertextBlob := encryptedKey.CiphertextBlob,
        EncryptionContext := Some(encryptedKey.EncryptionContext),
        GrantTokens := Some(grantTokens),
        KeyId := Some(kmsKeyArn),
        EncryptionAlgorithm := None
      )
    );
    var decryptResponse :- maybeDecryptResponse.MapFailure(e => Types.ComAmazonawsKms(e));

    :- Need(
      && decryptResponse.Plaintext.Some?
      && 32 == |decryptResponse.Plaintext.value|
      && encryptedKey.EncryptionContext[Structure.HIERARCHY_VERSION]
         == Structure.HIERARCHY_VERSION_VALUE_1,
      Types.KeyManagementException(
        message := ErrorMessages.KMS_DECRYPT_INVALID_KEY_LENGTH_HV1)
    );

    output := Success(decryptResponse);

  }

  // TODO-HV-2-M1 : Add a Dafny Test
  method DecryptKeyForHv2(
    ciphertextBlob: seq<uint8>,
    encryptionContextToKms: Types.EncryptionContextString,
    kmsArnFromStorage: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  )
    returns (output: Result<KMS.DecryptResponse, KmsError>)

    requires kmsClient.ValidState()
    requires KmsArn.ValidKmsArn?(kmsArnFromStorage)
    requires AttemptKmsOperation?(kmsConfiguration, kmsArnFromStorage)

    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()

    ensures output.Success?
            ==>
              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1
              && AwsKmsBranchKeyDecryptionForHV2?(
                   ciphertextBlob,
                   encryptionContextToKms,
                   kmsArnFromStorage,
                   kmsConfiguration,
                   grantTokens,
                   kmsClient,
                   Seq.Last(kmsClient.History.Decrypt)
                 )
    ensures output.Success?
            ==>
              && Seq.Last(kmsClient.History.Decrypt).output.Success?
              && output.value == Seq.Last(kmsClient.History.Decrypt).output.value
              && output.value.Plaintext.Some?
              && 80 == |output.value.Plaintext.value|
  {
    :- Need(
      && KmsArn.ValidKmsArn?(kmsArnFromStorage)
         // This check is overloaded.
         // It is incredibly unlikely that the the stored ciphertext
         // has dropped to 0 or exceeds the KMS limit.
         // So the error message is left unchanged.
      && KMS.IsValid_CiphertextType(ciphertextBlob),
      Types.KeyManagementException( message := ErrorMessages.RETRIEVED_KEYSTORE_ITEM_INVALID_KMS_ARN)
    );

    var kmsKeyArn := GetArn(kmsConfiguration, kmsArnFromStorage);
    var maybeDecryptResponse := kmsClient.Decrypt(
      KMS.DecryptRequest(
        CiphertextBlob := ciphertextBlob,
        EncryptionContext := Some(encryptionContextToKms),
        GrantTokens := Some(grantTokens),
        KeyId := Some(kmsKeyArn),
        EncryptionAlgorithm := None
      )
    );
    var decryptResponse :- maybeDecryptResponse.MapFailure(e => Types.ComAmazonawsKms(e));

    :- Need(
      && decryptResponse.Plaintext.Some?
      && 80 == |decryptResponse.Plaintext.value|,
      Types.BranchKeyCiphertextException(
        message := ErrorMessages.KMS_DECRYPT_INVALID_KEY_LENGTH_HV2)
    );

    output := Success(decryptResponse);
  }

  ghost predicate AwsKmsBranchKeyDecryptionForHV1?(
    versionItem: Types.EncryptedHierarchicalKey,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    decryptHistory: KMS.DafnyCallEvent<KMS.DecryptRequest, Result<KMS.DecryptResponse, KMS.Error>>
  )
    reads kmsClient.History

    requires Structure.EncryptedHierarchicalKeyFromStorage?(versionItem)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# The operation MUST use the configured `KMS SDK Client` to decrypt the value of the branch key field.
    requires decryptHistory in kmsClient.History.Decrypt
  {
    && Structure.BRANCH_KEY_FIELD !in  versionItem.EncryptionContext

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# If the Keystore's [AWS KMS Configuration](#aws-kms-configuration) is `KMS Key ARN` or `KMS MRKey ARN`,
    //# the `kms-arn` field of the DDB response item MUST be
    //# [compatible with](#aws-key-arn-compatibility) the configured KMS Key in
    //# the [AWS KMS Configuration](#aws-kms-configuration) for this keystore,
    //# or the operation MUST fail.
    && (kmsConfiguration.kmsKeyArn? ==> versionItem.KmsArn == kmsConfiguration.kmsKeyArn)
    && (kmsConfiguration.kmsMRKeyArn? ==> MrkMatch(versionItem.KmsArn, kmsConfiguration.kmsMRKeyArn))

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# If the Keystore's [AWS KMS Configuration](#aws-kms-configuration) is `Discovery` or `MRDiscovery`,
    //# the `kms-arn` field of DDB response item MUST NOT be an Alias
    //# or the operation MUST fail.
    && (kmsConfiguration.discovery? || kmsConfiguration.mrDiscovery? ==> KmsArn.ValidKmsArn?(versionItem.KmsArn))

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# When calling [AWS KMS Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html),
    //# the keystore operation MUST call with a request constructed as follows:

    && var decryptRequest := decryptHistory.input;
    && decryptRequest.KeyId.Some?
       //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
       //= type=implication
       //# - `KeyId`, if the KMS Configuration is Discovery, MUST be the `kms-arn` attribute value of the AWS DDB response item.
    && (kmsConfiguration.discovery? ==> decryptRequest.KeyId == Some(versionItem.KmsArn))

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# If the KMS Configuration is MRDiscovery, `KeyId` MUST be the `kms-arn` attribute value of the AWS DDB response item, with the region replaced by the configured region.
    && (kmsConfiguration.mrDiscovery? ==> decryptRequest.KeyId == Some(replaceRegion(versionItem.KmsArn, kmsConfiguration.mrDiscovery.region)))

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# Otherwise, it MUST BE the Keystore's configured KMS Key.
    && (kmsConfiguration.kmsKeyArn? ==> decryptRequest.KeyId == Some(kmsConfiguration.kmsKeyArn))
    && (kmsConfiguration.kmsMRKeyArn? ==> MrkMatch(decryptRequest.KeyId.value, kmsConfiguration.kmsMRKeyArn))

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# - `CiphertextBlob` MUST be the `CiphertextBlob` attribute value on the provided EncryptedHierarchicalKey
    && decryptRequest.CiphertextBlob == versionItem.CiphertextBlob

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# - `EncryptionContext` MUST be the [encryption context](#encryption-context) of the provided EncryptedHierarchicalKey
    && decryptRequest.EncryptionContext == Some(versionItem.EncryptionContext)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# - `GrantTokens` MUST be this keystore's [grant tokens](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
    && decryptRequest.GrantTokens == Some(grantTokens)

    && decryptHistory.output.Success?
    && decryptHistory.output.value.Plaintext.Some?
  }

  ghost predicate AwsKmsBranchKeyDecryptionForHV2?(
    ciphertextBlob: seq<uint8>,
    encryptionContextToKms: Types.EncryptionContextString,
    kmsArnFromStorage: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    decryptHistory: KMS.DafnyCallEvent<KMS.DecryptRequest, Result<KMS.DecryptResponse, KMS.Error>>
  )
    reads kmsClient.History

    requires decryptHistory in kmsClient.History.Decrypt
  {
    && (kmsConfiguration.kmsKeyArn? ==> kmsArnFromStorage == kmsConfiguration.kmsKeyArn)

    && (kmsConfiguration.kmsMRKeyArn? ==> MrkMatch(kmsArnFromStorage, kmsConfiguration.kmsMRKeyArn))

    && (kmsConfiguration.discovery? || kmsConfiguration.mrDiscovery? ==> KmsArn.ValidKmsArn?(kmsArnFromStorage))

    && var decryptRequest := decryptHistory.input;

    && decryptRequest.KeyId.Some?

    && (kmsConfiguration.discovery? ==> decryptRequest.KeyId == Some(kmsArnFromStorage))

    && (kmsConfiguration.mrDiscovery? ==> decryptRequest.KeyId == Some(replaceRegion(kmsArnFromStorage, kmsConfiguration.mrDiscovery.region)))

    && (kmsConfiguration.kmsKeyArn? ==> decryptRequest.KeyId == Some(kmsConfiguration.kmsKeyArn))

    && (kmsConfiguration.kmsMRKeyArn? ==> MrkMatch(decryptRequest.KeyId.value, kmsConfiguration.kmsMRKeyArn))

    && decryptRequest.CiphertextBlob == ciphertextBlob

    && decryptRequest.EncryptionContext == Some(encryptionContextToKms)

    && decryptRequest.GrantTokens == Some(grantTokens)

    && decryptHistory.output.Success?

    && decryptHistory.output.value.Plaintext.Some?

    && |decryptHistory.output.value.Plaintext.value| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int
  }

  //TODO-HV-2-M4: Move to HVUtils
  method packAndCallKMS(
    nameonly branchKeyContext: map<string, string>,
    nameonly cryptoAndKms: CryptoAndKms,
    nameonly material: seq<uint8>,
    nameonly encryptionContext: map<string, string>
  )
    returns (output: Result<Types.EncryptedHierarchicalKey, Types.Error>)
    requires
      && cryptoAndKms.ValidState()
      && Structure.BranchKeyContext?(branchKeyContext)
      && |material| == Structure.AES_256_LENGTH as int
      && AttemptKmsOperation?(cryptoAndKms.kmsConfig, branchKeyContext[Structure.KMS_FIELD])
      && GetKeyId(cryptoAndKms.kmsConfig) == branchKeyContext[Structure.KMS_FIELD]
         // TODO-HV-2-M? : Support KmsDecryptEncrypt?
      && cryptoAndKms.kms.kmsSimple?
    modifies cryptoAndKms.Modifies
    // Note: even if the method fails, the clients are ValidState
    ensures cryptoAndKms.ValidState()
    ensures
      // TODO-HV-2-GA: Update Specification for HV-2 Branch Key Creation
      && output.Success? ==>
        && var kms := cryptoAndKms.kms.kmsSimple.kmsClient;
        && |kms.History.Encrypt| == |old(kms.History.Encrypt)| + 1
        && kms.History.GenerateDataKey == old(kms.History.GenerateDataKey)
        && var kmsEvent :=  Seq.Last(kms.History.Encrypt);
        && kmsEvent.output.Success?
        && var kmsInput := kmsEvent.input;
        && Compatible?(cryptoAndKms.kmsConfig, kmsInput.KeyId)
        && |kmsInput.Plaintext| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int
        && kmsInput.EncryptionContext == Some(encryptionContext)
        && kmsInput.GrantTokens == Some(cryptoAndKms.kms.kmsSimple.grantTokens)
        && kmsEvent.output.value.CiphertextBlob.Some?
        && var digest := kmsInput.Plaintext[..Structure.BKC_DIGEST_LENGTH];
        && material == kmsInput.Plaintext[Structure.BKC_DIGEST_LENGTH..]
        && |cryptoAndKms.crypto.History.Digest| == |old(cryptoAndKms.crypto.History.Digest)| + 1
        && var digestEvent := Seq.Last(cryptoAndKms.crypto.History.Digest);
        && digestEvent.output.Success?
        && digestEvent.output.value == digest
        && digestEvent.input.digestAlgorithm == AtomicPrimitives.Types.SHA_384
  {
    var digest :- HvUtils.CreateBKCDigest(branchKeyContext, cryptoAndKms.crypto);
    var plaintextTuple := HvUtils.PackPlainTextTuple(digest, material);
    var wrappedMaterial? := EncryptKey(
      plaintextTuple,
      encryptionContext,
      branchKeyContext[Structure.KMS_FIELD],
      cryptoAndKms.kmsConfig,
      cryptoAndKms.kms.kmsSimple.grantTokens,
      cryptoAndKms.kms.kmsSimple.kmsClient
    );
    var wrappedMaterial :- wrappedMaterial?.MapFailure(e => ConvertKmsErrorToError(e));
    return Success(Structure.ConstructEncryptedHierarchicalKey(branchKeyContext, wrappedMaterial));
  }

  function ConvertKmsErrorToError(
    e: KmsError
  ): Types.Error
  {
    match e {
      // KMS errors ->
      case ComAmazonawsKms(comAmazonawsKms: KMS.Error) =>
        Types.ComAmazonawsKms(
          ComAmazonawsKms := comAmazonawsKms
        )
      case KeyManagementException(msg) =>
        Types.KeyManagementException(
          message := e.message
        )
      case BranchKeyCiphertextException(msg) =>
        Types.BranchKeyCiphertextException(
          message := e.message
        )
    }
  }

  function ExtractKmsOpaque(
    error: KmsError
  ): (opaqueError?: Option<KMS.OpaqueError>)
    ensures
      && error.ComAmazonawsKms?
      && error.ComAmazonawsKms.Opaque?
      ==> opaqueError?.Some? && opaqueError?.value == error.ComAmazonawsKms
  {
    match error {
      case Opaque(obj) => None
      case KeyManagementException(s) => None
      case BranchKeyCiphertextException(s) => None
      case ComAmazonawsKms(comAmazonawsKms: KMS.Error) =>
        match comAmazonawsKms {
          case Opaque(obj) => Some(comAmazonawsKms)
          case OpaqueWithText(obj, objMessage) => Some(comAmazonawsKms)
          case _ => None
        }
    }
  }

  function ExtractMessageFromKmsError(
    error: KmsError
  ): (errorMessage?: Option<string>)
  {
    match error {
      case Opaque(obj) => None
      case KeyManagementException(s) => Some(s)
      case BranchKeyCiphertextException(s) => Some(s)
      case ComAmazonawsKms(comAmazonawsKms: KMS.Error) =>
        match comAmazonawsKms {
          case Opaque(obj) => None
          case OpaqueWithText(obj, objMessage) => Some(objMessage)
          case _ => comAmazonawsKms.message
        }
    }
  }

}
