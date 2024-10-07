// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class GetKeyStorageInfoOutput
  {
    private string _name;
    private string _logicalName;
    public string Name
    {
      get { return this._name; }
      set { this._name = value; }
    }
    public bool IsSetName()
    {
      return this._name != null;
    }
    public string LogicalName
    {
      get { return this._logicalName; }
      set { this._logicalName = value; }
    }
    public bool IsSetLogicalName()
    {
      return this._logicalName != null;
    }
    public void Validate()
    {
      if (!IsSetName()) throw new System.ArgumentException("Missing value for required property 'Name'");
      if (!IsSetLogicalName()) throw new System.ArgumentException("Missing value for required property 'LogicalName'");

    }
  }
}
