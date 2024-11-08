// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public interface IKeyStorageInterface
  {
    AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyOutput WriteNewEncryptedBranchKey(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyInput input);
    AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionOutput WriteNewEncryptedBranchKeyVersion(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionInput input);
    AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyOutput GetEncryptedActiveBranchKey(AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyInput input);
    AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionOutput GetEncryptedBranchKeyVersion(AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionInput input);
    AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyOutput GetEncryptedBeaconKey(AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyInput input);
    AWS.Cryptography.KeyStore.GetKeyStorageInfoOutput GetKeyStorageInfo(AWS.Cryptography.KeyStore.GetKeyStorageInfoInput input);
    AWS.Cryptography.KeyStore.GetItemsForInitializeMutationOutput GetItemsForInitializeMutation(AWS.Cryptography.KeyStore.GetItemsForInitializeMutationInput input);
    AWS.Cryptography.KeyStore.WriteInitializeMutationOutput WriteInitializeMutation(AWS.Cryptography.KeyStore.WriteInitializeMutationInput input);
    AWS.Cryptography.KeyStore.WriteAtomicMutationOutput WriteAtomicMutation(AWS.Cryptography.KeyStore.WriteAtomicMutationInput input);
    AWS.Cryptography.KeyStore.QueryForVersionsOutput QueryForVersions(AWS.Cryptography.KeyStore.QueryForVersionsInput input);
    AWS.Cryptography.KeyStore.WriteMutatedVersionsOutput WriteMutatedVersions(AWS.Cryptography.KeyStore.WriteMutatedVersionsInput input);
    AWS.Cryptography.KeyStore.GetMutationOutput GetMutation(AWS.Cryptography.KeyStore.GetMutationInput input);
    AWS.Cryptography.KeyStore.DeleteMutationOutput DeleteMutation(AWS.Cryptography.KeyStore.DeleteMutationInput input);
    AWS.Cryptography.KeyStore.WriteMutationIndexOutput WriteMutationIndex(AWS.Cryptography.KeyStore.WriteMutationIndexInput input);
  }
}
