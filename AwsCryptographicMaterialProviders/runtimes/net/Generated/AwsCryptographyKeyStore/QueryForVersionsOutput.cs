// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class QueryForVersionsOutput
  {
    private System.IO.MemoryStream _exclusiveStartKey;
    private System.Collections.Generic.List<AWS.Cryptography.KeyStore.EncryptedHierarchicalKey> _items;
    public System.IO.MemoryStream ExclusiveStartKey
    {
      get { return this._exclusiveStartKey; }
      set { this._exclusiveStartKey = value; }
    }
    public bool IsSetExclusiveStartKey()
    {
      return this._exclusiveStartKey != null;
    }
    public System.Collections.Generic.List<AWS.Cryptography.KeyStore.EncryptedHierarchicalKey> Items
    {
      get { return this._items; }
      set { this._items = value; }
    }
    public bool IsSetItems()
    {
      return this._items != null;
    }
    public void Validate()
    {
      if (!IsSetExclusiveStartKey()) throw new System.ArgumentException("Missing value for required property 'ExclusiveStartKey'");
      if (!IsSetItems()) throw new System.ArgumentException("Missing value for required property 'Items'");

    }
  }
}
