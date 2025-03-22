// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "Structure.dfy"
include "KMSKeystoreOperations.dfy"
include "ErrorMessages.dfy"
include "KmsArn.dfy"
include "../../AwsCryptographicMaterialProviders/src/CanonicalEncryptionContext.dfy"
include "HierarchicalVersionUtils.dfy"
module GetKeys {
  import opened StandardLibrary
  import opened Wrappers
  import opened Seq

  import Structure
  import CanonicalEncryptionContext
  import DefaultKeyStorageInterface
  import KMSKeystoreOperations
  import ErrorMessages = KeyStoreErrorMessages
  import AtomicPrimitives
  import HierarchicalVersionUtils

  import Types = AwsCryptographyKeyStoreTypes
  import DDB = ComAmazonawsDynamodbTypes
  import KMS = ComAmazonawsKmsTypes
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

              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, activeItem.EncryptionContext)
              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
              //= type=implication
              //# The operation MUST decrypt the EncryptedHierarchicalKey according to the [AWS KMS Branch Key Decryption](#aws-kms-branch-key-decryption) section.
              // TODO: Verification
              // && (activeItem.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_2
              //     ==>
              //       && var hv2EC := HierarchicalVersionUtils.GetHV2EC(activeItem.EncryptionContext);
              //       && var hv2ActiveItem := Types.EncryptedHierarchicalKey(
              //           Identifier := activeItem.Identifier,
              //           Type := activeItem.Type,
              //           CreateTime := activeItem.CreateTime,
              //           KmsArn := activeItem.KmsArn,
              //           EncryptionContext := hv2EC,
              //           CiphertextBlob := activeItem.CiphertextBlob
              //         );
              //       && KMSKeystoreOperations.AwsKmsBranchKeyHV2Decryption?(
              //           activeItem,
              //           kmsConfiguration,
              //           grantTokens,
              //           kmsClient,
              //           Seq.Last(kmsClient.History.Decrypt)
              //         )
              //     )
              && KMSKeystoreOperations.AwsKmsBranchKeyHV1Decryption?(
                   activeItem,
                   kmsConfiguration,
                   grantTokens,
                   kmsClient,
                   Seq.Last(kmsClient.History.Decrypt)
                 )

              && var decryptResponse := Seq.Last(kmsClient.History.Decrypt).output.value;

              && Structure.ToBranchKeyMaterials(activeItem, decryptResponse.Plaintext.value).Success?

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
              //= type=implication
              //# This GetActiveBranchKey MUST construct [branch key materials](./structures.md#branch-key-materials)
              //# according to [Branch Key Materials From Authenticated Encryption Context](#branch-key-materials-from-authenticated-encryption-context).
              && var branchKeyMaterials :=  Structure.ToBranchKeyMaterials(
                                              activeItem,
                                              decryptResponse.Plaintext.value
                                            ).value;

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
              //= type=implication
              //# This operation MUST return the constructed [branch key materials](./structures.md#branch-key-materials).
              && output.value.branchKeyMaterials == branchKeyMaterials

              && output.value.branchKeyMaterials.branchKeyIdentifier == input.branchKeyIdentifier

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
      || storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
      || (
           && Structure.ActiveHierarchicalSymmetricKey?(branchKeyItemFromStorage)
           && branchKeyItemFromStorage.Identifier == input.branchKeyIdentifier
           && branchKeyItemFromStorage.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
         ),
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_ACTIVE_BRANCH_KEY_FROM_STORAGE)
    );
    :- Need(
      branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_1 ||
      branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_2,
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
    if (branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_1) {
      var branchKey: KMS.DecryptResponse :- KMSKeystoreOperations.DecryptKeyForHV1(
        branchKeyItemFromStorage,
        kmsConfiguration,
        grantTokens,
        kmsClient
      );

      var branchKeyMaterials :- Structure.ToBranchKeyMaterials(
        branchKeyItemFromStorage,
        branchKey.Plaintext.value
      );
      return Success(
          Types.GetActiveBranchKeyOutput(
            branchKeyMaterials := branchKeyMaterials
          ));
    } else if (branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_2) {
      // branchKeyItemFromStorage.EncryptionContext comes from storage is not the actual EC.
      // branchKeyItemFromStorage.EncryptionContext contains all the items in the dynamodb table and table name.
      var hv2EC := Structure.ExtractCustomEncryptionContextAs(branchKeyItemFromStorage.EncryptionContext);
      var hv2BranchKey := Types.EncryptedHierarchicalKey(
        Identifier := branchKeyItemFromStorage.Identifier,
        Type := branchKeyItemFromStorage.Type,
        CreateTime := branchKeyItemFromStorage.CreateTime,
        KmsArn := branchKeyItemFromStorage.KmsArn,
        EncryptionContext := hv2EC,
        CiphertextBlob := branchKeyItemFromStorage.CiphertextBlob
      );
      print "\nHv2 Branch Key: ";
      print hv2BranchKey;
      var branchKey: KMS.DecryptResponse :- KMSKeystoreOperations.DecryptKeyForHV2(
        hv2BranchKey,
        kmsConfiguration,
        grantTokens,
        kmsClient
      );
      var validateResult := HierarchicalVersionUtils.ValidateMdDigest(branchKey.Plaintext.value, branchKeyItemFromStorage);
      if (validateResult.Failure?) {
        return Failure(validateResult.error);
      }
      var branchKeyMaterials :- Structure.ToBranchKeyMaterials(
        branchKeyItemFromStorage,
        branchKey.Plaintext.value[Structure.MD_DIGEST_LENGTH..]
      );
      return Success(
          Types.GetActiveBranchKeyOutput(
            branchKeyMaterials := branchKeyMaterials
          ));
    } else {
      // This else block will never be reached because we have check for hierarchical keyring version before if-else.
      var e := Types.KeyStoreException(
        message := ErrorMessages.INVALID_HIERARCHY_VERSION
      );
      return Failure(e);
    }

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

              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, versionItem.EncryptionContext)
              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
              //= type=implication
              //# The operation MUST decrypt the branch key according to the [AWS KMS Branch Key Decryption](#aws-kms-branch-key-decryption) section.
              && KMSKeystoreOperations.AwsKmsBranchKeyHV1Decryption?(
                   versionItem,
                   kmsConfiguration,
                   grantTokens,
                   kmsClient,
                   Seq.Last(kmsClient.History.Decrypt)
                 )

              // && var versionEncryptionContext := Structure.ToBranchKeyContext(versionItem, logicalKeyStoreName);
              && var decryptResponse := Seq.Last(kmsClient.History.Decrypt).output.value;

              && Structure.ToBranchKeyMaterials(versionItem, decryptResponse.Plaintext.value).Success?

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
              //= type=implication
              //# This GetBranchKeyVersion MUST construct [branch key materials](./structures.md#branch-key-materials)
              //# according to [Branch Key Materials From Authenticated Encryption Context](#branch-key-materials-from-authenticated-encryption-context).
              && var branchKeyMaterials := Structure
                                           .ToBranchKeyMaterials(
                                             versionItem,
                                             decryptResponse.Plaintext.value
                                           )
                                           .value;

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
              //= type=implication
              //# This operation MUST return the constructed [branch key materials](./structures.md#branch-key-materials).
              && output.value.branchKeyMaterials == branchKeyMaterials

              && output.value.branchKeyMaterials.branchKeyIdentifier == input.branchKeyIdentifier
              && UTF8.Encode(input.branchKeyVersion).Success?
              && output.value.branchKeyMaterials.branchKeyVersion == UTF8.Encode(input.branchKeyVersion).value

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
      || storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
      || (
           && Structure.DecryptOnlyHierarchicalSymmetricKey?(branchKeyItemFromStorage)
           && branchKeyItemFromStorage.Identifier == input.branchKeyIdentifier
           && branchKeyItemFromStorage.Type == Types.HierarchicalSymmetricVersion(
                                                 Types.HierarchicalSymmetric(
                                                   Version := input.branchKeyVersion
                                                 ))
           && branchKeyItemFromStorage.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
         ),
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_BRANCH_KEY_VERSION_FROM_STORAGE)
    );
    :- Need(
      branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_1 ||
      branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_2,
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_HIERARCHY_VERSION
      )
    );

    if (branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_1) {
      var branchKey: KMS.DecryptResponse :- KMSKeystoreOperations.DecryptKeyForHV1(
        branchKeyItemFromStorage,
        kmsConfiguration,
        grantTokens,
        kmsClient
      );

      var branchKeyMaterials :- Structure.ToBranchKeyMaterials(
        branchKeyItemFromStorage,
        branchKey.Plaintext.value
      );

      return Success(
          Types.GetBranchKeyVersionOutput(
            branchKeyMaterials := branchKeyMaterials
          ));
    } else if (branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_2) {
      // branchKeyItemFromStorage.EncryptionContext comes from storage is not the actual EC.
      // branchKeyItemFromStorage.EncryptionContext contains all the items in the dynamodb table and table name.
      var hv2EC := HierarchicalVersionUtils.GetHV2EC(branchKeyItemFromStorage.EncryptionContext);
      var hv2BranchKey := Types.EncryptedHierarchicalKey(
        Identifier := branchKeyItemFromStorage.Identifier,
        Type := branchKeyItemFromStorage.Type,
        CreateTime := branchKeyItemFromStorage.CreateTime,
        KmsArn := branchKeyItemFromStorage.KmsArn,
        EncryptionContext := hv2EC,
        CiphertextBlob := branchKeyItemFromStorage.CiphertextBlob
      );
      var branchKey: KMS.DecryptResponse :- KMSKeystoreOperations.DecryptKeyForHV2(
        hv2BranchKey,
        kmsConfiguration,
        grantTokens,
        kmsClient
      );
      var validateResult := HierarchicalVersionUtils.ValidateMdDigest(branchKey.Plaintext.value, branchKeyItemFromStorage);
      if (validateResult.Failure?) {
        return Failure(validateResult.error);
      }
      var branchKeyMaterials :- Structure.ToBranchKeyMaterials(
        branchKeyItemFromStorage,
        branchKey.Plaintext.value[0..Structure.AES_256_LENGTH]
      );
      return Success(
          Types.GetBranchKeyVersionOutput(
            branchKeyMaterials := branchKeyMaterials
          ));
    } else {
      // This else block will never be reached because we have check for hierarchical keyring version before if-else.
      var e := Types.KeyStoreException(
        message := ErrorMessages.INVALID_HIERARCHY_VERSION
      );
      return Failure(e);
    }

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

              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, beaconItem.EncryptionContext)
              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
              //= type=implication
              //# The operation MUST decrypt the beacon key according to the [AWS KMS Branch Key Decryption](#aws-kms-branch-key-decryption) section.
              && KMSKeystoreOperations.AwsKmsBranchKeyHV1Decryption?(
                   beaconItem,
                   kmsConfiguration,
                   grantTokens,
                   kmsClient,
                   Seq.Last(kmsClient.History.Decrypt)
                 )

              && var decryptResponse := Seq.Last(kmsClient.History.Decrypt).output.value;

              && Structure.ToBeaconKeyMaterials(beaconItem, decryptResponse.Plaintext.value).Success?

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
              //= type=implication
              //# This GetBeaconKey MUST construct [beacon key materials](./structures.md#beacon-key-materials) from the decrypted branch key material
              //# and the `branchKeyId` from the returned `branch-key-id` field.
              && var beaconKeyMaterials := Structure.ToBeaconKeyMaterials(
                                             beaconItem,
                                             decryptResponse.Plaintext.value
                                           ).value;

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
              //= type=implication
              //# This operation MUST return the constructed [beacon key materials](./structures.md#beacon-key-materials).
              && output.value.beaconKeyMaterials == beaconKeyMaterials

              && output.value.beaconKeyMaterials.beaconKeyIdentifier == input.branchKeyIdentifier

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
      || storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
      || (
           && branchKeyItemFromStorage.Identifier == input.branchKeyIdentifier
           && Structure.ActiveHierarchicalSymmetricBeaconKey?(branchKeyItemFromStorage)
           && branchKeyItemFromStorage.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
         ),
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_BEACON_KEY_FROM_STORAGE)
    );
    :- Need(
      branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_1 ||
      branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_2,
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

    if (branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_1) {
      var branchKey: KMS.DecryptResponse :- KMSKeystoreOperations.DecryptKeyForHV1(
        branchKeyItemFromStorage,
        kmsConfiguration,
        grantTokens,
        kmsClient
      );

      var beaconKeyMaterials :- Structure.ToBeaconKeyMaterials(
        branchKeyItemFromStorage,
        branchKey.Plaintext.value
      );

      return Success(
          Types.GetBeaconKeyOutput(
            beaconKeyMaterials := beaconKeyMaterials
          ));
    } else if (branchKeyItemFromStorage.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_2) {
      // branchKeyItemFromStorage.EncryptionContext comes from storage is not the actual EC.
      // branchKeyItemFromStorage.EncryptionContext contains all the items in the dynamodb table and table name.
      var hv2EC := HierarchicalVersionUtils.GetHV2EC(branchKeyItemFromStorage.EncryptionContext);
      var hv2BranchKey := Types.EncryptedHierarchicalKey(
        Identifier := branchKeyItemFromStorage.Identifier,
        Type := branchKeyItemFromStorage.Type,
        CreateTime := branchKeyItemFromStorage.CreateTime,
        KmsArn := branchKeyItemFromStorage.KmsArn,
        EncryptionContext := hv2EC,
        CiphertextBlob := branchKeyItemFromStorage.CiphertextBlob
      );
      var branchKey: KMS.DecryptResponse :- KMSKeystoreOperations.DecryptKeyForHV2(
        hv2BranchKey,
        kmsConfiguration,
        grantTokens,
        kmsClient
      );
      var validateResult := HierarchicalVersionUtils.ValidateMdDigest(branchKey.Plaintext.value, branchKeyItemFromStorage);
      if (validateResult.Failure?) {
        return Failure(validateResult.error);
      }
      var beaconKeyMaterials :- Structure.ToBeaconKeyMaterials(
        branchKeyItemFromStorage,
        branchKey.Plaintext.value[0..Structure.AES_256_LENGTH]
      );
      return Success(
          Types.GetBeaconKeyOutput(
            beaconKeyMaterials := beaconKeyMaterials
          ));
    } else {
      // This else block will never be reached because we have check for hierarchical keyring version before if-else.
      var e := Types.KeyStoreException(
        message := ErrorMessages.INVALID_HIERARCHY_VERSION
      );
      return Failure(e);
    }
  }

}
