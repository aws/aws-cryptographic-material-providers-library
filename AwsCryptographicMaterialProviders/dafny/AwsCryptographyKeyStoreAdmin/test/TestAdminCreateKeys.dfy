// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../AwsCryptographyKeyStore/test/TestGetKeys.dfy"
include "../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "AdminFixtures.dfy"

module {:options "/functionSyntax:4" } TestAdminCreateKeys {
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

  method {:test} TestCreateBranchAndBeaconKeys()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));

    var input := Types.CreateKeyInput(
      Identifier := None,
      EncryptionContext := None,
      KmsArn := Types.KmsSymmetricKeyArn.KmsKeyArn(keyArn),
      Strategy := Some(strategy)
    );
    var identifier? :- expect underTest.CreateKey(input);
    var identifier := identifier?.Identifier;
    expect identifier?.HierarchyVersion == KeyStoreTypes.HierarchyVersion.v1,
      "KeyStoreAdmin should create branch key with `hierarchy-version-1` when no `HierarchyVersion` provided";

    // Get branch key items from storage
    TestGetKeys.VerifyGetKeys(
      identifier := identifier,
      keyStore := keyStore,
      storage := storage
    );

    // Since this process uses a read DDB table,
    // the number of records will forever increase.
    // To avoid this, remove the items.
    var _ := CleanupItems.DeleteBranchKey(Identifier:=identifier, ddbClient:=ddbClient);
  }
}
