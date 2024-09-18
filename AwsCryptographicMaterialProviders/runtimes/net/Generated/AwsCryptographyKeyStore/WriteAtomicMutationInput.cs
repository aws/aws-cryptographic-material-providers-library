// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class WriteAtomicMutationInput
  {
    private AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey _active;
    private AWS.Cryptography.KeyStore.WriteInitializeMutationVersion _version;
    private AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey _beacon;
    private System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey> _items;
    public AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey Active
    {
      get { return this._active; }
      set { this._active = value; }
    }
    public bool IsSetActive()
    {
      return this._active != null;
    }
    public AWS.Cryptography.KeyStore.WriteInitializeMutationVersion Version
    {
      get { return this._version; }
      set { this._version = value; }
    }
    public bool IsSetVersion()
    {
      return this._version != null;
    }
    public AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey Beacon
    {
      get { return this._beacon; }
      set { this._beacon = value; }
    }
    public bool IsSetBeacon()
    {
      return this._beacon != null;
    }
    public System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey> Items
    {
      get { return this._items; }
      set { this._items = value; }
    }
    public bool IsSetItems()
    {
      return this._items != null;
    }
    public void Validate()
    {
      if (!IsSetActive()) throw new System.ArgumentException("Missing value for required property 'Active'");
      if (!IsSetVersion()) throw new System.ArgumentException("Missing value for required property 'Version'");
      if (!IsSetBeacon()) throw new System.ArgumentException("Missing value for required property 'Beacon'");
      if (!IsSetItems()) throw new System.ArgumentException("Missing value for required property 'Items'");

    }
  }
}
