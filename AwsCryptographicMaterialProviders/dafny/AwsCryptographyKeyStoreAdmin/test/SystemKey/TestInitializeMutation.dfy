// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../AdminFixtures.dfy"

// Tests that Initialize Mutation with a System Key of Trust Storage:
// - Will FAKE Sign Commitment and Index
// - Will FAKE Validate Commitment and Index on second call
// - Will FAIL Validate if ciphertext blob is not "trustStorage"

// Tests that Initialize Mutation with a System Key of KMS:
// - Will Sign Commitment and Index
// - Will Validate Commitment and Index on second call

module {:options "/functionSyntax:4" } TestSystemKey.TestInitializeMutation {
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

  const trustStorageHPrefix := "\nTestSystemKey.TestInitializeMutation :: TrustStorageHappyCase :: "
  const trustStorageHCaseId := "dafny-system-key-test-initialize-mutation-trust-storage-happy-case"
  method {:test} TrustStorageHappyCase()
  {
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var underTest :- expect AdminFixtures.DefaultAdmin();
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var systemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage());
    var uuid :- expect UUID.GenerateUUID();
    var testId := trustStorageHCaseId + "-" + uuid;
    Fixtures.CreateHappyCaseId(id:=testId);

    var mutationsRequest := Types.Mutations(TerminalKmsArn := Some(Fixtures.postalHornKeyArn));
    var initInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := systemKey,
      // TODO-HV-2-Version
      // DoNotVersion := Some(false));
      DoNotVersion := Some(true));
    var initializeOutput :- expect underTest.InitializeMutation(initInput);
    var initializeToken := initializeOutput.MutationToken;

    var initializeAgainOutput :- expect underTest.InitializeMutation(initInput);
    expect initializeToken == initializeAgainOutput.MutationToken;

    var kmsSystemKey := Types.SystemKey.kmsSymmetricEncryption(
      kmsSymmetricEncryption := Types.KmsSymmetricEncryption(
        KmsArn := Fixtures.publicKeyArn,
        AwsKms := KeyStoreTypes.AwsKms(
          grantTokens := None,
          kmsClient := Some(kmsClient))));

    var sadInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := kmsSystemKey,
      // TODO-HV-2-Version
      // DoNotVersion := Some(false));
      DoNotVersion := Some(true));

    var sadOutput := underTest.InitializeMutation(sadInput);
    // TODO Restore this last expectation.
    expect sadOutput.Failure?, "Should have failed to initialize.";

    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
  }

  const kmsSymEncHPrefix := "\nTestSystemKey.TestInitializeMutation :: KmsSymEncHappyCase :: "
  const kmsSymEncHCaseId := "dafny-system-key-test-initialize-mutation-kmsSymEnc-happy-case"
  method {:test} KmsSymEncHappyCase()
  {
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var underTest :- expect AdminFixtures.DefaultAdmin();
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var kmsSystemKey := Types.SystemKey.kmsSymmetricEncryption(
      kmsSymmetricEncryption := Types.KmsSymmetricEncryption(
        KmsArn := Fixtures.publicKeyArn,
        AwsKms := KeyStoreTypes.AwsKms(
          grantTokens := None,
          kmsClient := Some(kmsClient))));
    var uuid :- expect UUID.GenerateUUID();
    var testId := trustStorageHCaseId + "-" + uuid;
    Fixtures.CreateHappyCaseId(id:=testId);

    var mutationsRequest := Types.Mutations(TerminalKmsArn := Some(Fixtures.postalHornKeyArn));
    var initInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := kmsSystemKey,
      // TODO-HV-2-Version
      // DoNotVersion := Some(false));
      DoNotVersion := Some(true));
    var initializeOutput :- expect underTest.InitializeMutation(initInput);
    var initializeToken := initializeOutput.MutationToken;

    var initializeAgainOutput :- expect underTest.InitializeMutation(initInput);
    expect initializeToken == initializeAgainOutput.MutationToken;

    var trustSK := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage());
    var sadInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := trustSK,
      // TODO-HV-2-Version
      // DoNotVersion := Some(false));
      DoNotVersion := Some(true));

    var sadOutput := underTest.InitializeMutation(sadInput);
    // TODO Restore this last expectation.
    expect sadOutput.Failure?, "Should have failed to initialize.";

    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
  }
}
