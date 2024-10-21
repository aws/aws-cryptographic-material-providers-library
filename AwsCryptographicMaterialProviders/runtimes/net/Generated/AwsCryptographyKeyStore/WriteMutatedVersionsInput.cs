// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class WriteMutatedVersionsInput
  {
    private System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey> _items;
    private AWS.Cryptography.KeyStore.MutationCommitment _mutationCommitment;
    private AWS.Cryptography.KeyStore.OverWriteMutationIndex _mutationIndex;
    private bool? _endMutation;
    public System.Collections.Generic.List<AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey> Items
    {
      get { return this._items; }
      set { this._items = value; }
    }
    public bool IsSetItems()
    {
      return this._items != null;
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
    public AWS.Cryptography.KeyStore.OverWriteMutationIndex MutationIndex
    {
      get { return this._mutationIndex; }
      set { this._mutationIndex = value; }
    }
    public bool IsSetMutationIndex()
    {
      return this._mutationIndex != null;
    }
    public bool EndMutation
    {
      get { return this._endMutation.GetValueOrDefault(); }
      set { this._endMutation = value; }
    }
    public bool IsSetEndMutation()
    {
      return this._endMutation.HasValue;
    }
    public void Validate()
    {
      if (!IsSetItems()) throw new System.ArgumentException("Missing value for required property 'Items'");
      if (!IsSetMutationCommitment()) throw new System.ArgumentException("Missing value for required property 'MutationCommitment'");
      if (!IsSetMutationIndex()) throw new System.ArgumentException("Missing value for required property 'MutationIndex'");
      if (!IsSetEndMutation()) throw new System.ArgumentException("Missing value for required property 'EndMutation'");

    }
  }
}
