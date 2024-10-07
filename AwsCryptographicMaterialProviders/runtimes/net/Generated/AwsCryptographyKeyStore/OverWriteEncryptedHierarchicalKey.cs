// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class OverWriteEncryptedHierarchicalKey
  {
    private AWS.Cryptography.KeyStore.EncryptedHierarchicalKey _encryptedHierarchicalKey;
    private AWS.Cryptography.KeyStore.EncryptedHierarchicalKey _old;
    public AWS.Cryptography.KeyStore.EncryptedHierarchicalKey EncryptedHierarchicalKey
    {
      get { return this._encryptedHierarchicalKey; }
      set { this._encryptedHierarchicalKey = value; }
    }
    public bool IsSetEncryptedHierarchicalKey()
    {
      return this._encryptedHierarchicalKey != null;
    }
    public AWS.Cryptography.KeyStore.EncryptedHierarchicalKey Old
    {
      get { return this._old; }
      set { this._old = value; }
    }
    public bool IsSetOld()
    {
      return this._old != null;
    }
    public void Validate()
    {
      if (!IsSetEncryptedHierarchicalKey()) throw new System.ArgumentException("Missing value for required property 'EncryptedHierarchicalKey'");
      if (!IsSetOld()) throw new System.ArgumentException("Missing value for required property 'Old'");

    }
  }
}
