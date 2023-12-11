// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.Primitives;
namespace AWS.Cryptography.Primitives
{
    using Amazon.Runtime;
    public class HKDFPolicy : ConstantClass
    {


        public static readonly HKDFPolicy REQUIRE_FIPS_HKDF = new HKDFPolicy("REQUIRE_FIPS_HKDF");

        public static readonly HKDFPolicy NONE = new HKDFPolicy("NONE");
        public static readonly HKDFPolicy[] Values =  {
 NONE , REQUIRE_FIPS_HKDF
};
        public HKDFPolicy(string value) : base(value) { }
    }
}
