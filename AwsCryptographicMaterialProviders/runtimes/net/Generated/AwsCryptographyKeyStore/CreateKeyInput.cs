// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class CreateKeyInput
  {
    private string _branchKeyIdentifier;
    private System.Collections.Generic.Dictionary<string, string> _encryptionContext;
    private string _arn;
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
    public string Arn
    {
      get { return this._arn; }
      set { this._arn = value; }
    }
    public bool IsSetArn()
    {
      return this._arn != null;
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

    }
  }
}
