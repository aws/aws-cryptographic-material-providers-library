// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../../../AwsCryptographyKeyStore/src/HierarchicalVersionUtils.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../AdminFixtures.dfy"

module {:options "/functionSyntax:4" } TestMutationHappyPath {
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

  const originalKmsId: string := Fixtures.keyArn
  const originalEC: KeyStoreTypes.EncryptionContextString := Fixtures.RobbieECString

  /**
    * This helper method tests the end-to-end mutation.
    * 
    * This helper method asserts:
    * 1. That a mutation can be successfully initialized
    * 2. That the mutation can be successfully applied
    * 3. That all branch key items after mutation are correctly updated with the terminal properties.
    */
  method MutationRoundTripTest(
    ddbClient: DDB.Types.IDynamoDBClient,
    storage: KeyStoreTypes.IKeyStorageInterface,
    keyStoreAdminUnderTest: Types.IKeyStoreAdminClient,
    strategy: Types.KeyManagementStrategy,
    keyStoreTerminal: KeyStoreTypes.IKeyStoreClient,
    branchKeyIdentifier: string,
    mutationsRequest: Types.Mutations,
    versionCount: int,
    initialHV: KeyStoreTypes.HierarchyVersion,
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
    ensures ddbClient.ValidState()
    ensures storage.ValidState()
    ensures keyStoreAdminUnderTest.ValidState()
    ensures keyStoreTerminal.ValidState()
  {
    // Create Branch Key with initial HierarchyVersion
    AdminFixtures.CreateHappyCaseId(
      id := branchKeyIdentifier,
      versionCount := versionCount,
      hierarchyVersion := initialHV
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
      initialHV := initialHV,
      keyStoreTerminal := keyStoreTerminal,
      branchKeyIdentifier := branchKeyIdentifier,
      mutationsRequest := mutationsRequest,
      expectedDecryptOnlyItems := expectedDecryptOnlyItems
    );

    var _ := CleanupItems.DeleteBranchKey(Identifier:=branchKeyIdentifier, ddbClient:=ddbClient);
  }

  /**
    * This helper method tests restarting an in-flight mutation 
    * by the deletion of the Mutation Index.
    * 
    * This helper method asserts:
    * 1. That the Mutation Index can be deleted and recreated successfully via InitializeMutation
    * 2. That the mutation token can be retrieved via InitializeMutation after index deletion
    * 3. That the mutation process can be resumed and completed after restart
    */
  method MutationRecoveryTest(
    ddbClient: DDB.Types.IDynamoDBClient,
    storage: KeyStoreTypes.IKeyStorageInterface,
    keyStoreAdminUnderTest: Types.IKeyStoreAdminClient,
    strategy: Types.KeyManagementStrategy,
    keyStoreTerminal: KeyStoreTypes.IKeyStoreClient,
    branchKeyIdentifier: string,
    mutationsRequest: Types.Mutations,
    versionCount: int,
    initialHV: KeyStoreTypes.HierarchyVersion,
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
    ensures ddbClient.ValidState()
    ensures storage.ValidState()
    ensures keyStoreAdminUnderTest.ValidState()
    ensures keyStoreTerminal.ValidState()
  {
    // Create Branch Key with initial HierarchyVersion
    AdminFixtures.CreateHappyCaseId(
      id := branchKeyIdentifier,
      versionCount := versionCount,
      hierarchyVersion := initialHV
    );

    // Step 1: Initialize Mutation
    var initInput := Types.InitializeMutationInput(
      Identifier := branchKeyIdentifier,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()),
      DoNotVersion := Some(doNotVersion));
    var initializeOutput :- expect keyStoreAdminUnderTest.InitializeMutation(initInput);

    // Step 2: Apply first mutation with small page size
    var applyInput := Types.ApplyMutationInput(
      MutationToken := initializeOutput.MutationToken,
      PageSize := Some(1),
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()));
    var applyOutput? := keyStoreAdminUnderTest.ApplyMutation(applyInput);
    expect applyOutput?.Success?, "First Apply Mutation FAILED";

    // Step 3: Delete Mutation Index to restart the mutation from the beginning
    var cleanedVersion? :- expect CleanupItems.DeleteTypeWithFailure(branchKeyIdentifier, Structure.MUTATION_INDEX_TYPE, ddbClient);

    // Step 4: Resume mutation without Index
    var resumedOutput :- expect keyStoreAdminUnderTest.InitializeMutation(initInput);
    expect resumedOutput.InitializeMutationFlag == Types.InitializeMutationFlag.ResumedWithoutIndex;

    // Step 5: Complete remaining mutations
    var finalApplyInput := Types.ApplyMutationInput(
      MutationToken := resumedOutput.MutationToken,
      PageSize := Some(24),
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()));
    var finalApplyOutput :- expect keyStoreAdminUnderTest.ApplyMutation(finalApplyInput);

    expect finalApplyOutput.MutationResult.CompleteMutation?, "Final Apply Mutation should complete!";

    // Verify results
    var expectedDecryptOnlyItems := if doNotVersion then
      versionCount + 1
    else
      versionCount + 2;
    verifyMutationResults(
      storage := storage,
      initialHV := initialHV,
      keyStoreTerminal := keyStoreTerminal,
      branchKeyIdentifier := branchKeyIdentifier,
      mutationsRequest := mutationsRequest,
      expectedDecryptOnlyItems := expectedDecryptOnlyItems
    );

    var _ := CleanupItems.DeleteBranchKey(Identifier:=branchKeyIdentifier, ddbClient:=ddbClient);
  }

  method verifyMutationResults(
    storage: KeyStoreTypes.IKeyStorageInterface,
    initialHV: KeyStoreTypes.HierarchyVersion,
    keyStoreTerminal: KeyStoreTypes.IKeyStoreClient,
    branchKeyIdentifier: string,
    mutationsRequest: Types.Mutations,
    expectedDecryptOnlyItems: int
  )
    requires storage.ValidState() && keyStoreTerminal.ValidState()
    modifies storage.Modifies, keyStoreTerminal.Modifies
  {
    var versionQuery := KeyStoreTypes.QueryForVersionsInput(
      Identifier := branchKeyIdentifier,
      PageSize := 24
    );
    var queryOut :- expect storage.QueryForVersions(versionQuery);
    var items := queryOut.Items;
    var (expectedKmsArn, expectedHV, expectedEncryptionContext) := getExpectedTerminalValues(mutationsRequest, initialHV);
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
      verifyTerminalProperties(item.EncryptionContext, expectedEncryptionContext, expectedKmsArn, expectedHV);

      // Get branchKeyVersion from storage
      branchKeyVersionInputForStorage := KeyStoreTypes.GetEncryptedBranchKeyVersionInput(
        Identifier := branchKeyIdentifier,
        Version := versionUUID
      );
      branchKeyVersionOutputFromStorage :- expect storage.GetEncryptedBranchKeyVersion(branchKeyVersionInputForStorage);
      verifyTerminalProperties(branchKeyVersionOutputFromStorage.Item.EncryptionContext, expectedEncryptionContext, expectedKmsArn, expectedHV);

      // Get branchKeyVersion from keystore
      branchKeyVersionInputForKeyStore := KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyIdentifier,
        branchKeyVersion := versionUUID
      );
      branchKeyVersionOutputFromKeyStore :- expect keyStoreTerminal.GetBranchKeyVersion(branchKeyVersionInputForKeyStore);
      branchKeyVersionOutputEC :- expect HvUtils.DecodeEncryptionContext(branchKeyVersionOutputFromKeyStore.branchKeyMaterials.encryptionContext);
      expect branchKeyVersionOutputEC == expectedEncryptionContext,
        "Retrived branch Key Version EC from keystore did not match with the expected EC.";

      itemIndex := 1 + itemIndex;
    }
    // Get activeBranchKey from storage
    var activeBranchKeyInputForStorage := KeyStoreTypes.GetEncryptedActiveBranchKeyInput(
      Identifier := branchKeyIdentifier
    );
    var activeBranchKeyOutputFromStorage :- expect storage.GetEncryptedActiveBranchKey(activeBranchKeyInputForStorage);
    verifyTerminalProperties(activeBranchKeyOutputFromStorage.Item.EncryptionContext, expectedEncryptionContext, expectedKmsArn, expectedHV);
    // Get activeBranchKey from keystore
    var activeBranchKeyOutput :- expect keyStoreTerminal.GetActiveBranchKey(KeyStoreTypes.GetActiveBranchKeyInput(branchKeyIdentifier := branchKeyIdentifier));
    var activeBranchKeyEC :- expect HvUtils.DecodeEncryptionContext(activeBranchKeyOutput.branchKeyMaterials.encryptionContext);
    expect activeBranchKeyEC == expectedEncryptionContext,
      "Retrived active branch key EC from keystore did not match with the expected EC";

    // Get BeaconKey from storage
    var beaconKeyInputForStorage := KeyStoreTypes.GetEncryptedBeaconKeyInput(
      Identifier := branchKeyIdentifier
    );
    var beaconKeyOutputFromStorage :- expect storage.GetEncryptedBeaconKey(beaconKeyInputForStorage);
    verifyTerminalProperties(activeBranchKeyOutputFromStorage.Item.EncryptionContext, expectedEncryptionContext, expectedKmsArn, expectedHV);
    // Get BeaconKey from keystore
    var beaconKeyOutput :- expect keyStoreTerminal.GetBeaconKey(KeyStoreTypes.GetBeaconKeyInput(branchKeyIdentifier := branchKeyIdentifier));
    var beaconKeyEC :- expect HvUtils.DecodeEncryptionContext(beaconKeyOutput.beaconKeyMaterials.encryptionContext);
    expect beaconKeyEC == expectedEncryptionContext,
      "Retrived beacon key EC from keystore did not match with the expected EC";
  }

  // returns (expectedKmsArn, expectedHV, expectedEncryptionContext)
  function getExpectedTerminalValues(
    mutationsRequest: Types.Mutations,
    initialHV: KeyStoreTypes.HierarchyVersion
  ) : (Result:(string, string, KeyStoreTypes.EncryptionContextString))
  {
    var kmsArn := if mutationsRequest.TerminalKmsArn.Some? then
                    mutationsRequest.TerminalKmsArn.value
                  else
                    originalKmsId;

    var hvVersion := if mutationsRequest.TerminalHierarchyVersion.Some? then
                       mutationsRequest.TerminalHierarchyVersion.value
                     else
                       initialHV;

    var encryptionContext := if mutationsRequest.TerminalEncryptionContext.Some? then
                               mutationsRequest.TerminalEncryptionContext.value
                             else
                               originalEC;

    (kmsArn, Structure.HierarchyVersionToString(hvVersion), encryptionContext)
  }

  method verifyTerminalProperties(
    actualEC: KeyStoreTypes.EncryptionContextString,
    expectedCustomEC: KeyStoreTypes.EncryptionContextString,
    expectedKMSArn: string,
    expectedHV: string
  ) {
    expect Structure.BranchKeyContext?(actualEC),
      "Actual EC is not a branch key context. It might not contain restricted keys.";
    if (expectedHV == "2") {
      expect HvUtils.HasUniqueTransformedKeys?(actualEC),
        "Actual EC does not have unique transformed keys.";
      expect HvUtils.SelectKmsEncryptionContextForHv2(actualEC) == expectedCustomEC,
        "Actual customer send EC and expected customer send EC did not match.";
    }
    expect
      actualEC[Structure.HIERARCHY_VERSION] == expectedHV,
      "Unexpect Hierarchy version found in the EC.";
    expect actualEC[Structure.KMS_FIELD] == expectedKMSArn,
      "Unexpect KMS Arn found in the EC.";
  }
}