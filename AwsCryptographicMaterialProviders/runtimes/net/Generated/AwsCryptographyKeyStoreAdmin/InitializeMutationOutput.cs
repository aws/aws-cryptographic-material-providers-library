// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class InitializeMutationOutput
  {
    private AWS.Cryptography.KeyStoreAdmin.MutationToken _mutationToken;
    private System.Collections.Generic.List<AWS.Cryptography.KeyStoreAdmin.MutatedBranchKeyItem> _mutatedBranchKeyItems;
    private AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag _initializeMutationFlag;
    private string _lastModifiedTime;
    public AWS.Cryptography.KeyStoreAdmin.MutationToken MutationToken
    {
      get { return this._mutationToken; }
      set { this._mutationToken = value; }
    }
    public bool IsSetMutationToken()
    {
      return this._mutationToken != null;
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
    public AWS.Cryptography.KeyStoreAdmin.InitializeMutationFlag InitializeMutationFlag
    {
      get { return this._initializeMutationFlag; }
      set { this._initializeMutationFlag = value; }
    }
    public bool IsSetInitializeMutationFlag()
    {
      return this._initializeMutationFlag != null;
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
      if (!IsSetMutationToken()) throw new System.ArgumentException("Missing value for required property 'MutationToken'");
      if (!IsSetMutatedBranchKeyItems()) throw new System.ArgumentException("Missing value for required property 'MutatedBranchKeyItems'");
      if (!IsSetInitializeMutationFlag()) throw new System.ArgumentException("Missing value for required property 'InitializeMutationFlag'");
      if (!IsSetLastModifiedTime()) throw new System.ArgumentException("Missing value for required property 'LastModifiedTime'");

    }
  }
}
