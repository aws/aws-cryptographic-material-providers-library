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
  import DefaultEncryptedKeyStore

  method {:opaque} DefaultAdmin(
    nameonly physicalName: string := Fixtures.branchKeyStoreName,
    nameonly logicalName: string := Fixtures.logicalKeyStoreName,
    nameonly ddbClient?: Option<DDB.Types.IDynamoDBClient> := None
  )
    returns (output: Result<Types.IKeyStoreAdminClient, Types.Error>)
    requires DDB.Types.IsValid_TableName(physicalName)
    ensures output.Success? ==> output.value.ValidState()
    requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
    modifies (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
  {
    var ddbClient: DDB.Types.IDynamoDBClient;
    if (ddbClient?.None?) {
      ddbClient :- expect DDB.DynamoDBClient();
    } else {
      ddbClient := ddbClient?.value;
    }
    // var storage :- expect DefaultStorage(
    //   physicalName := physicalName,
    //   logicalName := logicalName,
    //   ddbClient?:=Some(ddbClient)
    // );
    var storage := new DefaultEncryptedKeyStore.DynamoDBEncryptedKeyStore(
      ddbTableName := physicalName,
      ddbClient := ddbClient,
      logicalKeyStoreName := logicalName);

    var underTestConfig := Types.KeyStoreAdminConfig(
      logicalKeyStoreName := logicalName,
      storage := KeyStoreTypes.Storage.custom(storage));
    var underTest :- expect KeyStoreAdmin.KeyStoreAdmin(underTestConfig);
    // We may not need this, but **Oh My God** does it make verification go faster
    // assume {:axiom} underTest.Modifies == {} && ddbClient.Modifies == {} && ddbClient.ValidState() && underTest.ValidState();
    return Success(underTest);
  }

  method {:opaque} DefaultKeyManagerStrategy(
    // nameonly kmsId: Types.KMSIdentifier := Types.KMSIdentifier.kmsKeyArn(Fixtures.keyArn),
    // nameonly grantTokens
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
    // We may not need this, but **Oh My God** does it make verification go faster
    // assume {:axiom} strategy.AwsKmsReEncrypt.kmsClient.value.ValidState();  //&& strategy.AwsKmsReEncrypt.kmsClient.value.Modifies == {}
    return Success(strategy);
  }

  method DefaultKeyStore(
    nameonly kmsId: string := Fixtures.keyArn,
    nameonly physicalName: string := Fixtures.branchKeyStoreName,
    nameonly logicalName: string := Fixtures.logicalKeyStoreName,
    nameonly ddbClient?: Option<DDB.Types.IDynamoDBClient> := None,
    nameonly kmsClient?: Option<KMS.Types.IKMSClient> := None
  )
    returns (output: Result<KeyStoreTypes.IKeyStoreClient, Types.Error>)
    requires DDB.Types.IsValid_TableName(physicalName)
    requires KMS.Types.IsValid_KeyIdType(kmsId)
    requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
    requires kmsClient?.Some? ==> kmsClient?.value.ValidState()
    ensures output.Success? ==> output.value.ValidState()
    modifies (if kmsClient?.Some? then kmsClient?.value.Modifies else {})
             + (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
  {
    var ddbClient: DDB.Types.IDynamoDBClient;
    if (ddbClient?.None?) {
      ddbClient :- expect DDB.DynamoDBClient();
    } else {
      ddbClient := ddbClient?.value;
    }
    var kmsClient: KMS.Types.IKMSClient;
    if (kmsClient?.None?) {
      kmsClient :- expect KMS.KMSClient();
    } else {
      kmsClient := kmsClient?.value;
    }
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
    // We may not need this, but **Oh My God** does it make verification go faster
    // assume {:axiom} kmsClient.Modifies == {} && ddbClient.Modifies == {} && ddbClient.ValidState() && kmsClient.ValidState();
    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
    // assume {:axiom} keyStore.Modifies == {} == kmsClient.Modifies == ddbClient.Modifies && keyStore.ValidState();
    return Success(keyStore);
  }

  method {:opaque} CreateHappyCaseId(
    nameonly id: string,
    nameonly kmsId: string := Fixtures.keyArn,
    nameonly physicalName: string := Fixtures.branchKeyStoreName,
    nameonly logicalName: string := Fixtures.logicalKeyStoreName,
    nameonly versionCount: nat := 3//,
    // nameonly ddbClient?: Option<DDB.Types.IDynamoDBClient> := None,
    // nameonly kmsClient?: Option<KMS.Types.IKMSClient> := None//,
    // nameonly keyStore?: Option<KeyStoreTypes.IKeyStoreClient> := None
  )
    requires DDB.Types.IsValid_TableName(physicalName)
    requires KMS.Types.IsValid_KeyIdType(kmsId)
    requires 0 <= versionCount <= 5
    // modifies (if kmsClient?.Some? then kmsClient?.value.Modifies else {})
    // + (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
    // + (if keyStore?.Some? then keyStore?.value.Modifies else {})
  {
    var keyStore: KeyStoreTypes.IKeyStoreClient;
    // if (keyStore?.None?) {

    var ddbClient: DDB.Types.IDynamoDBClient;
    // if (ddbClient?.None?) {
    ddbClient :- expect DDB.DynamoDBClient();
    // } else {
    //   ddbClient := ddbClient?.value;
    // }
    var kmsClient: KMS.Types.IKMSClient;
    // if (kmsClient?.None?) {
    kmsClient :- expect KMS.KMSClient();
    // } else {
    //   kmsClient := kmsClient?.value;
    // }
    // keyStore :- expect DefaultKeyStore(
    //   kmsId:=kmsId,
    //   physicalName:=physicalName,
    //   logicalName:=logicalName,
    //   ddbClient?:=Some(ddbClient),
    //   kmsClient?:=Some(kmsClient));
    //   assume {:axiom} keyStore.ValidState(); //&& keyStore.Modifies == {} == kmsClient.Modifies == ddbClient.Modifies;
    // } else {
    //   keyStore := keyStore?.value;
    //   assume {:axiom} keyStore.ValidState();
    //   assume {:axiom} keyStore.Modifies == {} && keyStore.ValidState();
    // }

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
    // We may not need this, but **Oh My God** does it make verification go faster
    // assume {:axiom} kmsClient.Modifies == {} && ddbClient.Modifies == {} && ddbClient.ValidState() && kmsClient.ValidState();
    keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
    var input := KeyStoreTypes.CreateKeyInput(
      branchKeyIdentifier := Some(id),
      encryptionContext := Some(map[UTF8.EncodeAscii("Robbie") := UTF8.EncodeAscii("Is a dog.")])
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
    returns (output: Result<KeyStoreTypes.IEncryptedKeyStore, KeyStoreTypes.Error>)
    requires DDB.Types.IsValid_TableName(physicalName)
    // requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
    ensures output.Success? ==> output.value.ValidState()
    // modifies (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
  {
    var ddbClient: DDB.Types.IDynamoDBClient;
    // if (ddbClient?.None?) {
    ddbClient :- expect DDB.DynamoDBClient();
    // } else {
    //   ddbClient := ddbClient?.value;
    // }
    // assume {:axiom} ddbClient.Modifies == {} && ddbClient.ValidState();
    var underTest := new DefaultEncryptedKeyStore.DynamoDBEncryptedKeyStore(
      ddbTableName := physicalName,
      ddbClient := ddbClient,
      logicalKeyStoreName := logicalName);
    // We may not need this, but **Oh My God** does it make verification go faster
    // assume {:axiom} underTest.Modifies == {} && ddbClient.Modifies == {} && ddbClient.ValidState() && underTest.ValidState();
    output := Success(underTest);
  }

}
