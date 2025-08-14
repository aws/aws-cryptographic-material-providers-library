// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../AwsCryptographyKeyStore/test/TestGetKeys.dfy"

// TODO-HV-2-M2 : remove HV-1 restriction for Mutations
module {:options "/functionSyntax:4" } TestAdminHV1Only {
  import KeyStore
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import ComAmazonawsKmsTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import opened Wrappers
  import opened Fixtures
  import UUID
  import CleanupItems
  import TestGetKeys

  const testMutateForTerminalHV1FailsCaseId := "dafny-initialize-mutation-terminal-hv-1-rejection"
  // TestMutateForTerminalHV1Fails removed -- not applicable

  // TODO-HV-2-M3 : Probably make this a happy test?
  const testVersionKeyEncountersHV2FailsCaseId := "dafny-version-key-encounters-hv-2-rejection"
  const logPrefixVersion := "\n" + testVersionKeyEncountersHV2FailsCaseId + " :: "
  /*
  method {:test} TestVersionKeyEncountersHV2Fails()
  {
    var uuid :- expect UUID.GenerateUUID();
    var testId := testVersionKeyEncountersHV2FailsCaseId + "-" + uuid;
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    Fixtures.CreateHappyCaseId(id:=testId);
    var _ :- expect Fixtures.AddAttributeWithoutLibrary(
      id:=testId,
      keyValue:=Fixtures.KeyValue(key:=Structure.HIERARCHY_VERSION, value:=Structure.HIERARCHY_VERSION_VALUE_2),
      alsoViolateBeacon? := true, ddbClient? := Some(ddbClient),
      kmsClient?:=Some(kmsClient), violateReservedAttribute:=true);

    // print logPrefixVersion + "re-wrote the item to be described as HV-2 even though it's not" + "\n";

    var versionInput := KeyStoreTypes.VersionKeyInput(
      branchKeyIdentifier := testId);
    var actualOutput := keyStore.VersionKey(versionInput);

    // print logPrefixVersion + "actualOutput :: ", actualOutput, "\n";

    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
    expect actualOutput.Failure?, "Should have failed VersionKey when HV-2 encountered by VersionKey.";
  }
  */
}
