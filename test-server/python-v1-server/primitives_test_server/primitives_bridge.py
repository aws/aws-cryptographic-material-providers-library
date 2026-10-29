# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""Delegates each Primitives TestServer operation to the Python AtomicPrimitives
client built from this repo's ``AwsCryptographyPrimitives`` Dafny runtime.

Each handler takes the decoded rpcv2Cbor request map, calls the client, and
returns the response member map. A malformed request raises ``ServerError``
(serialized as ``GenericServerError``); a failure from the primitives client
raises ``PrimitivesError`` (serialized as ``PrimitivesError``).

The client is stateless across operations, so one instance is shared by all
request threads.
"""

from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.client import (
    AwsCryptographicPrimitives,
)
from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.config import (
    CryptoConfig,
)
from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives import models


class ServerError(Exception):
    """Framework-side failure: malformed request, unknown operation or enum."""


class PrimitivesError(Exception):
    """Failure forwarded from the AtomicPrimitives client."""


# AES-GCM key size in bytes per modeled algorithm. The GCM tag is 16 bytes.
_AES_KEY_LENGTH = {"AES_128_GCM": 16, "AES_192_GCM": 24, "AES_256_GCM": 32}
_GCM_TAG_LENGTH = 16

_CLIENT = AwsCryptographicPrimitives(CryptoConfig())


def _require(request, name):
    try:
        return request[name]
    except (KeyError, TypeError):
        raise ServerError(f"missing required field: {name}")


def _aes_gcm(request):
    algorithm = _require(request, "algorithm")
    key_length = _AES_KEY_LENGTH.get(algorithm)
    if key_length is None:
        raise ServerError(f"unknown AES algorithm: {algorithm}")
    return models.AES_GCM(
        key_length=key_length,
        tag_length=_GCM_TAG_LENGTH,
        iv_length=len(_require(request, "iv")),
    )


def aes_encrypt(request):
    enc_alg = _aes_gcm(request)
    try:
        output = _CLIENT.aes_encrypt(
            models.AESEncryptInput(
                enc_alg=enc_alg,
                iv=_require(request, "iv"),
                key=_require(request, "key"),
                msg=_require(request, "message"),
                aad=_require(request, "aad"),
            )
        )
    except Exception as exc:  # noqa: BLE001
        raise PrimitivesError(str(exc)) from exc
    return {"ciphertext": bytes(output.cipher_text), "authTag": bytes(output.auth_tag)}


def aes_decrypt(request):
    enc_alg = _aes_gcm(request)
    try:
        plaintext = _CLIENT.aes_decrypt(
            models.AESDecryptInput(
                enc_alg=enc_alg,
                key=_require(request, "key"),
                cipher_txt=_require(request, "ciphertext"),
                auth_tag=_require(request, "authTag"),
                iv=_require(request, "iv"),
                aad=_require(request, "aad"),
            )
        )
    except Exception as exc:  # noqa: BLE001
        raise PrimitivesError(str(exc)) from exc
    return {"plaintext": bytes(plaintext)}


def generate_random_bytes(request):
    try:
        data = _CLIENT.generate_random_bytes(
            models.GenerateRandomBytesInput(length=_require(request, "length"))
        )
    except Exception as exc:  # noqa: BLE001
        raise PrimitivesError(str(exc)) from exc
    return {"data": bytes(data)}


def digest(request):
    try:
        value = _CLIENT.digest(
            models.DigestInput(
                digest_algorithm=_require(request, "algorithm"),
                message=_require(request, "data"),
            )
        )
    except Exception as exc:  # noqa: BLE001
        raise PrimitivesError(str(exc)) from exc
    return {"digest": bytes(value)}


def hmac(request):
    try:
        value = _CLIENT.h_mac(
            models.HMacInput(
                digest_algorithm=_require(request, "algorithm"),
                key=_require(request, "key"),
                message=_require(request, "message"),
            )
        )
    except Exception as exc:  # noqa: BLE001
        raise PrimitivesError(str(exc)) from exc
    return {"digest": bytes(value)}


def hkdf(request):
    try:
        okm = _CLIENT.hkdf(
            models.HkdfInput(
                digest_algorithm=_require(request, "algorithm"),
                salt=_require(request, "salt"),
                ikm=_require(request, "ikm"),
                info=_require(request, "info"),
                expected_length=_require(request, "expectedLength"),
            )
        )
    except Exception as exc:  # noqa: BLE001
        raise PrimitivesError(str(exc)) from exc
    return {"okm": bytes(okm)}


def kbkdf_ctr_hmac(request):
    # KdfCounterMode assembles the SP800-108 fixed input as purpose || 0x00 ||
    # nonce || [L]; the modeled `info` is passed as the purpose label.
    try:
        okm = _CLIENT.kdf_counter_mode(
            models.KdfCtrInput(
                digest_algorithm=_require(request, "algorithm"),
                ikm=_require(request, "ikm"),
                expected_length=_require(request, "expectedLength"),
                purpose=_require(request, "info"),
            )
        )
    except Exception as exc:  # noqa: BLE001
        raise PrimitivesError(str(exc)) from exc
    return {"okm": bytes(okm)}


def ecdsa_generate_key_pair(request):
    try:
        output = _CLIENT.generate_ecdsa_signature_key(
            models.GenerateECDSASignatureKeyInput(
                signature_algorithm=_require(request, "algorithm")
            )
        )
    except Exception as exc:  # noqa: BLE001
        raise PrimitivesError(str(exc)) from exc
    return {
        "verificationKey": bytes(output.verification_key),
        "signingKey": bytes(output.signing_key),
    }


def ecdsa_sign(request):
    try:
        signature = _CLIENT.ecdsa_sign(
            models.ECDSASignInput(
                signature_algorithm=_require(request, "algorithm"),
                signing_key=_require(request, "signingKey"),
                message=_require(request, "message"),
            )
        )
    except Exception as exc:  # noqa: BLE001
        raise PrimitivesError(str(exc)) from exc
    return {"signature": bytes(signature)}


def ecdsa_verify(request):
    try:
        valid = _CLIENT.ecdsa_verify(
            models.ECDSAVerifyInput(
                signature_algorithm=_require(request, "algorithm"),
                verification_key=_require(request, "verificationKey"),
                message=_require(request, "message"),
                signature=_require(request, "signature"),
            )
        )
    except Exception as exc:  # noqa: BLE001
        raise PrimitivesError(str(exc)) from exc
    return {"valid": valid}


OPERATIONS = {
    "AesEncrypt": aes_encrypt,
    "AesDecrypt": aes_decrypt,
    "GenerateRandomBytes": generate_random_bytes,
    "Digest": digest,
    "Hmac": hmac,
    "Hkdf": hkdf,
    "KbkdfCtrHmac": kbkdf_ctr_hmac,
    "EcdsaGenerateKeyPair": ecdsa_generate_key_pair,
    "EcdsaSign": ecdsa_sign,
    "EcdsaVerify": ecdsa_verify,
}
