# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AwsCryptographyMaterialProvidersTestVectorKeysTypes import (
    GetKeyDescriptionInput_GetKeyDescriptionInput as DafnyGetKeyDescriptionInput,
    SerializeKeyDescriptionInput_SerializeKeyDescriptionInput as DafnySerializeKeyDescriptionInput,
    TestVectorCmmInput_TestVectorCmmInput as DafnyTestVectorCmmInput,
    TestVectorKeyringInput_TestVectorKeyringInput as DafnyTestVectorKeyringInput,
)
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.module_


import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
from typing import Union


class DafnyRequest:
    operation_name: str

    # dafny_operation_input can take on any one of the types
    # of the input values passed to the Dafny implementation
    dafny_operation_input: Union[
        DafnyGetKeyDescriptionInput,
        DafnySerializeKeyDescriptionInput,
        DafnyTestVectorKeyringInput,
        DafnyTestVectorCmmInput,
    ]

    def __init__(self, operation_name, dafny_operation_input):
        self.operation_name = operation_name
        self.dafny_operation_input = dafny_operation_input


class DafnyResponse(Wrappers.Result):
    def __init__(self):
        super().__init__(self)
