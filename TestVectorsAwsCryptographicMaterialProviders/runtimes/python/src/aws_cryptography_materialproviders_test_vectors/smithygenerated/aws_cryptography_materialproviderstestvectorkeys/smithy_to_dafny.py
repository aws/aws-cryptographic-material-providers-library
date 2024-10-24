# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from _dafny import Seq
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny
import aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny
from aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AwsCryptographyMaterialProvidersTestVectorKeysTypes import (
    CmmOperation_DECRYPT,
    CmmOperation_ENCRYPT,
    GetKeyDescriptionInput_GetKeyDescriptionInput as DafnyGetKeyDescriptionInput,
    GetKeyDescriptionOutput_GetKeyDescriptionOutput as DafnyGetKeyDescriptionOutput,
    HierarchyKeyring_HierarchyKeyring as DafnyHierarchyKeyring,
    KMSInfo_KMSInfo as DafnyKMSInfo,
    KeyDescription_AES,
    KeyDescription_ECDH,
    KeyDescription_Hierarchy,
    KeyDescription_Kms,
    KeyDescription_KmsECDH,
    KeyDescription_KmsMrk,
    KeyDescription_KmsMrkDiscovery,
    KeyDescription_KmsRsa,
    KeyDescription_Multi,
    KeyDescription_RSA,
    KeyDescription_RequiredEncryptionContext,
    KeyDescription_Static,
    KeyVectorsConfig_KeyVectorsConfig as DafnyKeyVectorsConfig,
    KmsEcdhKeyring_KmsEcdhKeyring as DafnyKmsEcdhKeyring,
    KmsMrkAwareDiscovery_KmsMrkAwareDiscovery as DafnyKmsMrkAwareDiscovery,
    KmsMrkAware_KmsMrkAware as DafnyKmsMrkAware,
    KmsRsaKeyring_KmsRsaKeyring as DafnyKmsRsaKeyring,
    MultiKeyring_MultiKeyring as DafnyMultiKeyring,
    RawAES_RawAES as DafnyRawAES,
    RawEcdh_RawEcdh as DafnyRawEcdh,
    RawRSA_RawRSA as DafnyRawRSA,
    RequiredEncryptionContextCMM_RequiredEncryptionContextCMM as DafnyRequiredEncryptionContextCMM,
    SerializeKeyDescriptionInput_SerializeKeyDescriptionInput as DafnySerializeKeyDescriptionInput,
    SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput as DafnySerializeKeyDescriptionOutput,
    StaticKeyring_StaticKeyring as DafnyStaticKeyring,
    TestVectorCmmInput_TestVectorCmmInput as DafnyTestVectorCmmInput,
    TestVectorKeyringInput_TestVectorKeyringInput as DafnyTestVectorKeyringInput,
)
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.module_
import aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models
import aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny
from smithy_dafny_standard_library.internaldafny.generated.Wrappers import (
    Option_None,
    Option_Some,
)


def aws_cryptography_materialproviderstestvectorkeys_TestVectorKeyringInput(
    native_input,
):
    return DafnyTestVectorKeyringInput(
        keyDescription=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_KeyDescription(
            native_input.key_description
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_KeyDescription(native_input):
    if isinstance(
        native_input,
        aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionKms,
    ):
        KeyDescription_union_value = KeyDescription_Kms(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_KMSInfo(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionKmsMrk,
    ):
        KeyDescription_union_value = KeyDescription_KmsMrk(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_KmsMrkAware(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionKmsMrkDiscovery,
    ):
        KeyDescription_union_value = KeyDescription_KmsMrkDiscovery(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_KmsMrkAwareDiscovery(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionRSA,
    ):
        KeyDescription_union_value = KeyDescription_RSA(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_RawRSA(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionAES,
    ):
        KeyDescription_union_value = KeyDescription_AES(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_RawAES(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionECDH,
    ):
        KeyDescription_union_value = KeyDescription_ECDH(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_RawEcdh(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionStatic,
    ):
        KeyDescription_union_value = KeyDescription_Static(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_StaticKeyring(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionKmsRsa,
    ):
        KeyDescription_union_value = KeyDescription_KmsRsa(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_KmsRsaKeyring(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionKmsECDH,
    ):
        KeyDescription_union_value = KeyDescription_KmsECDH(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_KmsEcdhKeyring(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionHierarchy,
    ):
        KeyDescription_union_value = KeyDescription_Hierarchy(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_HierarchyKeyring(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionMulti,
    ):
        KeyDescription_union_value = KeyDescription_Multi(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_MultiKeyring(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionRequiredEncryptionContext,
    ):
        KeyDescription_union_value = KeyDescription_RequiredEncryptionContext(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_RequiredEncryptionContextCMM(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return KeyDescription_union_value


def aws_cryptography_materialproviderstestvectorkeys_KMSInfo(native_input):
    return DafnyKMSInfo(
        keyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_KmsMrkAware(native_input):
    return DafnyKmsMrkAware(
        keyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_KmsMrkAwareDiscovery(native_input):
    return DafnyKmsMrkAwareDiscovery(
        keyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        defaultMrkRegion=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.default_mrk_region.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        awsKmsDiscoveryFilter=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DiscoveryFilter(
                        native_input.aws_kms_discovery_filter
                    )
                )
            )
            if (native_input.aws_kms_discovery_filter is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_RawRSA(native_input):
    return DafnyRawRSA(
        keyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        providerId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.provider_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        padding=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_PaddingScheme(
            native_input.padding
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_RawAES(native_input):
    return DafnyRawAES(
        keyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        providerId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.provider_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_RawEcdh(native_input):
    return DafnyRawEcdh(
        senderKeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.sender_key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        recipientKeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.recipient_key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        senderPublicKey=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.sender_public_key.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        recipientPublicKey=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.recipient_public_key.encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
        providerId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.provider_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        curveSpec=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.curve_spec.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        keyAgreementScheme=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_agreement_scheme.encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_StaticKeyring(native_input):
    return DafnyStaticKeyring(
        keyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_KmsRsaKeyring(native_input):
    return DafnyKmsRsaKeyring(
        keyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        encryptionAlgorithm=aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(
            native_input.encryption_algorithm
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_KmsEcdhKeyring(native_input):
    return DafnyKmsEcdhKeyring(
        senderKeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.sender_key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        recipientKeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.recipient_key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        senderPublicKey=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.sender_public_key.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        recipientPublicKey=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.recipient_public_key.encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
        curveSpec=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.curve_spec.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        keyAgreementScheme=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_agreement_scheme.encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_HierarchyKeyring(native_input):
    return DafnyHierarchyKeyring(
        keyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_MultiKeyring(native_input):
    return DafnyMultiKeyring(
        generator=(
            (
                Option_Some(
                    aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_KeyDescription(
                        native_input.generator
                    )
                )
            )
            if (native_input.generator is not None)
            else (Option_None())
        ),
        childKeyrings=Seq(
            [
                aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_KeyDescription(
                    list_element
                )
                for list_element in native_input.child_keyrings
            ]
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_RequiredEncryptionContextCMM(
    native_input,
):
    return DafnyRequiredEncryptionContextCMM(
        underlying=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_KeyDescription(
            native_input.underlying
        ),
        requiredEncryptionContextKeys=Seq(
            [
                Seq(list_element.encode("utf-8"))
                for list_element in native_input.required_encryption_context_keys
            ]
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_TestVectorCmmInput(native_input):
    return DafnyTestVectorCmmInput(
        keyDescription=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_KeyDescription(
            native_input.key_description
        ),
        forOperation=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_CmmOperation(
            native_input.for_operation
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_CmmOperation(native_input):
    if native_input == "ENCRYPT":
        return CmmOperation_ENCRYPT()

    elif native_input == "DECRYPT":
        return CmmOperation_DECRYPT()

    else:
        raise ValueError(f"No recognized enum value in enum type: {native_input=}")


def aws_cryptography_materialproviderstestvectorkeys_GetKeyDescriptionInput(
    native_input,
):
    return DafnyGetKeyDescriptionInput(
        json=Seq(native_input.json),
    )


def aws_cryptography_materialproviderstestvectorkeys_SerializeKeyDescriptionInput(
    native_input,
):
    return DafnySerializeKeyDescriptionInput(
        keyDescription=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_KeyDescription(
            native_input.key_description
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_CreateWrappedTestVectorCmmOutput(
    native_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(
        native_input
    )


def aws_cryptography_materialproviderstestvectorkeys_GetKeyDescriptionOutput(
    native_input,
):
    return DafnyGetKeyDescriptionOutput(
        keyDescription=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_KeyDescription(
            native_input.key_description
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_SerializeKeyDescriptionOutput(
    native_input,
):
    return DafnySerializeKeyDescriptionOutput(
        json=Seq(native_input.json),
    )


def aws_cryptography_materialproviderstestvectorkeys_KeyVectorsConfig(native_input):
    return DafnyKeyVectorsConfig(
        keyManifestPath=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_manifest_path.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )
