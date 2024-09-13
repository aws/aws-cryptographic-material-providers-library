// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class VersionKeyInput
  {
    private string _branchKeyIdentifier;
    private AWS.Cryptography.KeyStoreAdmin.KMSIdentifier _kmsArn;
    private AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy _strategy;
    public string BranchKeyIdentifier
    {
      get { return this._branchKeyIdentifier; }
      set { this._branchKeyIdentifier = value; }
    }
    public bool IsSetBranchKeyIdentifier()
    {
      return this._branchKeyIdentifier != null;
    }
    public AWS.Cryptography.KeyStoreAdmin.KMSIdentifier KmsArn
    {
      get { return this._kmsArn; }
      set { this._kmsArn = value; }
    }
    public bool IsSetKmsArn()
    {
      return this._kmsArn != null;
    }
    public AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy Strategy
    {
      get { return this._strategy; }
      set { this._strategy = value; }
    }
    public bool IsSetStrategy()
    {
      return this._strategy != null;
    }
    public void Validate()
    {
      if (!IsSetBranchKeyIdentifier()) throw new System.ArgumentException("Missing value for required property 'BranchKeyIdentifier'");
      if (!IsSetKmsArn()) throw new System.ArgumentException("Missing value for required property 'KmsArn'");

    }
  }
}
