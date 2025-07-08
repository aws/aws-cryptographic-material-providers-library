# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import _dafny
from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes import (
    CreateKeyOutput_CreateKeyOutput as DafnyCreateKeyOutput,
    CreateKeyStoreOutput_CreateKeyStoreOutput as DafnyCreateKeyStoreOutput,
    Error,
    Error_BranchKeyCiphertextException,
    Error_KeyStoreException,
    GetActiveBranchKeyOutput_GetActiveBranchKeyOutput as DafnyGetActiveBranchKeyOutput,
    GetBeaconKeyOutput_GetBeaconKeyOutput as DafnyGetBeaconKeyOutput,
    GetBranchKeyVersionOutput_GetBranchKeyVersionOutput as DafnyGetBranchKeyVersionOutput,
    GetKeyStoreInfoOutput_GetKeyStoreInfoOutput as DafnyGetKeyStoreInfoOutput,
    VersionKeyOutput_VersionKeyOutput as DafnyVersionKeyOutput,
)
import aws_cryptographic_material_providers.internaldafny.generated.module_
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy
from typing import Any

from .dafny_protocol import DafnyResponse
from .errors import (
    AwsCryptographicPrimitives,
    BranchKeyCiphertextException,
    CollectionOfErrors,
    ComAmazonawsDynamodb,
    ComAmazonawsKms,
    KeyStoreException,
    OpaqueError,
    ServiceError,
)
from aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.shim import (
    _sdk_error_to_dafny_error as com_amazonaws_dynamodb_sdk_error_to_dafny_error,
)
from aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.shim import (
    _sdk_error_to_dafny_error as com_amazonaws_kms_sdk_error_to_dafny_error,
)
from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.deserialize import (
    _deserialize_error as aws_cryptography_primitives_deserialize_error,
)

from .config import Config


def _deserialize_get_key_store_info(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetKeyStoreInfoOutput(
        input.value
    )


def _deserialize_create_key_store(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_CreateKeyStoreOutput(
        input.value
    )


def _deserialize_create_key(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_CreateKeyOutput(
        input.value
    )


def _deserialize_version_key(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_VersionKeyOutput(
        input.value
    )


def _deserialize_get_active_branch_key(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetActiveBranchKeyOutput(
        input.value
    )


def _deserialize_get_branch_key_version(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetBranchKeyVersionOutput(
        input.value
    )


def _deserialize_get_beacon_key(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetBeaconKeyOutput(
        input.value
    )


def _deserialize_error(error: Error) -> ServiceError:
    if error.is_Opaque:
        return OpaqueError(obj=error.obj)
    elif error.is_OpaqueWithText:
        return OpaqueErrorWithText(obj=error.obj, obj_message=error.objMessage)
    elif error.is_CollectionOfErrors:
        return CollectionOfErrors(
            message=_dafny.string_of(error.message),
            list=[_deserialize_error(dafny_e) for dafny_e in error.list],
        )
    elif error.is_BranchKeyCiphertextException:
        return BranchKeyCiphertextException(message=_dafny.string_of(error.message))
    elif error.is_KeyStoreException:
        return KeyStoreException(message=_dafny.string_of(error.message))
    elif error.is_AwsCryptographyPrimitives:
        return AwsCryptographicPrimitives(
            aws_cryptography_primitives_deserialize_error(
                error.AwsCryptographyPrimitives
            )
        )
    elif error.is_ComAmazonawsKms:
        return ComAmazonawsKms(message=_dafny.string_of(error.ComAmazonawsKms.message))
    elif error.is_ComAmazonawsDynamodb:
        return ComAmazonawsDynamodb(
            message=_dafny.string_of(error.ComAmazonawsDynamodb.message)
        )
    else:
        return OpaqueError(obj=error)
