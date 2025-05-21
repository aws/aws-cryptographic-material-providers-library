// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class KeyAgreementScheme
  {
    private AWS.Cryptography.MaterialProviders.StaticConfigurations _staticConfiguration;
    public AWS.Cryptography.MaterialProviders.StaticConfigurations StaticConfiguration
    {
      get { return this._staticConfiguration; }
      set { this._staticConfiguration = value; }
    }
    public bool IsSetStaticConfiguration()
    {
      return this._staticConfiguration != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetStaticConfiguration());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
