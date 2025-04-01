// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "../../../../AwsCryptographyPrimitives/Model/AwsCryptographyPrimitivesTypes.dfy"
include "../../AwsCryptographyKeyStore/src/Structure.dfy"
include "../../AwsCryptographyKeyStore/src/DefaultKeyStorageInterface.dfy"
include "../../AwsCryptographyKeyStore/src/KMSKeystoreOperations.dfy"
include "../../AwsCryptographyKeyStore/src/ErrorMessages.dfy"
include "../../AwsCryptographicMaterialProviders/src/AwsArnParsing.dfy"
include "../../AwsCryptographyKeyStore/src/KmsArn.dfy"
include "SystemKey/ContentHandler.dfy"

// TODO-HV-2-M1: WIP
module {:options "/functionSyntax:4" } CreateKeysHV2 {
  // TODO-HV-2-M1-FF: Group imports according to libraries
  import opened StandardLibrary
  import opened Wrappers
  import Structure
  import DefaultKeyStorageInterface
  import KMSKeystoreOperations
  import ErrorMessages = KeyStoreErrorMessages

  import opened Seq
  import opened UInt = StandardLibrary.UInt
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import Types = AwsCryptographyKeyStoreAdminTypes
  import DDB = ComAmazonawsDynamodbTypes
  import KMS = ComAmazonawsKmsTypes
  import AwsArnParsing
  import KmsArn
  import AtomicPrimitives
  import CanonicalEncryptionContext
  import Time
  import HvUtils = HierarchicalVersionUtils
  import CryptoTypes = AwsCryptographyPrimitivesTypes
  import ContentHandler = SystemKey.ContentHandler

  function ConvertKmsErrorToError(e: KMSKeystoreOperations.KmsError): Types.Error {
    match e {
      // Map KMS service errors
      case ComAmazonawsKms(kmsError) =>
        Types.ComAmazonawsKms(kmsError)

      // Map KeyManagementException
      case KeyManagementException(msg) =>
        Types.AwsCryptographyKeyStore(
          KeyStoreTypes.KeyManagementException(message := msg)
        )

      // Map BranchKeyCiphertextException
      case BranchKeyCiphertextException(msg) =>
        Types.AwsCryptographyKeyStore(
          KeyStoreTypes.BranchKeyCiphertextException(message := msg)
        )
    }
  }

  //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
  //= type=implication
  //# To create a branch key, this operation MUST take the following:
  //#
  //# - `branchKeyId`: The identifier
  //# - `encryptionContext`: Additional encryption context to bind to the created keys
  method CreateBranchAndBeaconKeys(
    branchKeyIdentifier: string,
    customEncryptionContext: map<string, string>,
    timestamp: string,
    branchKeyVersion: string,
    logicalKeyStoreName: string,
    kmsConfiguration: KeyStoreTypes.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    storage: KeyStoreTypes.IKeyStorageInterface,
    hierachyVersion: KeyStoreTypes.HierarchyVersion
  )
    returns (output: Result<Types.CreateKeyOutput, Types.Error>)
    requires 0 < |branchKeyIdentifier|
    requires 0 < |branchKeyVersion|
    requires forall k <- customEncryptionContext :: DDB.IsValid_AttributeName(Structure.ENCRYPTION_CONTEXT_PREFIX + k)
    requires storage.Modifies !! kmsClient.Modifies
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))

    requires hierachyVersion.v2?

    requires kmsClient.ValidState() && storage.ValidState()
    modifies storage.Modifies, kmsClient.Modifies
    ensures storage.ValidState() && kmsClient.ValidState()

    // TODO-HV-2-M1: Update Create Key
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=implication
    //# This operation MUST create a [branch key](structures.md#branch-key) and a [beacon key](structures.md#beacon-key) according to
    //# the [Branch Key and Beacon Key Creation](#branch-key-and-beacon-key-creation) section.
    ensures output.Success?
            ==>

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# The call to AWS KMS GenerateDataKeyWithoutPlaintext MUST use the configured AWS KMS client to make the call.
              // The second call is for the beacon key, the first call is the decrypt only. See Seq.Last(Seq.DropLast(
              && |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 3
              && old(kmsClient.History.Encrypt) < kmsClient.History.Encrypt

              // TODO-HV-2-M1-FF: Refactor EncryptionContext usage into BranchKeyContext
              && var decryptOnlyEncryptionContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
                                                       branchKeyIdentifier,
                                                       branchKeyVersion,
                                                       timestamp,
                                                       logicalKeyStoreName,
                                                       KMSKeystoreOperations.GetKeyId(kmsConfiguration),
                                                       hierachyVersion,
                                                       customEncryptionContext
                                                     );

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#logical-keystore-name
              //= type=implication
              //# The logical keystore name MUST be bound to every created key.
              && decryptOnlyEncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName

              // TODO-HV-2-M1: Refactor EncryptionContext usage into BranchKeyContext
              //= aws-encryption-sdk-specification/framework/branch-key-store.md#encryption-context
              //= type=implication
              //# Any additionally attributes in the EncryptionContext
              //# of the [encrypted hierarchical key](./key-store/key-storage.md#encryptedhierarchicalkey)
              //# MUST be added to the encryption context.
              && (forall k <- customEncryptionContext
                    ::
                      && Structure.ENCRYPTION_CONTEXT_PREFIX + k in decryptOnlyEncryptionContext
                      && decryptOnlyEncryptionContext[Structure.ENCRYPTION_CONTEXT_PREFIX + k] == customEncryptionContext[k])

              // //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              // //= type=implication
              // //# The wrapped Branch Keys, DECRYPT_ONLY and ACTIVE, MUST be created according to [Wrapped Branch Key Creation](#wrapped-branch-key-creation).
              // && WrappedBranchKeyCreation?(
              //      Seq.Last(kmsClient.History.Encrypt),
              //      kmsClient,
              //      kmsConfiguration,
              //      grantTokens,
              //      decryptOnlyEncryptionContext
              //    )

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# The operation MUST call [AWS KMS API GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html).
              && var beaconKmsRequest := Seq.Last(kmsClient.History.Encrypt);

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# The operation MUST call AWS KMS GenerateDataKeyWithoutPlaintext with a request constructed as follows:
              && var beaconKmsInput := beaconKmsRequest.input;

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# - `KeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
              && KMSKeystoreOperations.Compatible?(kmsConfiguration, beaconKmsInput.KeyId)

              // // TODO-HV-2-GA: Specification
              // // Plaintext bytes -> MDDigest(48) + Plaintext(32)
              // && beaconKmsInput.NumberOfBytes == Some(80)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# - `EncryptionContext` MUST be the [encryption context for beacon keys](#beacon-key-encryption-context).
              && beaconKmsInput.EncryptionContext == Some(HvUtils.SelectKmsEncryptionContextForHv2(Structure.BeaconKeyEncryptionContext(decryptOnlyEncryptionContext)))

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# - `GrantTokens` MUST be this keystore's [grant tokens](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
              && beaconKmsInput.GrantTokens == Some(grantTokens)

              // TODO-HV-2-GA: Make sure the return types
              && beaconKmsRequest.output.Success?
              && beaconKmsRequest.output.value.CiphertextBlob.Some?

              && |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1

              // && Seq.Last(storage.History.WriteNewEncryptedBranchKey).input.Active
              //    == Structure.ConstructEncryptedHierarchicalKey(
              //         Seq.Last(kmsClient.History.ReEncrypt).input.DestinationEncryptionContext.value,
              //         //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
              //         //= type=implication
              //         //# If the call to AWS KMS ReEncrypt succeeds,
              //         //# the operation MUST use the ReEncrypt result `CiphertextBlob`
              //         //# as the wrapped ACTIVE Branch Key.
              //         Seq.Last(kmsClient.History.ReEncrypt).output.value.CiphertextBlob.value
              //       )

              // && Seq.Last(storage.History.WriteNewEncryptedBranchKey).input.Version
              //    == Structure.ConstructEncryptedHierarchicalKey(
              //         Seq.Last(Seq.DropLast(kmsClient.History.GenerateDataKeyWithoutPlaintext)).input.EncryptionContext.value,
              //         //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
              //         //= type=implication
              //         //# If the call to AWS KMS GenerateDataKeyWithoutPlaintext succeeds,
              //         //# the operation MUST use the GenerateDataKeyWithoutPlaintext result `CiphertextBlob`
              //         //# as the wrapped DECRYPT_ONLY Branch Key.
              //         Seq.Last(Seq.DropLast(kmsClient.History.GenerateDataKeyWithoutPlaintext)).output.value.CiphertextBlob.value
              //       )

              // && Seq.Last(storage.History.WriteNewEncryptedBranchKey).input.Beacon
              //    == Structure.ConstructEncryptedHierarchicalKey(
              //         Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).input.EncryptionContext.value,
              //         //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //         //= type=implication
              //         //# If the call to AWS KMS GenerateDataKeyWithoutPlaintext succeeds,
              //         //# the operation MUST use the `CiphertextBlob` as the wrapped Beacon Key.
              //         Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.value.CiphertextBlob.value
              //       )

              && Seq.Last(storage.History.WriteNewEncryptedBranchKey).output.Success?

    // //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    // //= type=implication
    // //# If creation of the keys are successful,
    // //# then the key store MUST call the configured [KeyStorage interface's](./key-store/key-storage.md#interface)
    // //# [WriteNewEncryptedBranchKey](./key-store/key-storage.md#writenewencryptedbranchkey) with these 3 [EncryptedHierarchicalKeys](./key-store/key-storage.md#encryptedhierarchicalkey).
    // ensures
    //   && output.Success?
    //   && |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 2
    //   && |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 1
    //   && Seq.Last(Seq.DropLast(kmsClient.History.GenerateDataKeyWithoutPlaintext)).output.Success?
    //   && Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.Success?
    //   && Seq.Last(kmsClient.History.ReEncrypt).output.Success?
    //   ==>
    //     && |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=implication
    //# If writing to the keystore succeeds,
    //# the operation MUST return the branch-key-id that maps to both
    //# the branch key and the beacon key.
    ensures
      && |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1
      && Seq.Last(storage.History.WriteNewEncryptedBranchKey).output.Success?
      ==>
        && output.Success?
        && output.value.Identifier == branchKeyIdentifier


    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=implication
    //# Otherwise, this operation MUST yield an error.
    ensures

      || (&& |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 1
          && Seq.Last(kmsClient.History.Encrypt).output.Failure?
          ==> output.Failure?)

      || (&& |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 2
          && Seq.Last(Seq.DropLast(kmsClient.History.Encrypt)).output.Failure?
          ==> output.Failure?)

      || (&& |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 3
          && Seq.Last(Seq.DropLast(Seq.DropLast(kmsClient.History.Encrypt))).output.Failure?
          ==> output.Failure?)

      || (&& |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1
          && Seq.Last(storage.History.WriteNewEncryptedBranchKey).output.Failure?
          ==> output.Failure?)

  {
    // Construct Branch Key Contexts for ACTIVE, Version and Beacon items.
    var decryptOnlyBranchKeyContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
      branchKeyIdentifier,
      branchKeyVersion,
      timestamp,
      logicalKeyStoreName,
      KMSKeystoreOperations.GetKeyId(kmsConfiguration),
      hierachyVersion,
      customEncryptionContext
    );
    var activeBranchKeyContext := Structure.ActiveBranchKeyEncryptionContext(decryptOnlyBranchKeyContext);
    var beaconBranchKeyContext := Structure.BeaconKeyEncryptionContext(decryptOnlyBranchKeyContext);

    // Get crypto client
    var crypto? := HvUtils.ProvideCryptoClient();
    var crypto :- crypto?.MapFailure(
      e => Types.AwsCryptographyPrimitives(e)
    );

    // Create SHA-384 digests
    var decryptOnlyDigest :- HvUtils.CreateBKCDigest(decryptOnlyBranchKeyContext, crypto);
    var activeDigest :- HvUtils.CreateBKCDigest(activeBranchKeyContext, crypto);
    var beaconDigest :- HvUtils.CreateBKCDigest(beaconBranchKeyContext, crypto);

    // if (decryptOnlyDigest.Failure? || activeDigest.Failure? || beaconDigest.Failure?)

    // Generate AES Keys.
    // TODO-HV-2-M1: Map Failure -> AtomicPrimitives.Types.Error
    var activePlaintextMaterial? :- crypto.GenerateRandomBytes(
      CryptoTypes.GenerateRandomBytesInput(length := 32)
    );

    var beaconPlaintextMaterial? :- crypto.GenerateRandomBytes(
      CryptoTypes.GenerateRandomBytesInput(length := 32)
    );

    var activePlaintextTuple := HvUtils.PackPlainTextTuple(activeDigest, activePlaintextMaterial?);
    var decryptOnlyPlaintextTuple := HvUtils.PackPlainTextTuple(decryptOnlyDigest, activePlaintextMaterial?);
    var beaconPlaintextTuple := HvUtils.PackPlainTextTuple(beaconDigest, beaconPlaintextMaterial?);

    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, decryptOnlyBranchKeyContext[Structure.KMS_FIELD]);
    var wrappedDecryptOnlyBranchKey :- KMSKeystoreOperations.EncryptKey(
      decryptOnlyPlaintextTuple,
      customEncryptionContext,
      decryptOnlyBranchKeyContext[Structure.KMS_FIELD],
      kmsConfiguration,
      grantTokens,
      kmsClient
    );
    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, activeBranchKeyContext[Structure.KMS_FIELD]);
    var wrappedActiveBranchKey :- KMSKeystoreOperations.EncryptKey(
      activePlaintextTuple,
      customEncryptionContext,
      activeBranchKeyContext[Structure.KMS_FIELD],
      kmsConfiguration,
      grantTokens,
      kmsClient
    );
    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, beaconBranchKeyContext[Structure.KMS_FIELD]);
    var wrappedBeaconKey :- KMSKeystoreOperations.EncryptKey(
      beaconPlaintextTuple,
      customEncryptionContext,
      beaconBranchKeyContext[Structure.KMS_FIELD],
      kmsConfiguration,
      grantTokens,
      kmsClient
    );

    var _ :- storage.WriteNewEncryptedBranchKey(
      KeyStoreTypes.WriteNewEncryptedBranchKeyInput(
        Active := Structure.ConstructEncryptedHierarchicalKey(
          activeBranchKeyContext,
          wrappedActiveBranchKey
        ),
        Version := Structure.ConstructEncryptedHierarchicalKey(
          decryptOnlyBranchKeyContext,
          wrappedDecryptOnlyBranchKey
        ),
        Beacon := Structure.ConstructEncryptedHierarchicalKey(
          beaconBranchKeyContext,
          wrappedBeaconKey
        )
      )
    );

    output := Success(
      Types.CreateKeyOutput(
        Identifier := branchKeyIdentifier,
        HierarchyVersion := hierachyVersion
      ));
  }
}
