# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes import (
    AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16,
    AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16,
    AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16,
    AlgorithmSuiteId_DBE,
    AlgorithmSuiteId_ESDK,
    CacheType_Default,
    CacheType_MultiThreaded,
    CacheType_No,
    CacheType_Shared,
    CacheType_SingleThreaded,
    CacheType_StormTracking,
    CommitmentPolicy_DBE,
    CommitmentPolicy_ESDK,
    DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384,
    DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384,
    DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT,
    DerivationAlgorithm_HKDF,
    DerivationAlgorithm_IDENTITY,
    DerivationAlgorithm_None,
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
    KeyAgreementScheme_StaticConfiguration,
    KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey,
    KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery,
    Materials_BeaconKey,
    Materials_BranchKey,
    Materials_Decryption,
    Materials_Encryption,
    PaddingScheme_OAEP__SHA1__MGF1,
    PaddingScheme_OAEP__SHA256__MGF1,
    PaddingScheme_OAEP__SHA384__MGF1,
    PaddingScheme_OAEP__SHA512__MGF1,
    PaddingScheme_PKCS1,
    RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey,
    RawEcdhStaticConfigurations_PublicKeyDiscovery,
    RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey,
    SignatureAlgorithm_ECDSA,
    SignatureAlgorithm_None,
    StaticConfigurations_AWS__KMS__ECDH,
    StaticConfigurations_RAW__ECDH,
    SymmetricSignatureAlgorithm_HMAC,
    SymmetricSignatureAlgorithm_None,
    TimeUnits_Milliseconds,
    TimeUnits_Seconds,
)
import aws_cryptographic_material_providers.internaldafny.generated.module_
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models
import aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk
import aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy


def aws_cryptography_materialproviders_GetBranchKeyIdInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetBranchKeyIdInput(
        encryption_context={
            bytes(key.Elements).decode("utf-8"): bytes(value.Elements).decode("utf-8")
            for (key, value) in dafny_input.encryptionContext.items
        },
    )


def aws_cryptography_materialproviders_GetBranchKeyIdOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetBranchKeyIdOutput(
        branch_key_id=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.branchKeyId
        ).decode("utf-16-be"),
    )


def aws_cryptography_materialproviders_GetClientInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetClientInput(
        region=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.region).decode(
            "utf-16-be"
        ),
    )


def aws_cryptography_materialproviders_KmsClientReference(dafny_input):
    return dafny_input._impl


def aws_cryptography_materialproviders_GetClientOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KmsClientReference(
        dafny_input
    )


def aws_cryptography_materialproviders_Materials(dafny_input):
    # Convert Materials
    if isinstance(dafny_input, Materials_Encryption):
        Materials_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.MaterialsEncryption(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_EncryptionMaterials(
                dafny_input.Encryption
            )
        )
    elif isinstance(dafny_input, Materials_Decryption):
        Materials_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.MaterialsDecryption(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DecryptionMaterials(
                dafny_input.Decryption
            )
        )
    elif isinstance(dafny_input, Materials_BranchKey):
        Materials_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.MaterialsBranchKey(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_BranchKeyMaterials(
                dafny_input.BranchKey
            )
        )
    elif isinstance(dafny_input, Materials_BeaconKey):
        Materials_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.MaterialsBeaconKey(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_BeaconKeyMaterials(
                dafny_input.BeaconKey
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return Materials_union_value


def aws_cryptography_materialproviders_EncryptionMaterials(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.EncryptionMaterials(
        algorithm_suite=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_AlgorithmSuiteInfo(
            dafny_input.algorithmSuite
        ),
        encryption_context={
            bytes(key.Elements).decode("utf-8"): bytes(value.Elements).decode("utf-8")
            for (key, value) in dafny_input.encryptionContext.items
        },
        encrypted_data_keys=[
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_EncryptedDataKey(
                list_element
            )
            for list_element in dafny_input.encryptedDataKeys
        ],
        required_encryption_context_keys=[
            bytes(list_element.Elements).decode("utf-8")
            for list_element in dafny_input.requiredEncryptionContextKeys
        ],
        plaintext_data_key=(
            (bytes(dafny_input.plaintextDataKey.value))
            if (dafny_input.plaintextDataKey.is_Some)
            else None
        ),
        signing_key=(
            (bytes(dafny_input.signingKey.value))
            if (dafny_input.signingKey.is_Some)
            else None
        ),
        symmetric_signing_keys=(
            (
                [
                    bytes(list_element)
                    for list_element in dafny_input.symmetricSigningKeys.value
                ]
            )
            if (dafny_input.symmetricSigningKeys.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_DecryptionMaterials(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DecryptionMaterials(
        algorithm_suite=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_AlgorithmSuiteInfo(
            dafny_input.algorithmSuite
        ),
        encryption_context={
            bytes(key.Elements).decode("utf-8"): bytes(value.Elements).decode("utf-8")
            for (key, value) in dafny_input.encryptionContext.items
        },
        required_encryption_context_keys=[
            bytes(list_element.Elements).decode("utf-8")
            for list_element in dafny_input.requiredEncryptionContextKeys
        ],
        plaintext_data_key=(
            (bytes(dafny_input.plaintextDataKey.value))
            if (dafny_input.plaintextDataKey.is_Some)
            else None
        ),
        verification_key=(
            (bytes(dafny_input.verificationKey.value))
            if (dafny_input.verificationKey.is_Some)
            else None
        ),
        symmetric_signing_key=(
            (bytes(dafny_input.symmetricSigningKey.value))
            if (dafny_input.symmetricSigningKey.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_AlgorithmSuiteInfo(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.AlgorithmSuiteInfo(
        id=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_AlgorithmSuiteId(
            dafny_input.id
        ),
        binary_id=bytes(dafny_input.binaryId),
        message_version=dafny_input.messageVersion,
        encrypt=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_Encrypt(
            dafny_input.encrypt
        ),
        kdf=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DerivationAlgorithm(
            dafny_input.kdf
        ),
        commitment=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DerivationAlgorithm(
            dafny_input.commitment
        ),
        signature=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_SignatureAlgorithm(
            dafny_input.signature
        ),
        symmetric_signature=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_SymmetricSignatureAlgorithm(
            dafny_input.symmetricSignature
        ),
        edk_wrapping=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_EdkWrappingAlgorithm(
            dafny_input.edkWrapping
        ),
    )


def aws_cryptography_materialproviders_EncryptedDataKey(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.EncryptedDataKey(
        key_provider_id=bytes(dafny_input.keyProviderId.Elements).decode("utf-8"),
        key_provider_info=bytes(dafny_input.keyProviderInfo),
        ciphertext=bytes(dafny_input.ciphertext),
    )


def aws_cryptography_materialproviders_AlgorithmSuiteId(dafny_input):
    # Convert AlgorithmSuiteId
    if isinstance(dafny_input, AlgorithmSuiteId_ESDK):
        AlgorithmSuiteId_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.AlgorithmSuiteIdESDK(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ESDKAlgorithmSuiteId(
                dafny_input.ESDK
            )
        )
    elif isinstance(dafny_input, AlgorithmSuiteId_DBE):
        AlgorithmSuiteId_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.AlgorithmSuiteIdDBE(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DBEAlgorithmSuiteId(
                dafny_input.DBE
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return AlgorithmSuiteId_union_value


def aws_cryptography_materialproviders_Encrypt(dafny_input):
    # Convert Encrypt
    if isinstance(dafny_input, Encrypt_AES__GCM):
        Encrypt_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.EncryptAES_GCM(
            aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_AES_GCM(
                dafny_input.AES__GCM
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return Encrypt_union_value


def aws_cryptography_materialproviders_DerivationAlgorithm(dafny_input):
    # Convert DerivationAlgorithm
    if isinstance(dafny_input, DerivationAlgorithm_HKDF):
        DerivationAlgorithm_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DerivationAlgorithmHKDF(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_HKDF(
                dafny_input.HKDF
            )
        )
    elif isinstance(dafny_input, DerivationAlgorithm_IDENTITY):
        DerivationAlgorithm_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DerivationAlgorithmIDENTITY(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_IDENTITY(
                dafny_input.IDENTITY
            )
        )
    elif isinstance(dafny_input, DerivationAlgorithm_None):
        DerivationAlgorithm_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DerivationAlgorithmNone(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_None(
                dafny_input.None_
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return DerivationAlgorithm_union_value


def aws_cryptography_materialproviders_SignatureAlgorithm(dafny_input):
    # Convert SignatureAlgorithm
    if isinstance(dafny_input, SignatureAlgorithm_ECDSA):
        SignatureAlgorithm_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.SignatureAlgorithmECDSA(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ECDSA(
                dafny_input.ECDSA
            )
        )
    elif isinstance(dafny_input, SignatureAlgorithm_None):
        SignatureAlgorithm_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.SignatureAlgorithmNone(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_None(
                dafny_input.None_
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return SignatureAlgorithm_union_value


def aws_cryptography_materialproviders_SymmetricSignatureAlgorithm(dafny_input):
    # Convert SymmetricSignatureAlgorithm
    if isinstance(dafny_input, SymmetricSignatureAlgorithm_HMAC):
        SymmetricSignatureAlgorithm_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.SymmetricSignatureAlgorithmHMAC(
            aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_DigestAlgorithm(
                dafny_input.HMAC
            )
        )
    elif isinstance(dafny_input, SymmetricSignatureAlgorithm_None):
        SymmetricSignatureAlgorithm_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.SymmetricSignatureAlgorithmNone(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_None(
                dafny_input.None_
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return SymmetricSignatureAlgorithm_union_value


def aws_cryptography_materialproviders_EdkWrappingAlgorithm(dafny_input):
    # Convert EdkWrappingAlgorithm
    if isinstance(dafny_input, EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING):
        EdkWrappingAlgorithm_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.EdkWrappingAlgorithmDIRECT_KEY_WRAPPING(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DIRECT_KEY_WRAPPING(
                dafny_input.DIRECT__KEY__WRAPPING
            )
        )
    elif isinstance(dafny_input, EdkWrappingAlgorithm_IntermediateKeyWrapping):
        EdkWrappingAlgorithm_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.EdkWrappingAlgorithmIntermediateKeyWrapping(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_IntermediateKeyWrapping(
                dafny_input.IntermediateKeyWrapping
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return EdkWrappingAlgorithm_union_value


def aws_cryptography_materialproviders_ESDKAlgorithmSuiteId(dafny_input):
    if isinstance(
        dafny_input, ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF
    ):
        return "0x0014"

    elif isinstance(
        dafny_input, ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF
    ):
        return "0x0046"

    elif isinstance(
        dafny_input, ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF
    ):
        return "0x0078"

    elif isinstance(
        dafny_input, ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256
    ):
        return "0x0114"

    elif isinstance(
        dafny_input, ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256
    ):
        return "0x0146"

    elif isinstance(
        dafny_input, ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256
    ):
        return "0x0178"

    elif isinstance(
        dafny_input,
        ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256,
    ):
        return "0x0214"

    elif isinstance(
        dafny_input,
        ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384,
    ):
        return "0x0346"

    elif isinstance(
        dafny_input,
        ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384,
    ):
        return "0x0378"

    elif isinstance(
        dafny_input, ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY
    ):
        return "0x0478"

    elif isinstance(
        dafny_input,
        ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384,
    ):
        return "0x0578"

    else:
        raise ValueError(f"No recognized enum value in enum type: {dafny_input=}")


def aws_cryptography_materialproviders_DBEAlgorithmSuiteId(dafny_input):
    if isinstance(
        dafny_input,
        DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384,
    ):
        return "0x6700"

    elif isinstance(
        dafny_input,
        DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384,
    ):
        return "0x6701"

    else:
        raise ValueError(f"No recognized enum value in enum type: {dafny_input=}")


def aws_cryptography_materialproviders_HKDF(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.HKDF(
        hmac=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_DigestAlgorithm(
            dafny_input.hmac
        ),
        salt_length=dafny_input.saltLength,
        input_key_length=dafny_input.inputKeyLength,
        output_key_length=dafny_input.outputKeyLength,
    )


def aws_cryptography_materialproviders_IDENTITY(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.IDENTITY()
    )


def aws_cryptography_materialproviders_None(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.None_()
    )


def aws_cryptography_materialproviders_ECDSA(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.ECDSA(
        curve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDSASignatureAlgorithm(
            dafny_input.curve
        ),
    )


def aws_cryptography_materialproviders_DIRECT_KEY_WRAPPING(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DIRECT_KEY_WRAPPING()
    )


def aws_cryptography_materialproviders_IntermediateKeyWrapping(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.IntermediateKeyWrapping(
        key_encryption_key_kdf=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DerivationAlgorithm(
            dafny_input.keyEncryptionKeyKdf
        ),
        mac_key_kdf=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DerivationAlgorithm(
            dafny_input.macKeyKdf
        ),
        pdk_encrypt_algorithm=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_Encrypt(
            dafny_input.pdkEncryptAlgorithm
        ),
    )


def aws_cryptography_materialproviders_PutCacheEntryInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.PutCacheEntryInput(
        identifier=bytes(dafny_input.identifier),
        materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_Materials(
            dafny_input.materials
        ),
        creation_time=dafny_input.creationTime,
        expiry_time=dafny_input.expiryTime,
        messages_used=(
            (dafny_input.messagesUsed.value)
            if (dafny_input.messagesUsed.is_Some)
            else None
        ),
        bytes_used=(
            (dafny_input.bytesUsed.value) if (dafny_input.bytesUsed.is_Some) else None
        ),
    )


def smithy_api_Unit():
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.Unit()
    )


def aws_cryptography_materialproviders_GetCacheEntryInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetCacheEntryInput(
        identifier=bytes(dafny_input.identifier),
        bytes_used=(
            (dafny_input.bytesUsed.value) if (dafny_input.bytesUsed.is_Some) else None
        ),
    )


def aws_cryptography_materialproviders_GetCacheEntryOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetCacheEntryOutput(
        materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_Materials(
            dafny_input.materials
        ),
        creation_time=dafny_input.creationTime,
        expiry_time=dafny_input.expiryTime,
        messages_used=dafny_input.messagesUsed,
        bytes_used=dafny_input.bytesUsed,
    )


def aws_cryptography_materialproviders_UpdateUsageMetadataInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.UpdateUsageMetadataInput(
        identifier=bytes(dafny_input.identifier),
        bytes_used=dafny_input.bytesUsed,
    )


def aws_cryptography_materialproviders_DeleteCacheEntryInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DeleteCacheEntryInput(
        identifier=bytes(dafny_input.identifier),
    )


def aws_cryptography_materialproviders_CommitmentPolicy(dafny_input):
    # Convert CommitmentPolicy
    if isinstance(dafny_input, CommitmentPolicy_ESDK):
        CommitmentPolicy_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CommitmentPolicyESDK(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ESDKCommitmentPolicy(
                dafny_input.ESDK
            )
        )
    elif isinstance(dafny_input, CommitmentPolicy_DBE):
        CommitmentPolicy_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CommitmentPolicyDBE(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DBECommitmentPolicy(
                dafny_input.DBE
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return CommitmentPolicy_union_value


def aws_cryptography_materialproviders_ESDKCommitmentPolicy(dafny_input):
    if isinstance(dafny_input, ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT):
        return "FORBID_ENCRYPT_ALLOW_DECRYPT"

    elif isinstance(dafny_input, ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT):
        return "REQUIRE_ENCRYPT_ALLOW_DECRYPT"

    elif isinstance(
        dafny_input, ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT
    ):
        return "REQUIRE_ENCRYPT_REQUIRE_DECRYPT"

    else:
        raise ValueError(f"No recognized enum value in enum type: {dafny_input=}")


def aws_cryptography_materialproviders_DBECommitmentPolicy(dafny_input):
    if isinstance(dafny_input, DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT):
        return "REQUIRE_ENCRYPT_REQUIRE_DECRYPT"

    else:
        raise ValueError(f"No recognized enum value in enum type: {dafny_input=}")


def aws_cryptography_materialproviders_GetEncryptionMaterialsInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetEncryptionMaterialsInput(
        encryption_context={
            bytes(key.Elements).decode("utf-8"): bytes(value.Elements).decode("utf-8")
            for (key, value) in dafny_input.encryptionContext.items
        },
        commitment_policy=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CommitmentPolicy(
            dafny_input.commitmentPolicy
        ),
        algorithm_suite_id=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_AlgorithmSuiteId(
                    dafny_input.algorithmSuiteId.value
                )
            )
            if (dafny_input.algorithmSuiteId.is_Some)
            else None
        ),
        max_plaintext_length=(
            (dafny_input.maxPlaintextLength.value)
            if (dafny_input.maxPlaintextLength.is_Some)
            else None
        ),
        required_encryption_context_keys=(
            (
                [
                    bytes(list_element.Elements).decode("utf-8")
                    for list_element in dafny_input.requiredEncryptionContextKeys.value
                ]
            )
            if (dafny_input.requiredEncryptionContextKeys.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_GetEncryptionMaterialsOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetEncryptionMaterialsOutput(
        encryption_materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_EncryptionMaterials(
            dafny_input.encryptionMaterials
        ),
    )


def aws_cryptography_materialproviders_DecryptMaterialsInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DecryptMaterialsInput(
        algorithm_suite_id=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_AlgorithmSuiteId(
            dafny_input.algorithmSuiteId
        ),
        commitment_policy=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CommitmentPolicy(
            dafny_input.commitmentPolicy
        ),
        encrypted_data_keys=[
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_EncryptedDataKey(
                list_element
            )
            for list_element in dafny_input.encryptedDataKeys
        ],
        encryption_context={
            bytes(key.Elements).decode("utf-8"): bytes(value.Elements).decode("utf-8")
            for (key, value) in dafny_input.encryptionContext.items
        },
        reproduced_encryption_context=(
            (
                {
                    bytes(key.Elements)
                    .decode("utf-8"): bytes(value.Elements)
                    .decode("utf-8")
                    for (
                        key,
                        value,
                    ) in dafny_input.reproducedEncryptionContext.value.items
                }
            )
            if (dafny_input.reproducedEncryptionContext.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_DecryptMaterialsOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DecryptMaterialsOutput(
        decryption_materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DecryptionMaterials(
            dafny_input.decryptionMaterials
        ),
    )


def aws_cryptography_materialproviders_OnEncryptInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.OnEncryptInput(
        materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_EncryptionMaterials(
            dafny_input.materials
        ),
    )


def aws_cryptography_materialproviders_OnEncryptOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.OnEncryptOutput(
        materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_EncryptionMaterials(
            dafny_input.materials
        ),
    )


def aws_cryptography_materialproviders_OnDecryptInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.OnDecryptInput(
        materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DecryptionMaterials(
            dafny_input.materials
        ),
        encrypted_data_keys=[
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_EncryptedDataKey(
                list_element
            )
            for list_element in dafny_input.encryptedDataKeys
        ],
    )


def aws_cryptography_materialproviders_OnDecryptOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.OnDecryptOutput(
        materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DecryptionMaterials(
            dafny_input.materials
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsKeyringInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsKeyringInput(
        kms_key_id=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.kmsKeyId
        ).decode("utf-16-be"),
        kms_client=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KmsClientReference(
                    dafny_input.kmsClient
                )
            )
            if (dafny_input.kmsClient is not None)
            else None
        ),
        grant_tokens=(
            (
                [
                    b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                        "utf-16-be"
                    )
                    for list_element in dafny_input.grantTokens.value
                ]
            )
            if (dafny_input.grantTokens.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_DiscoveryFilter(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DiscoveryFilter(
        account_ids=[
            b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                "utf-16-be"
            )
            for list_element in dafny_input.accountIds
        ],
        partition=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.partition
        ).decode("utf-16-be"),
    )


def aws_cryptography_materialproviders_CreateAwsKmsDiscoveryKeyringInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsDiscoveryKeyringInput(
        kms_client=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KmsClientReference(
                    dafny_input.kmsClient
                )
            )
            if (dafny_input.kmsClient is not None)
            else None
        ),
        discovery_filter=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DiscoveryFilter(
                    dafny_input.discoveryFilter.value
                )
            )
            if (dafny_input.discoveryFilter.is_Some)
            else None
        ),
        grant_tokens=(
            (
                [
                    b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                        "utf-16-be"
                    )
                    for list_element in dafny_input.grantTokens.value
                ]
            )
            if (dafny_input.grantTokens.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_ClientSupplierReference(dafny_input):
    if hasattr(dafny_input, "_native_impl"):
        return dafny_input._native_impl

    else:
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references import (
            ClientSupplier,
        )

        return ClientSupplier(_impl=dafny_input)


def aws_cryptography_materialproviders_CreateAwsKmsMultiKeyringInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsMultiKeyringInput(
        generator=(
            (
                b"".join(
                    ord(c).to_bytes(2, "big") for c in dafny_input.generator.value
                ).decode("utf-16-be")
            )
            if (dafny_input.generator.is_Some)
            else None
        ),
        kms_key_ids=(
            (
                [
                    b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                        "utf-16-be"
                    )
                    for list_element in dafny_input.kmsKeyIds.value
                ]
            )
            if (dafny_input.kmsKeyIds.is_Some)
            else None
        ),
        client_supplier=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ClientSupplierReference(
                    dafny_input.clientSupplier.UnwrapOr(None)
                )
            )
            if (dafny_input.clientSupplier.UnwrapOr(None) is not None)
            else None
        ),
        grant_tokens=(
            (
                [
                    b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                        "utf-16-be"
                    )
                    for list_element in dafny_input.grantTokens.value
                ]
            )
            if (dafny_input.grantTokens.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsDiscoveryMultiKeyringInput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsDiscoveryMultiKeyringInput(
        regions=[
            b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                "utf-16-be"
            )
            for list_element in dafny_input.regions
        ],
        discovery_filter=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DiscoveryFilter(
                    dafny_input.discoveryFilter.value
                )
            )
            if (dafny_input.discoveryFilter.is_Some)
            else None
        ),
        client_supplier=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ClientSupplierReference(
                    dafny_input.clientSupplier.UnwrapOr(None)
                )
            )
            if (dafny_input.clientSupplier.UnwrapOr(None) is not None)
            else None
        ),
        grant_tokens=(
            (
                [
                    b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                        "utf-16-be"
                    )
                    for list_element in dafny_input.grantTokens.value
                ]
            )
            if (dafny_input.grantTokens.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsMrkKeyringInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsMrkKeyringInput(
        kms_key_id=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.kmsKeyId
        ).decode("utf-16-be"),
        kms_client=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KmsClientReference(
                    dafny_input.kmsClient
                )
            )
            if (dafny_input.kmsClient is not None)
            else None
        ),
        grant_tokens=(
            (
                [
                    b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                        "utf-16-be"
                    )
                    for list_element in dafny_input.grantTokens.value
                ]
            )
            if (dafny_input.grantTokens.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsMrkMultiKeyringInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsMrkMultiKeyringInput(
        generator=(
            (
                b"".join(
                    ord(c).to_bytes(2, "big") for c in dafny_input.generator.value
                ).decode("utf-16-be")
            )
            if (dafny_input.generator.is_Some)
            else None
        ),
        kms_key_ids=(
            (
                [
                    b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                        "utf-16-be"
                    )
                    for list_element in dafny_input.kmsKeyIds.value
                ]
            )
            if (dafny_input.kmsKeyIds.is_Some)
            else None
        ),
        client_supplier=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ClientSupplierReference(
                    dafny_input.clientSupplier.UnwrapOr(None)
                )
            )
            if (dafny_input.clientSupplier.UnwrapOr(None) is not None)
            else None
        ),
        grant_tokens=(
            (
                [
                    b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                        "utf-16-be"
                    )
                    for list_element in dafny_input.grantTokens.value
                ]
            )
            if (dafny_input.grantTokens.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryKeyringInput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsMrkDiscoveryKeyringInput(
        kms_client=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KmsClientReference(
                    dafny_input.kmsClient
                )
            )
            if (dafny_input.kmsClient is not None)
            else None
        ),
        discovery_filter=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DiscoveryFilter(
                    dafny_input.discoveryFilter.value
                )
            )
            if (dafny_input.discoveryFilter.is_Some)
            else None
        ),
        grant_tokens=(
            (
                [
                    b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                        "utf-16-be"
                    )
                    for list_element in dafny_input.grantTokens.value
                ]
            )
            if (dafny_input.grantTokens.is_Some)
            else None
        ),
        region=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.region).decode(
            "utf-16-be"
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryMultiKeyringInput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsMrkDiscoveryMultiKeyringInput(
        regions=[
            b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                "utf-16-be"
            )
            for list_element in dafny_input.regions
        ],
        discovery_filter=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DiscoveryFilter(
                    dafny_input.discoveryFilter.value
                )
            )
            if (dafny_input.discoveryFilter.is_Some)
            else None
        ),
        client_supplier=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ClientSupplierReference(
                    dafny_input.clientSupplier.UnwrapOr(None)
                )
            )
            if (dafny_input.clientSupplier.UnwrapOr(None) is not None)
            else None
        ),
        grant_tokens=(
            (
                [
                    b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                        "utf-16-be"
                    )
                    for list_element in dafny_input.grantTokens.value
                ]
            )
            if (dafny_input.grantTokens.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_BranchKeyIdSupplierReference(dafny_input):
    if hasattr(dafny_input, "_native_impl"):
        return dafny_input._native_impl

    else:
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references import (
            BranchKeyIdSupplier,
        )

        return BranchKeyIdSupplier(_impl=dafny_input)


def aws_cryptography_materialproviders_KeyStoreReference(dafny_input):
    from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.client import (
        KeyStore,
    )

    return KeyStore(config=None, dafny_client=dafny_input)


def aws_cryptography_materialproviders_CacheType(dafny_input):
    # Convert CacheType
    if isinstance(dafny_input, CacheType_Default):
        CacheType_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CacheTypeDefault(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DefaultCache(
                dafny_input.Default
            )
        )
    elif isinstance(dafny_input, CacheType_No):
        CacheType_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CacheTypeNo(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_NoCache(
                dafny_input.No
            )
        )
    elif isinstance(dafny_input, CacheType_SingleThreaded):
        CacheType_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CacheTypeSingleThreaded(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_SingleThreadedCache(
                dafny_input.SingleThreaded
            )
        )
    elif isinstance(dafny_input, CacheType_MultiThreaded):
        CacheType_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CacheTypeMultiThreaded(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_MultiThreadedCache(
                dafny_input.MultiThreaded
            )
        )
    elif isinstance(dafny_input, CacheType_StormTracking):
        CacheType_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CacheTypeStormTracking(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_StormTrackingCache(
                dafny_input.StormTracking
            )
        )
    elif isinstance(dafny_input, CacheType_Shared):
        CacheType_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CacheTypeShared(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CryptographicMaterialsCacheReference(
                dafny_input.Shared
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return CacheType_union_value


def aws_cryptography_materialproviders_DefaultCache(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DefaultCache(
        entry_capacity=dafny_input.entryCapacity,
    )


def aws_cryptography_materialproviders_NoCache(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.NoCache()
    )


def aws_cryptography_materialproviders_SingleThreadedCache(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.SingleThreadedCache(
        entry_capacity=dafny_input.entryCapacity,
        entry_pruning_tail_size=(
            (dafny_input.entryPruningTailSize.value)
            if (dafny_input.entryPruningTailSize.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_MultiThreadedCache(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.MultiThreadedCache(
        entry_capacity=dafny_input.entryCapacity,
        entry_pruning_tail_size=(
            (dafny_input.entryPruningTailSize.value)
            if (dafny_input.entryPruningTailSize.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_StormTrackingCache(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.StormTrackingCache(
        entry_capacity=dafny_input.entryCapacity,
        entry_pruning_tail_size=(
            (dafny_input.entryPruningTailSize.value)
            if (dafny_input.entryPruningTailSize.is_Some)
            else None
        ),
        grace_period=dafny_input.gracePeriod,
        grace_interval=dafny_input.graceInterval,
        fan_out=dafny_input.fanOut,
        in_flight_ttl=dafny_input.inFlightTTL,
        sleep_milli=dafny_input.sleepMilli,
        time_units=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_TimeUnits(
                    dafny_input.timeUnits.value
                )
            )
            if (dafny_input.timeUnits.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_CryptographicMaterialsCacheReference(
    dafny_input,
):
    if hasattr(dafny_input, "_native_impl"):
        return dafny_input._native_impl

    else:
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references import (
            CryptographicMaterialsCache,
        )

        return CryptographicMaterialsCache(_impl=dafny_input)


def aws_cryptography_materialproviders_TimeUnits(dafny_input):
    if isinstance(dafny_input, TimeUnits_Seconds):
        return "Seconds"

    elif isinstance(dafny_input, TimeUnits_Milliseconds):
        return "Milliseconds"

    else:
        raise ValueError(f"No recognized enum value in enum type: {dafny_input=}")


def aws_cryptography_materialproviders_CreateAwsKmsHierarchicalKeyringInput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsHierarchicalKeyringInput(
        branch_key_id=(
            (
                b"".join(
                    ord(c).to_bytes(2, "big") for c in dafny_input.branchKeyId.value
                ).decode("utf-16-be")
            )
            if (dafny_input.branchKeyId.is_Some)
            else None
        ),
        branch_key_id_supplier=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_BranchKeyIdSupplierReference(
                    dafny_input.branchKeyIdSupplier.UnwrapOr(None)
                )
            )
            if (dafny_input.branchKeyIdSupplier.UnwrapOr(None) is not None)
            else None
        ),
        key_store=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KeyStoreReference(
                    dafny_input.keyStore
                )
            )
            if (dafny_input.keyStore is not None)
            else None
        ),
        ttl_seconds=dafny_input.ttlSeconds,
        cache=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CacheType(
                    dafny_input.cache.value
                )
            )
            if (dafny_input.cache.is_Some)
            else None
        ),
        partition_id=(
            (
                b"".join(
                    ord(c).to_bytes(2, "big") for c in dafny_input.partitionId.value
                ).decode("utf-16-be")
            )
            if (dafny_input.partitionId.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_CreateAwsKmsRsaKeyringInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsRsaKeyringInput(
        public_key=(
            (bytes(dafny_input.publicKey.value))
            if (dafny_input.publicKey.is_Some)
            else None
        ),
        kms_key_id=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.kmsKeyId
        ).decode("utf-16-be"),
        encryption_algorithm=aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_EncryptionAlgorithmSpec(
            dafny_input.encryptionAlgorithm
        ),
        kms_client=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KmsClientReference(
                    dafny_input.kmsClient.UnwrapOr(None)
                )
            )
            if (dafny_input.kmsClient.UnwrapOr(None) is not None)
            else None
        ),
        grant_tokens=(
            (
                [
                    b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                        "utf-16-be"
                    )
                    for list_element in dafny_input.grantTokens.value
                ]
            )
            if (dafny_input.grantTokens.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_KmsEcdhStaticConfigurations(dafny_input):
    # Convert KmsEcdhStaticConfigurations
    if isinstance(dafny_input, KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery):
        KmsEcdhStaticConfigurations_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.KmsEcdhStaticConfigurationsKmsPublicKeyDiscovery(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KmsPublicKeyDiscoveryInput(
                dafny_input.KmsPublicKeyDiscovery
            )
        )
    elif isinstance(
        dafny_input, KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey
    ):
        KmsEcdhStaticConfigurations_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.KmsEcdhStaticConfigurationsKmsPrivateKeyToStaticPublicKey(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KmsPrivateKeyToStaticPublicKeyInput(
                dafny_input.KmsPrivateKeyToStaticPublicKey
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return KmsEcdhStaticConfigurations_union_value


def aws_cryptography_materialproviders_KmsPublicKeyDiscoveryInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.KmsPublicKeyDiscoveryInput(
        recipient_kms_identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.recipientKmsIdentifier
        ).decode("utf-16-be"),
    )


def aws_cryptography_materialproviders_KmsPrivateKeyToStaticPublicKeyInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.KmsPrivateKeyToStaticPublicKeyInput(
        sender_kms_identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.senderKmsIdentifier
        ).decode("utf-16-be"),
        sender_public_key=(
            (bytes(dafny_input.senderPublicKey.value))
            if (dafny_input.senderPublicKey.is_Some)
            else None
        ),
        recipient_public_key=bytes(dafny_input.recipientPublicKey),
    )


def aws_cryptography_materialproviders_CreateAwsKmsEcdhKeyringInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsEcdhKeyringInput(
        key_agreement_scheme=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KmsEcdhStaticConfigurations(
            dafny_input.KeyAgreementScheme
        ),
        curve_spec=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDHCurveSpec(
            dafny_input.curveSpec
        ),
        kms_client=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KmsClientReference(
                    dafny_input.kmsClient
                )
            )
            if (dafny_input.kmsClient is not None)
            else None
        ),
        grant_tokens=(
            (
                [
                    b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                        "utf-16-be"
                    )
                    for list_element in dafny_input.grantTokens.value
                ]
            )
            if (dafny_input.grantTokens.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_KeyringReference(dafny_input):
    if hasattr(dafny_input, "_native_impl"):
        return dafny_input._native_impl

    else:
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references import (
            Keyring,
        )

        return Keyring(_impl=dafny_input)


def aws_cryptography_materialproviders_CreateMultiKeyringInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateMultiKeyringInput(
        generator=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KeyringReference(
                    dafny_input.generator.UnwrapOr(None)
                )
            )
            if (dafny_input.generator.UnwrapOr(None) is not None)
            else None
        ),
        child_keyrings=[
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KeyringReference(
                list_element
            )
            for list_element in dafny_input.childKeyrings
        ],
    )


def aws_cryptography_materialproviders_AesWrappingAlg(dafny_input):
    if isinstance(dafny_input, AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16):
        return "ALG_AES128_GCM_IV12_TAG16"

    elif isinstance(dafny_input, AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16):
        return "ALG_AES192_GCM_IV12_TAG16"

    elif isinstance(dafny_input, AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16):
        return "ALG_AES256_GCM_IV12_TAG16"

    else:
        raise ValueError(f"No recognized enum value in enum type: {dafny_input=}")


def aws_cryptography_materialproviders_CreateRawAesKeyringInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateRawAesKeyringInput(
        key_namespace=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.keyNamespace
        ).decode("utf-16-be"),
        key_name=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.keyName
        ).decode("utf-16-be"),
        wrapping_key=bytes(dafny_input.wrappingKey),
        wrapping_alg=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_AesWrappingAlg(
            dafny_input.wrappingAlg
        ),
    )


def aws_cryptography_materialproviders_PaddingScheme(dafny_input):
    if isinstance(dafny_input, PaddingScheme_PKCS1):
        return "PKCS1"

    elif isinstance(dafny_input, PaddingScheme_OAEP__SHA1__MGF1):
        return "OAEP_SHA1_MGF1"

    elif isinstance(dafny_input, PaddingScheme_OAEP__SHA256__MGF1):
        return "OAEP_SHA256_MGF1"

    elif isinstance(dafny_input, PaddingScheme_OAEP__SHA384__MGF1):
        return "OAEP_SHA384_MGF1"

    elif isinstance(dafny_input, PaddingScheme_OAEP__SHA512__MGF1):
        return "OAEP_SHA512_MGF1"

    else:
        raise ValueError(f"No recognized enum value in enum type: {dafny_input=}")


def aws_cryptography_materialproviders_CreateRawRsaKeyringInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateRawRsaKeyringInput(
        key_namespace=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.keyNamespace
        ).decode("utf-16-be"),
        key_name=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.keyName
        ).decode("utf-16-be"),
        padding_scheme=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_PaddingScheme(
            dafny_input.paddingScheme
        ),
        public_key=(
            (bytes(dafny_input.publicKey.value))
            if (dafny_input.publicKey.is_Some)
            else None
        ),
        private_key=(
            (bytes(dafny_input.privateKey.value))
            if (dafny_input.privateKey.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_RawEcdhStaticConfigurations(dafny_input):
    # Convert RawEcdhStaticConfigurations
    if isinstance(dafny_input, RawEcdhStaticConfigurations_PublicKeyDiscovery):
        RawEcdhStaticConfigurations_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.RawEcdhStaticConfigurationsPublicKeyDiscovery(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_PublicKeyDiscoveryInput(
                dafny_input.PublicKeyDiscovery
            )
        )
    elif isinstance(
        dafny_input, RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey
    ):
        RawEcdhStaticConfigurations_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.RawEcdhStaticConfigurationsRawPrivateKeyToStaticPublicKey(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_RawPrivateKeyToStaticPublicKeyInput(
                dafny_input.RawPrivateKeyToStaticPublicKey
            )
        )
    elif isinstance(
        dafny_input, RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey
    ):
        RawEcdhStaticConfigurations_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.RawEcdhStaticConfigurationsEphemeralPrivateKeyToStaticPublicKey(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_EphemeralPrivateKeyToStaticPublicKeyInput(
                dafny_input.EphemeralPrivateKeyToStaticPublicKey
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return RawEcdhStaticConfigurations_union_value


def aws_cryptography_materialproviders_PublicKeyDiscoveryInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.PublicKeyDiscoveryInput(
        recipient_static_private_key=bytes(dafny_input.recipientStaticPrivateKey),
    )


def aws_cryptography_materialproviders_RawPrivateKeyToStaticPublicKeyInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.RawPrivateKeyToStaticPublicKeyInput(
        sender_static_private_key=bytes(dafny_input.senderStaticPrivateKey),
        recipient_public_key=bytes(dafny_input.recipientPublicKey),
    )


def aws_cryptography_materialproviders_EphemeralPrivateKeyToStaticPublicKeyInput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.EphemeralPrivateKeyToStaticPublicKeyInput(
        recipient_public_key=bytes(dafny_input.recipientPublicKey),
    )


def aws_cryptography_materialproviders_CreateRawEcdhKeyringInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateRawEcdhKeyringInput(
        key_agreement_scheme=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_RawEcdhStaticConfigurations(
            dafny_input.KeyAgreementScheme
        ),
        curve_spec=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDHCurveSpec(
            dafny_input.curveSpec
        ),
    )


def aws_cryptography_materialproviders_CreateDefaultCryptographicMaterialsManagerInput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateDefaultCryptographicMaterialsManagerInput(
        keyring=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KeyringReference(
                    dafny_input.keyring
                )
            )
            if (dafny_input.keyring is not None)
            else None
        ),
    )


def aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(
    dafny_input,
):
    if hasattr(dafny_input, "_native_impl"):
        return dafny_input._native_impl

    else:
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references import (
            CryptographicMaterialsManager,
        )

        return CryptographicMaterialsManager(_impl=dafny_input)


def aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMInput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateRequiredEncryptionContextCMMInput(
        underlying_cmm=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(
                    dafny_input.underlyingCMM.UnwrapOr(None)
                )
            )
            if (dafny_input.underlyingCMM.UnwrapOr(None) is not None)
            else None
        ),
        keyring=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KeyringReference(
                    dafny_input.keyring.UnwrapOr(None)
                )
            )
            if (dafny_input.keyring.UnwrapOr(None) is not None)
            else None
        ),
        required_encryption_context_keys=[
            bytes(list_element.Elements).decode("utf-8")
            for list_element in dafny_input.requiredEncryptionContextKeys
        ],
    )


def aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheInput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateCryptographicMaterialsCacheInput(
        cache=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CacheType(
            dafny_input.cache
        ),
    )


def aws_cryptography_materialproviders_CreateDefaultClientSupplierInput(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.CreateDefaultClientSupplierInput()
    )


def aws_cryptography_materialproviders_InitializeEncryptionMaterialsInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.InitializeEncryptionMaterialsInput(
        algorithm_suite_id=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_AlgorithmSuiteId(
            dafny_input.algorithmSuiteId
        ),
        encryption_context={
            bytes(key.Elements).decode("utf-8"): bytes(value.Elements).decode("utf-8")
            for (key, value) in dafny_input.encryptionContext.items
        },
        required_encryption_context_keys=[
            bytes(list_element.Elements).decode("utf-8")
            for list_element in dafny_input.requiredEncryptionContextKeys
        ],
        signing_key=(
            (bytes(dafny_input.signingKey.value))
            if (dafny_input.signingKey.is_Some)
            else None
        ),
        verification_key=(
            (bytes(dafny_input.verificationKey.value))
            if (dafny_input.verificationKey.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviders_InitializeDecryptionMaterialsInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.InitializeDecryptionMaterialsInput(
        algorithm_suite_id=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_AlgorithmSuiteId(
            dafny_input.algorithmSuiteId
        ),
        encryption_context={
            bytes(key.Elements).decode("utf-8"): bytes(value.Elements).decode("utf-8")
            for (key, value) in dafny_input.encryptionContext.items
        },
        required_encryption_context_keys=[
            bytes(list_element.Elements).decode("utf-8")
            for list_element in dafny_input.requiredEncryptionContextKeys
        ],
    )


def aws_cryptography_materialproviders_ValidEncryptionMaterialsTransitionInput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.ValidEncryptionMaterialsTransitionInput(
        start=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_EncryptionMaterials(
            dafny_input.start
        ),
        stop=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_EncryptionMaterials(
            dafny_input.stop
        ),
    )


def aws_cryptography_materialproviders_ValidDecryptionMaterialsTransitionInput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.ValidDecryptionMaterialsTransitionInput(
        start=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DecryptionMaterials(
            dafny_input.start
        ),
        stop=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DecryptionMaterials(
            dafny_input.stop
        ),
    )


def aws_cryptography_materialproviders_GetAlgorithmSuiteInfoInput(dafny_input):
    return bytes(dafny_input)


def aws_cryptography_materialproviders_ValidateCommitmentPolicyOnEncryptInput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.ValidateCommitmentPolicyOnEncryptInput(
        algorithm=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_AlgorithmSuiteId(
            dafny_input.algorithm
        ),
        commitment_policy=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CommitmentPolicy(
            dafny_input.commitmentPolicy
        ),
    )


def aws_cryptography_materialproviders_ValidateCommitmentPolicyOnDecryptInput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.ValidateCommitmentPolicyOnDecryptInput(
        algorithm=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_AlgorithmSuiteId(
            dafny_input.algorithm
        ),
        commitment_policy=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CommitmentPolicy(
            dafny_input.commitmentPolicy
        ),
    )


def aws_cryptography_materialproviders_CreateKeyringOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KeyringReference(
        dafny_input
    )


def aws_cryptography_materialproviders_CreateCryptographicMaterialsManagerOutput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(
        dafny_input
    )


def aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMOutput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(
        dafny_input
    )


def aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheOutput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CryptographicMaterialsCacheReference(
        dafny_input
    )


def aws_cryptography_materialproviders_CreateDefaultClientSupplierOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ClientSupplierReference(
        dafny_input
    )


def aws_cryptography_materialproviders_DdbClientReference(dafny_input):
    return dafny_input._impl


def aws_cryptography_materialproviders_StaticConfigurations(dafny_input):
    # Convert StaticConfigurations
    if isinstance(dafny_input, StaticConfigurations_AWS__KMS__ECDH):
        StaticConfigurations_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.StaticConfigurationsAWS_KMS_ECDH(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_KmsEcdhStaticConfigurations(
                dafny_input.AWS__KMS__ECDH
            )
        )
    elif isinstance(dafny_input, StaticConfigurations_RAW__ECDH):
        StaticConfigurations_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.StaticConfigurationsRAW_ECDH(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_RawEcdhStaticConfigurations(
                dafny_input.RAW__ECDH
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return StaticConfigurations_union_value


def aws_cryptography_materialproviders_KeyAgreementScheme(dafny_input):
    # Convert KeyAgreementScheme
    if isinstance(dafny_input, KeyAgreementScheme_StaticConfiguration):
        KeyAgreementScheme_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.KeyAgreementSchemeStaticConfiguration(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_StaticConfigurations(
                dafny_input.StaticConfiguration
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return KeyAgreementScheme_union_value


def aws_cryptography_materialproviders_MaterialProvidersConfig(dafny_input):
    # Deferred import of .config to avoid circular dependency
    import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.config

    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.config.MaterialProvidersConfig()
    )
