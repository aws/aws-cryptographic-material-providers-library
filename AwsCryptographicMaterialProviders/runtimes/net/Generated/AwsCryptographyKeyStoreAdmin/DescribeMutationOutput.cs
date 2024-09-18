// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class DescribeMutationOutput
  {
    private AWS.Cryptography.KeyStoreAdmin.MutationInFlight _mutationInFlight;
    public AWS.Cryptography.KeyStoreAdmin.MutationInFlight MutationInFlight
    {
      get { return this._mutationInFlight; }
      set { this._mutationInFlight = value; }
    }
    public bool IsSetMutationInFlight()
    {
      return this._mutationInFlight != null;
    }
    public void Validate()
    {
      if (!IsSetMutationInFlight()) throw new System.ArgumentException("Missing value for required property 'MutationInFlight'");

    }
  }
}
