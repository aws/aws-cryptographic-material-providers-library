# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy
import aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk
from aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AwsCryptographyMaterialProvidersTestVectorKeysTypes import (
    CmmOperation_DECRYPT,
    CmmOperation_ENCRYPT,
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
)
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.module_
import aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy
import aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models


def aws_cryptography_materialproviderstestvectorkeys_KeyDescription(dafny_input):
    # Convert KeyDescription
    if isinstance(dafny_input, KeyDescription_Kms):
        KeyDescription_union_value = aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionKms(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_KMSInfo(
                dafny_input.Kms
            )
        )
    elif isinstance(dafny_input, KeyDescription_KmsMrk):
        KeyDescription_union_value = aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionKmsMrk(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_KmsMrkAware(
                dafny_input.KmsMrk
            )
        )
    elif isinstance(dafny_input, KeyDescription_KmsMrkDiscovery):
        KeyDescription_union_value = aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionKmsMrkDiscovery(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_KmsMrkAwareDiscovery(
                dafny_input.KmsMrkDiscovery
            )
        )
    elif isinstance(dafny_input, KeyDescription_RSA):
        KeyDescription_union_value = aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionRSA(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_RawRSA(
                dafny_input.RSA
            )
        )
    elif isinstance(dafny_input, KeyDescription_AES):
        KeyDescription_union_value = aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionAES(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_RawAES(
                dafny_input.AES
            )
        )
    elif isinstance(dafny_input, KeyDescription_ECDH):
        KeyDescription_union_value = aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionECDH(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_RawEcdh(
                dafny_input.ECDH
            )
        )
    elif isinstance(dafny_input, KeyDescription_Static):
        KeyDescription_union_value = aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionStatic(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_StaticKeyring(
                dafny_input.Static
            )
        )
    elif isinstance(dafny_input, KeyDescription_KmsRsa):
        KeyDescription_union_value = aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionKmsRsa(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_KmsRsaKeyring(
                dafny_input.KmsRsa
            )
        )
    elif isinstance(dafny_input, KeyDescription_KmsECDH):
        KeyDescription_union_value = aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionKmsECDH(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_KmsEcdhKeyring(
                dafny_input.KmsECDH
            )
        )
    elif isinstance(dafny_input, KeyDescription_Hierarchy):
        KeyDescription_union_value = aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionHierarchy(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_HierarchyKeyring(
                dafny_input.Hierarchy
            )
        )
    elif isinstance(dafny_input, KeyDescription_Multi):
        KeyDescription_union_value = aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionMulti(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_MultiKeyring(
                dafny_input.Multi
            )
        )
    elif isinstance(dafny_input, KeyDescription_RequiredEncryptionContext):
        KeyDescription_union_value = aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KeyDescriptionRequiredEncryptionContext(
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_RequiredEncryptionContextCMM(
                dafny_input.RequiredEncryptionContext
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return KeyDescription_union_value


def aws_cryptography_materialproviderstestvectorkeys_KMSInfo(dafny_input):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KMSInfo(
        key_id=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.keyId).decode(
            "utf-16-be"
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_KmsMrkAware(dafny_input):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KmsMrkAware(
        key_id=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.keyId).decode(
            "utf-16-be"
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_KmsMrkAwareDiscovery(dafny_input):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KmsMrkAwareDiscovery(
        key_id=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.keyId).decode(
            "utf-16-be"
        ),
        default_mrk_region=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.defaultMrkRegion
        ).decode("utf-16-be"),
        aws_kms_discovery_filter=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DiscoveryFilter(
                    dafny_input.awsKmsDiscoveryFilter.value
                )
            )
            if (dafny_input.awsKmsDiscoveryFilter.is_Some)
            else None
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_RawRSA(dafny_input):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.RawRSA(
        key_id=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.keyId).decode(
            "utf-16-be"
        ),
        provider_id=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.providerId
        ).decode("utf-16-be"),
        padding=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_PaddingScheme(
            dafny_input.padding
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_RawAES(dafny_input):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.RawAES(
        key_id=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.keyId).decode(
            "utf-16-be"
        ),
        provider_id=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.providerId
        ).decode("utf-16-be"),
    )


def aws_cryptography_materialproviderstestvectorkeys_RawEcdh(dafny_input):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.RawEcdh(
        sender_key_id=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.senderKeyId
        ).decode("utf-16-be"),
        recipient_key_id=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.recipientKeyId
        ).decode("utf-16-be"),
        sender_public_key=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.senderPublicKey
        ).decode("utf-16-be"),
        recipient_public_key=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.recipientPublicKey
        ).decode("utf-16-be"),
        provider_id=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.providerId
        ).decode("utf-16-be"),
        curve_spec=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.curveSpec
        ).decode("utf-16-be"),
        key_agreement_scheme=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.keyAgreementScheme
        ).decode("utf-16-be"),
    )


def aws_cryptography_materialproviderstestvectorkeys_StaticKeyring(dafny_input):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.StaticKeyring(
        key_id=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.keyId).decode(
            "utf-16-be"
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_KmsRsaKeyring(dafny_input):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KmsRsaKeyring(
        key_id=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.keyId).decode(
            "utf-16-be"
        ),
        encryption_algorithm=aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_EncryptionAlgorithmSpec(
            dafny_input.encryptionAlgorithm
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_KmsEcdhKeyring(dafny_input):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.KmsEcdhKeyring(
        sender_key_id=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.senderKeyId
        ).decode("utf-16-be"),
        recipient_key_id=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.recipientKeyId
        ).decode("utf-16-be"),
        sender_public_key=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.senderPublicKey
        ).decode("utf-16-be"),
        recipient_public_key=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.recipientPublicKey
        ).decode("utf-16-be"),
        curve_spec=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.curveSpec
        ).decode("utf-16-be"),
        key_agreement_scheme=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.keyAgreementScheme
        ).decode("utf-16-be"),
    )


def aws_cryptography_materialproviderstestvectorkeys_HierarchyKeyring(dafny_input):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.HierarchyKeyring(
        key_id=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.keyId).decode(
            "utf-16-be"
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_MultiKeyring(dafny_input):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.MultiKeyring(
        generator=(
            (
                aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_KeyDescription(
                    dafny_input.generator.value
                )
            )
            if (dafny_input.generator.is_Some)
            else None
        ),
        child_keyrings=[
            aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_KeyDescription(
                list_element
            )
            for list_element in dafny_input.childKeyrings
        ],
    )


def aws_cryptography_materialproviderstestvectorkeys_RequiredEncryptionContextCMM(
    dafny_input,
):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.RequiredEncryptionContextCMM(
        underlying=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_KeyDescription(
            dafny_input.underlying
        ),
        required_encryption_context_keys=[
            bytes(list_element.Elements).decode("utf-8")
            for list_element in dafny_input.requiredEncryptionContextKeys
        ],
    )


def aws_cryptography_materialproviderstestvectorkeys_TestVectorKeyringInput(
    dafny_input,
):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.TestVectorKeyringInput(
        key_description=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_KeyDescription(
            dafny_input.keyDescription
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_CmmOperation(dafny_input):
    if isinstance(dafny_input, CmmOperation_ENCRYPT):
        return "ENCRYPT"

    elif isinstance(dafny_input, CmmOperation_DECRYPT):
        return "DECRYPT"

    else:
        raise ValueError(f"No recognized enum value in enum type: {dafny_input=}")


def aws_cryptography_materialproviderstestvectorkeys_TestVectorCmmInput(dafny_input):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.TestVectorCmmInput(
        key_description=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_KeyDescription(
            dafny_input.keyDescription
        ),
        for_operation=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_CmmOperation(
            dafny_input.forOperation
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_GetKeyDescriptionInput(
    dafny_input,
):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.GetKeyDescriptionInput(
        json=bytes(dafny_input.json),
    )


def aws_cryptography_materialproviderstestvectorkeys_SerializeKeyDescriptionInput(
    dafny_input,
):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.SerializeKeyDescriptionInput(
        key_description=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_KeyDescription(
            dafny_input.keyDescription
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_CreateWrappedTestVectorCmmOutput(
    dafny_input,
):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(
        dafny_input
    )


def aws_cryptography_materialproviderstestvectorkeys_GetKeyDescriptionOutput(
    dafny_input,
):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.GetKeyDescriptionOutput(
        key_description=aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_KeyDescription(
            dafny_input.keyDescription
        ),
    )


def aws_cryptography_materialproviderstestvectorkeys_SerializeKeyDescriptionOutput(
    dafny_input,
):
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.models.SerializeKeyDescriptionOutput(
        json=bytes(dafny_input.json),
    )


def aws_cryptography_materialproviderstestvectorkeys_KeyVectorsConfig(dafny_input):
    # Deferred import of .config to avoid circular dependency
    import aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.config

    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.config.KeyVectorsConfig(
        key_manifest_path=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.keyManifestPath
        ).decode("utf-16-be"),
    )
