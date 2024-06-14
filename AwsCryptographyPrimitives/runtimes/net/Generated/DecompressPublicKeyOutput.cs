// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.Primitives;
namespace AWS.Cryptography.Primitives
{
    public class DecompressPublicKeyOutput
    {
        private AWS.Cryptography.Primitives.ECCPublicKey _publicKey;
        public AWS.Cryptography.Primitives.ECCPublicKey PublicKey
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
            if (!IsSetPublicKey()) throw new System.ArgumentException("Missing value for required property 'PublicKey'");

        }
    }
}
