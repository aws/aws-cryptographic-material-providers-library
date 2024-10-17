// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class ApplyMutationResult
  {
    private AWS.Cryptography.KeyStoreAdmin.MutationToken _continueMutation;
    private AWS.Cryptography.KeyStoreAdmin.MutationComplete _completeMutation;
    public AWS.Cryptography.KeyStoreAdmin.MutationToken ContinueMutation
    {
      get { return this._continueMutation; }
      set { this._continueMutation = value; }
    }
    public bool IsSetContinueMutation()
    {
      return this._continueMutation != null;
    }
    public AWS.Cryptography.KeyStoreAdmin.MutationComplete CompleteMutation
    {
      get { return this._completeMutation; }
      set { this._completeMutation = value; }
    }
    public bool IsSetCompleteMutation()
    {
      return this._completeMutation != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetContinueMutation()) +
      Convert.ToUInt16(IsSetCompleteMutation());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
