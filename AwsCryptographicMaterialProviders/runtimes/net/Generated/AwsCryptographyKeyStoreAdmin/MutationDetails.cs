// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class MutationDetails
  {
    private AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyContext _original;
    private AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyContext _terminal;
    private AWS.Cryptography.KeyStoreAdmin.Mutations _input;
    private string _systemKey;
    private string _createTime;
    private string _uUID;
    public AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyContext Original
    {
      get { return this._original; }
      set { this._original = value; }
    }
    public bool IsSetOriginal()
    {
      return this._original != null;
    }
    public AWS.Cryptography.KeyStoreAdmin.MutableBranchKeyContext Terminal
    {
      get { return this._terminal; }
      set { this._terminal = value; }
    }
    public bool IsSetTerminal()
    {
      return this._terminal != null;
    }
    public AWS.Cryptography.KeyStoreAdmin.Mutations Input
    {
      get { return this._input; }
      set { this._input = value; }
    }
    public bool IsSetInput()
    {
      return this._input != null;
    }
    public string SystemKey
    {
      get { return this._systemKey; }
      set { this._systemKey = value; }
    }
    public bool IsSetSystemKey()
    {
      return this._systemKey != null;
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
    public void Validate()
    {
      if (!IsSetOriginal()) throw new System.ArgumentException("Missing value for required property 'Original'");
      if (!IsSetTerminal()) throw new System.ArgumentException("Missing value for required property 'Terminal'");
      if (!IsSetInput()) throw new System.ArgumentException("Missing value for required property 'Input'");
      if (!IsSetSystemKey()) throw new System.ArgumentException("Missing value for required property 'SystemKey'");
      if (!IsSetCreateTime()) throw new System.ArgumentException("Missing value for required property 'CreateTime'");
      if (!IsSetUUID()) throw new System.ArgumentException("Missing value for required property 'UUID'");

    }
  }
}
