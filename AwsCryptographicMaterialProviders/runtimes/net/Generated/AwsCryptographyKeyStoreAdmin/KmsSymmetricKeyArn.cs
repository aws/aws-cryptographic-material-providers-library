// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class KmsSymmetricKeyArn
  {
    private string _kmsKeyArn;
    private AWS.Cryptography.KeyStoreAdmin.KmsMRKey _kmsMRKey;
    public string KmsKeyArn
    {
      get { return this._kmsKeyArn; }
      set { this._kmsKeyArn = value; }
    }
    public bool IsSetKmsKeyArn()
    {
      return this._kmsKeyArn != null;
    }
    public AWS.Cryptography.KeyStoreAdmin.KmsMRKey KmsMRKey
    {
      get { return this._kmsMRKey; }
      set { this._kmsMRKey = value; }
    }
    public bool IsSetKmsMRKey()
    {
      return this._kmsMRKey != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetKmsKeyArn()) +
      Convert.ToUInt16(IsSetKmsMRKey());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
