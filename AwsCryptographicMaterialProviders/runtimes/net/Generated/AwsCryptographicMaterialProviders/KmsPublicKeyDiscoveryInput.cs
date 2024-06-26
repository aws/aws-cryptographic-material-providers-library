// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class KmsPublicKeyDiscoveryInput
  {
    private string _recipientKmsIdentifier;
    public string RecipientKmsIdentifier
    {
      get { return this._recipientKmsIdentifier; }
      set { this._recipientKmsIdentifier = value; }
    }
    public bool IsSetRecipientKmsIdentifier()
    {
      return this._recipientKmsIdentifier != null;
    }
    public void Validate()
    {
      if (!IsSetRecipientKmsIdentifier()) throw new System.ArgumentException("Missing value for required property 'RecipientKmsIdentifier'");

    }
  }
}
