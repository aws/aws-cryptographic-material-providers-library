# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny

from .dafny_protocol import DafnyRequest

from .config import Config


def _serialize_get_key_store_info(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="GetKeyStoreInfo", dafny_operation_input=None)

def _serialize_create_key_store(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="CreateKeyStore", dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_CreateKeyStoreInput(input))

def _serialize_create_key(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="CreateKey", dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_CreateKeyInput(input))

def _serialize_version_key(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="VersionKey", dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_VersionKeyInput(input))

def _serialize_get_active_branch_key(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="GetActiveBranchKey", dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetActiveBranchKeyInput(input))

def _serialize_get_branch_key_version(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="GetBranchKeyVersion", dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetBranchKeyVersionInput(input))

def _serialize_get_beacon_key(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="GetBeaconKey", dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetBeaconKeyInput(input))
