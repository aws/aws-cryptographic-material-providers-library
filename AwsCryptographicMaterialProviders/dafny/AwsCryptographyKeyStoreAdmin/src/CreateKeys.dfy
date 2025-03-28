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
  import MutateViaDecryptEncrypt
  import HierarchicalVersionUtils
  import CryptoTypes = AwsCryptographyPrimitivesTypes
  import ContentHandler = SystemKey.ContentHandler

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
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    storage: Types.IKeyStorageInterface
  )
    returns (output: Result<Types.CreateKeyOutput, Types.Error>)
    requires 0 < |branchKeyIdentifier|
    requires 0 < |branchKeyVersion|
    requires forall k <- customEncryptionContext :: DDB.IsValid_AttributeName(Structure.ENCRYPTION_CONTEXT_PREFIX + k)
    requires storage.Modifies !! kmsClient.Modifies
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))

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


    // //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    // //= type=implication
    // //# The operation MUST call [AWS KMS API GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html).
    // && var beaconKmsRequest := Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext);

    //           //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //           //= type=implication
    //           //# The operation MUST call AWS KMS GenerateDataKeyWithoutPlaintext with a request constructed as follows:
    //           && var beaconKmsInput := beaconKmsRequest.input;

    //           //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //           //= type=implication
    //           //# - `KeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
    //           && KMSKeystoreOperations.Compatible?(kmsConfiguration, beaconKmsInput.KeyId)

    //           //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //           //= type=implication
    //           //# - `NumberOfBytes` MUST be 32.
    //           && beaconKmsInput.NumberOfBytes == Some(32)

    //           //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //           //= type=implication
    //           //# - `EncryptionContext` MUST be the [encryption context for beacon keys](#beacon-key-encryption-context).
    //           && beaconKmsInput.EncryptionContext == Some(Structure.BeaconKeyEncryptionContext(decryptOnlyEncryptionContext))

    //           //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //           //= type=implication
    //           //# - `GrantTokens` MUST be this keystore's [grant tokens](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
    //           && beaconKmsInput.GrantTokens == Some(grantTokens)

    //           && beaconKmsRequest.output.Success?
    //           && beaconKmsRequest.output.value.CiphertextBlob.Some?

    //           && |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1

    //           && Seq.Last(storage.History.WriteNewEncryptedBranchKey).input.Active
    //              == Structure.ConstructEncryptedHierarchicalKey(
    //                   Seq.Last(kmsClient.History.ReEncrypt).input.DestinationEncryptionContext.value,
    //                   //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //                   //= type=implication
    //                   //# If the call to AWS KMS ReEncrypt succeeds,
    //                   //# the operation MUST use the ReEncrypt result `CiphertextBlob`
    //                   //# as the wrapped ACTIVE Branch Key.
    //                   Seq.Last(kmsClient.History.ReEncrypt).output.value.CiphertextBlob.value
    //                 )

    //           && Seq.Last(storage.History.WriteNewEncryptedBranchKey).input.Version
    //              == Structure.ConstructEncryptedHierarchicalKey(
    //                   Seq.Last(Seq.DropLast(kmsClient.History.GenerateDataKeyWithoutPlaintext)).input.EncryptionContext.value,
    //                   //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //                   //= type=implication
    //                   //# If the call to AWS KMS GenerateDataKeyWithoutPlaintext succeeds,
    //                   //# the operation MUST use the GenerateDataKeyWithoutPlaintext result `CiphertextBlob`
    //                   //# as the wrapped DECRYPT_ONLY Branch Key.
    //                   Seq.Last(Seq.DropLast(kmsClient.History.GenerateDataKeyWithoutPlaintext)).output.value.CiphertextBlob.value
    //                 )

    //           && Seq.Last(storage.History.WriteNewEncryptedBranchKey).input.Beacon
    //              == Structure.ConstructEncryptedHierarchicalKey(
    //                   Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).input.EncryptionContext.value,
    //                   //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //                   //= type=implication
    //                   //# If the call to AWS KMS GenerateDataKeyWithoutPlaintext succeeds,
    //                   //# the operation MUST use the `CiphertextBlob` as the wrapped Beacon Key.
    //                   Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.value.CiphertextBlob.value
    //                 )

    //           && Seq.Last(storage.History.WriteNewEncryptedBranchKey).output.Success?

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

    // //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    // //= type=implication
    // //# If writing to the keystore succeeds,
    // //# the operation MUST return the branch-key-id that maps to both
    // //# the branch key and the beacon key.
    // ensures
    //   && |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1
    //   && Seq.Last(storage.History.WriteNewEncryptedBranchKey).output.Success?
    //   ==>
    //     && output.Success?
    //     && output.value.branchKeyIdentifier == branchKeyIdentifier


    // //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    // //= type=implication
    // //# Otherwise, this operation MUST yield an error.
    // ensures

    //   || (&& |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 1
    //       && Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.Failure?
    //       ==> output.Failure?)

    //   || (&& |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 1
    //       && Seq.Last(kmsClient.History.ReEncrypt).output.Failure?
    //       ==> output.Failure?)

    //   || (&& |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 2
    //       && Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.Failure?
    //       ==> output.Failure?)

    //   || (&& |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1
    //       && Seq.Last(storage.History.WriteNewEncryptedBranchKey).output.Failure?
    //       ==> output.Failure?)

  {

    var decryptOnlyEncryptionContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
      branchKeyIdentifier,
      branchKeyVersion,
      timestamp,
      logicalKeyStoreName,
      KMSKeystoreOperations.GetKeyId(kmsConfiguration),
      customEncryptionContext
    );
    var activeEncryptionContext := Structure.ActiveBranchKeyEncryptionContext(decryptOnlyEncryptionContext);
    var beaconEncryptionContext := Structure.BeaconKeyEncryptionContext(decryptOnlyEncryptionContext);

    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, decryptOnlyEncryptionContext[Structure.KMS_FIELD]);
    var wrappedDecryptOnlyBranchKey :- KMSKeystoreOperations.GenerateKey(
      decryptOnlyEncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );
    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, activeEncryptionContext[Structure.KMS_FIELD]);
    var wrappedActiveBranchKey :- KMSKeystoreOperations.ReEncryptKey(
      wrappedDecryptOnlyBranchKey.CiphertextBlob.value,
      decryptOnlyEncryptionContext,
      activeEncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );
    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, beaconEncryptionContext[Structure.KMS_FIELD]);
    var wrappedBeaconKey :- KMSKeystoreOperations.GenerateKey(
      beaconEncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );

    var _ :- storage.WriteNewEncryptedBranchKey(
      Types.WriteNewEncryptedBranchKeyInput(
        Active := Structure.ConstructEncryptedHierarchicalKey(
          activeEncryptionContext,
          wrappedActiveBranchKey.CiphertextBlob.value
        ),
        Version := Structure.ConstructEncryptedHierarchicalKey(
          decryptOnlyEncryptionContext,
          wrappedDecryptOnlyBranchKey.CiphertextBlob.value
        ),
        Beacon := Structure.ConstructEncryptedHierarchicalKey(
          beaconEncryptionContext,
          wrappedBeaconKey.CiphertextBlob.value
        )
      )
    );

    output := Success(
      Types.CreateKeyOutput(
        branchKeyIdentifier := branchKeyIdentifier
      ));
  }

  method VersionActiveBranchKey(
    input: Types.VersionKeyInput,
    timestamp: string,
    branchKeyVersion: string,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    storage: Types.IKeyStorageInterface
  )
    returns (output: Result<Types.VersionKeyOutput, Types.Error>)
    requires 0 < |input.branchKeyIdentifier| && 0 < |branchKeyVersion|
    requires storage.Modifies !! kmsClient.Modifies
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
    requires storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
             ==>
               logicalKeyStoreName == (storage as DefaultKeyStorageInterface.DynamoDBKeyStorageInterface).logicalKeyStoreName

    requires kmsClient.ValidState() && storage.ValidState()
    modifies storage.Modifies, kmsClient.Modifies
    ensures storage.ValidState() && kmsClient.ValidState()

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
    //= type=implication
    //# VersionKey MUST first get the active version for the branch key from the keystore
    //# by calling the configured [KeyStorage interface's](./key-store/key-storage.md#interface)
    //# [GetEncryptedActiveBranchKey](./key-store/key-storage.md#getencryptedactivebranchkey)
    //# using the `branch-key-id`.
    ensures
      && |storage.History.GetEncryptedActiveBranchKey| == |old(storage.History.GetEncryptedActiveBranchKey)| + 1
      && Seq.Last(storage.History.GetEncryptedActiveBranchKey).input.Identifier == input.branchKeyIdentifier

    ensures output.Success?
            ==>
              && Seq.Last(storage.History.GetEncryptedActiveBranchKey).output.Success?
              && var oldActiveItem := Seq.Last(storage.History.GetEncryptedActiveBranchKey).output.value.Item;


              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# VersionKey MUST verify that the returned EncryptedHierarchicalKey MUST have the requested `branch-key-id`.
              && oldActiveItem.Identifier == input.branchKeyIdentifier

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# VersionKey MUST verify that the returned EncryptedHierarchicalKey is an ActiveHierarchicalSymmetricVersion.
              && Structure.ActiveHierarchicalSymmetricKey?(oldActiveItem)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# VersionKey MUST verify that the returned EncryptedHierarchicalKey MUST have a logical table name equal to the configured logical table name.
              && oldActiveItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# The `KmsArn` of the [EncryptedHierarchicalKey](./key-store/key-storage.md#encryptedhierarchicalkey)
              //# MUST be [compatible with](#aws-key-arn-compatibility)
              //# the configured `KMS ARN` in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, oldActiveItem.EncryptionContext[Structure.KMS_FIELD])
              && KMSKeystoreOperations.Compatible?(kmsConfiguration, oldActiveItem.KmsArn)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# The [EncryptedHierarchicalKey](./key-store/key-storage.md#encryptedhierarchicalkey)
              //# MUST be authenticated according to [authenticating a keystore item](#authenticating-an-encryptedhierarchicalkey).

              // TODO-HV-2-M1: Verify CreateKeyOutput?
              // //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              // //= type=implication
              // //# The operation MUST use the configured `KMS SDK Client` to authenticate the value of the keystore item.
              // && |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 3

              // //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              // //= type=implication
              // //# The operation MUST call [AWS KMS API ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html)
              // //# with a request constructed as follows:
              // && var reEncryptInput := Seq.Last(Seq.DropLast(kmsClient.History.ReEncrypt)).input;

              // //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              // //= type=implication
              // //# - `SourceEncryptionContext` MUST be the [encryption context](#encryption-context) of the EncryptedHierarchicalKey to be authenticated
              // && reEncryptInput.SourceEncryptionContext == Some(oldActiveItem.EncryptionContext)

              // //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              // //= type=implication
              // //# - `SourceKeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
              // && KMSKeystoreOperations.OptCompatible?(kmsConfiguration, reEncryptInput.SourceKeyId)

              // //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              // //= type=implication
              // //# - `CiphertextBlob` MUST be the `CiphertextBlob` attribute value on the EncryptedHierarchicalKey to be authenticated
              // && reEncryptInput.CiphertextBlob == oldActiveItem.CiphertextBlob

              // //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              // //= type=implication
              // //# - `GrantTokens` MUST be the configured [grant tokens](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
              // && reEncryptInput.GrantTokens == Some(grantTokens)

              // //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              // //= type=implication
              // //# - `DestinationKeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
              // && KMSKeystoreOperations.Compatible?(kmsConfiguration, reEncryptInput.DestinationKeyId)

              // //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              // //= type=implication
              // //# - `DestinationEncryptionContext` MUST be the [encryption context](#encryption-context) of the EncryptedHierarchicalKey to be authenticated
              // && reEncryptInput.DestinationEncryptionContext == Some(oldActiveItem.EncryptionContext)

              // && |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 1
              // && old(kmsClient.History.GenerateDataKeyWithoutPlaintext) < kmsClient.History.GenerateDataKeyWithoutPlaintext
              // && old(kmsClient.History.ReEncrypt) < kmsClient.History.ReEncrypt

              // && var decryptOnlyEncryptionContext := Structure.NewVersionFromActiveBranchKeyEncryptionContext(
              //                                          oldActiveItem.EncryptionContext,
              //                                          branchKeyVersion,
              //                                          timestamp
              //                                        );

              // TODO-HV-2-M1-FF: Add Predicate?
              // //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              // //= type=implication
              // //# The wrapped Branch Keys, DECRYPT_ONLY and ACTIVE, MUST be created according to [Wrapped Branch Key Creation](#wrapped-branch-key-creation).
              // && WrappedBranchKeyCreation?(
              //      Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext),
              //      Seq.Last(kmsClient.History.ReEncrypt),
              //      kmsClient,
              //      kmsConfiguration,
              //      grantTokens,
              //      decryptOnlyEncryptionContext
              //    )

              && |storage.History.WriteNewEncryptedBranchKeyVersion| == |old(storage.History.WriteNewEncryptedBranchKeyVersion)| + 1

              // TODO-HV-2-M1: Verify Storage Calls
              // //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              // //= type=implication
              // //# If creation of the keys are successful,
              // //# then the key store MUST call the configured [KeyStorage interface's](./key-store/key-storage.md#interface)
              // //# [WriteNewEncryptedBranchKeyVersion](./key-store/key-storage.md##writenewencryptedbranchkeyversion)
              // //# with these 2 [EncryptedHierarchicalKeys](./key-store/key-storage.md##encryptedhierarchicalkey).
              // && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).input.Active.Item
              //    == Structure.ConstructEncryptedHierarchicalKey(
              //         Seq.Last(kmsClient.History.ReEncrypt).input.DestinationEncryptionContext.value,
              //         Seq.Last(kmsClient.History.ReEncrypt).output.value.CiphertextBlob.value
              //       )

              // && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).input.Version
              //    == Structure.ConstructEncryptedHierarchicalKey(
              //         Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).input.EncryptionContext.value,
              //         Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.value.CiphertextBlob.value
              //       )

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# The `kms-arn` stored in the table MUST NOT change as a result of this operation,
              //# even if the KeyStore is configured with a `KMS MRKey ARN` that does not exactly match the stored ARN.
              && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).input.Active.Item.KmsArn == oldActiveItem.KmsArn
              && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).input.Version.KmsArn == oldActiveItem.KmsArn

              && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).output.Success?


              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# If the [WriteNewEncryptedBranchKeyVersion](./key-store/key-storage.md#writenewencryptedbranchkeyversion) is successful,
              //# this operation MUST return a successful response containing no additional data.
              && output == Success(Types.VersionKeyOutput)

    // TODO-HV-2-M1: Ensure Verification according to Encrypt/Decrypt Strategy
    ensures
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
      //= type=implication
      //# If the item fails to authenticate this operation MUST fail.
      || (&& |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 1
          && Seq.Last(kmsClient.History.Encrypt).output.Failure?
          ==> output.Failure?)

      || (&& |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 2
          && Seq.Last(Seq.DropLast(kmsClient.History.Encrypt)).output.Failure?
          ==> output.Failure?)

      || (&& |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 3
          && Seq.Last(Seq.DropLast(Seq.DropLast(kmsClient.History.Encrypt))).output.Failure?
          ==> output.Failure?)

      || (&& |storage.History.GetEncryptedActiveBranchKey| == |old(storage.History.GetEncryptedActiveBranchKey)| + 1
          && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).output.Failure?
          ==> output.Failure?)

      || (&& |storage.History.WriteNewEncryptedBranchKeyVersion| == |old(storage.History.WriteNewEncryptedBranchKeyVersion)| + 1
          && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).output.Failure?
          ==> output.Failure?)

  {

    var GetEncryptedActiveBranchKeyOutput :- storage.GetEncryptedActiveBranchKey(
      Types.GetEncryptedActiveBranchKeyInput(
        Identifier := input.branchKeyIdentifier
      )
    );
    var oldActiveItem := GetEncryptedActiveBranchKeyOutput.Item;

    :- Need(
      || storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
      || (
           && oldActiveItem.Identifier == input.branchKeyIdentifier
           && Structure.ActiveHierarchicalSymmetricKey?(oldActiveItem)
           && oldActiveItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
         ),
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_ACTIVE_BRANCH_KEY_FROM_STORAGE)
    );
    // TODO-HV-2-M3: Support Version in HV-2
    :- Need(
      oldActiveItem.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_1,
      Types.KeyStoreException(
        message := "At this time, VersionKey ONLY supports HV-1; BK's Active Item is HV-2.")
    );
    :- Need(
      && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, oldActiveItem.EncryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException(
        message := ErrorMessages.VERSION_KEY_KMS_KEY_ARN_DISAGREEMENT)
    );

    var _ :- KMSKeystoreOperations.ReEncryptKey(
      oldActiveItem.CiphertextBlob,
      oldActiveItem.EncryptionContext,
      oldActiveItem.EncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );

    var decryptOnlyEncryptionContext := Structure.NewVersionFromActiveBranchKeyEncryptionContext(
      oldActiveItem.EncryptionContext,
      branchKeyVersion,
      timestamp
    );

    var activeEncryptionContext := Structure.ActiveBranchKeyEncryptionContext(decryptOnlyEncryptionContext);

    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, decryptOnlyEncryptionContext[Structure.KMS_FIELD]);

    var wrappedDecryptOnlyBranchKey :- KMSKeystoreOperations.GenerateKey(
      decryptOnlyEncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );
    var wrappedActiveBranchKey :- KMSKeystoreOperations.ReEncryptKey(
      wrappedDecryptOnlyBranchKey.CiphertextBlob.value,
      decryptOnlyEncryptionContext,
      activeEncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );

    var active := Structure.ConstructEncryptedHierarchicalKey(
      activeEncryptionContext,
      wrappedActiveBranchKey.CiphertextBlob.value
    );
    var overWrite := Types.OverWriteEncryptedHierarchicalKey(
      Item := active,
      Old := oldActiveItem
    );

    var _ :- storage.WriteNewEncryptedBranchKeyVersion(
      Types.WriteNewEncryptedBranchKeyVersionInput(
        Active := overWrite,
        Version :=  Structure.ConstructEncryptedHierarchicalKey(
          decryptOnlyEncryptionContext,
          wrappedDecryptOnlyBranchKey.CiphertextBlob.value
        )
      )
    );

    output := Success(Types.VersionKeyOutput());
  }


  twostate predicate WrappedBranchKeyCreation?(
    new decryptOnlyEncryptHistory: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    new activeEncryptHistory: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    kmsClient: KMS.IKMSClient,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    decryptOnlyEncryptionContext: map<string, string>
  )
    reads kmsClient.History
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))


    // The history elements are "the things I added"
    requires old(kmsClient.History.GenerateDataKeyWithoutPlaintext) < kmsClient.History.GenerateDataKeyWithoutPlaintext
    requires old(kmsClient.History.Encrypt) < kmsClient.History.Encrypt

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# The call to AWS KMS Encrypt MUST use the configured AWS KMS client to make the call.
    requires
      && encryptHistory in kmsClient.History.Encrypt[|old(kmsClient.History.Encrypt)|..]
  {

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# The operation MUST call AWS KMS GenerateDataKeyWithoutPlaintext with a request constructed as follows:
    && var decryptOnlyKmsInput := generateHistory.input;

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `KeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
    && KMSKeystoreOperations.Compatible?(kmsConfiguration, decryptOnlyKmsInput.KeyId)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `NumberOfBytes` MUST be 32.
    && decryptOnlyKmsInput.NumberOfBytes == Some(32)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `EncryptionContext` MUST be the [DECRYPT_ONLY encryption context for branch keys](#decrypt_only-encryption-context).
    && Structure.BranchKeyContext?(decryptOnlyEncryptionContext)
    && decryptOnlyKmsInput.EncryptionContext == Some(decryptOnlyEncryptionContext)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - GenerateDataKeyWithoutPlaintext `GrantTokens` MUST be this keystore's [grant tokens](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
    && decryptOnlyKmsInput.GrantTokens == Some(grantTokens)

    && generateHistory.output.Success?
    && generateHistory.output.value.CiphertextBlob.Some?

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# The operation MUST call [AWS KMS API ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html)
    //# with a request constructed as follows:
    && var activeInput := reEncryptHistory.input;

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `SourceKeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
    && KMSKeystoreOperations.OptCompatible?(kmsConfiguration, activeInput.SourceKeyId)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `DestinationKeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
    && KMSKeystoreOperations.Compatible?(kmsConfiguration, activeInput.DestinationKeyId)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - ReEncrypt `GrantTokens` MUST be this keystore's [grant tokens](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
    && activeInput.GrantTokens == Some(grantTokens)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `CiphertextBlob` MUST be the wrapped DECRYPT_ONLY Branch Key.
    && activeInput.CiphertextBlob == generateHistory.output.value.CiphertextBlob.value

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `SourceEncryptionContext` MUST be the [DECRYPT_ONLY encryption context for branch keys](#decrypt_only-encryption-context).
    && activeInput.SourceEncryptionContext == Some(decryptOnlyEncryptionContext)

    && Structure.BRANCH_KEY_TYPE_PREFIX < decryptOnlyEncryptionContext[Structure.TYPE_FIELD]
    && Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD !in decryptOnlyEncryptionContext

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `DestinationEncryptionContext` MUST be the [ACTIVE encryption context for branch keys](#active-encryption-context).
    && activeInput.DestinationEncryptionContext == Some(Structure.ActiveBranchKeyEncryptionContext(decryptOnlyEncryptionContext))

    && reEncryptHistory.output.Success?
    && reEncryptHistory.output.value.CiphertextBlob.Some?

  }
}
