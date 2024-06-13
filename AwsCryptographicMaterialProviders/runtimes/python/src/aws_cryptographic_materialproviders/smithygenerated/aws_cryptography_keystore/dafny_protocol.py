# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes import (
    CreateKeyInput_CreateKeyInput as DafnyCreateKeyInput,
    CreateKeyStoreInput_CreateKeyStoreInput as DafnyCreateKeyStoreInput,
    GetActiveBranchKeyInput_GetActiveBranchKeyInput as DafnyGetActiveBranchKeyInput,
    GetBeaconKeyInput_GetBeaconKeyInput as DafnyGetBeaconKeyInput,
    GetBranchKeyVersionInput_GetBranchKeyVersionInput as DafnyGetBranchKeyVersionInput,
    VersionKeyInput_VersionKeyInput as DafnyVersionKeyInput,
)
import aws_cryptographic_materialproviders.internaldafny.generated.module_


import standard_library.internaldafny.generated.Wrappers as Wrappers
from typing import Union

class DafnyRequest:
    operation_name: str

    # dafny_operation_input can take on any one of the types
    # of the input values passed to the Dafny implementation
    dafny_operation_input: Union[
        DafnyGetActiveBranchKeyInput,
        DafnyVersionKeyInput,
        DafnyGetBranchKeyVersionInput,
        DafnyGetBeaconKeyInput,
        None,
        DafnyCreateKeyInput,
        DafnyCreateKeyStoreInput,
    ]

    def __init__(self, operation_name, dafny_operation_input):
        self.operation_name = operation_name
        self.dafny_operation_input = dafny_operation_input

class DafnyResponse(Wrappers.Result):
    def __init__(self):
        super().__init__(self)
