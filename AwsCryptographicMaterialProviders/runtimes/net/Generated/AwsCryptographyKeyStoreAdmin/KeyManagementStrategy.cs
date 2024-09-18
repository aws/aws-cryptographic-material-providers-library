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
    public AWS.Cryptography.KeyStore.AwsKms AwsKmsReEncrypt
    {
      get { return this._awsKmsReEncrypt; }
      set { this._awsKmsReEncrypt = value; }
    }
    public bool IsSetAwsKmsReEncrypt()
    {
      return this._awsKmsReEncrypt != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetAwsKmsReEncrypt());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
