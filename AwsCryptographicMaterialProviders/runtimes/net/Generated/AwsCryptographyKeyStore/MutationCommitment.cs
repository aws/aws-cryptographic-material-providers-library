// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class MutationCommitment
  {
    private string _identifier;
    private string _createTime;
    private string _uUID;
    private System.IO.MemoryStream _original;
    private System.IO.MemoryStream _terminal;
    private System.IO.MemoryStream _input;
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
    public System.IO.MemoryStream Input
    {
      get { return this._input; }
      set { this._input = value; }
    }
    public bool IsSetInput()
    {
      return this._input != null;
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
      if (!IsSetOriginal()) throw new System.ArgumentException("Missing value for required property 'Original'");
      if (!IsSetTerminal()) throw new System.ArgumentException("Missing value for required property 'Terminal'");
      if (!IsSetInput()) throw new System.ArgumentException("Missing value for required property 'Input'");
      if (!IsSetCiphertextBlob()) throw new System.ArgumentException("Missing value for required property 'CiphertextBlob'");

    }
  }
}
