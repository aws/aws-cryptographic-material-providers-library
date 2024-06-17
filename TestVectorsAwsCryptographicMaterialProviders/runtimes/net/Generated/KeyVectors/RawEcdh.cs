// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProvidersTestVectorKeys;
namespace AWS.Cryptography.MaterialProvidersTestVectorKeys
{
  public class RawEcdh
  {
    private string _senderKeyId;
    private string _recipientKeyId;
    private string _providerId;
    private string _curveSpec;
    private string _keyAgreementScheme;
    public string SenderKeyId
    {
      get { return this._senderKeyId; }
      set { this._senderKeyId = value; }
    }
    public bool IsSetSenderKeyId()
    {
      return this._senderKeyId != null;
    }
    public string RecipientKeyId
    {
      get { return this._recipientKeyId; }
      set { this._recipientKeyId = value; }
    }
    public bool IsSetRecipientKeyId()
    {
      return this._recipientKeyId != null;
    }
    public string ProviderId
    {
      get { return this._providerId; }
      set { this._providerId = value; }
    }
    public bool IsSetProviderId()
    {
      return this._providerId != null;
    }
    public string CurveSpec
    {
      get { return this._curveSpec; }
      set { this._curveSpec = value; }
    }
    public bool IsSetCurveSpec()
    {
      return this._curveSpec != null;
    }
    public string KeyAgreementScheme
    {
      get { return this._keyAgreementScheme; }
      set { this._keyAgreementScheme = value; }
    }
    public bool IsSetKeyAgreementScheme()
    {
      return this._keyAgreementScheme != null;
    }
    public void Validate()
    {
      if (!IsSetSenderKeyId()) throw new System.ArgumentException("Missing value for required property 'SenderKeyId'");
      if (!IsSetRecipientKeyId()) throw new System.ArgumentException("Missing value for required property 'RecipientKeyId'");
      if (!IsSetProviderId()) throw new System.ArgumentException("Missing value for required property 'ProviderId'");
      if (!IsSetCurveSpec()) throw new System.ArgumentException("Missing value for required property 'CurveSpec'");
      if (!IsSetKeyAgreementScheme()) throw new System.ArgumentException("Missing value for required property 'KeyAgreementScheme'");

    }
  }
}
