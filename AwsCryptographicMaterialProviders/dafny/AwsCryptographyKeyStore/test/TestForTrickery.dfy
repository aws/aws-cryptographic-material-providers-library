// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"
include "../src/Structure.dfy"
include "CleanupItems.dfy"

module TestForTrickery {
  import Types = AwsCryptographyKeyStoreTypes
  import ComAmazonawsKmsTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import DDBT = ComAmazonawsDynamodbTypes
  import KeyStore
  import opened Wrappers
  import opened Fixtures
  import Structure
  import UTF8
  import CleanupItems
  import DDBKeystoreOperations
  import UUID

  method {:test} TestUpdates()
  {
    TestErrorOnUpdate("stuff", "junk", None);
    TestErrorOnUpdate("stuff", "junk", Some(Types.HierarchyVersion.v1));
    TestErrorOnUpdate("stuff", "junk", Some(Types.HierarchyVersion.v2));

    TestErrorOnUpdate("hierarchy-version", "2", Some(Types.HierarchyVersion.v1));
    TestErrorOnUpdate("hierarchy-version", "1", Some(Types.HierarchyVersion.v2));

    TestErrorOnUpdate("hierarchy-version", "3", None);
    TestErrorOnUpdate("hierarchy-version", "3", Some(Types.HierarchyVersion.v1));
    TestErrorOnUpdate("hierarchy-version", "3", Some(Types.HierarchyVersion.v2));

    TestErrorOnUpdate("aws-crypto-ec:stuff", "junk", None);
    TestErrorOnUpdate("aws-crypto-ec:stuff", "junk", Some(Types.HierarchyVersion.v1));
    TestErrorOnUpdate("aws-crypto-ec:stuff", "junk", Some(Types.HierarchyVersion.v2));
  }

  method TestErrorOnUpdate(key : string, value : string, hierarchyVersion : Option<Types.HierarchyVersion>)
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);

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

    var branchKeyId :- expect keyStore.CreateKey(Types.CreateKeyInput(
                                                   branchKeyIdentifier := None,
                                                   encryptionContext := None,
                                                   hierarchyVersion := hierarchyVersion
                                                 ));

    var activeResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var _ := UpdateItem(ddbClient, branchKeyId.branchKeyIdentifier, "branch:ACTIVE", key, value);

    var activeError := keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));
    expect activeError.Failure?;

    var _ :- expect CleanupItems.DeleteBranchKey(Identifier := branchKeyId.branchKeyIdentifier, tableName := branchKeyStoreName, ddbClient := ddbClient);
  }

  method UpdateItem(ddb : DDBT.IDynamoDBClient, pk : string, sk : string, key : string, value : string) returns (output : DDBT.AttributeMap)
    requires ddb.ValidState()
    ensures ddb.ValidState()
    modifies ddb.Modifies
  {
    expect DDBT.IsValid_AttributeName(key);
    var input := DDBT.UpdateItemInput (
      TableName := branchKeyStoreName,
      Key :=  map["branch-key-id" := DDBT.AttributeValue.S(pk), "type" := DDBT.AttributeValue.S(sk)],
      UpdateExpression := Some("SET #key = :value"),
      ExpressionAttributeNames := Some(map["#key" := key]),
      ExpressionAttributeValues := Some(map[":value" := DDBT.AttributeValue.S(value)]),
      ReturnValues := Some(DDBT.ALL_NEW)
    );
    var update_result :- expect ddb.UpdateItem(input);
    expect update_result.Attributes.Some?;
    return update_result.Attributes.value;
  }
}

