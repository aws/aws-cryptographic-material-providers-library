// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class StaticDiscoveryRecipientInput
  {
    private System.IO.MemoryStream _senderStaticPrivateKey;
    public System.IO.MemoryStream SenderStaticPrivateKey
    {
      get { return this._senderStaticPrivateKey; }
      set { this._senderStaticPrivateKey = value; }
    }
    public bool IsSetSenderStaticPrivateKey()
    {
      return this._senderStaticPrivateKey != null;
    }
    public void Validate()
    {
      if (!IsSetSenderStaticPrivateKey()) throw new System.ArgumentException("Missing value for required property 'SenderStaticPrivateKey'");

    }
  }
}
