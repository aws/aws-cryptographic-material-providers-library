// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class RawEcdhStaticConfigurations
  {
    private AWS.Cryptography.MaterialProviders.PublicKeyDiscoveryInput _publicKeyDiscovery;
    private AWS.Cryptography.MaterialProviders.RawPrivateKeyToStaticPublicKeyInput _rawPrivateKeyToStaticPublicKey;
    private AWS.Cryptography.MaterialProviders.EphemeralPrivateKeyToStaticPublicKeyInput _ephemeralPrivateKeyToStaticPublicKey;
    public AWS.Cryptography.MaterialProviders.PublicKeyDiscoveryInput PublicKeyDiscovery
    {
      get { return this._publicKeyDiscovery; }
      set { this._publicKeyDiscovery = value; }
    }
    public bool IsSetPublicKeyDiscovery()
    {
      return this._publicKeyDiscovery != null;
    }
    public AWS.Cryptography.MaterialProviders.RawPrivateKeyToStaticPublicKeyInput RawPrivateKeyToStaticPublicKey
    {
      get { return this._rawPrivateKeyToStaticPublicKey; }
      set { this._rawPrivateKeyToStaticPublicKey = value; }
    }
    public bool IsSetRawPrivateKeyToStaticPublicKey()
    {
      return this._rawPrivateKeyToStaticPublicKey != null;
    }
    public AWS.Cryptography.MaterialProviders.EphemeralPrivateKeyToStaticPublicKeyInput EphemeralPrivateKeyToStaticPublicKey
    {
      get { return this._ephemeralPrivateKeyToStaticPublicKey; }
      set { this._ephemeralPrivateKeyToStaticPublicKey = value; }
    }
    public bool IsSetEphemeralPrivateKeyToStaticPublicKey()
    {
      return this._ephemeralPrivateKeyToStaticPublicKey != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetPublicKeyDiscovery()) +
      Convert.ToUInt16(IsSetRawPrivateKeyToStaticPublicKey()) +
      Convert.ToUInt16(IsSetEphemeralPrivateKeyToStaticPublicKey());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
