// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "../AdminFixtures.dfy"

// Tests for T-27 & T-18
//  1. if there is a mutation lock, the Active Version has already been updated.
//  2.  you are able to successfully version b-keys while an M-Lock exists
// This Test will:
// - Create a Branch Key and Version it 0 times
// - Look up the current Active Version as A1
// - Initialize a Mutation of that Branch Key
// - Look up the current Active Version as A2 & Mutation Lock
// - Assert the current Active Version is:
// -- In the Terminal State
// -- Created at the same time as Mutation Lock
// -- Not the same as previous Active A1
// - Then, it will Version the Branch Key
// - Look up the current Active Version as A3 & Mutation Lock
// - Assert that:
// -- The Active Version A3 is different than A2
// -- A3 & the Mutation Lock have different timestamps, and A3 is younger

// Finally, this test will delete all created items.

module {:options "/functionSyntax:4" } TestThreat27 {
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

  const happyCaseId := "test-initialize-versions-branch-key"
  const customEC := "aws-crypto-ec:Robbie"
  const kmsId: string := Fixtures.keyArn
  const physicalName: string := Fixtures.branchKeyStoreName
  const logicalName: string := Fixtures.logicalKeyStoreName

  method {:test} TestHappyCase()
  {
    print " running";

    // expect false;
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));

    var uuid :- expect UUID.GenerateUUID();
    var testId := happyCaseId + "-" + uuid;

    Fixtures.CreateHappyCaseId(id:=testId, versionCount:=0);
    print "\nTestThreat27 :: TestHappyCase :: Created the test items! testId: "
          + testId  +  "\n";
    var activeOneInput := KeyStoreTypes.GetEncryptedActiveBranchKeyInput(Identifier:=testId);
    var activeOne? :- expect storage.GetEncryptedActiveBranchKey(activeOneInput);
    expect "version" in activeOne?.Item.EncryptionContext;
    expect customEC in activeOne?.Item.EncryptionContext;
    // var activeOne := activeOne?.Item.EncryptionContext["version"];
    expect activeOne?.Item.Type.ActiveHierarchicalSymmetricVersion?;
    var activeOne := activeOne?.Item.Type.ActiveHierarchicalSymmetricVersion.Version;
    var robbieOne := activeOne?.Item.EncryptionContext["aws-crypto-ec:Robbie"];
    print "\nTestThreat27 :: TestHappyCase :: Established ActiveOne: " + activeOne + "\n";

    var timestamp :- expect Time.GetCurrentTimeStamp();
    var newCustomEC: KeyStoreTypes.EncryptionContextString := map["Robbie" := timestamp];
    var mutationsRequest := Types.Mutations(TerminalEncryptionContext := Some(newCustomEC));
    var testInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := Some(Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage())),
      DoNotVersion := Some(false));
    var initializeOutput :- expect underTest.InitializeMutation(testInput);

    print "\nTestThreat27 :: TestHappyCase :: Initialized Mutation: " + activeOne + "\n";

    var activeTwoInput := KeyStoreTypes.GetEncryptedActiveBranchKeyInput(Identifier:=testId);
    var activeTwo? :- expect storage.GetEncryptedActiveBranchKey(activeTwoInput);
    expect "version" in activeTwo?.Item.EncryptionContext;
    expect "aws-crypto-ec:Robbie" in activeTwo?.Item.EncryptionContext, "Custom EC is missing from Mutated Item";
    // var activeTwo := activeTwo?.Item.EncryptionContext["version"];
    expect activeTwo?.Item.Type.ActiveHierarchicalSymmetricVersion?;
    var activeTwo := activeTwo?.Item.Type.ActiveHierarchicalSymmetricVersion.Version;
    var robbieTwo := activeTwo?.Item.EncryptionContext["aws-crypto-ec:Robbie"];

    expect activeOne != activeTwo, "Initialize Mutation FAILED to Write New Active Branch Key";
    expect robbieTwo == timestamp, "Initialize Mutation FAILED to Mutate Custom EC";

    print "\nTestThreat27 :: TestHappyCase :: Verified activeTwo was created in Terminal: " + activeTwo + "\n";

    var versionTwoInput := KeyStoreTypes.GetEncryptedBranchKeyVersionInput(Identifier:=testId, Version:=activeTwo);
    var versionTwo? :- expect storage.GetEncryptedBranchKeyVersion(versionTwoInput);
    expect Structure.TYPE_FIELD in versionTwo?.Item.EncryptionContext;
    var versionTwo := versionTwo?.Item.EncryptionContext[Structure.TYPE_FIELD];
    expect customEC in versionTwo?.Item.EncryptionContext;
    expect timestamp == versionTwo?.Item.EncryptionContext[customEC], "Initialize Mutation Created Version in wrong state!";
    print "\nTestThreat27 :: TestHappyCase :: Verified versionTwo was created in Terminal: " + versionTwo + "\n";

    // Validate Beacon Key
    var beaconPostMutInput := KeyStoreTypes.GetEncryptedBeaconKeyInput(Identifier:=testId);
    var beaconPostMut? :-expect storage.GetEncryptedBeaconKey(beaconPostMutInput);
    expect Structure.TYPE_FIELD in beaconPostMut?.Item.EncryptionContext;
    var beaconPostMut := beaconPostMut?.Item.EncryptionContext[Structure.TYPE_FIELD];
    expect customEC in beaconPostMut?.Item.EncryptionContext;
    expect timestamp == beaconPostMut?.Item.EncryptionContext[customEC], "Initialize Mutation Mutated Beacon to wrong state!";
    print "\nTestThreat27 :: TestHappyCase :: Verified Beacon was Mutated to Terminal: " + beaconPostMut + "\n";

    var inputV := KeyStoreTypes.VersionKeyInput(
      branchKeyIdentifier := testId
    );
    var _ :- expect keyStore.VersionKey(inputV);

    print "\nTestThreat27 :: TestHappyCase :: Versioned ActiveTwo. testId: " + testId + "\n";

    var activeThreeInput := KeyStoreTypes.GetEncryptedActiveBranchKeyInput(Identifier:=testId);
    var activeThree? :- expect storage.GetEncryptedActiveBranchKey(activeThreeInput);
    expect "version" in activeThree?.Item.EncryptionContext;
    expect "aws-crypto-ec:Robbie" in activeThree?.Item.EncryptionContext;
    // var activeThree := activeThree?.Item.EncryptionContext["version"];
    expect activeThree?.Item.Type.ActiveHierarchicalSymmetricVersion?;
    var activeThree := activeThree?.Item.Type.ActiveHierarchicalSymmetricVersion.Version;
    var robbieThree := activeThree?.Item.EncryptionContext["aws-crypto-ec:Robbie"];

    expect robbieThree == timestamp, "Version made ACTIVE in wrong state!";

    var versionThreeInput := KeyStoreTypes.GetEncryptedBranchKeyVersionInput(Identifier:=testId, Version:=activeThree);
    var versionThree? :- expect storage.GetEncryptedBranchKeyVersion(versionThreeInput);
    expect customEC in versionThree?.Item.EncryptionContext;
    expect timestamp == versionThree?.Item.EncryptionContext[customEC], "Version made DECRYPT_ONLY in wrong state!";

    print "\nTestThreat27 :: TestHappyCase :: All expects passed! Trying to clean up testId: " + testId + "\n";

    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BRANCH_KEY_ACTIVE_TYPE, ddbClient);
    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BEACON_KEY_TYPE_VALUE, ddbClient);
    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.MUTATION_COMMITMENT_TYPE, ddbClient);
    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.MUTATION_INDEX_TYPE, ddbClient);
    print "\nTestThreat27 :: TestHappyCase :: Delete Version for activeOne: " + activeOne + "\n";
    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BRANCH_KEY_TYPE_PREFIX + activeOne, ddbClient);
    print "\nTestThreat27 :: TestHappyCase :: Delete Version for activeTwo: " + activeTwo + "\n";
    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BRANCH_KEY_TYPE_PREFIX + activeTwo, ddbClient);
    print "\nTestThreat27 :: TestHappyCase :: Delete Version for activeThree: " + activeThree + "\n";
    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BRANCH_KEY_TYPE_PREFIX + activeThree, ddbClient);

    print "TestThreat27.TestHappyCase: ";
  }
}
