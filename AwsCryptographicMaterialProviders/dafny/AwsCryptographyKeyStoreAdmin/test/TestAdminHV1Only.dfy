// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../src/KeyStoreAdminErrorMessages.dfy"
include "../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../AwsCryptographyKeyStore/test/TestGetKeys.dfy"
include "AdminFixtures.dfy"

// TODO-HV-2-M2 : remove HV-1 restriction for Mutations
module {:options "/functionSyntax:4" } TestAdminHV1Only {
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreAdmin
  import KeyStore
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import ComAmazonawsKmsTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import DefaultKeyStorageInterface
  import opened Wrappers
  import opened Fixtures
  import UUID
  import CleanupItems
  import AdminFixtures
  import TestGetKeys
  import KeyStoreAdminErrorMessages

  const testMutateForTerminalHV1FailsCaseId := "dafny-initialize-mutation-terminal-hv-1-rejection"
  method {:test} TestMutateForTerminalHV1Fails()
  {
    var uuid :- expect UUID.GenerateUUID();
    var testId := testMutateForTerminalHV1FailsCaseId + "-" + uuid;
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var strategy :- expect AdminFixtures.DecryptEncrypKeyManagerStrategy(
      decryptKmsClient?:=Some(kmsClient),
      encryptKmsClient?:=Some(kmsClient)
    );
    var systemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage());
    AdminFixtures.CreateHappyCaseId(id := testId, hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2, admin? := Some(underTest));
    var mutationsRequest := Types.Mutations(
      TerminalKmsArn := Some(Fixtures.postalHornKeyArn),
      TerminalHierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v1)
    );
    var initInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := systemKey,
      DoNotVersion := Some(true));
    var initializeOutput := underTest.InitializeMutation(initInput);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
    expect initializeOutput.Failure?, "Should have failed to InitializeMutation with terminal HV-1.";
    expect initializeOutput.error == Types.Error.UnsupportedFeatureException(message:=KeyStoreAdminErrorMessages.UNSUPPORTED_DOWNGRADE_HV);
  }

  // TODO-HV-2-M3 : Probably make this a happy test?
  const testMutateInitEncountersHV2FailsCaseId := "dafny-initialize-mutation-encounters-hv-2-rejection"
  const logPrefix := "\n" + testMutateInitEncountersHV2FailsCaseId + " :: "
  method {:test} TestMutateInitEncountersHV2FailsCaseId()
  {
    var uuid :- expect UUID.GenerateUUID();
    var testId := testMutateInitEncountersHV2FailsCaseId + "-" + uuid;
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var systemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage());
    Fixtures.CreateHappyCaseId(id:=testId);
    var _ :- expect AdminFixtures.AddAttributeWithoutLibrary(
      id:=testId,
      keyValue:=AdminFixtures.KeyValue(key:=Structure.HIERARCHY_VERSION, value:=Structure.HIERARCHY_VERSION_VALUE_2),
      alsoViolateBeacon? := true, ddbClient? := Some(ddbClient),
      kmsClient?:=Some(kmsClient), violateReservedAttribute:=true);
    var mutationsRequest := Types.Mutations(TerminalKmsArn := Some(Fixtures.postalHornKeyArn));
    var initInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := systemKey,
      DoNotVersion := Some(true));
    var initializeOutput := underTest.InitializeMutation(initInput);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
    expect initializeOutput.Failure?, "Should have failed InitializeMutation when HV-2 encountered by InitMutation.";
  }

  // TODO-HV-2-M3 : Probably make this a happy test?
  const testVersionKeyEncountersHV2FailsCaseId := "dafny-version-key-encounters-hv-2-rejection"
  const logPrefixVersion := "\n" + testVersionKeyEncountersHV2FailsCaseId + " :: "
  method {:test} TestVersionKeyEncountersHV2Fails()
  {
    var uuid :- expect UUID.GenerateUUID();
    var testId := testVersionKeyEncountersHV2FailsCaseId + "-" + uuid;
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var systemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage());
    Fixtures.CreateHappyCaseId(id:=testId);
    var _ :- expect AdminFixtures.AddAttributeWithoutLibrary(
      id:=testId,
      keyValue:=AdminFixtures.KeyValue(key:=Structure.HIERARCHY_VERSION, value:=Structure.HIERARCHY_VERSION_VALUE_2),
      alsoViolateBeacon? := true, ddbClient? := Some(ddbClient),
      kmsClient?:=Some(kmsClient), violateReservedAttribute:=true);

    // print logPrefixVersion + "re-wrote the item to be described as HV-2 even though it's not" + "\n";

    var versionInput := Types.VersionKeyInput(
      Identifier := testId,
      KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
      Strategy := Some(strategy));
    var actualOutput := underTest.VersionKey(versionInput);

    // print logPrefixVersion + "actualOutput :: ", actualOutput, "\n";

    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
    expect actualOutput.Failure?, "Should have failed VersionKey when HV-2 encountered by VersionKey.";
  }
}
