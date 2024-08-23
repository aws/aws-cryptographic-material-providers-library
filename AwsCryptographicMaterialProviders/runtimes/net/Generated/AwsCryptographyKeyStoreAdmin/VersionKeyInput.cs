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
    private string _kmsArn;
    private Amazon.KeyManagementService.IAmazonKeyManagementService _kmsClient;
    public string BranchKeyIdentifier
    {
      get { return this._branchKeyIdentifier; }
      set { this._branchKeyIdentifier = value; }
    }
    public bool IsSetBranchKeyIdentifier()
    {
      return this._branchKeyIdentifier != null;
    }
    public string KmsArn
    {
      get { return this._kmsArn; }
      set { this._kmsArn = value; }
    }
    public bool IsSetKmsArn()
    {
      return this._kmsArn != null;
    }
    public Amazon.KeyManagementService.IAmazonKeyManagementService KmsClient
    {
      get { return this._kmsClient; }
      set { this._kmsClient = value; }
    }
    public bool IsSetKmsClient()
    {
      return this._kmsClient != null;
    }
    public void Validate()
    {
      if (!IsSetBranchKeyIdentifier()) throw new System.ArgumentException("Missing value for required property 'BranchKeyIdentifier'");
      if (!IsSetKmsArn()) throw new System.ArgumentException("Missing value for required property 'KmsArn'");
      if (!IsSetKmsClient()) throw new System.ArgumentException("Missing value for required property 'KmsClient'");

    }
  }
}
