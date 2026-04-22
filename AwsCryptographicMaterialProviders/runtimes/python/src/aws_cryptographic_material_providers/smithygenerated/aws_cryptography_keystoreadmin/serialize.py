# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny

from .dafny_protocol import DafnyRequest

from .config import Config


def _serialize_create_key(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateKey",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_CreateKeyInput(
            input
        ),
    )


def _serialize_version_key(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="VersionKey",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_VersionKeyInput(
            input
        ),
    )


def _serialize_initialize_mutation(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="InitializeMutation",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_InitializeMutationInput(
            input
        ),
    )


def _serialize_apply_mutation(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="ApplyMutation",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_ApplyMutationInput(
            input
        ),
    )


def _serialize_describe_mutation(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="DescribeMutation",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_DescribeMutationInput(
            input
        ),
    )
