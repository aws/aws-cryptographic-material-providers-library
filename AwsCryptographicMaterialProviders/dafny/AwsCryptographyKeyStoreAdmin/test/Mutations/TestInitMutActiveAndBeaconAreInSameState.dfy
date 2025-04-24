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

  method {:test} TestSadCase()
  {
    // print " running";

    var ddbClient :- expect Fixtures.ProvideDDBClient(None);
    var kmsClient :- expect Fixtures.ProvideKMSClient(None);
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));

    var uuid :- expect UUID.GenerateUUID();
    var testId := sadCaseId + "-" + uuid;

    var kodaBytes :- expect UTF8.Encode("Koda");
    var isADogBytes :- expect UTF8.Encode("is a dog.");
    var originalEC := map[kodaBytes := isADogBytes];
    Fixtures.CreateHappyCaseId(id:=testId, versionCount:=1, customEC:=originalEC);

    // print testLogPrefix + " Created the legit test items with 2 versions! testId: " + testId + "\n";

    var _ :- expect AdminFixtures.AddAttributeWithoutLibrary(id := testId);

    // print testLogPrefix + " Violated the active and latest. testId: " + testId + "\n";

    var timestamp :- expect Time.GetCurrentTimeStamp();
    var newCustomEC: KeyStoreTypes.EncryptionContextString := map["Koda" := timestamp];
    var mutationsRequest := Types.Mutations(TerminalEncryptionContext := Some(newCustomEC));
    var initInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()),
      // TODO-HV-2-Version
      // DoNotVersion := Some(false));
      DoNotVersion := Some(true));
    var initializeOutput? := underTest.InitializeMutation(initInput);

    expect initializeOutput?.Failure?, "Initialize Mutation did not detect drifted Active & Beacon!";
    match initializeOutput?.error {
      case UnexpectedStateException(message) =>
        expect true;
      case _ => expect false, "Initialize Mutation should fail with Unexpected State Exception if Active & Beacon are different!";
    }
    // print testLogPrefix + " Initialize Mutation met expectations. Cleaning up\n";

    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
    // print "TestInitMutActiveAndBeaconAreInSameState.TestSadCase: ";
  }
}
