// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class CreateAwsKmsEcdhKeyringInput
  {
    private AWS.Cryptography.MaterialProviders.KmsEcdhStaticConfigurations _keyAgreementScheme;
    private AWS.Cryptography.Primitives.ECDHCurveSpec _curveSpec;
    private Amazon.KeyManagementService.IAmazonKeyManagementService _kmsClient;
    private System.Collections.Generic.List<string> _grantTokens;
    public AWS.Cryptography.MaterialProviders.KmsEcdhStaticConfigurations KeyAgreementScheme
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
    public Amazon.KeyManagementService.IAmazonKeyManagementService KmsClient
    {
      get { return this._kmsClient; }
      set { this._kmsClient = value; }
    }
    public bool IsSetKmsClient()
    {
      return this._kmsClient != null;
    }
    public System.Collections.Generic.List<string> GrantTokens
    {
      get { return this._grantTokens; }
      set { this._grantTokens = value; }
    }
    public bool IsSetGrantTokens()
    {
      return this._grantTokens != null;
    }
    public void Validate()
    {
      if (!IsSetKeyAgreementScheme()) throw new System.ArgumentException("Missing value for required property 'KeyAgreementScheme'");
      if (!IsSetCurveSpec()) throw new System.ArgumentException("Missing value for required property 'CurveSpec'");
      if (!IsSetKmsClient()) throw new System.ArgumentException("Missing value for required property 'KmsClient'");

    }
  }
}
