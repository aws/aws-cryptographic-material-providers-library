// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class WriteInitializeMutationInput
  {
    private AWS.Cryptography.KeyStore.EncryptedHierarchicalKey _active;
    private AWS.Cryptography.KeyStore.EncryptedHierarchicalKey _oldActive;
    private AWS.Cryptography.KeyStore.EncryptedHierarchicalKey _version;
    private AWS.Cryptography.KeyStore.EncryptedHierarchicalKey _beacon;
    private AWS.Cryptography.KeyStore.MutationLock _mutationLock;
    public AWS.Cryptography.KeyStore.EncryptedHierarchicalKey Active
    {
      get { return this._active; }
      set { this._active = value; }
    }
    public bool IsSetActive()
    {
      return this._active != null;
    }
    public AWS.Cryptography.KeyStore.EncryptedHierarchicalKey OldActive
    {
      get { return this._oldActive; }
      set { this._oldActive = value; }
    }
    public bool IsSetOldActive()
    {
      return this._oldActive != null;
    }
    public AWS.Cryptography.KeyStore.EncryptedHierarchicalKey Version
    {
      get { return this._version; }
      set { this._version = value; }
    }
    public bool IsSetVersion()
    {
      return this._version != null;
    }
    public AWS.Cryptography.KeyStore.EncryptedHierarchicalKey Beacon
    {
      get { return this._beacon; }
      set { this._beacon = value; }
    }
    public bool IsSetBeacon()
    {
      return this._beacon != null;
    }
    public AWS.Cryptography.KeyStore.MutationLock MutationLock
    {
      get { return this._mutationLock; }
      set { this._mutationLock = value; }
    }
    public bool IsSetMutationLock()
    {
      return this._mutationLock != null;
    }
    public void Validate()
    {
      if (!IsSetActive()) throw new System.ArgumentException("Missing value for required property 'Active'");
      if (!IsSetOldActive()) throw new System.ArgumentException("Missing value for required property 'OldActive'");
      if (!IsSetVersion()) throw new System.ArgumentException("Missing value for required property 'Version'");
      if (!IsSetBeacon()) throw new System.ArgumentException("Missing value for required property 'Beacon'");
      if (!IsSetMutationLock()) throw new System.ArgumentException("Missing value for required property 'MutationLock'");

    }
  }
}
