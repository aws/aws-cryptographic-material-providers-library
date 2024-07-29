// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public abstract class EncryptedKeyStoreBase : IEncryptedKeyStore
  {
    public AWS.Cryptography.KeyStore.WriteNewKeyToStoreOutput WriteNewKeyToStore(AWS.Cryptography.KeyStore.WriteNewKeyToStoreInput input)
    {
      input.Validate(); return _WriteNewKeyToStore(input);
    }
    protected abstract AWS.Cryptography.KeyStore.WriteNewKeyToStoreOutput _WriteNewKeyToStore(AWS.Cryptography.KeyStore.WriteNewKeyToStoreInput input);
    public AWS.Cryptography.KeyStore.WriteNewBranchKeyVersionToKeystoreOutput WriteNewBranchKeyVersionToKeystore(AWS.Cryptography.KeyStore.WriteNewBranchKeyVersionToKeystoreInput input)
    {
      input.Validate(); return _WriteNewBranchKeyVersionToKeystore(input);
    }
    protected abstract AWS.Cryptography.KeyStore.WriteNewBranchKeyVersionToKeystoreOutput _WriteNewBranchKeyVersionToKeystore(AWS.Cryptography.KeyStore.WriteNewBranchKeyVersionToKeystoreInput input);
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
    public AWS.Cryptography.KeyStore.GetTableNameOutput GetTableName(AWS.Cryptography.KeyStore.GetTableNameInput input)
    {
      input.Validate(); return _GetTableName(input);
    }
    protected abstract AWS.Cryptography.KeyStore.GetTableNameOutput _GetTableName(AWS.Cryptography.KeyStore.GetTableNameInput input);
  }
}
