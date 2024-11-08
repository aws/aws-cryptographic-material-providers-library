# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import _dafny
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy
from aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AwsCryptographyMaterialProvidersTestVectorKeysTypes import (
    Error,
    Error_KeyVectorException,
    GetKeyDescriptionOutput_GetKeyDescriptionOutput as DafnyGetKeyDescriptionOutput,
    SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput as DafnySerializeKeyDescriptionOutput,
)
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.module_
import aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy
from typing import Any

from .dafny_protocol import DafnyResponse
from .errors import CollectionOfErrors, KeyVectorException, OpaqueError, ServiceError

from .config import Config


def _deserialize_create_test_vector_keyring(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_wrapped_test_vector_keyring(
    input: DafnyResponse, config: Config
):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_wrapped_test_vector_cmm(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_CreateWrappedTestVectorCmmOutput(
        input.value
    )


def _deserialize_get_key_description(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_GetKeyDescriptionOutput(
        input.value
    )


def _deserialize_serialize_key_description(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_SerializeKeyDescriptionOutput(
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
    elif error.is_KeyVectorException:
        return KeyVectorException(message=_dafny.string_of(error.message))
    else:
        return OpaqueError(obj=error)
