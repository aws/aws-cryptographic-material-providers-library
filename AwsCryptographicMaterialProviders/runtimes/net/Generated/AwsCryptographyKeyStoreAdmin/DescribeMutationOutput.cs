// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class DescribeMutationOutput
  {
    private AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities _original;
    private AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyProperities _terminal;
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
    public void Validate()
    {

    }
  }
}
