// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class KmsRecipientConfiguration
  {
    private string _recipientKmsKeyId;
    private System.IO.MemoryStream _recipientPublicKey;
    public string RecipientKmsKeyId
    {
      get { return this._recipientKmsKeyId; }
      set { this._recipientKmsKeyId = value; }
    }
    public bool IsSetRecipientKmsKeyId()
    {
      return this._recipientKmsKeyId != null;
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
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetRecipientKmsKeyId()) +
      Convert.ToUInt16(IsSetRecipientPublicKey());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
