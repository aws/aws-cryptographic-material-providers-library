// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public abstract class KeyStorageInterfaceBase : IKeyStorageInterface
  {
    public AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyOutput WriteNewEncryptedBranchKey(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyInput input)
    {
      input.Validate(); return _WriteNewEncryptedBranchKey(input);
    }
    protected abstract AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyOutput _WriteNewEncryptedBranchKey(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyInput input);
    public AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionOutput WriteNewEncryptedBranchKeyVersion(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionInput input)
    {
      input.Validate(); return _WriteNewEncryptedBranchKeyVersion(input);
    }
    protected abstract AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionOutput _WriteNewEncryptedBranchKeyVersion(AWS.Cryptography.KeyStore.WriteNewEncryptedBranchKeyVersionInput input);
    public AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyOutput GetEncryptedActiveBranchKey(AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyInput input)
    {
      input.Validate(); return _GetEncryptedActiveBranchKey(input);
    }
    protected abstract AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyOutput _GetEncryptedActiveBranchKey(AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyInput input);
    public AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionOutput GetEncryptedBranchKeyVersion(AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionInput input)
    {
      input.Validate(); return _GetEncryptedBranchKeyVersion(input);
    }
    protected abstract AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionOutput _GetEncryptedBranchKeyVersion(AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionInput input);
    public AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyOutput GetEncryptedBeaconKey(AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyInput input)
    {
      input.Validate(); return _GetEncryptedBeaconKey(input);
    }
    protected abstract AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyOutput _GetEncryptedBeaconKey(AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyInput input);
    public AWS.Cryptography.KeyStore.GetKeyStorageInfoOutput GetKeyStorageInfo(AWS.Cryptography.KeyStore.GetKeyStorageInfoInput input)
    {
      input.Validate(); return _GetKeyStorageInfo(input);
    }
    protected abstract AWS.Cryptography.KeyStore.GetKeyStorageInfoOutput _GetKeyStorageInfo(AWS.Cryptography.KeyStore.GetKeyStorageInfoInput input);
    public AWS.Cryptography.KeyStore.GetItemsForInitializeMutationOutput GetItemsForInitializeMutation(AWS.Cryptography.KeyStore.GetItemsForInitializeMutationInput input)
    {
      input.Validate(); return _GetItemsForInitializeMutation(input);
    }
    protected abstract AWS.Cryptography.KeyStore.GetItemsForInitializeMutationOutput _GetItemsForInitializeMutation(AWS.Cryptography.KeyStore.GetItemsForInitializeMutationInput input);
    public AWS.Cryptography.KeyStore.WriteInitializeMutationOutput WriteInitializeMutation(AWS.Cryptography.KeyStore.WriteInitializeMutationInput input)
    {
      input.Validate(); return _WriteInitializeMutation(input);
    }
    protected abstract AWS.Cryptography.KeyStore.WriteInitializeMutationOutput _WriteInitializeMutation(AWS.Cryptography.KeyStore.WriteInitializeMutationInput input);
    public AWS.Cryptography.KeyStore.WriteAtomicMutationOutput WriteAtomicMutation(AWS.Cryptography.KeyStore.WriteAtomicMutationInput input)
    {
      input.Validate(); return _WriteAtomicMutation(input);
    }
    protected abstract AWS.Cryptography.KeyStore.WriteAtomicMutationOutput _WriteAtomicMutation(AWS.Cryptography.KeyStore.WriteAtomicMutationInput input);
    public AWS.Cryptography.KeyStore.QueryForVersionsOutput QueryForVersions(AWS.Cryptography.KeyStore.QueryForVersionsInput input)
    {
      input.Validate(); return _QueryForVersions(input);
    }
    protected abstract AWS.Cryptography.KeyStore.QueryForVersionsOutput _QueryForVersions(AWS.Cryptography.KeyStore.QueryForVersionsInput input);
    public AWS.Cryptography.KeyStore.WriteMutatedVersionsOutput WriteMutatedVersions(AWS.Cryptography.KeyStore.WriteMutatedVersionsInput input)
    {
      input.Validate(); return _WriteMutatedVersions(input);
    }
    protected abstract AWS.Cryptography.KeyStore.WriteMutatedVersionsOutput _WriteMutatedVersions(AWS.Cryptography.KeyStore.WriteMutatedVersionsInput input);
    public AWS.Cryptography.KeyStore.GetMutationOutput GetMutation(AWS.Cryptography.KeyStore.GetMutationInput input)
    {
      input.Validate(); return _GetMutation(input);
    }
    protected abstract AWS.Cryptography.KeyStore.GetMutationOutput _GetMutation(AWS.Cryptography.KeyStore.GetMutationInput input);
    public AWS.Cryptography.KeyStore.DeleteMutationOutput DeleteMutation(AWS.Cryptography.KeyStore.DeleteMutationInput input)
    {
      input.Validate(); return _DeleteMutation(input);
    }
    protected abstract AWS.Cryptography.KeyStore.DeleteMutationOutput _DeleteMutation(AWS.Cryptography.KeyStore.DeleteMutationInput input);
    public AWS.Cryptography.KeyStore.WriteMutationIndexOutput WriteMutationIndex(AWS.Cryptography.KeyStore.WriteMutationIndexInput input)
    {
      input.Validate(); return _WriteMutationIndex(input);
    }
    protected abstract AWS.Cryptography.KeyStore.WriteMutationIndexOutput _WriteMutationIndex(AWS.Cryptography.KeyStore.WriteMutationIndexInput input);
  }
}
