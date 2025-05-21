// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  using Amazon.Runtime;
  public class TimeUnits : ConstantClass
  {


    public static readonly TimeUnits Seconds = new TimeUnits("Seconds");

    public static readonly TimeUnits Milliseconds = new TimeUnits("Milliseconds");
    public static readonly TimeUnits[] Values =  {
 Milliseconds , Seconds
};
    public TimeUnits(string value) : base(value) { }
  }
}
