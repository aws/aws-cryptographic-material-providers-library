// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "Structure.dfy"
include "DefaultKeyStorageInterface.dfy"
include "KMSKeystoreOperations.dfy"
include "KeyStoreErrorMessages.dfy"
include "../../AwsCryptographicMaterialProviders/src/AwsArnParsing.dfy"
include "KmsArn.dfy"
include "HierarchicalVersionUtils.dfy"

module {:options "/functionSyntax:4" } CreateKeys {
  import opened StandardLibrary
  import opened Wrappers
  import Structure
  import DefaultKeyStorageInterface
  import KMSKeystoreOperations
  import ErrorMessages = KeyStoreErrorMessages

  import opened Seq
  import opened UInt = StandardLibrary.UInt
  import Types = AwsCryptographyKeyStoreTypes
  import DDB = ComAmazonawsDynamodbTypes
  import KMS = ComAmazonawsKmsTypes
  import HvUtils = HierarchicalVersionUtils
  import AwsArnParsing
  import KmsArn

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
              && |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 2
              && |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 1
              && old(kmsClient.History.GenerateDataKeyWithoutPlaintext) < kmsClient.History.GenerateDataKeyWithoutPlaintext
              && old(kmsClient.History.ReEncrypt) < kmsClient.History.ReEncrypt

              && var decryptOnlyEncryptionContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
                                                       branchKeyIdentifier,
                                                       branchKeyVersion,
                                                       timestamp,
                                                       logicalKeyStoreName,
                                                       KMSKeystoreOperations.GetKeyId(kmsConfiguration),
                                                       Types.HierarchyVersion.v1,
                                                       customEncryptionContext
                                                     );

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#logical-keystore-name
              //= type=implication
              //# The logical keystore name MUST be bound to every created key.
              && decryptOnlyEncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#encryption-context
              //= type=implication
              //# Any additionally attributes in the EncryptionContext
              //# of the [encrypted hierarchical key](./key-store/key-storage.md#encryptedhierarchicalkey)
              //# MUST be added to the encryption context.
              && (forall k <- customEncryptionContext
                    ::
                      && Structure.ENCRYPTION_CONTEXT_PREFIX + k in decryptOnlyEncryptionContext
                      && decryptOnlyEncryptionContext[Structure.ENCRYPTION_CONTEXT_PREFIX + k] == customEncryptionContext[k])

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# The wrapped Branch Keys, DECRYPT_ONLY and ACTIVE, MUST be created according to [Wrapped Branch Key Creation](#wrapped-branch-key-creation).
              && WrappedBranchKeyCreation?(
                   Seq.Last(Seq.DropLast(kmsClient.History.GenerateDataKeyWithoutPlaintext)),
                   Seq.Last(kmsClient.History.ReEncrypt),
                   kmsClient,
                   kmsConfiguration,
                   grantTokens,
                   decryptOnlyEncryptionContext
                 )


              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# The operation MUST call [AWS KMS API GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html).
              && var beaconKmsRequest := Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext);

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# The operation MUST call AWS KMS GenerateDataKeyWithoutPlaintext with a request constructed as follows:
              && var beaconKmsInput := beaconKmsRequest.input;

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# - `KeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
              && KMSKeystoreOperations.Compatible?(kmsConfiguration, beaconKmsInput.KeyId)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# - `NumberOfBytes` MUST be 32.
              && beaconKmsInput.NumberOfBytes == Some(32)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# - `EncryptionContext` MUST be the [encryption context for beacon keys](#beacon-key-encryption-context).
              && beaconKmsInput.EncryptionContext == Some(Structure.BeaconKeyEncryptionContext(decryptOnlyEncryptionContext))

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# - `GrantTokens` MUST be this keystore's [grant tokens](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
              && beaconKmsInput.GrantTokens == Some(grantTokens)

              && beaconKmsRequest.output.Success?
              && beaconKmsRequest.output.value.CiphertextBlob.Some?

              && |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1

              && Seq.Last(storage.History.WriteNewEncryptedBranchKey).input.Active
                 == Structure.ConstructEncryptedHierarchicalKey(
                      Seq.Last(kmsClient.History.ReEncrypt).input.DestinationEncryptionContext.value,
                      //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
                      //= type=implication
                      //# If the call to AWS KMS ReEncrypt succeeds,
                      //# the operation MUST use the ReEncrypt result `CiphertextBlob`
                      //# as the wrapped ACTIVE Branch Key.
                      Seq.Last(kmsClient.History.ReEncrypt).output.value.CiphertextBlob.value
                    )

              && Seq.Last(storage.History.WriteNewEncryptedBranchKey).input.Version
                 == Structure.ConstructEncryptedHierarchicalKey(
                      Seq.Last(Seq.DropLast(kmsClient.History.GenerateDataKeyWithoutPlaintext)).input.EncryptionContext.value,
                      //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
                      //= type=implication
                      //# If the call to AWS KMS GenerateDataKeyWithoutPlaintext succeeds,
                      //# the operation MUST use the GenerateDataKeyWithoutPlaintext result `CiphertextBlob`
                      //# as the wrapped DECRYPT_ONLY Branch Key.
                      Seq.Last(Seq.DropLast(kmsClient.History.GenerateDataKeyWithoutPlaintext)).output.value.CiphertextBlob.value
                    )

              && Seq.Last(storage.History.WriteNewEncryptedBranchKey).input.Beacon
                 == Structure.ConstructEncryptedHierarchicalKey(
                      Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).input.EncryptionContext.value,
                      //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
                      //= type=implication
                      //# If the call to AWS KMS GenerateDataKeyWithoutPlaintext succeeds,
                      //# the operation MUST use the `CiphertextBlob` as the wrapped Beacon Key.
                      Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.value.CiphertextBlob.value
                    )

              && Seq.Last(storage.History.WriteNewEncryptedBranchKey).output.Success?

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=implication
    //# If creation of the keys are successful,
    //# then the key store MUST call the configured [KeyStorage interface's](./key-store/key-storage.md#interface)
    //# [WriteNewEncryptedBranchKey](./key-store/key-storage.md#writenewencryptedbranchkey) with these 3 [EncryptedHierarchicalKeys](./key-store/key-storage.md#encryptedhierarchicalkey).
    ensures
      && output.Success?
      && |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 2
      && |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 1
      && Seq.Last(Seq.DropLast(kmsClient.History.GenerateDataKeyWithoutPlaintext)).output.Success?
      && Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.Success?
      && Seq.Last(kmsClient.History.ReEncrypt).output.Success?
      ==>
        && |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1

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
        && output.value.branchKeyIdentifier == branchKeyIdentifier


    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=implication
    //# Otherwise, this operation MUST yield an error.
    ensures

      || (&& |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 1
          && Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.Failure?
          ==> output.Failure?)

      || (&& |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 1
          && Seq.Last(kmsClient.History.ReEncrypt).output.Failure?
          ==> output.Failure?)

      || (&& |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 2
          && Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.Failure?
          ==> output.Failure?)

      || (&& |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1
          && Seq.Last(storage.History.WriteNewEncryptedBranchKey).output.Failure?
          ==> output.Failure?)

  {

    var decryptOnlyEncryptionContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
      branchKeyIdentifier,
      branchKeyVersion,
      timestamp,
      logicalKeyStoreName,
      KMSKeystoreOperations.GetKeyId(kmsConfiguration),
      Types.HierarchyVersion.v1,
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

  method {:vcs_split_on_every_assert} VersionActiveBranchKey(
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

  {
    var oldActiveItem :- fetchActiveItem(input.branchKeyIdentifier, storage, logicalKeyStoreName);
    var hierarchyVersion := oldActiveItem.EncryptionContext[Structure.HIERARCHY_VERSION];

    match hierarchyVersion {
      case "1" =>
        output := VersionActiveBranchKeyVersion1(
          oldActiveItem,
          timestamp,
          branchKeyVersion,
          logicalKeyStoreName,
          kmsConfiguration,
          grantTokens,
          kmsClient,
          storage
        );
      case "2" =>
        output := VersionActiveBranchKeyVersion2(
          oldActiveItem,
          timestamp,
          branchKeyVersion,
          logicalKeyStoreName,
          kmsConfiguration,
          grantTokens,
          kmsClient,
          storage
        );
      case _ =>
        output := Failure(Types.KeyStoreException(
                            message :=
                              "Active Branch Key found with an unsupported hierarchy-version.\n"
                              + "Only hierarchy-version 1 or hierarchy-version 2 are supported.\n"
                              + "Found hierarchy-version " + hierarchyVersion + ".\n"
                          ));
    }
  }

  method VersionActiveBranchKeyVersion1(
    oldActiveItem: Types.EncryptedHierarchicalKey,
    timestamp: string,
    branchKeyVersion: string,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    storage: Types.IKeyStorageInterface
  )
    returns (output: Result<Types.VersionKeyOutput, Types.Error>)
    requires 0 < |branchKeyVersion|
    requires Structure.ActiveHierarchicalSymmetricKey?(oldActiveItem)
    requires storage.Modifies !! kmsClient.Modifies
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
    requires storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
             ==>
               logicalKeyStoreName == (storage as DefaultKeyStorageInterface.DynamoDBKeyStorageInterface).logicalKeyStoreName

    requires kmsClient.ValidState() && storage.ValidState()
    modifies storage.Modifies, kmsClient.Modifies
    ensures storage.ValidState() && kmsClient.ValidState()

    ensures |storage.History.GetEncryptedActiveBranchKey| == |old(storage.History.GetEncryptedActiveBranchKey)|

    ensures output.Success?
            ==>
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

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# The operation MUST use the configured `KMS SDK Client` to authenticate the value of the keystore item.
              && |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 2 // This 2 because we need to wrap the new version

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# The operation MUST call [AWS KMS API ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html)
              //# with a request constructed as follows:
              && var reEncryptInput := Seq.Last(Seq.DropLast(kmsClient.History.ReEncrypt)).input;

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# - `SourceEncryptionContext` MUST be the [encryption context](#encryption-context) of the EncryptedHierarchicalKey to be authenticated
              && reEncryptInput.SourceEncryptionContext == Some(oldActiveItem.EncryptionContext)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# - `SourceKeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
              && KMSKeystoreOperations.OptCompatible?(kmsConfiguration, reEncryptInput.SourceKeyId)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# - `CiphertextBlob` MUST be the `CiphertextBlob` attribute value on the EncryptedHierarchicalKey to be authenticated
              && reEncryptInput.CiphertextBlob == oldActiveItem.CiphertextBlob

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# - `GrantTokens` MUST be the configured [grant tokens](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
              && reEncryptInput.GrantTokens == Some(grantTokens)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# - `DestinationKeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
              && KMSKeystoreOperations.Compatible?(kmsConfiguration, reEncryptInput.DestinationKeyId)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# - `DestinationEncryptionContext` MUST be the [encryption context](#encryption-context) of the EncryptedHierarchicalKey to be authenticated
              && reEncryptInput.DestinationEncryptionContext == Some(oldActiveItem.EncryptionContext)

              && |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 1
              && old(kmsClient.History.GenerateDataKeyWithoutPlaintext) < kmsClient.History.GenerateDataKeyWithoutPlaintext
              && old(kmsClient.History.ReEncrypt) < kmsClient.History.ReEncrypt

              && var decryptOnlyEncryptionContext := Structure.NewVersionFromActiveBranchKeyEncryptionContext(
                                                       oldActiveItem.EncryptionContext,
                                                       branchKeyVersion,
                                                       timestamp
                                                     );

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# The wrapped Branch Keys, DECRYPT_ONLY and ACTIVE, MUST be created according to [Wrapped Branch Key Creation](#wrapped-branch-key-creation).
              && WrappedBranchKeyCreation?(
                   Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext),
                   Seq.Last(kmsClient.History.ReEncrypt),
                   kmsClient,
                   kmsConfiguration,
                   grantTokens,
                   decryptOnlyEncryptionContext
                 )

              && |storage.History.WriteNewEncryptedBranchKeyVersion| == |old(storage.History.WriteNewEncryptedBranchKeyVersion)| + 1

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# If creation of the keys are successful,
              //# then the key store MUST call the configured [KeyStorage interface's](./key-store/key-storage.md#interface)
              //# [WriteNewEncryptedBranchKeyVersion](./key-store/key-storage.md##writenewencryptedbranchkeyversion)
              //# with these 2 [EncryptedHierarchicalKeys](./key-store/key-storage.md##encryptedhierarchicalkey).
              && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).input.Active.Item
                 == Structure.ConstructEncryptedHierarchicalKey(
                      Seq.Last(kmsClient.History.ReEncrypt).input.DestinationEncryptionContext.value,
                      Seq.Last(kmsClient.History.ReEncrypt).output.value.CiphertextBlob.value
                    )

              && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).input.Version
                 == Structure.ConstructEncryptedHierarchicalKey(
                      Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).input.EncryptionContext.value,
                      Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.value.CiphertextBlob.value
                    )

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

    ensures
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
      //= type=implication
      //# If the item fails to authenticate this operation MUST fail.
      || (&& |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 1
          && Seq.Last(kmsClient.History.ReEncrypt).output.Failure?
          ==> output.Failure?)

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
      //= type=implication
      //# Otherwise, this operation MUST yield an error.
      || (&& |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 1
          && Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.Failure?
          ==> output.Failure?)

      || (&& |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 2
          && Seq.Last(kmsClient.History.ReEncrypt).output.Failure?
          ==> output.Failure?)

      || (&& |storage.History.WriteNewEncryptedBranchKeyVersion| == |old(storage.History.WriteNewEncryptedBranchKeyVersion)| + 1
          && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).output.Failure?
          ==> output.Failure?)

  {
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

  method VersionActiveBranchKeyVersion2(
    oldActiveItem: Types.EncryptedHierarchicalKey,
    timestamp: string,
    branchKeyVersion: string,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    storage: Types.IKeyStorageInterface
  )
    returns (output: Result<Types.VersionKeyOutput, Types.Error>)
    requires 0 < |branchKeyVersion|
    requires Structure.ActiveHierarchicalSymmetricKey?(oldActiveItem)
    requires KmsArn.ValidKmsArn?(oldActiveItem.KmsArn)
    requires storage.Modifies !! kmsClient.Modifies
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
    requires storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
             ==>
               logicalKeyStoreName == (storage as DefaultKeyStorageInterface.DynamoDBKeyStorageInterface).logicalKeyStoreName

    requires kmsClient.ValidState() && storage.ValidState()
    modifies storage.Modifies, kmsClient.Modifies
    ensures storage.ValidState() && kmsClient.ValidState()
  {
    if !HvUtils.HasUniqueTransformedKeys?(oldActiveItem.EncryptionContext) {
      return Failure(Types.KeyStoreException(
                        message := ErrorMessages.NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS
                      ));
    }
    
    :- Need(
      && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, oldActiveItem.EncryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException(
        message := ErrorMessages.VERSION_KEY_KMS_KEY_ARN_DISAGREEMENT)
    );
    
    var ecToKMS := HvUtils.SelectKmsEncryptionContextForHv2(oldActiveItem.EncryptionContext);

    // we decrypt the oldActiveItem to get the ciphertext and then
    // we encrypt it to a versioned key
    var oldActiveItemPlaintext :- KMSKeystoreOperations.DecryptKeyForHv2(
      oldActiveItem.CiphertextBlob,
      ecToKMS,
      oldActiveItem.KmsArn,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );
    
    var decryptOnlyEncryptionContext := Structure.NewVersionFromActiveBranchKeyEncryptionContext(
      oldActiveItem.EncryptionContext,
      branchKeyVersion,
      timestamp
    );

    output := Failure(Types.KeyStoreException(message := "err")); 
  }

  twostate predicate WrappedBranchKeyCreation?(
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# The operation MUST call [AWS KMS API GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html).
    new generateHistory: KMS.DafnyCallEvent<KMS.GenerateDataKeyWithoutPlaintextRequest, Result<KMS.GenerateDataKeyWithoutPlaintextResponse, KMS.Error>>,
    new reEncryptHistory: KMS.DafnyCallEvent<KMS.ReEncryptRequest, Result<KMS.ReEncryptResponse, KMS.Error>>,
    kmsClient: KMS.IKMSClient,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    decryptOnlyEncryptionContext: map<string, string>
  )
    reads kmsClient.History
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))


    // The history elements are "the things I added"
    requires old(kmsClient.History.GenerateDataKeyWithoutPlaintext) < kmsClient.History.GenerateDataKeyWithoutPlaintext
    requires old(kmsClient.History.ReEncrypt) < kmsClient.History.ReEncrypt

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# The call to AWS KMS GenerateDataKeyWithoutPlaintext MUST use the configured AWS KMS client to make the call.
    requires
      && generateHistory in kmsClient.History.GenerateDataKeyWithoutPlaintext[|old(kmsClient.History.GenerateDataKeyWithoutPlaintext)|..]
      && reEncryptHistory in kmsClient.History.ReEncrypt[|old(kmsClient.History.ReEncrypt)|..]
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

  method fetchActiveItem(
    branchKeyId: string,
    storage: Types.IKeyStorageInterface,
    logicalKeyStoreName: string
  )
    returns (output: Result<Types.EncryptedHierarchicalKey, Types.Error>)
    requires 0 < |branchKeyId|
    requires storage.ValidState()
    requires storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
             ==>
               logicalKeyStoreName == (storage as DefaultKeyStorageInterface.DynamoDBKeyStorageInterface).logicalKeyStoreName
    modifies storage.Modifies
    ensures storage.ValidState()
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
    //= type=implication
    //# VersionKey MUST first get the active version for the branch key from the keystore
    //# by calling the configured [KeyStorage interface's](./key-store/key-storage.md#interface)
    //# [GetEncryptedActiveBranchKey](./key-store/key-storage.md#getencryptedactivebranchkey)
    //# using the `branch-key-id`.
    ensures
      && |storage.History.GetEncryptedActiveBranchKey| == |old(storage.History.GetEncryptedActiveBranchKey)| + 1
      && var getEncryptedActiveBranchKeyInput := Seq.Last(storage.History.GetEncryptedActiveBranchKey).input;
      && branchKeyId == getEncryptedActiveBranchKeyInput.Identifier
    ensures output.Success? ==>
              && |storage.History.GetEncryptedActiveBranchKey| == |old(storage.History.GetEncryptedActiveBranchKey)| + 1
              && Seq.Last(storage.History.GetEncryptedActiveBranchKey).output.Success?
              && var oldActiveItem := Seq.Last(storage.History.GetEncryptedActiveBranchKey).output.value.Item;
              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# VersionKey MUST verify that the returned EncryptedHierarchicalKey MUST have the requested `branch-key-id`.
              && oldActiveItem.Identifier == branchKeyId
                 //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
                 //= type=implication
                 //# VersionKey MUST verify that the returned EncryptedHierarchicalKey is an ActiveHierarchicalSymmetricVersion.
              && Structure.ActiveHierarchicalSymmetricKey?(oldActiveItem)
                 //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
                 //= type=implication
                 //# VersionKey MUST verify that the returned EncryptedHierarchicalKey MUST have a logical table name equal to the configured logical table name.
              && oldActiveItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
    ensures output.Success? ==>
              && Structure.ActiveHierarchicalSymmetricKey?(output.value)
              && KmsArn.ValidKmsArn?(output.value.KmsArn)
  {
    var getEncryptedActiveBranchKeyOutput :- storage.GetEncryptedActiveBranchKey(
      Types.GetEncryptedActiveBranchKeyInput(
        Identifier := branchKeyId
      ));
    var oldActiveItem := getEncryptedActiveBranchKeyOutput.Item;

    :- Need(
      || storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
      || (
           && oldActiveItem.Identifier == branchKeyId
           && Structure.ActiveHierarchicalSymmetricKey?(oldActiveItem)
           && oldActiveItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
         ),
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_ACTIVE_BRANCH_KEY_FROM_STORAGE)
    );
    :- Need(
      KmsArn.ValidKmsArn?(oldActiveItem.KmsArn),
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_ACTIVE_BRANCH_KEY_FROM_STORAGE)
    );

    return Success(oldActiveItem);
  }

}
