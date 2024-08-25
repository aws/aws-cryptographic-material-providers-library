// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class KMSRelationship
  {
    private Amazon.KeyManagementService.IAmazonKeyManagementService _reEncrypt;
    public Amazon.KeyManagementService.IAmazonKeyManagementService ReEncrypt
    {
      get { return this._reEncrypt; }
      set { this._reEncrypt = value; }
    }
    public bool IsSetReEncrypt()
    {
      return this._reEncrypt != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetReEncrypt());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
