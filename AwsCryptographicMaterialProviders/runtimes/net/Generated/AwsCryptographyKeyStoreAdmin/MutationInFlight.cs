// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class MutationInFlight
  {
    private AWS.Cryptography.KeyStoreAdmin.MutationDescription _yes;
    private string _no;
    public AWS.Cryptography.KeyStoreAdmin.MutationDescription Yes
    {
      get { return this._yes; }
      set { this._yes = value; }
    }
    public bool IsSetYes()
    {
      return this._yes != null;
    }
    public string No
    {
      get { return this._no; }
      set { this._no = value; }
    }
    public bool IsSetNo()
    {
      return this._no != null;
    }
    public void Validate()
    {
      var numberOfPropertiesSet = Convert.ToUInt16(IsSetYes()) +
      Convert.ToUInt16(IsSetNo());
      if (numberOfPropertiesSet == 0) throw new System.ArgumentException("No union value set");

      if (numberOfPropertiesSet > 1) throw new System.ArgumentException("Multiple union values set");

    }
  }
}
