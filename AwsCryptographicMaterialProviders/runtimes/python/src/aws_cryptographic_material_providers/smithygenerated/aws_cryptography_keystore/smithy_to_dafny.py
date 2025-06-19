# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from _dafny import Map, Seq
from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes import (
    BeaconKeyMaterials_BeaconKeyMaterials as DafnyBeaconKeyMaterials,
    BranchKeyMaterials_BranchKeyMaterials as DafnyBranchKeyMaterials,
    CreateKeyInput_CreateKeyInput as DafnyCreateKeyInput,
    CreateKeyOutput_CreateKeyOutput as DafnyCreateKeyOutput,
    CreateKeyStoreInput_CreateKeyStoreInput as DafnyCreateKeyStoreInput,
    CreateKeyStoreOutput_CreateKeyStoreOutput as DafnyCreateKeyStoreOutput,
    Discovery_Discovery as DafnyDiscovery,
    GetActiveBranchKeyInput_GetActiveBranchKeyInput as DafnyGetActiveBranchKeyInput,
    GetActiveBranchKeyOutput_GetActiveBranchKeyOutput as DafnyGetActiveBranchKeyOutput,
    GetBeaconKeyInput_GetBeaconKeyInput as DafnyGetBeaconKeyInput,
    GetBeaconKeyOutput_GetBeaconKeyOutput as DafnyGetBeaconKeyOutput,
    GetBranchKeyVersionInput_GetBranchKeyVersionInput as DafnyGetBranchKeyVersionInput,
    GetBranchKeyVersionOutput_GetBranchKeyVersionOutput as DafnyGetBranchKeyVersionOutput,
    GetKeyStoreInfoOutput_GetKeyStoreInfoOutput as DafnyGetKeyStoreInfoOutput,
    HierarchyVersion_v1,
    HierarchyVersion_v2,
    KMSConfiguration_discovery,
    KMSConfiguration_kmsKeyArn,
    KMSConfiguration_kmsMRKeyArn,
    KMSConfiguration_mrDiscovery,
    KeyStoreConfig_KeyStoreConfig as DafnyKeyStoreConfig,
    MRDiscovery_MRDiscovery as DafnyMRDiscovery,
    VersionKeyInput_VersionKeyInput as DafnyVersionKeyInput,
    VersionKeyOutput_VersionKeyOutput as DafnyVersionKeyOutput,
)
import aws_cryptographic_material_providers.internaldafny.generated.module_
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny
from aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes import (
    IDynamoDBClient,
)
import aws_cryptography_internal_dynamodb.internaldafny.generated.module_
from aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes import (
    IKMSClient,
)
import aws_cryptography_internal_kms.internaldafny.generated.module_
from smithy_dafny_standard_library.internaldafny.generated.Wrappers import (
    Option_None,
    Option_Some,
)


def smithy_api_Unit(native_input):
    return None


def aws_cryptography_keystore_CreateKeyStoreInput(native_input):
    return DafnyCreateKeyStoreInput()


def aws_cryptography_keystore_CreateKeyInput(native_input):
    return DafnyCreateKeyInput(
        branchKeyIdentifier=(
            (
                Option_Some(
                    Seq(
                        "".join(
                            [
                                chr(int.from_bytes(pair, "big"))
                                for pair in zip(
                                    *[
                                        iter(
                                            native_input.branch_key_identifier.encode(
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
            if (native_input.branch_key_identifier is not None)
            else (Option_None())
        ),
        encryptionContext=(
            (
                Option_Some(
                    Map(
                        {
                            Seq(key.encode("utf-8")): Seq(value.encode("utf-8"))
                            for (key, value) in native_input.encryption_context.items()
                        }
                    )
                )
            )
            if (native_input.encryption_context is not None)
            else (Option_None())
        ),
        hierarchyVersion=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_HierarchyVersion(
                        native_input.hierarchy_version
                    )
                )
            )
            if (native_input.hierarchy_version is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_keystore_HierarchyVersion(native_input):
    if native_input == "1":
        return HierarchyVersion_v1()

    elif native_input == "2":
        return HierarchyVersion_v2()

    else:
        raise ValueError(f"No recognized enum value in enum type: {native_input=}")


def aws_cryptography_keystore_VersionKeyInput(native_input):
    return DafnyVersionKeyInput(
        branchKeyIdentifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.branch_key_identifier.encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_keystore_GetActiveBranchKeyInput(native_input):
    return DafnyGetActiveBranchKeyInput(
        branchKeyIdentifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.branch_key_identifier.encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_keystore_GetBranchKeyVersionInput(native_input):
    return DafnyGetBranchKeyVersionInput(
        branchKeyIdentifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.branch_key_identifier.encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
        branchKeyVersion=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.branch_key_version.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_keystore_GetBeaconKeyInput(native_input):
    return DafnyGetBeaconKeyInput(
        branchKeyIdentifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.branch_key_identifier.encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_keystore_GetKeyStoreInfoOutput(native_input):
    return DafnyGetKeyStoreInfoOutput(
        keyStoreId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_store_id.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        keyStoreName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.key_store_name.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        logicalKeyStoreName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.logical_key_store_name.encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
        grantTokens=Seq(
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
                for list_element in native_input.grant_tokens
            ]
        ),
        kmsConfiguration=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_KMSConfiguration(
            native_input.kms_configuration
        ),
    )


def aws_cryptography_keystore_KMSConfiguration(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.KMSConfigurationKmsKeyArn,
    ):
        KMSConfiguration_union_value = KMSConfiguration_kmsKeyArn(
            Seq(
                "".join(
                    [
                        chr(int.from_bytes(pair, "big"))
                        for pair in zip(
                            *[iter(native_input.value.encode("utf-16-be"))] * 2
                        )
                    ]
                )
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.KMSConfigurationKmsMRKeyArn,
    ):
        KMSConfiguration_union_value = KMSConfiguration_kmsMRKeyArn(
            Seq(
                "".join(
                    [
                        chr(int.from_bytes(pair, "big"))
                        for pair in zip(
                            *[iter(native_input.value.encode("utf-16-be"))] * 2
                        )
                    ]
                )
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.KMSConfigurationDiscovery,
    ):
        KMSConfiguration_union_value = KMSConfiguration_discovery(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_Discovery(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.KMSConfigurationMrDiscovery,
    ):
        KMSConfiguration_union_value = KMSConfiguration_mrDiscovery(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_MRDiscovery(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return KMSConfiguration_union_value


def aws_cryptography_keystore_Discovery(native_input):
    return DafnyDiscovery()


def aws_cryptography_keystore_MRDiscovery(native_input):
    return DafnyMRDiscovery(
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


def aws_cryptography_keystore_CreateKeyStoreOutput(native_input):
    return DafnyCreateKeyStoreOutput(
        tableArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.table_arn.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_keystore_CreateKeyOutput(native_input):
    return DafnyCreateKeyOutput(
        branchKeyIdentifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.branch_key_identifier.encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_keystore_VersionKeyOutput(native_input):
    return DafnyVersionKeyOutput()


def aws_cryptography_keystore_GetActiveBranchKeyOutput(native_input):
    return DafnyGetActiveBranchKeyOutput(
        branchKeyMaterials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_BranchKeyMaterials(
            native_input.branch_key_materials
        ),
    )


def aws_cryptography_keystore_BranchKeyMaterials(native_input):
    return DafnyBranchKeyMaterials(
        branchKeyIdentifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.branch_key_identifier.encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
        branchKeyVersion=Seq(native_input.branch_key_version.encode("utf-8")),
        encryptionContext=Map(
            {
                Seq(key.encode("utf-8")): Seq(value.encode("utf-8"))
                for (key, value) in native_input.encryption_context.items()
            }
        ),
        branchKey=Seq(native_input.branch_key),
        kmsArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.kms_arn.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        createTime=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.create_time.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        hierarchyVersion=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_HierarchyVersion(
            native_input.hierarchy_version
        ),
    )


def aws_cryptography_keystore_GetBranchKeyVersionOutput(native_input):
    return DafnyGetBranchKeyVersionOutput(
        branchKeyMaterials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_BranchKeyMaterials(
            native_input.branch_key_materials
        ),
    )


def aws_cryptography_keystore_GetBeaconKeyOutput(native_input):
    return DafnyGetBeaconKeyOutput(
        beaconKeyMaterials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_BeaconKeyMaterials(
            native_input.beacon_key_materials
        ),
    )


def aws_cryptography_keystore_BeaconKeyMaterials(native_input):
    return DafnyBeaconKeyMaterials(
        beaconKeyIdentifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.beacon_key_identifier.encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
        encryptionContext=Map(
            {
                Seq(key.encode("utf-8")): Seq(value.encode("utf-8"))
                for (key, value) in native_input.encryption_context.items()
            }
        ),
        beaconKey=(
            (Option_Some(Seq(native_input.beacon_key)))
            if (native_input.beacon_key is not None)
            else (Option_None())
        ),
        hmacKeys=(
            (
                Option_Some(
                    Map(
                        {
                            Seq(
                                "".join(
                                    [
                                        chr(int.from_bytes(pair, "big"))
                                        for pair in zip(
                                            *[iter(key.encode("utf-16-be"))] * 2
                                        )
                                    ]
                                )
                            ): Seq(value)
                            for (key, value) in native_input.hmac_keys.items()
                        }
                    )
                )
            )
            if (native_input.hmac_keys is not None)
            else (Option_None())
        ),
        kmsArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.kms_arn.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        createTime=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.create_time.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        hierarchyVersion=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_HierarchyVersion(
            native_input.hierarchy_version
        ),
    )


def aws_cryptography_keystore_DdbClientReference(native_input):
    import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb

    client = aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb.default__.DynamoDBClient(
        boto_client=native_input
    )
    client.value.impl = native_input
    return client.value


def aws_cryptography_keystore_KmsClientReference(native_input):
    import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms

    client = aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms.default__.KMSClient(
        boto_client=native_input
    )
    client.value.impl = native_input
    return client.value


def aws_cryptography_keystore_KeyStoreConfig(native_input):
    return DafnyKeyStoreConfig(
        ddbTableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.ddb_table_name.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        kmsConfiguration=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_KMSConfiguration(
            native_input.kms_configuration
        ),
        logicalKeyStoreName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.logical_key_store_name.encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
        id=(
            (
                Option_Some(
                    Seq(
                        "".join(
                            [
                                chr(int.from_bytes(pair, "big"))
                                for pair in zip(
                                    *[iter(native_input.id.encode("utf-16-be"))] * 2
                                )
                            ]
                        )
                    )
                )
            )
            if (native_input.id is not None)
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
        ddbClient=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_DdbClientReference(
                        native_input.ddb_client
                    )
                )
            )
            if (
                (native_input.ddb_client is not None)
                and (
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_DdbClientReference(
                        native_input.ddb_client
                    )
                    is not None
                )
            )
            else (Option_None())
        ),
        kmsClient=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_KmsClientReference(
                        native_input.kms_client
                    )
                )
            )
            if (
                (native_input.kms_client is not None)
                and (
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_KmsClientReference(
                        native_input.kms_client
                    )
                    is not None
                )
            )
            else (Option_None())
        ),
    )
