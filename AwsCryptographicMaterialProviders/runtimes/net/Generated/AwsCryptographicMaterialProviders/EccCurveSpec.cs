// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.MaterialProviders;
namespace AWS.Cryptography.MaterialProviders
{
  using Amazon.Runtime;
  public class EccCurveSpec : ConstantClass
  {


    public static readonly EccCurveSpec ECC_NIST_P256 = new EccCurveSpec("secp256r1");

    public static readonly EccCurveSpec ECC_NIST_P384 = new EccCurveSpec("secp384r1");

    public static readonly EccCurveSpec ECC_NIST_P521 = new EccCurveSpec("secp521r1");

    public static readonly EccCurveSpec SM2 = new EccCurveSpec("SM2PKE");
    public static readonly EccCurveSpec[] Values =  {
 ECC_NIST_P256 , ECC_NIST_P384 , ECC_NIST_P521 , SM2
};
    public EccCurveSpec(string value) : base(value) { }
  }
}
