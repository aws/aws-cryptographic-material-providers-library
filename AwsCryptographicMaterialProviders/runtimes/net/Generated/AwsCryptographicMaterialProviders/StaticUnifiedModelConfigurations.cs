// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class StaticUnifiedModelConfigurations
  {
    private AWS.Cryptography.MaterialProviders.KmsEcdhConfigurations _aWS_KMS_ECDH;
    private AWS.Cryptography.MaterialProviders.RawEcdhConfigurations _rAW_ECDH;
    public AWS.Cryptography.MaterialProviders.KmsEcdhConfigurations AWS__KMS__ECDH
    {
      get { return this._aWS_KMS_ECDH; }
      set { this._aWS_KMS_ECDH = value; }
    }
    public bool IsSetAWS__KMS__ECDH()
    {
      return this._aWS_KMS_ECDH != null;
    }
    public AWS.Cryptography.MaterialProviders.RawEcdhConfigurations RAW__ECDH
    {
      get { return this._rAW_ECDH; }
      set { this._rAW_ECDH = value; }
    }
    public bool IsSetRAW__ECDH()
    {
      return this._rAW_ECDH != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetAWS__KMS__ECDH()) +
      Convert.ToUInt16(IsSetRAW__ECDH());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
