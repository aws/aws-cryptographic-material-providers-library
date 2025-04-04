// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../AwsCryptographyKeyStore/test/TestGetKeys.dfy"
include "../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "AdminFixtures.dfy"

// TODO-HV-2-M1 : remove HV-1 restriction for CreateKey
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

  const happyCaseId := "test-create-key-hv-2-happy-case"

  method {:test} TestCreateKeyForHV2HappyCase()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));

    var input := Types.CreateKeyInput(
      Identifier := None,
      EncryptionContext := None,
      KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
      Strategy := Some(strategy),
      HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
    );

    var createKeyOutput? :- expect underTest.CreateKey(input);
    expect createKeyOutput?.HierarchyVersion == KeyStoreTypes.HierarchyVersion.v2;

    // Get branch key items from storage
    TestGetKeys.VerifyGetKeys(
      identifier := createKeyOutput?.Identifier,
      keyStore := keyStore,
      storage := storage
    );

    // Since this process uses a read DDB table,
    // the number of records will forever increase.
    // To avoid this, remove the items.
    var _ := CleanupItems.DeleteBranchKey(Identifier:=createKeyOutput?.Identifier, ddbClient:=ddbClient);
  }

  method {:test} TestCreateKeyForHV2CreateOptions() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));

    // Create key with Custom EC & Branch Key Identifier
    var uuid :- expect UUID.GenerateUUID();
    var branchKeyId := happyCaseId + "-" + uuid;

    var customEC := map[UTF8.EncodeAscii("Koda") := UTF8.EncodeAscii("Is a dog.")];

    var input := Types.CreateKeyInput(
      Identifier := Some(branchKeyId),
      EncryptionContext := Some(customEC),
      KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
      Strategy := Some(strategy),
      HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
    );

    var createKeyOutput? :- expect underTest.CreateKey(input);
    expect branchKeyId == createKeyOutput?.Identifier;
    expect createKeyOutput?.HierarchyVersion == KeyStoreTypes.HierarchyVersion.v2;

    // Get branch key items from storage
    TestGetKeys.VerifyGetKeys(
      identifier := branchKeyId,
      keyStore := keyStore,
      storage := storage
    );

    // Since this process uses a read DDB table,
    // the number of records will forever increase.
    // To avoid this, remove the items.
    var _ := CleanupItems.DeleteBranchKey(Identifier:=branchKeyId, ddbClient:=ddbClient);
  }

  // TODO-HV-2-M2?: Document that BKSA ONLY calls KMS/DDB for the region of the supplied clients.
  // or Ensure BKSA has similar behavior as BKS in terms of MRK region.
  /*
  method {:test} TestCreateMRKForHV2()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));

    // Create key with Custom EC & Branch Key Identifier
    var uuid :- expect UUID.GenerateUUID();
    var branchKeyIdWest := happyCaseId + "-" + WestBranchKey + "-" + uuid;
    var branchKeyIdEast := happyCaseId + "-" + EastBranchKey + "-" + uuid;

    var customEC := map[UTF8.EncodeAscii("Koda") := UTF8.EncodeAscii("Is a dog.")];

    var westOutput? :- expect underTest.CreateKey(Types.CreateKeyInput(
                                                    Identifier := Some(branchKeyIdWest),
                                                    EncryptionContext := Some(customEC),
                                                    KmsArn := Types.KmsSymmetricKeyArn.KmsMRKeyArn(MrkArnWest),
                                                    Strategy := Some(strategy),
                                                    HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
                                                  ));
    expect westOutput?.Identifier == branchKeyIdWest;
    expect westOutput?.HierarchyVersion == KeyStoreTypes.HierarchyVersion.v2;
    print branchKeyIdWest + "\n";

    var eastOutput? :- expect underTest.CreateKey(Types.CreateKeyInput(
                                                    Identifier := Some(branchKeyIdEast),
                                                    EncryptionContext := Some(customEC),
                                                    KmsArn := Types.KmsSymmetricKeyArn.KmsMRKeyArn(MrkArnEast),
                                                    Strategy := Some(strategy),
                                                    HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
                                                  ));
    expect eastOutput?.Identifier == branchKeyIdEast;
    expect eastOutput?.HierarchyVersion == KeyStoreTypes.HierarchyVersion.v2;
    print branchKeyIdEast + "\n";
  }
  */

  // TODO-HV-2-M2 : Probably make this a happy test?
  const testMutateForHV2FailsCaseId := "dafny-initialize-mutation-hv-2-rejection"
  method {:test} TestMutateForHV2Fails()
  {
    var uuid :- expect UUID.GenerateUUID();
    var testId := testMutateForHV2FailsCaseId + "-" + uuid;
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var underTest :- expect AdminFixtures.DefaultAdmin();
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var systemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage());
    Fixtures.CreateHappyCaseId(id:=testId);

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
    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
    expect initializeOutput.Failure?, "Should have failed to InitializeMutation HV-2.";
  }

  // TODO-HV-2-M2 : Probably make this a happy test?
  const testMutateForHV1WithAwsKmsSimpleFailsCaseId := "dafny-initialize-mutation-hv-1-simpleKms-rejection"
  method {:test} TestMutateForHV1WithAwsKmsSimpleFails()
  {
    var uuid :- expect UUID.GenerateUUID();
    var testId := testMutateForHV1WithAwsKmsSimpleFailsCaseId + "-" + uuid;
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var underTest :- expect AdminFixtures.DefaultAdmin();
    var simpleStrategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var systemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage());
    Fixtures.CreateHappyCaseId(id:=testId);

    var mutationsRequest := Types.Mutations(
      TerminalKmsArn := Some(Fixtures.postalHornKeyArn),
      TerminalHierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v1)
    );
    var initInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(simpleStrategy),
      SystemKey := systemKey,
      DoNotVersion := Some(true));
    var initializeOutput := underTest.InitializeMutation(initInput);
    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
    expect initializeOutput.Failure?, "Should have failed to InitializeMutation for HV-1 with Simple.";
  }

  // TODO-HV-2-M2 : Probably make this a happy test?
  const testMutateInitEncountersHV2FailsCaseId := "dafny-initialize-mutation-encounters-hv-2-rejection"
  const logPrefix := "\n" + testMutateInitEncountersHV2FailsCaseId + " :: "
  method {:test} TestMutateInitEncountersHV2FailsCaseId()
  {
    var uuid :- expect UUID.GenerateUUID();
    var testId := testMutateInitEncountersHV2FailsCaseId + "-" + uuid;
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var underTest :- expect AdminFixtures.DefaultAdmin();
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var systemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage());
    Fixtures.CreateHappyCaseId(id:=testId);
    var _ :- expect AdminFixtures.AddAttributeWithoutLibrary(
      id:=testId,
      keyValue:=AdminFixtures.KeyValue(key:=Structure.HIERARCHY_VERSION, value:=Structure.HIERARCHY_VERSION_VALUE_2),
      alsoViolateBeacon? := true, ddbClient? := Some(ddbClient),
      kmsClient?:=Some(kmsClient), violateReservedAttribute:=true);

    print logPrefix + "re-wrote the item to be described as HV-2 even though it's not" + "\n";

    var mutationsRequest := Types.Mutations(TerminalKmsArn := Some(Fixtures.postalHornKeyArn));
    var initInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := systemKey,
      DoNotVersion := Some(true));
    var initializeOutput := underTest.InitializeMutation(initInput);

    print logPrefix + "initializeOutput :: ", initializeOutput, "\n";

    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
    expect initializeOutput.Failure?, "Should have failed InitializeMutation when HV-2 encountered by InitMutation.";
  }

  // TODO-HV-2-M2 : Probably make this a happy test?
  const testVersionKeyEncountersHV2FailsCaseId := "dafny-version-key-encounters-hv-2-rejection"
  const logPrefixVersion := "\n" + testVersionKeyEncountersHV2FailsCaseId + " :: "
  method {:test} TestVersionKeyEncountersHV2Fails()
  {
    var uuid :- expect UUID.GenerateUUID();
    var testId := testVersionKeyEncountersHV2FailsCaseId + "-" + uuid;
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var underTest :- expect AdminFixtures.DefaultAdmin();
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var systemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage());
    Fixtures.CreateHappyCaseId(id:=testId);
    var _ :- expect AdminFixtures.AddAttributeWithoutLibrary(
      id:=testId,
      keyValue:=AdminFixtures.KeyValue(key:=Structure.HIERARCHY_VERSION, value:=Structure.HIERARCHY_VERSION_VALUE_2),
      alsoViolateBeacon? := true, ddbClient? := Some(ddbClient),
      kmsClient?:=Some(kmsClient), violateReservedAttribute:=true);

    print logPrefixVersion + "re-wrote the item to be described as HV-2 even though it's not" + "\n";

    var versionInput := Types.VersionKeyInput(
      Identifier := testId,
      KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
      Strategy := Some(strategy));
    var actualOutput := underTest.VersionKey(versionInput);

    print logPrefixVersion + "actualOutput :: ", actualOutput, "\n";

    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
    expect actualOutput.Failure?, "Should have failed VersionKey when HV-2 encountered by VersionKey.";
  }
}
