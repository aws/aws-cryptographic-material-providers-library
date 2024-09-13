// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class DescribeMutationOutput
  {
    private AWS.Cryptography.KeyStoreAdmin.MutationToken _mutationToken;
    public AWS.Cryptography.KeyStoreAdmin.MutationToken MutationToken
    {
      get { return this._mutationToken; }
      set { this._mutationToken = value; }
    }
    public bool IsSetMutationToken()
    {
      return this._mutationToken != null;
    }
    public void Validate()
    {

    }
  }
}
