// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class OverWriteEncryptedHierarchicalKey
  {
    private AWS.Cryptography.KeyStore.EncryptedHierarchicalKey _item;
    private AWS.Cryptography.KeyStore.EncryptedHierarchicalKey _old;
    public AWS.Cryptography.KeyStore.EncryptedHierarchicalKey Item
    {
      get { return this._item; }
      set { this._item = value; }
    }
    public bool IsSetItem()
    {
      return this._item != null;
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
      if (!IsSetItem()) throw new System.ArgumentException("Missing value for required property 'Item'");
      if (!IsSetOld()) throw new System.ArgumentException("Missing value for required property 'Old'");

    }
  }
}
