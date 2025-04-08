// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../../../src/Index.dfy"
include "../../../TestUtils.dfy"
include "../../../../src/AlgorithmSuites.dfy"
include "../../../../src/Materials.dfy"
include "../../../../src/ErrorMessages.dfy"

// This file depends on resources that exist for the Keystore
include "../../../../../AwsCryptographyKeyStore/test/Fixtures.dfy"

module TestAwsKmsHierarchicalKeyring {
  import Types = AwsCryptographyMaterialProvidersTypes
  import ComAmazonawsKmsTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import DDBTypes = ComAmazonawsDynamodbTypes
  import KeyStore = KeyStore
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import Crypto = AwsCryptographyPrimitivesTypes
  import AtomicPrimitives
  import MaterialProviders
  import StormTracker
  import StormTrackingCMC
  import opened TestUtils
  import opened AlgorithmSuites
  import opened Materials
  import opened UInt = StandardLibrary.UInt
  import opened Wrappers
  import ErrorMessages

  import Fixtures

  const TEST_ESDK_ALG_SUITE_ID := Types.AlgorithmSuiteId.ESDK(Types.ALG_AES_256_GCM_IV12_TAG16_NO_KDF)
  const TEST_DBE_ALG_SUITE_ID := Types.AlgorithmSuiteId.DBE(Types.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_SYMSIG_HMAC_SHA384)
  // THIS IS A TESTING RESOURCE DO NOT USE IN A PRODUCTION ENVIRONMENT
  const keyArn := Fixtures.keyArn
  const branchKeyStoreName: DDBTypes.TableName := Fixtures.branchKeyStoreName
  const logicalKeyStoreName := branchKeyStoreName

  // These tests require a keystore populated with these keys
  const BRANCH_KEY_ID := Fixtures.branchKeyId

  // Constants for TestBranchKeySupplier
  const BRANCH_KEY : UTF8.ValidUTF8Bytes :=
    var s := [0x62, 0x72, 0x61, 0x6e, 0x63, 0x68, 0x4b, 0x65, 0x79];
    assert s == UTF8.EncodeAscii("branchKey");
    s

  const CASE_A : UTF8.ValidUTF8Bytes :=
    var s := [0x63, 0x61, 0x73, 0x65, 0x41];
    assert s == UTF8.EncodeAscii("caseA");
    s

  const CASE_B : UTF8.ValidUTF8Bytes :=
    var s := [0x63, 0x61, 0x73, 0x65, 0x42];
    assert s == UTF8.EncodeAscii("caseB");
    s

  const BRANCH_KEY_ID_A := BRANCH_KEY_ID
  const BRANCH_KEY_ID_B := Fixtures.branchKeyIdWithEC

  method GetTestMaterials(suiteId: Types.AlgorithmSuiteId) returns (out: Types.EncryptionMaterials)
  {
    var mpl :- expect MaterialProviders.MaterialProviders();

    var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);
    var suite := AlgorithmSuites.GetSuite(suiteId);
    // Add data key to test the case where i have a pdk
    var encryptionMaterialsIn :- expect mpl.InitializeEncryptionMaterials(
      Types.InitializeEncryptionMaterialsInput(
        algorithmSuiteId := suiteId,
        encryptionContext := encryptionContext,
        requiredEncryptionContextKeys := [],
        signingKey := None,
        verificationKey := None
      )
    );

    return encryptionMaterialsIn;
  }

  method {:test} TestHierarchyClientESDKSuite()
  {
    var branchKeyId := BRANCH_KEY_ID;
    // TTL = 166.67 hours
    var ttl : Types.PositiveLong := (1 * 60000) * 10;
    var mpl :- expect MaterialProviders.MaterialProviders();

    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := KeyStoreTypes.KMSConfiguration.kmsKeyArn(keyArn);

    var keyStoreConfig := KeyStoreTypes.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var hierarchyKeyring :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyId),
        branchKeyIdSupplier := None,
        keyStore := keyStore,
        ttlSeconds := ttl,
        cache := None,
        partitionId := None
      )
    );

    var materials := GetTestMaterials(TEST_ESDK_ALG_SUITE_ID);
    TestRoundtrip(hierarchyKeyring, materials, TEST_ESDK_ALG_SUITE_ID, branchKeyId);

    //Test with key in the materials
    var suite := AlgorithmSuites.GetSuite(TEST_ESDK_ALG_SUITE_ID);
    var zeroedKey := seq(AlgorithmSuites.GetEncryptKeyLength(suite) as nat, _ => 0); // Key is Zero
    materials := materials.(plaintextDataKey := Some(zeroedKey));
    TestRoundtrip(hierarchyKeyring, materials, TEST_ESDK_ALG_SUITE_ID, branchKeyId);
  }

  method {:test} TestHierarchyClientDBESuite() {
    var branchKeyId := BRANCH_KEY_ID;
    // TTL = 166.67 hours
    var ttl : Types.PositiveLong := (1 * 60000) * 10;
    var mpl :- expect MaterialProviders.MaterialProviders();

    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := KeyStoreTypes.KMSConfiguration.kmsKeyArn(keyArn);

    var keyStoreConfig := KeyStoreTypes.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var hierarchyKeyring :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyId),
        branchKeyIdSupplier := None,
        keyStore := keyStore,
        ttlSeconds := ttl,
        cache := None,
        partitionId := None
      )
    );

    var materials := GetTestMaterials(TEST_DBE_ALG_SUITE_ID);
    TestRoundtrip(hierarchyKeyring, materials, TEST_DBE_ALG_SUITE_ID, branchKeyId);

    //Test with key in the materials
    var suite := AlgorithmSuites.GetSuite(TEST_DBE_ALG_SUITE_ID);
    var zeroedKey := seq(AlgorithmSuites.GetEncryptKeyLength(suite) as nat, _ => 0); // Key is Zero
    materials := materials.(plaintextDataKey := Some(zeroedKey));
    TestRoundtrip(hierarchyKeyring, materials, TEST_DBE_ALG_SUITE_ID, branchKeyId);
  }

  method {:test} TestBranchKeyIdSupplier()
  {
    var branchKeyIdSupplier: Types.IBranchKeyIdSupplier := new DummyBranchKeyIdSupplier();
    // TTL = 166.67 hours
    var ttl : int64 := (1 * 60000) * 10;
    var mpl :- expect MaterialProviders.MaterialProviders();

    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := KeyStoreTypes.KMSConfiguration.kmsKeyArn(keyArn);

    var keyStoreConfig := KeyStoreTypes.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var hierarchyKeyring :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := None,
        branchKeyIdSupplier := Some(branchKeyIdSupplier),
        keyStore := keyStore,
        ttlSeconds := ttl,
        cache := None,
        partitionId := None
      )
    );

    // Test Encryption Context with Case A
    var materials := GetTestMaterials(TEST_DBE_ALG_SUITE_ID);
    var contextCaseA := materials.encryptionContext[BRANCH_KEY := CASE_A];
    materials := materials.(encryptionContext := contextCaseA);
    TestRoundtrip(hierarchyKeyring, materials, TEST_DBE_ALG_SUITE_ID, BRANCH_KEY_ID_A);

    // Test Encryption Context with Case B
    var contextCaseB := materials.encryptionContext[BRANCH_KEY := CASE_B];
    materials := materials.(encryptionContext := contextCaseB);
    TestRoundtrip(hierarchyKeyring, materials, TEST_DBE_ALG_SUITE_ID, BRANCH_KEY_ID_B);
  }

  method {:test} TestInvalidDataKeyError()
  {
    var branchKeyIdSupplier: Types.IBranchKeyIdSupplier := new DummyBranchKeyIdSupplier();
    // TTL = 166.67 hours
    var ttl : int64 := (1 * 60000) * 10;
    var mpl :- expect MaterialProviders.MaterialProviders();
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := KeyStoreTypes.KMSConfiguration.kmsKeyArn(keyArn);
    var keyStoreConfig := KeyStoreTypes.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );
    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
    var hierarchyKeyring :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := None,
        branchKeyIdSupplier := Some(branchKeyIdSupplier),
        keyStore := keyStore,
        ttlSeconds := ttl,
        cache := None,
        partitionId := None
      )
    );
    var materials := GetTestMaterials(TEST_DBE_ALG_SUITE_ID);
    var contextCaseA := materials.encryptionContext[BRANCH_KEY := CASE_A];
    var contextCaseB := materials.encryptionContext[BRANCH_KEY := CASE_B];
    var materialsA := materials.(encryptionContext := contextCaseA);
    var materialsB := materials.(encryptionContext := contextCaseB);

    TestInvalidDataKeyFailureCase(hierarchyKeyring, materialsA, materialsB, TEST_DBE_ALG_SUITE_ID);
  }

  method TestInvalidDataKeyFailureCase(
    hierarchyKeyring: Types.IKeyring,
    encryptionMaterialsInEncrypt: Types.EncryptionMaterials,
    encryptionMaterialsInDecrypt: Types.EncryptionMaterials,
    algorithmSuiteId: Types.AlgorithmSuiteId
  )
    requires hierarchyKeyring.ValidState()
    modifies hierarchyKeyring.Modifies
    ensures hierarchyKeyring.ValidState()
  {
    var encryptionMaterialsOut :- expect hierarchyKeyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsInEncrypt)
    );

    var mpl :- expect MaterialProviders.MaterialProviders();
    var _ :- expect mpl.EncryptionMaterialsHasPlaintextDataKey(encryptionMaterialsOut.materials);

    expect |encryptionMaterialsOut.materials.encryptedDataKeys| == 1;

    var edk := encryptionMaterialsOut.materials.encryptedDataKeys[0];

    var decryptionMaterialsIn :- expect mpl.InitializeDecryptionMaterials(
      Types.InitializeDecryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionMaterialsInDecrypt.encryptionContext,
        requiredEncryptionContextKeys := []
      )
    );
    var decryptionMaterialsOut := hierarchyKeyring.OnDecrypt(
      Types.OnDecryptInput(
        materials:=decryptionMaterialsIn,
        encryptedDataKeys:=[edk]
      )
    );
    expect decryptionMaterialsOut.IsFailure();
    expect decryptionMaterialsOut.error.AwsCryptographicMaterialProvidersException?;
    var expectedErrorMessage :- expect ErrorMessages.IncorrectDataKeys([edk],decryptionMaterialsIn.algorithmSuite);
    expect decryptionMaterialsOut.error.message == expectedErrorMessage;
  }

  method TestRoundtrip(
    hierarchyKeyring: Types.IKeyring,
    encryptionMaterialsIn: Types.EncryptionMaterials,
    algorithmSuiteId: Types.AlgorithmSuiteId,
    expectedBranchKeyId: string
  )
    requires hierarchyKeyring.ValidState()
    modifies hierarchyKeyring.Modifies
    ensures hierarchyKeyring.ValidState()
  {
    var encryptionMaterialsOut :- expect hierarchyKeyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );

    var mpl :- expect MaterialProviders.MaterialProviders();
    var _ :- expect mpl.EncryptionMaterialsHasPlaintextDataKey(encryptionMaterialsOut.materials);

    expect |encryptionMaterialsOut.materials.encryptedDataKeys| == 1;

    var edk := encryptionMaterialsOut.materials.encryptedDataKeys[0];

    // Verify the edk was created with the expected branch key
    var expectedBranchKeyIdUTF8 :- expect UTF8.Encode(expectedBranchKeyId);
    expect edk.keyProviderInfo == expectedBranchKeyIdUTF8;

    var decryptionMaterialsIn :- expect mpl.InitializeDecryptionMaterials(
      Types.InitializeDecryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionMaterialsIn.encryptionContext,
        requiredEncryptionContextKeys := []
      )
    );
    var decryptionMaterialsOut :- expect hierarchyKeyring.OnDecrypt(
      Types.OnDecryptInput(
        materials:=decryptionMaterialsIn,
        encryptedDataKeys:=[edk]
      )
    );

    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#ondecrypt
    //= type=test
    //# If a decryption succeeds, this keyring MUST add the resulting
    //# plaintext data key to the decryption materials and return the
    //# modified materials.
    expect encryptionMaterialsOut.materials.plaintextDataKey
        == decryptionMaterialsOut.materials.plaintextDataKey;
  }

  method {:test} TestSharedCacheWithSamePartitionIdAndSameLogicalKeyStoreName()
  {
    var branchKeyIdWest := BRANCH_KEY_ID;
    // TTL = 166.67 hours
    var ttl : Types.PositiveLong := (1 * 60000) * 10;
    var mpl :- expect MaterialProviders.MaterialProviders();

    var regionWest := "us-west-2";
    var regionEast := "us-east-2";

    var kmsClientWest :- expect KMS.KMSClientForRegion(regionWest);
    var kmsClientEast :- expect KMS.KMSClientForRegion(regionEast);
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := KeyStoreTypes.KMSConfiguration.kmsKeyArn(keyArn);

    // Create a Key Store with the a KMS configuration and
    // KMS client for a particular region (us-west-2 in this case)
    // with a logicalKeyStoreName
    var keyStoreConfigClientRegionWest := KeyStoreTypes.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClientWest)
    );

    var keyStoreClientRegionWest :- expect KeyStore.KeyStore(keyStoreConfigClientRegionWest);

    // Create a key store with the same branch key store and
    // KMS key configuration but with different client region
    // (us-east-2 in this case)
    // with the same logicalKeyStoreName as keyStoreConfigClientRegionWest
    var keyStoreConfigClientRegionEast := KeyStoreTypes.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClientEast)
    );

    var keyStoreClientRegionEast :- expect KeyStore.KeyStore(keyStoreConfigClientRegionEast);

    // Initialize the shared Cryptographic Materials Cache
    var sharedCacheInput :- expect mpl.CreateCryptographicMaterialsCache(
      Types.CreateCryptographicMaterialsCacheInput(
        cache := Types.CacheType.Default(
          Types.DefaultCache(
            entryCapacity := 100
          )
        )
      )
    );

    // Wrap the initialized shared Cryptographic Materials Cache as a `Shared` CacheType object
    var sharedCache := Types.CacheType.Shared(
      sharedCacheInput
    );

    // Create a Hierarchy Keyring HK1 with branchKeyIdWest,
    // keyStoreClientRegionWest and the shared cache `sharedCache`
    // with a partitionId
    var hierarchyKeyring1 :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyIdWest),
        branchKeyIdSupplier := None,
        keyStore := keyStoreClientRegionWest,
        ttlSeconds := ttl,
        cache := Some(sharedCache),
        partitionId := Some("partitionId")
      )
    );

    // Create a Hierarchy Keyring HK2 with branchKeyIdWest,
    // keyStoreClientRegionEast and the shared cache `sharedCache`
    // with the same partitionId as hierarchyKeyring1
    var hierarchyKeyring2 :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyIdWest),
        branchKeyIdSupplier := None,
        keyStore := keyStoreClientRegionEast,
        ttlSeconds := ttl,
        cache := Some(sharedCache),
        partitionId := Some("partitionId")
      )
    );

    // Get test materials
    var materials := GetTestMaterials(TEST_ESDK_ALG_SUITE_ID);

    // Commenting these tests out because these are ghost fields and cannot be added for now
    // Ensure that there are 0 KMS Decrypt and 0 DynamoDB GetItem calls until now
    // expect |kmsClientEast.History.Decrypt| == 0;
    // expect |kmsClientWest.History.Decrypt| == 0;
    // expect |ddbClient.History.GetItem| == 0;

    // Try encrypting the test materials with HK2, which has branchKeyIdWest
    // but its keystore is keyStoreClientRegionEast
    var encryptionMaterialsOutMismatchedRegion := hierarchyKeyring2.OnEncrypt(
      Types.OnEncryptInput(materials:=materials)
    );

    // This encryption should fail because of region mismatch
    expect encryptionMaterialsOutMismatchedRegion.IsFailure();

    // Commenting these tests out because these are ghost fields and cannot be added for now
    // Ensure that there are 1 KMS Decrypt calls for kmsClientEast, 0 for KMSClientWest and
    // 1 DynamoDB GetItem calls until now
    // expect |kmsClientEast.History.Decrypt| == 1;
    // expect |kmsClientWest.History.Decrypt| == 0;
    // expect |ddbClient.History.GetItem| == 1;

    // Encrypt and Decrypt round trip for the test materials with HK1,
    // which has branchKeyIdWest and its keystore is keyStoreClientRegionWest
    // This should pass
    TestRoundtrip(hierarchyKeyring1, materials, TEST_ESDK_ALG_SUITE_ID, branchKeyIdWest);

    // Commenting these tests out because these are ghost fields and cannot be added for now
    // Ensure that there are 1 KMS Decrypt calls for kmsClientEast, 2 for KMSClientWest and
    // 3 DynamoDB GetItem calls until now
    // expect |kmsClientEast.History.Decrypt| == 1;
    // expect |kmsClientWest.History.Decrypt| == 2;
    // expect |ddbClient.History.GetItem| == 3;

    // This should now pass because the material exists inside the cache.
    // This proves the cache entry from HK1 was hit by HK2.
    TestRoundtrip(hierarchyKeyring2, materials, TEST_ESDK_ALG_SUITE_ID, branchKeyIdWest);

    // Commenting these tests out because these are ghost fields and cannot be added for now
    // Ensure that the count doesn't change after the last round trip because the cached
    // entries are being used. That is, there are 1 KMS Decrypt calls for kmsClientEast,
    // 2 for KMSClientWest and 3 DynamoDB GetItem calls until now
    // expect |kmsClientEast.History.Decrypt| == 1;
    // expect |kmsClientWest.History.Decrypt| == 2;
    // expect |ddbClient.History.GetItem| == 3;
  }

  method {:test} TestSharedCacheWithDifferentUnspecifiedPartitionIdAndSameLogicalKeyStoreName()
  {
    var branchKeyIdWest := BRANCH_KEY_ID;
    // TTL = 166.67 hours
    var ttl : Types.PositiveLong := (1 * 60000) * 10;
    var mpl :- expect MaterialProviders.MaterialProviders();

    var regionWest := "us-west-2";
    var regionEast := "us-east-2";

    var kmsClientWest :- expect KMS.KMSClientForRegion(regionWest);
    var kmsClientEast :- expect KMS.KMSClientForRegion(regionEast);
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := KeyStoreTypes.KMSConfiguration.kmsKeyArn(keyArn);

    // Create a Key Store with the a KMS configuration and
    // KMS client for a particular region (us-west-2 in this case)
    // with a logicalKeyStoreName
    var keyStoreConfigClientRegionWest := KeyStoreTypes.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClientWest)
    );

    var keyStoreClientRegionWest :- expect KeyStore.KeyStore(keyStoreConfigClientRegionWest);

    // Create a key store with the same branch key store and
    // KMS key configuration but with different client region
    // (us-east-2 in this case)
    // with the same logicalKeyStoreName as keyStoreConfigClientRegionWest
    var keyStoreConfigClientRegionEast := KeyStoreTypes.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClientEast)
    );

    var keyStoreClientRegionEast :- expect KeyStore.KeyStore(keyStoreConfigClientRegionEast);

    // Initialize the shared Cryptographic Materials Cache
    var sharedCacheInput :- expect mpl.CreateCryptographicMaterialsCache(
      Types.CreateCryptographicMaterialsCacheInput(
        cache := Types.CacheType.Default(
          Types.DefaultCache(
            entryCapacity := 100
          )
        )
      )
    );

    // Wrap the initialized shared Cryptographic Materials Cache as a `Shared` CacheType object
    var sharedCache := Types.CacheType.Shared(
      sharedCacheInput
    );

    // Create a Hierarchy Keyring HK1 with branchKeyIdWest,
    // keyStoreClientRegionWest and the shared cache `sharedCache`
    // without specifying the partitionId, so that it is initialized to a random UUID
    var hierarchyKeyring1 :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyIdWest),
        branchKeyIdSupplier := None,
        keyStore := keyStoreClientRegionWest,
        ttlSeconds := ttl,
        cache := Some(sharedCache),
        partitionId := None
      )
    );

    // Create a Hierarchy Keyring HK2 with branchKeyIdWest,
    // keyStoreClientRegionEast and the shared cache `sharedCache`
    // without specifying the partitionId, so that it is initialized to a random UUID
    var hierarchyKeyring2 :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyIdWest),
        branchKeyIdSupplier := None,
        keyStore := keyStoreClientRegionEast,
        ttlSeconds := ttl,
        cache := Some(sharedCache),
        partitionId := None
      )
    );

    // Get test materials
    var materials := GetTestMaterials(TEST_ESDK_ALG_SUITE_ID);

    // Try encrypting the test materials with HK2, which has branchKeyIdWest
    // but its keystore is keyStoreClientRegionEast
    var encryptionMaterialsOutMismatchedRegion := hierarchyKeyring2.OnEncrypt(
      Types.OnEncryptInput(materials:=materials)
    );

    // This encryption should fail because of region mismatch
    expect encryptionMaterialsOutMismatchedRegion.IsFailure();

    // Encrypt and Decrypt round trip for the test materials with HK1,
    // which has branchKeyIdWest and its keystore is keyStoreClientRegionWest
    // This should pass
    TestRoundtrip(hierarchyKeyring1, materials, TEST_ESDK_ALG_SUITE_ID, branchKeyIdWest);

    // Again, try encrypting the test materials with HK2, which has branchKeyIdWest
    // but its keystore is keyStoreClientRegionEast
    var encryptionMaterialsOutMismatchedRegionFromCache := hierarchyKeyring2.OnEncrypt(
      Types.OnEncryptInput(materials:=materials)
    );

    // This encryption should fail because the partition IDs for HK1 and HK2 are different
    // even though the partition IDs are unspecified. In such a case, partition IDs are
    // initialized as UUIDs which have negligible probability of collision.
    // This proves the cache was missed.
    expect encryptionMaterialsOutMismatchedRegionFromCache.IsFailure();
  }

  method {:test} TestSharedCacheWithDifferentSpecifiedPartitionIdAndSameLogicalKeyStoreName()
  {
    var branchKeyIdWest := BRANCH_KEY_ID;
    // TTL = 166.67 hours
    var ttl : Types.PositiveLong := (1 * 60000) * 10;
    var mpl :- expect MaterialProviders.MaterialProviders();

    var regionWest := "us-west-2";
    var regionEast := "us-east-2";

    var kmsClientWest :- expect KMS.KMSClientForRegion(regionWest);
    var kmsClientEast :- expect KMS.KMSClientForRegion(regionEast);
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := KeyStoreTypes.KMSConfiguration.kmsKeyArn(keyArn);

    // Create a Key Store with the a KMS configuration and
    // KMS client for a particular region (us-west-2 in this case)
    // with a logicalKeyStoreName
    var keyStoreConfigClientRegionWest := KeyStoreTypes.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClientWest)
    );

    var keyStoreClientRegionWest :- expect KeyStore.KeyStore(keyStoreConfigClientRegionWest);

    // Create a key store with the same branch key store and
    // KMS key configuration but with different client region
    // (us-east-2 in this case)
    // with the same logicalKeyStoreName as keyStoreConfigClientRegionWest
    var keyStoreConfigClientRegionEast := KeyStoreTypes.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClientEast)
    );

    var keyStoreClientRegionEast :- expect KeyStore.KeyStore(keyStoreConfigClientRegionEast);

    // Initialize the shared Cryptographic Materials Cache
    var sharedCacheInput :- expect mpl.CreateCryptographicMaterialsCache(
      Types.CreateCryptographicMaterialsCacheInput(
        cache := Types.CacheType.Default(
          Types.DefaultCache(
            entryCapacity := 100
          )
        )
      )
    );

    // Wrap the shared Cryptographic Materials Cache as a `Shared` CacheType object
    var sharedCache := Types.CacheType.Shared(
      sharedCacheInput
    );

    // Create a Hierarchy Keyring HK1 with branchKeyIdWest,
    // keyStoreClientRegionWest and the shared cache `sharedCache`
    // with a partitionId "partitionIdHK1"
    var hierarchyKeyring1 :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyIdWest),
        branchKeyIdSupplier := None,
        keyStore := keyStoreClientRegionWest,
        ttlSeconds := ttl,
        cache := Some(sharedCache),
        partitionId := Some("partitionIdHK1")
      )
    );

    // Create a Hierarchy Keyring HK2 with branchKeyIdWest,
    // keyStoreClientRegionEast and the shared cache `sharedCache`
    // with a partitionId different than hierarchyKeyring1, which
    // in this case is "partitionIdHK2"
    var hierarchyKeyring2 :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyIdWest),
        branchKeyIdSupplier := None,
        keyStore := keyStoreClientRegionEast,
        ttlSeconds := ttl,
        cache := Some(sharedCache),
        partitionId := Some("partitionIdHK2")
      )
    );

    // Get test materials
    var materials := GetTestMaterials(TEST_ESDK_ALG_SUITE_ID);

    // Try encrypting the test materials with HK2, which has branchKeyIdWest
    // but its keystore is keyStoreClientRegionEast
    var encryptionMaterialsOutMismatchedRegion := hierarchyKeyring2.OnEncrypt(
      Types.OnEncryptInput(materials:=materials)
    );

    // This encryption should fail because of region mismatch
    expect encryptionMaterialsOutMismatchedRegion.IsFailure();

    // Encrypt and Decrypt round trip for the test materials with HK1,
    // which has branchKeyIdWest and its keystore is keyStoreClientRegionWest
    // This should pass
    TestRoundtrip(hierarchyKeyring1, materials, TEST_ESDK_ALG_SUITE_ID, branchKeyIdWest);

    // Again, try encrypting the test materials with HK2, which has branchKeyIdWest
    // but its keystore is keyStoreClientRegionEast
    var encryptionMaterialsOutMismatchedRegionFromCache := hierarchyKeyring2.OnEncrypt(
      Types.OnEncryptInput(materials:=materials)
    );

    // This encryption should fail because the partition IDs for HK1 and HK2 are different
    expect encryptionMaterialsOutMismatchedRegionFromCache.IsFailure();
  }

  method {:test} TestSharedCacheWithSamePartitionIdAndDifferentLogicalKeyStoreName()
  {
    var branchKeyIdWest := BRANCH_KEY_ID;
    // TTL = 166.67 hours
    var ttl : Types.PositiveLong := (1 * 60000) * 10;
    var mpl :- expect MaterialProviders.MaterialProviders();

    var regionWest := "us-west-2";
    var regionEast := "us-east-2";

    var kmsClientWest :- expect KMS.KMSClientForRegion(regionWest);
    var kmsClientEast :- expect KMS.KMSClientForRegion(regionEast);
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := KeyStoreTypes.KMSConfiguration.kmsKeyArn(keyArn);

    // Different logical key store names for both Key Stores
    var logicalKeyStoreName : DDBTypes.TableName := logicalKeyStoreName;
    var logicalKeyStoreNameNew : DDBTypes.TableName := logicalKeyStoreName + "New";

    // Create a Key Store with the a KMS configuration and
    // KMS client for a particular region (us-west-2 in this case)
    // with a logicalKeyStoreName
    var keyStoreConfigClientRegionWest := KeyStoreTypes.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClientWest)
    );

    var keyStoreClientRegionWest :- expect KeyStore.KeyStore(keyStoreConfigClientRegionWest);

    // Create a key store with the same branch key store and
    // KMS key configuration but with different client region
    // (us-east-2 in this case)
    // with a different logicalKeyStoreName as compared to keyStoreConfigClientRegionWest
    // which is logicalKeyStoreNameNew in this case
    var keyStoreConfigClientRegionEast := KeyStoreTypes.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreNameNew,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClientEast)
    );

    var keyStoreClientRegionEast :- expect KeyStore.KeyStore(keyStoreConfigClientRegionEast);

    // Initialize the shared Cryptographic Materials Cache
    var sharedCacheInput :- expect mpl.CreateCryptographicMaterialsCache(
      Types.CreateCryptographicMaterialsCacheInput(
        cache := Types.CacheType.Default(
          Types.DefaultCache(
            entryCapacity := 100
          )
        )
      )
    );

    // Wrap the initialized shared Cryptographic Materials Cache as a `Shared` CacheType object
    var sharedCache := Types.CacheType.Shared(
      sharedCacheInput
    );

    // Create a Hierarchy Keyring HK1 with branchKeyIdWest,
    // keyStoreClientRegionWest and the shared cache `sharedCache`
    // with a partitionId
    var hierarchyKeyring1 :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyIdWest),
        branchKeyIdSupplier := None,
        keyStore := keyStoreClientRegionWest,
        ttlSeconds := ttl,
        cache := Some(sharedCache),
        partitionId := Some("partitionId")
      )
    );

    // Create a Hierarchy Keyring HK2 with branchKeyIdWest,
    // keyStoreClientRegionEast and the shared cache `sharedCache`
    // with the same partitionId as hierarchyKeyring1
    var hierarchyKeyring2 :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyIdWest),
        branchKeyIdSupplier := None,
        keyStore := keyStoreClientRegionEast,
        ttlSeconds := ttl,
        cache := Some(sharedCache),
        partitionId := Some("partitionId")
      )
    );

    // Get test materials
    var materials := GetTestMaterials(TEST_ESDK_ALG_SUITE_ID);

    // Try encrypting the test materials with HK2, which has branchKeyIdWest
    // but its keystore is keyStoreClientRegionEast
    var encryptionMaterialsOutMismatchedRegion := hierarchyKeyring2.OnEncrypt(
      Types.OnEncryptInput(materials:=materials)
    );

    // This encryption should fail because of region mismatch
    expect encryptionMaterialsOutMismatchedRegion.IsFailure();

    // Encrypt and Decrypt round trip for the test materials with HK1,
    // which has branchKeyIdWest and its keystore is keyStoreClientRegionWest
    // This should pass
    TestRoundtrip(hierarchyKeyring1, materials, TEST_ESDK_ALG_SUITE_ID, branchKeyIdWest);

    // Again, try encrypting the test materials with HK2, which has branchKeyIdWest
    // but its keystore is keyStoreClientRegionEast
    var encryptionMaterialsOutMismatchedRegionFromCache := hierarchyKeyring2.OnEncrypt(
      Types.OnEncryptInput(materials:=materials)
    );

    // This encryption should fail because the logicalKeyStoreName for HK1 and HK2 are different
    expect encryptionMaterialsOutMismatchedRegionFromCache.IsFailure();
  }

  // Returns "hierarchy-test-v1" when EC contains kv pair "branchKey":"caseA"
  // Returns "hierarchy-test-active-active" when EC contains kv pair "branchKey":"caseB"
  // Otherwise returns a Failure
  class DummyBranchKeyIdSupplier extends Types.IBranchKeyIdSupplier
  {
    predicate ValidState()
      ensures ValidState() ==> History in Modifies
    {
      History in Modifies
    }

    constructor()
      ensures ValidState() && fresh(this) && fresh(History) && fresh(Modifies)
    {
      History := new Types.IBranchKeyIdSupplierCallHistory();
      Modifies := {History};
    }

    predicate GetBranchKeyIdEnsuresPublicly(input: Types.GetBranchKeyIdInput, output: Result<Types.GetBranchKeyIdOutput, Types.Error>)
    {true}

    method GetBranchKeyId'(input: Types.GetBranchKeyIdInput)
      returns (output: Result<Types.GetBranchKeyIdOutput, Types.Error>)
      requires ValidState()
      modifies Modifies - {History}
      decreases Modifies - {History}
      ensures ValidState()
      ensures GetBranchKeyIdEnsuresPublicly(input, output)
      ensures unchanged(History)
    {
      var context := input.encryptionContext;

      if BRANCH_KEY in context.Keys && context[BRANCH_KEY] == CASE_A {
        return Success(Types.GetBranchKeyIdOutput(branchKeyId:=BRANCH_KEY_ID_A));
      } else if BRANCH_KEY in context.Keys && context[BRANCH_KEY] == CASE_B {
        return Success(Types.GetBranchKeyIdOutput(branchKeyId:=BRANCH_KEY_ID_B));
      } else {
        return Failure(Types.AwsCryptographicMaterialProvidersException(message := "Can't determine branchKeyId from context"));
      }
    }
  }
}
