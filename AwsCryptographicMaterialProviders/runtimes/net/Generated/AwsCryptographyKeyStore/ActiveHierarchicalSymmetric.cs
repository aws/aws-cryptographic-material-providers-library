// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class ActiveHierarchicalSymmetric
  {
    private string _version;
    public string Version
    {
      get { return this._version; }
      set { this._version = value; }
    }
    public bool IsSetVersion()
    {
      return this._version != null;
    }
    public void Validate()
    {
      if (!IsSetVersion()) throw new System.ArgumentException("Missing value for required property 'Version'");

    }
  }
}
