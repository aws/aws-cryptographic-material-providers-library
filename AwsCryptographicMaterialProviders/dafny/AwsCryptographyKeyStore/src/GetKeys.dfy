// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "Structure.dfy"
include "KMSKeystoreOperations.dfy"
include "ErrorMessages.dfy"
include "KmsArn.dfy"
include "HierarchicalVersionUtils.dfy"

module GetKeys {
  import opened StandardLibrary
  import opened Wrappers
  import opened Seq
  import opened StandardLibrary.UInt

  import AtomicPrimitives
  import Structure
  import DefaultKeyStorageInterface
  import KMSKeystoreOperations
  import ErrorMessages = KeyStoreErrorMessages

  import Types = AwsCryptographyKeyStoreTypes
  import DDB = ComAmazonawsDynamodbTypes
  import KMS = ComAmazonawsKmsTypes
  import HvUtils = HierarchicalVersionUtils
  import UTF8
  import KmsArn

  method GetActiveKeyAndUnwrap(
    input: Types.GetActiveBranchKeyInput,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    storage: Types.IKeyStorageInterface
  )
    returns (output: Result<Types.GetActiveBranchKeyOutput, Types.Error>)
    requires storage.Modifies !! kmsClient.Modifies

    requires storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
             ==>
               logicalKeyStoreName == (storage as DefaultKeyStorageInterface.DynamoDBKeyStorageInterface).logicalKeyStoreName

    requires kmsClient.ValidState() && storage.ValidState()
    modifies storage.Modifies, kmsClient.Modifies
    ensures storage.ValidState() && kmsClient.ValidState()

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
    //= type=implication
    //# GetActiveBranchKey MUST get the active version for the branch key id from the keystore
    //# by calling the configured [KeyStorage interface's](./key-store/key-storage.md#interface)
    //# [GetEncryptedActiveBranchKey](./key-store/key-storage.md#getencryptedactivebranchkey)
    //# using the supplied `branch-key-id`.
    ensures
      && |storage.History.GetEncryptedActiveBranchKey| == |old(storage.History.GetEncryptedActiveBranchKey)| + 1
      && Seq.Last(storage.History.GetEncryptedActiveBranchKey).input.Identifier == input.branchKeyIdentifier

    ensures output.Success?
            ==>
              && Seq.Last(storage.History.GetEncryptedActiveBranchKey).output.Success?
              && var activeItem := Seq.Last(storage.History.GetEncryptedActiveBranchKey).output.value.Item;

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
              //= type=implication
              //# GetActiveBranchKey MUST verify that the returned EncryptedHierarchicalKey MUST have the requested `branch-key-id`.
              && activeItem.Identifier == input.branchKeyIdentifier

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
              //= type=implication
              //# GetActiveBranchKey MUST verify that the returned EncryptedHierarchicalKey is an ActiveHierarchicalSymmetricVersion.
              && Structure.ActiveHierarchicalSymmetricKey?(activeItem)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
              //= type=implication
              //# GetActiveBranchKey MUST verify that the returned EncryptedHierarchicalKey MUST have a logical table name equal to the configured logical table name.
              && activeItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#discovery
              //= type=implication
              //# The Keystore MAY use the KMS Key ARNs already
              //# persisted to the backing DynamoDB table,
              //# provided they are in records created
              //# with an identical Logical Keystore Name.
              && (kmsConfiguration.kmsKeyArn? ==> activeItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#mrdiscovery
              //= type=implication
              //# The Keystore MAY use the KMS Key ARNs already
              //# persisted to the backing DynamoDB table,
              //# provided they are in records created
              //# with an identical Logical Keystore Name.
              && (kmsConfiguration.kmsMRKeyArn? ==> activeItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName)

              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, activeItem.EncryptionContext[Structure.KMS_FIELD])
              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
              //= type=implication
              //# The operation MUST decrypt the EncryptedHierarchicalKey according to the [AWS KMS Branch Key Decryption](#aws-kms-branch-key-decryption) section.
              && var hv := activeItem.EncryptionContext[Structure.HIERARCHY_VERSION];
              && ValidateKmsDecryption(activeItem, kmsConfiguration, grantTokens, kmsClient, hv)

              && var decryptResponse := Seq.Last(kmsClient.History.Decrypt).output.value;

              && Structure.ToBranchKeyMaterials(activeItem, decryptResponse.Plaintext.value).Success?

              && if hv == Structure.HIERARCHY_VERSION_VALUE_1 then
                   //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
                   //= type=implication
                   //# This operation MUST return the constructed [branch key materials](./structures.md#branch-key-materials).
                   && ValidateActiveKeyBranchKeyMaterials(activeItem, decryptResponse.Plaintext.value, output.value, input.branchKeyIdentifier)

                 else if hv == Structure.HIERARCHY_VERSION_VALUE_2 then
                   && ValidateActiveKeyBranchKeyMaterials(activeItem, decryptResponse.Plaintext.value[Structure.BKC_DIGEST_LENGTH..], output.value, input.branchKeyIdentifier)

                 else
                   false

    ensures
      || (&& |storage.History.GetEncryptedActiveBranchKey| == |old(storage.History.GetEncryptedActiveBranchKey)| + 1
          && Seq.Last(storage.History.GetEncryptedActiveBranchKey).output.Failure?
          ==> output.Failure?)

      || (&& |storage.History.GetEncryptedActiveBranchKey| == |old(storage.History.GetEncryptedActiveBranchKey)| + 1
          && Seq.Last(storage.History.GetEncryptedActiveBranchKey).output.Success?
          && !Structure.ActiveHierarchicalSymmetricKey?(Seq.Last(storage.History.GetEncryptedActiveBranchKey).output.value.Item)
          ==> output.Failure?)

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
      //= type=implication
      //# If the branch key fails to decrypt, GetActiveBranchKey MUST fail.
      || (&& |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1
          && Seq.Last(kmsClient.History.Decrypt).output.Failure?
          ==> output.Failure?)
  {

    var ActiveOutput :- storage.GetEncryptedActiveBranchKey(
      Types.GetEncryptedActiveBranchKeyInput(
        Identifier := input.branchKeyIdentifier
      )
    );

    var branchKeyItemFromStorage := ActiveOutput.Item;

    :- Need(
      (|| storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
       || (
            && Structure.ActiveHierarchicalSymmetricKey?(branchKeyItemFromStorage)
            && branchKeyItemFromStorage.Identifier == input.branchKeyIdentifier
            && branchKeyItemFromStorage.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
          ))
      && KmsArn.ValidKmsArn?(branchKeyItemFromStorage.EncryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_ACTIVE_BRANCH_KEY_FROM_STORAGE)
    );
    :- Need(
      branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_1 ||
      branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_2,
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_HIERARCHY_VERSION
      )
    );
    :- Need(
      Structure.BranchKeyContext?(branchKeyItemFromStorage.EncryptionContext),
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_BRANCH_KEY_CONTEXT
      )
    );
    :- Need(
      KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, branchKeyItemFromStorage.EncryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException( message := ErrorMessages.GET_KEY_ARN_DISAGREEMENT)
    );
    var plainTextKey: seq<uint8>;
    if (branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_1) {
      var kmsRes: KMS.DecryptResponse :- KMSKeystoreOperations.DecryptKeyForHv1(
        branchKeyItemFromStorage,
        kmsConfiguration,
        grantTokens,
        kmsClient
      );
      plainTextKey := kmsRes.Plaintext.value;
    } else if (branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_2) {
      :- Need(
        HvUtils.HasUniqueTransformedKeys?(branchKeyItemFromStorage.EncryptionContext),
        Types.KeyStoreException(
          message := ErrorMessages.NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS
        )
      );
      plainTextKey :- DecryptAndValidateKeyForHV2 (
        branchKeyItemFromStorage,
        kmsConfiguration,
        grantTokens,
        kmsClient
      );
    } else {
      // This else block will never be reached because we have check for hierarchical keyring version before if-else.
      var e := Types.KeyStoreException(
        message := ErrorMessages.INVALID_HIERARCHY_VERSION
      );
      return Failure(e);
    }
    var branchKeyMaterials :- Structure.ToBranchKeyMaterials(
      branchKeyItemFromStorage,
      plainTextKey
    );

    return Success(
        Types.GetActiveBranchKeyOutput(
          branchKeyMaterials := branchKeyMaterials
        ));
  }

  method GetBranchKeyVersion(
    input: Types.GetBranchKeyVersionInput,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    storage: Types.IKeyStorageInterface
  )
    returns (output: Result<Types.GetBranchKeyVersionOutput, Types.Error>)
    requires storage.Modifies !! kmsClient.Modifies

    requires kmsClient.ValidState() && storage.ValidState()
    modifies storage.Modifies, kmsClient.Modifies
    ensures storage.ValidState() && kmsClient.ValidState()

    requires storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
             ==>
               logicalKeyStoreName == (storage as DefaultKeyStorageInterface.DynamoDBKeyStorageInterface).logicalKeyStoreName

    ensures
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
      //= type=implication
      //# GetBranchKeyVersion MUST get the requested version for the branch key id from the keystore
      //# by calling the configured [KeyStorage interface's](./key-store/key-storage.md#interface)
      //# [GetEncryptedActiveBranchKey](./key-store/key-storage.md#getencryptedbranchkeyversion)
      //# using the supplied `branch-key-id`.
      && |storage.History.GetEncryptedBranchKeyVersion| == |old(storage.History.GetEncryptedBranchKeyVersion)| + 1
      && Seq.Last(storage.History.GetEncryptedBranchKeyVersion).input
         == Types.GetEncryptedBranchKeyVersionInput(
              Identifier := input.branchKeyIdentifier,
              Version := input.branchKeyVersion
            )

    ensures output.Success?
            ==>
              && Seq.Last(storage.History.GetEncryptedBranchKeyVersion).output.Success?
              && var versionItem := Seq.Last(storage.History.GetEncryptedBranchKeyVersion).output.value.Item;

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
              //= type=implication
              //# GetBranchKeyVersion MUST verify that the returned EncryptedHierarchicalKey MUST have the requested `branch-key-id`.
              && versionItem.Identifier == input.branchKeyIdentifier

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
              //= type=implication
              //# GetActiveBranchKey MUST verify that the returned EncryptedHierarchicalKey is an HierarchicalSymmetricVersion.
              && Structure.DecryptOnlyHierarchicalSymmetricKey?(versionItem)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
              //= type=implication
              //# GetBranchKeyVersion MUST verify that the returned EncryptedHierarchicalKey MUST have the requested `branchKeyVersion`.
              && versionItem.Type == Types.HierarchicalSymmetricVersion(
                                       Types.HierarchicalSymmetric(
                                         Version := input.branchKeyVersion
                                       ))

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
              //= type=implication
              //# GetBranchKeyVersion MUST verify that the returned EncryptedHierarchicalKey MUST have a logical table name equal to the configured logical table name.
              && versionItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#discovery
              //= type=implication
              //# The Keystore MAY use the KMS Key ARNs already
              //# persisted to the backing DynamoDB table,
              //# provided they are in records created
              //# with an identical Logical Keystore Name.
              && (kmsConfiguration.kmsKeyArn? ==> versionItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#mrdiscovery
              //= type=implication
              //# The Keystore MAY use the KMS Key ARNs already
              //# persisted to the backing DynamoDB table,
              //# provided they are in records created
              //# with an identical Logical Keystore Name.
              && (kmsConfiguration.kmsMRKeyArn? ==> versionItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName)

              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, versionItem.EncryptionContext[Structure.KMS_FIELD])
              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1

              && var hv := versionItem.EncryptionContext[Structure.HIERARCHY_VERSION];
              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
              //= type=implication
              //# The operation MUST decrypt the branch key according to the [AWS KMS Branch Key Decryption](#aws-kms-branch-key-decryption) section.

              && ValidateKmsDecryption(versionItem, kmsConfiguration, grantTokens, kmsClient, hv)

              && var decryptResponse := Seq.Last(kmsClient.History.Decrypt).output.value;

              && Structure.ToBranchKeyMaterials(versionItem, decryptResponse.Plaintext.value).Success?

              && if hv == Structure.HIERARCHY_VERSION_VALUE_1 then
                   //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
                   //= type=implication
                   //# This GetBranchKeyVersion MUST construct [branch key materials](./structures.md#branch-key-materials)
                   //# according to [Branch Key Materials From Authenticated Encryption Context](#branch-key-materials-from-authenticated-encryption-context).

                   //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
                   //= type=implication
                   //# This operation MUST return the constructed [branch key materials](./structures.md#branch-key-materials).
                   ValidateBranchKeyVersionBranchKeyMaterials(versionItem, decryptResponse.Plaintext.value, output.value, input.branchKeyIdentifier, input.branchKeyVersion)

                 else if hv == Structure.HIERARCHY_VERSION_VALUE_2 then
                   ValidateBranchKeyVersionBranchKeyMaterials(versionItem, decryptResponse.Plaintext.value[Structure.BKC_DIGEST_LENGTH..], output.value, input.branchKeyIdentifier, input.branchKeyVersion)
                 else
                   false

    ensures
      || (&& |storage.History.GetEncryptedBranchKeyVersion| == |old(storage.History.GetEncryptedBranchKeyVersion)| + 1
          && Seq.Last(storage.History.GetEncryptedBranchKeyVersion).output.Failure?
          ==> output.Failure?)

      || (&& |storage.History.GetEncryptedBranchKeyVersion| == |old(storage.History.GetEncryptedBranchKeyVersion)| + 1
          && Seq.Last(storage.History.GetEncryptedBranchKeyVersion).output.Success?
          && !Structure.ActiveHierarchicalSymmetricKey?(Seq.Last(storage.History.GetEncryptedBranchKeyVersion).output.value.Item)
          ==> output.Failure?)

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
      //= type=implication
      //# If the branch key fails to decrypt, this operation MUST fail.
      || (&& |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1
          && Seq.Last(kmsClient.History.Decrypt).output.Failure?
          ==> output.Failure?)
  {
    var VersionItem :- storage.GetEncryptedBranchKeyVersion(
      Types.GetEncryptedBranchKeyVersionInput(
        Identifier := input.branchKeyIdentifier,
        Version := input.branchKeyVersion
      )
    );

    var branchKeyItemFromStorage := VersionItem.Item;

    :- Need(
      (|| storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
       || (
            && Structure.DecryptOnlyHierarchicalSymmetricKey?(branchKeyItemFromStorage)
            && branchKeyItemFromStorage.Identifier == input.branchKeyIdentifier
            && branchKeyItemFromStorage.Type == Types.HierarchicalSymmetricVersion(
                                                  Types.HierarchicalSymmetric(
                                                    Version := input.branchKeyVersion
                                                  ))
            && branchKeyItemFromStorage.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
          ))
      && KmsArn.ValidKmsArn?(branchKeyItemFromStorage.EncryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_BRANCH_KEY_VERSION_FROM_STORAGE)
    );
    :- Need(
      KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, branchKeyItemFromStorage.EncryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException( message := ErrorMessages.GET_KEY_ARN_DISAGREEMENT)
    );
    :- Need(
      branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_1 ||
      branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_2,
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_HIERARCHY_VERSION
      )
    );
    :- Need(
      Structure.BranchKeyContext?(branchKeyItemFromStorage.EncryptionContext),
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_BRANCH_KEY_CONTEXT
      )
    );

    var plainTextKey: seq<uint8>;
    if (branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_1) {
      var kmsRes: KMS.DecryptResponse :- KMSKeystoreOperations.DecryptKeyForHv1(
        branchKeyItemFromStorage,
        kmsConfiguration,
        grantTokens,
        kmsClient
      );
      plainTextKey := kmsRes.Plaintext.value;
    } else if (branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_2) {
      :- Need(
        HvUtils.HasUniqueTransformedKeys?(branchKeyItemFromStorage.EncryptionContext),
        Types.KeyStoreException(
          message := ErrorMessages.NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS
        )
      );
      plainTextKey :- DecryptAndValidateKeyForHV2 (
        branchKeyItemFromStorage,
        kmsConfiguration,
        grantTokens,
        kmsClient
      );
    } else {
      // This else block will never be reached because we have check for hierarchical keyring version before if-else.
      var e := Types.KeyStoreException(
        message := ErrorMessages.INVALID_HIERARCHY_VERSION
      );
      return Failure(e);
    }
    var branchKeyMaterials :- Structure.ToBranchKeyMaterials(
      branchKeyItemFromStorage,
      plainTextKey
    );

    return Success(
        Types.GetBranchKeyVersionOutput(
          branchKeyMaterials := branchKeyMaterials
        ));

  }

  method {:vcs_split_on_every_assert} GetBeaconKeyAndUnwrap(
    input: Types.GetBeaconKeyInput,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    storage: Types.IKeyStorageInterface
  )
    returns (output: Result<Types.GetBeaconKeyOutput, Types.Error>)
    requires storage.Modifies !! kmsClient.Modifies
    requires storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
             ==>
               logicalKeyStoreName == (storage as DefaultKeyStorageInterface.DynamoDBKeyStorageInterface).logicalKeyStoreName

    requires kmsClient.ValidState() && storage.ValidState()
    modifies storage.Modifies, kmsClient.Modifies
    ensures storage.ValidState() && kmsClient.ValidState()

    ensures
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
      //= type=implication
      //# GetBeaconKey MUST get the requested beacon key from the keystore
      //# by calling the configured [KeyStorage interface's](./key-store/key-storage.md#interface)
      //# [GetEncryptedBeaconKey](./key-store/key-storage.md#getencryptedbeaconkey)
      //# using the supplied `branch-key-id`.
      && |storage.History.GetEncryptedBeaconKey| == |old(storage.History.GetEncryptedBeaconKey)| + 1
      && Seq.Last(storage.History.GetEncryptedBeaconKey).input.Identifier == input.branchKeyIdentifier

    ensures output.Success? ==>
              && Seq.Last(storage.History.GetEncryptedBeaconKey).output.Success?
              && var beaconItem := Seq.Last(storage.History.GetEncryptedBeaconKey).output.value.Item;

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
              //= type=implication
              //# GetBeaconKey MUST verify that the returned EncryptedHierarchicalKey MUST have the requested `branch-key-id`.
              && beaconItem.Identifier == input.branchKeyIdentifier

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
              //= type=implication
              //# GetBeaconKey MUST verify that the returned EncryptedHierarchicalKey is an ActiveHierarchicalSymmetricBeacon.
              && Structure.ActiveHierarchicalSymmetricBeaconKey?(beaconItem)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
              //= type=implication
              //# GetBeaconKey MUST verify that the returned EncryptedHierarchicalKey MUST have a logical table name equal to the configured logical table name.
              && beaconItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#discovery
              //= type=implication
              //# The Keystore MAY use the KMS Key ARNs already
              //# persisted to the backing DynamoDB table,
              //# provided they are in records created
              //# with an identical Logical Keystore Name.
              && (kmsConfiguration.kmsKeyArn? ==> beaconItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#mrdiscovery
              //= type=implication
              //# The Keystore MAY use the KMS Key ARNs already
              //# persisted to the backing DynamoDB table,
              //# provided they are in records created
              //# with an identical Logical Keystore Name.
              && (kmsConfiguration.kmsMRKeyArn? ==> beaconItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName)

              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, beaconItem.EncryptionContext[Structure.KMS_FIELD])
              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
              //= type=implication
              //# The operation MUST decrypt the beacon key according to the [AWS KMS Branch Key Decryption](#aws-kms-branch-key-decryption) section.

              && var hv := beaconItem.EncryptionContext[Structure.HIERARCHY_VERSION];

              && ValidateKmsDecryption(beaconItem, kmsConfiguration, grantTokens, kmsClient, hv)

              && var decryptResponse := Seq.Last(kmsClient.History.Decrypt).output.value;

              && Structure.ToBeaconKeyMaterials(beaconItem, decryptResponse.Plaintext.value).Success?

              && if hv == Structure.HIERARCHY_VERSION_VALUE_1 then
                   //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
                   //= type=implication
                   //# This GetBeaconKey MUST construct [beacon key materials](./structures.md#beacon-key-materials) from the decrypted branch key material
                   //# and the `branchKeyId` from the returned `branch-key-id` field.

                   //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
                   //= type=implication
                   //# This operation MUST return the constructed [beacon key materials](./structures.md#beacon-key-materials).
                   && ValidateBeaconKeyMaterials(beaconItem, decryptResponse.Plaintext.value, output.value, input.branchKeyIdentifier)

                 else if hv == Structure.HIERARCHY_VERSION_VALUE_2 then
                   && ValidateBeaconKeyMaterials(beaconItem, decryptResponse.Plaintext.value[Structure.BKC_DIGEST_LENGTH..], output.value, input.branchKeyIdentifier)

                 else
                   false

    ensures
      || (&& |storage.History.GetEncryptedBeaconKey| == |old(storage.History.GetEncryptedBeaconKey)| + 1
          && Seq.Last(storage.History.GetEncryptedBeaconKey).output.Failure?
          ==> output.Failure?)

      || (&& |storage.History.GetEncryptedBeaconKey| == |old(storage.History.GetEncryptedBeaconKey)| + 1
          && Seq.Last(storage.History.GetEncryptedBeaconKey).output.Success?
          && !Structure.ActiveHierarchicalSymmetricKey?(Seq.Last(storage.History.GetEncryptedBeaconKey).output.value.Item)
          ==> output.Failure?)

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
      //= type=implication
      //# If the beacon key fails to decrypt, this operation MUST fail.
      || (&& |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1
          && Seq.Last(kmsClient.History.Decrypt).output.Failure?
          ==> output.Failure?)
  {

    var BeaconOutput :- storage.GetEncryptedBeaconKey(
      Types.GetEncryptedBeaconKeyInput(
        Identifier := input.branchKeyIdentifier
      )
    );

    var branchKeyItemFromStorage := BeaconOutput.Item;

    :- Need(
      (|| storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
       || (
            && branchKeyItemFromStorage.Identifier == input.branchKeyIdentifier
            && Structure.ActiveHierarchicalSymmetricBeaconKey?(branchKeyItemFromStorage)
            && branchKeyItemFromStorage.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
          ))
      && KmsArn.ValidKmsArn?(branchKeyItemFromStorage.EncryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_BEACON_KEY_FROM_STORAGE)
    );
    :- Need(
      && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, branchKeyItemFromStorage.EncryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException( message := ErrorMessages.GET_KEY_ARN_DISAGREEMENT)
    );
    :- Need(
      branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_1 ||
      branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_2,
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_HIERARCHY_VERSION
      )
    );
    :- Need(
      Structure.BranchKeyContext?(branchKeyItemFromStorage.EncryptionContext),
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_BRANCH_KEY_CONTEXT
      )
    );
    var plainTextKey: seq<uint8>;
    if (branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_1) {
      var kmsRes: KMS.DecryptResponse :- KMSKeystoreOperations.DecryptKeyForHv1(
        branchKeyItemFromStorage,
        kmsConfiguration,
        grantTokens,
        kmsClient
      );
      plainTextKey := kmsRes.Plaintext.value;
    } else if (branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_2) {
      :- Need(
        HvUtils.HasUniqueTransformedKeys?(branchKeyItemFromStorage.EncryptionContext),
        Types.KeyStoreException(
          message := ErrorMessages.NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS
        )
      );
      plainTextKey :- DecryptAndValidateKeyForHV2 (
        branchKeyItemFromStorage,
        kmsConfiguration,
        grantTokens,
        kmsClient
      );
    } else {
      // This else block will never be reached because we have check for hierarchical keyring version before if-else.
      var e := Types.KeyStoreException(
        message := ErrorMessages.INVALID_HIERARCHY_VERSION
      );
      return Failure(e);
    }
    var branchKeyMaterials :- Structure.ToBeaconKeyMaterials(
      branchKeyItemFromStorage,
      plainTextKey
    );

    return Success(
        Types.GetBeaconKeyOutput(
          beaconKeyMaterials := branchKeyMaterials
        ));
  }

  method DecryptAndValidateKeyForHV2(
    branchKeyItemFromStorage: Types.EncryptedHierarchicalKey,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  ) returns (result: Result<seq<uint8>, Types.Error>)

    requires Structure.BranchKeyContext?(branchKeyItemFromStorage.EncryptionContext)

    requires HvUtils.HasUniqueTransformedKeys?(branchKeyItemFromStorage.EncryptionContext)

    requires KmsArn.ValidKmsArn?(branchKeyItemFromStorage.KmsArn)

    requires KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, branchKeyItemFromStorage.KmsArn)

    requires kmsClient.ValidState()
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()

    ensures result.Success?
            ==>
              && var ciphertextBlob := branchKeyItemFromStorage.CiphertextBlob;

              && var kmsArnFromStorage := branchKeyItemFromStorage.KmsArn;

              && var ecToKMS := HvUtils.SelectKmsEncryptionContextForHv2(branchKeyItemFromStorage.EncryptionContext);

              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, branchKeyItemFromStorage.KmsArn)

              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1

              && KMSKeystoreOperations.AwsKmsBranchKeyDecryptionForHV2?(
                   ciphertextBlob,
                   ecToKMS,
                   kmsArnFromStorage,
                   kmsConfiguration,
                   grantTokens,
                   kmsClient,
                   Seq.Last(kmsClient.History.Decrypt)
                 )
              && var decryptResponse := Seq.Last(kmsClient.History.Decrypt).output.value;

              && result.value == decryptResponse.Plaintext.value[Structure.BKC_DIGEST_LENGTH..]
  {
    // Get encryption context for KMS

    // branchKeyItemFromStorage.EncryptionContext comes from storage and is not the actual encrytion context that is send to KMS.
    // branchKeyItemFromStorage.EncryptionContext contains all the items in the dynamodb table and table name.
    var ecToKMS := HvUtils.SelectKmsEncryptionContextForHv2(branchKeyItemFromStorage.EncryptionContext);

    // Decrypt the key using KMS
    var kmsDecryptRes :- KMSKeystoreOperations.DecryptKeyForHv2(
      branchKeyItemFromStorage.CiphertextBlob,
      ecToKMS,
      branchKeyItemFromStorage.KmsArn,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );

    // Get crypto client
    var crypto? := HvUtils.ProvideCryptoClient();
    if (crypto?.Failure?) {
      var e := Types.KeyStoreException(
        message := "Local Cryptography error: " +
        AtomicPrimitives.ErrorUtils.MessageOrUnknown(crypto?.error)
      );
      return Failure(e);
    }

    // Unpack the plaintext tuple
    var (protectedMdDigest, plainTextKey) :=
      HvUtils.UnpackPlainTextTuple(kmsDecryptRes.Plaintext.value);

    // Create and validate BKC digest
    var bkcFromStorage :- HvUtils.createBKCDigest(
      branchKeyItemFromStorage.EncryptionContext,
      crypto?.value
    );

    // Verify the digest matches
    if (bkcFromStorage != protectedMdDigest) {
      var e := Types.KeyStoreException(
        message := ErrorMessages.MD_DIGEST_SHA_NOT_MATCHED
      );
      return Failure(e);
    }

    // Return the plaintext key if all validations pass
    return Success(plainTextKey);
  }

  predicate ValidateKmsDecryption(
    item: Types.EncryptedHierarchicalKey,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    hv: string
  )
    requires Structure.BranchKeyContext?(item.EncryptionContext)
    requires 0 < |kmsClient.History.Decrypt|
    reads kmsClient.History
  {
    && ((hv == Structure.HIERARCHY_VERSION_VALUE_1) || (hv == Structure.HIERARCHY_VERSION_VALUE_2))

    && if hv == Structure.HIERARCHY_VERSION_VALUE_2 then

         && HvUtils.HasUniqueTransformedKeys?(item.EncryptionContext)

         && var ciphertextBlob := item.CiphertextBlob;

         && var kmsArnFromStorage := item.KmsArn;

         && var ecToKMS := HvUtils.SelectKmsEncryptionContextForHv2(item.EncryptionContext);

         && KMSKeystoreOperations.AwsKmsBranchKeyDecryptionForHV2?(
           ciphertextBlob,
           ecToKMS,
           kmsArnFromStorage,
           kmsConfiguration,
           grantTokens,
           kmsClient,
           Seq.Last(kmsClient.History.Decrypt)
         )

       else if hv == Structure.HIERARCHY_VERSION_VALUE_1 then
         && Structure.EncryptedHierarchicalKeyFromStorage?(item)
         && KMSKeystoreOperations.AwsKmsBranchKeyDecryptionForHV1?(
              item,
              kmsConfiguration,
              grantTokens,
              kmsClient,
              Seq.Last(kmsClient.History.Decrypt)
            )

       else false
  }

  predicate ValidateActiveKeyBranchKeyMaterials(
    item: Types.EncryptedHierarchicalKey,
    plainTextKey: seq<uint8>,
    activeBranchKeyOutput: Types.GetActiveBranchKeyOutput,
    expectedIdentifier: string
  )
    requires Structure.EncryptedHierarchicalKeyFromStorage?(item)
    requires
      || item.Type.ActiveHierarchicalSymmetricVersion?
      || item.Type.HierarchicalSymmetricVersion?
  {
    && var branchKeyMaterials :=  Structure.ToBranchKeyMaterials(
                                    item,
                                    plainTextKey
                                  );
    && branchKeyMaterials.Success?
    && activeBranchKeyOutput.branchKeyMaterials == branchKeyMaterials.value
    && activeBranchKeyOutput.branchKeyMaterials.branchKeyIdentifier == expectedIdentifier
  }

  predicate ValidateBranchKeyVersionBranchKeyMaterials(
    item: Types.EncryptedHierarchicalKey,
    plainTextKey: seq<uint8>,
    activeBranchKeyOutput: Types.GetBranchKeyVersionOutput,
    expectedIdentifier: string,
    actualBranchKeyVersion: string
  )
    requires Structure.EncryptedHierarchicalKeyFromStorage?(item)
    requires
      || item.Type.ActiveHierarchicalSymmetricVersion?
      || item.Type.HierarchicalSymmetricVersion?
  {
    && var branchKeyMaterials :=  Structure.ToBranchKeyMaterials(
                                    item,
                                    plainTextKey
                                  );
    && branchKeyMaterials.Success?
    && activeBranchKeyOutput.branchKeyMaterials == branchKeyMaterials.value
    && activeBranchKeyOutput.branchKeyMaterials.branchKeyIdentifier == expectedIdentifier
    && UTF8.Encode(actualBranchKeyVersion).Success?
    && activeBranchKeyOutput.branchKeyMaterials.branchKeyVersion == UTF8.Encode(actualBranchKeyVersion).value
  }

  predicate ValidateBeaconKeyMaterials(
    beaconItem: Types.EncryptedHierarchicalKey,
    plainTextKey: seq<uint8>,
    activeBranchKeyOutput: Types.GetBeaconKeyOutput,
    expectedIdentifier: string
  )
    requires Structure.ActiveHierarchicalSymmetricBeaconKey?(beaconItem)
  {
    && var beaconKeyMaterials :=  Structure.ToBeaconKeyMaterials(
                                    beaconItem,
                                    plainTextKey
                                  );
    && beaconKeyMaterials.Success?
    && activeBranchKeyOutput.beaconKeyMaterials == beaconKeyMaterials.value
    && activeBranchKeyOutput.beaconKeyMaterials.beaconKeyIdentifier == expectedIdentifier
  }
}
