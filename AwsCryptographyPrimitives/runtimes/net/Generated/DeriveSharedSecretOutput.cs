// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.Primitives;
namespace AWS.Cryptography.Primitives
{
    public class DeriveSharedSecretOutput
    {
        private System.IO.MemoryStream _sharedSecret;
        public System.IO.MemoryStream SharedSecret
        {
            get { return this._sharedSecret; }
            set { this._sharedSecret = value; }
        }
        public bool IsSetSharedSecret()
        {
            return this._sharedSecret != null;
        }
        public void Validate()
        {
            if (!IsSetSharedSecret()) throw new System.ArgumentException("Missing value for required property 'SharedSecret'");

        }
    }
}
