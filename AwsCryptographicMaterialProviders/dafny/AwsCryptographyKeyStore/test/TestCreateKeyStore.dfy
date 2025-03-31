// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographicMaterialProviders/src/AwsArnParsing.dfy"
include "Fixtures.dfy"

module TestCreateKeyStore {
  import Types = AwsCryptographyKeyStoreTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import KeyStore
  import opened Wrappers
  import opened AwsArnParsing
  import opened Fixtures

  method {:test} TestCreateKeyStore()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);

    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := Some(branchKeyStoreName),
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
    // we are not actually creating a table in CI but testing we have configured a table
    // with the expected construction
    var keyStoreArn :- expect keyStore.CreateKeyStore(Types.CreateKeyStoreInput());

    expect AwsArnParsing.ParseAmazonDynamodbTableName(keyStoreArn.tableArn).Success?;
    expect AwsArnParsing.ParseAmazonDynamodbTableName(keyStoreArn.tableArn).value == branchKeyStoreName;
  }

  method {:test} TestCreateKeyStoreFail()
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
    // Because we are using the new interface this will fail.
    var keyStoreArn := keyStore.CreateKeyStore(Types.CreateKeyStoreInput());

    expect keyStoreArn.Failure?;

  }
}
