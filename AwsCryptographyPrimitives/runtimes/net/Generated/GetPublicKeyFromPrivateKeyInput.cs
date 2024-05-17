// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.Primitives;
namespace AWS.Cryptography.Primitives
{
    public class GetPublicKeyFromPrivateKeyInput
    {
        private AWS.Cryptography.Primitives.ECDHCurveSpec _eccCurve;
        private System.IO.MemoryStream _privateKey;
        public AWS.Cryptography.Primitives.ECDHCurveSpec EccCurve
        {
            get { return this._eccCurve; }
            set { this._eccCurve = value; }
        }
        public bool IsSetEccCurve()
        {
            return this._eccCurve != null;
        }
        public System.IO.MemoryStream PrivateKey
        {
            get { return this._privateKey; }
            set { this._privateKey = value; }
        }
        public bool IsSetPrivateKey()
        {
            return this._privateKey != null;
        }
        public void Validate()
        {
            if (!IsSetEccCurve()) throw new System.ArgumentException("Missing value for required property 'EccCurve'");
            if (!IsSetPrivateKey()) throw new System.ArgumentException("Missing value for required property 'PrivateKey'");

        }
    }
}
