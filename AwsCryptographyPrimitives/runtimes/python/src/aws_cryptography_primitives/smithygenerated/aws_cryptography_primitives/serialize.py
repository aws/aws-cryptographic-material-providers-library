# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny

from .dafny_protocol import DafnyRequest

from .config import Config


def _serialize_generate_random_bytes(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="GenerateRandomBytes",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_GenerateRandomBytesInput(
            input
        ),
    )


def _serialize_digest(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="Digest",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_DigestInput(
            input
        ),
    )


def _serialize_h_mac(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="HMac",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_HMacInput(
            input
        ),
    )


def _serialize_hkdf_extract(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="HkdfExtract",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_HkdfExtractInput(
            input
        ),
    )


def _serialize_hkdf_expand(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="HkdfExpand",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_HkdfExpandInput(
            input
        ),
    )


def _serialize_hkdf(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="Hkdf",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_HkdfInput(
            input
        ),
    )


def _serialize_kdf_counter_mode(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="KdfCounterMode",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_KdfCtrInput(
            input
        ),
    )


def _serialize_aes_kdf_counter_mode(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="AesKdfCounterMode",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_AesKdfCtrInput(
            input
        ),
    )


def _serialize_aes_encrypt(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="AESEncrypt",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_AESEncryptInput(
            input
        ),
    )


def _serialize_aes_decrypt(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="AESDecrypt",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_AESDecryptInput(
            input
        ),
    )


def _serialize_generate_rsa_key_pair(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="GenerateRSAKeyPair",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_GenerateRSAKeyPairInput(
            input
        ),
    )


def _serialize_get_rsa_key_modulus_length(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="GetRSAKeyModulusLength",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_GetRSAKeyModulusLengthInput(
            input
        ),
    )


def _serialize_rsa_decrypt(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="RSADecrypt",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_RSADecryptInput(
            input
        ),
    )


def _serialize_rsa_encrypt(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="RSAEncrypt",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_RSAEncryptInput(
            input
        ),
    )


def _serialize_generate_ecdsa_signature_key(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="GenerateECDSASignatureKey",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_GenerateECDSASignatureKeyInput(
            input
        ),
    )


def _serialize_ecdsa_sign(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="ECDSASign",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDSASignInput(
            input
        ),
    )


def _serialize_ecdsa_verify(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="ECDSAVerify",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDSAVerifyInput(
            input
        ),
    )


def _serialize_generate_ecc_key_pair(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="GenerateECCKeyPair",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_GenerateECCKeyPairInput(
            input
        ),
    )


def _serialize_get_public_key_from_private_key(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="GetPublicKeyFromPrivateKey",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_GetPublicKeyFromPrivateKeyInput(
            input
        ),
    )


def _serialize_validate_public_key(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="ValidatePublicKey",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ValidatePublicKeyInput(
            input
        ),
    )


def _serialize_derive_shared_secret(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="DeriveSharedSecret",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_DeriveSharedSecretInput(
            input
        ),
    )


def _serialize_compress_public_key(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="CompressPublicKey",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_CompressPublicKeyInput(
            input
        ),
    )


def _serialize_decompress_public_key(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="DecompressPublicKey",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_DecompressPublicKeyInput(
            input
        ),
    )


def _serialize_parse_public_key(input, config: Config) -> DafnyRequest:
    return DafnyRequest(
        operation_name="ParsePublicKey",
        dafny_operation_input=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ParsePublicKeyInput(
            input
        ),
    )
