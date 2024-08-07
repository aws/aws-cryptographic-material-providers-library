// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.Primitives;
namespace AWS.Cryptography.Primitives
{
    public class DecompressPublicKeyInput
    {
        private System.IO.MemoryStream _compressedPublicKey;
        private AWS.Cryptography.Primitives.ECDHCurveSpec _eccCurve;
        public System.IO.MemoryStream CompressedPublicKey
        {
            get { return this._compressedPublicKey; }
            set { this._compressedPublicKey = value; }
        }
        public bool IsSetCompressedPublicKey()
        {
            return this._compressedPublicKey != null;
        }
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
            if (!IsSetCompressedPublicKey()) throw new System.ArgumentException("Missing value for required property 'CompressedPublicKey'");
            if (!IsSetEccCurve()) throw new System.ArgumentException("Missing value for required property 'EccCurve'");

        }
    }
}
