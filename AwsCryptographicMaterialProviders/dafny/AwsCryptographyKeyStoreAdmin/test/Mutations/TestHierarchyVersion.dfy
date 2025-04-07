// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../AdminFixtures.dfy"
  // include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
  // include "../../../AwsCryptographyKeyStore/test/TestGetKeys.dfy"
  // include "../../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"

module {:options "/functionSyntax:4" } TestHierarchyVersion {
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import AdminFixtures
  import Fixtures
  import opened Wrappers

  method {:test} {:vcs_split_on_every_assert} TestHasUniqueTransformedKeys() {
    var testId := "DO-NOT-EDIT-Branch-Key-For-HasUniqueTransformedKeys-Check";
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var underTest :- expect AdminFixtures.DefaultAdmin();
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
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
  }
}