// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class KmsEcdhConfigurations
  {
    private AWS.Cryptography.MaterialProviders.RecipientDiscoverySchemeInput _recipientDiscoveryScheme;
    private AWS.Cryptography.MaterialProviders.KmsSenderToStaticRecipientInput _kmsSenderToStaticRecipient;
    public AWS.Cryptography.MaterialProviders.RecipientDiscoverySchemeInput RecipientDiscoveryScheme
    {
      get { return this._recipientDiscoveryScheme; }
      set { this._recipientDiscoveryScheme = value; }
    }
    public bool IsSetRecipientDiscoveryScheme()
    {
      return this._recipientDiscoveryScheme != null;
    }
    public AWS.Cryptography.MaterialProviders.KmsSenderToStaticRecipientInput KmsSenderToStaticRecipient
    {
      get { return this._kmsSenderToStaticRecipient; }
      set { this._kmsSenderToStaticRecipient = value; }
    }
    public bool IsSetKmsSenderToStaticRecipient()
    {
      return this._kmsSenderToStaticRecipient != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetRecipientDiscoveryScheme()) +
      Convert.ToUInt16(IsSetKmsSenderToStaticRecipient());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
