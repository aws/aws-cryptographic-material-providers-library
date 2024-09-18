// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class Mutations
  {
    private string _terminalKmsArn;
    private System.Collections.Generic.Dictionary<string, string> _terminalEncryptionContext;
    public string TerminalKmsArn
    {
      get { return this._terminalKmsArn; }
      set { this._terminalKmsArn = value; }
    }
    public bool IsSetTerminalKmsArn()
    {
      return this._terminalKmsArn != null;
    }
    public System.Collections.Generic.Dictionary<string, string> TerminalEncryptionContext
    {
      get { return this._terminalEncryptionContext; }
      set { this._terminalEncryptionContext = value; }
    }
    public bool IsSetTerminalEncryptionContext()
    {
      return this._terminalEncryptionContext != null;
    }
    public void Validate()
    {

    }
  }
}
