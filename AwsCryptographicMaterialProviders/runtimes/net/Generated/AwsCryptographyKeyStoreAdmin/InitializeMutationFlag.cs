// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.KeyStoreAdmin;
namespace AWS.Cryptography.KeyStoreAdmin
{
  using Amazon.Runtime;
  public class InitializeMutationFlag : ConstantClass
  {


    public static readonly InitializeMutationFlag Created = new InitializeMutationFlag("Created");

    public static readonly InitializeMutationFlag Resumed = new InitializeMutationFlag("Resumed");

    public static readonly InitializeMutationFlag ResumedWithoutIndex = new InitializeMutationFlag("ResumedWithoutIndex");
    public static readonly InitializeMutationFlag[] Values =  {
 Created , Resumed , ResumedWithoutIndex
};
    public InitializeMutationFlag(string value) : base(value) { }
  }
}
