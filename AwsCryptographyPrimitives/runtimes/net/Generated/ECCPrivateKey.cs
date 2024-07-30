// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.Primitives;
namespace AWS.Cryptography.Primitives
{
    public class ECCPrivateKey
    {
        private System.IO.MemoryStream _pem;
        public System.IO.MemoryStream Pem
        {
            get { return this._pem; }
            set { this._pem = value; }
        }
        public bool IsSetPem()
        {
            return this._pem != null;
        }
        public void Validate()
        {
            if (!IsSetPem()) throw new System.ArgumentException("Missing value for required property 'Pem'");

        }
    }
}
