# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes import (
    AlgorithmSuiteInfo_AlgorithmSuiteInfo as DafnyAlgorithmSuiteInfo,
    CreateAwsKmsDiscoveryKeyringInput_CreateAwsKmsDiscoveryKeyringInput as DafnyCreateAwsKmsDiscoveryKeyringInput,
    CreateAwsKmsDiscoveryMultiKeyringInput_CreateAwsKmsDiscoveryMultiKeyringInput as DafnyCreateAwsKmsDiscoveryMultiKeyringInput,
    CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput as DafnyCreateAwsKmsEcdhKeyringInput,
    CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput as DafnyCreateAwsKmsHierarchicalKeyringInput,
    CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput as DafnyCreateAwsKmsKeyringInput,
    CreateAwsKmsMrkDiscoveryKeyringInput_CreateAwsKmsMrkDiscoveryKeyringInput as DafnyCreateAwsKmsMrkDiscoveryKeyringInput,
    CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput as DafnyCreateAwsKmsMrkDiscoveryMultiKeyringInput,
    CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput as DafnyCreateAwsKmsMrkKeyringInput,
    CreateAwsKmsMrkMultiKeyringInput_CreateAwsKmsMrkMultiKeyringInput as DafnyCreateAwsKmsMrkMultiKeyringInput,
    CreateAwsKmsMultiKeyringInput_CreateAwsKmsMultiKeyringInput as DafnyCreateAwsKmsMultiKeyringInput,
    CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput as DafnyCreateAwsKmsRsaKeyringInput,
    CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput as DafnyCreateCryptographicMaterialsCacheInput,
    CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput as DafnyCreateDefaultClientSupplierInput,
    CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput as DafnyCreateDefaultCryptographicMaterialsManagerInput,
    CreateMultiKeyringInput_CreateMultiKeyringInput as DafnyCreateMultiKeyringInput,
    CreateRawAesKeyringInput_CreateRawAesKeyringInput as DafnyCreateRawAesKeyringInput,
    CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput as DafnyCreateRawEcdhKeyringInput,
    CreateRawRsaKeyringInput_CreateRawRsaKeyringInput as DafnyCreateRawRsaKeyringInput,
    CreateRequiredEncryptionContextCMMInput_CreateRequiredEncryptionContextCMMInput as DafnyCreateRequiredEncryptionContextCMMInput,
    DecryptionMaterials_DecryptionMaterials as DafnyDecryptionMaterials,
    EncryptionMaterials_EncryptionMaterials as DafnyEncryptionMaterials,
    InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput as DafnyInitializeDecryptionMaterialsInput,
    InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput as DafnyInitializeEncryptionMaterialsInput,
    ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput as DafnyValidDecryptionMaterialsTransitionInput,
    ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput as DafnyValidEncryptionMaterialsTransitionInput,
    ValidateCommitmentPolicyOnDecryptInput_ValidateCommitmentPolicyOnDecryptInput as DafnyValidateCommitmentPolicyOnDecryptInput,
    ValidateCommitmentPolicyOnEncryptInput_ValidateCommitmentPolicyOnEncryptInput as DafnyValidateCommitmentPolicyOnEncryptInput,
)
import aws_cryptographic_material_providers.internaldafny.generated.module_
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.errors
from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.errors import (
    CollectionOfErrors,
    OpaqueError,
    ServiceError,
    _smithy_error_to_dafny_error,
)
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny
from typing import Any


import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.client as client_impl


class MaterialProvidersShim(
    aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient
):
    def __init__(self, _impl: client_impl):
        self._impl = _impl

    def CreateAwsKmsKeyring(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsKeyringInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsKeyringInput(
                input
            )
            smithy_client_response = self._impl.create_aws_kms_keyring(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateAwsKmsDiscoveryKeyring(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsDiscoveryKeyringInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsDiscoveryKeyringInput(
                input
            )
            smithy_client_response = self._impl.create_aws_kms_discovery_keyring(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateAwsKmsMultiKeyring(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsMultiKeyringInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsMultiKeyringInput(
                input
            )
            smithy_client_response = self._impl.create_aws_kms_multi_keyring(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateAwsKmsDiscoveryMultiKeyring(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsDiscoveryMultiKeyringInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsDiscoveryMultiKeyringInput(
                input
            )
            smithy_client_response = self._impl.create_aws_kms_discovery_multi_keyring(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateAwsKmsMrkKeyring(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsMrkKeyringInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsMrkKeyringInput(
                input
            )
            smithy_client_response = self._impl.create_aws_kms_mrk_keyring(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateAwsKmsMrkMultiKeyring(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsMrkMultiKeyringInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsMrkMultiKeyringInput(
                input
            )
            smithy_client_response = self._impl.create_aws_kms_mrk_multi_keyring(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateAwsKmsMrkDiscoveryKeyring(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsMrkDiscoveryKeyringInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryKeyringInput(
                input
            )
            smithy_client_response = self._impl.create_aws_kms_mrk_discovery_keyring(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateAwsKmsMrkDiscoveryMultiKeyring(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsMrkDiscoveryMultiKeyringInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryMultiKeyringInput(
                input
            )
            smithy_client_response = (
                self._impl.create_aws_kms_mrk_discovery_multi_keyring(
                    smithy_client_request
                )
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateAwsKmsHierarchicalKeyring(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsHierarchicalKeyringInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsHierarchicalKeyringInput(
                input
            )
            smithy_client_response = self._impl.create_aws_kms_hierarchical_keyring(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateAwsKmsRsaKeyring(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsRsaKeyringInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsRsaKeyringInput(
                input
            )
            smithy_client_response = self._impl.create_aws_kms_rsa_keyring(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateAwsKmsEcdhKeyring(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsEcdhKeyringInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsEcdhKeyringInput(
                input
            )
            smithy_client_response = self._impl.create_aws_kms_ecdh_keyring(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateMultiKeyring(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateMultiKeyringInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateMultiKeyringInput(
                input
            )
            smithy_client_response = self._impl.create_multi_keyring(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateRawAesKeyring(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateRawAesKeyringInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateRawAesKeyringInput(
                input
            )
            smithy_client_response = self._impl.create_raw_aes_keyring(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateRawRsaKeyring(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateRawRsaKeyringInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateRawRsaKeyringInput(
                input
            )
            smithy_client_response = self._impl.create_raw_rsa_keyring(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateRawEcdhKeyring(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateRawEcdhKeyringInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateRawEcdhKeyringInput(
                input
            )
            smithy_client_response = self._impl.create_raw_ecdh_keyring(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateDefaultCryptographicMaterialsManager(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateDefaultCryptographicMaterialsManagerInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateDefaultCryptographicMaterialsManagerInput(
                input
            )
            smithy_client_response = (
                self._impl.create_default_cryptographic_materials_manager(
                    smithy_client_request
                )
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateCryptographicMaterialsManagerOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateRequiredEncryptionContextCMM(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateRequiredEncryptionContextCMMInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMInput(
                input
            )
            smithy_client_response = self._impl.create_required_encryption_context_cmm(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateCryptographicMaterialsCache(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateCryptographicMaterialsCacheInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheInput(
                input
            )
            smithy_client_response = self._impl.create_cryptographic_materials_cache(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def CreateDefaultClientSupplier(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateDefaultClientSupplierInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateDefaultClientSupplierInput(
                input
            )
            smithy_client_response = self._impl.create_default_client_supplier(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateDefaultClientSupplierOutput(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def InitializeEncryptionMaterials(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.InitializeEncryptionMaterialsInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_InitializeEncryptionMaterialsInput(
                input
            )
            smithy_client_response = self._impl.initialize_encryption_materials(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_EncryptionMaterials(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def InitializeDecryptionMaterials(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.InitializeDecryptionMaterialsInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_InitializeDecryptionMaterialsInput(
                input
            )
            smithy_client_response = self._impl.initialize_decryption_materials(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DecryptionMaterials(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def ValidEncryptionMaterialsTransition(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.ValidEncryptionMaterialsTransitionInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ValidEncryptionMaterialsTransitionInput(
                input
            )
            smithy_client_response = self._impl.valid_encryption_materials_transition(
                smithy_client_request
            )
            return Wrappers.Result_Success(None)
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def ValidDecryptionMaterialsTransition(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.ValidDecryptionMaterialsTransitionInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ValidDecryptionMaterialsTransitionInput(
                input
            )
            smithy_client_response = self._impl.valid_decryption_materials_transition(
                smithy_client_request
            )
            return Wrappers.Result_Success(None)
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def EncryptionMaterialsHasPlaintextDataKey(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.EncryptionMaterials
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_EncryptionMaterials(
                input
            )
            smithy_client_response = (
                self._impl.encryption_materials_has_plaintext_data_key(
                    smithy_client_request
                )
            )
            return Wrappers.Result_Success(None)
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def DecryptionMaterialsWithPlaintextDataKey(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DecryptionMaterials
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DecryptionMaterials(
                input
            )
            smithy_client_response = (
                self._impl.decryption_materials_with_plaintext_data_key(
                    smithy_client_request
                )
            )
            return Wrappers.Result_Success(None)
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def GetAlgorithmSuiteInfo(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetAlgorithmSuiteInfoInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_GetAlgorithmSuiteInfoInput(
                input
            )
            smithy_client_response = self._impl.get_algorithm_suite_info(
                smithy_client_request
            )
            return Wrappers.Result_Success(
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_AlgorithmSuiteInfo(
                    smithy_client_response
                )
            )
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def ValidAlgorithmSuiteInfo(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.AlgorithmSuiteInfo
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_AlgorithmSuiteInfo(
                input
            )
            smithy_client_response = self._impl.valid_algorithm_suite_info(
                smithy_client_request
            )
            return Wrappers.Result_Success(None)
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def ValidateCommitmentPolicyOnEncrypt(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.ValidateCommitmentPolicyOnEncryptInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ValidateCommitmentPolicyOnEncryptInput(
                input
            )
            smithy_client_response = self._impl.validate_commitment_policy_on_encrypt(
                smithy_client_request
            )
            return Wrappers.Result_Success(None)
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

    def ValidateCommitmentPolicyOnDecrypt(self, input):
        try:
            smithy_client_request: (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.ValidateCommitmentPolicyOnDecryptInput
            ) = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ValidateCommitmentPolicyOnDecryptInput(
                input
            )
            smithy_client_response = self._impl.validate_commitment_policy_on_decrypt(
                smithy_client_request
            )
            return Wrappers.Result_Success(None)
        except Exception as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))
