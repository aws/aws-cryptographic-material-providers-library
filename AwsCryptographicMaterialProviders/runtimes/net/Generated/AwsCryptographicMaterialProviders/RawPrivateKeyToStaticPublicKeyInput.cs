// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class RawPrivateKeyToStaticPublicKeyInput
  {
    private System.IO.MemoryStream _senderStaticPrivateKey;
    private System.IO.MemoryStream _recipientPublicKey;
    public System.IO.MemoryStream SenderStaticPrivateKey
    {
      get { return this._senderStaticPrivateKey; }
      set { this._senderStaticPrivateKey = value; }
    }
    public bool IsSetSenderStaticPrivateKey()
    {
      return this._senderStaticPrivateKey != null;
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
      if (!IsSetSenderStaticPrivateKey()) throw new System.ArgumentException("Missing value for required property 'SenderStaticPrivateKey'");
      if (!IsSetRecipientPublicKey()) throw new System.ArgumentException("Missing value for required property 'RecipientPublicKey'");

    }
  }
}
