// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class PublicKeyDiscoveryInput
  {
    private System.IO.MemoryStream _recipientStaticPrivateKey;
    public System.IO.MemoryStream RecipientStaticPrivateKey
    {
      get { return this._recipientStaticPrivateKey; }
      set { this._recipientStaticPrivateKey = value; }
    }
    public bool IsSetRecipientStaticPrivateKey()
    {
      return this._recipientStaticPrivateKey != null;
    }
    public void Validate()
    {
      if (!IsSetRecipientStaticPrivateKey()) throw new System.ArgumentException("Missing value for required property 'RecipientStaticPrivateKey'");

    }
  }
}
