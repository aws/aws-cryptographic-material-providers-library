// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class SystemKey
  {
    private AWS.Cryptography.KeyStoreAdmin.KmsAes _kmsAes;
    private AWS.Cryptography.KeyStoreAdmin.TrustStorage _trustStorage;
    public AWS.Cryptography.KeyStoreAdmin.KmsAes KmsAes
    {
      get { return this._kmsAes; }
      set { this._kmsAes = value; }
    }
    public bool IsSetKmsAes()
    {
      return this._kmsAes != null;
    }
    public AWS.Cryptography.KeyStoreAdmin.TrustStorage TrustStorage
    {
      get { return this._trustStorage; }
      set { this._trustStorage = value; }
    }
    public bool IsSetTrustStorage()
    {
      return this._trustStorage != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetKmsAes()) +
      Convert.ToUInt16(IsSetTrustStorage());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
