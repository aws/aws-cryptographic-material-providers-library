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
  import KeyStoreAdminErrorMessages
  import AdminFixtures
  import Fixtures
  import CleanupItems
  import UUID
  import Time
  import Structure

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
    expect initializeOutput.error.message == KeyStoreErrorMessages.FOUND_EC_WITHOUT_PREFIX, "Incorrect error message. Should have had `KeyStoreErrorMessages.FOUND_EC_WITHOUT_PREFIX`";
  }

  method {:test} TestNonUniqueTerminalAndInferredECKeys() {

    var testId := "DO-NOT-EDIT-Branch-Key-For-TestNonUniqueTerminalAndInferredECKeys-Check";
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();

    // Commented code creates a branch key and adds {"Koda": "Is a dog."}
    // to the branch key item outside of the library's operations.
    // Adding {"Koda": "Is a dog."} will NOT create a non unique branch key context
    // and the EC will not be prefixed since its done outside our library

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
    expect initializeOutput.error.message == KeyStoreAdminErrorMessages.FOUND_EC_WITHOUT_PREFIX, "Incorrect error message. Should have had `KeyStoreAdminErrorMessages.FOUND_EC_WITHOUT_PREFIX`";
  }
}