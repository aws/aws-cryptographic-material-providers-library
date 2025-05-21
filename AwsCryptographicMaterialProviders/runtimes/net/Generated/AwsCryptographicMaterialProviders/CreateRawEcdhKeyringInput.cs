// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class CreateRawEcdhKeyringInput
  {
    private AWS.Cryptography.MaterialProviders.RawEcdhStaticConfigurations _keyAgreementScheme;
    private AWS.Cryptography.Primitives.ECDHCurveSpec _curveSpec;
    public AWS.Cryptography.MaterialProviders.RawEcdhStaticConfigurations KeyAgreementScheme
    {
      get { return this._keyAgreementScheme; }
      set { this._keyAgreementScheme = value; }
    }
    public bool IsSetKeyAgreementScheme()
    {
      return this._keyAgreementScheme != null;
    }
    public AWS.Cryptography.Primitives.ECDHCurveSpec CurveSpec
    {
      get { return this._curveSpec; }
      set { this._curveSpec = value; }
    }
    public bool IsSetCurveSpec()
    {
      return this._curveSpec != null;
    }
    public void Validate()
    {
      if (!IsSetKeyAgreementScheme()) throw new System.ArgumentException("Missing value for required property 'KeyAgreementScheme'");
      if (!IsSetCurveSpec()) throw new System.ArgumentException("Missing value for required property 'CurveSpec'");

    }
  }
}
