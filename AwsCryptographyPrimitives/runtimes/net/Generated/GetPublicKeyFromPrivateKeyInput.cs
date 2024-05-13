// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.Primitives;
namespace AWS.Cryptography.Primitives
{
    public class GetPublicKeyFromPrivateKeyInput
    {
        private System.IO.MemoryStream _privateKey;
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
            if (!IsSetPrivateKey()) throw new System.ArgumentException("Missing value for required property 'PrivateKey'");

        }
    }
}
