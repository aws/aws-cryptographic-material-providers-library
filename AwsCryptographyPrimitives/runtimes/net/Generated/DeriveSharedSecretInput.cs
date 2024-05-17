// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.Primitives;
namespace AWS.Cryptography.Primitives
{
    public class DeriveSharedSecretInput
    {
        private AWS.Cryptography.Primitives.ECDHCurveSpec _eccCurve;
        private System.IO.MemoryStream _privateKey;
        private System.IO.MemoryStream _publicKey;
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
        public System.IO.MemoryStream PublicKey
        {
            get { return this._publicKey; }
            set { this._publicKey = value; }
        }
        public bool IsSetPublicKey()
        {
            return this._publicKey != null;
        }
        public void Validate()
        {
            if (!IsSetEccCurve()) throw new System.ArgumentException("Missing value for required property 'EccCurve'");
            if (!IsSetPrivateKey()) throw new System.ArgumentException("Missing value for required property 'PrivateKey'");
            if (!IsSetPublicKey()) throw new System.ArgumentException("Missing value for required property 'PublicKey'");

        }
    }
}
