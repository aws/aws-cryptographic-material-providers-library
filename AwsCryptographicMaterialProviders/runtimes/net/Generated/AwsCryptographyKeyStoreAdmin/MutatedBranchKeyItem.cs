// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class MutatedBranchKeyItem
  {
    private string _itemType;
    private string _description;
    public string ItemType
    {
      get { return this._itemType; }
      set { this._itemType = value; }
    }
    public bool IsSetItemType()
    {
      return this._itemType != null;
    }
    public string Description
    {
      get { return this._description; }
      set { this._description = value; }
    }
    public bool IsSetDescription()
    {
      return this._description != null;
    }
    public void Validate()
    {
      if (!IsSetItemType()) throw new System.ArgumentException("Missing value for required property 'ItemType'");
      if (!IsSetDescription()) throw new System.ArgumentException("Missing value for required property 'Description'");

    }
  }
}
