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
    private string _kmsMRKeyArn;
    public string KmsKeyArn
    {
      get { return this._kmsKeyArn; }
      set { this._kmsKeyArn = value; }
    }
    public bool IsSetKmsKeyArn()
    {
      return this._kmsKeyArn != null;
    }
    public string KmsMRKeyArn
    {
      get { return this._kmsMRKeyArn; }
      set { this._kmsMRKeyArn = value; }
    }
    public bool IsSetKmsMRKeyArn()
    {
      return this._kmsMRKeyArn != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetKmsKeyArn()) +
      Convert.ToUInt16(IsSetKmsMRKeyArn());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
