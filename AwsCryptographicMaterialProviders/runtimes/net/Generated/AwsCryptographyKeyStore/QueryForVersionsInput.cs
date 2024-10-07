// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class QueryForVersionsInput
  {
    private System.IO.MemoryStream _pageIndex;
    private string _identifier;
    private int? _pageSize;
    public System.IO.MemoryStream PageIndex
    {
      get { return this._pageIndex; }
      set { this._pageIndex = value; }
    }
    public bool IsSetPageIndex()
    {
      return this._pageIndex != null;
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
