// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class Storage
  {
    private AWS.Cryptography.KeyStore.DynamoDBTable _ddb;
    private AWS.Cryptography.KeyStore.IKeyStorageInterface _custom;
    public AWS.Cryptography.KeyStore.DynamoDBTable Ddb
    {
      get { return this._ddb; }
      set { this._ddb = value; }
    }
    public bool IsSetDdb()
    {
      return this._ddb != null;
    }
    public AWS.Cryptography.KeyStore.IKeyStorageInterface Custom
    {
      get { return this._custom; }
      set { this._custom = value; }
    }
    public bool IsSetCustom()
    {
      return this._custom != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetDdb()) +
      Convert.ToUInt16(IsSetCustom());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
