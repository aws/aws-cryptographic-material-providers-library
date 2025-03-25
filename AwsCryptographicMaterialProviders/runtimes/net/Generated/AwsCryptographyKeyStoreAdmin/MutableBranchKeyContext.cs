// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class MutableBranchKeyContext
  {
    private string _kmsArn;
    private System.Collections.Generic.Dictionary<string, string> _encryptionContext;
    private AWS.Cryptography.KeyStore.HierarchyVersion _hierarchyVersion;
    public string KmsArn
    {
      get { return this._kmsArn; }
      set { this._kmsArn = value; }
    }
    public bool IsSetKmsArn()
    {
      return this._kmsArn != null;
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
    public AWS.Cryptography.KeyStore.HierarchyVersion HierarchyVersion
    {
      get { return this._hierarchyVersion; }
      set { this._hierarchyVersion = value; }
    }
    public bool IsSetHierarchyVersion()
    {
      return this._hierarchyVersion != null;
    }
    public void Validate()
    {
      if (!IsSetKmsArn()) throw new System.ArgumentException("Missing value for required property 'KmsArn'");
      if (!IsSetEncryptionContext()) throw new System.ArgumentException("Missing value for required property 'EncryptionContext'");
      if (!IsSetHierarchyVersion()) throw new System.ArgumentException("Missing value for required property 'HierarchyVersion'");

    }
  }
}
