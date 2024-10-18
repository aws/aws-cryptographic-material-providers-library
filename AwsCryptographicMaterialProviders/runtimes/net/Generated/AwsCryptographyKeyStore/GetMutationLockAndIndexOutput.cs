// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class GetMutationLockAndIndexOutput
  {
    private AWS.Cryptography.KeyStore.MutationLock _mutationLock;
    private AWS.Cryptography.KeyStore.MutationIndex _mutationIndex;
    public AWS.Cryptography.KeyStore.MutationLock MutationLock
    {
      get { return this._mutationLock; }
      set { this._mutationLock = value; }
    }
    public bool IsSetMutationLock()
    {
      return this._mutationLock != null;
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

    }
  }
}
