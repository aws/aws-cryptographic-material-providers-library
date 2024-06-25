// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.Primitives;
namespace AWS.Cryptography.Primitives
{
    public class ValidatePublicKeyOutput
    {
        private bool? _success;
        public bool Success
        {
            get { return this._success.GetValueOrDefault(); }
            set { this._success = value; }
        }
        public bool IsSetSuccess()
        {
            return this._success.HasValue;
        }
        public void Validate()
        {
            if (!IsSetSuccess()) throw new System.ArgumentException("Missing value for required property 'Success'");

        }
    }
}
