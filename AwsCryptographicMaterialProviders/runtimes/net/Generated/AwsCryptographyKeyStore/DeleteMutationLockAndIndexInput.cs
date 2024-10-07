// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class DeleteMutationLockAndIndexInput
  {
    private AWS.Cryptography.KeyStore.MutationLock _mutationLock;
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
      if (!IsSetMutationLock()) throw new System.ArgumentException("Missing value for required property 'MutationLock'");

    }
  }
}
