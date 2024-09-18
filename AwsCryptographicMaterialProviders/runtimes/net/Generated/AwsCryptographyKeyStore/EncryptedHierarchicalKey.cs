// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class EncryptedHierarchicalKey
  {
    private string _identifier;
    private AWS.Cryptography.KeyStore.HierarchicalKeyType _type;
    private string _createTime;
    private string _kmsArn;
    private System.Collections.Generic.Dictionary<string, string> _encryptionContext;
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
    public AWS.Cryptography.KeyStore.HierarchicalKeyType Type
    {
      get { return this._type; }
      set { this._type = value; }
    }
    public bool IsSetType()
    {
      return this._type != null;
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
    public string KmsArn
    {
      get { return this._kmsArn; }
      set { this._kmsArn = value; }
    }
    public bool IsSetKmsArn()
    {
      return this._kmsArn != null;
    }
    public System.Collections.Generic.Dictionary<string, string> EncryptionContext
    {
      get { return this._encryptionContext; }
      set { this._encryptionContext = value; }
    }
    public bool IsSetEncryptionContext()
    {
      return this._encryptionContext != null;
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
      if (!IsSetType()) throw new System.ArgumentException("Missing value for required property 'Type'");
      if (!IsSetCreateTime()) throw new System.ArgumentException("Missing value for required property 'CreateTime'");
      if (!IsSetKmsArn()) throw new System.ArgumentException("Missing value for required property 'KmsArn'");
      if (!IsSetEncryptionContext()) throw new System.ArgumentException("Missing value for required property 'EncryptionContext'");
      if (!IsSetCiphertextBlob()) throw new System.ArgumentException("Missing value for required property 'CiphertextBlob'");

    }
  }
}
