// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../src/KeyStoreAdminErrorMessages.dfy"
include "../AdminFixtures.dfy"
include "TestMutationHappyPath.dfy"

module {:options "/functionSyntax:4" } TestMutationsResume {
  import UUID
  import AdminFixtures
  import CleanupItems
  import KeyStoreAdminErrorMessages
  import TestMutationHappyPath
  import opened Fixtures
  import opened Wrappers
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import DDB = Com.Amazonaws.Dynamodb
  import KMS = Com.Amazonaws.Kms

  const terminalKmsIdHV1: string := Fixtures.postalHornKeyArn
  const terminalKmsIdHV2: string := Fixtures.kmsArnForHV2
  const terminalEC: KeyStoreTypes.EncryptionContextString := Fixtures.KodaECString
  const terminalHV: KeyStoreTypes.HierarchyVersion := KeyStoreTypes.HierarchyVersion.v2

  method {:test} TestHV1toHV1ResumeMutationReEncryptMutate() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(
      kmsClient?:=Some(kmsClient)
    );
    var doNotVersionOnMutate := true;
    TestHV1toHV1HappyCase(strategy, ddbClient, kmsClient, doNotVersionOnMutate);
  }

  method {:test} TestHV1toHV1ResumeMutationKmsSimpleMutate() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(
      kmsClient?:=Some(kmsClient)
    );
    var doNotVersionOnMutate := true;
    TestHV1toHV1HappyCase(strategy, ddbClient, kmsClient, doNotVersionOnMutate);
  }

  method {:test} TestHV1toHV1ResumeMutationDecryptEncryptMutate() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.DecryptEncrypKeyManagerStrategy(
      decryptKmsClient?:=Some(kmsClient),
      encryptKmsClient?:=Some(kmsClient)
    );
    var doNotVersionOnMutate := true;
    TestHV1toHV1HappyCase(strategy, ddbClient, kmsClient, doNotVersionOnMutate);
  }

  method {:test} TestHV1toHV1ResumeMutationReEncryptRotate() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(
      kmsClient?:=Some(kmsClient)
    );
    var doNotVersionOnMutate := false;
    TestHV1toHV1HappyCase(strategy, ddbClient, kmsClient, doNotVersionOnMutate);
  }

  method {:test} TestHV1toHV1ResumeMutationKmsSimpleRotate() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(
      kmsClient?:=Some(kmsClient)
    );
    var doNotVersionOnMutate := false;
    TestHV1toHV1HappyCase(strategy, ddbClient, kmsClient, doNotVersionOnMutate);
  }

  method {:test} TestHV1toHV1ResumeMutationDecryptEncryptRotate() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.DecryptEncrypKeyManagerStrategy(
      decryptKmsClient?:=Some(kmsClient),
      encryptKmsClient?:=Some(kmsClient)
    );
    var doNotVersionOnMutate := false;
    TestHV1toHV1HappyCase(strategy, ddbClient, kmsClient, doNotVersionOnMutate);
  }

  const happyCaseIdHV1toHV1 := "test-mutate-resume-hv1-to-hv1"
  method TestHV1toHV1HappyCase(strategy: Types.KeyManagementStrategy, ddbClient: DDB.Types.IDynamoDBClient, kmsClient: KMS.Types.IKMSClient, doNotVersionOnMutate : bool)
    requires ddbClient.ValidState() && kmsClient.ValidState()
    modifies ddbClient.Modifies, kmsClient.Modifies
  {
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var keyStoreOriginal :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    // Test HV2 mutating for EC only
    var uuidForECMutationTest :- expect UUID.GenerateUUID();
    var testIdForECMutation := happyCaseIdHV1toHV1 + "-" + uuidForECMutationTest;
    var mutationsRequestChangeHVAndEC := Types.Mutations(
      TerminalEncryptionContext := Some(terminalEC)
    );
    TestMutationHappyPath.MutationRoundTripTest(
      ddbClient := ddbClient,
      storage := storage,
      keyStoreAdminUnderTest := underTest,
      strategy := strategy,
      keyStoreTerminal := keyStoreOriginal,
      branchKeyIdentifier := testIdForECMutation,
      mutationsRequest := mutationsRequestChangeHVAndEC,
      versionCount := 1,
      initialHV := KeyStoreTypes.HierarchyVersion.v1,
      doNotVersion := doNotVersionOnMutate
    );

    // Uncomment to run tests for other mutations
    // // Test HV2 mutating for kmsArn
    // var uuidForKmsArnMutationTest :- expect UUID.GenerateUUID();
    // var testIdForKmsArnMutation := happyCaseIdHV1toHV1 + "-" + uuidForKmsArnMutationTest;
    // var mutationsRequestChangeHVAndKmsArn := Types.Mutations(
    //   TerminalKmsArn := Some(terminalKmsIdHV1)
    // );
    // var keyStoreTerminalForKmsArnMutation :- expect Fixtures.DefaultKeyStore(
    //   kmsId:=terminalKmsIdHV1,
    //   ddbClient?:=Some(ddbClient),
    //   kmsClient?:=Some(kmsClient));
    // TestMutationHappyPath.MutationRecoveryTest(
    //   ddbClient := ddbClient,
    //   storage := storage,
    //   keyStoreAdminUnderTest := underTest,
    //   strategy := strategy,
    //   keyStoreTerminal := keyStoreTerminalForKmsArnMutation,
    //   branchKeyIdentifier := testIdForKmsArnMutation,
    //   mutationsRequest := mutationsRequestChangeHVAndKmsArn,
    //   versionCount := 1,
    //   initialHV := KeyStoreTypes.HierarchyVersion.v1,
    //   doNotVersion := doNotVersionOnMutate
    // );

    // // Test HV2 mutating for EC and kmsArn
    // var uuidForKmsArnAndECMutationTest :- expect UUID.GenerateUUID();
    // var testIdForKmsArnAndECMutation := happyCaseIdHV1toHV1 + "-" + uuidForKmsArnAndECMutationTest;
    // var mutationsRequestChangeHVKmsArnAndEC := Types.Mutations(
    //   TerminalEncryptionContext := Some(terminalEC),
    //   TerminalKmsArn := Some(terminalKmsIdHV1)
    // );
    // var keyStoreTerminalForKmsArnAndECMutation :- expect Fixtures.DefaultKeyStore(
    //   kmsId:=terminalKmsIdHV1,
    //   ddbClient?:=Some(ddbClient),
    //   kmsClient?:=Some(kmsClient));
    // TestMutationHappyPath.MutationRecoveryTest(
    //   ddbClient := ddbClient,
    //   storage := storage,
    //   keyStoreAdminUnderTest := underTest,
    //   strategy := strategy,
    //   keyStoreTerminal := keyStoreTerminalForKmsArnAndECMutation,
    //   branchKeyIdentifier := testIdForKmsArnAndECMutation,
    //   mutationsRequest := mutationsRequestChangeHVKmsArnAndEC,
    //   versionCount := 1,
    //   initialHV := KeyStoreTypes.HierarchyVersion.v1,
    //   doNotVersion := doNotVersionOnMutate
    // );
  }

  method {:test} TestHV1toHV2ResumeMutationKMSSimple() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(
      kmsClient?:=Some(kmsClient)
    );
    TestHV1toHV2HappyCase(strategy, ddbClient, kmsClient);
  }

  method {:test} TestHV1toHV2ResumeMutationDecryptEncrypt() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.DecryptEncrypKeyManagerStrategy(
      decryptKmsClient?:=Some(kmsClient),
      encryptKmsClient?:=Some(kmsClient)
    );
    TestHV1toHV2HappyCase(strategy, ddbClient, kmsClient);
  }

  const happyCaseId := "test-mutate-hv1-to-hv2"
  method TestHV1toHV2HappyCase(strategy: Types.KeyManagementStrategy, ddbClient: DDB.Types.IDynamoDBClient, kmsClient: KMS.Types.IKMSClient)
    requires ddbClient.ValidState() && kmsClient.ValidState()
    modifies ddbClient.Modifies, kmsClient.Modifies
    ensures ddbClient.ValidState() && kmsClient.ValidState()
  {
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var keyStoreOriginal :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    // Test mutating HV1 to HV2 only
    var uuidForHV2MutationTest :- expect UUID.GenerateUUID();
    var testIdForHV2MutationOnly := happyCaseId + "-" + uuidForHV2MutationTest;
    var mutationsRequestChangeHV := Types.Mutations(
      TerminalHierarchyVersion := Some(terminalHV));
    TestMutationHappyPath.MutationRecoveryTest(
      ddbClient := ddbClient,
      storage := storage,
      keyStoreAdminUnderTest := underTest,
      strategy := strategy,
      keyStoreTerminal := keyStoreOriginal,
      branchKeyIdentifier := testIdForHV2MutationOnly,
      mutationsRequest := mutationsRequestChangeHV,
      versionCount := 1,
      initialHV := KeyStoreTypes.HierarchyVersion.v1,
      doNotVersion := true
    );

    // Uncomment to run tests for other mutations
    // // Test mutating HV1 to HV2 and EC
    // var uuidForHV2AndECMutationTest :- expect UUID.GenerateUUID();
    // var testIdForHV2AndECMutation := happyCaseId + "-" + uuidForHV2AndECMutationTest;
    // var mutationsRequestChangeHVAndEC := Types.Mutations(
    //   TerminalEncryptionContext := Some(terminalEC),
    //   TerminalHierarchyVersion := Some(terminalHV));
    // TestMutationHappyPath.MutationRecoveryTest(
    //   ddbClient := ddbClient,
    //   storage := storage,
    //   keyStoreAdminUnderTest := underTest,
    //   strategy := strategy,
    //   keyStoreTerminal := keyStoreOriginal,
    //   branchKeyIdentifier := testIdForHV2AndECMutation,
    //   mutationsRequest := mutationsRequestChangeHVAndEC,
    //   versionCount := 1,
    //   initialHV := KeyStoreTypes.HierarchyVersion.v1,
    //   doNotVersion := true
    // );

    // // Test mutating HV1 to HV2 and kmsArn
    // var uuidForHV2AndKmsArnMutationTest :- expect UUID.GenerateUUID();
    // var testIdForHV2AndKmsArnMutation := happyCaseId + "-" + uuidForHV2AndKmsArnMutationTest;
    // var mutationsRequestChangeHVAndKmsArn := Types.Mutations(
    //   TerminalKmsArn := Some(terminalKmsIdHV2),
    //   TerminalHierarchyVersion := Some(terminalHV));
    // var keyStoreTerminalForHV2AndKmsArnMutation :- expect Fixtures.DefaultKeyStore(
    //   kmsId:=terminalKmsIdHV2,
    //   ddbClient?:=Some(ddbClient),
    //   kmsClient?:=Some(kmsClient));
    // TestMutationHappyPath.MutationRecoveryTest(
    //   ddbClient := ddbClient,
    //   storage := storage,
    //   keyStoreAdminUnderTest := underTest,
    //   strategy := strategy,
    //   keyStoreTerminal := keyStoreTerminalForHV2AndKmsArnMutation,
    //   branchKeyIdentifier := testIdForHV2AndKmsArnMutation,
    //   mutationsRequest := mutationsRequestChangeHVAndKmsArn,
    //   versionCount := 1,
    //   initialHV := KeyStoreTypes.HierarchyVersion.v1,
    //   doNotVersion := true
    // );

    // // Test mutating HV1 to HV2, EC and kmsArn
    // var uuidForHV2KmsArnAndECMutationTest :- expect UUID.GenerateUUID();
    // var testIdForHV2KmsArnAndECMutation := happyCaseId + "-" + uuidForHV2KmsArnAndECMutationTest;
    // var mutationsRequestChangeHVKmsArnAndEC := Types.Mutations(
    //   TerminalEncryptionContext := Some(terminalEC),
    //   TerminalKmsArn := Some(terminalKmsIdHV2),
    //   TerminalHierarchyVersion := Some(terminalHV));
    // var keyStoreTerminalForHV2KmsArnAndECMutation :- expect Fixtures.DefaultKeyStore(
    //   kmsId:=terminalKmsIdHV2,
    //   ddbClient?:=Some(ddbClient),
    //   kmsClient?:=Some(kmsClient));
    // TestMutationHappyPath.MutationRecoveryTest(
    //   ddbClient := ddbClient,
    //   storage := storage,
    //   keyStoreAdminUnderTest := underTest,
    //   strategy := strategy,
    //   keyStoreTerminal := keyStoreTerminalForHV2KmsArnAndECMutation,
    //   branchKeyIdentifier := testIdForHV2KmsArnAndECMutation,
    //   mutationsRequest := mutationsRequestChangeHVKmsArnAndEC,
    //   versionCount := 1,
    //   initialHV := KeyStoreTypes.HierarchyVersion.v1,
    //   doNotVersion := true
    // );
  }

  method {:test} TestHV2toHV2ResumeMutationKMSSimple() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(
      kmsClient?:=Some(kmsClient)
    );
    TestHV2toHV2HappyCase(strategy, ddbClient, kmsClient);
  }

  method {:test} TestHV2toHV2ResumeMutationDecryptEncrypt() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.DecryptEncrypKeyManagerStrategy(
      decryptKmsClient?:=Some(kmsClient),
      encryptKmsClient?:=Some(kmsClient)
    );
    TestHV2toHV2HappyCase(strategy, ddbClient, kmsClient);
  }

  const happyCaseIdHV2toHV2 := "test-mutate-resume-hv2-to-hv2"
  method TestHV2toHV2HappyCase(strategy: Types.KeyManagementStrategy, ddbClient: DDB.Types.IDynamoDBClient, kmsClient: KMS.Types.IKMSClient)
    requires ddbClient.ValidState() && kmsClient.ValidState()
    modifies ddbClient.Modifies, kmsClient.Modifies
  {
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var keyStoreOriginal :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    // Test HV2 mutating for EC only
    var uuidForHV2AndECMutationTest :- expect UUID.GenerateUUID();
    var testIdForHV2AndECMutation := happyCaseIdHV2toHV2 + "-" + uuidForHV2AndECMutationTest;
    var mutationsRequestChangeHVAndEC := Types.Mutations(
      TerminalEncryptionContext := Some(terminalEC)
    );
    TestMutationHappyPath.MutationRecoveryTest(
      ddbClient := ddbClient,
      storage := storage,
      keyStoreAdminUnderTest := underTest,
      strategy := strategy,
      keyStoreTerminal := keyStoreOriginal,
      branchKeyIdentifier := testIdForHV2AndECMutation,
      mutationsRequest := mutationsRequestChangeHVAndEC,
      versionCount := 1,
      initialHV := KeyStoreTypes.HierarchyVersion.v2,
      doNotVersion := true
    );

    // Uncomment to run tests for other mutations
    // // Test HV2 mutating for kmsArn
    // var uuidForHV2AndKmsArnMutationTest :- expect UUID.GenerateUUID();
    // var testIdForHV2AndKmsArnMutation := happyCaseIdHV2toHV2 + "-" + uuidForHV2AndKmsArnMutationTest;
    // var mutationsRequestChangeHVAndKmsArn := Types.Mutations(
    //   TerminalKmsArn := Some(terminalKmsIdHV2)
    // );
    // var keyStoreTerminalForHV2AndKmsArnMutation :- expect Fixtures.DefaultKeyStore(
    //   kmsId:=terminalKmsIdHV2,
    //   ddbClient?:=Some(ddbClient),
    //   kmsClient?:=Some(kmsClient));
    // TestMutationHappyPath.MutationRecoveryTest(
    //   ddbClient := ddbClient,
    //   storage := storage,
    //   keyStoreAdminUnderTest := underTest,
    //   strategy := strategy,
    //   keyStoreTerminal := keyStoreTerminalForHV2AndKmsArnMutation,
    //   branchKeyIdentifier := testIdForHV2AndKmsArnMutation,
    //   mutationsRequest := mutationsRequestChangeHVAndKmsArn,
    //   versionCount := 1,
    //   initialHV := KeyStoreTypes.HierarchyVersion.v2,
    //   doNotVersion := true
    // );

    // // Test HV2 mutating for EC and kmsArn
    // var uuidForHV2KmsArnAndECMutationTest :- expect UUID.GenerateUUID();
    // var testIdForHV2KmsArnAndECMutation := happyCaseIdHV2toHV2 + "-" + uuidForHV2KmsArnAndECMutationTest;
    // var mutationsRequestChangeHVKmsArnAndEC := Types.Mutations(
    //   TerminalEncryptionContext := Some(terminalEC),
    //   TerminalKmsArn := Some(terminalKmsIdHV2)
    // );
    // var keyStoreTerminalForHV2KmsArnAndECMutation :- expect Fixtures.DefaultKeyStore(
    //   kmsId:=terminalKmsIdHV2,
    //   ddbClient?:=Some(ddbClient),
    //   kmsClient?:=Some(kmsClient));
    // TestMutationHappyPath.MutationRecoveryTest(
    //   ddbClient := ddbClient,
    //   storage := storage,
    //   keyStoreAdminUnderTest := underTest,
    //   strategy := strategy,
    //   keyStoreTerminal := keyStoreTerminalForHV2KmsArnAndECMutation,
    //   branchKeyIdentifier := testIdForHV2KmsArnAndECMutation,
    //   mutationsRequest := mutationsRequestChangeHVKmsArnAndEC,
    //   versionCount := 1,
    //   initialHV := KeyStoreTypes.HierarchyVersion.v2,
    //   doNotVersion := true
    // );
  }
}