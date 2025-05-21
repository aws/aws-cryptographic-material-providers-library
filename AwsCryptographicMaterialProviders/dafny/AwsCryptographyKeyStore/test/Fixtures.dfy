// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../../../StandardLibrary/src/Index.dfy"
include "../src/Index.dfy"

module Fixtures {
  import opened StandardLibrary.UInt
  import Types = AwsCryptographyKeyStoreTypes
  import DDB = Com.Amazonaws.Dynamodb
  import KMS = Com.Amazonaws.Kms
  import DefaultKeyStorageInterface
  import UTF8
  import Seq
  import opened Wrappers
  import KeyStore
  import Structure

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

  // Python method for getting Dafny byte sequence
  // def as_dafny_bytes(string):
  //   return "[" +  ", ".join(["0x" + character.encode("utf-8").hex() for character in string]) + "]"
  const abc : UTF8.ValidUTF8Bytes :=
    var s := [0x61, 0x62, 0x63];
    assert s == UTF8.EncodeAscii("abc");
    s

  const x123 : UTF8.ValidUTF8Bytes :=
    var s := [0x31, 0x32, 0x33];
    assert s == UTF8.EncodeAscii("123");
    s

  // The following are test resources that exist in tests accounts:
  const branchKeyStoreName := "KeyStoreDdbTable"
  const logicalKeyStoreName := branchKeyStoreName
  // Static Key Store Names (This uses the same logical key store name as in branchKeyStoreName)
  const staticBranchKeyStoreName := "KeyStoreStaticTable"
  const staticLogicalKeyStoreName := branchKeyStoreName
  // hierarchy-version-1 branch key
  const branchKeyId := "3f43a9af-08c5-4317-b694-3d3e883dcaef"
  const branchKeyIdActiveVersion := "a4905627-4b7f-4272-a847-f50dae245737"
  // This is branchKeyIdActiveVersion above, as utf8bytes
  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Decimal('Comma',false)&input=YTQ5MDU2MjctNGI3Zi00MjcyLWE4NDctZjUwZGFlMjQ1NzM3&oenc=65001
  const branchKeyIdActiveVersionUtf8Bytes: seq<uint8> := [
    97, 52, 57, 48, 53, 54, 50, 55, 45, 52,
    98, 55, 102, 45, 52, 50, 55, 50, 45, 97,
    56, 52, 55, 45, 102, 53, 48, 100, 97, 101,
    50, 52, 53, 55, 51, 55
  ]
  const branchKeyIdWithEC := "4bb57643-07c1-419e-92ad-0df0df149d7c"
  // hierarchy-version-2 branch key
  const hv2BranchKeyId := "4a0c7b92-3703-4209-8961-24b07ab6562b"
  const hv2BranchKeyVersion := "a0496b5c-e048-42bc-8b75-68a004851803"
  // This is hv2BranchKeyVersion above, as utf8bytes
  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Decimal('Comma',false)&input=YTA0OTZiNWMtZTA0OC00MmJjLThiNzUtNjhhMDA0ODUxODAz&oenc=65001
  const hv2BranchKeyIdActiveVersionUtf8Bytes: seq<uint8> := [
    97, 48, 52, 57, 54, 98, 53, 99, 45, 101, 48, 52,
    56, 45, 52, 50, 98, 99, 45, 56, 98, 55, 53, 45,
    54, 56, 97, 48, 48, 52, 56, 53, 49, 56, 48, 51
  ]
  // THESE ARE TESTING RESOURCES DO NOT USE IN A PRODUCTION ENVIRONMENT
  const keyArn := "arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126"
  const kmsArnForHV1 := "arn:aws:kms:us-west-2:370957321024:key/85cee5a8-fecb-41e9-affd-a1f7bb036884"
  const kmsArnForHV2 := "arn:aws:kms:us-west-2:370957321024:key/da179005-1c04-4b91-a103-ee43b9a707e6"
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
  const KmsMrkEC : Types.EncryptionContext := map[abc := x123]
  const RobbieEC : Types.EncryptionContext := map[Robbie := IsADog]
  const RobbieECString : Types.EncryptionContextString := map["Robbie" := "Is a dog."]
  const KodaECString : Types.EncryptionContextString := map["Koda" := "Is a dog."]
  const EastBranchKey : string := "MyEastBranch2"
  const EastBranchKeyIdActiveVersion : string := "6f22825b-bd56-4434-83e2-2782e2160172"
  const EastBranchKeyBranchKeyIdActiveVersionUtf8Bytes: seq<uint8> := [
    54, 102, 50, 50, 56, 50, 53, 98, 45, 98, 100,
    53, 54, 45, 52, 52, 51, 52, 45, 56, 51, 101, 50,
    45, 50, 55, 56, 50, 101, 50, 49, 54, 48, 49, 55, 50
  ]
  const WestBranchKey : string := "MyWestBranch2"
  const WestBranchKeyIdActiveVersion : string := "094715a4-b98d-4c98-bf50-17422a8938f4"
  const WestBranchKeyBranchKeyIdActiveVersionUtf8Bytes: seq<uint8> := [
    48, 57, 52, 55, 49, 53, 97, 52, 45, 98, 57, 56,
    100, 45, 52, 99, 57, 56, 45, 98, 102, 53, 48, 45,
    49, 55, 52, 50, 50, 97, 56, 57, 51, 56, 102, 52
  ]
  const publicKeyArn := "arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"
  const kmsSystemKey := "arn:aws:kms:us-west-2:370957321024:key/6613e250-b2e7-4c4c-a54e-2b241f837242"

  // TODO: After ~2024/06/11 launch, add the next two lines to cfn/ESDK-Hierarchy-CI.yaml
  const postalHornKeyArn := "arn:aws:kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8"
  const kmsKeyAlias := "arn:aws:kms:us-west-2:370957321024:alias/postalHorn"
  const postalHornBranchKeyId := "682dfba7-4c35-491d-8d6a-5a9c56194061"
  const postalHornBranchKeyActiveVersion := "6b7a8ef4-8c1c-4f63-b196-a6ef7e496e50"

  // Creation of this particular illegal Branch Key is detailed here:
  // `git rev-parse --show-toplevel`/cfn/lyingBranchKeyCreation.md
  const hierarchyV1InvalidKmsArnId := "kms-arn-attribute-is-lying"
  const hierarchyV1InvalidKmsArnVersion := "129c5c87-308a-41c9-8b9d-a27f66e915f4"
  // TODO-HV-2-FF : Document creation of lying branch keys
  const hierarchyV2InvalidKmsArnId := "DO-NOT-DELETE-test-hv2-get-key-wrong-kms-arn"
  const hierarchyV2InvalidKmsArnVersion := "e3df6cf8-3edc-4781-998e-c4731b755452"

  const hierarchyV2InvalidDigestId := "DO-NOT-DELETE-test-hv2-get-key-wrong-digest"
  const hierarchyV2InvalidDigestVersion := "755404a1-a295-4ec9-ba13-c540e16515d5"

  const hierarchyV2InvalidCiphertextId := "DO-NOT-DELETE-test-hv2-get-key-wrong-ciphertext"
  const hierarchyV2InvalidCiphertextVersion := "94a3bb88-bbaa-4830-99d4-7a949a02f4a1"

  const hierarchyV2InvalidPlaintextLengthId := "DO-NOT-DELETE-test-hv2-get-key-wrong-ciphertext-length"
  const hierarchyV2InvalidPlaintextLengthVersion := "04b459a3-0731-4ba8-b9ac-4e29eb6db485"

  const hierarchyV2MissingPrefixedECId := "DO-NOT-DELETE-test-hv2-get-key-missing-prefixed-ec"
  const hierarchyV2MissingPrefixedECVersion := "d3e7b039-71fb-41af-8549-2564a170935c"

  const hierarchyV2UnexpectedECId := "DO-NOT-DELETE-test-hv2-get-key-unexpected-ec"
  const hierarchyV2UnexpectedECVersion := "a01eec17-9b1c-4f4a-9b66-2c84816854ac"

  // Constants for Testing Storage
  const ORIGINAL_BYTES : UTF8.ValidUTF8Bytes :=
    var s := [0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x2d, 0x64, 0x6f, 0x65, 0x73, 0x2d, 0x6e, 0x6f, 0x74, 0x2d, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2d, 0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x61, 0x6c, 0x2d, 0x6f, 0x6e, 0x6c, 0x79, 0x2d, 0x74, 0x68, 0x61, 0x74, 0x2d, 0x69, 0x73, 0x2d, 0x62, 0x69, 0x6e, 0x61, 0x72, 0x79];
    assert s == UTF8.EncodeAscii("storage-does-not-validate-original-only-that-is-binary");
    s

  const TERMINAL_BYTES : UTF8.ValidUTF8Bytes :=
    var s := [0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x2d, 0x64, 0x6f, 0x65, 0x73, 0x2d, 0x6e, 0x6f, 0x74, 0x2d, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2d, 0x74, 0x65, 0x72, 0x6d, 0x69, 0x6e, 0x61, 0x6c, 0x2d, 0x6f, 0x6e, 0x6c, 0x79, 0x2d, 0x74, 0x68, 0x61, 0x74, 0x2d, 0x69, 0x73, 0x2d, 0x62, 0x69, 0x6e, 0x61, 0x72, 0x79];
    assert s == UTF8.EncodeAscii("storage-does-not-validate-terminal-only-that-is-binary");
    s

  const INPUT_BYTES : UTF8.ValidUTF8Bytes :=
    var s := [0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x2d, 0x64, 0x6f, 0x65, 0x73, 0x2d, 0x6e, 0x6f, 0x74, 0x2d, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2d, 0x69, 0x6e, 0x70, 0x75, 0x74, 0x2d, 0x6f, 0x6e, 0x6c, 0x79, 0x2d, 0x74, 0x68, 0x61, 0x74, 0x2d, 0x69, 0x73, 0x2d, 0x62, 0x69, 0x6e, 0x61, 0x72, 0x79];
    assert s == UTF8.EncodeAscii("storage-does-not-validate-input-only-that-is-binary");
    s

  const ENC_BYTES : UTF8.ValidUTF8Bytes :=
    var s := [0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x2d, 0x64, 0x6f, 0x65, 0x73, 0x2d, 0x6e, 0x6f, 0x74, 0x2d, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2d, 0x65, 0x6e, 0x63, 0x2d, 0x6f, 0x6e, 0x6c, 0x79, 0x2d, 0x74, 0x68, 0x61, 0x74, 0x2d, 0x69, 0x73, 0x2d, 0x62, 0x69, 0x6e, 0x61, 0x72, 0x79];
    assert s == UTF8.EncodeAscii("storage-does-not-validate-enc-only-that-is-binary");
    s

  const NOW_BYTES : UTF8.ValidUTF8Bytes :=
    var s := [0x6e, 0x6f, 0x77];
    assert s == UTF8.EncodeAscii("now");
    s

  // This function is the lie we will tell ourselves
  // about what the mutation scope is.
  // You MUST NOT reveal this value.
  function {:opaque} FixturesLie(): set<object>
  {{}}

  method ProvideDDBClient(
    ddbClient?: Option<DDB.Types.IDynamoDBClient> := None
  )
    returns (output: Result<DDB.Types.IDynamoDBClient, DDB.Types.Error>)
    requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
    modifies (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
    ensures output.Success?
            ==>
              && output.value.ValidState()
              && fresh(output.value)
              && fresh(output.value.Modifies)
  {
    var ddbClient: DDB.Types.IDynamoDBClient;
    if (ddbClient?.None?) {
      ddbClient :- DDB.DynamoDBClient();
    } else {
      ddbClient := ddbClient?.value;
    }
    assume {:axiom} ddbClient.Modifies < FixturesLie();
    assume {:axiom} fresh(ddbClient) && fresh(ddbClient.Modifies);
    return Success(ddbClient);
  }

  method ProvideKMSClient(
    kmsClient?: Option<KMS.Types.IKMSClient> := None
  )
    returns (output: Result<KMS.Types.IKMSClient, KMS.Types.Error>)
    requires kmsClient?.Some? ==> kmsClient?.value.ValidState()
    modifies (if kmsClient?.Some? then kmsClient?.value.Modifies else {})
    ensures output.Success?
            ==>
              && output.value.ValidState()
              && fresh(output.value)
              && fresh(output.value.Modifies)
  {
    var kmsClient: KMS.Types.IKMSClient;
    if (kmsClient?.None?) {
      kmsClient :- KMS.KMSClient();
    } else {
      kmsClient := kmsClient?.value;
    }
    assume {:axiom} kmsClient.Modifies < FixturesLie();
    assume {:axiom} fresh(kmsClient) && fresh(kmsClient.Modifies);
    return Success(kmsClient);
  }

  method DefaultStorage(
    nameonly physicalName: string := branchKeyStoreName,
    nameonly logicalName: string := logicalKeyStoreName,
    nameonly ddbClient?: Option<DDB.Types.IDynamoDBClient> := None
  )
    returns (output: Result<Types.IKeyStorageInterface, Types.Error>)
    requires DDB.Types.IsValid_TableName(physicalName)
    requires UTF8.IsASCIIString(physicalName) && UTF8.IsASCIIString(logicalName)
    requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
    ensures output.Success? ==> output.value.ValidState()
    ensures output.Success? ==> fresh(output.value) && fresh(output.value.Modifies)
    modifies (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
    ensures output.Success?
            ==>
              && output.value.ValidState()
              && fresh(output.value)
              && fresh(output.value.Modifies)
  {
    var ddbClient :- expect ProvideDDBClient(ddbClient?);
    assume {:axiom} fresh(ddbClient) && fresh(ddbClient.Modifies);
    var physicalNameUtf8 :- expect UTF8.Encode(physicalName);
    var logicalNameUtf8 :- expect UTF8.Encode(logicalName);
    var underTest := new DefaultKeyStorageInterface.DynamoDBKeyStorageInterface(
      ddbTableName := physicalName,
      ddbClient := ddbClient,
      logicalKeyStoreName := logicalName,
      ddbTableNameUtf8 := physicalNameUtf8,
      logicalKeyStoreNameUtf8 := logicalNameUtf8);
    output := Success(underTest);
  }

  method StaticStorage(
    nameonly ddbClient?: Option<DDB.Types.IDynamoDBClient> := None
  )
    returns (output: Result<Types.IKeyStorageInterface, Types.Error>)
    requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
    ensures output.Success? ==> output.value.ValidState()
    ensures output.Success? ==> fresh(output.value) && fresh(output.value.Modifies)
    modifies (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
    ensures output.Success?
            ==>
              && output.value.ValidState()
              && fresh(output.value)
              && fresh(output.value.Modifies)
  {
    output := DefaultStorage(
      physicalName := staticBranchKeyStoreName,
      logicalName := staticLogicalKeyStoreName,
      ddbClient? := ddbClient?
    );
  }

  method DefaultKeyStore(
    nameonly kmsId: string := keyArn,
    nameonly physicalName: string := branchKeyStoreName,
    nameonly logicalName: string := logicalKeyStoreName,
    nameonly ddbClient?: Option<DDB.Types.IDynamoDBClient> := None,
    nameonly kmsClient?: Option<KMS.Types.IKMSClient> := None
  )
    returns (output: Result<Types.IKeyStoreClient, Types.Error>)
    requires DDB.Types.IsValid_TableName(physicalName)
    requires KMS.Types.IsValid_KeyIdType(kmsId)
    requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
    requires kmsClient?.Some? ==> kmsClient?.value.ValidState()
    ensures output.Success? ==> output.value.ValidState()
    modifies (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
             + (if kmsClient?.Some? then kmsClient?.value.Modifies else {})
    ensures output.Success?
            ==>
              && output.value.ValidState()
              && fresh(output.value)
              && fresh(output.value.Modifies)
  {
    var ddbClient :- expect ProvideDDBClient(ddbClient?);
    assume {:axiom} fresh(ddbClient) && fresh(ddbClient.Modifies);
    var kmsClient :- expect ProvideKMSClient(kmsClient?);
    assume {:axiom} fresh(kmsClient) && fresh(kmsClient.Modifies);
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(kmsId);
    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalName,
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := physicalName,
            ddbClient := Some(ddbClient)
          ))),
      keyManagement := Some(
        Types.kms(
          Types.AwsKms(
            kmsClient := Some(kmsClient)
          )))
    );
    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
    return Success(keyStore);
  }

  method StaticKeyStore(
    nameonly kmsId: string := keyArn,
    nameonly physicalName: string := staticBranchKeyStoreName,
    nameonly logicalName: string := staticLogicalKeyStoreName,
    nameonly ddbClient?: Option<DDB.Types.IDynamoDBClient> := None,
    nameonly kmsClient?: Option<KMS.Types.IKMSClient> := None
  )
    returns (output: Result<Types.IKeyStoreClient, Types.Error>)
    requires DDB.Types.IsValid_TableName(physicalName)
    requires KMS.Types.IsValid_KeyIdType(kmsId)
    requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
    requires kmsClient?.Some? ==> kmsClient?.value.ValidState()
    ensures output.Success? ==> output.value.ValidState()
    modifies (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
             + (if kmsClient?.Some? then kmsClient?.value.Modifies else {})
    ensures output.Success?
            ==>
              && output.value.ValidState()
              && fresh(output.value)
              && fresh(output.value.Modifies)
  {
    output := DefaultKeyStore(
      kmsId := kmsId,
      physicalName := physicalName,
      logicalName := logicalName,
      ddbClient? := ddbClient?,
      kmsClient? := kmsClient?
    );
  }

  method KeyStoreFromKMSConfig(
    nameonly kmsConfig: Types.KMSConfiguration,
    nameonly physicalName: string := branchKeyStoreName,
    nameonly logicalName: string := logicalKeyStoreName,
    nameonly ddbClient?: Option<DDB.Types.IDynamoDBClient> := None
  )
    returns (output: Result<Types.IKeyStoreClient, Types.Error>)
    requires DDB.Types.IsValid_TableName(physicalName)
    ensures output.Success? ==> output.value.ValidState()
    ensures output.Success?
            ==>
              && output.value.ValidState()
              && fresh(output.value)
              && fresh(output.value.Modifies)
  {
    if ddbClient?.Some? {
      assume {:axiom} fresh(ddbClient?.value) && fresh(ddbClient?.value.Modifies);
    }
    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalName,
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := physicalName,
            ddbClient := ddbClient?
          )))
    );
    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
    return Success(keyStore);
  }

  datatype allThree = | allThree (
    active: Types.EncryptedHierarchicalKey,
    beacon: Types.EncryptedHierarchicalKey,
    decrypt: Types.EncryptedHierarchicalKey)

  method getItems(
    nameonly id: string,
    nameonly underTest: Types.IKeyStorageInterface
  )
    returns (output: Result<allThree, Types.Error>)
    requires underTest.ValidState()
    ensures underTest.ValidState()
    modifies underTest.Modifies
  {
    var activeInput := Types.GetEncryptedActiveBranchKeyInput(
      Identifier := id
    );
    var active? :- underTest.GetEncryptedActiveBranchKey(activeInput);
    var active := active?.Item;

    var beaconInput := Types.GetEncryptedBeaconKeyInput(
      Identifier := id
    );
    var beacon? :- underTest.GetEncryptedBeaconKey(beaconInput);
    var beacon := beacon?.Item;

    expect active.Type.ActiveHierarchicalSymmetricVersion?;
    var decryptInput := Types.GetEncryptedBranchKeyVersionInput(
      Identifier := id,
      Version := active.Type.ActiveHierarchicalSymmetricVersion.Version
    );
    var decrypt? :- underTest.GetEncryptedBranchKeyVersion(decryptInput);
    var decrypt := decrypt?.Item;
    output := Success(allThree(active, beacon, decrypt));
  }

  const Robbie : UTF8.ValidUTF8Bytes :=
    var s := [0x52, 0x6f, 0x62, 0x62, 0x69, 0x65];
    assert s == UTF8.EncodeAscii("Robbie");
    s

  const Koda : UTF8.ValidUTF8Bytes :=
    var s := [0x4b, 0x6f, 0x64, 0x61];
    assert s == UTF8.EncodeAscii("Koda");
    s

  const IsADog : UTF8.ValidUTF8Bytes :=
    var s := [0x49, 0x73, 0x20, 0x61, 0x20, 0x64, 0x6f, 0x67, 0x2e];
    assert s == UTF8.EncodeAscii("Is a dog.");
    s

  method CreateHappyCaseId(
    nameonly id: string,
    nameonly kmsId: string := keyArn,
    nameonly physicalName: string := branchKeyStoreName,
    nameonly logicalName: string := logicalKeyStoreName,
    nameonly versionCount: nat := 3,
    nameonly customEC: Types.EncryptionContext := RobbieEC
  )
    requires DDB.Types.IsValid_TableName(physicalName)
    requires KMS.Types.IsValid_KeyIdType(kmsId)
    requires 0 <= versionCount <= 5
    requires 0 < |customEC| // requires some EC
  {
    var keyStore :- expect DefaultKeyStore(kmsId:=kmsId, physicalName:=physicalName, logicalName:=logicalName);
    assume {:axiom} fresh(keyStore) && fresh(keyStore.Modifies);
    var input := Types.CreateKeyInput(
      branchKeyIdentifier := Some(id),
      encryptionContext := Some(customEC)
    );
    var branchKeyId :- expect keyStore.CreateKey(input);

    // If you need a new version
    var inputV := Types.VersionKeyInput(
      branchKeyIdentifier := id
    );
    var versionIndex := 0;
    while versionIndex < versionCount {
      var _ :- expect keyStore.VersionKey(inputV);
      versionIndex := versionIndex + 1;
    }
  }

  method GetItemFromDDB(
    nameonly id: string,
    nameonly typeStr: string,
    nameonly physicalName: string := branchKeyStoreName,
    nameonly ddbClient?: Option<DDB.Types.IDynamoDBClient> := None
  )
    returns (output: Result<DDB.Types.AttributeMap, string>)
    requires DDB.Types.IsValid_TableName(physicalName)
    requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
    modifies (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
  {
    var ddbClient: DDB.Types.IDynamoDBClient;
    if (ddbClient?.None?) {
      ddbClient :- expect DDB.DynamoDBClient();
    } else {
      ddbClient := ddbClient?.value;
    }
    var input := DDB.Types.GetItemInput(
      TableName := physicalName,
      Key := map[
        Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.Types.AttributeValue.S(id),
        Structure.TYPE_FIELD := DDB.Types.AttributeValue.S(typeStr)
      ],
      ConsistentRead := Some(true));
    var result? := ddbClient.GetItem(input);
    if (result?.Success? && result?.value.Item.Some? && 0 < |result?.value.Item.value| ) {
      return Success(result?.value.Item.value);
    }
    return Failure("Failed to GetItem. ID: " + id + " type: " + typeStr + " .");
  }

  method CopyBranchKey(
    nameonly Identifier: string,
    nameonly sourceTableName: string,
    nameonly targetTableName: string,
    nameonly ddbClient: DDB.Types.IDynamoDBClient
  )
    returns (output: Result<bool, DDB.Types.Error>)
    requires
      && ddbClient.ValidState()
      && DDB.Types.IsValid_TableName(sourceTableName)
      && DDB.Types.IsValid_TableName(targetTableName)
    modifies ddbClient.Modifies
    ensures ddbClient.ValidState()
  {
    // Query to get all items with the specified branch key ID
    var ExpressionAttributeNames := map[
      "#pk" := Structure.BRANCH_KEY_IDENTIFIER_FIELD
    ];
    var ExpressionAttributeValues := map[
      ":pk" := DDB.Types.AttributeValue.S(Identifier)
    ];
    var queryReq := DDB.Types.QueryInput(
      TableName := sourceTableName,
      KeyConditionExpression := Some("#pk = :pk"),
      ExpressionAttributeNames := Some(ExpressionAttributeNames),
      ExpressionAttributeValues := Some(ExpressionAttributeValues)
    );

    // Execute the query
    var queryRes :- ddbClient.Query(queryReq);
    if (queryRes.Items.None?) {
      return Success(true);
    }

    // Create put requests for each item
    var putItems: seq<DDB.Types.TransactWriteItem> :- Seq.MapWithResult(
      (item: DDB.Types.AttributeMap)
      =>
        :- Need(
             Structure.TYPE_FIELD in item,
             DDB.Types.Error.InternalServerError(message := Some("Item missing required type field"))
           );
        Success(
          DDB.Types.TransactWriteItem(
            Put := Some(
              DDB.Types.Put(
                Item := item,
                TableName := targetTableName
              )))),
      queryRes.Items.value);

    if (0 == |putItems|) {
      return Success(true);
    }

    // DynamoDB transactions are limited to 100 items
    var allItemsCopied := true;
    var remainingItems := putItems;

    while |remainingItems| > 0
      decreases |remainingItems|
    {
      var batchItems := if |remainingItems| > 100
      then remainingItems[..100]
      else remainingItems;

      var writeReq := DDB.Types.TransactWriteItemsInput(
        TransactItems := batchItems
      );
      var _ :- ddbClient.TransactWriteItems(writeReq);

      if |remainingItems| > 100 {
        remainingItems := remainingItems[100..];
        allItemsCopied := false;
      } else {
        remainingItems := [];
      }
    }

    return Success(allItemsCopied);
  }

  method CopyAllStaticBranchKeys(
    nameonly ddbClient: DDB.Types.IDynamoDBClient
  )
    returns (output: Result<bool, DDB.Types.Error>)
    requires ddbClient.ValidState()
    modifies ddbClient.Modifies
    ensures ddbClient.ValidState()
  {
    // List of (branchKeyId, hierarchyVersion)
    var branchKeys := [
      // HV1 Branch Keys
      branchKeyId,
      branchKeyIdWithEC,
      hierarchyV1InvalidKmsArnId,
      EastBranchKey,
      WestBranchKey,
      postalHornBranchKeyId,
      "STATIC-PRE-HV-2-MUTATION-WITH-SYSTEM-KEY",
      "STATIC-PRE-HV-2-MUTATION-WITH-TRUST-STORAGE",

      // HV2 Branch Keys
      hv2BranchKeyId,
      hierarchyV2InvalidKmsArnId,
      hierarchyV2InvalidDigestId,
      hierarchyV2InvalidCiphertextId,
      hierarchyV2InvalidPlaintextLengthId,
      hierarchyV2MissingPrefixedECId,
      hierarchyV2UnexpectedECId
    ];

    var idx := 0;
    while idx < |branchKeys|
      decreases |branchKeys| - idx
    {
      var id := branchKeys[idx];
      var _ :- CopyBranchKey(
        Identifier := id,
        sourceTableName := branchKeyStoreName,
        targetTableName := staticBranchKeyStoreName,
        ddbClient := ddbClient
      );

      idx := idx + 1;
    }

    return Success(true);
  }
  /*
    // Test to Copy All Static Branch Keys from `KeyStoreDdbTable` to `KeyStoreStaticTable`
    //
    // IMPORTANT:
    // The CI role does not have write access to `KeyStoreStaticTable` by default.
    // To copy static branch keys to the static key store table, you must:
    //   1. Assume the Admin role for the CI account
    //   2. Run this test with the proper IAM permissions
    //   3. Verify all keys were copied successfully
    //
    // This test should be performed carefully and only when necessary,
    // such as when setting up test environments or refreshing static test data.
    method {:test} TestCopyAllBranchKeys()
    {
      var ddbClient :- expect ProvideDDBClient();
      var success :- expect CopyAllStaticBranchKeys(ddbClient := ddbClient);
      expect success, "Failed to copy all branch keys";
    }
  */
}
