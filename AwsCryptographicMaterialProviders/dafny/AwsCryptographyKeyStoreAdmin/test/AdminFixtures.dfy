// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"

module {:options "/functionSyntax:4" } AdminFixtures {
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import KeyStoreAdmin
  import KeyStore
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import opened Wrappers
  import Fixtures
  import UTF8 = Fixtures.UTF8
  import DefaultKeyStorageInterface
  import Structure

  method DefaultAdmin(
    nameonly physicalName: string := Fixtures.branchKeyStoreName,
    nameonly logicalName: string := Fixtures.logicalKeyStoreName,
    nameonly ddbClient?: Option<DDB.Types.IDynamoDBClient> := None
  )
    returns (output: Result<Types.IKeyStoreAdminClient, Types.Error>)
    requires DDB.Types.IsValid_TableName(physicalName)
    ensures output.Success? ==> output.value.ValidState()
    requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
    modifies (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
    requires UTF8.IsASCIIString(physicalName) && UTF8.IsASCIIString(logicalName)
  {
    var ddbClient: DDB.Types.IDynamoDBClient;
    if (ddbClient?.None?) {
      ddbClient :- expect DDB.DynamoDBClient();
    } else {
      ddbClient := ddbClient?.value;
    }
    var physicalNameUtf8 :- expect UTF8.Encode(physicalName);
    var logicalNameUtf8 :- expect UTF8.Encode(logicalName);
    var storage := new DefaultKeyStorageInterface.DynamoDBKeyStorageInterface(
      ddbTableName := physicalName,
      ddbClient := ddbClient,
      logicalKeyStoreName := logicalName,
      ddbTableNameUtf8 := physicalNameUtf8,
      logicalKeyStoreNameUtf8 := logicalNameUtf8);

    var underTestConfig := Types.KeyStoreAdminConfig(
      logicalKeyStoreName := logicalName,
      storage := KeyStoreTypes.Storage.custom(storage));
    var underTest :- expect KeyStoreAdmin.KeyStoreAdmin(underTestConfig);
    // We may not need this, but **Oh My God** does it make verification go faster
    // assume {:axiom} underTest.Modifies == {} && ddbClient.Modifies == {} && ddbClient.ValidState() && underTest.ValidState();
    return Success(underTest);
  }

  method DefaultKeyManagerStrategy(
    nameonly kmsClient?: Option<KMS.Types.IKMSClient> := None
  )
    returns (output: Result<Types.KeyManagementStrategy, Types.Error>)
    requires kmsClient?.Some? ==> kmsClient?.value.ValidState()
    ensures output.Success? ==>
              && output.value.AwsKmsReEncrypt?
              && output.value.AwsKmsReEncrypt.kmsClient.Some?
              && output.value.AwsKmsReEncrypt.kmsClient.value.ValidState()
  {
    var kmsClient: KMS.Types.IKMSClient;
    if (kmsClient?.None?) {
      kmsClient :- expect KMS.KMSClient();
    } else {
      kmsClient := kmsClient?.value;
    }
    var strategy := Types.KeyManagementStrategy.AwsKmsReEncrypt(
      KeyStoreTypes.AwsKms(
        grantTokens := None,
        kmsClient := Some(kmsClient)
      ));
    return Success(strategy);
  }

  method DefaultKeyStore(
    nameonly kmsId: string := Fixtures.keyArn,
    nameonly physicalName: string := Fixtures.branchKeyStoreName,
    nameonly logicalName: string := Fixtures.logicalKeyStoreName
  )
    returns (output: Result<KeyStoreTypes.IKeyStoreClient, Types.Error>)
    requires DDB.Types.IsValid_TableName(physicalName)
    requires KMS.Types.IsValid_KeyIdType(kmsId)
    ensures output.Success? ==> output.value.ValidState()
  {
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsClient :- expect KMS.KMSClient();
    var kmsConfig := KeyStoreTypes.KMSConfiguration.kmsKeyArn(kmsId);
    var keyStoreConfig := KeyStoreTypes.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalName,
      storage := Some(
        KeyStoreTypes.ddb(
          KeyStoreTypes.DynamoDBTable(
            ddbTableName := physicalName,
            ddbClient := Some(ddbClient)
          ))),
      keyManagement := Some(
        KeyStoreTypes.kms(
          KeyStoreTypes.AwsKms(
            kmsClient := Some(kmsClient)
          )))
    );
    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
    return Success(keyStore);
  }

  method CreateHappyCaseId(
    nameonly id: string,
    nameonly kmsId: string := Fixtures.keyArn,
    nameonly physicalName: string := Fixtures.branchKeyStoreName,
    nameonly logicalName: string := Fixtures.logicalKeyStoreName,
    nameonly versionCount: nat := 3,
    nameonly customEC: KeyStoreTypes.EncryptionContext := map[UTF8.EncodeAscii("Robbie") := UTF8.EncodeAscii("Is a dog.")]
  )
    requires DDB.Types.IsValid_TableName(physicalName)
    requires KMS.Types.IsValid_KeyIdType(kmsId)
    requires 0 <= versionCount <= 5
    requires 0 < |customEC| // requires some EC
  {
    var keyStore :- expect DefaultKeyStore(kmsId:=kmsId, physicalName:=physicalName, logicalName:=logicalName);
    assume {:axiom} keyStore.Modifies == {}; // Turns off Verification, but lets us use DefaultKeyStore
    var input := KeyStoreTypes.CreateKeyInput(
      branchKeyIdentifier := Some(id),
      encryptionContext := Some(customEC)
    );
    var branchKeyId :- expect keyStore.CreateKey(input);

    // If you need a new version
    var inputV := KeyStoreTypes.VersionKeyInput(
      branchKeyIdentifier := id
    );
    var versionIndex := 0;
    while versionIndex < versionCount {
      var _ :- expect keyStore.VersionKey(inputV);
      versionIndex := versionIndex + 1;
    }
  }

  method DefaultStorage(
    nameonly physicalName: string := Fixtures.branchKeyStoreName,
    nameonly logicalName: string := Fixtures.logicalKeyStoreName,
    nameonly ddbClient?: Option<DDB.Types.IDynamoDBClient> := None
  )
    returns (output: Result<KeyStoreTypes.IKeyStorageInterface, KeyStoreTypes.Error>)
    requires DDB.Types.IsValid_TableName(physicalName)
    requires UTF8.IsASCIIString(physicalName) && UTF8.IsASCIIString(logicalName)
    requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
    ensures output.Success? ==> output.value.ValidState()
    modifies (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
  {
    output := Fixtures.DefaultStorage(physicalName := physicalName, logicalName := logicalName, ddbClient? := ddbClient?);
  }

  datatype KmsDdbError =
    | ComAmazonawsDynamodb(ComAmazonawsDynamodb: DDB.Types.Error)
    | ComAmazonawsKms(ComAmazonawsKms: KMS.Types.Error)

  datatype KeyValue = KeyValue(
    key: string := "Robbie",
    value: string := "Is a dog.")

  method AddAttributeWithoutLibrary(
    nameonly id: string,
    nameonly physicalName: string := Fixtures.branchKeyStoreName,
    nameonly logicalName: string := Fixtures.logicalKeyStoreName,
    nameonly keyValue: KeyValue := KeyValue(key:="Robbie", value:="Is a dog."),
    nameonly alsoViolateBeacon?: bool := false,
    nameonly ddbClient?: Option<DDB.Types.IDynamoDBClient> := None
  )
    returns (output: Result<bool, KmsDdbError>)
    requires DDB.Types.IsValid_TableName(physicalName)
    requires UTF8.IsASCIIString(physicalName) && UTF8.IsASCIIString(logicalName)
    requires keyValue.key !in Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES
    requires DDB.Types.IsValid_AttributeName(keyValue.key)
    requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
    modifies (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
  {
    var ddbClient: DDB.Types.IDynamoDBClient;
    if (ddbClient?.None?) {
      ddbClient :- expect DDB.DynamoDBClient();
    } else {
      ddbClient := ddbClient?.value;
    }
    var kmsClient :- expect KMS.KMSClient();
    var storage :- expect Fixtures.DefaultStorage(
      physicalName := physicalName, logicalName := logicalName, ddbClient? := Some(ddbClient));

    // Recommend commenting this out while developing this method,
    // and just ignore the modifies exeptions,
    // and then re-enabling it once everything is safe
    assume {:axiom} storage.Modifies == {};

    var allThree :- expect Fixtures.getItems(id:=id, underTest:=storage);
    var activeDDB :- expect ViolateItem(
      item := allThree.active, keyValue:=keyValue, kmsClient:=kmsClient, physicalName:=physicalName);
    var decryptDDB :- expect ViolateItem(
      item := allThree.decrypt, keyValue:=keyValue, kmsClient:=kmsClient, physicalName:=physicalName);
    var TransactItems := [activeDDB, decryptDDB];

    if (alsoViolateBeacon?) {
      var beaconDDB :- expect ViolateItem(
        item := allThree.beacon, keyValue:=keyValue, kmsClient:=kmsClient, physicalName:=physicalName);
      TransactItems := TransactItems + [beaconDDB];
    }

    var ddbRequest := DDB.Types.TransactWriteItemsInput(TransactItems := TransactItems);
    var ddbRes :- expect ddbClient.TransactWriteItems(ddbRequest);
    return Success(true);
  }

  method ViolateItem(
    nameonly item: KeyStoreTypes.EncryptedHierarchicalKey,
    nameonly keyValue: KeyValue,
    nameonly kmsClient: KMS.Types.IKMSClient,
    nameonly physicalName: string := Fixtures.branchKeyStoreName
  )
    returns (ddbPutItem: Result<DDB.Types.TransactWriteItem, KmsDdbError>)
    requires kmsClient.ValidState()
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()
    requires keyValue.key !in Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES
    requires DDB.Types.IsValid_AttributeName(keyValue.key)
    requires DDB.Types.IsValid_TableName(physicalName)
  {
    assume {:axiom} KMS.Types.IsValid_CiphertextType(item.CiphertextBlob);
    assume {:axiom} KMS.Types.IsValid_KeyIdType(item.KmsArn);
    var aMap := map[keyValue.key := keyValue.value];
    expect keyValue.key !in item.EncryptionContext, "key of KeyValue cannot already be in EC";
    var violatedEC := item.EncryptionContext + aMap;
    expect Structure.BranchKeyContext?(violatedEC), "Library is too good and won't let Tony cheat";
    var reEncryptReq := KMS.Types.ReEncryptRequest(
      CiphertextBlob := item.CiphertextBlob,
      SourceEncryptionContext := Some(item.EncryptionContext),
      DestinationKeyId := item.KmsArn,
      DestinationEncryptionContext := Some(violatedEC));

    var reEncryptRes :- expect kmsClient.ReEncrypt(reEncryptReq);
    expect reEncryptRes.CiphertextBlob.Some?, "KMS did not return ciphertext.";

    var violated := Structure.ConstructEncryptedHierarchicalKey(
      violatedEC, reEncryptRes.CiphertextBlob.value);

    expect forall k <- violatedEC.Keys :: DDB.Types.IsValid_AttributeName(k), "How did an invalid DDB Attribute Name get here?";
    return Success(
        DDB.Types.TransactWriteItem(
          Put := Some(DDB.Types.Put(
                        Item := Structure.ToAttributeMap(violated),
                        TableName := physicalName))));
  }
}

