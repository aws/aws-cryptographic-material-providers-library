# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from _dafny import Map, Seq
from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes import (
    ActiveHierarchicalSymmetricBeacon_ActiveHierarchicalSymmetricBeacon as DafnyActiveHierarchicalSymmetricBeacon,
    ActiveHierarchicalSymmetric_ActiveHierarchicalSymmetric as DafnyActiveHierarchicalSymmetric,
    AwsKms_AwsKms as DafnyAwsKms,
    BeaconKeyMaterials_BeaconKeyMaterials as DafnyBeaconKeyMaterials,
    BranchKeyMaterials_BranchKeyMaterials as DafnyBranchKeyMaterials,
    CreateKeyInput_CreateKeyInput as DafnyCreateKeyInput,
    CreateKeyOutput_CreateKeyOutput as DafnyCreateKeyOutput,
    CreateKeyStoreInput_CreateKeyStoreInput as DafnyCreateKeyStoreInput,
    CreateKeyStoreOutput_CreateKeyStoreOutput as DafnyCreateKeyStoreOutput,
    DeleteMutationInput_DeleteMutationInput as DafnyDeleteMutationInput,
    DeleteMutationOutput_DeleteMutationOutput as DafnyDeleteMutationOutput,
    Discovery_Discovery as DafnyDiscovery,
    DynamoDBTable_DynamoDBTable as DafnyDynamoDBTable,
    EncryptedHierarchicalKey_EncryptedHierarchicalKey as DafnyEncryptedHierarchicalKey,
    GetActiveBranchKeyInput_GetActiveBranchKeyInput as DafnyGetActiveBranchKeyInput,
    GetActiveBranchKeyOutput_GetActiveBranchKeyOutput as DafnyGetActiveBranchKeyOutput,
    GetBeaconKeyInput_GetBeaconKeyInput as DafnyGetBeaconKeyInput,
    GetBeaconKeyOutput_GetBeaconKeyOutput as DafnyGetBeaconKeyOutput,
    GetBranchKeyVersionInput_GetBranchKeyVersionInput as DafnyGetBranchKeyVersionInput,
    GetBranchKeyVersionOutput_GetBranchKeyVersionOutput as DafnyGetBranchKeyVersionOutput,
    GetEncryptedActiveBranchKeyInput_GetEncryptedActiveBranchKeyInput as DafnyGetEncryptedActiveBranchKeyInput,
    GetEncryptedActiveBranchKeyOutput_GetEncryptedActiveBranchKeyOutput as DafnyGetEncryptedActiveBranchKeyOutput,
    GetEncryptedBeaconKeyInput_GetEncryptedBeaconKeyInput as DafnyGetEncryptedBeaconKeyInput,
    GetEncryptedBeaconKeyOutput_GetEncryptedBeaconKeyOutput as DafnyGetEncryptedBeaconKeyOutput,
    GetEncryptedBranchKeyVersionInput_GetEncryptedBranchKeyVersionInput as DafnyGetEncryptedBranchKeyVersionInput,
    GetEncryptedBranchKeyVersionOutput_GetEncryptedBranchKeyVersionOutput as DafnyGetEncryptedBranchKeyVersionOutput,
    GetItemsForInitializeMutationInput_GetItemsForInitializeMutationInput as DafnyGetItemsForInitializeMutationInput,
    GetItemsForInitializeMutationOutput_GetItemsForInitializeMutationOutput as DafnyGetItemsForInitializeMutationOutput,
    GetKeyStorageInfoInput_GetKeyStorageInfoInput as DafnyGetKeyStorageInfoInput,
    GetKeyStorageInfoOutput_GetKeyStorageInfoOutput as DafnyGetKeyStorageInfoOutput,
    GetKeyStoreInfoOutput_GetKeyStoreInfoOutput as DafnyGetKeyStoreInfoOutput,
    GetMutationInput_GetMutationInput as DafnyGetMutationInput,
    GetMutationOutput_GetMutationOutput as DafnyGetMutationOutput,
    HierarchicalKeyType_ActiveHierarchicalSymmetricBeacon,
    HierarchicalKeyType_ActiveHierarchicalSymmetricVersion,
    HierarchicalKeyType_HierarchicalSymmetricVersion,
    HierarchicalSymmetric_HierarchicalSymmetric as DafnyHierarchicalSymmetric,
    KMSConfiguration_discovery,
    KMSConfiguration_kmsKeyArn,
    KMSConfiguration_kmsMRKeyArn,
    KMSConfiguration_mrDiscovery,
    KeyManagement_kms,
    KeyStoreConfig_KeyStoreConfig as DafnyKeyStoreConfig,
    MRDiscovery_MRDiscovery as DafnyMRDiscovery,
    MutationCommitment_MutationCommitment as DafnyMutationCommitment,
    MutationIndex_MutationIndex as DafnyMutationIndex,
    OverWriteEncryptedHierarchicalKey_OverWriteEncryptedHierarchicalKey as DafnyOverWriteEncryptedHierarchicalKey,
    OverWriteMutationIndex_OverWriteMutationIndex as DafnyOverWriteMutationIndex,
    QueryForVersionsInput_QueryForVersionsInput as DafnyQueryForVersionsInput,
    QueryForVersionsOutput_QueryForVersionsOutput as DafnyQueryForVersionsOutput,
    Storage_custom,
    Storage_ddb,
    VersionKeyInput_VersionKeyInput as DafnyVersionKeyInput,
    VersionKeyOutput_VersionKeyOutput as DafnyVersionKeyOutput,
    WriteAtomicMutationInput_WriteAtomicMutationInput as DafnyWriteAtomicMutationInput,
    WriteAtomicMutationOutput_WriteAtomicMutationOutput as DafnyWriteAtomicMutationOutput,
    WriteInitializeMutationInput_WriteInitializeMutationInput as DafnyWriteInitializeMutationInput,
    WriteInitializeMutationOutput_WriteInitializeMutationOutput as DafnyWriteInitializeMutationOutput,
    WriteInitializeMutationVersion_mutate,
    WriteInitializeMutationVersion_rotate,
    WriteMutatedVersionsInput_WriteMutatedVersionsInput as DafnyWriteMutatedVersionsInput,
    WriteMutatedVersionsOutput_WriteMutatedVersionsOutput as DafnyWriteMutatedVersionsOutput,
    WriteMutationIndexInput_WriteMutationIndexInput as DafnyWriteMutationIndexInput,
    WriteMutationIndexOutput_WriteMutationIndexOutput as DafnyWriteMutationIndexOutput,
    WriteNewEncryptedBranchKeyInput_WriteNewEncryptedBranchKeyInput as DafnyWriteNewEncryptedBranchKeyInput,
    WriteNewEncryptedBranchKeyOutput_WriteNewEncryptedBranchKeyOutput as DafnyWriteNewEncryptedBranchKeyOutput,
    WriteNewEncryptedBranchKeyVersionInput_WriteNewEncryptedBranchKeyVersionInput as DafnyWriteNewEncryptedBranchKeyVersionInput,
    WriteNewEncryptedBranchKeyVersionOutput_WriteNewEncryptedBranchKeyVersionOutput as DafnyWriteNewEncryptedBranchKeyVersionOutput,
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


def aws_cryptography_keystore_WriteNewEncryptedBranchKeyInput(native_input):
    return DafnyWriteNewEncryptedBranchKeyInput(
        Active=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_EncryptedHierarchicalKey(
            native_input.active
        ),
        Version=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_EncryptedHierarchicalKey(
            native_input.version
        ),
        Beacon=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_EncryptedHierarchicalKey(
            native_input.beacon
        ),
    )


def aws_cryptography_keystore_EncryptedHierarchicalKey(native_input):
    return DafnyEncryptedHierarchicalKey(
        Identifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.identifier.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Type=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_HierarchicalKeyType(
            native_input.type
        ),
        CreateTime=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.create_time.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        KmsArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.kms_arn.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        EncryptionContext=Map(
            {
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(*[iter(key.encode("utf-16-be"))] * 2)
                        ]
                    )
                ): Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(*[iter(value.encode("utf-16-be"))] * 2)
                        ]
                    )
                )
                for (key, value) in native_input.encryption_context.items()
            }
        ),
        CiphertextBlob=Seq(native_input.ciphertext_blob),
    )


def aws_cryptography_keystore_HierarchicalKeyType(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.HierarchicalKeyTypeActiveHierarchicalSymmetricVersion,
    ):
        HierarchicalKeyType_union_value = HierarchicalKeyType_ActiveHierarchicalSymmetricVersion(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_ActiveHierarchicalSymmetric(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.HierarchicalKeyTypeHierarchicalSymmetricVersion,
    ):
        HierarchicalKeyType_union_value = HierarchicalKeyType_HierarchicalSymmetricVersion(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_HierarchicalSymmetric(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.HierarchicalKeyTypeActiveHierarchicalSymmetricBeacon,
    ):
        HierarchicalKeyType_union_value = HierarchicalKeyType_ActiveHierarchicalSymmetricBeacon(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_ActiveHierarchicalSymmetricBeacon(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return HierarchicalKeyType_union_value


def aws_cryptography_keystore_ActiveHierarchicalSymmetric(native_input):
    return DafnyActiveHierarchicalSymmetric(
        Version=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.version.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_keystore_HierarchicalSymmetric(native_input):
    return DafnyHierarchicalSymmetric(
        Version=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.version.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_keystore_ActiveHierarchicalSymmetricBeacon(native_input):
    return DafnyActiveHierarchicalSymmetricBeacon()


def aws_cryptography_keystore_WriteNewEncryptedBranchKeyOutput(native_input):
    return DafnyWriteNewEncryptedBranchKeyOutput()


def aws_cryptography_keystore_WriteNewEncryptedBranchKeyVersionInput(native_input):
    return DafnyWriteNewEncryptedBranchKeyVersionInput(
        Active=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
            native_input.active
        ),
        Version=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_EncryptedHierarchicalKey(
            native_input.version
        ),
    )


def aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(native_input):
    return DafnyOverWriteEncryptedHierarchicalKey(
        Item=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_EncryptedHierarchicalKey(
            native_input.item
        ),
        Old=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_EncryptedHierarchicalKey(
            native_input.old
        ),
    )


def aws_cryptography_keystore_WriteNewEncryptedBranchKeyVersionOutput(native_input):
    return DafnyWriteNewEncryptedBranchKeyVersionOutput()


def aws_cryptography_keystore_GetEncryptedActiveBranchKeyInput(native_input):
    return DafnyGetEncryptedActiveBranchKeyInput(
        Identifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.identifier.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_keystore_GetEncryptedActiveBranchKeyOutput(native_input):
    return DafnyGetEncryptedActiveBranchKeyOutput(
        Item=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_EncryptedHierarchicalKey(
            native_input.item
        ),
    )


def aws_cryptography_keystore_GetEncryptedBranchKeyVersionInput(native_input):
    return DafnyGetEncryptedBranchKeyVersionInput(
        Identifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.identifier.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Version=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.version.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_keystore_GetEncryptedBranchKeyVersionOutput(native_input):
    return DafnyGetEncryptedBranchKeyVersionOutput(
        Item=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_EncryptedHierarchicalKey(
            native_input.item
        ),
    )


def aws_cryptography_keystore_GetEncryptedBeaconKeyInput(native_input):
    return DafnyGetEncryptedBeaconKeyInput(
        Identifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.identifier.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_keystore_GetEncryptedBeaconKeyOutput(native_input):
    return DafnyGetEncryptedBeaconKeyOutput(
        Item=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_EncryptedHierarchicalKey(
            native_input.item
        ),
    )


def aws_cryptography_keystore_GetKeyStorageInfoInput(native_input):
    return DafnyGetKeyStorageInfoInput()


def aws_cryptography_keystore_GetKeyStorageInfoOutput(native_input):
    return DafnyGetKeyStorageInfoOutput(
        Name=Seq(native_input.name.encode("utf-8")),
        LogicalName=Seq(native_input.logical_name.encode("utf-8")),
    )


def aws_cryptography_keystore_GetItemsForInitializeMutationInput(native_input):
    return DafnyGetItemsForInitializeMutationInput(
        Identifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.identifier.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_keystore_GetItemsForInitializeMutationOutput(native_input):
    return DafnyGetItemsForInitializeMutationOutput(
        ActiveItem=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_EncryptedHierarchicalKey(
            native_input.active_item
        ),
        BeaconItem=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_EncryptedHierarchicalKey(
            native_input.beacon_item
        ),
        MutationCommitment=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_MutationCommitment(
                        native_input.mutation_commitment
                    )
                )
            )
            if (native_input.mutation_commitment is not None)
            else (Option_None())
        ),
        MutationIndex=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_MutationIndex(
                        native_input.mutation_index
                    )
                )
            )
            if (native_input.mutation_index is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_keystore_MutationCommitment(native_input):
    return DafnyMutationCommitment(
        Identifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.identifier.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        CreateTime=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.create_time.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        UUID=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(*[iter(native_input.uuid.encode("utf-16-be"))] * 2)
                ]
            )
        ),
        Original=Seq(native_input.original),
        Terminal=Seq(native_input.terminal),
        Input=Seq(native_input.input),
        CiphertextBlob=Seq(native_input.ciphertext_blob),
    )


def aws_cryptography_keystore_MutationIndex(native_input):
    return DafnyMutationIndex(
        Identifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.identifier.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        CreateTime=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.create_time.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        UUID=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(*[iter(native_input.uuid.encode("utf-16-be"))] * 2)
                ]
            )
        ),
        PageIndex=Seq(native_input.page_index),
        LastModifiedTime=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.last_modified_time.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        CiphertextBlob=Seq(native_input.ciphertext_blob),
    )


def aws_cryptography_keystore_WriteInitializeMutationInput(native_input):
    return DafnyWriteInitializeMutationInput(
        Active=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
            native_input.active
        ),
        Version=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_WriteInitializeMutationVersion(
            native_input.version
        ),
        Beacon=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
            native_input.beacon
        ),
        MutationCommitment=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_MutationCommitment(
            native_input.mutation_commitment
        ),
        MutationIndex=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_MutationIndex(
            native_input.mutation_index
        ),
    )


def aws_cryptography_keystore_WriteInitializeMutationVersion(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteInitializeMutationVersionRotate,
    ):
        WriteInitializeMutationVersion_union_value = WriteInitializeMutationVersion_rotate(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_EncryptedHierarchicalKey(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteInitializeMutationVersionMutate,
    ):
        WriteInitializeMutationVersion_union_value = WriteInitializeMutationVersion_mutate(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return WriteInitializeMutationVersion_union_value


def aws_cryptography_keystore_WriteInitializeMutationOutput(native_input):
    return DafnyWriteInitializeMutationOutput()


def aws_cryptography_keystore_WriteAtomicMutationInput(native_input):
    return DafnyWriteAtomicMutationInput(
        Active=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
            native_input.active
        ),
        Version=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_WriteInitializeMutationVersion(
            native_input.version
        ),
        Beacon=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
            native_input.beacon
        ),
        Items=Seq(
            [
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
                    list_element
                )
                for list_element in native_input.items
            ]
        ),
    )


def aws_cryptography_keystore_WriteAtomicMutationOutput(native_input):
    return DafnyWriteAtomicMutationOutput()


def aws_cryptography_keystore_QueryForVersionsInput(native_input):
    return DafnyQueryForVersionsInput(
        ExclusiveStartKey=(
            (Option_Some(Seq(native_input.exclusive_start_key)))
            if (native_input.exclusive_start_key is not None)
            else (Option_None())
        ),
        Identifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.identifier.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        PageSize=native_input.page_size,
    )


def aws_cryptography_keystore_QueryForVersionsOutput(native_input):
    return DafnyQueryForVersionsOutput(
        ExclusiveStartKey=Seq(native_input.exclusive_start_key),
        Items=Seq(
            [
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_EncryptedHierarchicalKey(
                    list_element
                )
                for list_element in native_input.items
            ]
        ),
    )


def aws_cryptography_keystore_WriteMutatedVersionsInput(native_input):
    return DafnyWriteMutatedVersionsInput(
        Items=Seq(
            [
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
                    list_element
                )
                for list_element in native_input.items
            ]
        ),
        MutationCommitment=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_MutationCommitment(
            native_input.mutation_commitment
        ),
        MutationIndex=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_OverWriteMutationIndex(
            native_input.mutation_index
        ),
        EndMutation=native_input.end_mutation,
    )


def aws_cryptography_keystore_OverWriteMutationIndex(native_input):
    return DafnyOverWriteMutationIndex(
        Index=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_MutationIndex(
            native_input.index
        ),
        Old=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_MutationIndex(
            native_input.old
        ),
    )


def aws_cryptography_keystore_WriteMutatedVersionsOutput(native_input):
    return DafnyWriteMutatedVersionsOutput()


def aws_cryptography_keystore_GetMutationInput(native_input):
    return DafnyGetMutationInput(
        Identifier=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.identifier.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_keystore_GetMutationOutput(native_input):
    return DafnyGetMutationOutput(
        MutationCommitment=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_MutationCommitment(
                        native_input.mutation_commitment
                    )
                )
            )
            if (native_input.mutation_commitment is not None)
            else (Option_None())
        ),
        MutationIndex=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_MutationIndex(
                        native_input.mutation_index
                    )
                )
            )
            if (native_input.mutation_index is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_keystore_DeleteMutationInput(native_input):
    return DafnyDeleteMutationInput(
        MutationCommitment=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_MutationCommitment(
            native_input.mutation_commitment
        ),
    )


def aws_cryptography_keystore_DeleteMutationOutput(native_input):
    return DafnyDeleteMutationOutput()


def aws_cryptography_keystore_WriteMutationIndexInput(native_input):
    return DafnyWriteMutationIndexInput(
        MutationCommitment=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_MutationCommitment(
            native_input.mutation_commitment
        ),
        MutationIndex=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_MutationIndex(
            native_input.mutation_index
        ),
    )


def aws_cryptography_keystore_WriteMutationIndexOutput(native_input):
    return DafnyWriteMutationIndexOutput()


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
    )


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
    )


def aws_cryptography_keystore_KmsClientReference(native_input):
    import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms

    client = aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms.default__.KMSClient(
        boto_client=native_input
    )
    client.value.impl = native_input
    return client.value


def aws_cryptography_keystore_AwsKms(native_input):
    return DafnyAwsKms(
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


def aws_cryptography_keystore_DdbClientReference(native_input):
    import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb

    client = aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb.default__.DynamoDBClient(
        boto_client=native_input
    )
    client.value.impl = native_input
    return client.value


def aws_cryptography_keystore_DynamoDBTable(native_input):
    return DafnyDynamoDBTable(
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
    )


def aws_cryptography_keystore_KeyManagement(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.KeyManagementKms,
    ):
        KeyManagement_union_value = KeyManagement_kms(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_AwsKms(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return KeyManagement_union_value


def aws_cryptography_keystore_KeyStorageInterfaceReference(native_input):
    if hasattr(native_input, "_impl"):
        return native_input._impl

    else:
        return native_input


def aws_cryptography_keystore_Storage(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.StorageDdb,
    ):
        Storage_union_value = Storage_ddb(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_DynamoDBTable(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.StorageCustom,
    ):
        Storage_union_value = Storage_custom(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_KeyStorageInterfaceReference(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return Storage_union_value


def aws_cryptography_keystore_KeyStoreConfig(native_input):
    return DafnyKeyStoreConfig(
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
        keyManagement=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_KeyManagement(
                        native_input.key_management
                    )
                )
            )
            if (native_input.key_management is not None)
            else (Option_None())
        ),
        ddbTableName=(
            (
                Option_Some(
                    Seq(
                        "".join(
                            [
                                chr(int.from_bytes(pair, "big"))
                                for pair in zip(
                                    *[
                                        iter(
                                            native_input.ddb_table_name.encode(
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
            if (native_input.ddb_table_name is not None)
            else (Option_None())
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
        storage=(
            (
                Option_Some(
                    aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_Storage(
                        native_input.storage
                    )
                )
            )
            if (native_input.storage is not None)
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
