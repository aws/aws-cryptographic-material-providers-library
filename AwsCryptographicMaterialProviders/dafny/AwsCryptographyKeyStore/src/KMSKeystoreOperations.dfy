// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "Structure.dfy"
include "../../AwsCryptographicMaterialProviders/src/AwsArnParsing.dfy"
include "../../AwsCryptographicMaterialProviders/src/Keyrings/AwsKms/AwsKmsMrkMatchForDecrypt.dfy"
include "../../../dafny/AwsCryptographicMaterialProviders/src/AwsArnParsing.dfy"
include "KmsArn.dfy"
include "HierarchicalVersionUtils.dfy"
include "../../AwsCryptographicMaterialProviders/src/CanonicalEncryptionContext.dfy"

module {:options "/functionSyntax:4" } KMSKeystoreOperations {
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import Seq
  import Types = AwsCryptographyKeyStoreTypes
  import DDB = ComAmazonawsDynamodbTypes
  import KMS = ComAmazonawsKmsTypes
  import UTF8
  import Structure
  import opened AwsArnParsing
  import AwsKmsMrkMatchForDecrypt
  import KmsArn
  import AtomicPrimitives
  import HvUtils = HierarchicalVersionUtils
  import CanonicalEncryptionContext

  datatype CryptoAndKms = CryptoAndKms(
    kmsConfig: Types.KMSConfiguration,
    crypto: AtomicPrimitives.AtomicPrimitivesClient,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  ) {
    ghost predicate ValidState()
    {
      && HasKeyId(kmsConfig)
      && KmsArn.ValidKmsArn?(GetKeyId(kmsConfig))
      && crypto.ValidState() && kmsClient.ValidState()
    }
    ghost const Modifies := crypto.Modifies + kmsClient.Modifies
  }

  method {:vcs_split_on_every_assert} packAndCallKMS(
    nameonly branchKeyContext: map<string, string>,
    nameonly cryptoAndKms: CryptoAndKms,
    nameonly material: seq<uint8>,
    nameonly encryptionContext: map<string, string>
  )
    returns (output: Result<Structure.EncryptedHierarchicalKey, Types.Error>)
    requires
      && cryptoAndKms.ValidState()
      && Structure.BranchKeyContext?(branchKeyContext)
      && |material| == Structure.AES_256_LENGTH as int
      && AttemptKmsOperation?(cryptoAndKms.kmsConfig, branchKeyContext)
      && GetKeyId(cryptoAndKms.kmsConfig) == branchKeyContext[Structure.KMS_FIELD]
    // TODO-HV-2-M? : Support KmsDecryptEncrypt?
    modifies cryptoAndKms.Modifies
    // Note: even if the method fails, the clients are ValidState
    ensures cryptoAndKms.ValidState()
    ensures
      // TODO-HV-2-GA: Update Specification for HV-2 Branch Key Creation
      && output.Success? ==>
        && var crypto := cryptoAndKms.crypto;
        && |crypto.History.Digest| == |old(crypto.History.Digest)| + 1
        && old(crypto.History.Digest) < crypto.History.Digest
        && var digestEvent := Seq.Last(crypto.History.Digest);
        && HvUtils.EncodeEncryptionContext(branchKeyContext).Success?
        && var utf8BKContext := HvUtils.EncodeEncryptionContext(branchKeyContext).value;
        && CanonicalEncryptionContext.EncryptionContextToAAD(utf8BKContext).Success?
        && var canonicalEC := CanonicalEncryptionContext.EncryptionContextToAAD(utf8BKContext).value;
        && AtomicPrimitives.Types.DigestInput(
             digestAlgorithm := AtomicPrimitives.Types.SHA_384,
             message := canonicalEC
           ) == digestEvent.input
        && digestEvent.output.Success?
        && var digest := digestEvent.output.value;

        && var packedPlaintext := digest + material;
        && |packedPlaintext| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int

        && var kms := cryptoAndKms.kmsClient;
        && |kms.History.Encrypt| == |old(kms.History.Encrypt)| + 1
        && old(kms.History.Encrypt) < kms.History.Encrypt
        && kms.History.Encrypt == old(kms.History.Encrypt) + [Seq.Last(kms.History.Encrypt)]
        && Seq.Last(kms.History.Encrypt) == kms.History.Encrypt[|kms.History.Encrypt| -1]
        && kms.History.GenerateDataKey == old(kms.History.GenerateDataKey)
        && kms.History.Decrypt == old(kms.History.Decrypt)
        && var kmsEncryptEvent :=  Seq.Last(kms.History.Encrypt);
        && var kmsEncryptInput := kmsEncryptEvent.input;
        && Compatible?(cryptoAndKms.kmsConfig, kmsEncryptInput.KeyId)
        && var kmsKeyArn := GetKeyId(cryptoAndKms.kmsConfig);
        && KMS.EncryptRequest(
             KeyId := kmsKeyArn,
             Plaintext := packedPlaintext,
             EncryptionContext := Some(encryptionContext),
             GrantTokens := Some(cryptoAndKms.grantTokens)
           ) == kmsEncryptInput
        && kmsEncryptInput.Plaintext == digest + material
        && material == kmsEncryptInput.Plaintext[Structure.BKC_DIGEST_LENGTH..]
        && kmsEncryptEvent.output.Success?
        && kmsEncryptEvent.output.value.CiphertextBlob.Some?
        && kmsEncryptEvent.output.value.KeyId.Some?
        && kmsEncryptEvent.output.value.KeyId.value == kmsKeyArn // kmsKeyArn
        && KMS.IsValid_CiphertextType(kmsEncryptEvent.output.value.CiphertextBlob.value)
        && var wrappedMaterial := kmsEncryptEvent.output.value.CiphertextBlob.value;
        && Structure.ConstructEncryptedHierarchicalKey(branchKeyContext, wrappedMaterial) == output.value

    // ensures output.Success? ==>
    //           && var kmsKeyArn := GetKeyId(cryptoAndKms.kmsConfig);
    //           && Structure.BranchKeyContext?(output.value.EncryptionContext)
    //           && Structure.EncryptedHierarchicalKeyFromStorage?(output.value)
    //           && output.value.KmsArn == kmsKeyArn

  {
    var digest :- HvUtils.CreateBKCDigest(branchKeyContext, cryptoAndKms.crypto);
    var plaintextTuple := HvUtils.PackPlainTextTuple(digest, material);
    var wrappedMaterial :- EncryptKey(
      plaintextTuple,
      encryptionContext,
      branchKeyContext,
      cryptoAndKms.kmsConfig,
      cryptoAndKms.grantTokens,
      cryptoAndKms.kmsClient
    );
    return Success(Structure.ConstructEncryptedHierarchicalKey(branchKeyContext, wrappedMaterial));
  }

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

  predicate AttemptKmsOperation?(kmsConfiguration: Types.KMSConfiguration, encryptionContext: Structure.BranchKeyContext)
    ensures AttemptKmsOperation?(kmsConfiguration, encryptionContext) && HasKeyId(kmsConfiguration)
            ==> Compatible?(kmsConfiguration, encryptionContext[Structure.KMS_FIELD])
  {
    match kmsConfiguration
    case kmsKeyArn(arn) => (arn == encryptionContext[Structure.KMS_FIELD]) && KmsArn.ValidKmsArn?(arn)
    case kmsMRKeyArn(arn) => MrkMatch(arn, encryptionContext[Structure.KMS_FIELD]) && KmsArn.ValidKmsArn?(arn)
    case discovery(obj) => KmsArn.ValidKmsArn?(encryptionContext[Structure.KMS_FIELD])
    case mrDiscovery(obj) => KmsArn.ValidKmsArn?(encryptionContext[Structure.KMS_FIELD])
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

  method GenerateKey(
    encryptionContext: Structure.BranchKeyContext,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  )
    returns (res: Result<KMS.GenerateDataKeyWithoutPlaintextResponse, Types.Error>)
    requires kmsClient.ValidState()
    requires HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(GetKeyId(kmsConfiguration))
    requires AttemptKmsOperation?(kmsConfiguration, encryptionContext)
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
      Types.KeyStoreException(
        message := "Invalid response from KMS GenerateDataKey:: Invalid Key Id")
    );

    :- Need(
      && generateResponse.CiphertextBlob.Some?
      && KMS.IsValid_CiphertextType(generateResponse.CiphertextBlob.value),
      Types.KeyStoreException(
        message := "Invalid response from AWS KMS GenerateDataKey: Invalid ciphertext")
    );

    return Success(generateResponse);
  }

  method EncryptKey(
    plaintext: KMS.PlaintextType,
    encryptionContext: Structure.EncryptionContextString,
    branchKeyContext: Structure.EncryptionContextString,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  )
    returns (res: Result<KMS.CiphertextType, Types.Error>)
    requires kmsClient.ValidState()
    requires |plaintext| == 80 || |plaintext| == 32
    requires HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(GetKeyId(kmsConfiguration))
    requires Structure.BranchKeyContext?(branchKeyContext)
    requires AttemptKmsOperation?(kmsConfiguration, branchKeyContext)
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()
    ensures
      res.Success?
      ==>
        && |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 1
        && kmsClient.History.GenerateDataKey == old(kmsClient.History.GenerateDataKey)
        && kmsClient.History.Decrypt == old(kmsClient.History.Decrypt)
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
        && kmsClient.History.Encrypt == old(kmsClient.History.Encrypt) + [Seq.Last(kmsClient.History.Encrypt)]
        && Seq.Last(kmsClient.History.Encrypt) == kmsClient.History.Encrypt[|kmsClient.History.Encrypt| -1]
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
      Types.KeyStoreException(
        message := "Invalid response from AWS KMS Encrypt: KMS response's Ciphertext is invalid."
      )
    );
    :- Need(
      && encryptResponse.KeyId.Some?
      && encryptResponse.KeyId.value ==  kmsKeyArn,
      Types.KeyStoreException(
        message := "Invalid response from AWS KMS Encrypt: KMS Key ID of response did not match request."
      )
    );
    return Success(encryptResponse.CiphertextBlob.value);
  }

  method ReEncryptKey(
    ciphertext: seq<uint8>,
    sourceEncryptionContext: Structure.BranchKeyContext,
    destinationEncryptionContext: Structure.BranchKeyContext,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  )
    returns (res: Result<KMS.ReEncryptResponse, Types.Error>)
    requires KMS.IsValid_CiphertextType(ciphertext)
    requires
      // This is to validate the encryption context
      || (destinationEncryptionContext == sourceEncryptionContext)
      || (
           && Structure.BRANCH_KEY_TYPE_PREFIX < sourceEncryptionContext[Structure.TYPE_FIELD]
           && Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD !in sourceEncryptionContext
           && destinationEncryptionContext == Structure.ActiveBranchKeyEncryptionContext(sourceEncryptionContext)
         )
    requires AttemptKmsOperation?(kmsConfiguration, destinationEncryptionContext)
    requires HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(GetKeyId(kmsConfiguration))
    requires kmsClient.ValidState()
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()

    ensures
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

    ensures res.Success? ==>
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
      Types.KeyStoreException(
        message := "Invalid response from KMS ReEncrypt:: Invalid Key Id")
    );

    :- Need(
      && reEncryptResponse.CiphertextBlob.Some?
      && KMS.IsValid_CiphertextType(reEncryptResponse.CiphertextBlob.value),
      Types.KeyStoreException(
        message := "Invalid response from AWS KMS ReEncrypt: Invalid ciphertext.")
    );

    return Success(reEncryptResponse);
  }

  method GetPlaintextDataKeyViaGenerateDataKey(
    nameonly encryptionContext: map<string, string>,
    nameonly kmsConfiguration: Types.KMSConfiguration,
    nameonly grantTokens: KMS.GrantTokenList,
    nameonly kmsClient: KMS.IKMSClient
  )
    returns (output: Result<KMS.GenerateDataKeyResponse, Types.Error>)
    requires
      // TODO-HV2-DecryptEncrypt support Decrypt/Encrypt
      && kmsClient.ValidState()
      && HasKeyId(kmsConfiguration)
      && KmsArn.ValidKmsArn?(GetKeyId(kmsConfiguration))
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()
    ensures output.Success?
            ==>
              && var kms := kmsClient;
              && old(kms.History.Encrypt) == kms.History.Encrypt
              && old(kms.History.Decrypt) == kms.History.Decrypt
              && |kms.History.GenerateDataKey| == |old(kms.History.GenerateDataKey)| + 1
              && old(kms.History.GenerateDataKey) < kms.History.GenerateDataKey
              && var kmsGenerateDataKeyEvent := Seq.Last(kms.History.GenerateDataKey);
              && var kmsKeyArn := GetKeyId(kmsConfiguration);
              && KMS.GenerateDataKeyRequest(
                   KeyId := kmsKeyArn,
                   NumberOfBytes := Some(32),
                   EncryptionContext := Some(encryptionContext),
                   GrantTokens := Some(grantTokens)
                 ) == kmsGenerateDataKeyEvent.input
              && kmsGenerateDataKeyEvent.output.Success?
              && kmsGenerateDataKeyEvent.output.value.Plaintext.Some?
              && |kmsGenerateDataKeyEvent.output.value.Plaintext.value| == 32
              && kmsGenerateDataKeyEvent.output.value.KeyId.Some?
              && kmsGenerateDataKeyEvent.output.value.KeyId.value == kmsKeyArn
              && kmsGenerateDataKeyEvent.output.value == output.value
  {
    var kmsKeyArn := GetKeyId(kmsConfiguration);
    var generateDataKeyInput := KMS.GenerateDataKeyRequest(
      KeyId := kmsKeyArn,
      NumberOfBytes := Some(32),
      EncryptionContext := Some(encryptionContext),
      GrantTokens := Some(grantTokens)
    );

    var generateDataKeyResponse? := kmsClient.GenerateDataKey(
      generateDataKeyInput
    );

    var generateDataKeyResponse :- generateDataKeyResponse?
    .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));

    :- Need(
      && generateDataKeyResponse.Plaintext.Some?
      && |generateDataKeyResponse.Plaintext.value| == 32,
      Types.KeyStoreException(
        message := "Invalid response from AWS KMS GenerateDataKey: KMS response's Plaintext is invalid."
      )
    );
    :- Need(
      && generateDataKeyResponse.KeyId.Some?
      && generateDataKeyResponse.KeyId.value ==  kmsKeyArn,
      Types.KeyStoreException(
        message := "Invalid response from AWS KMS GenerateDataKey: KMS Key ID of response did not match request."
      )
    );

    output := Success(generateDataKeyResponse);
  }

  method DecryptKey(
    encryptionContext: Structure.BranchKeyContext,
    item: Structure.BranchKeyItem,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  )
    returns (output: Result<KMS.DecryptResponse, Types.Error>)
    requires KmsArn.ValidKmsArn?(encryptionContext[Structure.KMS_FIELD])
    requires item == Structure.ToAttributeMap(encryptionContext, item[Structure.BRANCH_KEY_FIELD].B)
    requires AttemptKmsOperation?(kmsConfiguration, encryptionContext)

    requires kmsClient.ValidState()
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()

    ensures
      && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1
      && var kmsKeyArn := GetArn(kmsConfiguration, encryptionContext[Structure.KMS_FIELD]);
      && KMS.DecryptRequest(
        CiphertextBlob := item[Structure.BRANCH_KEY_FIELD].B,
        EncryptionContext := Some(encryptionContext),
        GrantTokens := Some(grantTokens),
        KeyId := Some(kmsKeyArn),
        EncryptionAlgorithm := None
      )
         == Seq.Last(kmsClient.History.Decrypt).input
    ensures output.Success?
            ==>
              && Seq.Last(kmsClient.History.Decrypt).output.Success?
              && output.value == Seq.Last(kmsClient.History.Decrypt).output.value
              && output.value.Plaintext.Some?
              && 32 == |output.value.Plaintext.value|
  {
    var kmsKeyArn := GetArn(kmsConfiguration, encryptionContext[Structure.KMS_FIELD]);
    var maybeDecryptResponse := kmsClient.Decrypt(
      KMS.DecryptRequest(
        CiphertextBlob := item[Structure.BRANCH_KEY_FIELD].B,
        EncryptionContext := Some(encryptionContext),
        GrantTokens := Some(grantTokens),
        KeyId := Some(kmsKeyArn),
        EncryptionAlgorithm := None
      )
    );
    var decryptResponse :- maybeDecryptResponse.MapFailure(e => Types.ComAmazonawsKms(e));

    OptionalSequenceIsSafeBecauseItIsInMemory(decryptResponse.Plaintext);
    :- Need(
      && decryptResponse.Plaintext.Some?
      && 32 == |decryptResponse.Plaintext.value| as uint64,
      Types.KeyStoreException(
        message := "Invalid response from AWS KMS Decrypt: Key is not 32 bytes.")
    );

    output := Success(decryptResponse);

  }

}
