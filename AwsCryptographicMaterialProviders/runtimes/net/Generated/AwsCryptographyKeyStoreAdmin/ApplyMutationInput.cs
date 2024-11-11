// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class ApplyMutationInput
  {
    private AWS.Cryptography.KeyStoreAdmin.MutationToken _mutationToken;
    private int? _pageSize;
    private AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy _strategy;
    private AWS.Cryptography.KeyStoreAdmin.SystemKey _systemKey;
    public AWS.Cryptography.KeyStoreAdmin.MutationToken MutationToken
    {
      get { return this._mutationToken; }
      set { this._mutationToken = value; }
    }
    public bool IsSetMutationToken()
    {
      return this._mutationToken != null;
    }
    public int PageSize
    {
      get { return this._pageSize.GetValueOrDefault(); }
      set { this._pageSize = value; }
    }
    public bool IsSetPageSize()
    {
      return this._pageSize.HasValue;
    }
    public AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy Strategy
    {
      get { return this._strategy; }
      set { this._strategy = value; }
    }
    public bool IsSetStrategy()
    {
      return this._strategy != null;
    }
    public AWS.Cryptography.KeyStoreAdmin.SystemKey SystemKey
    {
      get { return this._systemKey; }
      set { this._systemKey = value; }
    }
    public bool IsSetSystemKey()
    {
      return this._systemKey != null;
    }
    public void Validate()
    {
      if (!IsSetMutationToken()) throw new System.ArgumentException("Missing value for required property 'MutationToken'");

    }
  }
}
