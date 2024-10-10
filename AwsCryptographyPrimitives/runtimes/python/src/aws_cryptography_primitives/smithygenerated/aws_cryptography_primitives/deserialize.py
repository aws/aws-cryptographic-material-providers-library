# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import _dafny
from aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes import (
    AESEncryptOutput_AESEncryptOutput as DafnyAESEncryptOutput,
    CompressPublicKeyOutput_CompressPublicKeyOutput as DafnyCompressPublicKeyOutput,
    DecompressPublicKeyOutput_DecompressPublicKeyOutput as DafnyDecompressPublicKeyOutput,
    DeriveSharedSecretOutput_DeriveSharedSecretOutput as DafnyDeriveSharedSecretOutput,
    Error,
    Error_AwsCryptographicPrimitivesError,
    GenerateECCKeyPairOutput_GenerateECCKeyPairOutput as DafnyGenerateECCKeyPairOutput,
    GenerateECDSASignatureKeyOutput_GenerateECDSASignatureKeyOutput as DafnyGenerateECDSASignatureKeyOutput,
    GenerateRSAKeyPairOutput_GenerateRSAKeyPairOutput as DafnyGenerateRSAKeyPairOutput,
    GetPublicKeyFromPrivateKeyOutput_GetPublicKeyFromPrivateKeyOutput as DafnyGetPublicKeyFromPrivateKeyOutput,
    GetRSAKeyModulusLengthOutput_GetRSAKeyModulusLengthOutput as DafnyGetRSAKeyModulusLengthOutput,
    ParsePublicKeyOutput_ParsePublicKeyOutput as DafnyParsePublicKeyOutput,
    ValidatePublicKeyOutput_ValidatePublicKeyOutput as DafnyValidatePublicKeyOutput,
)
import aws_cryptography_primitives.internaldafny.generated.module_
import aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy
from typing import Any

from .dafny_protocol import DafnyResponse
from .errors import (
    AwsCryptographicPrimitivesError,
    CollectionOfErrors,
    OpaqueError,
    ServiceError,
)

from .config import Config


def _deserialize_generate_random_bytes(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_GenerateRandomBytesOutput(
        input.value
    )


def _deserialize_digest(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_DigestOutput(
        input.value
    )


def _deserialize_h_mac(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_HMacOutput(
        input.value
    )


def _deserialize_hkdf_extract(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_HkdfExtractOutput(
        input.value
    )


def _deserialize_hkdf_expand(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_HkdfExpandOutput(
        input.value
    )


def _deserialize_hkdf(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_HkdfOutput(
        input.value
    )


def _deserialize_kdf_counter_mode(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_KdfCtrOutput(
        input.value
    )


def _deserialize_aes_kdf_counter_mode(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_AesKdfCtrOutput(
        input.value
    )


def _deserialize_aes_encrypt(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_AESEncryptOutput(
        input.value
    )


def _deserialize_aes_decrypt(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_AESDecryptOutput(
        input.value
    )


def _deserialize_generate_rsa_key_pair(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_GenerateRSAKeyPairOutput(
        input.value
    )


def _deserialize_get_rsa_key_modulus_length(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_GetRSAKeyModulusLengthOutput(
        input.value
    )


def _deserialize_rsa_decrypt(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_RSADecryptOutput(
        input.value
    )


def _deserialize_rsa_encrypt(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_RSAEncryptOutput(
        input.value
    )


def _deserialize_generate_ecdsa_signature_key(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_GenerateECDSASignatureKeyOutput(
        input.value
    )


def _deserialize_ecdsa_sign(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDSASignOutput(
        input.value
    )


def _deserialize_ecdsa_verify(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDSAVerifyOutput(
        input.value
    )


def _deserialize_generate_ecc_key_pair(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_GenerateECCKeyPairOutput(
        input.value
    )


def _deserialize_get_public_key_from_private_key(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_GetPublicKeyFromPrivateKeyOutput(
        input.value
    )


def _deserialize_validate_public_key(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ValidatePublicKeyOutput(
        input.value
    )


def _deserialize_derive_shared_secret(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_DeriveSharedSecretOutput(
        input.value
    )


def _deserialize_compress_public_key(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_CompressPublicKeyOutput(
        input.value
    )


def _deserialize_decompress_public_key(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_DecompressPublicKeyOutput(
        input.value
    )


def _deserialize_parse_public_key(input: DafnyResponse, config: Config):

    if input.IsFailure():
        return _deserialize_error(input.error)
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ParsePublicKeyOutput(
        input.value
    )


def _deserialize_error(error: Error) -> ServiceError:
    if error.is_Opaque:
        return OpaqueError(obj=error.obj, alt_text=error.alt__text)
    elif error.is_CollectionOfErrors:
        return CollectionOfErrors(
            message=_dafny.string_of(error.message),
            list=[_deserialize_error(dafny_e) for dafny_e in error.list],
        )
    elif error.is_AwsCryptographicPrimitivesError:
        return AwsCryptographicPrimitivesError(message=_dafny.string_of(error.message))
    else:
        return OpaqueError(obj=error, alt_text=repr(error))
