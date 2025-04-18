// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "AdminFixtures.dfy"

/** Tests the logic in Mutation State Structures */
module {:options "/functionSyntax:4" } TestMutationStateStructures {
  import opened Wrappers
  import UUID
  import Fixtures
  import Types = AwsCryptographyKeyStoreAdminTypes
  import AdminFixtures
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb

  // Test a pre-HV-2 Mutation Commitment Deserializes Correctly
  method {:test} TestPreHV2DeserializeMutation()
  {
    var underTest :- expect AdminFixtures.DefaultAdmin();
    var request := Types.DescribeMutationInput(
      Identifier:=AdminFixtures.STATIC_PRE_HV2_MUTATION_WITH_SYSTEM_KEY
    );
    var response := underTest.DescribeMutation(request);
    expect response.Success?, "";
  }
}
