// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../AwsCryptographyKeyStore/test/BranchKeyValidators.dfy"
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
  import opened Wrappers
  import opened Fixtures
  import UUID
  import CleanupItems
  import AdminFixtures
  import BranchKeyValidators

  // TODO-HV-2-FOLLOW : TestCreateSRKForHV1, TestCreateForHV1NoBKID, TestCreateForHV1BbkidNoECFails

  const sadCaseId := "test-sad-case-admin-create-key-hv-1"
  method {:test} TestCreateMRKForHV1Fails()
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
    var bkid := sadCaseId + "-west-mrk-" + uuid;
    // Create an HV-1 BK with a West MRK by calling us-west-2
    var bk := /* expect */ underTest.CreateKey(
      Types.CreateKeyInput(
        Identifier := Some(bkid),
        EncryptionContext := Some(KmsMrkEC),
        KmsArn := Types.KmsSymmetricKeyArn.KmsMRKey(Types.KmsMRKey.KmsMRKey(KeyArn := MrkArnWest, Region := "us-west-2")),
        // us-west-2 b/c CI region is us-west-2 and KMS Client is created
        Strategy := Some(strategy)
      ));
    // TODO-BKSA-MRK-Support : Allow for MRK
    if (bk.Success?) {
      var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
    }
    expect bk.Failure?, "MRK config is not supported by the BKSA";
    // TODO : move error message to BKSA Error Messages
    expect bk.error == Types.UnsupportedFeatureException(
                         message := "At this time, the MRK configuration is not supported by the Admin client.");
    // TODO-BKSA-MRK-Support : Allow for MRK
    // expect bk.Identifier == bkid;
    // // Validate an HV-1 BK with a West MRK by calling us-east-1
    // BranchKeyValidators.VerifyGetKeys(bkid, keyStoreEast, storage,
    //                                   encryptionContext := KmsMrkEC);
    // var keyStoreWest :- expect KeyStoreFromKMSConfig(
    //   // Passing in KmsMrkConfigWest causes the KMS Client to be created for us-west-2
    //   // bk's KMS-ARN is replicated to us-west-2
    //   kmsConfig := KmsMrkConfigWest,
    //   ddbClient? := Some(ddbClient)
    // );
    // // Validate an HV-1 BK with a West MRK by calling us-west-2
    // BranchKeyValidators.VerifyGetKeys(bkid, keyStoreWest, storage,
    //                                   encryptionContext := KmsMrkEC);
    // var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
  }

  // TODO-HV-2-M2?: Document that BKSA ONLY calls KMS/DDB for the region of the supplied clients.
  // or Ensure BKSA has similar behavior as BKS in terms of MRK region.
  const sadCaseIdHV2 := "test-sad-case-admin-create-key-hv-2"
  method {:test} TestCreateMRKForHV2Fails()
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
    var bkid := sadCaseIdHV2 + "-west-mrk-" + uuid;
    // Create an HV-2 BK with a West MRK by calling us-west-2
    var bk := /* expect */ underTest.CreateKey(
      Types.CreateKeyInput(
        Identifier := Some(bkid),
        EncryptionContext := Some(RobbieEC),
        KmsArn := Types.KmsSymmetricKeyArn.KmsMRKey(Types.KmsMRKey.KmsMRKey(KeyArn := MrkArnWest, Region := "us-west-2")),
        // us-west-2 b/c CI region is us-west-2 and KMS Client is created
        Strategy := Some(strategy),
        HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));
    // TODO-BKSA-MRK-Support : Allow for MRK
    if (bk.Success?) {
      var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
    }
    expect bk.Failure?, "MRK config is not supported by the BKSA";
    // TODO : move error message to BKSA Error Messages
    expect bk.error == Types.UnsupportedFeatureException(
                         message := "At this time, the MRK configuration is not supported by the Admin client.");
    // TODO-BKSA-MRK-Support : Allow for MRK
    // expect bk.Identifier == bkid;
    // // Validate an HV-2 BK with a West MRK by calling us-east-1
    // BranchKeyValidators.VerifyGetKeys(bkid, keyStoreEast, storage,
    //                                   encryptionContext := RobbieEC,
    //                                   hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2);
    // var keyStoreWest :- expect KeyStoreFromKMSConfig(
    //   // Passing in KmsMrkConfigWest causes the KMS Client to be created for us-west-2
    //   // bk's KMS-ARN is replicated to us-west-2
    //   kmsConfig := KmsMrkConfigWest,
    //   ddbClient? := Some(ddbClient)
    // );
    // // Validate an HV-2 BK with a West MRK by calling us-west-2
    // BranchKeyValidators.VerifyGetKeys(bkid, keyStoreWest, storage,
    //                                   encryptionContext := RobbieEC,
    //                                   hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2);
    // var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
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
}
