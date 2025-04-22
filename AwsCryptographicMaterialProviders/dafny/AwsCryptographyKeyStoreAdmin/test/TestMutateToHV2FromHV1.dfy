// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "AdminFixtures.dfy"
include "Mutations/TestMutationHappyPath.dfy"

// TODO-HV-2-M2: Move this to ./Mutations
module {:options "/functionSyntax:4" } TestMutateToHV2FromHV1 {
  import UUID
  import AdminFixtures
  import CleanupItems
  import TestMutationHappyPath
  import opened Fixtures
  import opened Wrappers
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes

  const testMutateForHV2ErrorsForNotKMSSimple := "dafny-initialize-mutation-hv-2-bad-strategy"
  const happyCaseId := "test-mutate-hv1-to-hv2"
  const terminalKmsId: string := Fixtures.kmsArnForHV2
  const terminalEC: KeyStoreTypes.EncryptionContextString := Fixtures.KodaECString
  const terminalHV: KeyStoreTypes.HierarchyVersion := KeyStoreTypes.HierarchyVersion.v2

  method {:test} TestMutateForHV2ErrorsForNotKMSSimple()
  {
    var uuid :- expect UUID.GenerateUUID();
    var testId := testMutateForHV2ErrorsForNotKMSSimple + "-" + uuid;
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
    expect initializeOutput.error.message == "Unsupported KeyManagementStrategy. Only KeyManagementStrategy.AwsKmsReEncrypt and KeyManagementStrategy.AwsKmsDecryptEncrypt is allowed when terminal hierarchical version is 1. Only KeyManagementStrategy.kmsSimple is allowed when terminal hierarchical version is 2.", "Incorrect error message. Should have had `Only KeyManagementStrategy.AwsKmsSimple is allowed when mutating to hv-2.`";
  }

  const testMutateForHV2SucceedsForKMSSimple := "dafny-initialize-mutation-hv-2-allowed"
  method {:test} TestMutateForHV2SucceedsForKMSSimple()
  {
    var uuid :- expect UUID.GenerateUUID();
    var testId := testMutateForHV2SucceedsForKMSSimple + "-" + uuid;
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
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
    expect initializeOutput.Success?, "Should have succeeded to InitializeMutation HV-2 for HV-2";
  }

  method {:test} TestHV1toHV2HappyCase()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
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
    var uuid :- expect UUID.GenerateUUID();
    var testId2 := happyCaseId + "-" + uuid;
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
      TerminalKmsArn := Some(terminalKmsId),
      TerminalHierarchyVersion := Some(terminalHV));
    var keyStoreTerminalForHV2AndKmsArnMutation :- expect Fixtures.DefaultKeyStore(
      kmsId:=terminalKmsId,
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
      TerminalKmsArn := Some(terminalKmsId),
      TerminalHierarchyVersion := Some(terminalHV));
    var keyStoreTerminalForHV2KmsArnAndECMutation :- expect Fixtures.DefaultKeyStore(
      kmsId:=terminalKmsId,
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
}