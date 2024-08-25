// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class CreateKeyInput
  {
    private string _branchKeyIdentifier;
    private System.Collections.Generic.Dictionary<string, string> _encryptionContext;
    private AWS.Cryptography.KeyStoreAdmin.KMSIdentifier _kmsArn;
    private Amazon.KeyManagementService.IAmazonKeyManagementService _kmsClient;
    private System.Collections.Generic.List<string> _grantTokens;
    public string BranchKeyIdentifier
    {
      get { return this._branchKeyIdentifier; }
      set { this._branchKeyIdentifier = value; }
    }
    public bool IsSetBranchKeyIdentifier()
    {
      return this._branchKeyIdentifier != null;
    }
    public System.Collections.Generic.Dictionary<string, string> EncryptionContext
    {
      get { return this._encryptionContext; }
      set { this._encryptionContext = value; }
    }
    public bool IsSetEncryptionContext()
    {
      return this._encryptionContext != null;
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
    public Amazon.KeyManagementService.IAmazonKeyManagementService KmsClient
    {
      get { return this._kmsClient; }
      set { this._kmsClient = value; }
    }
    public bool IsSetKmsClient()
    {
      return this._kmsClient != null;
    }
    public System.Collections.Generic.List<string> GrantTokens
    {
      get { return this._grantTokens; }
      set { this._grantTokens = value; }
    }
    public bool IsSetGrantTokens()
    {
      return this._grantTokens != null;
    }
    public void Validate()
    {
      if (!IsSetKmsArn()) throw new System.ArgumentException("Missing value for required property 'KmsArn'");
      if (!IsSetKmsClient()) throw new System.ArgumentException("Missing value for required property 'KmsClient'");

    }
  }
}
