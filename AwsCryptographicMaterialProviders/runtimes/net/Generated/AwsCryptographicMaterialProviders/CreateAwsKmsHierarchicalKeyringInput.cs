// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class CreateAwsKmsHierarchicalKeyringInput
  {
    private string _branchKeyId;
    private AWS.Cryptography.MaterialProviders.IBranchKeyIdSupplier _branchKeyIdSupplier;
    private AWS.Cryptography.KeyStore.KeyStore _keyStore;
    private long? _ttlSeconds;
    private AWS.Cryptography.MaterialProviders.CacheType _cache;
    private string _partitionId;
    private int? _limitMessages;
    public string BranchKeyId
    {
      get { return this._branchKeyId; }
      set { this._branchKeyId = value; }
    }
    public bool IsSetBranchKeyId()
    {
      return this._branchKeyId != null;
    }
    public AWS.Cryptography.MaterialProviders.IBranchKeyIdSupplier BranchKeyIdSupplier
    {
      get { return this._branchKeyIdSupplier; }
      set { this._branchKeyIdSupplier = value; }
    }
    public bool IsSetBranchKeyIdSupplier()
    {
      return this._branchKeyIdSupplier != null;
    }
    public AWS.Cryptography.KeyStore.KeyStore KeyStore
    {
      get { return this._keyStore; }
      set { this._keyStore = value; }
    }
    public bool IsSetKeyStore()
    {
      return this._keyStore != null;
    }
    public long TtlSeconds
    {
      get { return this._ttlSeconds.GetValueOrDefault(); }
      set { this._ttlSeconds = value; }
    }
    public bool IsSetTtlSeconds()
    {
      return this._ttlSeconds.HasValue;
    }
    public AWS.Cryptography.MaterialProviders.CacheType Cache
    {
      get { return this._cache; }
      set { this._cache = value; }
    }
    public bool IsSetCache()
    {
      return this._cache != null;
    }
    public string PartitionId
    {
      get { return this._partitionId; }
      set { this._partitionId = value; }
    }
    public bool IsSetPartitionId()
    {
      return this._partitionId != null;
    }
    public int LimitMessages
    {
      get { return this._limitMessages.GetValueOrDefault(); }
      set { this._limitMessages = value; }
    }
    public bool IsSetLimitMessages()
    {
      return this._limitMessages.HasValue;
    }
    public void Validate()
    {
      if (!IsSetKeyStore()) throw new System.ArgumentException("Missing value for required property 'KeyStore'");
      if (!IsSetTtlSeconds()) throw new System.ArgumentException("Missing value for required property 'TtlSeconds'");
      if (IsSetLimitMessages())
      {
        if (LimitMessages < 0)
        {
          throw new System.ArgumentException(
              String.Format("Member LimitMessages of structure CreateAwsKmsHierarchicalKeyringInput has type PositiveInteger which has a minimum of 0 but was given the value {0}.", LimitMessages));
        }
      }
    }
  }
}
