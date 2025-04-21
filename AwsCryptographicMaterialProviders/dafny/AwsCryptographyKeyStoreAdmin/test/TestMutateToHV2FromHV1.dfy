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
  import opened Fixtures
  import opened Wrappers
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes

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

    // var timestamp :- expect Time.GetCurrentTimeStamp();
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
      "Test expects there to be 2 Decrypt Only items! Found: " + String.Base10Int2String(|items|);
    // print testLogPrefix + " Read the 2 Decrypt Only items! testId: " + testId + "\n";

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