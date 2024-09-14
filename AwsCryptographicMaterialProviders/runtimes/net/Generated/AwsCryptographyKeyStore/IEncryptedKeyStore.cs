// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public interface IEncryptedKeyStore
  {
    AWS.Cryptography.KeyStore.WriteNewKeyOutput WriteNewKey(AWS.Cryptography.KeyStore.WriteNewKeyInput input);
    AWS.Cryptography.KeyStore.WriteNewVersionOutput WriteNewVersion(AWS.Cryptography.KeyStore.WriteNewVersionInput input);
    AWS.Cryptography.KeyStore.GetActiveOutput GetActive(AWS.Cryptography.KeyStore.GetActiveInput input);
    AWS.Cryptography.KeyStore.GetVersionOutput GetVersion(AWS.Cryptography.KeyStore.GetVersionInput input);
    AWS.Cryptography.KeyStore.GetBeaconOutput GetBeacon(AWS.Cryptography.KeyStore.GetBeaconInput input);
    AWS.Cryptography.KeyStore.DescribeEncryptedKeyStoreOutput DescribeEncryptedKeyStore(AWS.Cryptography.KeyStore.DescribeEncryptedKeyStoreInput input);
    AWS.Cryptography.KeyStore.GetItemsForInitializeMutationOutput GetItemsForInitializeMutation(AWS.Cryptography.KeyStore.GetItemsForInitializeMutationInput input);
    AWS.Cryptography.KeyStore.WriteItemsForInitializeMutationOutput WriteItemsForInitializeMutation(AWS.Cryptography.KeyStore.WriteItemsForInitializeMutationInput input);
    AWS.Cryptography.KeyStore.QueryForVersionsOutput QueryForVersions(AWS.Cryptography.KeyStore.QueryForVersionsInput input);
    AWS.Cryptography.KeyStore.WriteMutatedVersionsOutput WriteMutatedVersions(AWS.Cryptography.KeyStore.WriteMutatedVersionsInput input);
    AWS.Cryptography.KeyStore.WriteCompleteMutationOutput WriteCompleteMutation(AWS.Cryptography.KeyStore.WriteCompleteMutationInput input);
  }
}
