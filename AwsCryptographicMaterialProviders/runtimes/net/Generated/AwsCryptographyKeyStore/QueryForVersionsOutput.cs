// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class QueryForVersionsOutput
  {
    private System.IO.MemoryStream _pageIndex;
    private System.Collections.Generic.List<AWS.Cryptography.KeyStore.EncryptedHierarchicalKey> _items;
    public System.IO.MemoryStream PageIndex
    {
      get { return this._pageIndex; }
      set { this._pageIndex = value; }
    }
    public bool IsSetPageIndex()
    {
      return this._pageIndex != null;
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
      if (!IsSetPageIndex()) throw new System.ArgumentException("Missing value for required property 'PageIndex'");
      if (!IsSetItems()) throw new System.ArgumentException("Missing value for required property 'Items'");

    }
  }
}
