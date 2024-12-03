# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from _dafny import Map, Seq
from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes import (
    AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16,
    AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16,
    AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16,
    AlgorithmSuiteId_DBE,
    AlgorithmSuiteId_ESDK,
    AlgorithmSuiteInfo_AlgorithmSuiteInfo as DafnyAlgorithmSuiteInfo,
    CacheType_Default,
    CacheType_MultiThreaded,
    CacheType_No,
    CacheType_Shared,
    CacheType_SingleThreaded,
    CacheType_StormTracking,
    CommitmentPolicy_DBE,
    CommitmentPolicy_ESDK,
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
    DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384,
    DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384,
    DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT,
    DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING as DafnyDIRECT_KEY_WRAPPING,
    DecryptMaterialsInput_DecryptMaterialsInput as DafnyDecryptMaterialsInput,
    DecryptMaterialsOutput_DecryptMaterialsOutput as DafnyDecryptMaterialsOutput,
    DecryptionMaterials_DecryptionMaterials as DafnyDecryptionMaterials,
    DefaultCache_DefaultCache as DafnyDefaultCache,
    DeleteCacheEntryInput_DeleteCacheEntryInput as DafnyDeleteCacheEntryInput,
    DerivationAlgorithm_HKDF,
    DerivationAlgorithm_IDENTITY,
    DerivationAlgorithm_None,
    DiscoveryFilter_DiscoveryFilter as DafnyDiscoveryFilter,
    ECDSA_ECDSA as DafnyECDSA,
    ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256,
    ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256,
    ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF,
    ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256,
    ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384,
    ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF,
    ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY,
    ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384,
    ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256,
    ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384,
    ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF,
    ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT,
    ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT,
    ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT,
    EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING,
    EdkWrappingAlgorithm_IntermediateKeyWrapping,
    Encrypt_AES__GCM,
    EncryptedDataKey_EncryptedDataKey as DafnyEncryptedDataKey,
    EncryptionMaterials_EncryptionMaterials as DafnyEncryptionMaterials,
    EphemeralPrivateKeyToStaticPublicKeyInput_EphemeralPrivateKeyToStaticPublicKeyInput as DafnyEphemeralPrivateKeyToStaticPublicKeyInput,
    GetBranchKeyIdInput_GetBranchKeyIdInput as DafnyGetBranchKeyIdInput,
    GetBranchKeyIdOutput_GetBranchKeyIdOutput as DafnyGetBranchKeyIdOutput,
    GetCacheEntryInput_GetCacheEntryInput as DafnyGetCacheEntryInput,
    GetCacheEntryOutput_GetCacheEntryOutput as DafnyGetCacheEntryOutput,
    GetClientInput_GetClientInput as DafnyGetClientInput,
    GetEncryptionMaterialsInput_GetEncryptionMaterialsInput as DafnyGetEncryptionMaterialsInput,
    GetEncryptionMaterialsOutput_GetEncryptionMaterialsOutput as DafnyGetEncryptionMaterialsOutput,
    HKDF_HKDF as DafnyHKDF,
    IDENTITY_IDENTITY as DafnyIDENTITY,
    InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput as DafnyInitializeDecryptionMaterialsInput,
    InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput as DafnyInitializeEncryptionMaterialsInput,
    IntermediateKeyWrapping_IntermediateKeyWrapping as DafnyIntermediateKeyWrapping,
    KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey,
    KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery,
    KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput as DafnyKmsPrivateKeyToStaticPublicKeyInput,
    KmsPublicKeyDiscoveryInput_KmsPublicKeyDiscoveryInput as DafnyKmsPublicKeyDiscoveryInput,
    MaterialProvidersConfig_MaterialProvidersConfig as DafnyMaterialProvidersConfig,
    Materials_BeaconKey,
    Materials_BranchKey,
    Materials_Decryption,
    Materials_Encryption,
    MultiThreadedCache_MultiThreadedCache as DafnyMultiThreadedCache,
    NoCache_NoCache as DafnyNoCache,
    None__None as DafnyNone,
    OnDecryptInput_OnDecryptInput as DafnyOnDecryptInput,
    OnDecryptOutput_OnDecryptOutput as DafnyOnDecryptOutput,
    OnEncryptInput_OnEncryptInput as DafnyOnEncryptInput,
    OnEncryptOutput_OnEncryptOutput as DafnyOnEncryptOutput,
    PaddingScheme_OAEP__SHA1__MGF1,
    PaddingScheme_OAEP__SHA256__MGF1,
    PaddingScheme_OAEP__SHA384__MGF1,
    PaddingScheme_OAEP__SHA512__MGF1,
    PaddingScheme_PKCS1,
    PublicKeyDiscoveryInput_PublicKeyDiscoveryInput as DafnyPublicKeyDiscoveryInput,
    PutCacheEntryInput_PutCacheEntryInput as DafnyPutCacheEntryInput,
    RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey,
    RawEcdhStaticConfigurations_PublicKeyDiscovery,
    RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey,
    RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput as DafnyRawPrivateKeyToStaticPublicKeyInput,
    SignatureAlgorithm_ECDSA,
    SignatureAlgorithm_None,
    SingleThreadedCache_SingleThreadedCache as DafnySingleThreadedCache,
    StormTrackingCache_StormTrackingCache as DafnyStormTrackingCache,
    SymmetricSignatureAlgorithm_HMAC,
    SymmetricSignatureAlgorithm_None,
    TimeUnits_Milliseconds,
    TimeUnits_Seconds,
    UpdateUsageMetadataInput_UpdateUsageMetadataInput as DafnyUpdateUsageMetadataInput,
    ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput as DafnyValidDecryptionMaterialsTransitionInput,
    ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput as DafnyValidEncryptionMaterialsTransitionInput,
    ValidateCommitmentPolicyOnDecryptInput_ValidateCommitmentPolicyOnDecryptInput as DafnyValidateCommitmentPolicyOnDecryptInput,
    ValidateCommitmentPolicyOnEncryptInput_ValidateCommitmentPolicyOnEncryptInput as DafnyValidateCommitmentPolicyOnEncryptInput,
)
import aws_cryptographic_material_providers.internaldafny.generated.module_
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny
from aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes import (
    IKMSClient,
)
import aws_cryptography_internal_kms.internaldafny.generated.module_
import aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny
import aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny
from smithy_dafny_standard_library.internaldafny.generated.Wrappers import (
    Option_None,
    Option_Some,
)


def aws_cryptography_materialproviders_GetBranchKeyIdInput(native_input):
    return DafnyGetBranchKeyIdInput(
        encryptionContext=Map(
            {
                Seq(key.encode("utf-8")): Seq(value.encode("utf-8"))
                for (key, value) in native_input.encryption_context.items()
            }
        ),
    )


def aws_cryptography_materialproviders_GetBranchKeyIdOutput(native_input):
    return DafnyGetBranchKeyIdOutput(
        branchKeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.branch_key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_materialproviders_GetClientInput(native_input):
    return DafnyGetClientInput(
        region=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.region.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_materialproviders_GetClientOutput(native_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KmsClientReference(
        native_input
    )


def aws_cryptography_materialproviders_KmsClientReference(native_input):
    import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms

    client = aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms.default__.KMSClient(
        boto_client=native_input
    )
    client.value.impl = native_input
    return client.value


def aws_cryptography_materialproviders_PutCacheEntryInput(native_input):
    return DafnyPutCacheEntryInput(
        identifier=Seq(native_input.identifier),
        materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_Materials(
            native_input.materials
        ),
        creationTime=native_input.creation_time,
        expiryTime=native_input.expiry_time,
        messagesUsed=(
            (Option_Some(native_input.messages_used))
            if (native_input.messages_used is not None)
            else (Option_None())
        ),
        bytesUsed=(
            (Option_Some(native_input.bytes_used))
            if (native_input.bytes_used is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_Materials(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.MaterialsEncryption,
    ):
        Materials_union_value = Materials_Encryption(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_EncryptionMaterials(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.MaterialsDecryption,
    ):
        Materials_union_value = Materials_Decryption(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DecryptionMaterials(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.MaterialsBranchKey,
    ):
        Materials_union_value = Materials_BranchKey(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_BranchKeyMaterials(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.MaterialsBeaconKey,
    ):
        Materials_union_value = Materials_BeaconKey(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_BeaconKeyMaterials(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return Materials_union_value


def aws_cryptography_materialproviders_EncryptionMaterials(native_input):
    return DafnyEncryptionMaterials(
        algorithmSuite=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_AlgorithmSuiteInfo(
            native_input.algorithm_suite
        ),
        encryptionContext=Map(
            {
                Seq(key.encode("utf-8")): Seq(value.encode("utf-8"))
                for (key, value) in native_input.encryption_context.items()
            }
        ),
        encryptedDataKeys=Seq(
            [
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_EncryptedDataKey(
                    list_element
                )
                for list_element in native_input.encrypted_data_keys
            ]
        ),
        requiredEncryptionContextKeys=Seq(
            [
                Seq(list_element.encode("utf-8"))
                for list_element in native_input.required_encryption_context_keys
            ]
        ),
        plaintextDataKey=(
            (Option_Some(Seq(native_input.plaintext_data_key)))
            if (native_input.plaintext_data_key is not None)
            else (Option_None())
        ),
        signingKey=(
            (Option_Some(Seq(native_input.signing_key)))
            if (native_input.signing_key is not None)
            else (Option_None())
        ),
        symmetricSigningKeys=(
            (
                Option_Some(
                    Seq(
                        [
                            Seq(list_element)
                            for list_element in native_input.symmetric_signing_keys
                        ]
                    )
                )
            )
            if (native_input.symmetric_signing_keys is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_DecryptionMaterials(native_input):
    return DafnyDecryptionMaterials(
        algorithmSuite=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_AlgorithmSuiteInfo(
            native_input.algorithm_suite
        ),
        encryptionContext=Map(
            {
                Seq(key.encode("utf-8")): Seq(value.encode("utf-8"))
                for (key, value) in native_input.encryption_context.items()
            }
        ),
        requiredEncryptionContextKeys=Seq(
            [
                Seq(list_element.encode("utf-8"))
                for list_element in native_input.required_encryption_context_keys
            ]
        ),
        plaintextDataKey=(
            (Option_Some(Seq(native_input.plaintext_data_key)))
            if (native_input.plaintext_data_key is not None)
            else (Option_None())
        ),
        verificationKey=(
            (Option_Some(Seq(native_input.verification_key)))
            if (native_input.verification_key is not None)
            else (Option_None())
        ),
        symmetricSigningKey=(
            (Option_Some(Seq(native_input.symmetric_signing_key)))
            if (native_input.symmetric_signing_key is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_AlgorithmSuiteInfo(native_input):
    return DafnyAlgorithmSuiteInfo(
        id=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_AlgorithmSuiteId(
            native_input.id
        ),
        binaryId=Seq(native_input.binary_id),
        messageVersion=native_input.message_version,
        encrypt=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_Encrypt(
            native_input.encrypt
        ),
        kdf=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DerivationAlgorithm(
            native_input.kdf
        ),
        commitment=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DerivationAlgorithm(
            native_input.commitment
        ),
        signature=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_SignatureAlgorithm(
            native_input.signature
        ),
        symmetricSignature=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_SymmetricSignatureAlgorithm(
            native_input.symmetric_signature
        ),
        edkWrapping=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_EdkWrappingAlgorithm(
            native_input.edk_wrapping
        ),
    )


def aws_cryptography_materialproviders_EncryptedDataKey(native_input):
    return DafnyEncryptedDataKey(
        keyProviderId=Seq(native_input.key_provider_id.encode("utf-8")),
        keyProviderInfo=Seq(native_input.key_provider_info),
        ciphertext=Seq(native_input.ciphertext),
    )


def aws_cryptography_materialproviders_AlgorithmSuiteId(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.AlgorithmSuiteIdESDK,
    ):
        AlgorithmSuiteId_union_value = AlgorithmSuiteId_ESDK(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ESDKAlgorithmSuiteId(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.AlgorithmSuiteIdDBE,
    ):
        AlgorithmSuiteId_union_value = AlgorithmSuiteId_DBE(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DBEAlgorithmSuiteId(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return AlgorithmSuiteId_union_value


def aws_cryptography_materialproviders_Encrypt(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.EncryptAES_GCM,
    ):
        Encrypt_union_value = Encrypt_AES__GCM(
            aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_AES_GCM(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return Encrypt_union_value


def aws_cryptography_materialproviders_DerivationAlgorithm(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DerivationAlgorithmHKDF,
    ):
        DerivationAlgorithm_union_value = DerivationAlgorithm_HKDF(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_HKDF(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DerivationAlgorithmIDENTITY,
    ):
        DerivationAlgorithm_union_value = DerivationAlgorithm_IDENTITY(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_IDENTITY(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DerivationAlgorithmNone,
    ):
        DerivationAlgorithm_union_value = DerivationAlgorithm_None(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_None(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return DerivationAlgorithm_union_value


def aws_cryptography_materialproviders_SignatureAlgorithm(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.SignatureAlgorithmECDSA,
    ):
        SignatureAlgorithm_union_value = SignatureAlgorithm_ECDSA(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ECDSA(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.SignatureAlgorithmNone,
    ):
        SignatureAlgorithm_union_value = SignatureAlgorithm_None(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_None(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return SignatureAlgorithm_union_value


def aws_cryptography_materialproviders_SymmetricSignatureAlgorithm(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.SymmetricSignatureAlgorithmHMAC,
    ):
        SymmetricSignatureAlgorithm_union_value = SymmetricSignatureAlgorithm_HMAC(
            aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_DigestAlgorithm(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.SymmetricSignatureAlgorithmNone,
    ):
        SymmetricSignatureAlgorithm_union_value = SymmetricSignatureAlgorithm_None(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_None(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return SymmetricSignatureAlgorithm_union_value


def aws_cryptography_materialproviders_EdkWrappingAlgorithm(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.EdkWrappingAlgorithmDIRECT_KEY_WRAPPING,
    ):
        EdkWrappingAlgorithm_union_value = EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DIRECT_KEY_WRAPPING(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.EdkWrappingAlgorithmIntermediateKeyWrapping,
    ):
        EdkWrappingAlgorithm_union_value = EdkWrappingAlgorithm_IntermediateKeyWrapping(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_IntermediateKeyWrapping(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return EdkWrappingAlgorithm_union_value


def aws_cryptography_materialproviders_ESDKAlgorithmSuiteId(native_input):
    if native_input == "0x0014":
        return ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF()

    elif native_input == "0x0046":
        return ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF()

    elif native_input == "0x0078":
        return ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF()

    elif native_input == "0x0114":
        return ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256()

    elif native_input == "0x0146":
        return ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256()

    elif native_input == "0x0178":
        return ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256()

    elif native_input == "0x0214":
        return (
            ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256()
        )

    elif native_input == "0x0346":
        return (
            ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()
        )

    elif native_input == "0x0378":
        return (
            ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()
        )

    elif native_input == "0x0478":
        return ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY()

    elif native_input == "0x0578":
        return (
            ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384()
        )

    else:
        raise ValueError(f"No recognized enum value in enum type: {native_input=}")


def aws_cryptography_materialproviders_DBEAlgorithmSuiteId(native_input):
    if native_input == "0x6700":
        return (
            DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384()
        )

    elif native_input == "0x6701":
        return (
            DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384()
        )

    else:
        raise ValueError(f"No recognized enum value in enum type: {native_input=}")


def aws_cryptography_materialproviders_HKDF(native_input):
    return DafnyHKDF(
        hmac=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_DigestAlgorithm(
            native_input.hmac
        ),
        saltLength=native_input.salt_length,
        inputKeyLength=native_input.input_key_length,
        outputKeyLength=native_input.output_key_length,
    )


def aws_cryptography_materialproviders_IDENTITY(native_input):
    return DafnyIDENTITY()


def aws_cryptography_materialproviders_None(native_input):
    return DafnyNone()


def aws_cryptography_materialproviders_ECDSA(native_input):
    return DafnyECDSA(
        curve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDSASignatureAlgorithm(
            native_input.curve
        ),
    )


def aws_cryptography_materialproviders_DIRECT_KEY_WRAPPING(native_input):
    return DafnyDIRECT_KEY_WRAPPING()


def aws_cryptography_materialproviders_IntermediateKeyWrapping(native_input):
    return DafnyIntermediateKeyWrapping(
        keyEncryptionKeyKdf=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DerivationAlgorithm(
            native_input.key_encryption_key_kdf
        ),
        macKeyKdf=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DerivationAlgorithm(
            native_input.mac_key_kdf
        ),
        pdkEncryptAlgorithm=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_Encrypt(
            native_input.pdk_encrypt_algorithm
        ),
    )


def smithy_api_Unit(native_input):
    return None


def aws_cryptography_materialproviders_GetCacheEntryInput(native_input):
    return DafnyGetCacheEntryInput(
        identifier=Seq(native_input.identifier),
        bytesUsed=(
            (Option_Some(native_input.bytes_used))
            if (native_input.bytes_used is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_GetCacheEntryOutput(native_input):
    return DafnyGetCacheEntryOutput(
        materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_Materials(
            native_input.materials
        ),
        creationTime=native_input.creation_time,
        expiryTime=native_input.expiry_time,
        messagesUsed=native_input.messages_used,
        bytesUsed=native_input.bytes_used,
    )


def aws_cryptography_materialproviders_UpdateUsageMetadataInput(native_input):
    return DafnyUpdateUsageMetadataInput(
        identifier=Seq(native_input.identifier),
        bytesUsed=native_input.bytes_used,
    )


def aws_cryptography_materialproviders_DeleteCacheEntryInput(native_input):
    return DafnyDeleteCacheEntryInput(
        identifier=Seq(native_input.identifier),
    )


def aws_cryptography_materialproviders_GetEncryptionMaterialsInput(native_input):
    return DafnyGetEncryptionMaterialsInput(
        encryptionContext=Map(
            {
                Seq(key.encode("utf-8")): Seq(value.encode("utf-8"))
                for (key, value) in native_input.encryption_context.items()
            }
        ),
        commitmentPolicy=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CommitmentPolicy(
            native_input.commitment_policy
        ),
        algorithmSuiteId=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_AlgorithmSuiteId(
                        native_input.algorithm_suite_id
                    )
                )
            )
            if (native_input.algorithm_suite_id is not None)
            else (Option_None())
        ),
        maxPlaintextLength=(
            (Option_Some(native_input.max_plaintext_length))
            if (native_input.max_plaintext_length is not None)
            else (Option_None())
        ),
        requiredEncryptionContextKeys=(
            (
                Option_Some(
                    Seq(
                        [
                            Seq(list_element.encode("utf-8"))
                            for list_element in native_input.required_encryption_context_keys
                        ]
                    )
                )
            )
            if (native_input.required_encryption_context_keys is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_CommitmentPolicy(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CommitmentPolicyESDK,
    ):
        CommitmentPolicy_union_value = CommitmentPolicy_ESDK(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ESDKCommitmentPolicy(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CommitmentPolicyDBE,
    ):
        CommitmentPolicy_union_value = CommitmentPolicy_DBE(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DBECommitmentPolicy(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return CommitmentPolicy_union_value


def aws_cryptography_materialproviders_ESDKCommitmentPolicy(native_input):
    if native_input == "FORBID_ENCRYPT_ALLOW_DECRYPT":
        return ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT()

    elif native_input == "REQUIRE_ENCRYPT_ALLOW_DECRYPT":
        return ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT()

    elif native_input == "REQUIRE_ENCRYPT_REQUIRE_DECRYPT":
        return ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT()

    else:
        raise ValueError(f"No recognized enum value in enum type: {native_input=}")


def aws_cryptography_materialproviders_DBECommitmentPolicy(native_input):
    if native_input == "REQUIRE_ENCRYPT_REQUIRE_DECRYPT":
        return DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT()

    else:
        raise ValueError(f"No recognized enum value in enum type: {native_input=}")


def aws_cryptography_materialproviders_GetEncryptionMaterialsOutput(native_input):
    return DafnyGetEncryptionMaterialsOutput(
        encryptionMaterials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_EncryptionMaterials(
            native_input.encryption_materials
        ),
    )


def aws_cryptography_materialproviders_DecryptMaterialsInput(native_input):
    return DafnyDecryptMaterialsInput(
        algorithmSuiteId=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_AlgorithmSuiteId(
            native_input.algorithm_suite_id
        ),
        commitmentPolicy=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CommitmentPolicy(
            native_input.commitment_policy
        ),
        encryptedDataKeys=Seq(
            [
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_EncryptedDataKey(
                    list_element
                )
                for list_element in native_input.encrypted_data_keys
            ]
        ),
        encryptionContext=Map(
            {
                Seq(key.encode("utf-8")): Seq(value.encode("utf-8"))
                for (key, value) in native_input.encryption_context.items()
            }
        ),
        reproducedEncryptionContext=(
            (
                Option_Some(
                    Map(
                        {
                            Seq(key.encode("utf-8")): Seq(value.encode("utf-8"))
                            for (
                                key,
                                value,
                            ) in native_input.reproduced_encryption_context.items()
                        }
                    )
                )
            )
            if (native_input.reproduced_encryption_context is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_DecryptMaterialsOutput(native_input):
    return DafnyDecryptMaterialsOutput(
        decryptionMaterials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DecryptionMaterials(
            native_input.decryption_materials
        ),
    )


def aws_cryptography_materialproviders_OnEncryptInput(native_input):
    return DafnyOnEncryptInput(
        materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_EncryptionMaterials(
            native_input.materials
        ),
    )


def aws_cryptography_materialproviders_OnEncryptOutput(native_input):
    return DafnyOnEncryptOutput(
        materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_EncryptionMaterials(
            native_input.materials
        ),
    )


def aws_cryptography_materialproviders_OnDecryptInput(native_input):
    return DafnyOnDecryptInput(
        materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DecryptionMaterials(
            native_input.materials
        ),
        encryptedDataKeys=Seq(
            [
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_EncryptedDataKey(
                    list_element
                )
                for list_element in native_input.encrypted_data_keys
            ]
        ),
    )


def aws_cryptography_materialproviders_OnDecryptOutput(native_input):
    return DafnyOnDecryptOutput(
        materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DecryptionMaterials(
            native_input.materials
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsKeyringInput(native_input):
    return DafnyCreateAwsKmsKeyringInput(
        kmsKeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.kms_key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        kmsClient=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KmsClientReference(
            native_input.kms_client
        ),
        grantTokens=(
            (
                Option_Some(
                    Seq(
                        [
                            Seq(
                                "".join(
                                    [
                                        chr(int.from_bytes(pair, "big"))
                                        for pair in zip(
                                            *[iter(list_element.encode("utf-16-be"))]
                                            * 2
                                        )
                                    ]
                                )
                            )
                            for list_element in native_input.grant_tokens
                        ]
                    )
                )
            )
            if (native_input.grant_tokens is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsDiscoveryKeyringInput(native_input):
    return DafnyCreateAwsKmsDiscoveryKeyringInput(
        kmsClient=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KmsClientReference(
            native_input.kms_client
        ),
        discoveryFilter=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DiscoveryFilter(
                        native_input.discovery_filter
                    )
                )
            )
            if (native_input.discovery_filter is not None)
            else (Option_None())
        ),
        grantTokens=(
            (
                Option_Some(
                    Seq(
                        [
                            Seq(
                                "".join(
                                    [
                                        chr(int.from_bytes(pair, "big"))
                                        for pair in zip(
                                            *[iter(list_element.encode("utf-16-be"))]
                                            * 2
                                        )
                                    ]
                                )
                            )
                            for list_element in native_input.grant_tokens
                        ]
                    )
                )
            )
            if (native_input.grant_tokens is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_DiscoveryFilter(native_input):
    return DafnyDiscoveryFilter(
        accountIds=Seq(
            [
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(list_element.encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
                for list_element in native_input.account_ids
            ]
        ),
        partition=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.partition.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsMultiKeyringInput(native_input):
    return DafnyCreateAwsKmsMultiKeyringInput(
        generator=(
            (
                Option_Some(
                    Seq(
                        "".join(
                            [
                                chr(int.from_bytes(pair, "big"))
                                for pair in zip(
                                    *[iter(native_input.generator.encode("utf-16-be"))]
                                    * 2
                                )
                            ]
                        )
                    )
                )
            )
            if (native_input.generator is not None)
            else (Option_None())
        ),
        kmsKeyIds=(
            (
                Option_Some(
                    Seq(
                        [
                            Seq(
                                "".join(
                                    [
                                        chr(int.from_bytes(pair, "big"))
                                        for pair in zip(
                                            *[iter(list_element.encode("utf-16-be"))]
                                            * 2
                                        )
                                    ]
                                )
                            )
                            for list_element in native_input.kms_key_ids
                        ]
                    )
                )
            )
            if (native_input.kms_key_ids is not None)
            else (Option_None())
        ),
        clientSupplier=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ClientSupplierReference(
                        native_input.client_supplier
                    )
                )
            )
            if (
                (native_input.client_supplier is not None)
                and (
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ClientSupplierReference(
                        native_input.client_supplier
                    )
                    is not None
                )
            )
            else (Option_None())
        ),
        grantTokens=(
            (
                Option_Some(
                    Seq(
                        [
                            Seq(
                                "".join(
                                    [
                                        chr(int.from_bytes(pair, "big"))
                                        for pair in zip(
                                            *[iter(list_element.encode("utf-16-be"))]
                                            * 2
                                        )
                                    ]
                                )
                            )
                            for list_element in native_input.grant_tokens
                        ]
                    )
                )
            )
            if (native_input.grant_tokens is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_ClientSupplierReference(native_input):
    if hasattr(native_input, "_impl"):
        return native_input._impl

    else:
        return native_input


def aws_cryptography_materialproviders_CreateAwsKmsDiscoveryMultiKeyringInput(
    native_input,
):
    return DafnyCreateAwsKmsDiscoveryMultiKeyringInput(
        regions=Seq(
            [
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(list_element.encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
                for list_element in native_input.regions
            ]
        ),
        discoveryFilter=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DiscoveryFilter(
                        native_input.discovery_filter
                    )
                )
            )
            if (native_input.discovery_filter is not None)
            else (Option_None())
        ),
        clientSupplier=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ClientSupplierReference(
                        native_input.client_supplier
                    )
                )
            )
            if (
                (native_input.client_supplier is not None)
                and (
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ClientSupplierReference(
                        native_input.client_supplier
                    )
                    is not None
                )
            )
            else (Option_None())
        ),
        grantTokens=(
            (
                Option_Some(
                    Seq(
                        [
                            Seq(
                                "".join(
                                    [
                                        chr(int.from_bytes(pair, "big"))
                                        for pair in zip(
                                            *[iter(list_element.encode("utf-16-be"))]
                                            * 2
                                        )
                                    ]
                                )
                            )
                            for list_element in native_input.grant_tokens
                        ]
                    )
                )
            )
            if (native_input.grant_tokens is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsMrkKeyringInput(native_input):
    return DafnyCreateAwsKmsMrkKeyringInput(
        kmsKeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.kms_key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        kmsClient=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KmsClientReference(
            native_input.kms_client
        ),
        grantTokens=(
            (
                Option_Some(
                    Seq(
                        [
                            Seq(
                                "".join(
                                    [
                                        chr(int.from_bytes(pair, "big"))
                                        for pair in zip(
                                            *[iter(list_element.encode("utf-16-be"))]
                                            * 2
                                        )
                                    ]
                                )
                            )
                            for list_element in native_input.grant_tokens
                        ]
                    )
                )
            )
            if (native_input.grant_tokens is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsMrkMultiKeyringInput(native_input):
    return DafnyCreateAwsKmsMrkMultiKeyringInput(
        generator=(
            (
                Option_Some(
                    Seq(
                        "".join(
                            [
                                chr(int.from_bytes(pair, "big"))
                                for pair in zip(
                                    *[iter(native_input.generator.encode("utf-16-be"))]
                                    * 2
                                )
                            ]
                        )
                    )
                )
            )
            if (native_input.generator is not None)
            else (Option_None())
        ),
        kmsKeyIds=(
            (
                Option_Some(
                    Seq(
                        [
                            Seq(
                                "".join(
                                    [
                                        chr(int.from_bytes(pair, "big"))
                                        for pair in zip(
                                            *[iter(list_element.encode("utf-16-be"))]
                                            * 2
                                        )
                                    ]
                                )
                            )
                            for list_element in native_input.kms_key_ids
                        ]
                    )
                )
            )
            if (native_input.kms_key_ids is not None)
            else (Option_None())
        ),
        clientSupplier=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ClientSupplierReference(
                        native_input.client_supplier
                    )
                )
            )
            if (
                (native_input.client_supplier is not None)
                and (
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ClientSupplierReference(
                        native_input.client_supplier
                    )
                    is not None
                )
            )
            else (Option_None())
        ),
        grantTokens=(
            (
                Option_Some(
                    Seq(
                        [
                            Seq(
                                "".join(
                                    [
                                        chr(int.from_bytes(pair, "big"))
                                        for pair in zip(
                                            *[iter(list_element.encode("utf-16-be"))]
                                            * 2
                                        )
                                    ]
                                )
                            )
                            for list_element in native_input.grant_tokens
                        ]
                    )
                )
            )
            if (native_input.grant_tokens is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryKeyringInput(
    native_input,
):
    return DafnyCreateAwsKmsMrkDiscoveryKeyringInput(
        kmsClient=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KmsClientReference(
            native_input.kms_client
        ),
        discoveryFilter=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DiscoveryFilter(
                        native_input.discovery_filter
                    )
                )
            )
            if (native_input.discovery_filter is not None)
            else (Option_None())
        ),
        grantTokens=(
            (
                Option_Some(
                    Seq(
                        [
                            Seq(
                                "".join(
                                    [
                                        chr(int.from_bytes(pair, "big"))
                                        for pair in zip(
                                            *[iter(list_element.encode("utf-16-be"))]
                                            * 2
                                        )
                                    ]
                                )
                            )
                            for list_element in native_input.grant_tokens
                        ]
                    )
                )
            )
            if (native_input.grant_tokens is not None)
            else (Option_None())
        ),
        region=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.region.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryMultiKeyringInput(
    native_input,
):
    return DafnyCreateAwsKmsMrkDiscoveryMultiKeyringInput(
        regions=Seq(
            [
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(list_element.encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
                for list_element in native_input.regions
            ]
        ),
        discoveryFilter=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DiscoveryFilter(
                        native_input.discovery_filter
                    )
                )
            )
            if (native_input.discovery_filter is not None)
            else (Option_None())
        ),
        clientSupplier=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ClientSupplierReference(
                        native_input.client_supplier
                    )
                )
            )
            if (
                (native_input.client_supplier is not None)
                and (
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ClientSupplierReference(
                        native_input.client_supplier
                    )
                    is not None
                )
            )
            else (Option_None())
        ),
        grantTokens=(
            (
                Option_Some(
                    Seq(
                        [
                            Seq(
                                "".join(
                                    [
                                        chr(int.from_bytes(pair, "big"))
                                        for pair in zip(
                                            *[iter(list_element.encode("utf-16-be"))]
                                            * 2
                                        )
                                    ]
                                )
                            )
                            for list_element in native_input.grant_tokens
                        ]
                    )
                )
            )
            if (native_input.grant_tokens is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsHierarchicalKeyringInput(
    native_input,
):
    return DafnyCreateAwsKmsHierarchicalKeyringInput(
        branchKeyId=(
            (
                Option_Some(
                    Seq(
                        "".join(
                            [
                                chr(int.from_bytes(pair, "big"))
                                for pair in zip(
                                    *[
                                        iter(
                                            native_input.branch_key_id.encode(
                                                "utf-16-be"
                                            )
                                        )
                                    ]
                                    * 2
                                )
                            ]
                        )
                    )
                )
            )
            if (native_input.branch_key_id is not None)
            else (Option_None())
        ),
        branchKeyIdSupplier=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_BranchKeyIdSupplierReference(
                        native_input.branch_key_id_supplier
                    )
                )
            )
            if (
                (native_input.branch_key_id_supplier is not None)
                and (
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_BranchKeyIdSupplierReference(
                        native_input.branch_key_id_supplier
                    )
                    is not None
                )
            )
            else (Option_None())
        ),
        keyStore=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KeyStoreReference(
            native_input.key_store
        ),
        ttlSeconds=native_input.ttl_seconds,
        cache=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CacheType(
                        native_input.cache
                    )
                )
            )
            if (native_input.cache is not None)
            else (Option_None())
        ),
        partitionId=(
            (
                Option_Some(
                    Seq(
                        "".join(
                            [
                                chr(int.from_bytes(pair, "big"))
                                for pair in zip(
                                    *[
                                        iter(
                                            native_input.partition_id.encode(
                                                "utf-16-be"
                                            )
                                        )
                                    ]
                                    * 2
                                )
                            ]
                        )
                    )
                )
            )
            if (native_input.partition_id is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_BranchKeyIdSupplierReference(native_input):
    if hasattr(native_input, "_impl"):
        return native_input._impl

    else:
        return native_input


def aws_cryptography_materialproviders_KeyStoreReference(native_input):
    return native_input._config.dafnyImplInterface.impl


def aws_cryptography_materialproviders_CacheType(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CacheTypeDefault,
    ):
        CacheType_union_value = CacheType_Default(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DefaultCache(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CacheTypeNo,
    ):
        CacheType_union_value = CacheType_No(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_NoCache(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CacheTypeSingleThreaded,
    ):
        CacheType_union_value = CacheType_SingleThreaded(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_SingleThreadedCache(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CacheTypeMultiThreaded,
    ):
        CacheType_union_value = CacheType_MultiThreaded(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_MultiThreadedCache(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CacheTypeStormTracking,
    ):
        CacheType_union_value = CacheType_StormTracking(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_StormTrackingCache(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CacheTypeShared,
    ):
        CacheType_union_value = CacheType_Shared(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CryptographicMaterialsCacheReference(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return CacheType_union_value


def aws_cryptography_materialproviders_DefaultCache(native_input):
    return DafnyDefaultCache(
        entryCapacity=native_input.entry_capacity,
    )


def aws_cryptography_materialproviders_NoCache(native_input):
    return DafnyNoCache()


def aws_cryptography_materialproviders_SingleThreadedCache(native_input):
    return DafnySingleThreadedCache(
        entryCapacity=native_input.entry_capacity,
        entryPruningTailSize=(
            (Option_Some(native_input.entry_pruning_tail_size))
            if (native_input.entry_pruning_tail_size is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_MultiThreadedCache(native_input):
    return DafnyMultiThreadedCache(
        entryCapacity=native_input.entry_capacity,
        entryPruningTailSize=(
            (Option_Some(native_input.entry_pruning_tail_size))
            if (native_input.entry_pruning_tail_size is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_StormTrackingCache(native_input):
    return DafnyStormTrackingCache(
        entryCapacity=native_input.entry_capacity,
        entryPruningTailSize=(
            (Option_Some(native_input.entry_pruning_tail_size))
            if (native_input.entry_pruning_tail_size is not None)
            else (Option_None())
        ),
        gracePeriod=native_input.grace_period,
        graceInterval=native_input.grace_interval,
        fanOut=native_input.fan_out,
        inFlightTTL=native_input.in_flight_ttl,
        sleepMilli=native_input.sleep_milli,
        timeUnits=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_TimeUnits(
                        native_input.time_units
                    )
                )
            )
            if (native_input.time_units is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_CryptographicMaterialsCacheReference(
    native_input,
):
    if hasattr(native_input, "_impl"):
        return native_input._impl

    else:
        return native_input


def aws_cryptography_materialproviders_TimeUnits(native_input):
    if native_input == "Seconds":
        return TimeUnits_Seconds()

    elif native_input == "Milliseconds":
        return TimeUnits_Milliseconds()

    else:
        raise ValueError(f"No recognized enum value in enum type: {native_input=}")


def aws_cryptography_materialproviders_CreateAwsKmsRsaKeyringInput(native_input):
    return DafnyCreateAwsKmsRsaKeyringInput(
        publicKey=(
            (Option_Some(Seq(native_input.public_key)))
            if (native_input.public_key is not None)
            else (Option_None())
        ),
        kmsKeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.kms_key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        encryptionAlgorithm=aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(
            native_input.encryption_algorithm
        ),
        kmsClient=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KmsClientReference(
                        native_input.kms_client
                    )
                )
            )
            if (
                (native_input.kms_client is not None)
                and (
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KmsClientReference(
                        native_input.kms_client
                    )
                    is not None
                )
            )
            else (Option_None())
        ),
        grantTokens=(
            (
                Option_Some(
                    Seq(
                        [
                            Seq(
                                "".join(
                                    [
                                        chr(int.from_bytes(pair, "big"))
                                        for pair in zip(
                                            *[iter(list_element.encode("utf-16-be"))]
                                            * 2
                                        )
                                    ]
                                )
                            )
                            for list_element in native_input.grant_tokens
                        ]
                    )
                )
            )
            if (native_input.grant_tokens is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsEcdhKeyringInput(native_input):
    return DafnyCreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KmsEcdhStaticConfigurations(
            native_input.key_agreement_scheme
        ),
        curveSpec=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDHCurveSpec(
            native_input.curve_spec
        ),
        kmsClient=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KmsClientReference(
            native_input.kms_client
        ),
        grantTokens=(
            (
                Option_Some(
                    Seq(
                        [
                            Seq(
                                "".join(
                                    [
                                        chr(int.from_bytes(pair, "big"))
                                        for pair in zip(
                                            *[iter(list_element.encode("utf-16-be"))]
                                            * 2
                                        )
                                    ]
                                )
                            )
                            for list_element in native_input.grant_tokens
                        ]
                    )
                )
            )
            if (native_input.grant_tokens is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_KmsEcdhStaticConfigurations(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.KmsEcdhStaticConfigurationsKmsPublicKeyDiscovery,
    ):
        KmsEcdhStaticConfigurations_union_value = KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KmsPublicKeyDiscoveryInput(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.KmsEcdhStaticConfigurationsKmsPrivateKeyToStaticPublicKey,
    ):
        KmsEcdhStaticConfigurations_union_value = KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KmsPrivateKeyToStaticPublicKeyInput(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return KmsEcdhStaticConfigurations_union_value


def aws_cryptography_materialproviders_KmsPublicKeyDiscoveryInput(native_input):
    return DafnyKmsPublicKeyDiscoveryInput(
        recipientKmsIdentifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[
                            iter(
                                native_input.recipient_kms_identifier.encode(
                                    "utf-16-be"
                                )
                            )
                        ]
                        * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_materialproviders_KmsPrivateKeyToStaticPublicKeyInput(
    native_input,
):
    return DafnyKmsPrivateKeyToStaticPublicKeyInput(
        senderKmsIdentifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.sender_kms_identifier.encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
        senderPublicKey=(
            (Option_Some(Seq(native_input.sender_public_key)))
            if (native_input.sender_public_key is not None)
            else (Option_None())
        ),
        recipientPublicKey=Seq(native_input.recipient_public_key),
    )


def aws_cryptography_materialproviders_CreateMultiKeyringInput(native_input):
    return DafnyCreateMultiKeyringInput(
        generator=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KeyringReference(
                        native_input.generator
                    )
                )
            )
            if (
                (native_input.generator is not None)
                and (
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KeyringReference(
                        native_input.generator
                    )
                    is not None
                )
            )
            else (Option_None())
        ),
        childKeyrings=Seq(
            [
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KeyringReference(
                    list_element
                )
                for list_element in native_input.child_keyrings
            ]
        ),
    )


def aws_cryptography_materialproviders_KeyringReference(native_input):
    if hasattr(native_input, "_impl"):
        return native_input._impl

    else:
        return native_input


def aws_cryptography_materialproviders_CreateRawAesKeyringInput(native_input):
    return DafnyCreateRawAesKeyringInput(
        keyNamespace=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_namespace.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        keyName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_name.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        wrappingKey=Seq(native_input.wrapping_key),
        wrappingAlg=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_AesWrappingAlg(
            native_input.wrapping_alg
        ),
    )


def aws_cryptography_materialproviders_AesWrappingAlg(native_input):
    if native_input == "ALG_AES128_GCM_IV12_TAG16":
        return AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16()

    elif native_input == "ALG_AES192_GCM_IV12_TAG16":
        return AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16()

    elif native_input == "ALG_AES256_GCM_IV12_TAG16":
        return AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()

    else:
        raise ValueError(f"No recognized enum value in enum type: {native_input=}")


def aws_cryptography_materialproviders_CreateRawRsaKeyringInput(native_input):
    return DafnyCreateRawRsaKeyringInput(
        keyNamespace=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_namespace.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        keyName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_name.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        paddingScheme=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_PaddingScheme(
            native_input.padding_scheme
        ),
        publicKey=(
            (Option_Some(Seq(native_input.public_key)))
            if (native_input.public_key is not None)
            else (Option_None())
        ),
        privateKey=(
            (Option_Some(Seq(native_input.private_key)))
            if (native_input.private_key is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_PaddingScheme(native_input):
    if native_input == "PKCS1":
        return PaddingScheme_PKCS1()

    elif native_input == "OAEP_SHA1_MGF1":
        return PaddingScheme_OAEP__SHA1__MGF1()

    elif native_input == "OAEP_SHA256_MGF1":
        return PaddingScheme_OAEP__SHA256__MGF1()

    elif native_input == "OAEP_SHA384_MGF1":
        return PaddingScheme_OAEP__SHA384__MGF1()

    elif native_input == "OAEP_SHA512_MGF1":
        return PaddingScheme_OAEP__SHA512__MGF1()

    else:
        raise ValueError(f"No recognized enum value in enum type: {native_input=}")


def aws_cryptography_materialproviders_CreateRawEcdhKeyringInput(native_input):
    return DafnyCreateRawEcdhKeyringInput(
        KeyAgreementScheme=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_RawEcdhStaticConfigurations(
            native_input.key_agreement_scheme
        ),
        curveSpec=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDHCurveSpec(
            native_input.curve_spec
        ),
    )


def aws_cryptography_materialproviders_RawEcdhStaticConfigurations(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.RawEcdhStaticConfigurationsPublicKeyDiscovery,
    ):
        RawEcdhStaticConfigurations_union_value = RawEcdhStaticConfigurations_PublicKeyDiscovery(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_PublicKeyDiscoveryInput(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.RawEcdhStaticConfigurationsRawPrivateKeyToStaticPublicKey,
    ):
        RawEcdhStaticConfigurations_union_value = RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_RawPrivateKeyToStaticPublicKeyInput(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.RawEcdhStaticConfigurationsEphemeralPrivateKeyToStaticPublicKey,
    ):
        RawEcdhStaticConfigurations_union_value = RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_EphemeralPrivateKeyToStaticPublicKeyInput(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return RawEcdhStaticConfigurations_union_value


def aws_cryptography_materialproviders_PublicKeyDiscoveryInput(native_input):
    return DafnyPublicKeyDiscoveryInput(
        recipientStaticPrivateKey=Seq(native_input.recipient_static_private_key),
    )


def aws_cryptography_materialproviders_RawPrivateKeyToStaticPublicKeyInput(
    native_input,
):
    return DafnyRawPrivateKeyToStaticPublicKeyInput(
        senderStaticPrivateKey=Seq(native_input.sender_static_private_key),
        recipientPublicKey=Seq(native_input.recipient_public_key),
    )


def aws_cryptography_materialproviders_EphemeralPrivateKeyToStaticPublicKeyInput(
    native_input,
):
    return DafnyEphemeralPrivateKeyToStaticPublicKeyInput(
        recipientPublicKey=Seq(native_input.recipient_public_key),
    )


def aws_cryptography_materialproviders_CreateDefaultCryptographicMaterialsManagerInput(
    native_input,
):
    return DafnyCreateDefaultCryptographicMaterialsManagerInput(
        keyring=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KeyringReference(
            native_input.keyring
        ),
    )


def aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMInput(
    native_input,
):
    return DafnyCreateRequiredEncryptionContextCMMInput(
        underlyingCMM=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(
                        native_input.underlying_cmm
                    )
                )
            )
            if (
                (native_input.underlying_cmm is not None)
                and (
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(
                        native_input.underlying_cmm
                    )
                    is not None
                )
            )
            else (Option_None())
        ),
        keyring=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KeyringReference(
                        native_input.keyring
                    )
                )
            )
            if (
                (native_input.keyring is not None)
                and (
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KeyringReference(
                        native_input.keyring
                    )
                    is not None
                )
            )
            else (Option_None())
        ),
        requiredEncryptionContextKeys=Seq(
            [
                Seq(list_element.encode("utf-8"))
                for list_element in native_input.required_encryption_context_keys
            ]
        ),
    )


def aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(
    native_input,
):
    if hasattr(native_input, "_impl"):
        return native_input._impl

    else:
        return native_input


def aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheInput(
    native_input,
):
    return DafnyCreateCryptographicMaterialsCacheInput(
        cache=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CacheType(
            native_input.cache
        ),
    )


def aws_cryptography_materialproviders_CreateDefaultClientSupplierInput(native_input):
    return DafnyCreateDefaultClientSupplierInput()


def aws_cryptography_materialproviders_InitializeEncryptionMaterialsInput(native_input):
    return DafnyInitializeEncryptionMaterialsInput(
        algorithmSuiteId=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_AlgorithmSuiteId(
            native_input.algorithm_suite_id
        ),
        encryptionContext=Map(
            {
                Seq(key.encode("utf-8")): Seq(value.encode("utf-8"))
                for (key, value) in native_input.encryption_context.items()
            }
        ),
        requiredEncryptionContextKeys=Seq(
            [
                Seq(list_element.encode("utf-8"))
                for list_element in native_input.required_encryption_context_keys
            ]
        ),
        signingKey=(
            (Option_Some(Seq(native_input.signing_key)))
            if (native_input.signing_key is not None)
            else (Option_None())
        ),
        verificationKey=(
            (Option_Some(Seq(native_input.verification_key)))
            if (native_input.verification_key is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviders_InitializeDecryptionMaterialsInput(native_input):
    return DafnyInitializeDecryptionMaterialsInput(
        algorithmSuiteId=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_AlgorithmSuiteId(
            native_input.algorithm_suite_id
        ),
        encryptionContext=Map(
            {
                Seq(key.encode("utf-8")): Seq(value.encode("utf-8"))
                for (key, value) in native_input.encryption_context.items()
            }
        ),
        requiredEncryptionContextKeys=Seq(
            [
                Seq(list_element.encode("utf-8"))
                for list_element in native_input.required_encryption_context_keys
            ]
        ),
    )


def aws_cryptography_materialproviders_ValidEncryptionMaterialsTransitionInput(
    native_input,
):
    return DafnyValidEncryptionMaterialsTransitionInput(
        start=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_EncryptionMaterials(
            native_input.start
        ),
        stop=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_EncryptionMaterials(
            native_input.stop
        ),
    )


def aws_cryptography_materialproviders_ValidDecryptionMaterialsTransitionInput(
    native_input,
):
    return DafnyValidDecryptionMaterialsTransitionInput(
        start=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DecryptionMaterials(
            native_input.start
        ),
        stop=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DecryptionMaterials(
            native_input.stop
        ),
    )


def aws_cryptography_materialproviders_GetAlgorithmSuiteInfoInput(native_input):
    return Seq(native_input)


def aws_cryptography_materialproviders_ValidateCommitmentPolicyOnEncryptInput(
    native_input,
):
    return DafnyValidateCommitmentPolicyOnEncryptInput(
        algorithm=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_AlgorithmSuiteId(
            native_input.algorithm
        ),
        commitmentPolicy=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CommitmentPolicy(
            native_input.commitment_policy
        ),
    )


def aws_cryptography_materialproviders_ValidateCommitmentPolicyOnDecryptInput(
    native_input,
):
    return DafnyValidateCommitmentPolicyOnDecryptInput(
        algorithm=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_AlgorithmSuiteId(
            native_input.algorithm
        ),
        commitmentPolicy=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CommitmentPolicy(
            native_input.commitment_policy
        ),
    )


def aws_cryptography_materialproviders_CreateKeyringOutput(native_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_KeyringReference(
        native_input
    )


def aws_cryptography_materialproviders_CreateCryptographicMaterialsManagerOutput(
    native_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(
        native_input
    )


def aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMOutput(
    native_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(
        native_input
    )


def aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheOutput(
    native_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CryptographicMaterialsCacheReference(
        native_input
    )


def aws_cryptography_materialproviders_CreateDefaultClientSupplierOutput(native_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_ClientSupplierReference(
        native_input
    )


def aws_cryptography_materialproviders_MaterialProvidersConfig(native_input):
    return DafnyMaterialProvidersConfig()
