// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class DeleteMutationInput
  {
    private AWS.Cryptography.KeyStore.MutationCommitment _mutationCommitment;
    public AWS.Cryptography.KeyStore.MutationCommitment MutationCommitment
    {
      get { return this._mutationCommitment; }
      set { this._mutationCommitment = value; }
    }
    public bool IsSetMutationCommitment()
    {
      return this._mutationCommitment != null;
    }
    public void Validate()
    {
      if (!IsSetMutationCommitment()) throw new System.ArgumentException("Missing value for required property 'MutationCommitment'");

    }
  }
}
