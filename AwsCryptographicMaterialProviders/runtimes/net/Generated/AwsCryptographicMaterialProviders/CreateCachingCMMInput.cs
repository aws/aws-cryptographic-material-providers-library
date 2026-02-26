// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class CreateCachingCMMInput
  {
    private AWS.Cryptography.MaterialProviders.ICryptographicMaterialsCache _underlyingCMC;
    private int? _cacheLimitTtlSeconds;
    private AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager _underlyingCMM;
    private AWS.Cryptography.MaterialProviders.IKeyring _keyring;
    private string _partitionKey;
    private long? _limitBytes;
    private int? _limitMessages;
    public AWS.Cryptography.MaterialProviders.ICryptographicMaterialsCache UnderlyingCMC
    {
      get { return this._underlyingCMC; }
      set { this._underlyingCMC = value; }
    }
    public bool IsSetUnderlyingCMC()
    {
      return this._underlyingCMC != null;
    }
    public int CacheLimitTtlSeconds
    {
      get { return this._cacheLimitTtlSeconds.GetValueOrDefault(); }
      set { this._cacheLimitTtlSeconds = value; }
    }
    public bool IsSetCacheLimitTtlSeconds()
    {
      return this._cacheLimitTtlSeconds.HasValue;
    }
    public AWS.Cryptography.MaterialProviders.ICryptographicMaterialsManager UnderlyingCMM
    {
      get { return this._underlyingCMM; }
      set { this._underlyingCMM = value; }
    }
    public bool IsSetUnderlyingCMM()
    {
      return this._underlyingCMM != null;
    }
    public AWS.Cryptography.MaterialProviders.IKeyring Keyring
    {
      get { return this._keyring; }
      set { this._keyring = value; }
    }
    public bool IsSetKeyring()
    {
      return this._keyring != null;
    }
    public string PartitionKey
    {
      get { return this._partitionKey; }
      set { this._partitionKey = value; }
    }
    public bool IsSetPartitionKey()
    {
      return this._partitionKey != null;
    }
    public long LimitBytes
    {
      get { return this._limitBytes.GetValueOrDefault(); }
      set { this._limitBytes = value; }
    }
    public bool IsSetLimitBytes()
    {
      return this._limitBytes.HasValue;
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
      if (!IsSetUnderlyingCMC()) throw new System.ArgumentException("Missing value for required property 'UnderlyingCMC'");
      if (!IsSetCacheLimitTtlSeconds()) throw new System.ArgumentException("Missing value for required property 'CacheLimitTtlSeconds'");

    }
  }
}
