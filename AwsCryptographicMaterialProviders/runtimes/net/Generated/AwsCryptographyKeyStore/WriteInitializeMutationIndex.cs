// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class WriteInitializeMutationIndex
  {
    private AWS.Cryptography.KeyStore.MutationIndex _create;
    private AWS.Cryptography.KeyStore.OverWriteMutationIndex _update;
    public AWS.Cryptography.KeyStore.MutationIndex Create
    {
      get { return this._create; }
      set { this._create = value; }
    }
    public bool IsSetCreate()
    {
      return this._create != null;
    }
    public AWS.Cryptography.KeyStore.OverWriteMutationIndex Update
    {
      get { return this._update; }
      set { this._update = value; }
    }
    public bool IsSetUpdate()
    {
      return this._update != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetCreate()) +
      Convert.ToUInt16(IsSetUpdate());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
