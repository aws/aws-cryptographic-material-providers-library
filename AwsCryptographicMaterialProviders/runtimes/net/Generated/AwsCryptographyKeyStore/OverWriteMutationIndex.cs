// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class OverWriteMutationIndex
  {
    private AWS.Cryptography.KeyStore.MutationIndex _index;
    private AWS.Cryptography.KeyStore.MutationIndex _old;
    public AWS.Cryptography.KeyStore.MutationIndex Index
    {
      get { return this._index; }
      set { this._index = value; }
    }
    public bool IsSetIndex()
    {
      return this._index != null;
    }
    public AWS.Cryptography.KeyStore.MutationIndex Old
    {
      get { return this._old; }
      set { this._old = value; }
    }
    public bool IsSetOld()
    {
      return this._old != null;
    }
    public void Validate()
    {
      if (!IsSetIndex()) throw new System.ArgumentException("Missing value for required property 'Index'");
      if (!IsSetOld()) throw new System.ArgumentException("Missing value for required property 'Old'");

    }
  }
}
