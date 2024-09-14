// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public abstract class EncryptedKeyStoreBase : IEncryptedKeyStore
  {
    public AWS.Cryptography.KeyStore.WriteNewKeyOutput WriteNewKey(AWS.Cryptography.KeyStore.WriteNewKeyInput input)
    {
      input.Validate(); return _WriteNewKey(input);
    }
    protected abstract AWS.Cryptography.KeyStore.WriteNewKeyOutput _WriteNewKey(AWS.Cryptography.KeyStore.WriteNewKeyInput input);
    public AWS.Cryptography.KeyStore.WriteNewVersionOutput WriteNewVersion(AWS.Cryptography.KeyStore.WriteNewVersionInput input)
    {
      input.Validate(); return _WriteNewVersion(input);
    }
    protected abstract AWS.Cryptography.KeyStore.WriteNewVersionOutput _WriteNewVersion(AWS.Cryptography.KeyStore.WriteNewVersionInput input);
    public AWS.Cryptography.KeyStore.GetActiveOutput GetActive(AWS.Cryptography.KeyStore.GetActiveInput input)
    {
      input.Validate(); return _GetActive(input);
    }
    protected abstract AWS.Cryptography.KeyStore.GetActiveOutput _GetActive(AWS.Cryptography.KeyStore.GetActiveInput input);
    public AWS.Cryptography.KeyStore.GetVersionOutput GetVersion(AWS.Cryptography.KeyStore.GetVersionInput input)
    {
      input.Validate(); return _GetVersion(input);
    }
    protected abstract AWS.Cryptography.KeyStore.GetVersionOutput _GetVersion(AWS.Cryptography.KeyStore.GetVersionInput input);
    public AWS.Cryptography.KeyStore.GetBeaconOutput GetBeacon(AWS.Cryptography.KeyStore.GetBeaconInput input)
    {
      input.Validate(); return _GetBeacon(input);
    }
    protected abstract AWS.Cryptography.KeyStore.GetBeaconOutput _GetBeacon(AWS.Cryptography.KeyStore.GetBeaconInput input);
    public AWS.Cryptography.KeyStore.DescribeEncryptedKeyStoreOutput DescribeEncryptedKeyStore(AWS.Cryptography.KeyStore.DescribeEncryptedKeyStoreInput input)
    {
      input.Validate(); return _DescribeEncryptedKeyStore(input);
    }
    protected abstract AWS.Cryptography.KeyStore.DescribeEncryptedKeyStoreOutput _DescribeEncryptedKeyStore(AWS.Cryptography.KeyStore.DescribeEncryptedKeyStoreInput input);
    public AWS.Cryptography.KeyStore.GetItemsForInitializeMutationOutput GetItemsForInitializeMutation(AWS.Cryptography.KeyStore.GetItemsForInitializeMutationInput input)
    {
      input.Validate(); return _GetItemsForInitializeMutation(input);
    }
    protected abstract AWS.Cryptography.KeyStore.GetItemsForInitializeMutationOutput _GetItemsForInitializeMutation(AWS.Cryptography.KeyStore.GetItemsForInitializeMutationInput input);
    public AWS.Cryptography.KeyStore.WriteItemsForInitializeMutationOutput WriteItemsForInitializeMutation(AWS.Cryptography.KeyStore.WriteItemsForInitializeMutationInput input)
    {
      input.Validate(); return _WriteItemsForInitializeMutation(input);
    }
    protected abstract AWS.Cryptography.KeyStore.WriteItemsForInitializeMutationOutput _WriteItemsForInitializeMutation(AWS.Cryptography.KeyStore.WriteItemsForInitializeMutationInput input);
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
    public AWS.Cryptography.KeyStore.WriteCompleteMutationOutput WriteCompleteMutation(AWS.Cryptography.KeyStore.WriteCompleteMutationInput input)
    {
      input.Validate(); return _WriteCompleteMutation(input);
    }
    protected abstract AWS.Cryptography.KeyStore.WriteCompleteMutationOutput _WriteCompleteMutation(AWS.Cryptography.KeyStore.WriteCompleteMutationInput input);
  }
}
