// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class MutationToken
  {
    private string _identifier;
    private System.IO.MemoryStream _original;
    private System.IO.MemoryStream _terminal;
    private System.IO.MemoryStream _exclusiveStartKey;
    private string _uUID;
    private string _createTime;
    public string Identifier
    {
      get { return this._identifier; }
      set { this._identifier = value; }
    }
    public bool IsSetIdentifier()
    {
      return this._identifier != null;
    }
    public System.IO.MemoryStream Original
    {
      get { return this._original; }
      set { this._original = value; }
    }
    public bool IsSetOriginal()
    {
      return this._original != null;
    }
    public System.IO.MemoryStream Terminal
    {
      get { return this._terminal; }
      set { this._terminal = value; }
    }
    public bool IsSetTerminal()
    {
      return this._terminal != null;
    }
    public System.IO.MemoryStream ExclusiveStartKey
    {
      get { return this._exclusiveStartKey; }
      set { this._exclusiveStartKey = value; }
    }
    public bool IsSetExclusiveStartKey()
    {
      return this._exclusiveStartKey != null;
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
    public string CreateTime
    {
      get { return this._createTime; }
      set { this._createTime = value; }
    }
    public bool IsSetCreateTime()
    {
      return this._createTime != null;
    }
    public void Validate()
    {
      if (!IsSetIdentifier()) throw new System.ArgumentException("Missing value for required property 'Identifier'");
      if (!IsSetOriginal()) throw new System.ArgumentException("Missing value for required property 'Original'");
      if (!IsSetTerminal()) throw new System.ArgumentException("Missing value for required property 'Terminal'");
      if (!IsSetCreateTime()) throw new System.ArgumentException("Missing value for required property 'CreateTime'");

    }
  }
}
