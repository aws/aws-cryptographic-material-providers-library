# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes import (
    AESDecryptInput_AESDecryptInput as DafnyAESDecryptInput,
    AESEncryptInput_AESEncryptInput as DafnyAESEncryptInput,
    AesKdfCtrInput_AesKdfCtrInput as DafnyAesKdfCtrInput,
    CompressPublicKeyInput_CompressPublicKeyInput as DafnyCompressPublicKeyInput,
    DecompressPublicKeyInput_DecompressPublicKeyInput as DafnyDecompressPublicKeyInput,
    DeriveSharedSecretInput_DeriveSharedSecretInput as DafnyDeriveSharedSecretInput,
    DigestInput_DigestInput as DafnyDigestInput,
    ECDSASignInput_ECDSASignInput as DafnyECDSASignInput,
    ECDSAVerifyInput_ECDSAVerifyInput as DafnyECDSAVerifyInput,
    GenerateECCKeyPairInput_GenerateECCKeyPairInput as DafnyGenerateECCKeyPairInput,
    GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput as DafnyGenerateECDSASignatureKeyInput,
    GenerateRSAKeyPairInput_GenerateRSAKeyPairInput as DafnyGenerateRSAKeyPairInput,
    GenerateRandomBytesInput_GenerateRandomBytesInput as DafnyGenerateRandomBytesInput,
    GetPublicKeyFromPrivateKeyInput_GetPublicKeyFromPrivateKeyInput as DafnyGetPublicKeyFromPrivateKeyInput,
    GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput as DafnyGetRSAKeyModulusLengthInput,
    HMacInput_HMacInput as DafnyHMacInput,
    HkdfExpandInput_HkdfExpandInput as DafnyHkdfExpandInput,
    HkdfExtractInput_HkdfExtractInput as DafnyHkdfExtractInput,
    HkdfInput_HkdfInput as DafnyHkdfInput,
    KdfCtrInput_KdfCtrInput as DafnyKdfCtrInput,
    ParsePublicKeyInput_ParsePublicKeyInput as DafnyParsePublicKeyInput,
    RSADecryptInput_RSADecryptInput as DafnyRSADecryptInput,
    RSAEncryptInput_RSAEncryptInput as DafnyRSAEncryptInput,
    ValidatePublicKeyInput_ValidatePublicKeyInput as DafnyValidatePublicKeyInput,
)
import aws_cryptography_primitives.internaldafny.generated.module_


import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
from typing import Union


class DafnyRequest:
    operation_name: str

    # dafny_operation_input can take on any one of the types
    # of the input values passed to the Dafny implementation
    dafny_operation_input: Union[
        DafnyGetRSAKeyModulusLengthInput,
        DafnyGetPublicKeyFromPrivateKeyInput,
        DafnyGenerateECDSASignatureKeyInput,
        DafnyHkdfExtractInput,
        DafnyECDSASignInput,
        DafnyHkdfInput,
        DafnyRSADecryptInput,
        DafnyDigestInput,
        DafnyHMacInput,
        DafnyHkdfExpandInput,
        DafnyParsePublicKeyInput,
        DafnyECDSAVerifyInput,
        DafnyCompressPublicKeyInput,
        DafnyAESDecryptInput,
        DafnyGenerateECCKeyPairInput,
        DafnyDeriveSharedSecretInput,
        DafnyAESEncryptInput,
        DafnyDecompressPublicKeyInput,
        DafnyAesKdfCtrInput,
        DafnyKdfCtrInput,
        DafnyGenerateRSAKeyPairInput,
        DafnyValidatePublicKeyInput,
        DafnyGenerateRandomBytesInput,
        DafnyRSAEncryptInput,
    ]

    def __init__(self, operation_name, dafny_operation_input):
        self.operation_name = operation_name
        self.dafny_operation_input = dafny_operation_input


class DafnyResponse(Wrappers.Result):
    def __init__(self):
        super().__init__(self)
