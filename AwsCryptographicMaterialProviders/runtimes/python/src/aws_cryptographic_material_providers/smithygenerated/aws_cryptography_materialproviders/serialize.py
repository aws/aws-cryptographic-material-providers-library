# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny

from .dafny_protocol import DafnyRequest

from .config import Config


def _serialize_create_aws_kms_keyring(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateAwsKmsKeyring",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateAwsKmsKeyringInput(
            input
        ),
    )


def _serialize_create_aws_kms_discovery_keyring(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateAwsKmsDiscoveryKeyring",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateAwsKmsDiscoveryKeyringInput(
            input
        ),
    )


def _serialize_create_aws_kms_multi_keyring(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateAwsKmsMultiKeyring",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateAwsKmsMultiKeyringInput(
            input
        ),
    )


def _serialize_create_aws_kms_discovery_multi_keyring(
    input, config: Config
) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateAwsKmsDiscoveryMultiKeyring",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateAwsKmsDiscoveryMultiKeyringInput(
            input
        ),
    )


def _serialize_create_aws_kms_mrk_keyring(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateAwsKmsMrkKeyring",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateAwsKmsMrkKeyringInput(
            input
        ),
    )


def _serialize_create_aws_kms_mrk_multi_keyring(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateAwsKmsMrkMultiKeyring",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateAwsKmsMrkMultiKeyringInput(
            input
        ),
    )


def _serialize_create_aws_kms_mrk_discovery_keyring(
    input, config: Config
) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateAwsKmsMrkDiscoveryKeyring",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryKeyringInput(
            input
        ),
    )


def _serialize_create_aws_kms_mrk_discovery_multi_keyring(
    input, config: Config
) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateAwsKmsMrkDiscoveryMultiKeyring",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryMultiKeyringInput(
            input
        ),
    )


def _serialize_create_aws_kms_hierarchical_keyring(
    input, config: Config
) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateAwsKmsHierarchicalKeyring",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateAwsKmsHierarchicalKeyringInput(
            input
        ),
    )


def _serialize_create_aws_kms_rsa_keyring(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateAwsKmsRsaKeyring",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateAwsKmsRsaKeyringInput(
            input
        ),
    )


def _serialize_create_aws_kms_ecdh_keyring(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateAwsKmsEcdhKeyring",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateAwsKmsEcdhKeyringInput(
            input
        ),
    )


def _serialize_create_multi_keyring(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateMultiKeyring",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateMultiKeyringInput(
            input
        ),
    )


def _serialize_create_raw_aes_keyring(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateRawAesKeyring",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateRawAesKeyringInput(
            input
        ),
    )


def _serialize_create_raw_rsa_keyring(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateRawRsaKeyring",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateRawRsaKeyringInput(
            input
        ),
    )


def _serialize_create_raw_ecdh_keyring(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateRawEcdhKeyring",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateRawEcdhKeyringInput(
            input
        ),
    )


def _serialize_create_default_cryptographic_materials_manager(
    input, config: Config
) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateDefaultCryptographicMaterialsManager",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateDefaultCryptographicMaterialsManagerInput(
            input
        ),
    )


def _serialize_create_required_encryption_context_cmm(
    input, config: Config
) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateRequiredEncryptionContextCMM",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMInput(
            input
        ),
    )


def _serialize_create_cryptographic_materials_cache(
    input, config: Config
) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateCryptographicMaterialsCache",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheInput(
            input
        ),
    )


def _serialize_create_default_client_supplier(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CreateDefaultClientSupplier",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateDefaultClientSupplierInput(
            input
        ),
    )


def _serialize_initialize_encryption_materials(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="InitializeEncryptionMaterials",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_InitializeEncryptionMaterialsInput(
            input
        ),
    )


def _serialize_initialize_decryption_materials(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="InitializeDecryptionMaterials",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_InitializeDecryptionMaterialsInput(
            input
        ),
    )


def _serialize_valid_encryption_materials_transition(
    input, config: Config
) -> DafnyRequest:
    return DafnyRequest(
        operation_name="ValidEncryptionMaterialsTransition",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ValidEncryptionMaterialsTransitionInput(
            input
        ),
    )


def _serialize_valid_decryption_materials_transition(
    input, config: Config
) -> DafnyRequest:
    return DafnyRequest(
        operation_name="ValidDecryptionMaterialsTransition",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ValidDecryptionMaterialsTransitionInput(
            input
        ),
    )


def _serialize_encryption_materials_has_plaintext_data_key(
    input, config: Config
) -> DafnyRequest:
    return DafnyRequest(
        operation_name="EncryptionMaterialsHasPlaintextDataKey",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_EncryptionMaterials(
            input
        ),
    )


def _serialize_decryption_materials_with_plaintext_data_key(
    input, config: Config
) -> DafnyRequest:
    return DafnyRequest(
        operation_name="DecryptionMaterialsWithPlaintextDataKey",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DecryptionMaterials(
            input
        ),
    )


def _serialize_get_algorithm_suite_info(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="GetAlgorithmSuiteInfo",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_GetAlgorithmSuiteInfoInput(
            input
        ),
    )


def _serialize_valid_algorithm_suite_info(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="ValidAlgorithmSuiteInfo",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_AlgorithmSuiteInfo(
            input
        ),
    )


def _serialize_validate_commitment_policy_on_encrypt(
    input, config: Config
) -> DafnyRequest:
    return DafnyRequest(
        operation_name="ValidateCommitmentPolicyOnEncrypt",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ValidateCommitmentPolicyOnEncryptInput(
            input
        ),
    )


def _serialize_validate_commitment_policy_on_decrypt(
    input, config: Config
) -> DafnyRequest:
    return DafnyRequest(
        operation_name="ValidateCommitmentPolicyOnDecrypt",
        dafny_operation_input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ValidateCommitmentPolicyOnDecryptInput(
            input
        ),
    )
