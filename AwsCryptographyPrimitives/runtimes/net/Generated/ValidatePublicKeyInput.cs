// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.Primitives;
namespace AWS.Cryptography.Primitives
{
    public class ValidatePublicKeyInput
    {
        private System.IO.MemoryStream _privateKey;
        private System.IO.MemoryStream _publicKey;
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
            if (!IsSetPrivateKey()) throw new System.ArgumentException("Missing value for required property 'PrivateKey'");
            if (!IsSetPublicKey()) throw new System.ArgumentException("Missing value for required property 'PublicKey'");

        }
    }
}
