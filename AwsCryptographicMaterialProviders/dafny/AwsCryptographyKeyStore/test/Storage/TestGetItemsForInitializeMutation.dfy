// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Fixtures.dfy"

module {:options "/functionSyntax:4"} TestGetItemsForInitializeMutation {
  import UInt = Fixtures.UInt
  import Types = Fixtures.Types
  import UTF8 = Fixtures.UTF8
  import opened Wrappers
  import DefaultKeyStorageInterface
  import Fixtures
  import Structure
  import DDB = Com.Amazonaws.Dynamodb
  import KMS = Com.Amazonaws.Kms
  import KeyStore

  const physicalName: DDB.Types.TableName := Fixtures.branchKeyStoreName
  const logicalName := Fixtures.logicalKeyStoreName
  // The Key Store will consider this mutation lock invalid
  // The Storage layer will not.
  const mLockedId := "test-get-items-for-initialize-mutation"

  method {:test} TestHappyCase()
  {
    var underTest :- expect Fixtures.DefaultStorage();
    var input := Types.GetItemsForInitializeMutationInput(
      Identifier := Fixtures.branchKeyId
    );
    var output :- expect underTest.GetItemsForInitializeMutation(input);
    expect Structure.TYPE_FIELD in output.ActiveItem.EncryptionContext,
                                   "`type` missing from activeItem!";
    expect
      output.ActiveItem.Type.ActiveHierarchicalSymmetricVersion?,
      "activeItem was not Active? 'type': " + output.ActiveItem.EncryptionContext[Structure.TYPE_FIELD];
    expect Structure.TYPE_FIELD in output.BeaconItem.EncryptionContext,
                                   "`type` missing from beaconItem!";
    expect
      output.BeaconItem.Type.ActiveHierarchicalSymmetricBeacon?,
      "beaconItem was not Beacon? 'type': " + output.BeaconItem.EncryptionContext[Structure.TYPE_FIELD];
    expect
      output.MutationCommitment.None?,
      "MutationCommitment was not None. 'UUID': " + output.MutationCommitment.value.UUID;
    expect
      output.MutationIndex.None?,
      "MutationIndex was not None. 'UUID': " + output.MutationIndex.value.UUID;
  }

  method {:test} TestHappyCaseMLocked()
  {
    var underTest :- expect Fixtures.DefaultStorage();
    var input := Types.GetItemsForInitializeMutationInput(
      Identifier := mLockedId
    );
    var output :- expect underTest.GetItemsForInitializeMutation(input);
    expect Structure.TYPE_FIELD in output.ActiveItem.EncryptionContext,
                                   "`type` missing from activeItem!";
    expect
      output.ActiveItem.Type.ActiveHierarchicalSymmetricVersion?,
      "activeItem was not Active? 'type': " + output.ActiveItem.EncryptionContext[Structure.TYPE_FIELD];
    expect Structure.TYPE_FIELD in output.BeaconItem.EncryptionContext,
                                   "`type` missing from beaconItem!";
    expect
      output.BeaconItem.Type.ActiveHierarchicalSymmetricBeacon?,
      "beaconItem was not Beacon? 'type': " + output.BeaconItem.EncryptionContext[Structure.TYPE_FIELD];
    expect
      output.MutationCommitment.Some?,
      "MutationCommitment was not Some.";
    expect
      output.MutationIndex.Some?,
      "MutationIndex was not Some.";
  }
}