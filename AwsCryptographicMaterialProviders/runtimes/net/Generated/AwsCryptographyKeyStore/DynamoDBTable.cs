// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class DynamoDBTable
  {
    private string _ddbTableName;
    private Amazon.DynamoDBv2.IAmazonDynamoDB _ddbClient;
    public string DdbTableName
    {
      get { return this._ddbTableName; }
      set { this._ddbTableName = value; }
    }
    public bool IsSetDdbTableName()
    {
      return this._ddbTableName != null;
    }
    public Amazon.DynamoDBv2.IAmazonDynamoDB DdbClient
    {
      get { return this._ddbClient; }
      set { this._ddbClient = value; }
    }
    public bool IsSetDdbClient()
    {
      return this._ddbClient != null;
    }
    public void Validate()
    {
      if (!IsSetDdbTableName()) throw new System.ArgumentException("Missing value for required property 'DdbTableName'");

    }
  }
}
