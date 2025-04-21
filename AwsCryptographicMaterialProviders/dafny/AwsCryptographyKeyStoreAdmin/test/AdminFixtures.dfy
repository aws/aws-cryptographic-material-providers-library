// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"

module {:options "/functionSyntax:4" } AdminFixtures {
  // Standard Library Imports
  import opened Wrappers
  import UTF8 = Fixtures.UTF8
    // SDK Imports
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
    // (Branch) Key Store Imports
  import KeyStore
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import Fixtures
  import DefaultKeyStorageInterface
  import Structure
    // (Branch) Key Store Admin Imports
  import KeyStoreAdmin
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KmsUtils

  // These are Branch Keys that are in an "in-flight" mutation,
  // but that mutation was started pre-HV-2.
  const STATIC_PRE_HV2_MUTATION_WITH_SYSTEM_KEY := "STATIC-PRE-HV-2-MUTATION-WITH-SYSTEM-KEY"
  const STATIC_PRE_HV2_MUTATION_WITH_TRUST_STORAGE := "STATIC-PRE-HV-2-MUTATION-WITH-TRUST-STORAGE"

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
      logicalKeyStoreNameUtf8 := logicalNameUtf8
    );

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

  method SimpleKeyManagerStrategy(
    nameonly kmsClient?: Option<KMS.Types.IKMSClient> := None
  )
    returns (output: Result<Types.KeyManagementStrategy, Types.Error>)
    requires kmsClient?.Some? ==> kmsClient?.value.ValidState()
    ensures output.Success? ==>
              && output.value.AwsKmsSimple?
              && output.value.AwsKmsSimple.kmsClient.Some?
              && output.value.AwsKmsSimple.kmsClient.value.ValidState()
    modifies (if kmsClient?.Some? then kmsClient?.value.Modifies else {})
  {
    var kmsClient :- expect Fixtures.ProvideKMSClient(kmsClient?);
    assume {:axiom} fresh(kmsClient) && fresh(kmsClient.Modifies);
    var strategy := Types.KeyManagementStrategy.AwsKmsSimple(
      KeyStoreTypes.AwsKms(
        grantTokens := None,
        kmsClient := Some(kmsClient)
      ));
    return Success(strategy);
  }

  method DecryptEncrypKeyManagerStrategy(
    nameonly decryptKmsClient?: Option<KMS.Types.IKMSClient> := None,
    nameonly encryptKmsClient?: Option<KMS.Types.IKMSClient> := None
  )
    returns (output: Result<Types.KeyManagementStrategy, Types.Error>)
    requires decryptKmsClient?.Some? ==> decryptKmsClient?.value.ValidState()
    requires encryptKmsClient?.Some? ==> encryptKmsClient?.value.ValidState()
    ensures output.Success? ==>
              && output.value.AwsKmsDecryptEncrypt?
              && output.value.AwsKmsDecryptEncrypt.decrypt.Some?
              && output.value.AwsKmsDecryptEncrypt.encrypt.Some?
              && output.value.AwsKmsDecryptEncrypt.decrypt.value.kmsClient.Some?
              && output.value.AwsKmsDecryptEncrypt.decrypt.value.kmsClient.value.ValidState()
              && output.value.AwsKmsDecryptEncrypt.encrypt.value.kmsClient.Some?
              && output.value.AwsKmsDecryptEncrypt.encrypt.value.kmsClient.value.ValidState()
    modifies (if decryptKmsClient?.Some? then decryptKmsClient?.value.Modifies else {})
    modifies (if encryptKmsClient?.Some? then encryptKmsClient?.value.Modifies else {})
  {
    var decryptKmsClient :- expect Fixtures.ProvideKMSClient(decryptKmsClient?);
    var encryptKmsClient :- expect Fixtures.ProvideKMSClient(encryptKmsClient?);
    assume {:axiom} fresh(decryptKmsClient) && fresh(decryptKmsClient.Modifies);
    assume {:axiom} fresh(encryptKmsClient) && fresh(encryptKmsClient.Modifies);

    var strategy := Types.KeyManagementStrategy.AwsKmsDecryptEncrypt(
      Types.AwsKmsDecryptEncrypt.AwsKmsDecryptEncrypt(
        decrypt := Some(KeyStoreTypes.AwsKms(
                          grantTokens := None,
                          kmsClient := Some(decryptKmsClient)
                        )),
        encrypt := Some(KeyStoreTypes.AwsKms(
                          grantTokens := None,
                          kmsClient := Some(encryptKmsClient)
                        ))
      )
    );
    return Success(strategy);
  }

  method ProvideKMSTuple(
    nameonly kmsClient?: Option<KMS.Types.IKMSClient> := None,
    nameonly grantTokens?: Option<KMS.Types.GrantTokenList> := None
  )
    returns (output: Result<KmsUtils.KMSTuple, Types.Error>)
    requires kmsClient?.Some? ==> kmsClient?.value.ValidState()
    requires grantTokens?.Some? ==> KMS.Types.IsValid_GrantTokenList(grantTokens?.value)
    ensures output.Success? ==> output.value.ValidState()
    ensures output.Success? ==> fresh(output.value.kmsClient)
    ensures output.Success? ==> fresh(output.value.kmsClient.Modifies)
    ensures output.Success? ==> fresh(output.value.Modifies)
    modifies (if kmsClient?.Some? then kmsClient?.value.Modifies else {})
  {
    var kmsClient :- expect Fixtures.ProvideKMSClient(kmsClient?);
    assume {:axiom} fresh(kmsClient) && fresh(kmsClient.Modifies);
    var grantTokens := if grantTokens?.Some? then grantTokens?.value else [];
    output := Success(KmsUtils.KMSTuple(kmsClient, grantTokens));
  }

  datatype KmsDdbError =
    | ComAmazonawsDynamodb(ComAmazonawsDynamodb: DDB.Types.Error)
    | ComAmazonawsKms(ComAmazonawsKms: KMS.Types.Error)

  datatype KeyValue = KeyValue(
    key: string := "Robbie",
    value: string := "Is a dog.")

  /** Adds an "un-modeled Attribute" to the Active & Decrypt.
   If alsoViolateBeacion?, also add to Beacon.
   If violateReservedAttribute, the reserved attributes can be modified,
   such as 'create-time' or 'version'. */
  method AddAttributeWithoutLibrary(
    nameonly id: string,
    nameonly physicalName: string := Fixtures.branchKeyStoreName,
    nameonly logicalName: string := Fixtures.logicalKeyStoreName,
    nameonly keyValue: KeyValue := KeyValue(key:="Robbie", value:="Is a dog."),
    nameonly alsoViolateBeacon?: bool := false,
    nameonly ddbClient?: Option<DDB.Types.IDynamoDBClient> := None,
    nameonly kmsClient?: Option<KMS.Types.IKMSClient> := None,
    nameonly violateReservedAttribute: bool := false
  )
    returns (output: Result<bool, KmsDdbError>)
    requires DDB.Types.IsValid_TableName(physicalName)
    requires UTF8.IsASCIIString(physicalName) && UTF8.IsASCIIString(logicalName)
    // Either the keyValue is NOT reserved, or this is violating a reserved attribute
    requires violateReservedAttribute || keyValue.key !in Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES
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
      item := allThree.active, keyValue:=keyValue, kmsClient:=kmsClient, physicalName:=physicalName, violateReservedAttribute:=violateReservedAttribute);
    var decryptDDB :- expect ViolateItem(
      item := allThree.decrypt, keyValue:=keyValue, kmsClient:=kmsClient, physicalName:=physicalName, violateReservedAttribute:=violateReservedAttribute);
    var TransactItems := [activeDDB, decryptDDB];

    if (alsoViolateBeacon?) {
      var beaconDDB :- expect ViolateItem(
        item := allThree.beacon, keyValue:=keyValue, kmsClient:=kmsClient, physicalName:=physicalName, violateReservedAttribute:=violateReservedAttribute);
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
    nameonly physicalName: string := Fixtures.branchKeyStoreName,
    nameonly violateReservedAttribute: bool := false
  )
    returns (ddbPutItem: Result<DDB.Types.TransactWriteItem, KmsDdbError>)
    requires kmsClient.ValidState()
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()
    // Either the keyValue is NOT reserved, or this is violating a reserved attribute
    requires violateReservedAttribute || keyValue.key !in Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES
    requires DDB.Types.IsValid_AttributeName(keyValue.key)
    requires DDB.Types.IsValid_TableName(physicalName)
  {
    assume {:axiom} KMS.Types.IsValid_CiphertextType(item.CiphertextBlob);
    assume {:axiom} KMS.Types.IsValid_KeyIdType(item.KmsArn);
    var violatedEC;
    var aMap := map[keyValue.key := keyValue.value];
    if (!violateReservedAttribute) {
      expect keyValue.key !in item.EncryptionContext, "key of KeyValue cannot already be in EC";
      violatedEC := item.EncryptionContext + aMap;
      expect Structure.BranchKeyContext?(violatedEC), "Library is too good and won't let Tony cheat";
    } else {
      violatedEC := item.EncryptionContext + aMap;
    }
    var reEncryptReq := KMS.Types.ReEncryptRequest(
      CiphertextBlob := item.CiphertextBlob,
      SourceEncryptionContext := Some(item.EncryptionContext),
      DestinationKeyId := item.KmsArn,
      DestinationEncryptionContext := Some(violatedEC));

    var reEncryptRes :- expect kmsClient.ReEncrypt(reEncryptReq);
    expect reEncryptRes.CiphertextBlob.Some?, "KMS did not return ciphertext.";

    // This assumption is a LIE; but I am not copying a bunch of methods
    assume {:axiom} Structure.BranchKeyContext?(violatedEC);
    var violated := Structure.ConstructEncryptedHierarchicalKey(
      violatedEC, reEncryptRes.CiphertextBlob.value);

    expect forall k <- violatedEC.Keys :: DDB.Types.IsValid_AttributeName(k), "How did an invalid DDB Attribute Name get here?";
    return Success(
        DDB.Types.TransactWriteItem(
          Put := Some(DDB.Types.Put(
                        Item := Structure.ToAttributeMap(violated),
                        TableName := physicalName))));
  }

  // TODO-HV-2-M3-Version: Support Versioning of Happy Case Id along with Create.
  method CreateHappyCaseId(
    nameonly id: string,
    nameonly kmsId: string := Fixtures.keyArn,
    nameonly hierarchyVersion: KeyStoreTypes.HierarchyVersion := KeyStoreTypes.HierarchyVersion.v1,
    nameonly strategy: Types.KeyManagementStrategy,
    nameonly admin?: Option<Types.IKeyStoreAdminClient> := None,
    // nameonly versionCount: nat := 3,
    nameonly customEC: KeyStoreTypes.EncryptionContext := map[UTF8.EncodeAscii("Robbie") := UTF8.EncodeAscii("Is a dog.")]
  )
    requires KMS.Types.IsValid_KeyIdType(kmsId)
    requires 0 < |customEC|
  {
    var admin;
    if admin?.None? {
      admin :- expect DefaultAdmin(
        physicalName := Fixtures.branchKeyStoreName,
        logicalName := Fixtures.logicalKeyStoreName,
        ddbClient? := None
      );
    } else {
      admin := admin?.value;
    }
    assume {:axiom} fresh(admin) && fresh(admin.Modifies);
    var input := Types.CreateKeyInput(
      Identifier := Some(id),
      EncryptionContext := Some(customEC),
      KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(kmsId),
      Strategy := Some(strategy),
      HierarchyVersion := Some(hierarchyVersion)
    );
    var branchKeyId :- expect admin.CreateKey(input);
  }
}

