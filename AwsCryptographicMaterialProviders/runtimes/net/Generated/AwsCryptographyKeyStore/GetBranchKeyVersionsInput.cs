// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class GetBranchKeyVersionsInput
  {
    private string _branchKeyIdentifier;
    private int? _count;
    public string BranchKeyIdentifier
    {
      get { return this._branchKeyIdentifier; }
      set { this._branchKeyIdentifier = value; }
    }
    public bool IsSetBranchKeyIdentifier()
    {
      return this._branchKeyIdentifier != null;
    }
    public int Count
    {
      get { return this._count.GetValueOrDefault(); }
      set { this._count = value; }
    }
    public bool IsSetCount()
    {
      return this._count.HasValue;
    }
    public void Validate()
    {
      if (!IsSetBranchKeyIdentifier()) throw new System.ArgumentException("Missing value for required property 'BranchKeyIdentifier'");
      if (!IsSetCount()) throw new System.ArgumentException("Missing value for required property 'Count'");

    }
  }
}
