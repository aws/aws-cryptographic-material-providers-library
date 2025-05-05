// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../AwsCryptographyKeyStore/test/BranchKeyValidators.dfy"
include "../src/KeyStoreAdminErrorMessages.dfy"
include "AdminFixtures.dfy"

module {:options "/functionSyntax:4" } TestAdminCreateKeys {
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreAdmin
  import KeyStore
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import ComAmazonawsKmsTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import DefaultKeyStorageInterface
  import KeyStoreErrorMessages
  import opened Wrappers
  import opened Fixtures
  import UUID
  import CleanupItems
  import AdminFixtures
  import BranchKeyValidators
  import KeyStoreAdminErrorMessages

  // TODO-HV-2-FOLLOW : TestCreateSRKForHV1, TestCreateForHV1NoBKID, TestCreateForHV1BbkidNoECFails

  const mrkCaseId := "test-mrk-case-admin-create-key-hv-1"
  method {:test} TestCreateMrkForHV1Succeeds()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var keyStoreEast :- expect KeyStoreFromKMSConfig(
      kmsConfig := KmsMrkConfigEast,
      ddbClient? := Some(ddbClient)
    );
    var uuid :- expect UUID.GenerateUUID();
    var bkid := mrkCaseId + "-west-mrk-" + uuid;
    // Create an HV-1 BK with a West MRK by calling us-west-2
    var bk :- expect underTest.CreateKey(
      Types.CreateKeyInput(
        Identifier := Some(bkid),
        EncryptionContext := Some(KmsMrkEC),
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(MrkArnWest),
        // us-west-2 b/c CI region is us-west-2 and KMS Client is created
        Strategy := Some(strategy)
      ));
    expect bk.Identifier == bkid;
    // Validate an HV-1 BK with a West MRK by calling us-east-1
    BranchKeyValidators.VerifyGetKeys(bkid, keyStoreEast, storage,
                                      encryptionContext := KmsMrkEC);
    var keyStoreWest :- expect KeyStoreFromKMSConfig(
      // Passing in KmsMrkConfigWest causes the KMS Client to be created for us-west-2
      // bk's KMS-ARN is replicated to us-west-2
      kmsConfig := KmsMrkConfigWest,
      ddbClient? := Some(ddbClient)
    );
    // Validate an HV-1 BK with a West MRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bkid, keyStoreWest, storage,
                                      encryptionContext := KmsMrkEC);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
  }

  // TODO-HV-2-M2?: Document that BKSA ONLY calls KMS/DDB for the region of the supplied clients.
  // or Ensure BKSA has similar behavior as BKS in terms of MRK region.
  const mrkCaseIdHV2 := "test-mrk-case-admin-create-key-hv-2"
  method {:test} TestCreateMRKForHV2Succeeds()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var keyStoreEast :- expect KeyStoreFromKMSConfig(
      kmsConfig := KmsMrkConfigEast,
      ddbClient? := Some(ddbClient)
    );
    var uuid :- expect UUID.GenerateUUID();
    var bkid := mrkCaseIdHV2 + "-west-mrk-" + uuid;
    // Create an HV-2 BK with a West MRK by calling us-west-2
    var bk :- expect underTest.CreateKey(
      Types.CreateKeyInput(
        Identifier := Some(bkid),
        EncryptionContext := Some(RobbieEC),
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(MrkArnWest),
        // us-west-2 b/c CI region is us-west-2 and KMS Client is created
        Strategy := Some(strategy),
        HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));
    expect bk.Identifier == bkid;
    // Validate an HV-2 BK with a West MRK by calling us-east-1
    BranchKeyValidators.VerifyGetKeys(bkid, keyStoreEast, storage,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2);
    var keyStoreWest :- expect KeyStoreFromKMSConfig(
      // Passing in KmsMrkConfigWest causes the KMS Client to be created for us-west-2
      // bk's KMS-ARN is replicated to us-west-2
      kmsConfig := KmsMrkConfigWest,
      ddbClient? := Some(ddbClient)
    );
    // Validate an HV-2 BK with a West MRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bkid, keyStoreWest, storage,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
  }

  const happyCaseIdHV2 := "test-happy-case-admin-create-key-hv-2"
  method {:test} TestCreateSRKForHV2()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var uuid :- expect UUID.GenerateUUID();
    var bkid := happyCaseIdHV2 + "-west-srk-" + uuid;
    // Create an HV-2 BK with a West SRK by calling us-west-2
    var bk :- expect underTest.CreateKey(
      Types.CreateKeyInput(
        Identifier := Some(bkid),
        EncryptionContext := Some(RobbieEC),
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        // us-west-2 b/c CI region is us-west-2 and KMS Client is created
        Strategy := Some(strategy),
        HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));
    expect bk.Identifier == bkid;
    // Validate an HV-2 BK with a West SRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bkid, keyStore, storage,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
  }

  method {:test} TestCreateSRKForHV2NoEC()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var bk :- expect underTest.CreateKey(
      Types.CreateKeyInput(
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        Strategy := Some(strategy),
        HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));
    BranchKeyValidators.VerifyGetKeys(bk.Identifier, keyStore, storage,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bk.Identifier, ddbClient:=ddbClient);
  }

  method {:test} TestCreateSRKForHV2BkidWithNoECFails()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var uuid :- expect UUID.GenerateUUID();
    var bkid := happyCaseIdHV2 + "-west-srk-no-ec-fails-" + uuid;
    var bk? := underTest.CreateKey(
      Types.CreateKeyInput(
        Identifier := Some(bkid),
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        Strategy := Some(strategy),
        HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));
    expect bk?.Failure?, "Admin CreateKey, with an Identifier, but no EC, MUST Fail";
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
  }

  const happyCaseIdHV1 := "test-happy-case-admin-create-key-hv-1"
  method {:test} TestCreateSrkForHV1()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var uuid :- expect UUID.GenerateUUID();
    var bkid := happyCaseIdHV1 + "-west-srk-" + uuid;
    // Create an HV-1 BK with a West MRK by calling us-west-2
    var bk :- expect underTest.CreateKey(
      Types.CreateKeyInput(
        Identifier := Some(bkid),
        EncryptionContext := Some(RobbieEC),
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        // us-west-2 b/c CI region is us-west-2 and KMS Client is created
        Strategy := Some(strategy)
      ));
    expect bk.Identifier == bkid;
    // Validate an HV-2 BK with a West SRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bkid, keyStore, storage,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v1);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
  }

  method {:test} TestCreateForHV1NoBKID()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var uuid :- expect UUID.GenerateUUID();
    // Create an HV-1 BK with a West MRK by calling us-west-2
    var bk :- expect underTest.CreateKey(
      Types.CreateKeyInput(
        Identifier := None(),
        EncryptionContext := Some(RobbieEC),
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        // us-west-2 b/c CI region is us-west-2 and KMS Client is created
        Strategy := Some(strategy)
      ));
    // Validate an HV-2 BK with a West SRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bk.Identifier, keyStore, storage,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v1);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bk.Identifier, ddbClient:=ddbClient);
  }

  method {:test} TestCreateHv1AndVersion()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var uuid :- expect UUID.GenerateUUID();
    // Create an HV-1 BK with a West MRK by calling us-west-2
    var bk :- expect underTest.CreateKey(
      Types.CreateKeyInput(
        Identifier := None(),
        EncryptionContext := Some(RobbieEC),
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        // us-west-2 b/c CI region is us-west-2 and KMS Client is created
        Strategy := Some(strategy)
      ));
    // Validate an HV-2 BK with a West SRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bk.Identifier, keyStore, storage,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v1);

    var versionedBk :- expect underTest.VersionKey(
      Types.VersionKeyInput(
        Identifier := bk.Identifier,
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        // us-west-2 b/c CI region is us-west-2 and KMS Client is created
        Strategy := Some(strategy)
      )
    );

    var _ := CleanupItems.DeleteBranchKey(Identifier:=bk.Identifier, ddbClient:=ddbClient);
  }

  method {:test} TestCreateHv2AndVersion()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var uuid :- expect UUID.GenerateUUID();
    var bkid := happyCaseIdHV2 + "-west-srk-" + uuid;
    // Create an HV-2 BK with a West SRK by calling us-west-2
    var bk :- expect underTest.CreateKey(
      Types.CreateKeyInput(
        Identifier := Some(bkid),
        EncryptionContext := Some(RobbieEC),
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        // us-west-2 b/c CI region is us-west-2 and KMS Client is created
        Strategy := Some(strategy),
        HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));
    expect bk.Identifier == bkid;
    // Validate an HV-2 BK with a West SRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bkid, keyStore, storage,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2);

    var initialActiveResult :- expect keyStore.GetActiveBranchKey(
      KeyStoreTypes.GetActiveBranchKeyInput(
        branchKeyIdentifier := bk.Identifier
      ));
    var initialActiveVersion :- expect UTF8.Decode(initialActiveResult.branchKeyMaterials.branchKeyVersion);
    var initialGetVersionResult :- expect keyStore.GetBranchKeyVersion(
      KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := bk.Identifier,
        branchKeyVersion := initialActiveVersion
      ));

    expect initialActiveResult.branchKeyMaterials.branchKeyVersion == initialGetVersionResult.branchKeyMaterials.branchKeyVersion;

    var versionedBk := underTest.VersionKey(
      Types.VersionKeyInput(
        Identifier := bkid,
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        // us-west-2 b/c CI region is us-west-2 and KMS Client is created
        Strategy := Some(strategy)
      )
    );

    // Validate an HV-2 BK with a West SRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bkid, keyStore, storage,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2);

    var versionedActiveResult :- expect keyStore.GetActiveBranchKey(
      KeyStoreTypes.GetActiveBranchKeyInput(
        branchKeyIdentifier := bk.Identifier
      ));
    var versionedActiveVersion :- expect UTF8.Decode(versionedActiveResult.branchKeyMaterials.branchKeyVersion);
    var versionedGetVersionResult :- expect keyStore.GetBranchKeyVersion(
      KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := bk.Identifier,
        branchKeyVersion := versionedActiveVersion
      ));

    expect versionedActiveResult.branchKeyMaterials.branchKeyVersion == versionedGetVersionResult.branchKeyMaterials.branchKeyVersion;
    expect initialActiveResult.branchKeyMaterials.branchKeyVersion != versionedActiveResult.branchKeyMaterials.branchKeyVersion;
    expect initialGetVersionResult.branchKeyMaterials.branchKeyVersion != versionedGetVersionResult.branchKeyMaterials.branchKeyVersion;

    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);

  }

  method {:test} TestCreateKeyStrategyCompatibility() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    // Key Management Strategies
    var simpleStrategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var reEncryptStrategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var decryptEncryptStrategy :- expect AdminFixtures.DecryptEncrypKeyManagerStrategy(decryptKmsClient?:=Some(kmsClient), encryptKmsClient?:=Some(kmsClient));
    // Admin
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));

    // Sad Cases
    // Create HV-1 BK with DecryptEncrypt Strategy (expects Failure)
    var hv1DecryptOutput := underTest.CreateKey(
      Types.CreateKeyInput(
        Identifier := Some(branchKeyId),
        EncryptionContext := Some(RobbieEC),
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        Strategy := Some(decryptEncryptStrategy),
        HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v1)
      ));
    expect
      && hv1DecryptOutput.Failure?
      && hv1DecryptOutput.error.KeyStoreAdminException?
      && (hv1DecryptOutput.error.message == KeyStoreErrorMessages.UNSUPPORTED_KEY_MANAGEMENT_STRATEGY_CREATE),
         "Branch Key Creation should have failed while creating with Unsupported KeyManagementStrategy";

    // Create HV-2 BK with DecryptEncrypt Strategy (expects Failure)
    var hv2DecryptOutput := underTest.CreateKey(
      Types.CreateKeyInput(
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        Strategy := Some(decryptEncryptStrategy),
        HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));
    expect
      && hv2DecryptOutput.Failure?
      && hv2DecryptOutput.error.KeyStoreAdminException?
      && (hv2DecryptOutput.error.message == KeyStoreErrorMessages.UNSUPPORTED_KEY_MANAGEMENT_STRATEGY_CREATE_HV_2),
         "Branch Key Creation should have failed while creating with Unsupported KeyManagementStrategy";

    // Create HV-2 BK with ReEncrypt Strategy (expects Failure)
    var hv2ReEncryptOutput := underTest.CreateKey(
      Types.CreateKeyInput(
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        Strategy := Some(reEncryptStrategy),
        HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));
    expect
      && hv2ReEncryptOutput.Failure?
      && hv2ReEncryptOutput.error.KeyStoreAdminException?
      && (hv2ReEncryptOutput.error.message == KeyStoreErrorMessages.UNSUPPORTED_KEY_MANAGEMENT_STRATEGY_CREATE_HV_2),
         "Branch Key Creation should have failed while creating with Unsupported KeyManagementStrategy";

    // Happy Cases
    // Create HV-1 BK with ReEncrypt Strategy (expects Success)
    var hv1ReEncryptOutput := underTest.CreateKey(
      Types.CreateKeyInput(
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        Strategy := Some(reEncryptStrategy),
        HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v1)
      ));
    expect hv1ReEncryptOutput.Success?;
    var _ := CleanupItems.DeleteBranchKey(Identifier:=hv1ReEncryptOutput.value.Identifier, ddbClient:=ddbClient);

    // Create HV-1 BK with KmsSimple Strategy (expects Success)
    var hv1KmsSimpleOutput := underTest.CreateKey(
      Types.CreateKeyInput(
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        Strategy := Some(simpleStrategy),
        HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v1)
      ));
    expect hv1KmsSimpleOutput.Success?;
    var _ := CleanupItems.DeleteBranchKey(Identifier:=hv1KmsSimpleOutput.value.Identifier, ddbClient:=ddbClient);

    // Create HV-2 BK with KmsSimple Strategy (expects Success)
    var hv2KmsSimpleOutput := underTest.CreateKey(
      Types.CreateKeyInput(
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        Strategy := Some(simpleStrategy),
        HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));
    expect hv2KmsSimpleOutput.Success?;
    var _ := CleanupItems.DeleteBranchKey(Identifier:=hv2KmsSimpleOutput.value.Identifier, ddbClient:=ddbClient);
  }

  method {:test} TestVersionKeyStrategyCompatibility() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    // Key Management Strategies
    var simpleStrategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var reEncryptStrategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var decryptEncryptStrategy :- expect AdminFixtures.DecryptEncrypKeyManagerStrategy(decryptKmsClient?:=Some(kmsClient), encryptKmsClient?:=Some(kmsClient));
    // Admin
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));

    var uuid :- expect UUID.GenerateUUID();
    var bkidHV1 := "test-version-key-unsupported-strategy-hv-1-" + uuid;
    var bkidHV2 := "test-version-key-unsupported-strategy-hv-2-" + uuid;

    // Create Happy Case Branch Keys for HV1 & HV-2
    AdminFixtures.CreateHappyCaseId(
      id := bkidHV1,
      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v1,
      admin? := Some(underTest)
    );
    AdminFixtures.CreateHappyCaseId(
      id := bkidHV2,
      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2,
      admin? := Some(underTest)
    );

    // Sad Cases
    // Version HV-1 BK with DecryptEncrypt Strategy (expects Failure)
    var hv1DecryptOutput := underTest.VersionKey(
      Types.VersionKeyInput(
        Identifier := bkidHV1,
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        Strategy := Some(decryptEncryptStrategy)
      )
    );
    expect
      && hv1DecryptOutput.Failure?
      && hv1DecryptOutput.error.KeyStoreAdminException?
      && (hv1DecryptOutput.error.message == KeyStoreAdminErrorMessages.UNSUPPORTED_KEY_MANAGEMENT_STRATEGY_DECRYPT_ENCRYPT_VERSION),
         "Branch Key Version should have failed while versioning with Unsupported KeyManagementStrategy";

    // Version HV-2 BK with DecryptEncrypt Strategy (expects Failure)
    var hv2DecryptOutput := underTest.VersionKey(
      Types.VersionKeyInput(
        Identifier := bkidHV2,
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        Strategy := Some(decryptEncryptStrategy)
      )
    );
    expect
      && hv2DecryptOutput.Failure?
      && hv2DecryptOutput.error.KeyStoreAdminException?
      && (hv2DecryptOutput.error.message == KeyStoreAdminErrorMessages.UNSUPPORTED_KEY_MANAGEMENT_STRATEGY_DECRYPT_ENCRYPT_VERSION),
         "Branch Key Version should have failed while versioning with Unsupported KeyManagementStrategy";

    // Version HV-2 BK with ReEncrypt Strategy (expects Failure)
    var hv2ReEncryptOutput := underTest.VersionKey(
      Types.VersionKeyInput(
        Identifier := bkidHV2,
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        Strategy := Some(reEncryptStrategy)
      )
    );
    expect
      && hv2ReEncryptOutput.Failure?
      && hv2ReEncryptOutput.error.AwsCryptographyKeyStore?
      && (hv2ReEncryptOutput.error.AwsCryptographyKeyStore.message == KeyStoreErrorMessages.UNSUPPORTED_KEY_MANAGEMENT_STRATEGY_VERSION_HV_2),
         "Branch Key Version should have failed while versioning with Unsupported KeyManagementStrategy";

    // Happy Cases
    // Version HV-1 BK with ReEncrypt & KmsSimple strategies (expects Success)
    var hv1ReEncryptOutput := underTest.VersionKey(
      Types.VersionKeyInput(
        Identifier := bkidHV1,
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        Strategy := Some(reEncryptStrategy)
      )
    );
    expect hv1ReEncryptOutput.Success?;
    var hv1KmsSimpleOutput := underTest.VersionKey(
      Types.VersionKeyInput(
        Identifier := bkidHV1,
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        Strategy := Some(simpleStrategy)
      )
    );
    expect hv1KmsSimpleOutput.Success?;

    // Version HV-2 BK with KmsSimple strategies (expects Success)
    var hv2KmsSimpleOutput := underTest.VersionKey(
      Types.VersionKeyInput(
        Identifier := bkidHV2,
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
        Strategy := Some(simpleStrategy)
      )
    );
    expect hv2KmsSimpleOutput.Success?;

    // Cleanup
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkidHV1, ddbClient:=ddbClient);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkidHV2, ddbClient:=ddbClient);
  }
}
