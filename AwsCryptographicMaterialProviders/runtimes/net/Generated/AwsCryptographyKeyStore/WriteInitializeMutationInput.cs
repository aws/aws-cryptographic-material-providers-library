// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class WriteInitializeMutationInput
  {
    private AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey _active;
    private AWS.Cryptography.KeyStore.WriteInitializeMutationVersion _version;
    private AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey _beacon;
    private AWS.Cryptography.KeyStore.MutationCommitment _mutationCommitment;
    private AWS.Cryptography.KeyStore.MutationIndex _mutationIndex;
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
    public void Validate()
    {
      if (!IsSetActive()) throw new System.ArgumentException("Missing value for required property 'Active'");
      if (!IsSetVersion()) throw new System.ArgumentException("Missing value for required property 'Version'");
      if (!IsSetBeacon()) throw new System.ArgumentException("Missing value for required property 'Beacon'");
      if (!IsSetMutationCommitment()) throw new System.ArgumentException("Missing value for required property 'MutationCommitment'");
      if (!IsSetMutationIndex()) throw new System.ArgumentException("Missing value for required property 'MutationIndex'");

    }
  }
}
