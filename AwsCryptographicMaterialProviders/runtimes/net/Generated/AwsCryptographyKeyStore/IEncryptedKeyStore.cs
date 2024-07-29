// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public interface IEncryptedKeyStore
  {
    AWS.Cryptography.KeyStore.WriteNewKeyToStoreOutput WriteNewKeyToStore(AWS.Cryptography.KeyStore.WriteNewKeyToStoreInput input);
    AWS.Cryptography.KeyStore.WriteNewBranchKeyVersionToKeystoreOutput WriteNewBranchKeyVersionToKeystore(AWS.Cryptography.KeyStore.WriteNewBranchKeyVersionToKeystoreInput input);
    AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyOutput GetEncryptedActiveBranchKey(AWS.Cryptography.KeyStore.GetEncryptedActiveBranchKeyInput input);
    AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionOutput GetEncryptedBranchKeyVersion(AWS.Cryptography.KeyStore.GetEncryptedBranchKeyVersionInput input);
    AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyOutput GetEncryptedBeaconKey(AWS.Cryptography.KeyStore.GetEncryptedBeaconKeyInput input);
    AWS.Cryptography.KeyStore.GetTableNameOutput GetTableName(AWS.Cryptography.KeyStore.GetTableNameInput input);
  }
}
