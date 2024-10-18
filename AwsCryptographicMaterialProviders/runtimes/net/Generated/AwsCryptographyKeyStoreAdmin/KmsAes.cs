// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class KmsAes
  {
    private AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier _kmsAesIdentifier;
    private AWS.Cryptography.KeyStore.AwsKms _awsKms;
    public AWS.Cryptography.KeyStoreAdmin.KmsAesIdentifier KmsAesIdentifier
    {
      get { return this._kmsAesIdentifier; }
      set { this._kmsAesIdentifier = value; }
    }
    public bool IsSetKmsAesIdentifier()
    {
      return this._kmsAesIdentifier != null;
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
      if (!IsSetKmsAesIdentifier()) throw new System.ArgumentException("Missing value for required property 'KmsAesIdentifier'");
      if (!IsSetAwsKms()) throw new System.ArgumentException("Missing value for required property 'AwsKms'");

    }
  }
}
