# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes import (
    ApplyMutationResult_CompleteMutation,
    ApplyMutationResult_ContinueMutation,
    InitializeMutationFlag_Created,
    InitializeMutationFlag_Resumed,
    InitializeMutationFlag_ResumedWithoutIndex,
    KeyManagementStrategy_AwsKmsDecryptEncrypt,
    KeyManagementStrategy_AwsKmsReEncrypt,
    KeyManagementStrategy_AwsKmsSimple,
    KmsSymmetricKeyArn_KmsKeyArn,
    KmsSymmetricKeyArn_KmsMRKeyArn,
    MutationInFlight_No,
    MutationInFlight_Yes,
    SystemKey_kmsSymmetricEncryption,
    SystemKey_trustStorage,
)
import aws_cryptographic_material_providers.internaldafny.generated.module_
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models


def aws_cryptography_keystoreadmin_KmsSymmetricKeyArn(dafny_input):
    # Convert KmsSymmetricKeyArn
    if isinstance(dafny_input, KmsSymmetricKeyArn_KmsKeyArn):
        KmsSymmetricKeyArn_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.KmsSymmetricKeyArnKmsKeyArn(
            b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.KmsKeyArn).decode(
                "utf-16-be"
            )
        )
    elif isinstance(dafny_input, KmsSymmetricKeyArn_KmsMRKeyArn):
        KmsSymmetricKeyArn_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.KmsSymmetricKeyArnKmsMRKeyArn(
            b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.KmsMRKeyArn).decode(
                "utf-16-be"
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return KmsSymmetricKeyArn_union_value


def aws_cryptography_keystoreadmin_KeyManagementStrategy(dafny_input):
    # Convert KeyManagementStrategy
    if isinstance(dafny_input, KeyManagementStrategy_AwsKmsReEncrypt):
        KeyManagementStrategy_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.KeyManagementStrategyAwsKmsReEncrypt(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_AwsKms(
                dafny_input.AwsKmsReEncrypt
            )
        )
    elif isinstance(dafny_input, KeyManagementStrategy_AwsKmsDecryptEncrypt):
        KeyManagementStrategy_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.KeyManagementStrategyAwsKmsDecryptEncrypt(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_AwsKmsDecryptEncrypt(
                dafny_input.AwsKmsDecryptEncrypt
            )
        )
    elif isinstance(dafny_input, KeyManagementStrategy_AwsKmsSimple):
        KeyManagementStrategy_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.KeyManagementStrategyAwsKmsSimple(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_AwsKms(
                dafny_input.AwsKmsSimple
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return KeyManagementStrategy_union_value


def aws_cryptography_keystoreadmin_AwsKmsDecryptEncrypt(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.AwsKmsDecryptEncrypt(
        decrypt=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_AwsKms(
                    dafny_input.decrypt.value
                )
            )
            if (dafny_input.decrypt.is_Some)
            else None
        ),
        encrypt=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_AwsKms(
                    dafny_input.encrypt.value
                )
            )
            if (dafny_input.encrypt.is_Some)
            else None
        ),
    )


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
        kms_arn=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_KmsSymmetricKeyArn(
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
        hierarchy_version=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_HierarchyVersion(
                    dafny_input.HierarchyVersion.value
                )
            )
            if (dafny_input.HierarchyVersion.is_Some)
            else None
        ),
    )


def aws_cryptography_keystoreadmin_VersionKeyInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.VersionKeyInput(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
        kms_arn=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_KmsSymmetricKeyArn(
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
        terminal_hierarchy_version=(
            (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_HierarchyVersion(
                    dafny_input.TerminalHierarchyVersion.value
                )
            )
            if (dafny_input.TerminalHierarchyVersion.is_Some)
            else None
        ),
    )


def aws_cryptography_keystoreadmin_SystemKey(dafny_input):
    # Convert SystemKey
    if isinstance(dafny_input, SystemKey_kmsSymmetricEncryption):
        SystemKey_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.SystemKeyKmsSymmetricEncryption(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_KmsSymmetricEncryption(
                dafny_input.kmsSymmetricEncryption
            )
        )
    elif isinstance(dafny_input, SystemKey_trustStorage):
        SystemKey_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.SystemKeyTrustStorage(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_TrustStorage(
                dafny_input.trustStorage
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return SystemKey_union_value


def aws_cryptography_keystoreadmin_KmsSymmetricEncryption(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.KmsSymmetricEncryption(
        kms_arn=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.KmsArn).decode(
            "utf-16-be"
        ),
        aws_kms=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_AwsKms(
            dafny_input.AwsKms
        ),
    )


def aws_cryptography_keystoreadmin_TrustStorage(dafny_input):
    return (
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.TrustStorage()
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
        system_key=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_SystemKey(
            dafny_input.SystemKey
        ),
        do_not_version=(
            (dafny_input.DoNotVersion.value)
            if (dafny_input.DoNotVersion.is_Some)
            else None
        ),
    )


def aws_cryptography_keystoreadmin_MutationToken(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.MutationToken(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
        uuid=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.UUID).decode(
            "utf-16-be"
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
        system_key=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_SystemKey(
            dafny_input.SystemKey
        ),
    )


def aws_cryptography_keystoreadmin_DescribeMutationInput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.DescribeMutationInput(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
    )


def aws_cryptography_keystoreadmin_CreateKeyOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.CreateKeyOutput(
        identifier=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Identifier
        ).decode("utf-16-be"),
        hierarchy_version=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_HierarchyVersion(
            dafny_input.HierarchyVersion
        ),
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


def aws_cryptography_keystoreadmin_InitializeMutationFlag(dafny_input):
    if isinstance(dafny_input, InitializeMutationFlag_Created):
        return "Created"

    elif isinstance(dafny_input, InitializeMutationFlag_Resumed):
        return "Resumed"

    elif isinstance(dafny_input, InitializeMutationFlag_ResumedWithoutIndex):
        return "ResumedWithoutIndex"

    else:
        raise ValueError(f"No recognized enum value in enum type: {dafny_input=}")


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
        initialize_mutation_flag=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_InitializeMutationFlag(
            dafny_input.InitializeMutationFlag
        ),
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


def aws_cryptography_keystoreadmin_MutationInFlight(dafny_input):
    # Convert MutationInFlight
    if isinstance(dafny_input, MutationInFlight_Yes):
        MutationInFlight_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.MutationInFlightYes(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_MutationDescription(
                dafny_input.Yes
            )
        )
    elif isinstance(dafny_input, MutationInFlight_No):
        MutationInFlight_union_value = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.MutationInFlightNo(
            b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.No).decode(
                "utf-16-be"
            )
        )
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return MutationInFlight_union_value


def aws_cryptography_keystoreadmin_MutationDescription(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.MutationDescription(
        mutation_details=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_MutationDetails(
            dafny_input.MutationDetails
        ),
        mutation_token=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_MutationToken(
            dafny_input.MutationToken
        ),
    )


def aws_cryptography_keystoreadmin_MutationDetails(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.MutationDetails(
        original=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_MutableBranchKeyProperties(
            dafny_input.Original
        ),
        terminal=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_MutableBranchKeyProperties(
            dafny_input.Terminal
        ),
        input=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_Mutations(
            dafny_input.Input
        ),
        system_key=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.SystemKey
        ).decode("utf-16-be"),
        create_time=b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.CreateTime
        ).decode("utf-16-be"),
        uuid=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.UUID).decode(
            "utf-16-be"
        ),
    )


def aws_cryptography_keystoreadmin_MutableBranchKeyProperties(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.MutableBranchKeyProperties(
        kms_arn=b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.KmsArn).decode(
            "utf-16-be"
        ),
        custom_encryption_context={
            b"".join(ord(c).to_bytes(2, "big") for c in key)
            .decode("utf-16-be"): b"".join(ord(c).to_bytes(2, "big") for c in value)
            .decode("utf-16-be")
            for (key, value) in dafny_input.CustomEncryptionContext.items
        },
        hierarchy_version=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_HierarchyVersion(
            dafny_input.HierarchyVersion
        ),
    )


def aws_cryptography_keystoreadmin_DescribeMutationOutput(dafny_input):
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.models.DescribeMutationOutput(
        mutation_in_flight=aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_MutationInFlight(
            dafny_input.MutationInFlight
        ),
    )


def aws_cryptography_keystoreadmin_DdbClientReference(dafny_input):
    return dafny_input._impl


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


def aws_cryptography_keystoreadmin_KeyStoreReference(dafny_input):
    from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.client import (
        KeyStore,
    )

    return KeyStore(config=None, dafny_client=dafny_input)


def aws_cryptography_keystoreadmin_KmsClientReference(dafny_input):
    return dafny_input._impl


def aws_cryptography_keystoreadmin_PrimitivesReference(dafny_input):
    from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.client import (
        AwsCryptographicPrimitives,
    )

    return AwsCryptographicPrimitives(config=None, dafny_client=dafny_input)
