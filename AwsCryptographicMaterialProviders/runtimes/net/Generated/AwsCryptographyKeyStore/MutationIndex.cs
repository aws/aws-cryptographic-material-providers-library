// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class MutationIndex
  {
    private string _identifier;
    private string _createTime;
    private string _uUID;
    private System.IO.MemoryStream _pageIndex;
    private System.IO.MemoryStream _enc;
    public string Identifier
    {
      get { return this._identifier; }
      set { this._identifier = value; }
    }
    public bool IsSetIdentifier()
    {
      return this._identifier != null;
    }
    public string CreateTime
    {
      get { return this._createTime; }
      set { this._createTime = value; }
    }
    public bool IsSetCreateTime()
    {
      return this._createTime != null;
    }
    public string UUID
    {
      get { return this._uUID; }
      set { this._uUID = value; }
    }
    public bool IsSetUUID()
    {
      return this._uUID != null;
    }
    public System.IO.MemoryStream PageIndex
    {
      get { return this._pageIndex; }
      set { this._pageIndex = value; }
    }
    public bool IsSetPageIndex()
    {
      return this._pageIndex != null;
    }
    public System.IO.MemoryStream Enc
    {
      get { return this._enc; }
      set { this._enc = value; }
    }
    public bool IsSetEnc()
    {
      return this._enc != null;
    }
    public void Validate()
    {
      if (!IsSetIdentifier()) throw new System.ArgumentException("Missing value for required property 'Identifier'");
      if (!IsSetCreateTime()) throw new System.ArgumentException("Missing value for required property 'CreateTime'");
      if (!IsSetUUID()) throw new System.ArgumentException("Missing value for required property 'UUID'");
      if (!IsSetPageIndex()) throw new System.ArgumentException("Missing value for required property 'PageIndex'");
      if (!IsSetEnc()) throw new System.ArgumentException("Missing value for required property 'Enc'");

    }
  }
}
