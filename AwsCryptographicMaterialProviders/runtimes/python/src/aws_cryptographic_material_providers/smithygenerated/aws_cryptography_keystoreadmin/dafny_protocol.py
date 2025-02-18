# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes import (
    ApplyMutationInput_ApplyMutationInput as DafnyApplyMutationInput,
    AtomicMutationInput_AtomicMutationInput as DafnyAtomicMutationInput,
    CreateKeyInput_CreateKeyInput as DafnyCreateKeyInput,
    DescribeMutationInput_DescribeMutationInput as DafnyDescribeMutationInput,
    InitializeMutationInput_InitializeMutationInput as DafnyInitializeMutationInput,
    VersionKeyInput_VersionKeyInput as DafnyVersionKeyInput,
)
import aws_cryptographic_material_providers.internaldafny.generated.module_


import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
from typing import Union


class DafnyRequest:
    operation_name: str

    # dafny_operation_input can take on any one of the types
    # of the input values passed to the Dafny implementation
    dafny_operation_input: Union[
        DafnyDescribeMutationInput,
        DafnyApplyMutationInput,
        DafnyAtomicMutationInput,
        DafnyCreateKeyInput,
        DafnyVersionKeyInput,
        DafnyInitializeMutationInput,
    ]

    def __init__(self, operation_name, dafny_operation_input):
        self.operation_name = operation_name
        self.dafny_operation_input = dafny_operation_input


class DafnyResponse(Wrappers.Result):
    def __init__(self):
        super().__init__(self)
