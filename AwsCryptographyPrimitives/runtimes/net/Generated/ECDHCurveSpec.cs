// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.Primitives;
namespace AWS.Cryptography.Primitives
{
    using Amazon.Runtime;
    public class ECDHCurveSpec : ConstantClass
    {


        public static readonly ECDHCurveSpec ECC_NIST_P256 = new ECDHCurveSpec("ECC_NIST_P256");

        public static readonly ECDHCurveSpec ECC_NIST_P384 = new ECDHCurveSpec("ECC_NIST_P384");

        public static readonly ECDHCurveSpec ECC_NIST_P521 = new ECDHCurveSpec("ECC_NIST_P521");

        public static readonly ECDHCurveSpec SM2 = new ECDHCurveSpec("SM2");
        public static readonly ECDHCurveSpec[] Values =  {
 ECC_NIST_P256 , ECC_NIST_P384 , ECC_NIST_P521 , SM2
};
        public ECDHCurveSpec(string value) : base(value) { }
    }
}
