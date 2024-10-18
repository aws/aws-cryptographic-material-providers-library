// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class UpdateMutationIndexInput
  {
    private AWS.Cryptography.KeyStore.MutationIndex _mutationIndex;
    private AWS.Cryptography.KeyStore.MutationIndex _oldMutationIndex;
    public AWS.Cryptography.KeyStore.MutationIndex MutationIndex
    {
      get { return this._mutationIndex; }
      set { this._mutationIndex = value; }
    }
    public bool IsSetMutationIndex()
    {
      return this._mutationIndex != null;
    }
    public AWS.Cryptography.KeyStore.MutationIndex OldMutationIndex
    {
      get { return this._oldMutationIndex; }
      set { this._oldMutationIndex = value; }
    }
    public bool IsSetOldMutationIndex()
    {
      return this._oldMutationIndex != null;
    }
    public void Validate()
    {
      if (!IsSetMutationIndex()) throw new System.ArgumentException("Missing value for required property 'MutationIndex'");
      if (!IsSetOldMutationIndex()) throw new System.ArgumentException("Missing value for required property 'OldMutationIndex'");

    }
  }
}
