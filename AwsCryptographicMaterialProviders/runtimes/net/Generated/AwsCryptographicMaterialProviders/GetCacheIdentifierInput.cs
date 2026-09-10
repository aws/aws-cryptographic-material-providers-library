// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class GetCacheIdentifierInput
  {
    private AWS.Cryptography.MaterialProviders.IKeyring _keyring;
    private string _branchKeyId;
    private string _branchKeyVersion;
    public AWS.Cryptography.MaterialProviders.IKeyring Keyring
    {
      get { return this._keyring; }
      set { this._keyring = value; }
    }
    public bool IsSetKeyring()
    {
      return this._keyring != null;
    }
    public string BranchKeyId
    {
      get { return this._branchKeyId; }
      set { this._branchKeyId = value; }
    }
    public bool IsSetBranchKeyId()
    {
      return this._branchKeyId != null;
    }
    public string BranchKeyVersion
    {
      get { return this._branchKeyVersion; }
      set { this._branchKeyVersion = value; }
    }
    public bool IsSetBranchKeyVersion()
    {
      return this._branchKeyVersion != null;
    }
    public void Validate()
    {
      if (!IsSetKeyring()) throw new System.ArgumentException("Missing value for required property 'Keyring'");
      if (!IsSetBranchKeyId()) throw new System.ArgumentException("Missing value for required property 'BranchKeyId'");

    }
  }
}
