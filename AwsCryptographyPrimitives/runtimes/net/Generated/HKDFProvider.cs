// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.Primitives;
namespace AWS.Cryptography.Primitives
{
    using Amazon.Runtime;
    public class HKDFProvider : ConstantClass
    {


        public static readonly HKDFProvider ACCP = new HKDFProvider("ACCP");

        public static readonly HKDFProvider MPL = new HKDFProvider("MPL");
        public static readonly HKDFProvider[] Values =  {
 ACCP , MPL
};
        public HKDFProvider(string value) : base(value) { }
    }
}
