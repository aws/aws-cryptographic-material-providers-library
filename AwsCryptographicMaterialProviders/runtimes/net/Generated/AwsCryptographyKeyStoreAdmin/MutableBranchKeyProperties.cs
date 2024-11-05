// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class MutableBranchKeyProperties
  {
    private string _kmsArn;
    private System.Collections.Generic.Dictionary<string, string> _customEncryptionContext;
    public string KmsArn
    {
      get { return this._kmsArn; }
      set { this._kmsArn = value; }
    }
    public bool IsSetKmsArn()
    {
      return this._kmsArn != null;
    }
    public System.Collections.Generic.Dictionary<string, string> CustomEncryptionContext
    {
      get { return this._customEncryptionContext; }
      set { this._customEncryptionContext = value; }
    }
    public bool IsSetCustomEncryptionContext()
    {
      return this._customEncryptionContext != null;
    }
    public void Validate()
    {
      if (!IsSetKmsArn()) throw new System.ArgumentException("Missing value for required property 'KmsArn'");
      if (!IsSetCustomEncryptionContext()) throw new System.ArgumentException("Missing value for required property 'CustomEncryptionContext'");

    }
  }
}
