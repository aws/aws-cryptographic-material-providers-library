# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from _dafny import Map, Seq
from aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes import (
    ApplyMutationInput_ApplyMutationInput as DafnyApplyMutationInput,
    ApplyMutationOutput_ApplyMutationOutput as DafnyApplyMutationOutput,
    ApplyMutationResult_CompleteMutation,
    ApplyMutationResult_ContinueMutation,
    CreateKeyInput_CreateKeyInput as DafnyCreateKeyInput,
    CreateKeyOutput_CreateKeyOutput as DafnyCreateKeyOutput,
    DescribeMutationInput_DescribeMutationInput as DafnyDescribeMutationInput,
    DescribeMutationOutput_DescribeMutationOutput as DafnyDescribeMutationOutput,
    InitializeMutationFlag_Created,
    InitializeMutationFlag_Resumed,
    InitializeMutationFlag_ResumedWithoutIndex,
    InitializeMutationInput_InitializeMutationInput as DafnyInitializeMutationInput,
    InitializeMutationOutput_InitializeMutationOutput as DafnyInitializeMutationOutput,
    KeyManagementStrategy_AwsKmsReEncrypt,
    KeyStoreAdminConfig_KeyStoreAdminConfig as DafnyKeyStoreAdminConfig,
    KmsAesIdentifier_KmsKeyArn,
    KmsAesIdentifier_KmsMRKeyArn,
    KmsAes_KmsAes as DafnyKmsAes,
    MutableBranchKeyProperities_MutableBranchKeyProperities as DafnyMutableBranchKeyProperities,
    MutatedBranchKeyItem_MutatedBranchKeyItem as DafnyMutatedBranchKeyItem,
    MutationComplete_MutationComplete as DafnyMutationComplete,
    MutationToken_MutationToken as DafnyMutationToken,
    Mutations_Mutations as DafnyMutations,
    SystemKey_KmsAes,
    SystemKey_TrustStorage,
    TrustStorage_TrustStorage as DafnyTrustStorage,
    VersionKeyInput_VersionKeyInput as DafnyVersionKeyInput,
    VersionKeyOutput_VersionKeyOutput as DafnyVersionKeyOutput,
)
import aws_cryptographic_materialproviders.internaldafny.generated.module_
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.models
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny
from smithy_dafny_standard_library.internaldafny.generated.Wrappers import (
    Option_None,
    Option_Some,
)


def aws_cryptography_keystoreadmin_CreateKeyInput(native_input):
    return DafnyCreateKeyInput(
        Identifier=(
            (
                Option_Some(
                    Seq(
                        "".join(
                            [
                                chr(int.from_bytes(pair, "big"))
                                for pair in zip(
                                    *[iter(native_input.identifier.encode("utf-16-be"))]
                                    * 2
                                )
                            ]
                        )
                    )
                )
            )
            if (native_input.identifier is not None)
            else (Option_None())
        ),
        EncryptionContext=(
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
        KmsArn=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_KmsAesIdentifier(
            native_input.kms_arn
        ),
        Strategy=(
            (
                Option_Some(
                    aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_KeyManagementStrategy(
                        native_input.strategy
                    )
                )
            )
            if (native_input.strategy is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_keystoreadmin_KmsAesIdentifier(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.models.KmsAesIdentifierKmsKeyArn,
    ):
        KmsAesIdentifier_union_value = KmsAesIdentifier_KmsKeyArn(
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
        aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.models.KmsAesIdentifierKmsMRKeyArn,
    ):
        KmsAesIdentifier_union_value = KmsAesIdentifier_KmsMRKeyArn(
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
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return KmsAesIdentifier_union_value


def aws_cryptography_keystoreadmin_KeyManagementStrategy(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.models.KeyManagementStrategyAwsKmsReEncrypt,
    ):
        KeyManagementStrategy_union_value = KeyManagementStrategy_AwsKmsReEncrypt(
            aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_AwsKms(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return KeyManagementStrategy_union_value


def aws_cryptography_keystoreadmin_VersionKeyInput(native_input):
    return DafnyVersionKeyInput(
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
        KmsArn=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_KmsAesIdentifier(
            native_input.kms_arn
        ),
        Strategy=(
            (
                Option_Some(
                    aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_KeyManagementStrategy(
                        native_input.strategy
                    )
                )
            )
            if (native_input.strategy is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_keystoreadmin_InitializeMutationInput(native_input):
    return DafnyInitializeMutationInput(
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
        Mutations=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_Mutations(
            native_input.mutations
        ),
        Strategy=(
            (
                Option_Some(
                    aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_KeyManagementStrategy(
                        native_input.strategy
                    )
                )
            )
            if (native_input.strategy is not None)
            else (Option_None())
        ),
        SystemKey=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_SystemKey(
            native_input.system_key
        ),
    )


def aws_cryptography_keystoreadmin_Mutations(native_input):
    return DafnyMutations(
        TerminalKmsArn=(
            (
                Option_Some(
                    Seq(
                        "".join(
                            [
                                chr(int.from_bytes(pair, "big"))
                                for pair in zip(
                                    *[
                                        iter(
                                            native_input.terminal_kms_arn.encode(
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
            if (native_input.terminal_kms_arn is not None)
            else (Option_None())
        ),
        TerminalEncryptionContext=(
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
                            ): Seq(
                                "".join(
                                    [
                                        chr(int.from_bytes(pair, "big"))
                                        for pair in zip(
                                            *[iter(value.encode("utf-16-be"))] * 2
                                        )
                                    ]
                                )
                            )
                            for (
                                key,
                                value,
                            ) in native_input.terminal_encryption_context.items()
                        }
                    )
                )
            )
            if (native_input.terminal_encryption_context is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_keystoreadmin_SystemKey(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.models.SystemKeyKmsAes,
    ):
        SystemKey_union_value = SystemKey_KmsAes(
            aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_KmsAes(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.models.SystemKeyTrustStorage,
    ):
        SystemKey_union_value = SystemKey_TrustStorage(
            aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_TrustStorage(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return SystemKey_union_value


def aws_cryptography_keystoreadmin_KmsAes(native_input):
    return DafnyKmsAes(
        KmsAesIdentifier=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_KmsAesIdentifier(
            native_input.kms_aes_identifier
        ),
        AwsKms=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_AwsKms(
            native_input.aws_kms
        ),
    )


def aws_cryptography_keystoreadmin_TrustStorage(native_input):
    return DafnyTrustStorage()


def aws_cryptography_keystoreadmin_ApplyMutationInput(native_input):
    return DafnyApplyMutationInput(
        MutationToken=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_MutationToken(
            native_input.mutation_token
        ),
        PageSize=(
            (Option_Some(native_input.page_size))
            if (native_input.page_size is not None)
            else (Option_None())
        ),
        Strategy=(
            (
                Option_Some(
                    aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_KeyManagementStrategy(
                        native_input.strategy
                    )
                )
            )
            if (native_input.strategy is not None)
            else (Option_None())
        ),
        SystemKey=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_SystemKey(
            native_input.system_key
        ),
    )


def aws_cryptography_keystoreadmin_MutationToken(native_input):
    return DafnyMutationToken(
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
        UUID=(
            (
                Option_Some(
                    Seq(
                        "".join(
                            [
                                chr(int.from_bytes(pair, "big"))
                                for pair in zip(
                                    *[iter(native_input.uuid.encode("utf-16-be"))] * 2
                                )
                            ]
                        )
                    )
                )
            )
            if (native_input.uuid is not None)
            else (Option_None())
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
    )


def aws_cryptography_keystoreadmin_DescribeMutationInput(native_input):
    return DafnyDescribeMutationInput(
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


def aws_cryptography_keystoreadmin_CreateKeyOutput(native_input):
    return DafnyCreateKeyOutput(
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


def aws_cryptography_keystoreadmin_VersionKeyOutput(native_input):
    return DafnyVersionKeyOutput()


def aws_cryptography_keystoreadmin_InitializeMutationOutput(native_input):
    return DafnyInitializeMutationOutput(
        MutationToken=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_MutationToken(
            native_input.mutation_token
        ),
        MutatedBranchKeyItems=Seq(
            [
                aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_MutatedBranchKeyItem(
                    list_element
                )
                for list_element in native_input.mutated_branch_key_items
            ]
        ),
        InitializeMutationFlag=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_InitializeMutationFlag(
            native_input.initialize_mutation_flag
        ),
    )


def aws_cryptography_keystoreadmin_MutatedBranchKeyItem(native_input):
    return DafnyMutatedBranchKeyItem(
        ItemType=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.item_type.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Description=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input.description.encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def aws_cryptography_keystoreadmin_InitializeMutationFlag(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.models.InitializeMutationFlagCreated,
    ):
        InitializeMutationFlag_union_value = InitializeMutationFlag_Created(
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
        aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.models.InitializeMutationFlagResumed,
    ):
        InitializeMutationFlag_union_value = InitializeMutationFlag_Resumed(
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
        aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.models.InitializeMutationFlagResumedWithoutIndex,
    ):
        InitializeMutationFlag_union_value = InitializeMutationFlag_ResumedWithoutIndex(
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
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return InitializeMutationFlag_union_value


def aws_cryptography_keystoreadmin_ApplyMutationOutput(native_input):
    return DafnyApplyMutationOutput(
        MutationResult=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_ApplyMutationResult(
            native_input.mutation_result
        ),
        MutatedBranchKeyItems=Seq(
            [
                aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_MutatedBranchKeyItem(
                    list_element
                )
                for list_element in native_input.mutated_branch_key_items
            ]
        ),
    )


def aws_cryptography_keystoreadmin_ApplyMutationResult(native_input):
    if isinstance(
        native_input,
        aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.models.ApplyMutationResultContinueMutation,
    ):
        ApplyMutationResult_union_value = ApplyMutationResult_ContinueMutation(
            aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_MutationToken(
                native_input.value
            )
        )
    elif isinstance(
        native_input,
        aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.models.ApplyMutationResultCompleteMutation,
    ):
        ApplyMutationResult_union_value = ApplyMutationResult_CompleteMutation(
            aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_MutationComplete(
                native_input.value
            )
        )
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return ApplyMutationResult_union_value


def aws_cryptography_keystoreadmin_MutationComplete(native_input):
    return DafnyMutationComplete()


def aws_cryptography_keystoreadmin_DescribeMutationOutput(native_input):
    return DafnyDescribeMutationOutput(
        Original=(
            (
                Option_Some(
                    aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_MutableBranchKeyProperities(
                        native_input.original
                    )
                )
            )
            if (native_input.original is not None)
            else (Option_None())
        ),
        Terminal=(
            (
                Option_Some(
                    aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_MutableBranchKeyProperities(
                        native_input.terminal
                    )
                )
            )
            if (native_input.terminal is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_keystoreadmin_MutableBranchKeyProperities(native_input):
    return DafnyMutableBranchKeyProperities(
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
        CustomEncryptionContext=Map(
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
                for (key, value) in native_input.custom_encryption_context.items()
            }
        ),
    )


def aws_cryptography_keystoreadmin_KeyStoreAdminConfig(native_input):
    return DafnyKeyStoreAdminConfig(
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
        storage=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_Storage(
            native_input.storage
        ),
    )
