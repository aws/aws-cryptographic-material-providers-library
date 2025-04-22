// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "AdminFixtures.dfy"

module {:options "/functionSyntax:4" } TestMutateToHV2FromHV1 {
  import UUID
  import AdminFixtures
  import CleanupItems
  import Time
  import opened Fixtures
  import opened Wrappers
  import DDB = Com.Amazonaws.Dynamodb
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import String = StandardLibrary.String

  const testMutateForHV2ErrorsForNotKMSSimple := "dafny-initialize-mutation-hv-2-bad-strategy"
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
      TerminalHierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
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
      TerminalHierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
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


  const happyCaseId := "test-mutate-hv1-to-hv2"
  const kmsId: string := Fixtures.keyArn
  const physicalName: string := Fixtures.branchKeyStoreName
  const logicalName: string := Fixtures.logicalKeyStoreName
  const testLogPrefix := "\nTestKmsArnChanged :: TestHappyCase :: "

  method {:test} {:vcs_split_on_every_assert} TestHV1toHV2HappyCase()
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
      TerminalHierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2));
    mutationHappyPathTest(
      ddbClient := ddbClient,
      storage := storage,
      keyStoreAdminUnderTest := underTest,
      strategy := strategy,
      keyStoreTerminal := keyStoreOriginal,
      branchKeyIdentifier := testIdForHV2MutationOnly,
      mutationsRequest := mutationsRequestChangeHV,
      versionCount := 1,
      doNotVersion := true
    );

    // Test mutating HV1 to HV2 and EC
    var uuidForHV2AndECMutationTest :- expect UUID.GenerateUUID();
    var testIdForHV2AndECMutation := happyCaseId + "-" + uuidForHV2AndECMutationTest;
    var uuid :- expect UUID.GenerateUUID();
    var testId2 := happyCaseId + "-" + uuid;
    var timestamp :- expect Time.GetCurrentTimeStamp();
    var newCustomEC: KeyStoreTypes.EncryptionContextString := map["Robbie" := timestamp];
    var mutationsRequestChangeHVAndEC := Types.Mutations(
      TerminalEncryptionContext := Some(newCustomEC),
      TerminalHierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2));
    mutationHappyPathTest(
      ddbClient := ddbClient,
      storage := storage,
      keyStoreAdminUnderTest := underTest,
      strategy := strategy,
      keyStoreTerminal := keyStoreOriginal,
      branchKeyIdentifier := testIdForHV2AndECMutation,
      mutationsRequest := mutationsRequestChangeHVAndEC,
      versionCount := 1,
      doNotVersion := true
    );

    // Test mutating HV1 to HV2 and kmsArn
    var uuidForHV2AndKmsArnMutationTest :- expect UUID.GenerateUUID();
    var testIdForHV2AndKmsArnMutation := happyCaseId + "-" + uuidForHV2AndKmsArnMutationTest;
    var mutationsRequestChangeHVAndKmsArn := Types.Mutations(
      TerminalKmsArn := Some(Fixtures.kmsArnForHV2),
      TerminalHierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2));
    var keyStoreTerminal :- expect Fixtures.DefaultKeyStore(
      kmsId:=Fixtures.kmsArnForHV2,
      ddbClient?:=Some(ddbClient),
      kmsClient?:=Some(kmsClient));
    mutationHappyPathTest(
      ddbClient := ddbClient,
      storage := storage,
      keyStoreAdminUnderTest := underTest,
      strategy := strategy,
      keyStoreTerminal := keyStoreTerminal,
      branchKeyIdentifier := uuidForHV2AndKmsArnMutationTest,
      mutationsRequest := mutationsRequestChangeHVAndKmsArn,
      versionCount := 1,
      doNotVersion := true
    );
  }

  method mutationHappyPathTest(
    ddbClient: DDB.Types.IDynamoDBClient,
    storage: KeyStoreTypes.IKeyStorageInterface,
    keyStoreAdminUnderTest: Types.IKeyStoreAdminClient,
    strategy: Types.KeyManagementStrategy,
    keyStoreTerminal: KeyStoreTypes.IKeyStoreClient,
    branchKeyIdentifier: string,
    mutationsRequest: Types.Mutations,
    versionCount: int,
    doNotVersion: bool
  )
    requires ddbClient.ValidState()
    requires storage.ValidState()
    requires keyStoreAdminUnderTest.ValidState()
    requires keyStoreTerminal.ValidState()
    requires 0 <= versionCount <= 5
    modifies ddbClient.Modifies
    modifies storage.Modifies
    modifies keyStoreAdminUnderTest.Modifies
    modifies keyStoreTerminal.Modifies
  {
    Fixtures.CreateHappyCaseId(id:=branchKeyIdentifier, versionCount:=versionCount);
    var initInput := Types.InitializeMutationInput(
      Identifier := branchKeyIdentifier,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()),
      DoNotVersion := Some(true));
    var initializeOutput :- expect keyStoreAdminUnderTest.InitializeMutation(initInput);
    var initializeToken := initializeOutput.MutationToken;

    // print testLogPrefix + " Initialized Mutation. M-Lock UUID " + initializeToken.UUID + "\n";

    var testInput := Types.ApplyMutationInput(
      MutationToken := initializeToken,
      PageSize := Some(24),
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()));
    var applyOutput :- expect keyStoreAdminUnderTest.ApplyMutation(testInput);

    // print testLogPrefix + " Applied Mutation w/ pageSize 24. branchKeyIdentifier: " + branchKeyIdentifier + "\n";
    expect applyOutput.MutationResult.CompleteMutation?, "Apply Mutation output should not continue!";

    var versionQuery := KeyStoreTypes.QueryForVersionsInput(
      Identifier := branchKeyIdentifier,
      PageSize := 24
    );
    var queryOut :- expect storage.QueryForVersions(versionQuery);
    var items := queryOut.Items;
    expect
      |items| == 2,
      "Test expects there to be 2 Decrypt Only items! Found: " + String.Base10Int2String(|items|);

    var itemIndex := 0;
    var inputV: KeyStoreTypes.GetBranchKeyVersionInput;
    while itemIndex < |items|
    {
      var item := items[itemIndex];
      expect
        item.Type.HierarchicalSymmetricVersion?,
        "Query for Decrypt Only returned a non-Decrypt Only!";
      var versionUUID := item.Type.HierarchicalSymmetricVersion.Version;
      expect "type" in item.EncryptionContext, "Decrypt Only item is missing 'type' from EC!!";
      var expectedKmsArn := if mutationsRequest.TerminalKmsArn.Some? then
        mutationsRequest.TerminalKmsArn.value
      else
        Fixtures.keyArn;
      expect
        item.KmsArn == expectedKmsArn,
        "KmsArn of Item is incorrect. Item: " + versionUUID;
      expect Structure.HIERARCHY_VERSION in item.EncryptionContext, "Hierarchy version not in EC";
      expect
        item.EncryptionContext[Structure.HIERARCHY_VERSION] == "2",
        "Hierarchy version is not mutated to 2";
      inputV := KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyIdentifier,
        branchKeyVersion := versionUUID
      );
      var _ :- expect keyStoreTerminal.GetBranchKeyVersion(inputV);
      itemIndex := 1 + itemIndex;
    }

    var a :- expect keyStoreTerminal.GetActiveBranchKey(KeyStoreTypes.GetActiveBranchKeyInput(branchKeyIdentifier := branchKeyIdentifier));
    var _ :- expect keyStoreTerminal.GetBeaconKey(KeyStoreTypes.GetBeaconKeyInput(branchKeyIdentifier := branchKeyIdentifier));
    var _ := CleanupItems.DeleteBranchKey(Identifier:=branchKeyIdentifier, ddbClient:=ddbClient);
  }

  method verifyMutationResults(
    storage: KeyStoreTypes.IKeyStorageInterface,
    keyStoreTerminal: KeyStoreTypes.IKeyStoreClient,
    branchKeyIdentifier: string,
    mutationsRequest: Types.Mutations
  ) returns (success: bool)
    requires storage.ValidState()
    requires keyStoreTerminal.ValidState()
    modifies storage.Modifies
    modifies keyStoreTerminal.Modifies
  {
    var versionQuery := KeyStoreTypes.QueryForVersionsInput(
      Identifier := branchKeyIdentifier,
      PageSize := 24
    );
    var queryOut :- expect storage.QueryForVersions(versionQuery);
    var items := queryOut.Items;
    expect
      |items| == 2,
      "Test expects there to be 2 Decrypt Only items! Found: " + String.Base10Int2String(|items|);

    var itemIndex := 0;
    var inputV: KeyStoreTypes.GetBranchKeyVersionInput;
    while itemIndex < |items|
    {
      var item := items[itemIndex];
      expect
        item.Type.HierarchicalSymmetricVersion?,
        "Query for Decrypt Only returned a non-Decrypt Only!";
      var versionUUID := item.Type.HierarchicalSymmetricVersion.Version;
      expect "type" in item.EncryptionContext, "Decrypt Only item is missing 'type' from EC!!";

      // Use mutationsRequest.TerminalKmsArn if provided, otherwise use Fixtures.keyArn
      var expectedKmsArn := if mutationsRequest.TerminalKmsArn.Some? then
        mutationsRequest.TerminalKmsArn.value
      else
        Fixtures.keyArn;
      expect
        item.KmsArn == expectedKmsArn,
        "KmsArn of Item is incorrect. Item: " + versionUUID;

      expect Structure.HIERARCHY_VERSION in item.EncryptionContext, "Hierarchy version not in EC";
      expect
        item.EncryptionContext[Structure.HIERARCHY_VERSION] == "2",
        "Hierarchy version is not mutated to 2";

      inputV := KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyIdentifier,
        branchKeyVersion := versionUUID
      );
      var _ :- expect keyStoreTerminal.GetBranchKeyVersion(inputV);
      itemIndex := 1 + itemIndex;
    }

    var _ :- expect keyStoreTerminal.GetActiveBranchKey(KeyStoreTypes.GetActiveBranchKeyInput(branchKeyIdentifier := branchKeyIdentifier));
    var _ :- expect keyStoreTerminal.GetBeaconKey(KeyStoreTypes.GetBeaconKeyInput(branchKeyIdentifier := branchKeyIdentifier));

    return true;
  }

}