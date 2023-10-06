// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProvidersTestVectorKeys;
namespace AWS.Cryptography.MaterialProvidersTestVectorKeys
{
  public class CachingCMM
  {
    private AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription _underlying;
    private int? _cacheLimitTtlSeconds;
    private long? _limitBytes;
    private int? _limitMessages;
    private System.IO.MemoryStream _getEntryIdentifier;
    private System.IO.MemoryStream _putEntryIdentifier;
    public AWS.Cryptography.MaterialProvidersTestVectorKeys.KeyDescription Underlying
    {
      get { return this._underlying; }
      set { this._underlying = value; }
    }
    public bool IsSetUnderlying()
    {
      return this._underlying != null;
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
    public System.IO.MemoryStream GetEntryIdentifier
    {
      get { return this._getEntryIdentifier; }
      set { this._getEntryIdentifier = value; }
    }
    public bool IsSetGetEntryIdentifier()
    {
      return this._getEntryIdentifier != null;
    }
    public System.IO.MemoryStream PutEntryIdentifier
    {
      get { return this._putEntryIdentifier; }
      set { this._putEntryIdentifier = value; }
    }
    public bool IsSetPutEntryIdentifier()
    {
      return this._putEntryIdentifier != null;
    }
    public void Validate()
    {
      if (!IsSetUnderlying()) throw new System.ArgumentException("Missing value for required property 'Underlying'");
      if (!IsSetCacheLimitTtlSeconds()) throw new System.ArgumentException("Missing value for required property 'CacheLimitTtlSeconds'");

    }
  }
}
