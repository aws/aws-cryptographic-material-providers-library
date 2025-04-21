// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../AdminFixtures.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"

module {:options "/functionSyntax:4" } TestHierarchyVersion {
  import opened Wrappers
  import UTF8
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import KeyStoreErrorMessages
  import AdminFixtures
  import Fixtures
  import CleanupItems
  import UUID
  import Time
  import Structure
  import String = StandardLibrary.String

  method {:test} TestInitializeMutationFailsWithNonUniqueBranchKeyContext() {

    var testId := "DO-NOT-EDIT-Branch-Key-For-HasUniqueTransformedKeys-Check";
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();

    // Commented code creates a branch key and adds {"Robbie": "Is a dog."}
    // to the branch key item outside of the library's operations.
    // Adding {"Robbie": "Is a dog."} will create a non unique branch key context

    // Fixtures.CreateHappyCaseId(
    //   id:=testId,
    //   versionCount:=0,
    //   customEC := map[UTF8.EncodeAscii("Robbie") := UTF8.EncodeAscii("Is a dog.")]);
    // var _ :- expect AdminFixtures.AddAttributeWithoutLibrary(
    //   id:=testId,
    //   keyValue:=AdminFixtures.KeyValue(key:="Robbie", value:="Is a dog."),
    //   alsoViolateBeacon? := true, ddbClient? := Some(ddbClient),
    //   kmsClient?:=Some(kmsClient));

    var underTest :- expect AdminFixtures.DefaultAdmin();
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var systemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage());

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

    expect initializeOutput.Failure?, "Should have failed to InitializeMutation HV-2.";
    expect initializeOutput.error.KeyStoreAdminException?, "Should have KeyStoreAdminException";
    expect initializeOutput.error.message == KeyStoreErrorMessages.NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS, "Incorrect error message. Should have had `KeyStoreErrorMessages.NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS`";
  }

  method {:test} TestNonUniqueTerminalAndInferredECKeys() {

    var testId := "DO-NOT-EDIT-Branch-Key-For-TestNonUniqueTerminalAndInferredECKeys-Check";
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();

    // Commented code creates a branch key and adds {"Koda": "Is a dog."}
    // to the branch key item outside of the library's operations.
    // Adding {"Koda": "Is a dog."} will NOT create a non unique branch key context

    // Fixtures.CreateHappyCaseId(
    //   id:=testId,
    //   versionCount:=0,
    //   customEC := map[UTF8.EncodeAscii("Robbie") := UTF8.EncodeAscii("Is a dog.")]);
    // var _ :- expect AdminFixtures.AddAttributeWithoutLibrary(
    //   id:=testId,
    //   keyValue:=AdminFixtures.KeyValue(key:="Koda", value:="Is a dog."),
    //   alsoViolateBeacon? := true, ddbClient? := Some(ddbClient),
    //   kmsClient?:=Some(kmsClient));

    var underTest :- expect AdminFixtures.DefaultAdmin();
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var systemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage());

    var terminalEC: KeyStoreTypes.EncryptionContextString := map["Koda" := "Is a dog."];
    var mutationsRequest := Types.Mutations(
      TerminalKmsArn := Some(Fixtures.postalHornKeyArn),
      TerminalHierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2),
      TerminalEncryptionContext := Some(terminalEC)
    );
    var initInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := systemKey,
      DoNotVersion := Some(true));
    var initializeOutput := underTest.InitializeMutation(initInput);

    expect initializeOutput.Failure?, "Should have failed to InitializeMutation HV-2.";
    expect initializeOutput.error.KeyStoreAdminException?, "Should have KeyStoreAdminException";
    expect initializeOutput.error.message == KeyStoreErrorMessages.NOT_UNIQUE_TERMINAL_EC_AND_EXISTING_ATTRIBUTE, "Incorrect error message. Should have had `KeyStoreErrorMessages.NOT_UNIQUE_TERMINAL_EC_AND_EXISTING_ATTRIBUTE`";
  }

  // TODO-HV-2-M2: Uncomment and work (if needed) in happy case
  const happyCaseId := "test-mutate-hv-only"
  const customEC := "aws-crypto-ec:Robbie"
  const kmsId: string := Fixtures.keyArn
  const physicalName: string := Fixtures.branchKeyStoreName
  const logicalName: string := Fixtures.logicalKeyStoreName
  const testLogPrefix := "\nTestKmsArnChanged :: TestHappyCase :: "

  method {:test} {:vcs_split_on_every_assert} TestHappyCase()
  {
    // print " running";

    // expect false; // disable test till other investigation is done
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();

    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var keyStoreOriginal :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    var uuid :- expect UUID.GenerateUUID();
    var testId := happyCaseId + "-" + uuid;

    Fixtures.CreateHappyCaseId(id:=testId, versionCount:=1);

    // print testLogPrefix + " Created the test items with 2 versions! testId: " + testId + "\n";

    var timestamp :- expect Time.GetCurrentTimeStamp();
    var mutationsRequest := Types.Mutations(
      TerminalHierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2));
    var initInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()),
      DoNotVersion := Some(true));
    var initializeOutput :- expect underTest.InitializeMutation(initInput);
    var initializeToken := initializeOutput.MutationToken;

    // print testLogPrefix + " Initialized Mutation. M-Lock UUID " + initializeToken.UUID + "\n";

    var testInput := Types.ApplyMutationInput(
      MutationToken := initializeToken,
      PageSize := Some(24),
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()));
    var applyOutput :- expect underTest.ApplyMutation(testInput);

    // print testLogPrefix + " Applied Mutation w/ pageSize 24. testId: " + testId + "\n";
    expect applyOutput.MutationResult.CompleteMutation?, "Apply Mutation output should not continue!";

    var versionQuery := KeyStoreTypes.QueryForVersionsInput(
      Identifier := testId,
      PageSize := 24
    );
    var queryOut :- expect storage.QueryForVersions(versionQuery);
    var items := queryOut.Items;
    expect
      |items| == 2,
      "Test expects there to be 3 Decrypt Only items! Found: " + String.Base10Int2String(|items|);
    // print testLogPrefix + " Read the 3 Decrypt Only items! testId: " + testId + "\n";

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
      expect
        item.KmsArn == Fixtures.keyArn,
        "KmsArn of Item is incorrect. Item: " + versionUUID;
      expect Structure.HIERARCHY_VERSION in item.EncryptionContext, "Hierarchy version not in EC";
      expect
        item.EncryptionContext[Structure.HIERARCHY_VERSION] == "2",
        "Hierarchy version is not mutated to 2";
      inputV := KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := testId,
        branchKeyVersion := versionUUID
      );
      var _ :- expect keyStoreOriginal.GetBranchKeyVersion(inputV);

      // print testLogPrefix + " Validated Decrypt Only and tried to clean it up: " + item.EncryptionContext["type"] + "\n";
      itemIndex := 1 + itemIndex;
    }

    var _ :- expect keyStoreOriginal.GetActiveBranchKey(KeyStoreTypes.GetActiveBranchKeyInput(branchKeyIdentifier := testId));
    // print testLogPrefix + " Active Validated with KMS/KeyStore: " + testId + "\n";

    var _ :- expect keyStoreOriginal.GetBeaconKey(KeyStoreTypes.GetBeaconKeyInput(branchKeyIdentifier := testId));
    // print testLogPrefix + " Beacon Validated with KMS/KeyStore: " + testId + "\n";
    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);

    // print "TestKmsArnChanged.TestHappyCase: ";
  }
}