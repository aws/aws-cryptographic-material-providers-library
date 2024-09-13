// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../../../StandardLibrary/src/Index.dfy"
include "../src/Index.dfy"

module Fixtures {
  import opened StandardLibrary.UInt
  import Types = AwsCryptographyKeyStoreTypes
  import DDB = Types.ComAmazonawsDynamodbTypes
  import DDBOperations = Com.Amazonaws.Dynamodb
  import DefaultEncryptedKeyStore
  import UTF8
  import opened Wrappers

  method EncodeEncryptionContext(
    input: map<string,string>
  )
    returns (output: Result<Types.EncryptionContext, string>)
  {
    var encodedEncryptionContext
      := set k <- input
      ::
        (UTF8.Encode(k), UTF8.Encode(input[k]), k);
    :- Need(forall i <- encodedEncryptionContext
              ::
                && i.0.Success?
                && i.1.Success?
                && var encoded := UTF8.Decode(i.0.value);
                && encoded.Success?
                && i.2 == encoded.value
           ,
            "Unable to encode string");

    output := Success(map i <- encodedEncryptionContext :: i.0.value := i.1.value);
  }

  method DecodeEncryptionContext(input : Types.EncryptionContext)
    returns (output: Result<map<string,string>, string>)
  {
    var decodedEncryptionContext
      := set k <- input
      ::
        (UTF8.Decode(k), UTF8.Decode(input[k]), k);
    :- Need(forall i <- decodedEncryptionContext
              ::
                && i.0.Success?
                && i.1.Success?
                && var decoded := UTF8.Encode(i.0.value);
                && decoded.Success?
                && i.2 == decoded.value
           ,
            "Unable to decode string");

    output := Success(map i <- decodedEncryptionContext :: i.0.value := i.1.value);
  }


  // The following are test resources that exist in tests accounts:

  const branchKeyStoreName := "KeyStoreDdbTable"
  const logicalKeyStoreName := branchKeyStoreName
  const branchKeyId := "75789115-1deb-4fe3-a2ec-be9e885d1945"
  const branchKeyIdActiveVersion := "fed7ad33-0774-4f97-aa5e-6c766fc8af9f"

  const branchKeyIdWithEC := "4bb57643-07c1-419e-92ad-0df0df149d7c"
  // This is branchKeyIdActiveVersion above, as utf8bytes
  const branchKeyIdActiveVersionUtf8Bytes: seq<uint8> := [
    102, 101, 100, 55,  97, 100,  51, 51,  45,
    48,  55,  55, 52,  45,  52, 102, 57,  55,
    45,  97,  97, 53, 101,  45,  54, 99,  55,
    54,  54, 102, 99,  56,  97, 102, 57, 102
  ]
  // THESE ARE TESTING RESOURCES DO NOT USE IN A PRODUCTION ENVIRONMENT
  const keyArn := "arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126"
  const keyId := "9d989aa2-2f9c-438c-a745-cc57d3ad0126"

  // mrkRsaKeyArn is an RSA Key
  const mrkRsaKeyArn := "arn:aws:kms:us-west-2:370957321024:key/mrk-63d386cb70614ea59b32ad65c9315297"

  const MrkArnEast : string := "arn:aws:kms:us-east-1:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7"
  const MrkArnWest : string := "arn:aws:kms:us-west-2:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7"
  // Key MUST NOT exist in ap-south-2
  const MrkArnAP : string := "arn:aws:kms:ap-south-2:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7"
  const KmsConfigEast : Types.KMSConfiguration := Types.KMSConfiguration.kmsKeyArn(MrkArnEast)
  const KmsConfigWest : Types.KMSConfiguration := Types.KMSConfiguration.kmsKeyArn(MrkArnWest)
  const KmsMrkConfigEast : Types.KMSConfiguration := Types.KMSConfiguration.kmsMRKeyArn(MrkArnEast)
  const KmsMrkConfigWest : Types.KMSConfiguration := Types.KMSConfiguration.kmsMRKeyArn(MrkArnWest)
  const KmsSrkConfigEast : Types.KMSConfiguration := Types.KMSConfiguration.kmsKeyArn(MrkArnEast)
  const KmsSrkConfigWest : Types.KMSConfiguration := Types.KMSConfiguration.kmsKeyArn(MrkArnWest)
  const KmsMrkConfigAP : Types.KMSConfiguration := Types.KMSConfiguration.kmsMRKeyArn(MrkArnAP)
  const KmsMrkEC : Types.EncryptionContext := map[UTF8.EncodeAscii("abc") := UTF8.EncodeAscii("123")]
  const EastBranchKey : string := "MyEastBranch2"
  const WestBranchKey : string := "MyWestBranch2"
  const publicKeyArn := "arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"

  // TODO: After ~2024/06/11 launch, add the next two lines to cfn/ESDK-Hierarchy-CI.yaml
  const postalHornKeyArn := "arn:aws:kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8"
  const kmsKeyAlias := "arn:aws:kms:us-west-2:370957321024:alias/postalHorn"
  const postalHornBranchKeyId := "682dfba7-4c35-491d-8d6a-5a9c56194061"
  const postalHornBranchKeyActiveVersion := "6b7a8ef4-8c1c-4f63-b196-a6ef7e496e50"

  // Creation of this particular illegal Branch Key is detailed here:
  // `git rev-parse --show-toplevel`/cfn/lyingBranchKeyCreation.md
  const lyingBranchKeyId := "kms-arn-attribute-is-lying"
  const lyingBranchKeyDecryptOnlyVersion := "129c5c87-308a-41c9-8b9d-a27f66e915f4"

  // The Key Store will consider this mutation lock invalid
  // The Storage layer will not.
  // const mutationLockBranchKeyId := "test-get-items-for-initialize-mutation"

  method {:opaque} defaultStorage(
    nameonly tableName: string := branchKeyStoreName,
    nameonly logicalName: string := logicalKeyStoreName,
    nameonly ddbClient?: Option<DDB.IDynamoDBClient> := None
  )
    returns (output: Result<Types.IEncryptedKeyStore, DDB.Error>)
    requires DDB.IsValid_TableName(tableName)
    ensures output.Success?
            ==> output.value.ValidState() && output.value.Modifies == {}
  {
    var ddbClient: DDB.IDynamoDBClient;  //:- DDBOperations.DynamoDBClient();
    if (ddbClient?.None?) {
      ddbClient :- DDBOperations.DynamoDBClient();
    } else {
      ddbClient := ddbClient?.value;
    }
    assume {:axiom} ddbClient.Modifies == {} && ddbClient.ValidState();
    var underTest := new DefaultEncryptedKeyStore.DynamoDBEncryptedKeyStore(
      ddbTableName := tableName,
      ddbClient := ddbClient,
      logicalKeyStoreName := logicalName);
    // We may not need this, but **Oh My God** does it make verification go faster
    assume {:axiom} underTest.Modifies == {} && ddbClient.Modifies == {} && ddbClient.ValidState() && underTest.ValidState();
    output := Success(underTest);
  }

  datatype allThree = | allThree (
    active: Types.EncryptedHierarchicalKey,
    beacon: Types.EncryptedHierarchicalKey,
    decrypt: Types.EncryptedHierarchicalKey)

  method getItems(
    nameonly id: string,
    nameonly version: string,
    nameonly underTest: Types.IEncryptedKeyStore
  )
    returns (output: Result<allThree, Types.Error>)
    requires underTest.ValidState()
    ensures underTest.ValidState()
    modifies underTest.Modifies
  {
    var activeInput := Types.GetActiveInput(
      Identifier := id
    );
    var active? :- expect underTest.GetActive(activeInput);
    var active := active?.Item;

    var beaconInput := Types.GetBeaconInput(
      Identifier := id
    );
    var beacon? :- expect underTest.GetBeacon(beaconInput);
    var beacon := beacon?.Item;

    var decryptInput := Types.GetVersionInput(
      Identifier := id,
      Version := version
    );
    var decrypt? :- expect underTest.GetVersion(decryptInput);
    var decrypt := decrypt?.Item;
    output := Success(allThree(active, beacon, decrypt));
  }
}
