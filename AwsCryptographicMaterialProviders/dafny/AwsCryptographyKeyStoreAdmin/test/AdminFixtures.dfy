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
    ensures output.Success?
            ==>
              && output.value.ValidState()
              && fresh(output.value)
              && fresh(output.value.Modifies)
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient(ddbClient?);
    assume {:axiom} fresh(ddbClient) && fresh(ddbClient.Modifies);
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
    modifies (if kmsClient?.Some? then kmsClient?.value.Modifies else {})
  {
    var kmsClient :- expect Fixtures.ProvideKMSClient(kmsClient?);
    assume {:axiom} fresh(kmsClient) && fresh(kmsClient.Modifies);
    var strategy := Types.KeyManagementStrategy.AwsKmsReEncrypt(
      KeyStoreTypes.AwsKms(
        grantTokens := None,
        kmsClient := Some(kmsClient)
      ));
    return Success(strategy);
  }

  datatype KmsDdbError =
    | ComAmazonawsDynamodb(ComAmazonawsDynamodb: DDB.Types.Error)
    | ComAmazonawsKms(ComAmazonawsKms: KMS.Types.Error)

  datatype KeyValue = KeyValue(
    key: string := "Robbie",
    value: string := "Is a dog.")

  /** Adds an "un-modeled Attribute" to the Active & Decrypt. */
  /** If alsoViolateBeacion?, also add to Beacon.*/
  method AddAttributeWithoutLibrary(
    nameonly id: string,
    nameonly physicalName: string := Fixtures.branchKeyStoreName,
    nameonly logicalName: string := Fixtures.logicalKeyStoreName,
    nameonly keyValue: KeyValue := KeyValue(key:="Robbie", value:="Is a dog."),
    nameonly alsoViolateBeacon?: bool := false,
    nameonly ddbClient?: Option<DDB.Types.IDynamoDBClient> := None,
    nameonly kmsClient?: Option<KMS.Types.IKMSClient> := None
  )
    returns (output: Result<bool, KmsDdbError>)
    requires DDB.Types.IsValid_TableName(physicalName)
    requires UTF8.IsASCIIString(physicalName) && UTF8.IsASCIIString(logicalName)
    requires keyValue.key !in Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES
    requires DDB.Types.IsValid_AttributeName(keyValue.key)
    requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
    modifies (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
             + (if kmsClient?.Some? then kmsClient?.value.Modifies else {})
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient(ddbClient?);
    var kmsClient :- expect Fixtures.ProvideKMSClient(None);
    var storage :- expect Fixtures.DefaultStorage(
      physicalName := physicalName, logicalName := logicalName, ddbClient? := Some(ddbClient));

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

