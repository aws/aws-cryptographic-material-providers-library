// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Fixtures.dfy"

module {:options "/functionSyntax:4"} TestGetItemsForInitializeMutation {
  import UInt = Fixtures.UInt
  import Types = Fixtures.Types
  import UTF8 = Fixtures.UTF8
  import opened Wrappers
  import DefaultEncryptedKeyStore
  import DDB = Types.ComAmazonawsDynamodbTypes
  import Fixtures
  import Structure
  import DDBOperations = Com.Amazonaws.Dynamodb
  import KMSOperations = Com.Amazonaws.Kms
  import KeyStore

  const ddbTableName: DDB.TableName := Fixtures.branchKeyStoreName
  const logicalKeyStoreName := Fixtures.logicalKeyStoreName
  // The Key Store will consider this mutation lock invalid
  // The Storage layer will not.
  const mLockedId := "test-get-items-for-initialize-mutation"

  method {:test} TestHappyCase()
  {
    var ddbClient: DDB.IDynamoDBClient :- expect DDBOperations.DynamoDBClient();
    var underTest := new DefaultEncryptedKeyStore.DynamoDBEncryptedKeyStore(
      ddbTableName := ddbTableName,
      ddbClient := ddbClient,
      logicalKeyStoreName := logicalKeyStoreName);
    var input := Types.GetItemsForInitializeMutationInput(
      Identifier := Fixtures.branchKeyId
    );
    assume {:axiom} underTest.Modifies == {} && ddbClient.Modifies == {} && ddbClient.ValidState() && underTest.ValidState();
    var output :- expect underTest.GetItemsForInitializeMutation(input);

    expect
      output.activeItem.Type.ActiveHierarchicalSymmetricVersion?,
      "activeItem was not Active? 'type': " + output.activeItem.EncryptionContext[Structure.TYPE_FIELD];
    expect
      output.beaconItem.Type.ActiveHierarchicalSymmetricBeacon?,
      "beaconItem was not Beacon? 'type': " + output.beaconItem.EncryptionContext[Structure.TYPE_FIELD];
    expect
      output.mutationLock.None?,
      "MutationLock was not None. 'UUID': " + output.mutationLock.value.UUID;
  }

  method {:test} TestHappyCaseMLocked()
  {
    var ddbClient: DDB.IDynamoDBClient :- expect DDBOperations.DynamoDBClient();
    var underTest := new DefaultEncryptedKeyStore.DynamoDBEncryptedKeyStore(
      ddbTableName := ddbTableName,
      ddbClient := ddbClient,
      logicalKeyStoreName := logicalKeyStoreName);
    var input := Types.GetItemsForInitializeMutationInput(
      Identifier := mLockedId
    );
    // We may not need this, but **Oh My God** does it make verification go faster
    assume {:axiom} underTest.Modifies == {} && ddbClient.Modifies == {} && ddbClient.ValidState() && underTest.ValidState();
    var output :- expect underTest.GetItemsForInitializeMutation(input);

    expect
      output.activeItem.Type.ActiveHierarchicalSymmetricVersion?,
      "activeItem was not Active? 'type': " + output.activeItem.EncryptionContext[Structure.TYPE_FIELD];
    expect
      output.beaconItem.Type.ActiveHierarchicalSymmetricBeacon?,
      "beaconItem was not Beacon? 'type': " + output.beaconItem.EncryptionContext[Structure.TYPE_FIELD];
    expect
      output.mutationLock.Some?,
      "MutationLock was not Some.";
  }


  // If you need to re-create the Mutation Lock case

  // method {:test} CreateMutationLockBranchKey()
  // {
  //   var kmsClient :- expect KMSOperations.KMSClient();
  //   var ddbClient :- expect DDBOperations.DynamoDBClient();
  //   var kmsConfig := Types.KMSConfiguration.kmsKeyArn(Fixtures.keyArn);
  //   var keyStoreConfig := Types.KeyStoreConfig(
  //     id := None,
  //     kmsConfiguration := kmsConfig,
  //     logicalKeyStoreName := logicalKeyStoreName,
  //     storage := Some(
  //       Types.ddb(
  //         Types.DynamoDBTable(
  //           ddbTableName := ddbTableName,
  //           ddbClient := Some(ddbClient)
  //         ))),
  //     keyManagement := Some(
  //       Types.kms(
  //         Types.AwsKms(
  //           kmsClient := Some(kmsClient)
  //         )))
  //   );
  //   // We may not need this, but **Oh My God** does it make verification go faster
  //   assume {:axiom} kmsClient.Modifies == {} && ddbClient.Modifies == {} && ddbClient.ValidState() && kmsClient.ValidState();
  //   var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
  //   assume {:axiom} keyStore.Modifies == {} == kmsClient.Modifies == ddbClient.Modifies && keyStore.ValidState();

  //   var input := Types.CreateKeyInput(
  //     // branchKeyIdentifier := Some(mLockedId),
  //     // branchKeyIdentifier := Some("test-write-and-delete-m-lock"),
  //     // branchKeyIdentifier := Some("test-query-for-versions"),
  //     branchKeyIdentifier := Some("test-write-mutated-items"),
  //     encryptionContext := Some(map[UTF8.EncodeAscii("Robbie") := UTF8.EncodeAscii("Is a dog.")])
  //   );
  //   var branchKeyId :- expect keyStore.CreateKey(input);

  //   // If you need a new version

  //   var inputV := Types.VersionKeyInput(
  //     // branchKeyIdentifier := "test-write-and-delete-m-lock"
  //     // branchKeyIdentifier := "test-query-for-versions"
  //     branchKeyIdentifier := "test-write-mutated-items"
  //   );
  //   var _ :- expect keyStore.VersionKey(inputV);
  //   var _ :- expect keyStore.VersionKey(inputV);
  //   var _ :- expect keyStore.VersionKey(inputV);
  // }

  // method {:test} CreateMLockManually()
  // {
  //   var item: DDB.PutItemInputAttributeMap :=
  //     map[
  //     "type":=DDB.AttributeValue.S(Structure.MUTATION_LOCK_TYPE),
  //     Structure.HIERARCHY_VERSION := DDB.AttributeValue.N("1"),
  //     Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S("test-write-mutated-items"),//mLockedId),
  //     Structure.KEY_CREATE_TIME :=  DDB.AttributeValue.S("now!"),
  //     Structure.M_LOCK_UUID := DDB.AttributeValue.S("this-is-not-a-uuid-but-storage-does-not-validate-this"),
  //     Structure.M_LOCK_ORIGINAL := DDB.AttributeValue.B(UTF8.EncodeAscii("storage-does-not-validate-original-only-that-is-binary")),
  //     Structure.M_LOCK_TERMINAL := DDB.AttributeValue.B(UTF8.EncodeAscii("storage-does-not-validate-terminal-only-that-is-binary"))
  //   ];
  //   var ddbClient :- expect DDBOperations.DynamoDBClient();
  //   var input := DDB.PutItemInput(TableName := ddbTableName, Item := item);
  //   assume {:axiom} ddbClient.Modifies == {} && ddbClient.ValidState();
  //   var output :- expect ddbClient.PutItem(input);
  // }
}
