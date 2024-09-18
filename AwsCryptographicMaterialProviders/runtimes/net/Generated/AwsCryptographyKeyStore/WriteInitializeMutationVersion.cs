// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStore;
namespace AWS.Cryptography.KeyStore
{
  public class WriteInitializeMutationVersion
  {
    private AWS.Cryptography.KeyStore.EncryptedHierarchicalKey _rotate;
    private AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey _mutate;
    public AWS.Cryptography.KeyStore.EncryptedHierarchicalKey Rotate
    {
      get { return this._rotate; }
      set { this._rotate = value; }
    }
    public bool IsSetRotate()
    {
      return this._rotate != null;
    }
    public AWS.Cryptography.KeyStore.OverWriteEncryptedHierarchicalKey Mutate
    {
      get { return this._mutate; }
      set { this._mutate = value; }
    }
    public bool IsSetMutate()
    {
      return this._mutate != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetRotate()) +
      Convert.ToUInt16(IsSetMutate());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
