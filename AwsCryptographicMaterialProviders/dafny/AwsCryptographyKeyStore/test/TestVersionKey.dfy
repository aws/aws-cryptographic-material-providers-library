// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"
include "CleanupItems.dfy"

module TestVersionKey {
  import Types = AwsCryptographyKeyStoreTypes
  import ComAmazonawsKmsTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import KeyStore
  import UUID
  import opened StandardLibrary
  import opened Wrappers
  import opened AwsKmsUtils
  import opened Fixtures
  import CleanupItems
  import Structure
  import DDBKeystoreOperations

  method {:test} TestVersionKey()
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

    // Create a new key
    // We will create a use this new key per run to avoid tripping up
    // when running in different runtimes
    var branchKeyId :- expect keyStore.CreateKey(Types.CreateKeyInput(
                                                   branchKeyIdentifier := None,
                                                   encryptionContext := None
                                                 ));

    var oldActiveResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var oldActiveVersion :- expect UTF8.Decode(oldActiveResult.branchKeyMaterials.branchKeyVersion);

    var versionKeyResult :- expect keyStore.VersionKey(
      Types.VersionKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var getBranchKeyVersionResult :- expect keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier,
        // We get the old active key by using the version
        branchKeyVersion := oldActiveVersion
      )
    );

    var newActiveResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var newActiveVersion :- expect UTF8.Decode(newActiveResult.branchKeyMaterials.branchKeyVersion);

    // Since this process uses a read DDB table,
    // the number of records will forever increase.
    // To avoid this, remove the items.
    CleanupItems.DeleteVersion(branchKeyId.branchKeyIdentifier, newActiveVersion, ddbClient);
    CleanupItems.DeleteVersion(branchKeyId.branchKeyIdentifier, oldActiveVersion, ddbClient);
    CleanupItems.DeleteActive(branchKeyId.branchKeyIdentifier, ddbClient);

    // We expect that getting the old active key has the same version as getting a branch key through the get version key api
    expect getBranchKeyVersionResult.branchKeyMaterials.branchKeyVersion == oldActiveResult.branchKeyMaterials.branchKeyVersion;
    expect getBranchKeyVersionResult.branchKeyMaterials.branchKey == oldActiveResult.branchKeyMaterials.branchKey;
    // We expect that if we rotate the branch key, the returned materials MUST NOT be equal to the previous active key.
    expect getBranchKeyVersionResult.branchKeyMaterials.branchKeyVersion != newActiveResult.branchKeyMaterials.branchKeyVersion;
    expect getBranchKeyVersionResult.branchKeyMaterials.branchKey != newActiveResult.branchKeyMaterials.branchKey;
  }

  method {:test} TestMrkVersionKey()
  {
    var ddbClient :- expect DDB.DynamoDBClient();

    var eastKeyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := KmsMrkConfigEast,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient)
    );

    var westKeyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := KmsMrkConfigWest,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient)
    );

    var eastKeyStore :- expect KeyStore.KeyStore(eastKeyStoreConfig);
    var westKeyStore :- expect KeyStore.KeyStore(westKeyStoreConfig);

    // Create a new key with the WEST key store
    // We will create a use this new key per run to avoid tripping up
    // when running in different runtimes
    var branchKeyId :- expect westKeyStore.CreateKey(Types.CreateKeyInput(
                                                       branchKeyIdentifier := None,
                                                       encryptionContext := None
                                                     ));

    var oldActiveResult :- expect westKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var oldActiveVersion :- expect UTF8.Decode(oldActiveResult.branchKeyMaterials.branchKeyVersion);

    // Version the key with the EAST key store
    var versionKeyResult :- expect eastKeyStore.VersionKey(
      Types.VersionKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var getBranchKeyVersionResultWest :- expect westKeyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier,
        // We get the old active key by using the version
        branchKeyVersion := oldActiveVersion
      )
    );

    var getBranchKeyVersionResultEast :- expect eastKeyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier,
        // We get the old active key by using the version
        branchKeyVersion := oldActiveVersion
      )
    );
    if (getBranchKeyVersionResultWest != getBranchKeyVersionResultEast) {
      print "getBranchKeyVersionResultWest\n", getBranchKeyVersionResultWest, "\n";
      print "getBranchKeyVersionResultEast\n", getBranchKeyVersionResultEast, "\n";
    }
    expect getBranchKeyVersionResultWest == getBranchKeyVersionResultEast;

    var newActiveResultWest :- expect westKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));
    var newActiveResultEast :- expect eastKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    expect newActiveResultWest == newActiveResultEast;

    var newActiveVersionWest :- expect UTF8.Decode(newActiveResultWest.branchKeyMaterials.branchKeyVersion);
    var newActiveVersionEast :- expect UTF8.Decode(newActiveResultEast.branchKeyMaterials.branchKeyVersion);
    expect newActiveVersionWest == newActiveVersionEast;

    // Since this process uses a read DDB table,
    // the number of records will forever increase.
    // To avoid this, remove the items.
    CleanupItems.DeleteVersion(branchKeyId.branchKeyIdentifier, newActiveVersionEast, ddbClient);
    CleanupItems.DeleteVersion(branchKeyId.branchKeyIdentifier, oldActiveVersion, ddbClient);
    CleanupItems.DeleteActive(branchKeyId.branchKeyIdentifier, ddbClient);

    // We expect that getting the old active key has the same version as getting a branch key through the get version key api
    expect getBranchKeyVersionResultEast.branchKeyMaterials.branchKeyVersion == oldActiveResult.branchKeyMaterials.branchKeyVersion;
    expect getBranchKeyVersionResultEast.branchKeyMaterials.branchKey == oldActiveResult.branchKeyMaterials.branchKey;
    // We expect that if we rotate the branch key, the returned materials MUST NOT be equal to the previous active key.
    expect getBranchKeyVersionResultEast.branchKeyMaterials.branchKeyVersion != newActiveResultEast.branchKeyMaterials.branchKeyVersion;
    expect getBranchKeyVersionResultEast.branchKeyMaterials.branchKey != newActiveResultEast.branchKeyMaterials.branchKey;
  }

  method {:test} InsertingADuplicateVersionWillFail()
  {
    var ddbClient :- expect DDB.DynamoDBClient();

    var encryptionContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
      branchKeyId,
      branchKeyIdActiveVersion,
      "",
      "",
      keyArn,
      map[]
    );

    var output := DDBKeystoreOperations.WriteNewBranchKeyVersionToKeystore(
      Structure.ToAttributeMap(encryptionContext, [1]),
      Structure.ToAttributeMap(Structure.ActiveBranchKeyEncryptionContext(encryptionContext), [2]),
      branchKeyStoreName,
      ddbClient
    );

    expect output.Failure?;
  }

  method {:test} VersioningANonexistentBranchKeyWillFail()
  {
    var ddbClient :- expect DDB.DynamoDBClient();

    var encryptionContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
      "!= branchKeyId",
      branchKeyIdActiveVersion,
      "",
      "",
      keyArn,
      map[]
    );

    var output := DDBKeystoreOperations.WriteNewBranchKeyVersionToKeystore(
      Structure.ToAttributeMap(encryptionContext, [1]),
      Structure.ToAttributeMap(Structure.ActiveBranchKeyEncryptionContext(encryptionContext), [2]),
      branchKeyStoreName,
      ddbClient
    );

    expect output.Failure?;
  }

}
