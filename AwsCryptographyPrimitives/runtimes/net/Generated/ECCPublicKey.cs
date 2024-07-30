// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.Primitives;
namespace AWS.Cryptography.Primitives
{
    public class ECCPublicKey
    {
        private System.IO.MemoryStream _der;
        public System.IO.MemoryStream Der
        {
            get { return this._der; }
            set { this._der = value; }
        }
        public bool IsSetDer()
        {
            return this._der != null;
        }
        public void Validate()
        {
            if (!IsSetDer()) throw new System.ArgumentException("Missing value for required property 'Der'");

        }
    }
}
