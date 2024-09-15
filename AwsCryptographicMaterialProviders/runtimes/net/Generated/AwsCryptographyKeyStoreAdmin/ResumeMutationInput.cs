// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class ResumeMutationInput
  {
    private string _branchKeyIdentifier;
    private AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities _original;
    private AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities _terminal;
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
    public AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities Original
    {
      get { return this._original; }
      set { this._original = value; }
    }
    public bool IsSetOriginal()
    {
      return this._original != null;
    }
    public AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities Terminal
    {
      get { return this._terminal; }
      set { this._terminal = value; }
    }
    public bool IsSetTerminal()
    {
      return this._terminal != null;
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
      if (!IsSetOriginal()) throw new System.ArgumentException("Missing value for required property 'Original'");
      if (!IsSetTerminal()) throw new System.ArgumentException("Missing value for required property 'Terminal'");

    }
  }
}
