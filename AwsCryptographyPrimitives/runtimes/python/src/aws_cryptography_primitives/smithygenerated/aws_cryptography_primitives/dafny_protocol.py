# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes import (
    AESDecryptInput_AESDecryptInput as DafnyAESDecryptInput,
    AESEncryptInput_AESEncryptInput as DafnyAESEncryptInput,
    AesKdfCtrInput_AesKdfCtrInput as DafnyAesKdfCtrInput,
    DigestInput_DigestInput as DafnyDigestInput,
    ECDSASignInput_ECDSASignInput as DafnyECDSASignInput,
    ECDSAVerifyInput_ECDSAVerifyInput as DafnyECDSAVerifyInput,
    GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput as DafnyGenerateECDSASignatureKeyInput,
    GenerateRSAKeyPairInput_GenerateRSAKeyPairInput as DafnyGenerateRSAKeyPairInput,
    GenerateRandomBytesInput_GenerateRandomBytesInput as DafnyGenerateRandomBytesInput,
    GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput as DafnyGetRSAKeyModulusLengthInput,
    HMacInput_HMacInput as DafnyHMacInput,
    HkdfExpandInput_HkdfExpandInput as DafnyHkdfExpandInput,
    HkdfExtractInput_HkdfExtractInput as DafnyHkdfExtractInput,
    HkdfInput_HkdfInput as DafnyHkdfInput,
    KdfCtrInput_KdfCtrInput as DafnyKdfCtrInput,
    RSADecryptInput_RSADecryptInput as DafnyRSADecryptInput,
    RSAEncryptInput_RSAEncryptInput as DafnyRSAEncryptInput,
)
import module_


import standard_library.internaldafny.generated.Wrappers as Wrappers
from typing import Union

class DafnyRequest:
    operation_name: str

    # dafny_operation_input can take on any one of the types
    # of the input values passed to the Dafny implementation
    dafny_operation_input: Union[
        DafnyGetRSAKeyModulusLengthInput,
        DafnyGenerateECDSASignatureKeyInput,
        DafnyHkdfExtractInput,
        DafnyECDSASignInput,
        DafnyHkdfInput,
        DafnyRSADecryptInput,
        DafnyDigestInput,
        DafnyHMacInput,
        DafnyHkdfExpandInput,
        DafnyECDSAVerifyInput,
        DafnyAESDecryptInput,
        DafnyAESEncryptInput,
        DafnyAesKdfCtrInput,
        DafnyKdfCtrInput,
        DafnyGenerateRSAKeyPairInput,
        DafnyGenerateRandomBytesInput,
        DafnyRSAEncryptInput,
    ]

    def __init__(self, operation_name, dafny_operation_input):
        self.operation_name = operation_name
        self.dafny_operation_input = dafny_operation_input

class DafnyResponse(Wrappers.Result):
    def __init__(self):
        super().__init__(self)
