// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class AwsKmsDecryptEncrypt
  {
    private AWS.Cryptography.KeyStore.AwsKms _decrypt;
    private AWS.Cryptography.KeyStore.AwsKms _encrypt;
    public AWS.Cryptography.KeyStore.AwsKms Decrypt
    {
      get { return this._decrypt; }
      set { this._decrypt = value; }
    }
    public bool IsSetDecrypt()
    {
      return this._decrypt != null;
    }
    public AWS.Cryptography.KeyStore.AwsKms Encrypt
    {
      get { return this._encrypt; }
      set { this._encrypt = value; }
    }
    public bool IsSetEncrypt()
    {
      return this._encrypt != null;
    }
    public void Validate()
    {

    }
  }
}
