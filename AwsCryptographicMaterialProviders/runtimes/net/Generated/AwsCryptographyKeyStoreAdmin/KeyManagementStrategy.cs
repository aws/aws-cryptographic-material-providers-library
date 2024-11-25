// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class KeyManagementStrategy
  {
    private AWS.Cryptography.KeyStore.AwsKms _awsKmsReEncrypt;
    private AWS.Cryptography.KeyStoreAdmin.AwsKmsDecryptEncrypt _awsKmsDecryptEncrypt;
    public AWS.Cryptography.KeyStore.AwsKms AwsKmsReEncrypt
    {
      get { return this._awsKmsReEncrypt; }
      set { this._awsKmsReEncrypt = value; }
    }
    public bool IsSetAwsKmsReEncrypt()
    {
      return this._awsKmsReEncrypt != null;
    }
    public AWS.Cryptography.KeyStoreAdmin.AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt
    {
      get { return this._awsKmsDecryptEncrypt; }
      set { this._awsKmsDecryptEncrypt = value; }
    }
    public bool IsSetAwsKmsDecryptEncrypt()
    {
      return this._awsKmsDecryptEncrypt != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetAwsKmsReEncrypt()) +
      Convert.ToUInt16(IsSetAwsKmsDecryptEncrypt());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
