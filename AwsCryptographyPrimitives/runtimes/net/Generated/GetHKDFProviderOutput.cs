// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
using System;
using AWS.Cryptography.Primitives;
namespace AWS.Cryptography.Primitives
{
    public class GetHKDFProviderOutput
    {
        private AWS.Cryptography.Primitives.HKDFProvider _provider;
        public AWS.Cryptography.Primitives.HKDFProvider Provider
        {
            get { return this._provider; }
            set { this._provider = value; }
        }
        public bool IsSetProvider()
        {
            return this._provider != null;
        }
        public void Validate()
        {
            if (!IsSetProvider()) throw new System.ArgumentException("Missing value for required property 'Provider'");

        }
    }
}
