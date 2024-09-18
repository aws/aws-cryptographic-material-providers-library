// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class KmsSymmetricEncryption
  {
    private AWS.Cryptography.KeyStoreAdmin.KmsSymmetricKeyArn _kmsArn;
    private AWS.Cryptography.KeyStore.AwsKms _awsKms;
    public AWS.Cryptography.KeyStoreAdmin.KmsSymmetricKeyArn KmsArn
    {
      get { return this._kmsArn; }
      set { this._kmsArn = value; }
    }
    public bool IsSetKmsArn()
    {
      return this._kmsArn != null;
    }
    public AWS.Cryptography.KeyStore.AwsKms AwsKms
    {
      get { return this._awsKms; }
      set { this._awsKms = value; }
    }
    public bool IsSetAwsKms()
    {
      return this._awsKms != null;
    }
    public void Validate()
    {
      if (!IsSetKmsArn()) throw new System.ArgumentException("Missing value for required property 'KmsArn'");
      if (!IsSetAwsKms()) throw new System.ArgumentException("Missing value for required property 'AwsKms'");

    }
  }
}
