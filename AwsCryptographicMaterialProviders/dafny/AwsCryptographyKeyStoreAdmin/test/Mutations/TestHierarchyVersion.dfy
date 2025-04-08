// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../AdminFixtures.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"

module {:options "/functionSyntax:4" } TestHierarchyVersion {
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import KeyStoreErrorMessages
  import AdminFixtures
  import Fixtures
  import opened Wrappers

  method {:test} TestInitializeMutationFailsWithNonUniqueBranchKeyContext() {

    var testId := "DO-NOT-EDIT-Branch-Key-For-HasUniqueTransformedKeys-Check";

    // Commented code that adds {"Robbie": "Is a dog."} to the dynamodb item "DO-NOT-EDIT-Branch-Key-For-HasUniqueTransformedKeys-Check" in table KeyStoreDdbTable
    // This code will create a branch key and make changes so that branch key item contains non unique branch key context key
    //
    // Fixtures.CreateHappyCaseId(id:=testId);
    // var _ :- expect AdminFixtures.AddAttributeWithoutLibrary(
    //   id:=testId,
    //   keyValue:=AdminFixtures.KeyValue(key:=ECkey, value:=ECvalue),
    //   alsoViolateBeacon? := true, ddbClient? := Some(ddbClient),
    //   kmsClient?:=Some(kmsClient), violateReservedAttribute:=true);
    
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

    // TODO-HV-2-M2: Uncomment these test. Currently, Failure(Types.KeyStoreAdminException(message :="At this time, Mutations do not support mutations to hierarchy-version-2.")) mask the UnexpectedStateException for NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS
    expect initializeOutput.error.KeyStoreAdminException?, "Should have KeyStoreAdminException";
    expect initializeOutput.error.message == KeyStoreErrorMessages.NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS, "Incorrect error message. Should have had `KeyStoreErrorMessages.NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS`";
  }
}