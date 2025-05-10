// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "AdminFixtures.dfy"

module {:options "/functionSyntax:4" } TestHv2KmsExceptions {
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

  // Call CreateBK with a KMS-ARN the CI principle does not have
  // kms:Encrypt permission for; expect a Error and failure.
  const testHV2CreationKMSDeniedId := "test-hv-2-bk-creation-kms-denied"
  method {:test} TestHV2CreationKMSDenied() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));

    var bk := underTest.CreateKey(
      Types.CreateKeyInput(
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(Fixtures.kmsArnForHV1),
        Strategy := Some(strategy),
        HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));

    expect bk.Failure?, "Expected a Failure when creating a branch key with KMS Arn without Encrypt Permission";
    match bk.error {
      case AwsCryptographyKeyStore(nestedError) =>
        match nestedError {
          case ComAmazonawsKms(kmsNestedError) =>
            expect kmsNestedError.OpaqueWithText?, "Branch Key Creation SHOULD Fail with KMS OpaqueWithText Exception, ";
          case _ => expect false, "Branch Key Creation SHOULD fail with KMS nested Exception";
        }
      case _ => expect false, "Branch Key Creation SHOULD Fail with AwsCryptographyKeyStore Exception.";
    }
  }

  // Call Init Mutation with a KMS-ARN the CI principle does not have
  // kms:Encrypt permission for; expect a Error and failure.
  const testHV2MutationKMSDeniedId := "test-hv-2-bk-mutation-kms-denied"
  method {:test} TestHV2MutationKMSDenied() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));

    var uuid :- expect UUID.GenerateUUID();
    var testId := testHV2MutationKMSDeniedId + "-" + uuid;
    AdminFixtures.CreateHappyCaseId(id := testId, hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2, strategy? := Some(strategy), admin? := Some(underTest));

    // Mutating HV2 Branch Key with a Kms Key with ReEncyrpt Only KMS Permissions
    var mutationsRequest := Types.Mutations(TerminalKmsArn := Some(Fixtures.kmsArnForHV1));

    var initInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()),
      DoNotVersion := Some(false));
    var initializeOutput := underTest.InitializeMutation(initInput);

    expect initializeOutput.Failure?, "Expected a Failure when mutating a branch key with KMS Arn without Encrypt Permission";
    // TODO-HV-2-M2: We should expect a MutationTo Exception when terminalKmsArn
    // does not have HV-2 permissions when mutating a HV-2 branch keys.
    // expect initializeOutput.error.MutationToException?,
    // "Expected a MutationTo Exception when mutating a branch key with KMS Arn without Encrypt Permission for HV2 Branch Keys";

    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
  }
}