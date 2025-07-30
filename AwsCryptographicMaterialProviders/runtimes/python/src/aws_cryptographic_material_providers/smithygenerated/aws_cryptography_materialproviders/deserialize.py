# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import _dafny
from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes import (
    DecryptionMaterials_DecryptionMaterials as DafnyDecryptionMaterials,
    EncryptionMaterials_EncryptionMaterials as DafnyEncryptionMaterials,
    Error,
    Error_AwsCryptographicMaterialProvidersException,
    Error_EntryAlreadyExists,
    Error_EntryDoesNotExist,
    Error_InFlightTTLExceeded,
    Error_InvalidAlgorithmSuiteInfo,
    Error_InvalidAlgorithmSuiteInfoOnDecrypt,
    Error_InvalidAlgorithmSuiteInfoOnEncrypt,
    Error_InvalidDecryptionMaterials,
    Error_InvalidDecryptionMaterialsTransition,
    Error_InvalidEncryptionMaterials,
    Error_InvalidEncryptionMaterialsTransition,
)
import aws_cryptographic_material_providers.internaldafny.generated.module_
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy
from typing import Any

from .dafny_protocol import DafnyResponse
from .errors import (
    AwsCryptographicMaterialProvidersException,
    AwsCryptographicPrimitives,
    CollectionOfErrors,
    ComAmazonawsDynamodb,
    ComAmazonawsKms,
    EntryAlreadyExists,
    EntryDoesNotExist,
    InFlightTTLExceeded,
    InvalidAlgorithmSuiteInfo,
    InvalidAlgorithmSuiteInfoOnDecrypt,
    InvalidAlgorithmSuiteInfoOnEncrypt,
    InvalidDecryptionMaterials,
    InvalidDecryptionMaterialsTransition,
    InvalidEncryptionMaterials,
    InvalidEncryptionMaterialsTransition,
    KeyStore,
    OpaqueError,
    OpaqueWithTextError,
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

from ..aws_cryptography_keystore.deserialize import (
    _deserialize_error as aws_cryptography_keystore_deserialize_error,
)
from .config import Config


def _deserialize_create_aws_kms_keyring(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_aws_kms_discovery_keyring(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_aws_kms_multi_keyring(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_aws_kms_discovery_multi_keyring(
    input: DafnyResponse, config: Config
):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_aws_kms_mrk_keyring(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_aws_kms_mrk_multi_keyring(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_aws_kms_mrk_discovery_keyring(
    input: DafnyResponse, config: Config
):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_aws_kms_mrk_discovery_multi_keyring(
    input: DafnyResponse, config: Config
):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_aws_kms_hierarchical_keyring(
    input: DafnyResponse, config: Config
):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_aws_kms_rsa_keyring(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_aws_kms_ecdh_keyring(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_multi_keyring(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_raw_aes_keyring(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_raw_rsa_keyring(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_raw_ecdh_keyring(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(
        input.value
    )


def _deserialize_create_default_cryptographic_materials_manager(
    input: DafnyResponse, config: Config
):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateCryptographicMaterialsManagerOutput(
        input.value
    )


def _deserialize_create_required_encryption_context_cmm(
    input: DafnyResponse, config: Config
):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMOutput(
        input.value
    )


def _deserialize_create_cryptographic_materials_cache(
    input: DafnyResponse, config: Config
):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheOutput(
        input.value
    )


def _deserialize_create_default_client_supplier(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateDefaultClientSupplierOutput(
        input.value
    )


def _deserialize_initialize_encryption_materials(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_EncryptionMaterials(
        input.value
    )


def _deserialize_initialize_decryption_materials(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DecryptionMaterials(
        input.value
    )


def _deserialize_valid_encryption_materials_transition(
    input: DafnyResponse, config: Config
):

    return None


def _deserialize_valid_decryption_materials_transition(
    input: DafnyResponse, config: Config
):

    return None


def _deserialize_encryption_materials_has_plaintext_data_key(
    input: DafnyResponse, config: Config
):

    return None


def _deserialize_decryption_materials_with_plaintext_data_key(
    input: DafnyResponse, config: Config
):

    return None


def _deserialize_get_algorithm_suite_info(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_AlgorithmSuiteInfo(
        input.value
    )


def _deserialize_valid_algorithm_suite_info(input: DafnyResponse, config: Config):

    return None


def _deserialize_validate_commitment_policy_on_encrypt(
    input: DafnyResponse, config: Config
):

    return None


def _deserialize_validate_commitment_policy_on_decrypt(
    input: DafnyResponse, config: Config
):

    return None


def _deserialize_error(error: Error) -> ServiceError:
    if error.is_Opaque:
        return OpaqueError(obj=error.obj)
    elif error.is_OpaqueWithText:
        return OpaqueWithTextError(
            obj=error.obj, obj_message=_dafny.string_of(error.objMessage)
        )
    elif error.is_CollectionOfErrors:
        return CollectionOfErrors(
            message=_dafny.string_of(error.message),
            list=[_deserialize_error(dafny_e) for dafny_e in error.list],
        )
    elif error.is_AwsCryptographicMaterialProvidersException:
        return AwsCryptographicMaterialProvidersException(
            message=_dafny.string_of(error.message)
        )
    elif error.is_EntryAlreadyExists:
        return EntryAlreadyExists(message=_dafny.string_of(error.message))
    elif error.is_EntryDoesNotExist:
        return EntryDoesNotExist(message=_dafny.string_of(error.message))
    elif error.is_InFlightTTLExceeded:
        return InFlightTTLExceeded(message=_dafny.string_of(error.message))
    elif error.is_InvalidAlgorithmSuiteInfo:
        return InvalidAlgorithmSuiteInfo(message=_dafny.string_of(error.message))
    elif error.is_InvalidAlgorithmSuiteInfoOnDecrypt:
        return InvalidAlgorithmSuiteInfoOnDecrypt(
            message=_dafny.string_of(error.message)
        )
    elif error.is_InvalidAlgorithmSuiteInfoOnEncrypt:
        return InvalidAlgorithmSuiteInfoOnEncrypt(
            message=_dafny.string_of(error.message)
        )
    elif error.is_InvalidDecryptionMaterials:
        return InvalidDecryptionMaterials(message=_dafny.string_of(error.message))
    elif error.is_InvalidDecryptionMaterialsTransition:
        return InvalidDecryptionMaterialsTransition(
            message=_dafny.string_of(error.message)
        )
    elif error.is_InvalidEncryptionMaterials:
        return InvalidEncryptionMaterials(message=_dafny.string_of(error.message))
    elif error.is_InvalidEncryptionMaterialsTransition:
        return InvalidEncryptionMaterialsTransition(
            message=_dafny.string_of(error.message)
        )
    elif error.is_AwsCryptographyPrimitives:
        return AwsCryptographicPrimitives(
            aws_cryptography_primitives_deserialize_error(
                error.AwsCryptographyPrimitives
            )
        )
    elif error.is_AwsCryptographyKeyStore:
        return KeyStore(
            aws_cryptography_keystore_deserialize_error(error.AwsCryptographyKeyStore)
        )
    elif error.is_ComAmazonawsKms:
        if hasattr(error.ComAmazonawsKms, "objMessage"):
            return ComAmazonawsKms(
                message=_dafny.string_of(error.ComAmazonawsKms.objMessage)
            )
        else:
            return ComAmazonawsKms(
                message=_dafny.string_of(error.ComAmazonawsKms.message)
            )
    elif error.is_ComAmazonawsDynamodb:
        if hasattr(error.ComAmazonawsDynamodb, "objMessage"):
            return ComAmazonawsDynamodb(
                message=_dafny.string_of(error.ComAmazonawsDynamodb.objMessage)
            )
        else:
            return ComAmazonawsDynamodb(
                message=_dafny.string_of(error.ComAmazonawsDynamodb.message)
            )
    else:
        return OpaqueError(obj=error)
