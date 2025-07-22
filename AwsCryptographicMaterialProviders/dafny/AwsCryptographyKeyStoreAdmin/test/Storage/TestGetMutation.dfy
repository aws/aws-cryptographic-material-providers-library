// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../AdminFixtures.dfy"
include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"


module {:options "/functionSyntax:4"} TestGetMutation {
  import Types = AwsCryptographyKeyStoreAdminTypes
  import UInt = Fixtures.UInt
  import KeyStoreTypes = Fixtures.Types
  import UTF8 = Fixtures.UTF8
  import opened Wrappers
  import DefaultKeyStorageInterface
  import Fixtures
  import AdminFixtures
  import Structure
  import DDB = Com.Amazonaws.Dynamodb
  import KMS = Com.Amazonaws.Kms
  import KeyStore
  import Time
  import CleanupItems

  const TEST_NO_COMMITMENT_NO_INDEX_BKID := "test-storage-get-mutation-no-commitment-no-index"
  method {:test} TestNoCommitmentNoIndexExpectSuccessWithNone()
  {
    var underTest :- expect Fixtures.DefaultStorage();
    var input := KeyStoreTypes.GetMutationInput(
      Identifier := TEST_NO_COMMITMENT_NO_INDEX_BKID
    );
    var output? := underTest.GetMutation(input);
    expect output?.Success?, "GetMutation should have succeeded, but it failed!";
    var output := output?.value;
    expect output.MutationCommitment.None?, "There should be no Mutation Commitment";
    expect output.MutationIndex.None?, "There should be no Mutation Index";
  }

  const TEST_YES_COMMITMENT_NO_INDEX_BKID := "test-storage-get-mutation-yes-commitment-no-index"
  method {:test} TestYesCommitmentNoIndexExpectSuccessWithNone()
  {
    // CreateCommitmentIndexBK(id := TEST_YES_COMMITMENT_NO_INDEX_BKID); // Insert to re-create the test-id.
    var underTest :- expect Fixtures.DefaultStorage();
    var input := KeyStoreTypes.GetMutationInput(
      Identifier := TEST_YES_COMMITMENT_NO_INDEX_BKID
    );
    var output? := underTest.GetMutation(input);
    expect output?.Success?, "GetMutation should have succeeded, but it failed!";
    var output := output?.value;
    if (!output.MutationCommitment.Some?){
      print "GetMutation succeeded but Mutation Commitment was not returned! Printing output object: ", output;
    }
    expect output.MutationCommitment.Some?, "There should be a Mutation Commitment";
    expect output.MutationIndex.None?, "There should be no Mutation Index";
  }

  const TEST_NO_COMMITMENT_YES_INDEX_BKID := "test-storage-get-mutation-no-commitment-yes-index"
  method {:test} TestNoCommitmentYesIndexExpectSuccessWithNone()
  {
    // CreateCommitmentIndexBK(id := TEST_NO_COMMITMENT_YES_INDEX_BKID, withCommitment := false, withIndex := true); // Insert to re-create the test-id.
    var underTest :- expect Fixtures.DefaultStorage();
    var input := KeyStoreTypes.GetMutationInput(
      Identifier := TEST_NO_COMMITMENT_YES_INDEX_BKID
    );
    var output? := underTest.GetMutation(input);
    expect output?.Success?, "GetMutation should have succeeded, but it failed!";
    var output := output?.value;
    expect output.MutationCommitment.None?, "There should be a Mutation Commitment";
    expect output.MutationIndex.Some?, "There should be no Mutation Index";
  }

  method CreateCommitmentIndexBK(
    nameonly id: string,
    nameonly withCommitment: bool := true,
    nameonly withIndex: bool := false
  )
  {
    // Create BK
    Fixtures.CreateHappyCaseId(id:=id, versionCount:=2);
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    // Validate BK
    var _ :- expect keyStore.GetActiveBranchKey(KeyStoreTypes.GetActiveBranchKeyInput(branchKeyIdentifier := id));

    // Prep for mutation
    var timestamp :- expect Time.GetCurrentTimeStamp();
    var newCustomEC: KeyStoreTypes.EncryptionContextString := map["Robbie" := timestamp];
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var ksAdmin :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));

    // Start a Mutation; do not finish it.
    var mutationsRequest := Types.Mutations(TerminalEncryptionContext := Some(newCustomEC));
    var testInput := Types.InitializeMutationInput(
      Identifier := id,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()),
      DoNotVersion := Some(true));
    var initializeOutput :- expect ksAdmin.InitializeMutation(testInput);

    // Validate BK
    var _ :- expect keyStore.GetActiveBranchKey(KeyStoreTypes.GetActiveBranchKeyInput(branchKeyIdentifier := id));

    if (!withIndex) {
      // Delete the Index
      var _ := CleanupItems.DeleteTypeWithFailure(id, Structure.MUTATION_INDEX_TYPE, ddbClient);
    }
    if (!withCommitment) {
      // Delete the Commitment
      var _ := CleanupItems.DeleteTypeWithFailure(id, Structure.MUTATION_COMMITMENT_TYPE, ddbClient);
    }
  }
}
