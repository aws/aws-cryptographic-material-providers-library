// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class RawEcdhConfigurations
  {
    private AWS.Cryptography.MaterialProviders.StaticDiscoveryRecipientInput _staticDiscoveryRecipient;
    private AWS.Cryptography.MaterialProviders.StaticSenderStaticRecipientInput _staticSenderStaticRecipient;
    private AWS.Cryptography.MaterialProviders.EphemeralSenderToStaticRecipientInput _ephemeralSenderToStaticKmsRecipient;
    public AWS.Cryptography.MaterialProviders.StaticDiscoveryRecipientInput StaticDiscoveryRecipient
    {
      get { return this._staticDiscoveryRecipient; }
      set { this._staticDiscoveryRecipient = value; }
    }
    public bool IsSetStaticDiscoveryRecipient()
    {
      return this._staticDiscoveryRecipient != null;
    }
    public AWS.Cryptography.MaterialProviders.StaticSenderStaticRecipientInput StaticSenderStaticRecipient
    {
      get { return this._staticSenderStaticRecipient; }
      set { this._staticSenderStaticRecipient = value; }
    }
    public bool IsSetStaticSenderStaticRecipient()
    {
      return this._staticSenderStaticRecipient != null;
    }
    public AWS.Cryptography.MaterialProviders.EphemeralSenderToStaticRecipientInput EphemeralSenderToStaticKmsRecipient
    {
      get { return this._ephemeralSenderToStaticKmsRecipient; }
      set { this._ephemeralSenderToStaticKmsRecipient = value; }
    }
    public bool IsSetEphemeralSenderToStaticKmsRecipient()
    {
      return this._ephemeralSenderToStaticKmsRecipient != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetStaticDiscoveryRecipient()) +
      Convert.ToUInt16(IsSetStaticSenderStaticRecipient()) +
      Convert.ToUInt16(IsSetEphemeralSenderToStaticKmsRecipient());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
