// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../src/KeyStoreAdminErrorMessages.dfy"
include "../AdminFixtures.dfy"
include "TestMutationHappyPath.dfy"

// TODO-HV-2-Mutate-Version: Add Mutation tests for DoNotVersion = false
module {:options "/functionSyntax:4" } TestMutations {
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

  const testMutateForHV2ErrorsForKmsReEncrypt := "dafny-initialize-mutation-hv-2-bad-strategy"
  const happyCaseId := "test-mutate-hv1-to-hv2"
  const terminalKmsIdHV1: string := Fixtures.postalHornKeyArn
  const terminalKmsIdHV2: string := Fixtures.kmsArnForHV2
  const terminalEC: KeyStoreTypes.EncryptionContextString := Fixtures.KodaECString
  const terminalHV: KeyStoreTypes.HierarchyVersion := KeyStoreTypes.HierarchyVersion.v2

  method {:test} TestMutateForHV2ErrorsForKmsReEncrypt()
  {
    var uuid :- expect UUID.GenerateUUID();
    var testId := testMutateForHV2ErrorsForKmsReEncrypt + "-" + uuid;
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var systemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage());
    Fixtures.CreateHappyCaseId(id:=testId);

    var mutationsRequest := Types.Mutations(
      TerminalKmsArn := Some(Fixtures.postalHornKeyArn),
      TerminalHierarchyVersion := Some(terminalHV)
    );
    var initInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := systemKey,
      DoNotVersion := Some(true));
    var initializeOutput := underTest.InitializeMutation(initInput);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
    expect initializeOutput.Failure?, "Should have failed to InitializeMutation HV-2.";
    expect initializeOutput.error.UnsupportedFeatureException?;
    // TODO-HV-2-M4: Support other key strategy as well.
    expect initializeOutput.error.message == KeyStoreAdminErrorMessages.UNSUPPORTED_KEY_MANAGEMENT_STRATEGY,
      "Incorrect error message. Should have had `" + KeyStoreAdminErrorMessages.UNSUPPORTED_KEY_MANAGEMENT_STRATEGY + "`";
  }

  method {:test} TestHV1toHV1HappyCaseReEncrypt() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(
      kmsClient?:=Some(kmsClient)
    );
    TestHV1toHV1HappyCase(strategy, ddbClient, kmsClient);
  }

  method {:test} TestHV1toHV1HappyCaseDecryptEncrypt() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.DecryptEncrypKeyManagerStrategy(
      decryptKmsClient?:=Some(kmsClient),
      encryptKmsClient?:=Some(kmsClient)
    );
    TestHV1toHV1HappyCase(strategy, ddbClient, kmsClient);
  }

  const happyCaseIdHV1toHV1 := "test-mutate-hv1-to-hv1"
  method TestHV1toHV1HappyCase(strategy: Types.KeyManagementStrategy, ddbClient: DDB.Types.IDynamoDBClient, kmsClient: KMS.Types.IKMSClient)
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
      doNotVersion := true
    );

    // Test HV2 mutating for kmsArn
    var uuidForKmsArnMutationTest :- expect UUID.GenerateUUID();
    var testIdForKmsArnMutation := happyCaseIdHV1toHV1 + "-" + uuidForKmsArnMutationTest;
    var mutationsRequestChangeHVAndKmsArn := Types.Mutations(
      TerminalKmsArn := Some(terminalKmsIdHV1)
    );
    var keyStoreTerminalForKmsArnMutation :- expect Fixtures.DefaultKeyStore(
      kmsId:=terminalKmsIdHV1,
      ddbClient?:=Some(ddbClient),
      kmsClient?:=Some(kmsClient));
    TestMutationHappyPath.MutationRoundTripTest(
      ddbClient := ddbClient,
      storage := storage,
      keyStoreAdminUnderTest := underTest,
      strategy := strategy,
      keyStoreTerminal := keyStoreTerminalForKmsArnMutation,
      branchKeyIdentifier := testIdForKmsArnMutation,
      mutationsRequest := mutationsRequestChangeHVAndKmsArn,
      versionCount := 1,
      initialHV := KeyStoreTypes.HierarchyVersion.v1,
      doNotVersion := true
    );

    // Test HV2 mutating for EC and kmsArn
    var uuidForKmsArnAndECMutationTest :- expect UUID.GenerateUUID();
    var testIdForKmsArnAndECMutation := happyCaseIdHV1toHV1 + "-" + uuidForKmsArnAndECMutationTest;
    var mutationsRequestChangeHVKmsArnAndEC := Types.Mutations(
      TerminalEncryptionContext := Some(terminalEC),
      TerminalKmsArn := Some(terminalKmsIdHV1)
    );
    var keyStoreTerminalForKmsArnAndECMutation :- expect Fixtures.DefaultKeyStore(
      kmsId:=terminalKmsIdHV1,
      ddbClient?:=Some(ddbClient),
      kmsClient?:=Some(kmsClient));
    TestMutationHappyPath.MutationRoundTripTest(
      ddbClient := ddbClient,
      storage := storage,
      keyStoreAdminUnderTest := underTest,
      strategy := strategy,
      keyStoreTerminal := keyStoreTerminalForKmsArnAndECMutation,
      branchKeyIdentifier := testIdForKmsArnAndECMutation,
      mutationsRequest := mutationsRequestChangeHVKmsArnAndEC,
      versionCount := 1,
      initialHV := KeyStoreTypes.HierarchyVersion.v1,
      doNotVersion := true
    );
  }

  method {:test} TestHV1toHV2HappyCaseKMSSimple() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(
      kmsClient?:=Some(kmsClient)
    );
    TestHV1toHV2HappyCase(strategy, ddbClient, kmsClient);
  }

  method {:test} TestHV1toHV2HappyCaseDecryptEncrypt() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.DecryptEncrypKeyManagerStrategy(
      decryptKmsClient?:=Some(kmsClient),
      encryptKmsClient?:=Some(kmsClient)
    );
    TestHV1toHV2HappyCase(strategy, ddbClient, kmsClient);
  }

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
    TestMutationHappyPath.MutationRoundTripTest(
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

    // Test mutating HV1 to HV2 and EC
    var uuidForHV2AndECMutationTest :- expect UUID.GenerateUUID();
    var testIdForHV2AndECMutation := happyCaseId + "-" + uuidForHV2AndECMutationTest;
    var mutationsRequestChangeHVAndEC := Types.Mutations(
      TerminalEncryptionContext := Some(terminalEC),
      TerminalHierarchyVersion := Some(terminalHV));
    TestMutationHappyPath.MutationRoundTripTest(
      ddbClient := ddbClient,
      storage := storage,
      keyStoreAdminUnderTest := underTest,
      strategy := strategy,
      keyStoreTerminal := keyStoreOriginal,
      branchKeyIdentifier := testIdForHV2AndECMutation,
      mutationsRequest := mutationsRequestChangeHVAndEC,
      versionCount := 1,
      initialHV := KeyStoreTypes.HierarchyVersion.v1,
      doNotVersion := true
    );

    // Test mutating HV1 to HV2 and kmsArn
    var uuidForHV2AndKmsArnMutationTest :- expect UUID.GenerateUUID();
    var testIdForHV2AndKmsArnMutation := happyCaseId + "-" + uuidForHV2AndKmsArnMutationTest;
    var mutationsRequestChangeHVAndKmsArn := Types.Mutations(
      TerminalKmsArn := Some(terminalKmsIdHV2),
      TerminalHierarchyVersion := Some(terminalHV));
    var keyStoreTerminalForHV2AndKmsArnMutation :- expect Fixtures.DefaultKeyStore(
      kmsId:=terminalKmsIdHV2,
      ddbClient?:=Some(ddbClient),
      kmsClient?:=Some(kmsClient));
    TestMutationHappyPath.MutationRoundTripTest(
      ddbClient := ddbClient,
      storage := storage,
      keyStoreAdminUnderTest := underTest,
      strategy := strategy,
      keyStoreTerminal := keyStoreTerminalForHV2AndKmsArnMutation,
      branchKeyIdentifier := testIdForHV2AndKmsArnMutation,
      mutationsRequest := mutationsRequestChangeHVAndKmsArn,
      versionCount := 1,
      initialHV := KeyStoreTypes.HierarchyVersion.v1,
      doNotVersion := true
    );

    // Test mutating HV1 to HV2, EC and kmsArn
    var uuidForHV2KmsArnAndECMutationTest :- expect UUID.GenerateUUID();
    var testIdForHV2KmsArnAndECMutation := happyCaseId + "-" + uuidForHV2KmsArnAndECMutationTest;
    var mutationsRequestChangeHVKmsArnAndEC := Types.Mutations(
      TerminalEncryptionContext := Some(terminalEC),
      TerminalKmsArn := Some(terminalKmsIdHV2),
      TerminalHierarchyVersion := Some(terminalHV));
    var keyStoreTerminalForHV2KmsArnAndECMutation :- expect Fixtures.DefaultKeyStore(
      kmsId:=terminalKmsIdHV2,
      ddbClient?:=Some(ddbClient),
      kmsClient?:=Some(kmsClient));
    TestMutationHappyPath.MutationRoundTripTest(
      ddbClient := ddbClient,
      storage := storage,
      keyStoreAdminUnderTest := underTest,
      strategy := strategy,
      keyStoreTerminal := keyStoreTerminalForHV2KmsArnAndECMutation,
      branchKeyIdentifier := testIdForHV2KmsArnAndECMutation,
      mutationsRequest := mutationsRequestChangeHVKmsArnAndEC,
      versionCount := 1,
      initialHV := KeyStoreTypes.HierarchyVersion.v1,
      doNotVersion := true
    );
  }

  method {:test} TestHV2toHV2HappyCaseKMSSimple() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(
      kmsClient?:=Some(kmsClient)
    );
    TestHV2toHV2HappyCase(strategy, ddbClient, kmsClient);
  }

  method {:test} TestHV2toHV2HappyCaseDecryptEncrypt() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.DecryptEncrypKeyManagerStrategy(
      decryptKmsClient?:=Some(kmsClient),
      encryptKmsClient?:=Some(kmsClient)
    );
    TestHV2toHV2HappyCase(strategy, ddbClient, kmsClient);
  }

  const happyCaseIdHV2toHV2 := "test-mutate-hv2-to-hv2"
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
    TestMutationHappyPath.MutationRoundTripTest(
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

    // Test HV2 mutating for kmsArn
    var uuidForHV2AndKmsArnMutationTest :- expect UUID.GenerateUUID();
    var testIdForHV2AndKmsArnMutation := happyCaseIdHV2toHV2 + "-" + uuidForHV2AndKmsArnMutationTest;
    var mutationsRequestChangeHVAndKmsArn := Types.Mutations(
      TerminalKmsArn := Some(terminalKmsIdHV2)
    );
    var keyStoreTerminalForHV2AndKmsArnMutation :- expect Fixtures.DefaultKeyStore(
      kmsId:=terminalKmsIdHV2,
      ddbClient?:=Some(ddbClient),
      kmsClient?:=Some(kmsClient));
    TestMutationHappyPath.MutationRoundTripTest(
      ddbClient := ddbClient,
      storage := storage,
      keyStoreAdminUnderTest := underTest,
      strategy := strategy,
      keyStoreTerminal := keyStoreTerminalForHV2AndKmsArnMutation,
      branchKeyIdentifier := testIdForHV2AndKmsArnMutation,
      mutationsRequest := mutationsRequestChangeHVAndKmsArn,
      versionCount := 1,
      initialHV := KeyStoreTypes.HierarchyVersion.v2,
      doNotVersion := true
    );

    // Test HV2 mutating for EC and kmsArn
    var uuidForHV2KmsArnAndECMutationTest :- expect UUID.GenerateUUID();
    var testIdForHV2KmsArnAndECMutation := happyCaseIdHV2toHV2 + "-" + uuidForHV2KmsArnAndECMutationTest;
    var mutationsRequestChangeHVKmsArnAndEC := Types.Mutations(
      TerminalEncryptionContext := Some(terminalEC),
      TerminalKmsArn := Some(terminalKmsIdHV2)
    );
    var keyStoreTerminalForHV2KmsArnAndECMutation :- expect Fixtures.DefaultKeyStore(
      kmsId:=terminalKmsIdHV2,
      ddbClient?:=Some(ddbClient),
      kmsClient?:=Some(kmsClient));
    TestMutationHappyPath.MutationRoundTripTest(
      ddbClient := ddbClient,
      storage := storage,
      keyStoreAdminUnderTest := underTest,
      strategy := strategy,
      keyStoreTerminal := keyStoreTerminalForHV2KmsArnAndECMutation,
      branchKeyIdentifier := testIdForHV2KmsArnAndECMutation,
      mutationsRequest := mutationsRequestChangeHVKmsArnAndEC,
      versionCount := 1,
      initialHV := KeyStoreTypes.HierarchyVersion.v2,
      doNotVersion := true
    );
  }
}