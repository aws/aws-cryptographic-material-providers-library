// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class KmsSenderToStaticRecipientInput
  {
    private string _senderKmsIdentifier;
    private AWS.Cryptography.MaterialProviders.KmsRecipientConfiguration _recipientConfiguration;
    public string SenderKmsIdentifier
    {
      get { return this._senderKmsIdentifier; }
      set { this._senderKmsIdentifier = value; }
    }
    public bool IsSetSenderKmsIdentifier()
    {
      return this._senderKmsIdentifier != null;
    }
    public AWS.Cryptography.MaterialProviders.KmsRecipientConfiguration RecipientConfiguration
    {
      get { return this._recipientConfiguration; }
      set { this._recipientConfiguration = value; }
    }
    public bool IsSetRecipientConfiguration()
    {
      return this._recipientConfiguration != null;
    }
    public void Validate()
    {
      if (!IsSetSenderKmsIdentifier()) throw new System.ArgumentException("Missing value for required property 'SenderKmsIdentifier'");
      if (!IsSetRecipientConfiguration()) throw new System.ArgumentException("Missing value for required property 'RecipientConfiguration'");

    }
  }
}
