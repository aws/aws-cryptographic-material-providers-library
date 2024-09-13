// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class ApplyMutationOutput
  {
    private AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult _result;
    private System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> _mutatedBranchKeyItems;
    public AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult Result
    {
      get { return this._result; }
      set { this._result = value; }
    }
    public bool IsSetResult()
    {
      return this._result != null;
    }
    public System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> MutatedBranchKeyItems
    {
      get { return this._mutatedBranchKeyItems; }
      set { this._mutatedBranchKeyItems = value; }
    }
    public bool IsSetMutatedBranchKeyItems()
    {
      return this._mutatedBranchKeyItems != null;
    }
    public void Validate()
    {
      if (!IsSetResult()) throw new System.ArgumentException("Missing value for required property 'Result'");
      if (!IsSetMutatedBranchKeyItems()) throw new System.ArgumentException("Missing value for required property 'MutatedBranchKeyItems'");

    }
  }
}
