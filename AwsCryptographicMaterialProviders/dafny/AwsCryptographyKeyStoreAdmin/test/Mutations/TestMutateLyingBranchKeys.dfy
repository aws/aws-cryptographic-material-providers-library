// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../AdminFixtures.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../../AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy"

module {:options "/functionSyntax:4" } TestMutateLyingBranchKey {
  import opened Wrappers
  import UTF8
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import KeyStoreErrorMessages
  import AdminFixtures
  import Fixtures
  import CleanupItems
  import TestLyingBranchKey

  // Test Case: Unexpected Encryption Context
  // The Branch Key's encryption context in DDB includes additional unmodeled EC: "unexpected-key:unexpected-value"
  // Expected Error: KMS.InvalidCiphertextException due to unexpected encryption context
  method {:test} TestHv2MutateForLyingBranchKeyUnexpectedEC() {
    var admin :- expect AdminFixtures.StaticAdmin();
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy();

    var terminalEC: KeyStoreTypes.EncryptionContextString := map["Koda" := "Is a dog."];
    var mutationsRequest := Types.Mutations(
      TerminalKmsArn := Some(Fixtures.postalHornKeyArn),
      TerminalHierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2),
      TerminalEncryptionContext := Some(terminalEC)
    );
    var initInput := Types.InitializeMutationInput(
      Identifier := Fixtures.hierarchyV2UnexpectedECId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()),
      DoNotVersion := Some(true));
    var initializeOutput := admin.InitializeMutation(initInput);
    expect initializeOutput.Failure?;
    expect initializeOutput.error.MutationFromException?;
  }

  // Test Case: Missing Encryption Context
  // The Branch Key's encryption context in DDB: "TamperedKey:TamperedValue"
  // Actual encryption context used with KMS Requests: "ExampleContextKey:ExampleContextValue"
  // Expected Error: KMS.InvalidCiphertextException due to encryption context mismatch
  method {:test} TestHv2MutateForLyingBranchKeyMissingPrefixedEC() {
    var admin :- expect AdminFixtures.StaticAdmin();
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy();

    var terminalEC: KeyStoreTypes.EncryptionContextString := map["Koda" := "Is a dog."];
    var mutationsRequest := Types.Mutations(
      TerminalKmsArn := Some(Fixtures.postalHornKeyArn),
      TerminalHierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2),
      TerminalEncryptionContext := Some(terminalEC)
    );
    var initInput := Types.InitializeMutationInput(
      Identifier := Fixtures.hierarchyV2MissingPrefixedECId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()),
      DoNotVersion := Some(true));
    var initializeOutput := admin.InitializeMutation(initInput);
    expect initializeOutput.Failure?;
    expect initializeOutput.error.MutationFromException?;
  }
}