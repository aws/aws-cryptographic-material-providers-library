// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Fixtures.dfy"

module {:options "/functionSyntax:4"} TestGetMutation {
  import UInt = Fixtures.UInt
  import Types = Fixtures.Types
  import UTF8 = Fixtures.UTF8
  import opened Wrappers
  import DefaultKeyStorageInterface
  import Fixtures
  import Structure
  import DDB = Com.Amazonaws.Dynamodb
  import KMS = Com.Amazonaws.Kms
  import KeyStore

  const TEST_NO_COMMITMENT_NO_INDEX_BKID := "test-storage-get-mutation-no-commitment-no-index"
  method {:test} TestNoCommitmentNoIndex()
  {
    var underTest :- expect Fixtures.DefaultStorage();
    var input := Types.GetMutationInput(
      Identifier := TEST_NO_COMMITMENT_NO_INDEX_BKID
    );
    var output? := underTest.GetMutation(input);
    expect output?.Success?, "GetMutation should have succeeded, but it failed!";
    var output := output?.value;
    expect output.MutationCommitment.None?, "There should be no Mutation Commitment";
    expect output.MutationIndex.None?, "There should be no Mutation Index";
  }
}
