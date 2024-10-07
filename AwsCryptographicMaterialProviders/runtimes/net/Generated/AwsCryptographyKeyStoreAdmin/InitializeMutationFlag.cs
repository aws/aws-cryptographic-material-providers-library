// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class InitializeMutationFlag
  {
    private string _created;
    private string _resumed;
    private string _resumedWithoutIndex;
    public string Created
    {
      get { return this._created; }
      set { this._created = value; }
    }
    public bool IsSetCreated()
    {
      return this._created != null;
    }
    public string Resumed
    {
      get { return this._resumed; }
      set { this._resumed = value; }
    }
    public bool IsSetResumed()
    {
      return this._resumed != null;
    }
    public string ResumedWithoutIndex
    {
      get { return this._resumedWithoutIndex; }
      set { this._resumedWithoutIndex = value; }
    }
    public bool IsSetResumedWithoutIndex()
    {
      return this._resumedWithoutIndex != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetCreated()) +
      Convert.ToUInt16(IsSetResumed()) +
      Convert.ToUInt16(IsSetResumedWithoutIndex());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
