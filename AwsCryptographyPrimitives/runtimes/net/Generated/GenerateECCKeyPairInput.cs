// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.Primitives;
namespace AWS.Cryptography.Primitives
{
    public class GenerateECCKeyPairInput
    {
        private AWS.Cryptography.Primitives.ECDHCurveSpec _eccCurve;
        public AWS.Cryptography.Primitives.ECDHCurveSpec EccCurve
        {
            get { return this._eccCurve; }
            set { this._eccCurve = value; }
        }
        public bool IsSetEccCurve()
        {
            return this._eccCurve != null;
        }
        public void Validate()
        {
            if (!IsSetEccCurve()) throw new System.ArgumentException("Missing value for required property 'EccCurve'");

        }
    }
}
