// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class WriteMutatedVersionsInput
  {
    private System.Collections.Generic.List<AWS.Cryptography.KeyStore.EncryptedHierarchicalKey> _items;
    private string _identifier;
    private System.IO.MemoryStream _original;
    private System.IO.MemoryStream _terminal;
    private bool? _completeMutation;
    public System.Collections.Generic.List<AWS.Cryptography.KeyStore.EncryptedHierarchicalKey> Items
    {
      get { return this._items; }
      set { this._items = value; }
    }
    public bool IsSetItems()
    {
      return this._items != null;
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
    public bool CompleteMutation
    {
      get { return this._completeMutation.GetValueOrDefault(); }
      set { this._completeMutation = value; }
    }
    public bool IsSetCompleteMutation()
    {
      return this._completeMutation.HasValue;
    }
    public void Validate()
    {
      if (!IsSetItems()) throw new System.ArgumentException("Missing value for required property 'Items'");
      if (!IsSetIdentifier()) throw new System.ArgumentException("Missing value for required property 'Identifier'");
      if (!IsSetOriginal()) throw new System.ArgumentException("Missing value for required property 'Original'");
      if (!IsSetTerminal()) throw new System.ArgumentException("Missing value for required property 'Terminal'");
      if (!IsSetCompleteMutation()) throw new System.ArgumentException("Missing value for required property 'CompleteMutation'");

    }
  }
}
