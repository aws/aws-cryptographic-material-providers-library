// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class VersionKeyInput
  {
    private string _identifier;
    private AWS.Cryptography.KeyStoreAdmin.KmsSymmetricKeyArn _kmsArn;
    private AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy _strategy;
    private AWS.Cryptography.KeyStore.HierarchyVersion _hierarchyVersion;
    public string Identifier
    {
      get { return this._identifier; }
      set { this._identifier = value; }
    }
    public bool IsSetIdentifier()
    {
      return this._identifier != null;
    }
    public AWS.Cryptography.KeyStoreAdmin.KmsSymmetricKeyArn KmsArn
    {
      get { return this._kmsArn; }
      set { this._kmsArn = value; }
    }
    public bool IsSetKmsArn()
    {
      return this._kmsArn != null;
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
    public AWS.Cryptography.KeyStore.HierarchyVersion HierarchyVersion
    {
      get { return this._hierarchyVersion; }
      set { this._hierarchyVersion = value; }
    }
    public bool IsSetHierarchyVersion()
    {
      return this._hierarchyVersion != null;
    }
    public void Validate()
    {
      if (!IsSetIdentifier()) throw new System.ArgumentException("Missing value for required property 'Identifier'");
      if (!IsSetKmsArn()) throw new System.ArgumentException("Missing value for required property 'KmsArn'");

    }
  }
}
