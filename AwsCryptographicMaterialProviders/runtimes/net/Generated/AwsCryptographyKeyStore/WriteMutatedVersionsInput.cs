// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class WriteMutatedVersionsInput
  {
    private System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey> _items;
    private AWS.Cryptography.KeyStore.MutationLock _mutationLock;
    public System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey> Items
    {
      get { return this._items; }
      set { this._items = value; }
    }
    public bool IsSetItems()
    {
      return this._items != null;
    }
    public AWS.Cryptography.KeyStore.MutationLock MutationLock
    {
      get { return this._mutationLock; }
      set { this._mutationLock = value; }
    }
    public bool IsSetMutationLock()
    {
      return this._mutationLock != null;
    }
    public void Validate()
    {
      if (!IsSetItems()) throw new System.ArgumentException("Missing value for required property 'Items'");
      if (!IsSetMutationLock()) throw new System.ArgumentException("Missing value for required property 'MutationLock'");

    }
  }
}
