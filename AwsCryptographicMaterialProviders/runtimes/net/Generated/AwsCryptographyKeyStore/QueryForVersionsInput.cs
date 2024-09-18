// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class QueryForVersionsInput
  {
    private System.IO.MemoryStream _exclusiveStartKey;
    private string _identifier;
    private int? _pageSize;
    public System.IO.MemoryStream ExclusiveStartKey
    {
      get { return this._exclusiveStartKey; }
      set { this._exclusiveStartKey = value; }
    }
    public bool IsSetExclusiveStartKey()
    {
      return this._exclusiveStartKey != null;
    }
    public string Identifier
    {
      get { return this._identifier; }
      set { this._identifier = value; }
    }
    public bool IsSetIdentifier()
    {
      return this._identifier != null;
    }
    public int PageSize
    {
      get { return this._pageSize.GetValueOrDefault(); }
      set { this._pageSize = value; }
    }
    public bool IsSetPageSize()
    {
      return this._pageSize.HasValue;
    }
    public void Validate()
    {
      if (!IsSetIdentifier()) throw new System.ArgumentException("Missing value for required property 'Identifier'");
      if (!IsSetPageSize()) throw new System.ArgumentException("Missing value for required property 'PageSize'");

    }
  }
}
