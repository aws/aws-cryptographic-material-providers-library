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
    private AWS.Cryptography.KeyStore.HierarchyVersion _hierarchyVersion;
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

    }
  }
}
