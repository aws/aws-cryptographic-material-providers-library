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

  method {:test} {:vcs_split_on_every_assert} TestInitializeMutationFailsWithNonUniqueBranchKeyContext() {
    // Commented code that adds {"Robbie": "Is a dog."} to the dynamodb item
    // This code will create a branch key and make changes so that branch key item contains non unique branch key context key
    //
    // var ddbClient :- expect Fixtures.ProvideDDBClient();
    // var kmsClient :- expect Fixtures.ProvideKMSClient();
    // var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);
    // var keyStoreConfig := Types.KeyStoreConfig(
    //   id := None,
    //   kmsConfiguration := kmsConfig,
    //   logicalKeyStoreName := logicalKeyStoreName,
    //   storage := Some(
    //     Types.ddb(
    //       Types.DynamoDBTable(
    //         ddbTableName := branchKeyStoreName,
    //         ddbClient := Some(ddbClient)
    //       )))
    // );
    // var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
    // var ECkey := "Robbie"
    // var ECvalue := "Is a dog."
    // var encryptionContext :- expect EncodeEncryptionContext(map[
    //                                                           ECkey := ECvalue
    //                                                         ]);
    // var branchKeyId :- expect keyStore.CreateKey(Types.CreateKeyInput(
    //                                                branchKeyIdentifier := Some("DO-NOT-EDIT-Branch-Key-For-HasUniqueTransformedKeys-Check"),
    //                                                encryptionContext := Some(encryptionContext)
    //                                              ));
    // var _ :- expect AdminFixtures.AddAttributeWithoutLibrary(
    //   id:="DO-NOT-EDIT-Branch-Key-For-HasUniqueTransformedKeys-Check",
    //   keyValue:=AdminFixtures.KeyValue(key:=ECkey, value:=ECvalue),
    //   alsoViolateBeacon? := true, ddbClient? := Some(ddbClient),
    //   kmsClient?:=Some(kmsClient), violateReservedAttribute:=true);

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
    // TODO-HV2-M2: Uncomment these test. Currently, Failure(Types.KeyStoreAdminException(message :="At this time, Mutations do not support mutations to hierarchy-version-2.")) mask the UnexpectedStateException for NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS
    // expect initializeOutput.error.KeyStoreAdminException?, "Should have KeyStoreAdminException";
    // expect initializeOutput.error.message == KeyStoreErrorMessages.NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS, "Incorrect error message. Should have had `KeyStoreErrorMessages.NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS`";
  }
}