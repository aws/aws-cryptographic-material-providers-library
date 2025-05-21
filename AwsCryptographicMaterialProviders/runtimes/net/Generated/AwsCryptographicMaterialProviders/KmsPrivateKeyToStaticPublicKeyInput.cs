// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class KmsPrivateKeyToStaticPublicKeyInput
  {
    private string _senderKmsIdentifier;
    private System.IO.MemoryStream _senderPublicKey;
    private System.IO.MemoryStream _recipientPublicKey;
    public string SenderKmsIdentifier
    {
      get { return this._senderKmsIdentifier; }
      set { this._senderKmsIdentifier = value; }
    }
    public bool IsSetSenderKmsIdentifier()
    {
      return this._senderKmsIdentifier != null;
    }
    public System.IO.MemoryStream SenderPublicKey
    {
      get { return this._senderPublicKey; }
      set { this._senderPublicKey = value; }
    }
    public bool IsSetSenderPublicKey()
    {
      return this._senderPublicKey != null;
    }
    public System.IO.MemoryStream RecipientPublicKey
    {
      get { return this._recipientPublicKey; }
      set { this._recipientPublicKey = value; }
    }
    public bool IsSetRecipientPublicKey()
    {
      return this._recipientPublicKey != null;
    }
    public void Validate()
    {
      if (!IsSetSenderKmsIdentifier()) throw new System.ArgumentException("Missing value for required property 'SenderKmsIdentifier'");
      if (!IsSetRecipientPublicKey()) throw new System.ArgumentException("Missing value for required property 'RecipientPublicKey'");

    }
  }
}
