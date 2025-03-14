// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class HierarchicalKeyType
  {
    private AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetric _activeHierarchicalSymmetricVersion;
    private AWS.Cryptography.KeyStore.HierarchicalSymmetric _hierarchicalSymmetricVersion;
    private AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetricBeacon _activeHierarchicalSymmetricBeacon;
    public AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetric ActiveHierarchicalSymmetricVersion
    {
      get { return this._activeHierarchicalSymmetricVersion; }
      set { this._activeHierarchicalSymmetricVersion = value; }
    }
    public bool IsSetActiveHierarchicalSymmetricVersion()
    {
      return this._activeHierarchicalSymmetricVersion != null;
    }
    public AWS.Cryptography.KeyStore.HierarchicalSymmetric HierarchicalSymmetricVersion
    {
      get { return this._hierarchicalSymmetricVersion; }
      set { this._hierarchicalSymmetricVersion = value; }
    }
    public bool IsSetHierarchicalSymmetricVersion()
    {
      return this._hierarchicalSymmetricVersion != null;
    }
    public AWS.Cryptography.KeyStore.ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon
    {
      get { return this._activeHierarchicalSymmetricBeacon; }
      set { this._activeHierarchicalSymmetricBeacon = value; }
    }
    public bool IsSetActiveHierarchicalSymmetricBeacon()
    {
      return this._activeHierarchicalSymmetricBeacon != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetActiveHierarchicalSymmetricVersion()) +
      Convert.ToUInt16(IsSetHierarchicalSymmetricVersion()) +
      Convert.ToUInt16(IsSetActiveHierarchicalSymmetricBeacon());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
