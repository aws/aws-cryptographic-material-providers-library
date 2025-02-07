# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes import (
    HierarchicalKeyType_ActiveHierarchicalSymmetricBeacon,
    HierarchicalKeyType_ActiveHierarchicalSymmetricVersion,
    HierarchicalKeyType_HierarchicalSymmetricVersion,
    KMSConfiguration_discovery,
    KMSConfiguration_kmsKeyArn,
    KMSConfiguration_kmsMRKeyArn,
    KMSConfiguration_mrDiscovery,
    KeyManagement_kms,
    Storage_custom,
    Storage_ddb,
    WriteInitializeMutationVersion_mutate,
    WriteInitializeMutationVersion_rotate,
)
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models


def aws_cryptography_keystore_EncryptedHierarchicalKey(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.EncryptedHierarchicalKey(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
        type=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_HierarchicalKeyType(
            dafny_input.Type
        ),
        create_time=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.CreateTime
        ).decode("utf-16-be"),
        kms_arn=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.KmsArn).decode(
            "utf-16-be"
        ),
        encryption_context={
            b"".join(ord(c).to_bytes(2, "big") for c in key)
            .decode("utf-16-be"): b"".join(ord(c).to_bytes(2, "big") for c in value)
            .decode("utf-16-be")
            for (key, value) in dafny_input.EncryptionContext.items
        },
        ciphertext_blob=bytes(dafny_input.CiphertextBlob),
    )


def aws_cryptography_keystore_HierarchicalKeyType(dafny_input):
    # Convert HierarchicalKeyType
    if isinstance(dafny_input, HierarchicalKeyType_ActiveHierarchicalSymmetricVersion):
        HierarchicalKeyType_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.HierarchicalKeyTypeActiveHierarchicalSymmetricVersion(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_ActiveHierarchicalSymmetric(
                dafny_input.ActiveHierarchicalSymmetricVersion
            )
        )
    elif isinstance(dafny_input, HierarchicalKeyType_HierarchicalSymmetricVersion):
        HierarchicalKeyType_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.HierarchicalKeyTypeHierarchicalSymmetricVersion(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_HierarchicalSymmetric(
                dafny_input.HierarchicalSymmetricVersion
            )
        )
    elif isinstance(dafny_input, HierarchicalKeyType_ActiveHierarchicalSymmetricBeacon):
        HierarchicalKeyType_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.HierarchicalKeyTypeActiveHierarchicalSymmetricBeacon(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_ActiveHierarchicalSymmetricBeacon(
                dafny_input.ActiveHierarchicalSymmetricBeacon
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return HierarchicalKeyType_union_value


def aws_cryptography_keystore_ActiveHierarchicalSymmetric(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.ActiveHierarchicalSymmetric(
        version=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.Version).decode(
            "utf-16-be"
        ),
    )


def aws_cryptography_keystore_HierarchicalSymmetric(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.HierarchicalSymmetric(
        version=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.Version).decode(
            "utf-16-be"
        ),
    )


def aws_cryptography_keystore_ActiveHierarchicalSymmetricBeacon(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.ActiveHierarchicalSymmetricBeacon()
    )


def aws_cryptography_keystore_WriteNewEncryptedBranchKeyInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteNewEncryptedBranchKeyInput(
        active=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_EncryptedHierarchicalKey(
            dafny_input.Active
        ),
        version=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_EncryptedHierarchicalKey(
            dafny_input.Version
        ),
        beacon=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_EncryptedHierarchicalKey(
            dafny_input.Beacon
        ),
    )


def aws_cryptography_keystore_WriteNewEncryptedBranchKeyOutput(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteNewEncryptedBranchKeyOutput()
    )


def aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.OverWriteEncryptedHierarchicalKey(
        item=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_EncryptedHierarchicalKey(
            dafny_input.Item
        ),
        old=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_EncryptedHierarchicalKey(
            dafny_input.Old
        ),
    )


def aws_cryptography_keystore_WriteNewEncryptedBranchKeyVersionInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteNewEncryptedBranchKeyVersionInput(
        active=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
            dafny_input.Active
        ),
        version=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_EncryptedHierarchicalKey(
            dafny_input.Version
        ),
    )


def aws_cryptography_keystore_WriteNewEncryptedBranchKeyVersionOutput(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteNewEncryptedBranchKeyVersionOutput()
    )


def aws_cryptography_keystore_GetEncryptedActiveBranchKeyInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedActiveBranchKeyInput(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
    )


def aws_cryptography_keystore_GetEncryptedActiveBranchKeyOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedActiveBranchKeyOutput(
        item=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_EncryptedHierarchicalKey(
            dafny_input.Item
        ),
    )


def aws_cryptography_keystore_GetEncryptedBranchKeyVersionInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedBranchKeyVersionInput(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
        version=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.Version).decode(
            "utf-16-be"
        ),
    )


def aws_cryptography_keystore_GetEncryptedBranchKeyVersionOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedBranchKeyVersionOutput(
        item=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_EncryptedHierarchicalKey(
            dafny_input.Item
        ),
    )


def aws_cryptography_keystore_GetEncryptedBeaconKeyInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedBeaconKeyInput(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
    )


def aws_cryptography_keystore_GetEncryptedBeaconKeyOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedBeaconKeyOutput(
        item=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_EncryptedHierarchicalKey(
            dafny_input.Item
        ),
    )


def aws_cryptography_keystore_GetKeyStorageInfoInput(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetKeyStorageInfoInput()
    )


def aws_cryptography_keystore_GetKeyStorageInfoOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetKeyStorageInfoOutput(
        name=bytes(dafny_input.Name.Elements).decode("utf-8"),
        logical_name=bytes(dafny_input.LogicalName.Elements).decode("utf-8"),
    )


def aws_cryptography_keystore_GetItemsForInitializeMutationInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetItemsForInitializeMutationInput(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
    )


def aws_cryptography_keystore_MutationCommitment(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.MutationCommitment(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
        create_time=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.CreateTime
        ).decode("utf-16-be"),
        uuid=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.UUID).decode(
            "utf-16-be"
        ),
        original=bytes(dafny_input.Original),
        terminal=bytes(dafny_input.Terminal),
        input=bytes(dafny_input.Input),
        ciphertext_blob=bytes(dafny_input.CiphertextBlob),
    )


def aws_cryptography_keystore_MutationIndex(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.MutationIndex(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
        create_time=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.CreateTime
        ).decode("utf-16-be"),
        uuid=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.UUID).decode(
            "utf-16-be"
        ),
        page_index=bytes(dafny_input.PageIndex),
        last_modified_time=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.LastModifiedTime
        ).decode("utf-16-be"),
        ciphertext_blob=bytes(dafny_input.CiphertextBlob),
    )


def aws_cryptography_keystore_GetItemsForInitializeMutationOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetItemsForInitializeMutationOutput(
        active_item=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_EncryptedHierarchicalKey(
            dafny_input.ActiveItem
        ),
        beacon_item=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_EncryptedHierarchicalKey(
            dafny_input.BeaconItem
        ),
        mutation_commitment=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_MutationCommitment(
                    dafny_input.MutationCommitment.value
                )
            )
            if (dafny_input.MutationCommitment.is_Some)
            else None
        ),
        mutation_index=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_MutationIndex(
                    dafny_input.MutationIndex.value
                )
            )
            if (dafny_input.MutationIndex.is_Some)
            else None
        ),
    )


def aws_cryptography_keystore_WriteInitializeMutationVersion(dafny_input):
    # Convert WriteInitializeMutationVersion
    if isinstance(dafny_input, WriteInitializeMutationVersion_rotate):
        WriteInitializeMutationVersion_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteInitializeMutationVersionRotate(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_EncryptedHierarchicalKey(
                dafny_input.rotate
            )
        )
    elif isinstance(dafny_input, WriteInitializeMutationVersion_mutate):
        WriteInitializeMutationVersion_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteInitializeMutationVersionMutate(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
                dafny_input.mutate
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return WriteInitializeMutationVersion_union_value


def aws_cryptography_keystore_WriteInitializeMutationInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteInitializeMutationInput(
        active=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
            dafny_input.Active
        ),
        version=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_WriteInitializeMutationVersion(
            dafny_input.Version
        ),
        beacon=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
            dafny_input.Beacon
        ),
        mutation_commitment=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_MutationCommitment(
            dafny_input.MutationCommitment
        ),
        mutation_index=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_MutationIndex(
            dafny_input.MutationIndex
        ),
    )


def aws_cryptography_keystore_WriteInitializeMutationOutput(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteInitializeMutationOutput()
    )


def aws_cryptography_keystore_WriteAtomicMutationInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteAtomicMutationInput(
        active=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
            dafny_input.Active
        ),
        version=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_WriteInitializeMutationVersion(
            dafny_input.Version
        ),
        beacon=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
            dafny_input.Beacon
        ),
        items=[
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
                list_element
            )
            for list_element in dafny_input.Items
        ],
    )


def aws_cryptography_keystore_WriteAtomicMutationOutput(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteAtomicMutationOutput()
    )


def aws_cryptography_keystore_QueryForVersionsInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.QueryForVersionsInput(
        exclusive_start_key=(
            (bytes(dafny_input.ExclusiveStartKey.value))
            if (dafny_input.ExclusiveStartKey.is_Some)
            else None
        ),
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
        page_size=dafny_input.PageSize,
    )


def aws_cryptography_keystore_QueryForVersionsOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.QueryForVersionsOutput(
        exclusive_start_key=bytes(dafny_input.ExclusiveStartKey),
        items=[
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_EncryptedHierarchicalKey(
                list_element
            )
            for list_element in dafny_input.Items
        ],
    )


def aws_cryptography_keystore_OverWriteMutationIndex(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.OverWriteMutationIndex(
        index=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_MutationIndex(
            dafny_input.Index
        ),
        old=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_MutationIndex(
            dafny_input.Old
        ),
    )


def aws_cryptography_keystore_WriteMutatedVersionsInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteMutatedVersionsInput(
        items=[
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_OverWriteEncryptedHierarchicalKey(
                list_element
            )
            for list_element in dafny_input.Items
        ],
        mutation_commitment=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_MutationCommitment(
            dafny_input.MutationCommitment
        ),
        mutation_index=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_OverWriteMutationIndex(
            dafny_input.MutationIndex
        ),
        end_mutation=dafny_input.EndMutation,
    )


def aws_cryptography_keystore_WriteMutatedVersionsOutput(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteMutatedVersionsOutput()
    )


def aws_cryptography_keystore_GetMutationInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetMutationInput(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
    )


def aws_cryptography_keystore_GetMutationOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetMutationOutput(
        mutation_commitment=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_MutationCommitment(
                    dafny_input.MutationCommitment.value
                )
            )
            if (dafny_input.MutationCommitment.is_Some)
            else None
        ),
        mutation_index=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_MutationIndex(
                    dafny_input.MutationIndex.value
                )
            )
            if (dafny_input.MutationIndex.is_Some)
            else None
        ),
    )


def aws_cryptography_keystore_DeleteMutationInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.DeleteMutationInput(
        mutation_commitment=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_MutationCommitment(
            dafny_input.MutationCommitment
        ),
    )


def aws_cryptography_keystore_DeleteMutationOutput(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.DeleteMutationOutput()
    )


def aws_cryptography_keystore_WriteMutationIndexInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteMutationIndexInput(
        mutation_commitment=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_MutationCommitment(
            dafny_input.MutationCommitment
        ),
        mutation_index=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_MutationIndex(
            dafny_input.MutationIndex
        ),
    )


def aws_cryptography_keystore_WriteMutationIndexOutput(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteMutationIndexOutput()
    )


def smithy_api_Unit():
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.Unit()
    )


def aws_cryptography_keystore_CreateKeyStoreInput(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.CreateKeyStoreInput()
    )


def aws_cryptography_keystore_CreateKeyInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.CreateKeyInput(
        branch_key_identifier=(
            (
                b"".join(
                    ord(c).to_bytes(2, "big")
                    for c in dafny_input.branchKeyIdentifier.value
                ).decode("utf-16-be")
            )
            if (dafny_input.branchKeyIdentifier.is_Some)
            else None
        ),
        encryption_context=(
            (
                {
                    bytes(key.Elements)
                    .decode("utf-8"): bytes(value.Elements)
                    .decode("utf-8")
                    for (key, value) in dafny_input.encryptionContext.value.items
                }
            )
            if (dafny_input.encryptionContext.is_Some)
            else None
        ),
    )


def aws_cryptography_keystore_VersionKeyInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.VersionKeyInput(
        branch_key_identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.branchKeyIdentifier
        ).decode("utf-16-be"),
    )


def aws_cryptography_keystore_GetActiveBranchKeyInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetActiveBranchKeyInput(
        branch_key_identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.branchKeyIdentifier
        ).decode("utf-16-be"),
    )


def aws_cryptography_keystore_GetBranchKeyVersionInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetBranchKeyVersionInput(
        branch_key_identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.branchKeyIdentifier
        ).decode("utf-16-be"),
        branch_key_version=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.branchKeyVersion
        ).decode("utf-16-be"),
    )


def aws_cryptography_keystore_GetBeaconKeyInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetBeaconKeyInput(
        branch_key_identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.branchKeyIdentifier
        ).decode("utf-16-be"),
    )


def aws_cryptography_keystore_KMSConfiguration(dafny_input):
    # Convert KMSConfiguration
    if isinstance(dafny_input, KMSConfiguration_kmsKeyArn):
        KMSConfiguration_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.KMSConfigurationKmsKeyArn(
            b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.kmsKeyArn).decode(
                "utf-16-be"
            )
        )
    elif isinstance(dafny_input, KMSConfiguration_kmsMRKeyArn):
        KMSConfiguration_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.KMSConfigurationKmsMRKeyArn(
            b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.kmsMRKeyArn).decode(
                "utf-16-be"
            )
        )
    elif isinstance(dafny_input, KMSConfiguration_discovery):
        KMSConfiguration_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.KMSConfigurationDiscovery(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_Discovery(
                dafny_input.discovery
            )
        )
    elif isinstance(dafny_input, KMSConfiguration_mrDiscovery):
        KMSConfiguration_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.KMSConfigurationMrDiscovery(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_MRDiscovery(
                dafny_input.mrDiscovery
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return KMSConfiguration_union_value


def aws_cryptography_keystore_Discovery(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.Discovery()
    )


def aws_cryptography_keystore_MRDiscovery(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.MRDiscovery(
        region=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.region).decode(
            "utf-16-be"
        ),
    )


def aws_cryptography_keystore_GetKeyStoreInfoOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetKeyStoreInfoOutput(
        key_store_id=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.keyStoreId
        ).decode("utf-16-be"),
        key_store_name=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.keyStoreName
        ).decode("utf-16-be"),
        logical_key_store_name=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.logicalKeyStoreName
        ).decode("utf-16-be"),
        grant_tokens=[
            b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                "utf-16-be"
            )
            for list_element in dafny_input.grantTokens
        ],
        kms_configuration=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_KMSConfiguration(
            dafny_input.kmsConfiguration
        ),
    )


def aws_cryptography_keystore_CreateKeyStoreOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.CreateKeyStoreOutput(
        table_arn=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.tableArn
        ).decode("utf-16-be"),
    )


def aws_cryptography_keystore_CreateKeyOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.CreateKeyOutput(
        branch_key_identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.branchKeyIdentifier
        ).decode("utf-16-be"),
    )


def aws_cryptography_keystore_VersionKeyOutput(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.VersionKeyOutput()
    )


def aws_cryptography_keystore_BranchKeyMaterials(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.BranchKeyMaterials(
        branch_key_identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.branchKeyIdentifier
        ).decode("utf-16-be"),
        branch_key_version=bytes(dafny_input.branchKeyVersion.Elements).decode("utf-8"),
        encryption_context={
            bytes(key.Elements).decode("utf-8"): bytes(value.Elements).decode("utf-8")
            for (key, value) in dafny_input.encryptionContext.items
        },
        branch_key=bytes(dafny_input.branchKey),
    )


def aws_cryptography_keystore_GetActiveBranchKeyOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetActiveBranchKeyOutput(
        branch_key_materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_BranchKeyMaterials(
            dafny_input.branchKeyMaterials
        ),
    )


def aws_cryptography_keystore_GetBranchKeyVersionOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetBranchKeyVersionOutput(
        branch_key_materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_BranchKeyMaterials(
            dafny_input.branchKeyMaterials
        ),
    )


def aws_cryptography_keystore_BeaconKeyMaterials(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.BeaconKeyMaterials(
        beacon_key_identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.beaconKeyIdentifier
        ).decode("utf-16-be"),
        encryption_context={
            bytes(key.Elements).decode("utf-8"): bytes(value.Elements).decode("utf-8")
            for (key, value) in dafny_input.encryptionContext.items
        },
        beacon_key=(
            (bytes(dafny_input.beaconKey.value))
            if (dafny_input.beaconKey.is_Some)
            else None
        ),
        hmac_keys=(
            (
                {
                    b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                        "utf-16-be"
                    ): bytes(value)
                    for (key, value) in dafny_input.hmacKeys.value.items
                }
            )
            if (dafny_input.hmacKeys.is_Some)
            else None
        ),
    )


def aws_cryptography_keystore_GetBeaconKeyOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetBeaconKeyOutput(
        beacon_key_materials=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_BeaconKeyMaterials(
            dafny_input.beaconKeyMaterials
        ),
    )


def aws_cryptography_keystore_KmsClientReference(dafny_input):
    return dafny_input._impl


def aws_cryptography_keystore_AwsKms(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.AwsKms(
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
        kms_client=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_KmsClientReference(
                    dafny_input.kmsClient.UnwrapOr(None)
                )
            )
            if (dafny_input.kmsClient.UnwrapOr(None) is not None)
            else None
        ),
    )


def aws_cryptography_keystore_DdbClientReference(dafny_input):
    return dafny_input._impl


def aws_cryptography_keystore_DynamoDBTable(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.DynamoDBTable(
        ddb_table_name=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ddbTableName
        ).decode("utf-16-be"),
        ddb_client=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_DdbClientReference(
                    dafny_input.ddbClient.UnwrapOr(None)
                )
            )
            if (dafny_input.ddbClient.UnwrapOr(None) is not None)
            else None
        ),
    )


def aws_cryptography_keystore_KeyManagement(dafny_input):
    # Convert KeyManagement
    if isinstance(dafny_input, KeyManagement_kms):
        KeyManagement_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.KeyManagementKms(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_AwsKms(
                dafny_input.kms
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return KeyManagement_union_value


def aws_cryptography_keystore_KeyStorageInterfaceReference(dafny_input):
    if hasattr(dafny_input, "_native_impl"):
        return dafny_input._native_impl

    else:
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.references import (
            KeyStorageInterface,
        )

        return KeyStorageInterface(_impl=dafny_input)


def aws_cryptography_keystore_Storage(dafny_input):
    # Convert Storage
    if isinstance(dafny_input, Storage_ddb):
        Storage_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.StorageDdb(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_DynamoDBTable(
                dafny_input.ddb
            )
        )
    elif isinstance(dafny_input, Storage_custom):
        Storage_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.StorageCustom(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_KeyStorageInterfaceReference(
                dafny_input.custom
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return Storage_union_value


def aws_cryptography_keystore_KeyStoreConfig(dafny_input):
    # Deferred import of .config to avoid circular dependency
    import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.config

    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.config.KeyStoreConfig(
        kms_configuration=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_KMSConfiguration(
            dafny_input.kmsConfiguration
        ),
        logical_key_store_name=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.logicalKeyStoreName
        ).decode("utf-16-be"),
        key_management=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_KeyManagement(
                    dafny_input.keyManagement.value
                )
            )
            if (dafny_input.keyManagement.is_Some)
            else None
        ),
        ddb_table_name=(
            (
                b"".join(
                    ord(c).to_bytes(2, "big") for c in dafny_input.ddbTableName.value
                ).decode("utf-16-be")
            )
            if (dafny_input.ddbTableName.is_Some)
            else None
        ),
        id=(
            (
                b"".join(
                    ord(c).to_bytes(2, "big") for c in dafny_input.id.value
                ).decode("utf-16-be")
            )
            if (dafny_input.id.is_Some)
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
        storage=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_Storage(
                    dafny_input.storage.value
                )
            )
            if (dafny_input.storage.is_Some)
            else None
        ),
        ddb_client=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_DdbClientReference(
                    dafny_input.ddbClient.UnwrapOr(None)
                )
            )
            if (dafny_input.ddbClient.UnwrapOr(None) is not None)
            else None
        ),
        kms_client=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_KmsClientReference(
                    dafny_input.kmsClient.UnwrapOr(None)
                )
            )
            if (dafny_input.kmsClient.UnwrapOr(None) is not None)
            else None
        ),
    )
