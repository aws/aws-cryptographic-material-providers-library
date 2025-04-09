// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "AdminFixtures.dfy"

module {:options "/functionSyntax:4" } TestHV2Threats {
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

  /*
    // TODO: Create a Happy Case to Create HV-2 Key
    method {:test} TestCreateSRKForHV2NoEC()
    {
      var ddbClient :- expect Fixtures.ProvideDDBClient();
      var kmsClient :- expect Fixtures.ProvideKMSClient();
      var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
      var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
      var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
      var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
      var bk :- expect underTest.CreateKey(
        Types.CreateKeyInput(
          KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
          Strategy := Some(strategy),
          HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
        ));
      BranchKeyValidators.VerifyGetKeys(bk.Identifier, keyStore, storage,
                                        hierarchyVersion := KeyStoreTypes.HierarchyVersion.v2);
      var _ := CleanupItems.DeleteBranchKey(Identifier:=bk.Identifier, ddbClient:=ddbClient);
    }
  */

  // Call CreateBK with a KMS-ARN the CI principle does not have
  // kms:Encrypt permission for; expect a Error and failure.
  const testHV2CreationKMSDeniedId := "test-hv-2-bk-creation-kms-denied"
  method {:test} TestHV2CreationKMSDenied() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    // var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    // var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));

    var bk :- expect underTest.CreateKey(
      Types.CreateKeyInput(
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(Fixtures.hv1ReEncryptOnlyKeyArn),
        Strategy := Some(strategy),
        HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));

    expect bk.Failure?, "Expected a Failure when creating a branch key with KMS Arn without Encrypt Permission";
    match bk.error {
      case ComAmazonawsKms(nestedError) =>
        print nestedError;
      case _ => expect false, "Branch Key Creation SHOULD Fail with KMS Exception.";
    }
  }

  // Call Init Mutation with a KMS-ARN the CI principle does not have
  // kms:Encrypt permission for; expect a Error and failure.
  method {:test} TestHV2MutationKMSDenied() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var strategy :- expect AdminFixtures.SimpleKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));

    var bk :- expect underTest.CreateKey(
      Types.CreateKeyInput(
        KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(Fixtures.keyArn),
        Strategy := Some(strategy),
        HierarchyVersion := Some(KeyStoreTypes.HierarchyVersion.v2)
      ));

    // Mutating HV2 Branch Key with a Kms Key with ReEncyrptOnly KMS Permissions
    var mutationsRequest := Types.Mutations(TerminalKmsArn := Some(Fixtures.hv1ReEncryptOnlyKeyArn));

    var initInput := Types.InitializeMutationInput(
      Identifier := bk.Identifier,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()),
      DoNotVersion := Some(false));
    var initializeOutput :- expect underTest.InitializeMutation(initInput);

    expect initializeOutput.Failure?, "Expected a Failure when mutating a branch key with KMS Arn without Encrypt Permission";
    match initializeOutput.error {
      case MutationToException(nestedError) =>
        // TODO-HV2-Threat-Model: Expect exceptions
        print nestedError;
      case _ => expect false, "Branch Key Mutations SHOULD Fail with KMS Exception.";
    }

    var _ := CleanupItems.DeleteBranchKey(Identifier:=bk.Identifier, ddbClient:=ddbClient);
  }

  // Create a static HV-2 BK and tamper it; call Get* on it,
  // expect BKS.BranchKeyCiphertextException is thrown.
  method {:test} TestHV2GetKeyDigestWrong() {
    // This Test could be moved to KeyStore if we only use Static Branch Key
    // 1. Create a Branch Key for HV-2

    // 2. Update an Attribute like CustomEC

    // 3. Call Get Key

    // 4. Expect Failure and match to exact exception
  }

  // Create a static HV-2 BK; replace enc with a blob that is the wrong length;
  // call Get* on it; expect a BKS.BranchKeyCiphertextException to be thrown.
  method {:test} TestHV2GetKeyCiphertextWrongLength() {
    // This Test could be moved to KeyStore if we only use Static Branch Key
    // 1. Create a Branch Key for HV-2

    // 2. Update an Attribute "enc" with a different blob

    // 3. Call Get Key

    // 4. Expect Failure and match to exact exception
  }

  // Create a static HV-2 BK; carefully tamper it so only the KMS-ARN field
  // disagrees with the Humbolt Key ID embedded in the cipher-text;
  // call Get* on it; expect a reasonable BKS.BranchKeyCiphertextException is thrown.
  method {:test} TestHV2GetKeyCiphertextWrongKmsArn() {
    // This Test could be moved to KeyStore if we only use Static Branch Key
    // 1. Create a Branch Key for HV-2

    // 2. Update an Attribute "kmsKeyArn" with a different Valid KMS Arn for HV-2
    // Clarify what does `Humbolt Key ID` mean

    // 3. Call Get Key

    // 4. Expect Failure and match to exact exception
  }
}
