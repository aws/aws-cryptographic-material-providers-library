# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny

from .dafny_protocol import DafnyRequest

from .config import Config


def _serialize_create_test_vector_keyring(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateTestVectorKeyring",
        dafny_operation_input=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_TestVectorKeyringInput(
            input
        ),
    )


def _serialize_create_wrapped_test_vector_keyring(
    input, config: Config
) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateWrappedTestVectorKeyring",
        dafny_operation_input=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_TestVectorKeyringInput(
            input
        ),
    )


def _serialize_create_wrapped_test_vector_cmm(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateWrappedTestVectorCmm",
        dafny_operation_input=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_TestVectorCmmInput(
            input
        ),
    )


def _serialize_get_key_description(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="GetKeyDescription",
        dafny_operation_input=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_GetKeyDescriptionInput(
            input
        ),
    )


def _serialize_serialize_key_description(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="SerializeKeyDescription",
        dafny_operation_input=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_SerializeKeyDescriptionInput(
            input
        ),
    )
