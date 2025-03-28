// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"
include "CleanupItems.dfy"

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

  /*
    // If you need to re-create the MRK Branch Keys
  
    method {:test} TestCreateMRK()
    {
      var ddbClient :- expect DDB.DynamoDBClient();
  
      var keyStoreConfigEast := Types.KeyStoreConfig(
        id := None,
        kmsConfiguration := KmsConfigEast,
        logicalKeyStoreName := logicalKeyStoreName,
        grantTokens := None,
        ddbTableName := branchKeyStoreName,
        ddbClient := Some(ddbClient)
      );
  
      var keyStoreConfigWest := Types.KeyStoreConfig(
        id := None,
        kmsConfiguration := KmsConfigWest,
        logicalKeyStoreName := logicalKeyStoreName,
        grantTokens := None,
        ddbTableName := branchKeyStoreName,
        ddbClient := Some(ddbClient)
      );
  
      var keyStoreEast :- expect KeyStore.KeyStore(keyStoreConfigEast);
      var keyStoreWest :- expect KeyStore.KeyStore(keyStoreConfigWest);
  
      var branchKeyIdWest :- expect keyStoreWest.CreateKey(Types.CreateKeyInput(
                                                             branchKeyIdentifier := Some(WestBranchKey),
                                                             encryptionContext := Some(KmsMrkEC)
                                                           ));
  
      var branchKeyIdEast :- expect keyStoreEast.CreateKey(Types.CreateKeyInput(
                                                             branchKeyIdentifier := Some(EastBranchKey),
                                                             encryptionContext := Some(KmsMrkEC)
                                                           ));
  
      expect branchKeyIdEast.branchKeyIdentifier == EastBranchKey;
      expect branchKeyIdWest.branchKeyIdentifier == WestBranchKey;
    }
  */

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

    var encryptedActive :- expect keyStore.config.storage.GetEncryptedActiveBranchKey(
      Types.GetEncryptedActiveBranchKeyInput(
        Identifier := branchKeyId.branchKeyIdentifier
      )
    );

    var encryptedVersion :- expect keyStore.config.storage.GetEncryptedBranchKeyVersion(
      Types.GetEncryptedBranchKeyVersionInput(
        Identifier := branchKeyId.branchKeyIdentifier,
        Version := encryptedActive.Item.Type.ActiveHierarchicalSymmetricVersion.Version
      )
    );

    var encryptedBeacon :- expect keyStore.config.storage.GetEncryptedBeaconKey(
      Types.GetEncryptedBeaconKeyInput(
        Identifier := branchKeyId.branchKeyIdentifier
      )
    );

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //= type=test
    //# This timestamp MUST be in ISO 8601 format in UTC, to microsecond precision (e.g. “YYYY-MM-DDTHH:mm:ss.ssssssZ“)
    expect ISO8601?(encryptedActive.Item.CreateTime);
    expect ISO8601?(encryptedVersion.Item.CreateTime);
    expect ISO8601?(encryptedBeacon.Item.CreateTime);

    // Since this process uses a read DDB table,
    // the number of records will forever increase.
    // To avoid this, remove the items.
    var _ := CleanupItems.DeleteBranchKey(Identifier:=branchKeyId.branchKeyIdentifier, ddbClient:=ddbClient);

    expect beaconKeyResult.beaconKeyMaterials.beaconKey.Some?;
    expect |beaconKeyResult.beaconKeyMaterials.beaconKey.value| == 32;
    expect |activeResult.branchKeyMaterials.branchKey| == 32;
    expect versionResult.branchKeyMaterials.branchKey == activeResult.branchKeyMaterials.branchKey;
    expect versionResult.branchKeyMaterials.branchKeyIdentifier
        == activeResult.branchKeyMaterials.branchKeyIdentifier
        == beaconKeyResult.beaconKeyMaterials.beaconKeyIdentifier;
    expect versionResult.branchKeyMaterials.branchKeyVersion == activeResult.branchKeyMaterials.branchKeyVersion;

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=test
    //# If no branch key id is provided,
    //# then this operation MUST create a [version 4 UUID](https://www.ietf.org/rfc/rfc4122.txt)
    //# to be used as the branch key id.
    var idByteUUID :- expect UUID.ToByteArray(activeResult.branchKeyMaterials.branchKeyIdentifier);
    var idRoundTrip :- expect UUID.FromByteArray(idByteUUID);
    expect idRoundTrip == activeResult.branchKeyMaterials.branchKeyIdentifier;


    //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //= type=test
    //# This guid MUST be [version 4 UUID](https://www.ietf.org/rfc/rfc4122.txt)
    var versionString :- expect UTF8.Decode(activeResult.branchKeyMaterials.branchKeyVersion);
    var versionByteUUID :- expect UUID.ToByteArray(versionString);
    var versionRoundTrip :- expect UUID.FromByteArray(versionByteUUID);
    expect versionRoundTrip == versionString;

  }

  lemma ISO8601Test()
  {
    assert ISO8601?("2024-08-06T17:23:25.000874Z");
  }

  predicate ISO8601?(
    CreateTime: string
  )
  {
    // “YYYY-MM-DDTHH:mm:ss.ssssssZ“
    && |CreateTime| == 27
    && CreateTime[4] == '-'
    && CreateTime[7] == '-'
    && CreateTime[10] == 'T'
    && CreateTime[13] == ':'
    && CreateTime[16] == ':'
    && CreateTime[19] == '.'
    && CreateTime[26] == 'Z'
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
