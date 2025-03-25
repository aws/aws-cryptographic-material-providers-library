// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class KmsMRKey
  {
    private string _keyArn;
    private string _region;
    public string KeyArn
    {
      get { return this._keyArn; }
      set { this._keyArn = value; }
    }
    public bool IsSetKeyArn()
    {
      return this._keyArn != null;
    }
    public string Region
    {
      get { return this._region; }
      set { this._region = value; }
    }
    public bool IsSetRegion()
    {
      return this._region != null;
    }
    public void Validate()
    {
      if (!IsSetKeyArn()) throw new System.ArgumentException("Missing value for required property 'KeyArn'");
      if (!IsSetRegion()) throw new System.ArgumentException("Missing value for required property 'Region'");

    }
  }
}
