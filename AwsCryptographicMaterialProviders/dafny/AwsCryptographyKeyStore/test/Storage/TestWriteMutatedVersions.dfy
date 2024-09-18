// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Fixtures.dfy"
include "../CleanupItems.dfy"

module {:options "/functionSyntax:4"} TestWriteMutatedVersions {
  import Fixtures
  import UInt = Fixtures.UInt
  import Types = Fixtures.Types
  import UTF8 = Fixtures.UTF8
  import DDB = Com.Amazonaws.Dynamodb
  import KMS = Com.Amazonaws.Kms
  import Time
  import CleanupItems
  import opened Wrappers
  import String = StandardLibrary.String
  import opened Seq
  import Structure
  import KeyStore
  import UUID

  const ddbTableName: DDB.Types.TableName := Fixtures.branchKeyStoreName
  const logicalKeyStoreName := Fixtures.logicalKeyStoreName
  const happyCaseId := "test-write-mutated-items"
  const original := UTF8.EncodeAscii("storage-does-not-validate-original-only-that-is-binary")
  const terminal := UTF8.EncodeAscii("storage-does-not-validate-terminal-only-that-is-binary")

  method {:test} TestHappyCase()
  {
    print " running";
    var ddbClient :- expect DDB.DynamoDBClient();
    var underTest :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var uuid :- expect UUID.GenerateUUID();
    var testId := happyCaseId + "-" + uuid;
    CreateHappyCaseId(testId);

    print "\nTestWriteMutatedVersions :: TestHappyCase :: Created the test items! testId: "
          + testId  +  "\n";
    var inputQuery := Types.QueryForVersionsInput(
      Identifier := testId,
      pageSize := 24
    );
    assume {:axiom} underTest.Modifies == {}; // Turns off verification, but allows calling underTest
    var queryOut :- expect underTest.QueryForVersions(inputQuery);
    var items := queryOut.items;
    expect
      |items| == 4,
      "Test expects there to be 4 Decrypt Only items! Found: " + String.Base10Int2String(|items|);
    print "\nTestWriteMutatedVersions :: TestHappyCase :: Read the test items! testId: "
          + testId  +  "\n";

    var timestamp :- expect Time.GetCurrentTimeStamp();
    var mutatedItems: Types.EncryptedHierarchicalKeys := [];
    var itemIndex := 0;
    while itemIndex < |items|
    {
      var item := items[itemIndex];
      expect
        "aws-crypto-ec:Robbie" in item.EncryptionContext,
                                  "Robbie should be a Key in the Custom Encryption Context of all items for this test.";
      var temp := item.EncryptionContext["aws-crypto-ec:Robbie" := timestamp];
      expect Structure.BranchKeyContext?(temp);
      var newItem := Structure.ConstructEncryptedHierarchicalKey(temp, item.CiphertextBlob);
      mutatedItems := mutatedItems + [newItem];
      itemIndex := 1 + itemIndex;
    }

    var input := Types.WriteMutatedVersionsInput(
      items := mutatedItems,
      Identifier := testId,
      Original := original,
      Terminal := terminal,
      CompleteMutation := false
    );

    var output :- expect underTest.WriteMutatedVersions(input);
    print "\nTestWriteMutatedVersions :: TestHappyCase :: Wrote the \"mutated\" test items! testId: "
          + testId  +  "\n";

    queryOut :- expect underTest.QueryForVersions(inputQuery);
    items := queryOut.items;
    print "\nTestWriteMutatedVersions :: TestHappyCase :: Read the \"mutated\" test items! testId: "
          + testId  +  "\n";
    itemIndex := 0;
    while itemIndex < |items|
    {
      var item := items[itemIndex];
      expect
        "aws-crypto-ec:Robbie" in item.EncryptionContext,
                                  "Robbie should be a Key in the Custom Encryption Context of all items for this test.";
      expect
        item.EncryptionContext["aws-crypto-ec:Robbie"] == timestamp,
        "Robbie should be a Key in the Custom Encryption Context of all items for this test.";
      // This is a best effort
      expect Structure.TYPE_FIELD in item.EncryptionContext;
      var _ := CleanupItems.DeleteTypeWithFailure(testId, item.EncryptionContext[Structure.TYPE_FIELD], ddbClient);
      itemIndex := 1 + itemIndex;
    }
    expect
      itemIndex == 4,
      "There should have been 4 mutated items!";
    print "\nTestWriteMutatedVersions :: TestHappyCase :: Validated and tried to delete the read \"mutated\" test items! testId: "
          + testId  +  "\n";
    // This is all a best effort; let's hope we don't run out of UUIDs!
    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BRANCH_KEY_ACTIVE_TYPE, ddbClient);
    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BEACON_KEY_TYPE_VALUE, ddbClient);
    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.MUTATION_LOCK_TYPE, ddbClient);
    print "\nTestWriteMutatedVersions :: TestHappyCase :: Tried to Delete the other items. testId: "
          + testId  +  "\n";
    print "TestWriteMutatedVersions.TestHappyCase: ";
  }

  method {:opaque} CreateHappyCaseId(
    id: string,
    ddbClient?: Option<DDB.Types.IDynamoDBClient> := None
  )
  {
    var ddbClient: DDB.Types.IDynamoDBClient;  //:- DDBOperations.DynamoDBClient();
    if (ddbClient?.None?) {
      ddbClient :- expect DDB.DynamoDBClient();
    } else {
      ddbClient := ddbClient?.value;
    }
    assume {:axiom} ddbClient.Modifies == {} && ddbClient.ValidState();
    var kmsClient :- expect KMS.KMSClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(Fixtures.keyArn);
    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := ddbTableName,
            ddbClient := Some(ddbClient)
          ))),
      keyManagement := Some(
        Types.kms(
          Types.AwsKms(
            kmsClient := Some(kmsClient)
          )))
    );
    // We may not need this, but **Oh My God** does it make verification go faster
    assume {:axiom} kmsClient.Modifies == {} && ddbClient.Modifies == {} && ddbClient.ValidState() && kmsClient.ValidState();
    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
    assume {:axiom} keyStore.Modifies == {} == kmsClient.Modifies == ddbClient.Modifies && keyStore.ValidState();

    var input := Types.CreateKeyInput(
      branchKeyIdentifier := Some(id),
      encryptionContext := Some(map[UTF8.EncodeAscii("Robbie") := UTF8.EncodeAscii("Is a dog.")])
    );
    var branchKeyId :- expect keyStore.CreateKey(input);

    // If you need a new version

    var inputV := Types.VersionKeyInput(
      branchKeyIdentifier := id
    );
    var _ :- expect keyStore.VersionKey(inputV);
    var _ :- expect keyStore.VersionKey(inputV);
    var _ :- expect keyStore.VersionKey(inputV);

    var item: DDB.Types.PutItemInputAttributeMap :=
      map[
        "type":=DDB.Types.AttributeValue.S(Structure.MUTATION_LOCK_TYPE),
        Structure.HIERARCHY_VERSION := DDB.Types.AttributeValue.N("1"),
        Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.Types.AttributeValue.S(id),
        Structure.KEY_CREATE_TIME :=  DDB.Types.AttributeValue.S("now!"),
        Structure.M_LOCK_UUID := DDB.Types.AttributeValue.S("this-is-not-a-uuid-but-storage-does-not-validate-this"),
        Structure.M_LOCK_ORIGINAL := DDB.Types.AttributeValue.B(UTF8.EncodeAscii("storage-does-not-validate-original-only-that-is-binary")),
        Structure.M_LOCK_TERMINAL := DDB.Types.AttributeValue.B(UTF8.EncodeAscii("storage-does-not-validate-terminal-only-that-is-binary"))
      ];
    var inputPut := DDB.Types.PutItemInput(TableName := ddbTableName, Item := item);
    assume {:axiom} ddbClient.Modifies == {} && ddbClient.ValidState();
    var _ :- expect ddbClient.PutItem(inputPut);
  }

}
