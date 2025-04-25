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

  // TODO-HV-2-FF: MutationRoundTripTest could be used by all mutation happy case test.
  // This is only being used by happycases with terminal hv as 2
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
  {
    match initialHV {
      case v1 =>
        Fixtures.CreateHappyCaseId(
          id := branchKeyIdentifier,
          versionCount := versionCount
        );
      case v2 =>
        // TODO-HV-2-Version: Once, we support version key for HV2 keys.
        // Uncomment this to directly create HV2 keys with versions.
        // AdminFixtures.CreateHappyCaseId(
        //   id := branchKeyIdentifier,
        //   // versionCount := versionCount,
        //   hierarchyVersion := initialHV
        // );
        Fixtures.CreateHappyCaseId(
          id := branchKeyIdentifier,
          versionCount := versionCount
        );
        // TODO-HV-2-Version: Below is Temporary Logic to have HV-2 Key with multiple decrypt-only/version items
        // Add Mutation Logic Here for Mutating from HV-1 to HV-2
        var initInput := Types.InitializeMutationInput(
          Identifier := branchKeyIdentifier,
          Mutations := Types.Mutations(
            TerminalHierarchyVersion := Some(initialHV)
          ),
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
    }

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