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
    private string _lastModifiedTime;
    private System.IO.MemoryStream _ciphertextBlob;
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
    public string LastModifiedTime
    {
      get { return this._lastModifiedTime; }
      set { this._lastModifiedTime = value; }
    }
    public bool IsSetLastModifiedTime()
    {
      return this._lastModifiedTime != null;
    }
    public System.IO.MemoryStream CiphertextBlob
    {
      get { return this._ciphertextBlob; }
      set { this._ciphertextBlob = value; }
    }
    public bool IsSetCiphertextBlob()
    {
      return this._ciphertextBlob != null;
    }
    public void Validate()
    {
      if (!IsSetIdentifier()) throw new System.ArgumentException("Missing value for required property 'Identifier'");
      if (!IsSetCreateTime()) throw new System.ArgumentException("Missing value for required property 'CreateTime'");
      if (!IsSetUUID()) throw new System.ArgumentException("Missing value for required property 'UUID'");
      if (!IsSetPageIndex()) throw new System.ArgumentException("Missing value for required property 'PageIndex'");
      if (!IsSetLastModifiedTime()) throw new System.ArgumentException("Missing value for required property 'LastModifiedTime'");
      if (!IsSetCiphertextBlob()) throw new System.ArgumentException("Missing value for required property 'CiphertextBlob'");

    }
  }
}
