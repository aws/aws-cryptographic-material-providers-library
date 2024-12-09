// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class AwsKms
  {
    private System.Collections.Generic.List<string> _grantTokens;
    private Amazon.KeyManagementService.IAmazonKeyManagementService _kmsClient;
    public System.Collections.Generic.List<string> GrantTokens
    {
      get { return this._grantTokens; }
      set { this._grantTokens = value; }
    }
    public bool IsSetGrantTokens()
    {
      return this._grantTokens != null;
    }
    public Amazon.KeyManagementService.IAmazonKeyManagementService KmsClient
    {
      get { return this._kmsClient; }
      set { this._kmsClient = value; }
    }
    public bool IsSetKmsClient()
    {
      return this._kmsClient != null;
    }
    public void Validate()
    {

    }
  }
}
