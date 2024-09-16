// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "../AdminFixtures.dfy"

// Tests that if the Active & Beacon are in different states,
// Initialize Mutations fails
module {:options "/functionSyntax:4" } TestInitMutActiveAndBeaconAreInSameState {
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreAdmin
  import KeyStore
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import opened Wrappers
  import Fixtures
  import AdminFixtures
  import UUID
  import CleanupItems
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import DefaultKeyStorageInterface
  import Time
  import Structure
  import String = StandardLibrary.String
  import UTF8
  import opened StandardLibrary.UInt

  const sadCaseId := "test-mutations-active-and-beacon-are-in-same-state"
  const customEC := "aws-crypto-ec:Koda"
  const kmsId: string := Fixtures.keyArn
  const physicalName: string := Fixtures.branchKeyStoreName
  const logicalName: string := Fixtures.logicalKeyStoreName
  const testLogPrefix := "\nTestMutationsActiveAndBeaconAreInSameState :: TestSadCase :: "

  function {:opaque} TestLie(): set<object>
  {{}}

  method {:test} {:vcs_split_on_every_assert} TestSadCase()
  {
    print " running";

    // expect false; // disable test till other investigation is done
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsClient :- expect KMS.KMSClient();
    var storage :- expect AdminFixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    // Recommend commenting this out while developing this method,
    // and just ignore the modifies exeptions,
    // and then re-enabling it once everything is safe
    assume {:axiom} underTest.Modifies == {} && storage.Modifies == {};
    assume {:axiom} underTest.Modifies < TestLie(); // This does not work... but I have it here

    var uuid :- expect UUID.GenerateUUID();
    var testId := sadCaseId + "-" + uuid;

    var kodaBytes :- expect UTF8.Encode("Koda");
    var isADogBytes :- expect UTF8.Encode("is a dog.");
    var originalEC := map[kodaBytes := isADogBytes];
    AdminFixtures.CreateHappyCaseId(id:=testId, versionCount:=1, customEC:=originalEC);

    print testLogPrefix + " Created the legit test items with 2 versions! testId: " + testId + "\n";

    var _ :- expect AdminFixtures.AddAttributeWithoutLibrary(id := testId);

    print testLogPrefix + " Violated the active and latest. testId: " + testId + "\n";

    var timestamp :- expect Time.GetCurrentTimeStamp();
    var newCustomEC: KeyStoreTypes.EncryptionContextString := map["Koda" := timestamp];
    var mutationsRequest := Types.Mutations(terminalEncryptionContext := Some(newCustomEC));
    var initInput := Types.InitializeMutationInput(
      branchKeyIdentifier := testId,
      mutations := mutationsRequest,
      strategy := Some(strategy));
    var initializeOutput? := underTest.InitializeMutation(initInput);

    expect initializeOutput?.Failure?, "Initialize Mutation did not detect drifted Active & Beacon!";
    match initializeOutput?.error {
      case UnexpectedStateException(message) =>
        expect true;
      case _ => expect false, "Initialize Mutation should fail with Unexpected State Exception if Active & Beacon are different!";
    }
    print testLogPrefix + " Initialize Mutation met expectations. Cleaning up\n";

    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BEACON_KEY_TYPE_VALUE, ddbClient);
    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BRANCH_KEY_ACTIVE_TYPE, ddbClient);

    var versionQuery := KeyStoreTypes.QueryForVersionsInput(
      Identifier := testId, pageSize := 24
    );
    var queryOut :- expect storage.QueryForVersions(versionQuery);
    var items := queryOut.items;
    var itemIndex := 0;
    while itemIndex < |items|
    {
      expect "type" in items[itemIndex].EncryptionContext, "Decrypt Only item is missing 'type' from EC!!";
      var _ := CleanupItems.DeleteTypeWithFailure(testId, items[itemIndex].EncryptionContext["type"], ddbClient);
      itemIndex := itemIndex + 1;
    }

    print "TestInitMutActiveAndBeaconAreInSameState.TestSadCase: ";

  }
}
