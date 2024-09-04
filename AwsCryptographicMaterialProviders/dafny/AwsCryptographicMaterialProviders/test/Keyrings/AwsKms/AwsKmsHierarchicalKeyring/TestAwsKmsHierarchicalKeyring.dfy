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
  import Aws.Cryptography.Primitives
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
  const WEST_BRANCH_KEY_ID := Fixtures.WestBranchKey
  const EAST_BRANCH_KEY_ID := Fixtures.EastBranchKey

  // Constants for TestBranchKeySupplier
  const BRANCH_KEY := UTF8.EncodeAscii("branchKey")
  const CASE_A := UTF8.EncodeAscii("caseA")
  const CASE_B := UTF8.EncodeAscii("caseB")
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
        cache := None
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
        cache := None
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
        cache := None
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
        cache := None
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

  method {:test} TestSharedCacheWithSamePartitionId()
  {
    var branchKeyIdWest := WEST_BRANCH_KEY_ID;
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

    // Initialize the Cryptographic Materials Cache
    var initializedCacheInput :- expect mpl.CreateCryptographicMaterialsCache(
      Types.CreateCryptographicMaterialsCacheInput(
        cache := Types.CacheType.Default(
          Types.DefaultCache(
            entryCapacity := 100
          )
        )
      )
    );

    // Wrap the initialized Cryptographic Materials Cache as an `Initialized` CacheType object
    var initializedCache := Types.CacheType.Initialized(
      initializedCacheInput
    );

    // Create a Hierarchy Keyring HK1 with branchKeyIdWest,
    // keyStoreClientRegionWest and the initialized cache initializedCache
    var hierarchyKeyring1 :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyIdWest),
        branchKeyIdSupplier := None,
        keyStore := keyStoreClientRegionWest,
        ttlSeconds := ttl,
        cache := Some(initializedCache),
        partitionId := Some("partitionId")
      )
    );

    // Create a Hierarchy Keyring HK2 with branchKeyIdWest,
    // keyStoreClientRegionEast and the initialized cache initializedCache
    var hierarchyKeyring2 :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyIdWest),
        branchKeyIdSupplier := None,
        keyStore := keyStoreClientRegionEast,
        ttlSeconds := ttl,
        cache := Some(initializedCache),
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


    // This should now pass because the material exists inside the cache
    TestRoundtrip(hierarchyKeyring2, materials, TEST_ESDK_ALG_SUITE_ID, branchKeyIdWest);
  }

  method {:test} TestSharedCacheWithDifferentUnspecifiedPartitionId()
  {
    var branchKeyIdWest := WEST_BRANCH_KEY_ID;
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

    // Initialize the Cryptographic Materials Cache
    var initializedCacheInput :- expect mpl.CreateCryptographicMaterialsCache(
      Types.CreateCryptographicMaterialsCacheInput(
        cache := Types.CacheType.Default(
          Types.DefaultCache(
            entryCapacity := 100
          )
        )
      )
    );

    // Wrap the initialized Cryptographic Materials Cache as an `Initialized` CacheType object
    var initializedCache := Types.CacheType.Initialized(
      initializedCacheInput
    );

    // Create a Hierarchy Keyring HK1 with branchKeyIdWest,
    // keyStoreClientRegionWest and the initialized cache initializedCache
    var hierarchyKeyring1 :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyIdWest),
        branchKeyIdSupplier := None,
        keyStore := keyStoreClientRegionWest,
        ttlSeconds := ttl,
        cache := Some(initializedCache)
      )
    );

    // Create a Hierarchy Keyring HK2 with branchKeyIdWest,
    // keyStoreClientRegionEast and the initialized cache initializedCache
    var hierarchyKeyring2 :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyIdWest),
        branchKeyIdSupplier := None,
        keyStore := keyStoreClientRegionEast,
        ttlSeconds := ttl,
        cache := Some(initializedCache)
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
    // initialized as UUIDs which have negligible probability of collision
    expect encryptionMaterialsOutMismatchedRegionFromCache.IsFailure();
  }

  method {:test} TestSharedCacheWithDifferentSpecifiedPartitionId()
  {
    var branchKeyIdWest := WEST_BRANCH_KEY_ID;
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

    // Initialize the Cryptographic Materials Cache
    var initializedCacheInput :- expect mpl.CreateCryptographicMaterialsCache(
      Types.CreateCryptographicMaterialsCacheInput(
        cache := Types.CacheType.Default(
          Types.DefaultCache(
            entryCapacity := 100
          )
        )
      )
    );

    // Wrap the initialized Cryptographic Materials Cache as an `Initialized` CacheType object
    var initializedCache := Types.CacheType.Initialized(
      initializedCacheInput
    );

    // Create a Hierarchy Keyring HK1 with branchKeyIdWest,
    // keyStoreClientRegionWest and the initialized cache initializedCache
    var hierarchyKeyring1 :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyIdWest),
        branchKeyIdSupplier := None,
        keyStore := keyStoreClientRegionWest,
        ttlSeconds := ttl,
        cache := Some(initializedCache),
        partitionId := Some("partitionIdHK1")
      )
    );

    // Create a Hierarchy Keyring HK2 with branchKeyIdWest,
    // keyStoreClientRegionEast and the initialized cache initializedCache
    var hierarchyKeyring2 :- expect mpl.CreateAwsKmsHierarchicalKeyring(
      Types.CreateAwsKmsHierarchicalKeyringInput(
        branchKeyId := Some(branchKeyIdWest),
        branchKeyIdSupplier := None,
        keyStore := keyStoreClientRegionEast,
        ttlSeconds := ttl,
        cache := Some(initializedCache),
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
