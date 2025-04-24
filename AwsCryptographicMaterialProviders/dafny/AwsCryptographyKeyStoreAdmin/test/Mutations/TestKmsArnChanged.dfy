// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "../AdminFixtures.dfy"

// Tests that a Kms Arn only change:
// - Completes with paging
// - Changes the KmsArn on all Items
// - All items can be decrypted by KMS

module {:options "/functionSyntax:4" } TestKmsArnChanged {
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

  const happyCaseId := "test-mutate-kms-arn-only"
  const customEC := "aws-crypto-ec:Robbie"
  const kmsId: string := Fixtures.keyArn
  const physicalName: string := Fixtures.branchKeyStoreName
  const logicalName: string := Fixtures.logicalKeyStoreName
  const testLogPrefix := "\nTestKmsArnChanged :: TestHappyCase :: "

  method {:test} {:vcs_split_on_every_assert} TestHappyCase()
  {
    // print " running";

    // expect false; // disable test till other investigation is done
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();

    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var keyStoreOriginal :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var keyStoreTerminal :- expect Fixtures.DefaultKeyStore(
      kmsId:=Fixtures.postalHornKeyArn,
      ddbClient?:=Some(ddbClient),
      kmsClient?:=Some(kmsClient));

    var uuid :- expect UUID.GenerateUUID();
    var testId := happyCaseId + "-" + uuid;

    Fixtures.CreateHappyCaseId(id:=testId, versionCount:=1);

    // print testLogPrefix + " Created the test items with 2 versions! testId: " + testId + "\n";

    var timestamp :- expect Time.GetCurrentTimeStamp();
    var mutationsRequest := Types.Mutations(
      TerminalKmsArn := Some(Fixtures.postalHornKeyArn));
    var initInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()),
      // TODO-HV-2-Version
      // DoNotVersion := Some(false));
      DoNotVersion := Some(true));
    var initializeOutput :- expect underTest.InitializeMutation(initInput);
    var initializeToken := initializeOutput.MutationToken;

    // print testLogPrefix + " Initialized Mutation. M-Lock UUID " + initializeToken.UUID + "\n";

    var testInput := Types.ApplyMutationInput(
      MutationToken := initializeToken,
      PageSize := Some(24),
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()));
    var applyOutput :- expect underTest.ApplyMutation(testInput);

    // print testLogPrefix + " Applied Mutation w/ pageSize 24. testId: " + testId + "\n";
    expect applyOutput.MutationResult.CompleteMutation?, "Apply Mutation output should not continue!";

    var versionQuery := KeyStoreTypes.QueryForVersionsInput(
      Identifier := testId,
      PageSize := 24
    );
    var queryOut :- expect storage.QueryForVersions(versionQuery);
    var items := queryOut.Items;
    expect
      // TODO-HV-2-Version
      // |items| == 3,
      |items| == 2,
      "Test expects there to be 3 Decrypt Only items! Found: " + String.Base10Int2String(|items|);
    // print testLogPrefix + " Read the 3 Decrypt Only items! testId: " + testId + "\n";

    var itemIndex := 0;
    var inputV: KeyStoreTypes.GetBranchKeyVersionInput;
    while itemIndex < |items|
    {
      var item := items[itemIndex];
      expect
        item.Type.HierarchicalSymmetricVersion?,
        "Query for Decrypt Only returned a non-Decrypt Only!";
      var versionUUID := item.Type.HierarchicalSymmetricVersion.Version;
      expect "type" in item.EncryptionContext, "Decrypt Only item is missing 'type' from EC!!";
      expect
        item.KmsArn == Fixtures.postalHornKeyArn,
        "KmsArn of Item is incorrect. Item: " + versionUUID;
      inputV := KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := testId,
        branchKeyVersion := versionUUID
      );
      var _ :- expect keyStoreTerminal.GetBranchKeyVersion(inputV);

      // print testLogPrefix + " Validated Decrypt Only and tried to clean it up: " + item.EncryptionContext["type"] + "\n";
      itemIndex := 1 + itemIndex;
    }

    var _ :- expect keyStoreTerminal.GetActiveBranchKey(KeyStoreTypes.GetActiveBranchKeyInput(branchKeyIdentifier := testId));
    // print testLogPrefix + " Active Validated with KMS/KeyStore: " + testId + "\n";

    var _ :- expect keyStoreTerminal.GetBeaconKey(KeyStoreTypes.GetBeaconKeyInput(branchKeyIdentifier := testId));
    // print testLogPrefix + " Beacon Validated with KMS/KeyStore: " + testId + "\n";
    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);

    // print "TestKmsArnChanged.TestHappyCase: ";
  }
}
