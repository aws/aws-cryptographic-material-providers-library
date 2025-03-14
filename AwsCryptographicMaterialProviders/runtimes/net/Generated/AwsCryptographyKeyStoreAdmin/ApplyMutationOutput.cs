// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class ApplyMutationOutput
  {
    private AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult _mutationResult;
    private System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> _mutatedBranchKeyItems;
    private string _lastModifiedTime;
    public AWS.Cryptography.KeyStoreAdmin.ApplyMutationResult MutationResult
    {
      get { return this._mutationResult; }
      set { this._mutationResult = value; }
    }
    public bool IsSetMutationResult()
    {
      return this._mutationResult != null;
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
    public string LastModifiedTime
    {
      get { return this._lastModifiedTime; }
      set { this._lastModifiedTime = value; }
    }
    public bool IsSetLastModifiedTime()
    {
      return this._lastModifiedTime != null;
    }
    public void Validate()
    {
      if (!IsSetMutationResult()) throw new System.ArgumentException("Missing value for required property 'MutationResult'");
      if (!IsSetMutatedBranchKeyItems()) throw new System.ArgumentException("Missing value for required property 'MutatedBranchKeyItems'");
      if (!IsSetLastModifiedTime()) throw new System.ArgumentException("Missing value for required property 'LastModifiedTime'");

    }
  }
}
