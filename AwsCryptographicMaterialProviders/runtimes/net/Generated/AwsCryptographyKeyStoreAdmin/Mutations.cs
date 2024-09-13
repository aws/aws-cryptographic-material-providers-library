// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class Mutations
  {
    private string _finalKmsArn;
    private System.Collections.Generic.Dictionary<string, string> _finalEncryptionContext;
    public string FinalKmsArn
    {
      get { return this._finalKmsArn; }
      set { this._finalKmsArn = value; }
    }
    public bool IsSetFinalKmsArn()
    {
      return this._finalKmsArn != null;
    }
    public System.Collections.Generic.Dictionary<string, string> FinalEncryptionContext
    {
      get { return this._finalEncryptionContext; }
      set { this._finalEncryptionContext = value; }
    }
    public bool IsSetFinalEncryptionContext()
    {
      return this._finalEncryptionContext != null;
    }
    public void Validate()
    {

    }
  }
}
