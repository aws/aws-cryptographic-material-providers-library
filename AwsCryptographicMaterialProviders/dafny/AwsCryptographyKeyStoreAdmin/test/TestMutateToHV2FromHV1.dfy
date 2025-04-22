// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/src/HierarchicalVersionUtils.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "AdminFixtures.dfy"

module {:options "/functionSyntax:4" } TestMutateToHV2FromHV1 {
  import UUID
  import AdminFixtures
  import CleanupItems
  import opened Fixtures
  import opened Wrappers
  import DDB = Com.Amazonaws.Dynamodb
  import HvUtils = HierarchicalVersionUtils
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
  const originalKmsId: string := Fixtures.keyArn
  const terminalKmsId: string := Fixtures.kmsArnForHV2
  const originalEC: KeyStoreTypes.EncryptionContextString := Fixtures.RobbieECString
  const newCustomEC: KeyStoreTypes.EncryptionContextString := Fixtures.KodaECString

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
    Fixtures.CreateHappyCaseId(
      id := branchKeyIdentifier,
      versionCount := versionCount
    );
    var initInput := Types.InitializeMutationInput(
      Identifier := branchKeyIdentifier,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()),
      DoNotVersion := Some(doNotVersion));
    var initializeOutput :- expect keyStoreAdminUnderTest.InitializeMutation(initInput);
    var initializeToken := initializeOutput.MutationToken;
    var testInput := Types.ApplyMutationInput(
      MutationToken := initializeToken,
      PageSize := Some(24),
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()));
    var applyOutput :- expect keyStoreAdminUnderTest.ApplyMutation(testInput);

    expect applyOutput.MutationResult.CompleteMutation?, "Apply Mutation output should not continue!";

    var expectedDecryptOnlyItems := if doNotVersion then
      versionCount + 1
    else
      versionCount + 2;
    verifyMutationResults(
      storage := storage,
      keyStoreTerminal := keyStoreTerminal,
      branchKeyIdentifier := branchKeyIdentifier,
      mutationsRequest := mutationsRequest,
      expectedDecryptOnlyItems := expectedDecryptOnlyItems
    );

    var _ := CleanupItems.DeleteBranchKey(Identifier:=branchKeyIdentifier, ddbClient:=ddbClient);
  }

  method verifyMutationResults(
    storage: KeyStoreTypes.IKeyStorageInterface,
    keyStoreTerminal: KeyStoreTypes.IKeyStoreClient,
    branchKeyIdentifier: string,
    mutationsRequest: Types.Mutations,
    expectedDecryptOnlyItems: int
  )
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
    var (expectedKmsArn, expectedEncryptionContext) := getExpectedTerminalValues(mutationsRequest);
    expect
      |items| == expectedDecryptOnlyItems,
      "Test expects there to be " + String.Base10Int2String(expectedDecryptOnlyItems) + " Decrypt Only items! Found: " + String.Base10Int2String(|items|);

    var itemIndex := 0;

    var branchKeyVersionInputForStorage: KeyStoreTypes.GetEncryptedBranchKeyVersionInput;
    var branchKeyVersionOutputFromStorage: KeyStoreTypes.GetEncryptedBranchKeyVersionOutput;
    var branchKeyVersionInputForKeyStore: KeyStoreTypes.GetBranchKeyVersionInput;
    var branchKeyVersionOutputFromKeyStore: KeyStoreTypes.GetBranchKeyVersionOutput;
    var branchKeyVersionOutputEC: KeyStoreTypes.EncryptionContextString;

    while itemIndex < |items|
    {
      var item := items[itemIndex];
      expect
        item.Type.HierarchicalSymmetricVersion?,
        "Query for Decrypt Only returned a non-Decrypt Only!";
      var versionUUID := item.Type.HierarchicalSymmetricVersion.Version;
      expect "type" in item.EncryptionContext, "Decrypt Only item is missing 'type' from EC!!";
      verifyTerminalProperties(item.EncryptionContext, expectedEncryptionContext, expectedKmsArn);

      // Get branchKeyVersion from storage
      branchKeyVersionInputForStorage := KeyStoreTypes.GetEncryptedBranchKeyVersionInput(
        Identifier := branchKeyIdentifier,
        Version := versionUUID
      );
      branchKeyVersionOutputFromStorage :- expect storage.GetEncryptedBranchKeyVersion(branchKeyVersionInputForStorage);
      verifyTerminalProperties(branchKeyVersionOutputFromStorage.Item.EncryptionContext, expectedEncryptionContext, expectedKmsArn);

      // Get branchKeyVersion from keystore
      branchKeyVersionInputForKeyStore := KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyIdentifier,
        branchKeyVersion := versionUUID
      );
      branchKeyVersionOutputFromKeyStore :- expect keyStoreTerminal.GetBranchKeyVersion(branchKeyVersionInputForKeyStore);
      branchKeyVersionOutputEC :- expect HvUtils.DecodeEncryptionContext(branchKeyVersionOutputFromKeyStore.branchKeyMaterials.encryptionContext);
      expect branchKeyVersionOutputEC == expectedEncryptionContext;

      itemIndex := 1 + itemIndex;
    }
    // Get activeBranchKey from storage
    var activeBranchKeyInputForStorage := KeyStoreTypes.GetEncryptedActiveBranchKeyInput(
      Identifier := branchKeyIdentifier
    );
    var activeBranchKeyOutputFromStorage :- expect storage.GetEncryptedActiveBranchKey(activeBranchKeyInputForStorage);
    verifyTerminalProperties(activeBranchKeyOutputFromStorage.Item.EncryptionContext, expectedEncryptionContext, expectedKmsArn);
    // Get activeBranchKey from keystore
    var activeBranchKeyOutput :- expect keyStoreTerminal.GetActiveBranchKey(KeyStoreTypes.GetActiveBranchKeyInput(branchKeyIdentifier := branchKeyIdentifier));
    var activeBranchKeyEC :- expect HvUtils.DecodeEncryptionContext(activeBranchKeyOutput.branchKeyMaterials.encryptionContext);
    expect activeBranchKeyEC == expectedEncryptionContext;

    // Get BeaconKey from storage
    var beaconKeyInputForStorage := KeyStoreTypes.GetEncryptedBeaconKeyInput(
      Identifier := branchKeyIdentifier
    );
    var beaconKeyOutputFromStorage :- expect storage.GetEncryptedBeaconKey(beaconKeyInputForStorage);
    verifyTerminalProperties(activeBranchKeyOutputFromStorage.Item.EncryptionContext, expectedEncryptionContext, expectedKmsArn);
    // Get BeaconKey from keystore
    var beaconKeyOutput :- expect keyStoreTerminal.GetBeaconKey(KeyStoreTypes.GetBeaconKeyInput(branchKeyIdentifier := branchKeyIdentifier));
    var beaconKeyEC :- expect HvUtils.DecodeEncryptionContext(beaconKeyOutput.beaconKeyMaterials.encryptionContext);
    expect beaconKeyEC == expectedEncryptionContext;
  }

  // returns (expectedKmsArn, expectedEncryptionContext)
  function getExpectedTerminalValues(
    mutationsRequest: Types.Mutations
  ) : (Result:(string, KeyStoreTypes.EncryptionContextString))
  {
    var kmsArn := if mutationsRequest.TerminalKmsArn.Some? then
                    mutationsRequest.TerminalKmsArn.value
                  else
                    originalKmsId;

    var encryptionContext := if mutationsRequest.TerminalEncryptionContext.Some? then
                               mutationsRequest.TerminalEncryptionContext.value
                             else
                               originalEC;

    (kmsArn, encryptionContext)
  }

  method verifyTerminalProperties(
    actualEC: KeyStoreTypes.EncryptionContextString,
    expectedCustomEC: KeyStoreTypes.EncryptionContextString,
    expectedKMSArn: string
  ) {
    expect Structure.BranchKeyContext?(actualEC);
    expect HvUtils.HasUniqueTransformedKeys?(actualEC);
    expect HvUtils.SelectKmsEncryptionContextForHv2(actualEC) == expectedCustomEC;
    expect
      actualEC[Structure.HIERARCHY_VERSION] == "2",
      "Hierarchy version is not mutated to 2";
    expect actualEC[Structure.KMS_FIELD] == expectedKMSArn;
  }
}