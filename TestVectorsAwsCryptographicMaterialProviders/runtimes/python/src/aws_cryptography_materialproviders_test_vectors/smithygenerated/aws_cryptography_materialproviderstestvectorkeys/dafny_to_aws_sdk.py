# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes import (
    EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1,
    EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256,
    EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT,
)
import aws_cryptography_internal_kms.internaldafny.generated.module_


def com_amazonaws_kms_EncryptionAlgorithmSpec(dafny_input):
    # Convert EncryptionAlgorithmSpec
    if isinstance(dafny_input, EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT):
        return "SYMMETRIC_DEFAULT"

    elif isinstance(dafny_input, EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1):
        return "RSAES_OAEP_SHA_1"

    elif isinstance(dafny_input, EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256):
        return "RSAES_OAEP_SHA_256"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)
