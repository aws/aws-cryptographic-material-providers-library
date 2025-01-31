// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class KeyStoreAdminConfig
  {
    private string _logicalKeyStoreName;
    private AWS.Cryptography.KeyStore.Storage _storage;
    public string LogicalKeyStoreName
    {
      get { return this._logicalKeyStoreName; }
      set { this._logicalKeyStoreName = value; }
    }
    public bool IsSetLogicalKeyStoreName()
    {
      return this._logicalKeyStoreName != null;
    }
    public AWS.Cryptography.KeyStore.Storage Storage
    {
      get { return this._storage; }
      set { this._storage = value; }
    }
    public bool IsSetStorage()
    {
      return this._storage != null;
    }
    public void Validate()
    {
      if (!IsSetLogicalKeyStoreName()) throw new System.ArgumentException("Missing value for required property 'LogicalKeyStoreName'");
      if (!IsSetStorage()) throw new System.ArgumentException("Missing value for required property 'Storage'");

    }
  }
}
