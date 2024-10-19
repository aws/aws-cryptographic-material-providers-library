// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class WriteInitializeMutationInput
  {
    private AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey _beacon;
    private AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey _active;
    private AWS.Cryptography.KeyStore.EncryptedHierarchicalKey _version;
    private AWS.Cryptography.KeyStore.MutationCommitment _mutationCommitment;
    private AWS.Cryptography.KeyStore.MutationIndex _mutationIndex;
    private AWS.Cryptography.KeyStore.OverWriteMutationIndex _overWriteMutationIndex;
    private System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey> _versions;
    public AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey Beacon
    {
      get { return this._beacon; }
      set { this._beacon = value; }
    }
    public bool IsSetBeacon()
    {
      return this._beacon != null;
    }
    public AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey Active
    {
      get { return this._active; }
      set { this._active = value; }
    }
    public bool IsSetActive()
    {
      return this._active != null;
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
    public AWS.Cryptography.KeyStore.MutationCommitment MutationCommitment
    {
      get { return this._mutationCommitment; }
      set { this._mutationCommitment = value; }
    }
    public bool IsSetMutationCommitment()
    {
      return this._mutationCommitment != null;
    }
    public AWS.Cryptography.KeyStore.MutationIndex MutationIndex
    {
      get { return this._mutationIndex; }
      set { this._mutationIndex = value; }
    }
    public bool IsSetMutationIndex()
    {
      return this._mutationIndex != null;
    }
    public AWS.Cryptography.KeyStore.OverWriteMutationIndex OverWriteMutationIndex
    {
      get { return this._overWriteMutationIndex; }
      set { this._overWriteMutationIndex = value; }
    }
    public bool IsSetOverWriteMutationIndex()
    {
      return this._overWriteMutationIndex != null;
    }
    public System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey> Versions
    {
      get { return this._versions; }
      set { this._versions = value; }
    }
    public bool IsSetVersions()
    {
      return this._versions != null;
    }
    public void Validate()
    {
      if (!IsSetBeacon()) throw new System.ArgumentException("Missing value for required property 'Beacon'");
      if (!IsSetVersions()) throw new System.ArgumentException("Missing value for required property 'Versions'");

    }
  }
}
