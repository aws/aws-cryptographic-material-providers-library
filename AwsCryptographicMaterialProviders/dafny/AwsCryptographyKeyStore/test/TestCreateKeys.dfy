// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"
include "CleanupItems.dfy"
include "TestGetKeys.dfy"

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
  import TestGetKeys

  const happyCaseId := "test-happy-case-create-key-hv-1"

  method {:test} {:isolate_assertions} TestCreateMRKForHV1()
  {
    var ddbClient :- expect DDB.DynamoDBClient();

    var keyStoreConfigEast := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := KmsConfigEast,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := branchKeyStoreName,
            ddbClient := Some(ddbClient)
          )))
    );

    var keyStoreConfigWest := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := KmsConfigWest,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := branchKeyStoreName,
            ddbClient := Some(ddbClient)
          )))
    );

    // Create key with Custom EC & Branch Key Identifier
    var uuid :- expect UUID.GenerateUUID();
    var branchKeyIdWest := happyCaseId + "-" + "west" + "-" + uuid;
    // print branchKeyIdWest;
    var branchKeyIdEast := happyCaseId + "-" + "east" + "-" + uuid;
    // print branchKeyIdEast;

    var keyStoreEast :- expect KeyStore.KeyStore(keyStoreConfigEast);
    var keyStoreWest :- expect KeyStore.KeyStore(keyStoreConfigWest);

    var branchKeyIdWest? :- expect keyStoreWest.CreateKey(Types.CreateKeyInput(
                                                            branchKeyIdentifier := Some(branchKeyIdWest),
                                                            encryptionContext := Some(KmsMrkEC)
                                                          ));

    var branchKeyIdEast? :- expect keyStoreEast.CreateKey(Types.CreateKeyInput(
                                                            branchKeyIdentifier := Some(branchKeyIdEast),
                                                            encryptionContext := Some(KmsMrkEC)
                                                          ));

    expect branchKeyIdEast?.branchKeyIdentifier == branchKeyIdEast;
    expect branchKeyIdWest?.branchKeyIdentifier == branchKeyIdWest;

    var _ := CleanupItems.DeleteBranchKey(Identifier:=branchKeyIdWest, ddbClient:=ddbClient);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=branchKeyIdEast, ddbClient:=ddbClient);
  }

  method {:test} TestCreateBranchAndBeaconKeys()
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

    var branchKeyId :- expect keyStore.CreateKey(Types.CreateKeyInput(
                                                   branchKeyIdentifier := None,
                                                   encryptionContext := None
                                                 ));

    // Get branch key items from storage
    TestGetKeys.VerifyGetKeys(
      identifier := branchKeyId.branchKeyIdentifier,
      keyStore := keyStore,
      storage := keyStore.config.storage
    );

    // Since this process uses a read DDB table,
    // the number of records will forever increase.
    // To avoid this, remove the items.
    var _ := CleanupItems.DeleteBranchKey(Identifier:=branchKeyId.branchKeyIdentifier, ddbClient:=ddbClient);
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
