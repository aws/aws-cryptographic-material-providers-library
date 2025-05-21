// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class KMSConfiguration
  {
    private string _kmsKeyArn;
    private string _kmsMRKeyArn;
    private AWS.Cryptography.KeyStore.Discovery _discovery;
    private AWS.Cryptography.KeyStore.MRDiscovery _mrDiscovery;
    public string KmsKeyArn
    {
      get { return this._kmsKeyArn; }
      set { this._kmsKeyArn = value; }
    }
    public bool IsSetKmsKeyArn()
    {
      return this._kmsKeyArn != null;
    }
    public string KmsMRKeyArn
    {
      get { return this._kmsMRKeyArn; }
      set { this._kmsMRKeyArn = value; }
    }
    public bool IsSetKmsMRKeyArn()
    {
      return this._kmsMRKeyArn != null;
    }
    public AWS.Cryptography.KeyStore.Discovery Discovery
    {
      get { return this._discovery; }
      set { this._discovery = value; }
    }
    public bool IsSetDiscovery()
    {
      return this._discovery != null;
    }
    public AWS.Cryptography.KeyStore.MRDiscovery MrDiscovery
    {
      get { return this._mrDiscovery; }
      set { this._mrDiscovery = value; }
    }
    public bool IsSetMrDiscovery()
    {
      return this._mrDiscovery != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetKmsKeyArn()) +
      Convert.ToUInt16(IsSetKmsMRKeyArn()) +
      Convert.ToUInt16(IsSetDiscovery()) +
      Convert.ToUInt16(IsSetMrDiscovery());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
