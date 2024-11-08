# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import _dafny
from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes import (
    ApplyMutationOutput_ApplyMutationOutput as DafnyApplyMutationOutput,
    CreateKeyOutput_CreateKeyOutput as DafnyCreateKeyOutput,
    DescribeMutationOutput_DescribeMutationOutput as DafnyDescribeMutationOutput,
    Error,
    Error_KeyStoreAdminException,
    Error_MutationConflictException,
    Error_MutationFromException,
    Error_MutationInvalidException,
    Error_MutationToException,
    Error_MutationVerificationException,
    Error_UnexpectedStateException,
    Error_UnsupportedFeatureException,
    InitializeMutationOutput_InitializeMutationOutput as DafnyInitializeMutationOutput,
    VersionKeyOutput_VersionKeyOutput as DafnyVersionKeyOutput,
)
import aws_cryptographic_material_providers.internaldafny.generated.module_
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy
from typing import Any

from .dafny_protocol import DafnyResponse
from .errors import (
    CollectionOfErrors,
    ComAmazonawsDynamodb,
    ComAmazonawsKms,
    KeyStore,
    KeyStoreAdminException,
    MutationConflictException,
    MutationFromException,
    MutationInvalidException,
    MutationToException,
    MutationVerificationException,
    OpaqueError,
    ServiceError,
    UnexpectedStateException,
    UnsupportedFeatureException,
)
from aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.shim import (
    _sdk_error_to_dafny_error as com_amazonaws_dynamodb_sdk_error_to_dafny_error,
)
from aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.shim import (
    _sdk_error_to_dafny_error as com_amazonaws_kms_sdk_error_to_dafny_error,
)

from ..aws_cryptography_keystore.deserialize import (
    _deserialize_error as aws_cryptography_keystore_deserialize_error,
)
from .config import Config


def _deserialize_create_key(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_CreateKeyOutput(
        input.value
    )


def _deserialize_version_key(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_VersionKeyOutput(
        input.value
    )


def _deserialize_initialize_mutation(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_InitializeMutationOutput(
        input.value
    )


def _deserialize_apply_mutation(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_ApplyMutationOutput(
        input.value
    )


def _deserialize_describe_mutation(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_DescribeMutationOutput(
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
    elif error.is_KeyStoreAdminException:
        return KeyStoreAdminException(message=_dafny.string_of(error.message))
    elif error.is_MutationConflictException:
        return MutationConflictException(message=_dafny.string_of(error.message))
    elif error.is_MutationFromException:
        return MutationFromException(message=_dafny.string_of(error.message))
    elif error.is_MutationInvalidException:
        return MutationInvalidException(message=_dafny.string_of(error.message))
    elif error.is_MutationToException:
        return MutationToException(message=_dafny.string_of(error.message))
    elif error.is_MutationVerificationException:
        return MutationVerificationException(message=_dafny.string_of(error.message))
    elif error.is_UnexpectedStateException:
        return UnexpectedStateException(message=_dafny.string_of(error.message))
    elif error.is_UnsupportedFeatureException:
        return UnsupportedFeatureException(message=_dafny.string_of(error.message))
    elif error.is_AwsCryptographyKeyStore:
        return KeyStore(
            aws_cryptography_keystore_deserialize_error(error.AwsCryptographyKeyStore)
        )
    elif error.is_ComAmazonawsKms:
        return ComAmazonawsKms(message=_dafny.string_of(error.ComAmazonawsKms.message))
    elif error.is_ComAmazonawsDynamodb:
        return ComAmazonawsDynamodb(
            message=_dafny.string_of(error.ComAmazonawsDynamodb.message)
        )
    else:
        return OpaqueError(obj=error)
