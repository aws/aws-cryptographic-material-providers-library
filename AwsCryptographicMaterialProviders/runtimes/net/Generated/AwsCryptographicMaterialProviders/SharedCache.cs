// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  public class SharedCache
  {
    private AWS.Cryptography.MaterialProviders.ICryptographicMaterialsCache _cache;
    public AWS.Cryptography.MaterialProviders.ICryptographicMaterialsCache Cache
    {
      get { return this._cache; }
      set { this._cache = value; }
    }
    public bool IsSetCache()
    {
      return this._cache != null;
    }
    public void Validate()
    {
      if (!IsSetCache()) throw new System.ArgumentException("Missing value for required property 'Cache'");

    }
  }
}
