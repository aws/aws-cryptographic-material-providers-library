// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class GetItemsForInitializeMutationOutput
  {
    private AWS.Cryptography.KeyStore.EncryptedHierarchicalKey _activeItem;
    private AWS.Cryptography.KeyStore.EncryptedHierarchicalKey _beaconItem;
    private AWS.Cryptography.KeyStore.MutationCommitment _mutationCommitment;
    private AWS.Cryptography.KeyStore.MutationIndex _mutationIndex;
    public AWS.Cryptography.KeyStore.EncryptedHierarchicalKey ActiveItem
    {
      get { return this._activeItem; }
      set { this._activeItem = value; }
    }
    public bool IsSetActiveItem()
    {
      return this._activeItem != null;
    }
    public AWS.Cryptography.KeyStore.EncryptedHierarchicalKey BeaconItem
    {
      get { return this._beaconItem; }
      set { this._beaconItem = value; }
    }
    public bool IsSetBeaconItem()
    {
      return this._beaconItem != null;
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
      if (!IsSetActiveItem()) throw new System.ArgumentException("Missing value for required property 'ActiveItem'");
      if (!IsSetBeaconItem()) throw new System.ArgumentException("Missing value for required property 'BeaconItem'");

    }
  }
}
