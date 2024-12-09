// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class InitializeMutationInput
  {
    private string _identifier;
    private AWS.Cryptography.KeyStoreAdmin.Mutations _mutations;
    private AWS.Cryptography.KeyStoreAdmin.KeyManagementStrategy _strategy;
    private AWS.Cryptography.KeyStoreAdmin.SystemKey _systemKey;
    private bool? _doNotVersion;
    public string Identifier
    {
      get { return this._identifier; }
      set { this._identifier = value; }
    }
    public bool IsSetIdentifier()
    {
      return this._identifier != null;
    }
    public AWS.Cryptography.KeyStoreAdmin.Mutations Mutations
    {
      get { return this._mutations; }
      set { this._mutations = value; }
    }
    public bool IsSetMutations()
    {
      return this._mutations != null;
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
    public AWS.Cryptography.KeyStoreAdmin.SystemKey SystemKey
    {
      get { return this._systemKey; }
      set { this._systemKey = value; }
    }
    public bool IsSetSystemKey()
    {
      return this._systemKey != null;
    }
    public bool DoNotVersion
    {
      get { return this._doNotVersion.GetValueOrDefault(); }
      set { this._doNotVersion = value; }
    }
    public bool IsSetDoNotVersion()
    {
      return this._doNotVersion.HasValue;
    }
    public void Validate()
    {
      if (!IsSetIdentifier()) throw new System.ArgumentException("Missing value for required property 'Identifier'");
      if (!IsSetMutations()) throw new System.ArgumentException("Missing value for required property 'Mutations'");
      if (!IsSetSystemKey()) throw new System.ArgumentException("Missing value for required property 'SystemKey'");

    }
  }
}
