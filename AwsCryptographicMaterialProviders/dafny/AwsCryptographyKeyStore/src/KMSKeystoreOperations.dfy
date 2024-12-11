// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "Structure.dfy"
include "../../AwsCryptographicMaterialProviders/src/AwsArnParsing.dfy"
include "../../AwsCryptographicMaterialProviders/src/Keyrings/AwsKms/AwsKmsMrkMatchForDecrypt.dfy"
include "../../../dafny/AwsCryptographicMaterialProviders/src/AwsArnParsing.dfy"
include "KmsArn.dfy"

module {:options "/functionSyntax:4" } KMSKeystoreOperations {
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import Seq
  import Types = AwsCryptographyKeyStoreTypes
  import DDB = ComAmazonawsDynamodbTypes
  import KMS = ComAmazonawsKmsTypes
  import UTF8
  import Structure
  import opened AwsArnParsing
  import AwsKmsMrkMatchForDecrypt
  import KmsArn
  import ErrorMessages = KeyStoreErrorMessages

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

  method ReEncryptKey(
    ciphertext: seq<uint8>,
    sourceEncryptionContext: Structure.BranchKeyContext,
    destinationEncryptionContext: Structure.BranchKeyContext,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  )
    returns (res: Result<KMS.ReEncryptResponse, Types.Error>)
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
      Types.KeyStoreException(
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

  method DecryptKey(
    encryptedKey: Types.EncryptedHierarchicalKey,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  )
    returns (output: Result<KMS.DecryptResponse, Types.Error>)
    requires Structure.EncryptedHierarchicalKey?(encryptedKey)

    requires kmsClient.ValidState()
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()

    ensures !KmsArn.ValidKmsArn?(encryptedKey.KmsArn) ==> output.Failure?
    ensures !AttemptKmsOperation?(kmsConfiguration, encryptedKey.EncryptionContext) ==> output.Failure?

    ensures output.Success?
            ==>
              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1
              && AwsKmsBranchKeyDecryption?(
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
  {
    :- Need(
      && KmsArn.ValidKmsArn?(encryptedKey.KmsArn)
         // This check is overloaded.
         // It is incredibly unlikely that the the stored ciphertext
         // has dropped to 0 or exceeds the KMS limit.
         // So the error message is left unchanged.
      && KMS.IsValid_CiphertextType(encryptedKey.CiphertextBlob),
      Types.KeyStoreException( message := ErrorMessages.RETRIEVED_KEYSTORE_ITEM_INVALID_KMS_ARN)
    );

    :- Need(
      AttemptKmsOperation?(kmsConfiguration, encryptedKey.EncryptionContext),
      Types.KeyStoreException( message := ErrorMessages.GET_KEY_ARN_DISAGREEMENT)
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
      && 32 == |decryptResponse.Plaintext.value|,
      Types.KeyStoreException(
        message := "Invalid response from AWS KMS Decrypt: Key is not 32 bytes.")
    );

    output := Success(decryptResponse);

  }


  ghost predicate AwsKmsBranchKeyDecryption?(
    versionItem: Types.EncryptedHierarchicalKey,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    decryptHistory: KMS.DafnyCallEvent<KMS.DecryptRequest, Result<KMS.DecryptResponse, KMS.Error>>
  )
    reads kmsClient.History

    requires Structure.EncryptedHierarchicalKey?(versionItem)

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

}
