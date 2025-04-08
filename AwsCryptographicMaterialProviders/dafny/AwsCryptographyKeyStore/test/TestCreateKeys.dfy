// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"
include "CleanupItems.dfy"
include "BranchKeyValidators.dfy"


module {:options "/functionSyntax:4" } TestCreateKeys {
  import Types = AwsCryptographyKeyStoreTypes
  import ComAmazonawsKmsTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import KeyStore
  import opened Wrappers
  import opened Fixtures
  import UTF8
  import CleanupItems
  import Structure
  import DefaultKeyStorageInterface
  import KmsArn
  import UUID
  import AwsArnParsing
  import BranchKeyValidators

  const happyCaseId := "test-happy-case-create-key-hv-1"
  method {:test} TestCreateMRKForHV1()
  {
    var ddbClient :- expect DDB.DynamoDBClient();
    var storage :- expect DefaultStorage(ddbClient? := Some(ddbClient));
    var keyStoreEast :- expect KeyStoreFromKMSConfig(
      kmsConfig := KmsConfigEast,
      ddbClient? := Some(ddbClient)
    );
    var uuid :- expect UUID.GenerateUUID();
    var bkid := happyCaseId + "-east-mrk-" + uuid;
    var bk :- expect keyStoreEast.CreateKey(
      Types.CreateKeyInput(
        branchKeyIdentifier := Some(bkid),
        encryptionContext := Some(KmsMrkEC)
      ));
    expect bk.branchKeyIdentifier == bkid;
    BranchKeyValidators.VerifyGetKeys(bkid, keyStoreEast, storage,
                                      encryptionContext := KmsMrkEC);
    var keyStoreWest :- expect KeyStoreFromKMSConfig(
      // Passing in KmsMrkConfigWest causes the KMS Client to be created for us-west-2
      // EastBranchKey's KMS-ARN is replicated to us-west-2
      kmsConfig := KmsMrkConfigWest,
      ddbClient? := Some(ddbClient)
    );
    BranchKeyValidators.VerifyGetKeys(bkid, keyStoreWest, storage,
                                      encryptionContext := KmsMrkEC);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
  }

  method {:test} TestCreateSRKForHV1()
  {
    var ddbClient :- expect DDB.DynamoDBClient();
    var storage :- expect DefaultStorage(ddbClient? := Some(ddbClient));
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);
    var keyStore :- expect KeyStoreFromKMSConfig(
      kmsConfig := kmsConfig,
      ddbClient? := Some(ddbClient)
    );
    var uuid :- expect UUID.GenerateUUID();
    var bkid := happyCaseId + "-srk-" + uuid;
    var bk :- expect keyStore.CreateKey(
      Types.CreateKeyInput(
        branchKeyIdentifier := Some(bkid),
        encryptionContext := Some(KmsMrkEC)
      ));
    expect bk.branchKeyIdentifier == bkid;
    BranchKeyValidators.VerifyGetKeys(bkid, keyStore, storage,
                                      encryptionContext := KmsMrkEC);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
  }

  method {:test} TestCreateOptions()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);

    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := branchKeyStoreName,
            ddbClient := Some(ddbClient)
          ))),
      keyManagement := Some(
        Types.kms(
          Types.AwsKms(
            kmsClient := Some(kmsClient)
          )))
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    // Use a UUID so multiple tests can run :)
    var id :- expect UUID.GenerateUUID();

    var encryptionContext :- expect EncodeEncryptionContext(map[
                                                              "some" := "encryption",
                                                              "context" := "values"
                                                            ]);

    var branchKeyId :- expect keyStore.CreateKey(Types.CreateKeyInput(
                                                   branchKeyIdentifier := Some(id),
                                                   encryptionContext := Some(encryptionContext)
                                                 ));

    var beaconKeyResult :- expect keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var activeResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var branchKeyVersion :- expect UTF8.Decode(activeResult.branchKeyMaterials.branchKeyVersion);
    var versionResult :- expect keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier,
        branchKeyVersion := branchKeyVersion
      ));

    // Since this process uses a read DDB table,
    // the number of records will forever increase.
    // To avoid this, remove the items.
    var _ := CleanupItems.DeleteBranchKey(Identifier:=branchKeyId.branchKeyIdentifier, ddbClient:=ddbClient);

    expect id
        == versionResult.branchKeyMaterials.branchKeyIdentifier
        == activeResult.branchKeyMaterials.branchKeyIdentifier
        == beaconKeyResult.beaconKeyMaterials.beaconKeyIdentifier;

    expect encryptionContext
        == versionResult.branchKeyMaterials.encryptionContext
        == activeResult.branchKeyMaterials.encryptionContext
        == beaconKeyResult.beaconKeyMaterials.encryptionContext;

  }

  method {:test} TestCreateDuplicate()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);

    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := branchKeyStoreName,
            ddbClient := Some(ddbClient)
          ))),
      keyManagement := Some(
        Types.kms(
          Types.AwsKms(
            kmsClient := Some(kmsClient)
          )))
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var attempt := keyStore.CreateKey(
      Types.CreateKeyInput(
        branchKeyIdentifier := Some(branchKeyId),
        encryptionContext := None
      ));

    expect attempt.Failure?;
  }

  method {:test} InsertingADuplicateWillFail()
  {
    var ddbClient :- expect DDB.DynamoDBClient();
    var customEC := map[];

    expect 0 < |branchKeyId|;
    expect 0 < |branchKeyIdActiveVersion|;
    expect forall k <- customEC :: DDB.Types.IsValid_AttributeName(Structure.ENCRYPTION_CONTEXT_PREFIX + k);
    expect KMS.Types.IsValid_KeyIdType(keyArn);
    expect AwsArnParsing.ParseAwsKmsArn(keyArn).Success?;
    expect KmsArn.ValidKmsArn?(keyArn);

    var encryptionContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
      branchKeyId,
      branchKeyIdActiveVersion,
      "",
      "",
      keyArn,
      Types.HierarchyVersion.v1,
      customEC
    );
    var ddbTableNameUtf8 :- expect UTF8.Encode(branchKeyStoreName);
    var logicalKeyStoreNameUtf8 :- expect UTF8.Encode("");

    var storage := new DefaultKeyStorageInterface.DynamoDBKeyStorageInterface(
      ddbTableName := branchKeyStoreName,
      ddbClient := ddbClient,
      logicalKeyStoreName := "",
      ddbTableNameUtf8 := ddbTableNameUtf8,
      logicalKeyStoreNameUtf8 := logicalKeyStoreNameUtf8
    );

    var output := storage.WriteNewEncryptedBranchKey(
      Types.WriteNewEncryptedBranchKeyInput(
        Version := Structure.ConstructEncryptedHierarchicalKey(encryptionContext, [1]),
        Active := Structure.ConstructEncryptedHierarchicalKey(Structure.ActiveBranchKeyEncryptionContext(encryptionContext), [2]),
        Beacon := Structure.ConstructEncryptedHierarchicalKey(Structure.BeaconKeyEncryptionContext(encryptionContext), [2])
      )
    );

    expect output.Failure?;
  }

  method {:test} InsertingADuplicateWillWithADifferentVersionFail()
  {
    var ddbClient :- expect DDB.DynamoDBClient();
    var customEC := map[];

    expect 0 < |branchKeyId|;
    expect 0 < |branchKeyIdActiveVersion|;
    expect forall k <- customEC :: DDB.Types.IsValid_AttributeName(Structure.ENCRYPTION_CONTEXT_PREFIX + k);
    expect KMS.Types.IsValid_KeyIdType(keyArn);
    expect AwsArnParsing.ParseAwsKmsArn(keyArn).Success?;
    expect KmsArn.ValidKmsArn?(keyArn);

    var encryptionContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
      branchKeyId,
      "!= branchKeyIdActiveVersion",
      "",
      "",
      keyArn,
      Types.HierarchyVersion.v1,
      customEC
    );
    var ddbTableNameUtf8 :- expect UTF8.Encode(branchKeyStoreName);
    var logicalKeyStoreNameUtf8 :- expect UTF8.Encode("");

    var storage := new DefaultKeyStorageInterface.DynamoDBKeyStorageInterface(
      ddbTableName := branchKeyStoreName,
      ddbClient := ddbClient,
      logicalKeyStoreName := "",
      ddbTableNameUtf8 := ddbTableNameUtf8,
      logicalKeyStoreNameUtf8 := logicalKeyStoreNameUtf8
    );

    var output := storage.WriteNewEncryptedBranchKey(
      Types.WriteNewEncryptedBranchKeyInput(
        Version := Structure.ConstructEncryptedHierarchicalKey(encryptionContext, [1]),
        Active := Structure.ConstructEncryptedHierarchicalKey(Structure.ActiveBranchKeyEncryptionContext(encryptionContext), [2]),
        Beacon := Structure.ConstructEncryptedHierarchicalKey(Structure.BeaconKeyEncryptionContext(encryptionContext), [2])
      )
    );

    expect output.Failure?;
  }
}
