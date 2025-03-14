// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  public class MutationDescription
  {
    private AWS.Cryptography.KeyStoreAdmin.MutationDetails _mutationDetails;
    private AWS.Cryptography.KeyStoreAdmin.MutationToken _mutationToken;
    private string _lastModifiedTime;
    public AWS.Cryptography.KeyStoreAdmin.MutationDetails MutationDetails
    {
      get { return this._mutationDetails; }
      set { this._mutationDetails = value; }
    }
    public bool IsSetMutationDetails()
    {
      return this._mutationDetails != null;
    }
    public AWS.Cryptography.KeyStoreAdmin.MutationToken MutationToken
    {
      get { return this._mutationToken; }
      set { this._mutationToken = value; }
    }
    public bool IsSetMutationToken()
    {
      return this._mutationToken != null;
    }
    public string LastModifiedTime
    {
      get { return this._lastModifiedTime; }
      set { this._lastModifiedTime = value; }
    }
    public bool IsSetLastModifiedTime()
    {
      return this._lastModifiedTime != null;
    }
    public void Validate()
    {
      if (!IsSetMutationDetails()) throw new System.ArgumentException("Missing value for required property 'MutationDetails'");
      if (!IsSetMutationToken()) throw new System.ArgumentException("Missing value for required property 'MutationToken'");
      if (!IsSetLastModifiedTime()) throw new System.ArgumentException("Missing value for required property 'LastModifiedTime'");

    }
  }
}
