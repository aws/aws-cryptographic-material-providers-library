// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class KmsEcdhStaticConfigurations
  {
    private AWS.Cryptography.MaterialProviders.KmsPublicKeyDiscoveryInput _kmsPublicKeyDiscovery;
    private AWS.Cryptography.MaterialProviders.KmsPrivateKeyToStaticPublicKeyInput _kmsPrivateKeyToStaticPublicKey;
    public AWS.Cryptography.MaterialProviders.KmsPublicKeyDiscoveryInput KmsPublicKeyDiscovery
    {
      get { return this._kmsPublicKeyDiscovery; }
      set { this._kmsPublicKeyDiscovery = value; }
    }
    public bool IsSetKmsPublicKeyDiscovery()
    {
      return this._kmsPublicKeyDiscovery != null;
    }
    public AWS.Cryptography.MaterialProviders.KmsPrivateKeyToStaticPublicKeyInput KmsPrivateKeyToStaticPublicKey
    {
      get { return this._kmsPrivateKeyToStaticPublicKey; }
      set { this._kmsPrivateKeyToStaticPublicKey = value; }
    }
    public bool IsSetKmsPrivateKeyToStaticPublicKey()
    {
      return this._kmsPrivateKeyToStaticPublicKey != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetKmsPublicKeyDiscovery()) +
      Convert.ToUInt16(IsSetKmsPrivateKeyToStaticPublicKey());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
