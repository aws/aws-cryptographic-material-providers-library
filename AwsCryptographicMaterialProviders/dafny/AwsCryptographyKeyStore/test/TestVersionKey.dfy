// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"
include "CleanupItems.dfy"

module TestVersionKey {
  import Types = AwsCryptographyKeyStoreTypes
  import ComAmazonawsKmsTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import KeyStore
  import UUID
  import opened StandardLibrary
  import opened Wrappers
  import opened AwsKmsUtils
  import opened Fixtures
  import CleanupItems
  import Structure
  import DDBKeystoreOperations
  import ComAmazonawsDynamodbTypes
  import KeyStoreErrorMessages

  method {:test} TestVersionKey()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);
    expect ComAmazonawsDynamodbTypes.IsValid_TableName(branchKeyStoreName);

    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    // Create a new key
    // We will create a use this new key per run to avoid tripping up
    // when running in different runtimes
    var branchKeyId :- expect keyStore.CreateKey(Types.CreateKeyInput(
                                                   branchKeyIdentifier := None,
                                                   encryptionContext := None
                                                 ));

    var oldActiveResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var oldActiveVersion :- expect UTF8.Decode(oldActiveResult.branchKeyMaterials.branchKeyVersion);

    var versionKeyResult :- expect keyStore.VersionKey(
      Types.VersionKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var getBranchKeyVersionResult :- expect keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier,
        // We get the old active key by using the version
        branchKeyVersion := oldActiveVersion
      )
    );

    var newActiveResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var newActiveVersion :- expect UTF8.Decode(newActiveResult.branchKeyMaterials.branchKeyVersion);

    // Since this process uses a read DDB table,
    // the number of records will forever increase.
    // To avoid this, remove the items.
    CleanupItems.DeleteVersion(branchKeyId.branchKeyIdentifier, newActiveVersion, ddbClient);
    CleanupItems.DeleteVersion(branchKeyId.branchKeyIdentifier, oldActiveVersion, ddbClient);
    CleanupItems.DeleteActive(branchKeyId.branchKeyIdentifier, ddbClient);

    // We expect that getting the old active key has the same version as getting a branch key through the get version key api
    expect getBranchKeyVersionResult.branchKeyMaterials.branchKeyVersion == oldActiveResult.branchKeyMaterials.branchKeyVersion;
    expect getBranchKeyVersionResult.branchKeyMaterials.branchKey == oldActiveResult.branchKeyMaterials.branchKey;
    // We expect that if we rotate the branch key, the returned materials MUST NOT be equal to the previous active key.
    expect getBranchKeyVersionResult.branchKeyMaterials.branchKeyVersion != newActiveResult.branchKeyMaterials.branchKeyVersion;
    expect getBranchKeyVersionResult.branchKeyMaterials.branchKey != newActiveResult.branchKeyMaterials.branchKey;
  }

  method {:test} TestVersionKeyWithEC()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);
    expect ComAmazonawsDynamodbTypes.IsValid_TableName(branchKeyStoreName);

    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    // Create a new key
    // We will create a use this new key per run to avoid tripping up
    // when running in different runtimes
    var id :- expect UUID.GenerateUUID();

    var customEC := map[
      "some" := "encryption",
      "context" := "values"
    ];
    var encryptionContext :- expect EncodeEncryptionContext(customEC);

    var branchKeyId :- expect keyStore.CreateKey(Types.CreateKeyInput(
                                                   branchKeyIdentifier := Some(id),
                                                   encryptionContext := Some(encryptionContext)
                                                 ));

    expect branchKeyId.branchKeyIdentifier == id;

    var oldActiveResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));
    var mat := oldActiveResult.branchKeyMaterials;
    expect mat.branchKeyIdentifier == id;
    var matEC :- expect DecodeEncryptionContext(mat.encryptionContext);
    expect matEC == customEC;

    var oldActiveVersion :- expect UTF8.Decode(oldActiveResult.branchKeyMaterials.branchKeyVersion);

    var versionKeyResult :- expect keyStore.VersionKey(
      Types.VersionKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var getBranchKeyVersionResult :- expect keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier,
        // We get the old active key by using the version
        branchKeyVersion := oldActiveVersion
      )
    );
    var mat2 := getBranchKeyVersionResult.branchKeyMaterials;
    expect mat.branchKeyIdentifier == id;
    var mat2EC :- expect DecodeEncryptionContext(mat.encryptionContext);
    expect mat2EC == customEC;
    expect mat2.branchKeyVersion == mat.branchKeyVersion;

    var newActiveResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));
    var mat3 := newActiveResult.branchKeyMaterials;
    expect mat.branchKeyIdentifier == id;
    var mat3EC :- expect DecodeEncryptionContext(mat.encryptionContext);
    expect mat3EC == customEC;
    expect mat3.branchKeyVersion != mat.branchKeyVersion;

    var newActiveVersion :- expect UTF8.Decode(newActiveResult.branchKeyMaterials.branchKeyVersion);

    expect newActiveVersion != oldActiveVersion;

    // Since this process uses a real DDB table,
    // the number of records will forever increase.
    // To avoid this, remove the items.
    CleanupItems.DeleteVersion(branchKeyId.branchKeyIdentifier, newActiveVersion, ddbClient);
    CleanupItems.DeleteVersion(branchKeyId.branchKeyIdentifier, oldActiveVersion, ddbClient);
    CleanupItems.DeleteActive(branchKeyId.branchKeyIdentifier, ddbClient);

    // We expect that getting the old active key has the same version as getting a branch key through the get version key api
    expect getBranchKeyVersionResult.branchKeyMaterials.branchKeyVersion == oldActiveResult.branchKeyMaterials.branchKeyVersion;
    expect getBranchKeyVersionResult.branchKeyMaterials.branchKey == oldActiveResult.branchKeyMaterials.branchKey;
    // We expect that if we rotate the branch key, the returned materials MUST NOT be equal to the previous active key.
    expect getBranchKeyVersionResult.branchKeyMaterials.branchKeyVersion != newActiveResult.branchKeyMaterials.branchKeyVersion;
    expect getBranchKeyVersionResult.branchKeyMaterials.branchKey != newActiveResult.branchKeyMaterials.branchKey;
    // We expect that the custom EC is consistent across all versions of a Branch Key
    // Which makes this a test for:
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
    //= type=test
    //# - Every key-value pair of the custom [encryption context](./structures.md#encryption-context-3) that is associated with the branch key
    //# MUST be added with an Attribute Name of `aws-crypto-ec:` + the Key and Attribute Value (S) of the value.
    expect matEC == customEC;
    expect mat2EC == customEC;
    expect mat3EC == customEC;
  }

  method {:test} TestMrkVersionKey()
  {
    var ddbClient :- expect DDB.DynamoDBClient();

    var eastKeyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := KmsMrkConfigEast,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient)
    );

    var westKeyStoreConfig    := eastKeyStoreConfig.(kmsConfiguration := KmsMrkConfigWest);
    var eastSrkKeyStoreConfig := eastKeyStoreConfig.(kmsConfiguration := KmsSrkConfigEast);
    var westSrkKeyStoreConfig := eastKeyStoreConfig.(kmsConfiguration := KmsSrkConfigWest);

    var eastKeyStore :- expect KeyStore.KeyStore(eastKeyStoreConfig);
    var westKeyStore :- expect KeyStore.KeyStore(westKeyStoreConfig);
    var eastSrkKeyStore :- expect KeyStore.KeyStore(eastSrkKeyStoreConfig);
    var westSrkKeyStore :- expect KeyStore.KeyStore(westSrkKeyStoreConfig);

    // Create a new key with the WEST key store
    // We will create a use this new key per run to avoid tripping up
    // when running in different runtimes
    var branchKeyId :- expect westKeyStore.CreateKey(Types.CreateKeyInput(
                                                       branchKeyIdentifier := None,
                                                       encryptionContext := None
                                                     ));

    var oldActiveResult :- expect westKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var oldActiveVersion :- expect UTF8.Decode(oldActiveResult.branchKeyMaterials.branchKeyVersion);

    // Version the key with the EAST key store
    var versionKeyResult :- expect eastKeyStore.VersionKey(
      Types.VersionKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var getBranchKeyVersionResultWest :- expect westKeyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier,
        // We get the old active key by using the version
        branchKeyVersion := oldActiveVersion
      )
    );

    var getBranchKeyVersionResultEast :- expect eastKeyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier,
        // We get the old active key by using the version
        branchKeyVersion := oldActiveVersion
      )
    );

    expect getBranchKeyVersionResultWest == getBranchKeyVersionResultEast;

    var newActiveResultWest :- expect westKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));
    var newActiveResultEast :- expect eastKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    expect newActiveResultWest == newActiveResultEast;

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
    // = type=test
    // # The `kms-arn` stored in the DDB table MUST NOT change as a result of this operation,
    //# even if the KeyStore is configured with a `KMS MRKey ARN` that does not exactly match the stored ARN.
    var newActiveResultSrkWest :- expect westSrkKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));
    // westSrkKeyStore succeeds, because ARN is still west
    expect newActiveResultSrkWest == newActiveResultEast;
    var newActiveResultSrkEastResult := eastSrkKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));
    // eastSrkKeyStore fails, because ARN is still west
    expect newActiveResultSrkEastResult.Failure?;
    expect newActiveResultSrkEastResult.error ==
           Types.KeyStoreException(message :=  KeyStoreErrorMessages.GET_KEY_ARN_DISAGREEMENT);

    var newActiveVersionWest :- expect UTF8.Decode(newActiveResultWest.branchKeyMaterials.branchKeyVersion);
    var newActiveVersionEast :- expect UTF8.Decode(newActiveResultEast.branchKeyMaterials.branchKeyVersion);
    expect newActiveVersionWest == newActiveVersionEast;

    // Since this process uses a read DDB table,
    // the number of records will forever increase.
    // To avoid this, remove the items.
    CleanupItems.DeleteVersion(branchKeyId.branchKeyIdentifier, newActiveVersionEast, ddbClient);
    CleanupItems.DeleteVersion(branchKeyId.branchKeyIdentifier, oldActiveVersion, ddbClient);
    CleanupItems.DeleteActive(branchKeyId.branchKeyIdentifier, ddbClient);

    // We expect that getting the old active key has the same version as getting a branch key through the get version key api
    expect getBranchKeyVersionResultEast.branchKeyMaterials.branchKeyVersion == oldActiveResult.branchKeyMaterials.branchKeyVersion;
    expect getBranchKeyVersionResultEast.branchKeyMaterials.branchKey == oldActiveResult.branchKeyMaterials.branchKey;
    // We expect that if we rotate the branch key, the returned materials MUST NOT be equal to the previous active key.
    expect getBranchKeyVersionResultEast.branchKeyMaterials.branchKeyVersion != newActiveResultEast.branchKeyMaterials.branchKeyVersion;
    expect getBranchKeyVersionResultEast.branchKeyMaterials.branchKey != newActiveResultEast.branchKeyMaterials.branchKey;
  }

  //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
  //= type=TODO
  //# The `kms-arn` field of DDB response item MUST be [compatible with](#aws-key-arn-compatibility)
  //# the configured `KMS ARN` in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.

  method {:test} {:vcs_split_on_every_assert} InsertingADuplicateVersionWillFail()
  {
    assume {:axiom} false;
    var ddbClient :- expect DDB.DynamoDBClient();

    expect 0 < |branchKeyId|;
    expect 0 < |branchKeyIdActiveVersion|;
    var customEncryptionContext: map<string, string> := map[];
    expect forall k <- customEncryptionContext :: ComAmazonawsDynamodbTypes.IsValid_AttributeName(Structure.ENCRYPTION_CONTEXT_PREFIX + k);

    var encryptionContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
      branchKeyId,
      branchKeyIdActiveVersion,
      "",
      "",
      keyArn,
      Types.HierarchyVersion.v1,
      map[]
    );

    expect ComAmazonawsDynamodbTypes.IsValid_TableName(branchKeyStoreName);
    var myBranchKeyStoreName : ComAmazonawsDynamodbTypes.TableName := branchKeyStoreName;
    var versionBranchKeyItem : Structure.VersionBranchKeyItem := Structure.ToAttributeMap(encryptionContext, [1]);
    var activeBranchKeyItem : Structure.ActiveBranchKeyItem := Structure.ToAttributeMap(Structure.ActiveBranchKeyEncryptionContext(encryptionContext), [2]);
    expect activeBranchKeyItem[Structure.BRANCH_KEY_IDENTIFIER_FIELD] == versionBranchKeyItem[Structure.BRANCH_KEY_IDENTIFIER_FIELD];
    expect activeBranchKeyItem[Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD] == versionBranchKeyItem[Structure.TYPE_FIELD];

    var output := DDBKeystoreOperations.WriteNewBranchKeyVersionToKeystore(
      versionBranchKeyItem,
      activeBranchKeyItem,
      myBranchKeyStoreName,
      ddbClient
    );

    expect output.Failure?;
  }

  method {:test} {:vcs_split_on_every_assert} VersioningANonexistentBranchKeyWillFail()
  {
    assume {:axiom} false;
    var ddbClient :- expect DDB.DynamoDBClient();

    var encryptionContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
      "!= branchKeyId",
      branchKeyIdActiveVersion,
      "",
      "",
      keyArn,
      Types.HierarchyVersion.v1,
      map[]
    );

    var versionBranchKeyItem : Structure.VersionBranchKeyItem := Structure.ToAttributeMap(encryptionContext, [1]);
    var activeBranchKeyItem : Structure.ActiveBranchKeyItem := Structure.ToAttributeMap(Structure.ActiveBranchKeyEncryptionContext(encryptionContext), [2]);
    expect activeBranchKeyItem[Structure.BRANCH_KEY_IDENTIFIER_FIELD] == versionBranchKeyItem[Structure.BRANCH_KEY_IDENTIFIER_FIELD];
    expect activeBranchKeyItem[Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD] == versionBranchKeyItem[Structure.TYPE_FIELD];
    expect ComAmazonawsDynamodbTypes.IsValid_TableName(branchKeyStoreName);
    var myBranchKeyStoreName : ComAmazonawsDynamodbTypes.TableName := branchKeyStoreName;

    var output := DDBKeystoreOperations.WriteNewBranchKeyVersionToKeystore(
      versionBranchKeyItem,
      activeBranchKeyItem,
      myBranchKeyStoreName,
      ddbClient
    );

    expect output.Failure?;
  }

}
