// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../AwsCryptographyKeyStore/test/BranchKeyValidators.dfy"

module {:options "/functionSyntax:4" } TestAdminCreateKeys {
  import KeyStore
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import ComAmazonawsKmsTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import KeyStoreErrorMessages
  import opened Wrappers
  import opened Fixtures
  import UUID
  import CleanupItems
  import BranchKeyValidators

  // TODO-HV-2-FOLLOW : TestCreateSRKForHV1, TestCreateForHV1NoBKID, TestCreateForHV1BkidNoECFails

  const mrkCaseId := "test-mrk-case-admin-create-key-hv-1"
  method {:test} TestCreateMrkForHV1Succeeds()
  {
    var ddbClient :- expect ProvideDDBClient();
    var keyStore :- expect KeyStoreFromKMSConfig(ddbClient?:=Some(ddbClient), kmsConfig := KmsMrkConfigWest);
    var keyStoreEast :- expect KeyStoreFromKMSConfig(
      kmsConfig := KmsMrkConfigEast,
      ddbClient? := Some(ddbClient)
    );
    var uuid :- expect UUID.GenerateUUID();
    var bkid := mrkCaseId + "-west-mrk-" + uuid;
    // Create an HV-1 BK with a West MRK by calling us-west-2
    var bk :- expect keyStore.CreateKey(
      Types.CreateKeyInput(
        branchKeyIdentifier := Some(bkid),
        encryptionContext := Some(KmsMrkEC)
      ));
    expect bk.branchKeyIdentifier == bkid;
    // Validate an HV-1 BK with a West MRK by calling us-east-1
    BranchKeyValidators.VerifyGetKeys(bkid, keyStoreEast,
                                      encryptionContext := KmsMrkEC);
    var keyStoreWest :- expect KeyStoreFromKMSConfig(
      // Passing in KmsMrkConfigWest causes the KMS Client to be created for us-west-2
      // bk's KMS-ARN is replicated to us-west-2
      kmsConfig := KmsMrkConfigWest,
      ddbClient? := Some(ddbClient)
    );
    // Validate an HV-1 BK with a West MRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bkid, keyStoreWest,
                                      encryptionContext := KmsMrkEC);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
  }

  // TODO-HV-2-M2?: Document that BKSA ONLY calls KMS/DDB for the region of the supplied clients.
  // or Ensure BKSA has similar behavior as BKS in terms of MRK region.
  const mrkCaseIdHV2 := "test-mrk-case-admin-create-key-hv-2"
  method {:test} TestCreateMRKForHV2Succeeds()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var keyStore :- expect KeyStoreFromKMSConfig(
      // Passing in KmsMrkConfigWest causes the KMS Client to be created for us-west-2
      // bk's KMS-ARN is replicated to us-west-2
      kmsConfig := KmsMrkConfigWest,
      ddbClient? := Some(ddbClient)
    );
    var keyStoreEast :- expect KeyStoreFromKMSConfig(
      kmsConfig := KmsMrkConfigEast,
      ddbClient? := Some(ddbClient)
    );
    var uuid :- expect UUID.GenerateUUID();
    var bkid := mrkCaseIdHV2 + "-west-mrk-" + uuid;
    // Create an HV-2 BK with a West MRK by calling us-west-2
    var bk :- expect keyStore.CreateKey(
      Types.CreateKeyInput(
        branchKeyIdentifier := Some(bkid),
        encryptionContext := Some(RobbieEC),
        hierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));
    expect bk.branchKeyIdentifier == bkid;
    // Validate an HV-2 BK with a West MRK by calling us-east-1
    BranchKeyValidators.VerifyGetKeys(bkid, keyStoreEast,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2);
    var keyStoreWest :- expect KeyStoreFromKMSConfig(
      // Passing in KmsMrkConfigWest causes the KMS Client to be created for us-west-2
      // bk's KMS-ARN is replicated to us-west-2
      kmsConfig := KmsMrkConfigWest,
      ddbClient? := Some(ddbClient)
    );
    // Validate an HV-2 BK with a West MRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bkid, keyStoreWest,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
  }
  const happyCaseIdHV2 := "test-happy-case-admin-create-key-hv-2"

  method {:test} TestCreateSRKForHV2()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    var uuid :- expect UUID.GenerateUUID();
    var bkid := happyCaseIdHV2 + "-west-srk-" + uuid;
    // Create an HV-2 BK with a West SRK by calling us-west-2
    var bk :- expect keyStore.CreateKey(
      Types.CreateKeyInput(
        branchKeyIdentifier := Some(bkid),
        encryptionContext := Some(RobbieEC),
        hierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));
    expect bk.branchKeyIdentifier == bkid;
    // Validate an HV-2 BK with a West SRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bkid, keyStore,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
  }

  method {:test} TestCreateSRKForHV2NoEC()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    var bk :- expect keyStore.CreateKey(
      Types.CreateKeyInput(
        hierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));
    BranchKeyValidators.VerifyGetKeys(bk.branchKeyIdentifier, keyStore,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bk.branchKeyIdentifier, ddbClient:=ddbClient);
  }

  method {:test} TestCreateSRKForHV2BkidWithNoECFails()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    var uuid :- expect UUID.GenerateUUID();
    var bkid := happyCaseIdHV2 + "-west-srk-no-ec-fails-" + uuid;
    var bk? := keyStore.CreateKey(
      Types.CreateKeyInput(
        branchKeyIdentifier := Some(bkid),
        hierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));
    expect bk?.Failure?, "Admin CreateKey, with an Identifier, but no EC, MUST Fail";
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
  }

  const happyCaseIdHV1 := "test-happy-case-admin-create-key-hv-1"
  method {:test} TestCreateSrkForHV1()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    var uuid :- expect UUID.GenerateUUID();
    var bkid := happyCaseIdHV1 + "-west-srk-" + uuid;
    // Create an HV-1 BK with a West MRK by calling us-west-2
    var bk :- expect keyStore.CreateKey(
      Types.CreateKeyInput(
        branchKeyIdentifier := Some(bkid),
        encryptionContext := Some(RobbieEC)
      ));
    expect bk.branchKeyIdentifier == bkid;
    // Validate an HV-2 BK with a West SRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bkid, keyStore,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v1);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);
  }

  method {:test} TestCreateForHV1NoBKID()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    var uuid :- expect UUID.GenerateUUID();
    // Create an HV-1 BK with a West MRK by calling us-west-2
    var bk :- expect keyStore.CreateKey(
      Types.CreateKeyInput(
        branchKeyIdentifier := None(),
        encryptionContext := Some(RobbieEC)
      ));
    // Validate an HV-2 BK with a West SRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bk.branchKeyIdentifier, keyStore,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v1);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=bk.branchKeyIdentifier, ddbClient:=ddbClient);
  }

  method {:test} TestCreateHv1AndVersion()
  {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    var uuid :- expect UUID.GenerateUUID();
    // Create an HV-1 BK with a West MRK by calling us-west-2
    var bk :- expect keyStore.CreateKey(
      Types.CreateKeyInput(
        branchKeyIdentifier := None(),
        encryptionContext := Some(RobbieEC)
      ));
    // Validate an HV-2 BK with a West SRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bk.branchKeyIdentifier, keyStore,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v1);

    var versionedBk :- expect keyStore.VersionKey(
      KeyStoreTypes.VersionKeyInput(
        branchKeyIdentifier := bk.branchKeyIdentifier
      )
    );

    var _ := CleanupItems.DeleteBranchKey(Identifier:=bk.branchKeyIdentifier, ddbClient:=ddbClient);
  }


  method {:test} TestCreateHv2AndVersion()
  {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    var uuid :- expect UUID.GenerateUUID();
    var bkid := happyCaseIdHV2 + "-west-srk-" + uuid;
    // Create an HV-2 BK with a West SRK by calling us-west-2
    var bk :- expect keyStore.CreateKey(
      Types.CreateKeyInput(
        branchKeyIdentifier := Some(bkid),
        encryptionContext := Some(RobbieEC),
        hierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));
    expect bk.branchKeyIdentifier == bkid;
    // Validate an HV-2 BK with a West SRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bkid, keyStore,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2);

    var initialActiveResult :- expect keyStore.GetActiveBranchKey(
      KeyStoreTypes.GetActiveBranchKeyInput(
        branchKeyIdentifier := bk.branchKeyIdentifier
      ));
    var initialActiveVersion :- expect UTF8.Decode(initialActiveResult.branchKeyMaterials.branchKeyVersion);
    var initialGetVersionResult :- expect keyStore.GetBranchKeyVersion(
      KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := bk.branchKeyIdentifier,
        branchKeyVersion := initialActiveVersion
      ));

    expect initialActiveResult.branchKeyMaterials.branchKeyVersion == initialGetVersionResult.branchKeyMaterials.branchKeyVersion;

    var versionedBk := keyStore.VersionKey(
      Types.VersionKeyInput(
        branchKeyIdentifier := bkid
      )
    );

    // Validate an HV-2 BK with a West SRK by calling us-west-2
    BranchKeyValidators.VerifyGetKeys(bkid, keyStore,
                                      encryptionContext := RobbieEC,
                                      hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2);

    var versionedActiveResult :- expect keyStore.GetActiveBranchKey(
      KeyStoreTypes.GetActiveBranchKeyInput(
        branchKeyIdentifier := bk.branchKeyIdentifier
      ));
    var versionedActiveVersion :- expect UTF8.Decode(versionedActiveResult.branchKeyMaterials.branchKeyVersion);
    var versionedGetVersionResult :- expect keyStore.GetBranchKeyVersion(
      KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := bk.branchKeyIdentifier,
        branchKeyVersion := versionedActiveVersion
      ));

    expect versionedActiveResult.branchKeyMaterials.branchKeyVersion == versionedGetVersionResult.branchKeyMaterials.branchKeyVersion;
    expect initialActiveResult.branchKeyMaterials.branchKeyVersion != versionedActiveResult.branchKeyMaterials.branchKeyVersion;
    expect initialGetVersionResult.branchKeyMaterials.branchKeyVersion != versionedGetVersionResult.branchKeyMaterials.branchKeyVersion;

    var _ := CleanupItems.DeleteBranchKey(Identifier:=bkid, ddbClient:=ddbClient);

  }

  // TestCreateKeyStrategyCompatibility removed -- not applicable
  // TestVersionKeyStrategyCompatibility removed -- not applicable
}
