// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class KeyManagement
  {
    private AWS.Cryptography.KeyStore.AwsKms _kms;
    public AWS.Cryptography.KeyStore.AwsKms Kms
    {
      get { return this._kms; }
      set { this._kms = value; }
    }
    public bool IsSetKms()
    {
      return this._kms != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetKms());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
