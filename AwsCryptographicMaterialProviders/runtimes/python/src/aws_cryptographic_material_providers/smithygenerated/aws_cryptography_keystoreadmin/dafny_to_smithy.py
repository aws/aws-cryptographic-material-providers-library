# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes import (
    ApplyMutationResult_CompleteMutation,
    ApplyMutationResult_ContinueMutation,
    KMSIdentifier_KmsKeyArn,
    KMSIdentifier_KmsMRKeyArn,
    KeyManagementStrategy_AwsKmsReEncrypt,
)
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models


def aws_cryptography_keystoreadmin_KMSIdentifier(dafny_input):
    # Convert KMSIdentifier
    if isinstance(dafny_input, KMSIdentifier_KmsKeyArn):
        KMSIdentifier_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.KMSIdentifierKmsKeyArn(
            b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.KmsKeyArn).decode(
                "utf-16-be"
            )
        )
    elif isinstance(dafny_input, KMSIdentifier_KmsMRKeyArn):
        KMSIdentifier_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.KMSIdentifierKmsMRKeyArn(
            b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.KmsMRKeyArn).decode(
                "utf-16-be"
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return KMSIdentifier_union_value


def aws_cryptography_keystoreadmin_KeyManagementStrategy(dafny_input):
    # Convert KeyManagementStrategy
    if isinstance(dafny_input, KeyManagementStrategy_AwsKmsReEncrypt):
        KeyManagementStrategy_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.KeyManagementStrategyAwsKmsReEncrypt(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_AwsKms(
                dafny_input.AwsKmsReEncrypt
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return KeyManagementStrategy_union_value


def aws_cryptography_keystoreadmin_CreateKeyInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.CreateKeyInput(
        identifier=(
            (
                b"".join(
                    ord(c).to_bytes(2, "big") for c in dafny_input.Identifier.value
                ).decode("utf-16-be")
            )
            if (dafny_input.Identifier.is_Some)
            else None
        ),
        encryption_context=(
            (
                {
                    bytes(key.Elements)
                    .decode("utf-8"): bytes(value.Elements)
                    .decode("utf-8")
                    for (key, value) in dafny_input.EncryptionContext.value.items
                }
            )
            if (dafny_input.EncryptionContext.is_Some)
            else None
        ),
        kms_arn=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_KMSIdentifier(
            dafny_input.KmsArn
        ),
        strategy=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_KeyManagementStrategy(
                    dafny_input.Strategy.value
                )
            )
            if (dafny_input.Strategy.is_Some)
            else None
        ),
    )


def aws_cryptography_keystoreadmin_VersionKeyInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.VersionKeyInput(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
        kms_arn=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_KMSIdentifier(
            dafny_input.KmsArn
        ),
        strategy=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_KeyManagementStrategy(
                    dafny_input.Strategy.value
                )
            )
            if (dafny_input.Strategy.is_Some)
            else None
        ),
    )


def aws_cryptography_keystoreadmin_Mutations(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.Mutations(
        terminal_kms_arn=(
            (
                b"".join(
                    ord(c).to_bytes(2, "big") for c in dafny_input.TerminalKmsArn.value
                ).decode("utf-16-be")
            )
            if (dafny_input.TerminalKmsArn.is_Some)
            else None
        ),
        terminal_encryption_context=(
            (
                {
                    b"".join(ord(c).to_bytes(2, "big") for c in key)
                    .decode("utf-16-be"): b"".join(
                        ord(c).to_bytes(2, "big") for c in value
                    )
                    .decode("utf-16-be")
                    for (
                        key,
                        value,
                    ) in dafny_input.TerminalEncryptionContext.value.items
                }
            )
            if (dafny_input.TerminalEncryptionContext.is_Some)
            else None
        ),
    )


def aws_cryptography_keystoreadmin_InitializeMutationInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.InitializeMutationInput(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
        mutations=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_Mutations(
            dafny_input.Mutations
        ),
        strategy=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_KeyManagementStrategy(
                    dafny_input.Strategy.value
                )
            )
            if (dafny_input.Strategy.is_Some)
            else None
        ),
    )


def aws_cryptography_keystoreadmin_MutationToken(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.MutationToken(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
        original=bytes(dafny_input.Original),
        terminal=bytes(dafny_input.Terminal),
        exclusive_start_key=(
            (bytes(dafny_input.ExclusiveStartKey.value))
            if (dafny_input.ExclusiveStartKey.is_Some)
            else None
        ),
        uuid=(
            (
                b"".join(
                    ord(c).to_bytes(2, "big") for c in dafny_input.UUID.value
                ).decode("utf-16-be")
            )
            if (dafny_input.UUID.is_Some)
            else None
        ),
        create_time=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.CreateTime
        ).decode("utf-16-be"),
    )


def aws_cryptography_keystoreadmin_ApplyMutationInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.ApplyMutationInput(
        mutation_token=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_MutationToken(
            dafny_input.MutationToken
        ),
        page_size=(
            (dafny_input.PageSize.value) if (dafny_input.PageSize.is_Some) else None
        ),
        strategy=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_KeyManagementStrategy(
                    dafny_input.Strategy.value
                )
            )
            if (dafny_input.Strategy.is_Some)
            else None
        ),
    )


def aws_cryptography_keystoreadmin_CreateKeyOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.CreateKeyOutput(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
    )


def aws_cryptography_keystoreadmin_VersionKeyOutput(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.VersionKeyOutput()
    )


def aws_cryptography_keystoreadmin_MutatedBranchKeyItem(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.MutatedBranchKeyItem(
        item_type=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ItemType
        ).decode("utf-16-be"),
        description=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Description
        ).decode("utf-16-be"),
    )


def aws_cryptography_keystoreadmin_InitializeMutationOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.InitializeMutationOutput(
        mutation_token=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_MutationToken(
            dafny_input.MutationToken
        ),
        mutated_branch_key_items=[
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_MutatedBranchKeyItem(
                list_element
            )
            for list_element in dafny_input.MutatedBranchKeyItems
        ],
    )


def aws_cryptography_keystoreadmin_ApplyMutationResult(dafny_input):
    # Convert ApplyMutationResult
    if isinstance(dafny_input, ApplyMutationResult_ContinueMutation):
        ApplyMutationResult_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.ApplyMutationResultContinueMutation(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_MutationToken(
                dafny_input.ContinueMutation
            )
        )
    elif isinstance(dafny_input, ApplyMutationResult_CompleteMutation):
        ApplyMutationResult_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.ApplyMutationResultCompleteMutation(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_MutationComplete(
                dafny_input.CompleteMutation
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return ApplyMutationResult_union_value


def aws_cryptography_keystoreadmin_MutationComplete(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.MutationComplete()
    )


def aws_cryptography_keystoreadmin_ApplyMutationOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.ApplyMutationOutput(
        mutation_result=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_ApplyMutationResult(
            dafny_input.MutationResult
        ),
        mutated_branch_key_items=[
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_MutatedBranchKeyItem(
                list_element
            )
            for list_element in dafny_input.MutatedBranchKeyItems
        ],
    )


def aws_cryptography_keystoreadmin_KeyStoreAdminConfig(dafny_input):
    # Deferred import of .config to avoid circular dependency
    import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.config

    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.config.KeyStoreAdminConfig(
        logical_key_store_name=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.logicalKeyStoreName
        ).decode("utf-16-be"),
        storage=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_Storage(
            dafny_input.storage
        ),
    )
