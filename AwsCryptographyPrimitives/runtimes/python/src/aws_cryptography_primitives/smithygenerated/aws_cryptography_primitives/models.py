# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from typing import Any, Dict, Optional


class AES_GCM:
    key_length: int
    tag_length: int
    iv_length: int

    def __init__(
        self,
        *,
        key_length: int = 0,
        tag_length: int = 0,
        iv_length: int = 0,
    ):
        if (key_length is not None) and (key_length < 1):
            raise ValueError("key_length must be greater than or equal to 1")

        if (key_length is not None) and (key_length > 32):
            raise ValueError("key_length must be less than or equal to 32")

        self.key_length = key_length
        if (tag_length is not None) and (tag_length < 0):
            raise ValueError("tag_length must be greater than or equal to 0")

        if (tag_length is not None) and (tag_length > 32):
            raise ValueError("tag_length must be less than or equal to 32")

        self.tag_length = tag_length
        if (iv_length is not None) and (iv_length < 0):
            raise ValueError("iv_length must be greater than or equal to 0")

        if (iv_length is not None) and (iv_length > 255):
            raise ValueError("iv_length must be less than or equal to 255")

        self.iv_length = iv_length

    def as_dict(self) -> Dict[str, Any]:
        """Converts the AES_GCM to a dictionary."""
        d: Dict[str, Any] = {}

        if self.key_length is not None:
            d["key_length"] = self.key_length

        if self.tag_length is not None:
            d["tag_length"] = self.tag_length

        if self.iv_length is not None:
            d["iv_length"] = self.iv_length

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AES_GCM":
        """Creates a AES_GCM from a dictionary."""
        kwargs: Dict[str, Any] = {}

        if "key_length" in d:
            kwargs["key_length"] = d["key_length"]

        if "tag_length" in d:
            kwargs["tag_length"] = d["tag_length"]

        if "iv_length" in d:
            kwargs["iv_length"] = d["iv_length"]

        return AES_GCM(**kwargs)

    def __repr__(self) -> str:
        result = "AES_GCM("
        if self.key_length is not None:
            result += f"key_length={repr(self.key_length)}, "

        if self.tag_length is not None:
            result += f"tag_length={repr(self.tag_length)}, "

        if self.iv_length is not None:
            result += f"iv_length={repr(self.iv_length)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AES_GCM):
            return False
        attributes: list[str] = [
            "key_length",
            "tag_length",
            "iv_length",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class AESDecryptInput:
    enc_alg: AES_GCM
    key: bytes | bytearray
    cipher_txt: bytes | bytearray
    auth_tag: bytes | bytearray
    iv: bytes | bytearray
    aad: bytes | bytearray

    def __init__(
        self,
        *,
        enc_alg: AES_GCM,
        key: bytes | bytearray,
        cipher_txt: bytes | bytearray,
        auth_tag: bytes | bytearray,
        iv: bytes | bytearray,
        aad: bytes | bytearray,
    ):
        self.enc_alg = enc_alg
        self.key = key
        self.cipher_txt = cipher_txt
        self.auth_tag = auth_tag
        self.iv = iv
        self.aad = aad

    def as_dict(self) -> Dict[str, Any]:
        """Converts the AESDecryptInput to a dictionary."""
        return {
            "enc_alg": self.enc_alg.as_dict(),
            "key": self.key,
            "cipher_txt": self.cipher_txt,
            "auth_tag": self.auth_tag,
            "iv": self.iv,
            "aad": self.aad,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AESDecryptInput":
        """Creates a AESDecryptInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "enc_alg": AES_GCM.from_dict(d["enc_alg"]),
            "key": d["key"],
            "cipher_txt": d["cipher_txt"],
            "auth_tag": d["auth_tag"],
            "iv": d["iv"],
            "aad": d["aad"],
        }

        return AESDecryptInput(**kwargs)

    def __repr__(self) -> str:
        result = "AESDecryptInput("
        if self.enc_alg is not None:
            result += f"enc_alg={repr(self.enc_alg)}, "

        if self.key is not None:
            result += f"key={repr(self.key)}, "

        if self.cipher_txt is not None:
            result += f"cipher_txt={repr(self.cipher_txt)}, "

        if self.auth_tag is not None:
            result += f"auth_tag={repr(self.auth_tag)}, "

        if self.iv is not None:
            result += f"iv={repr(self.iv)}, "

        if self.aad is not None:
            result += f"aad={repr(self.aad)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AESDecryptInput):
            return False
        attributes: list[str] = [
            "enc_alg",
            "key",
            "cipher_txt",
            "auth_tag",
            "iv",
            "aad",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class AESEncryptInput:
    enc_alg: AES_GCM
    iv: bytes | bytearray
    key: bytes | bytearray
    msg: bytes | bytearray
    aad: bytes | bytearray

    def __init__(
        self,
        *,
        enc_alg: AES_GCM,
        iv: bytes | bytearray,
        key: bytes | bytearray,
        msg: bytes | bytearray,
        aad: bytes | bytearray,
    ):
        self.enc_alg = enc_alg
        self.iv = iv
        self.key = key
        self.msg = msg
        self.aad = aad

    def as_dict(self) -> Dict[str, Any]:
        """Converts the AESEncryptInput to a dictionary."""
        return {
            "enc_alg": self.enc_alg.as_dict(),
            "iv": self.iv,
            "key": self.key,
            "msg": self.msg,
            "aad": self.aad,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AESEncryptInput":
        """Creates a AESEncryptInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "enc_alg": AES_GCM.from_dict(d["enc_alg"]),
            "iv": d["iv"],
            "key": d["key"],
            "msg": d["msg"],
            "aad": d["aad"],
        }

        return AESEncryptInput(**kwargs)

    def __repr__(self) -> str:
        result = "AESEncryptInput("
        if self.enc_alg is not None:
            result += f"enc_alg={repr(self.enc_alg)}, "

        if self.iv is not None:
            result += f"iv={repr(self.iv)}, "

        if self.key is not None:
            result += f"key={repr(self.key)}, "

        if self.msg is not None:
            result += f"msg={repr(self.msg)}, "

        if self.aad is not None:
            result += f"aad={repr(self.aad)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AESEncryptInput):
            return False
        attributes: list[str] = [
            "enc_alg",
            "iv",
            "key",
            "msg",
            "aad",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class AESEncryptOutput:
    cipher_text: bytes | bytearray
    auth_tag: bytes | bytearray

    def __init__(
        self,
        *,
        cipher_text: bytes | bytearray,
        auth_tag: bytes | bytearray,
    ):
        self.cipher_text = cipher_text
        self.auth_tag = auth_tag

    def as_dict(self) -> Dict[str, Any]:
        """Converts the AESEncryptOutput to a dictionary."""
        return {
            "cipher_text": self.cipher_text,
            "auth_tag": self.auth_tag,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AESEncryptOutput":
        """Creates a AESEncryptOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "cipher_text": d["cipher_text"],
            "auth_tag": d["auth_tag"],
        }

        return AESEncryptOutput(**kwargs)

    def __repr__(self) -> str:
        result = "AESEncryptOutput("
        if self.cipher_text is not None:
            result += f"cipher_text={repr(self.cipher_text)}, "

        if self.auth_tag is not None:
            result += f"auth_tag={repr(self.auth_tag)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AESEncryptOutput):
            return False
        attributes: list[str] = [
            "cipher_text",
            "auth_tag",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class AesKdfCtrInput:
    ikm: bytes | bytearray
    expected_length: int
    nonce: Optional[bytes | bytearray]

    def __init__(
        self,
        *,
        ikm: bytes | bytearray,
        expected_length: int = 0,
        nonce: Optional[bytes | bytearray] = None,
    ):
        self.ikm = ikm
        if (expected_length is not None) and (expected_length < 0):
            raise ValueError("expected_length must be greater than or equal to 0")

        self.expected_length = expected_length
        self.nonce = nonce

    def as_dict(self) -> Dict[str, Any]:
        """Converts the AesKdfCtrInput to a dictionary."""
        d: Dict[str, Any] = {
            "ikm": self.ikm,
        }

        if self.expected_length is not None:
            d["expected_length"] = self.expected_length

        if self.nonce is not None:
            d["nonce"] = self.nonce

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AesKdfCtrInput":
        """Creates a AesKdfCtrInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "ikm": d["ikm"],
        }

        if "expected_length" in d:
            kwargs["expected_length"] = d["expected_length"]

        if "nonce" in d:
            kwargs["nonce"] = d["nonce"]

        return AesKdfCtrInput(**kwargs)

    def __repr__(self) -> str:
        result = "AesKdfCtrInput("
        if self.ikm is not None:
            result += f"ikm={repr(self.ikm)}, "

        if self.expected_length is not None:
            result += f"expected_length={repr(self.expected_length)}, "

        if self.nonce is not None:
            result += f"nonce={repr(self.nonce)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AesKdfCtrInput):
            return False
        attributes: list[str] = [
            "ikm",
            "expected_length",
            "nonce",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class ECDHCurveSpec:
    ECC_NIST_P256 = "ECC_NIST_P256"

    ECC_NIST_P384 = "ECC_NIST_P384"

    ECC_NIST_P521 = "ECC_NIST_P521"

    SM2 = "SM2"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset({"ECC_NIST_P256", "ECC_NIST_P384", "ECC_NIST_P521", "SM2"})


class ECCPublicKey:
    der: bytes | bytearray

    def __init__(
        self,
        *,
        der: bytes | bytearray,
    ):
        self.der = der

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ECCPublicKey to a dictionary."""
        return {
            "der": self.der,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ECCPublicKey":
        """Creates a ECCPublicKey from a dictionary."""
        kwargs: Dict[str, Any] = {
            "der": d["der"],
        }

        return ECCPublicKey(**kwargs)

    def __repr__(self) -> str:
        result = "ECCPublicKey("
        if self.der is not None:
            result += f"der={repr(self.der)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ECCPublicKey):
            return False
        attributes: list[str] = [
            "der",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CompressPublicKeyInput:
    public_key: ECCPublicKey
    ecc_curve: str

    def __init__(
        self,
        *,
        public_key: ECCPublicKey,
        ecc_curve: str,
    ):
        self.public_key = public_key
        self.ecc_curve = ecc_curve

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CompressPublicKeyInput to a dictionary."""
        return {
            "public_key": self.public_key.as_dict(),
            "ecc_curve": self.ecc_curve,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CompressPublicKeyInput":
        """Creates a CompressPublicKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "public_key": ECCPublicKey.from_dict(d["public_key"]),
            "ecc_curve": d["ecc_curve"],
        }

        return CompressPublicKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "CompressPublicKeyInput("
        if self.public_key is not None:
            result += f"public_key={repr(self.public_key)}, "

        if self.ecc_curve is not None:
            result += f"ecc_curve={repr(self.ecc_curve)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CompressPublicKeyInput):
            return False
        attributes: list[str] = [
            "public_key",
            "ecc_curve",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CompressPublicKeyOutput:
    compressed_public_key: bytes | bytearray

    def __init__(
        self,
        *,
        compressed_public_key: bytes | bytearray,
    ):
        self.compressed_public_key = compressed_public_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CompressPublicKeyOutput to a dictionary."""
        return {
            "compressed_public_key": self.compressed_public_key,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CompressPublicKeyOutput":
        """Creates a CompressPublicKeyOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "compressed_public_key": d["compressed_public_key"],
        }

        return CompressPublicKeyOutput(**kwargs)

    def __repr__(self) -> str:
        result = "CompressPublicKeyOutput("
        if self.compressed_public_key is not None:
            result += f"compressed_public_key={repr(self.compressed_public_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CompressPublicKeyOutput):
            return False
        attributes: list[str] = [
            "compressed_public_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class DecompressPublicKeyInput:
    compressed_public_key: bytes | bytearray
    ecc_curve: str

    def __init__(
        self,
        *,
        compressed_public_key: bytes | bytearray,
        ecc_curve: str,
    ):
        self.compressed_public_key = compressed_public_key
        self.ecc_curve = ecc_curve

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DecompressPublicKeyInput to a dictionary."""
        return {
            "compressed_public_key": self.compressed_public_key,
            "ecc_curve": self.ecc_curve,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DecompressPublicKeyInput":
        """Creates a DecompressPublicKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "compressed_public_key": d["compressed_public_key"],
            "ecc_curve": d["ecc_curve"],
        }

        return DecompressPublicKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "DecompressPublicKeyInput("
        if self.compressed_public_key is not None:
            result += f"compressed_public_key={repr(self.compressed_public_key)}, "

        if self.ecc_curve is not None:
            result += f"ecc_curve={repr(self.ecc_curve)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DecompressPublicKeyInput):
            return False
        attributes: list[str] = [
            "compressed_public_key",
            "ecc_curve",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class DecompressPublicKeyOutput:
    public_key: ECCPublicKey

    def __init__(
        self,
        *,
        public_key: ECCPublicKey,
    ):
        self.public_key = public_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DecompressPublicKeyOutput to a dictionary."""
        return {
            "public_key": self.public_key.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DecompressPublicKeyOutput":
        """Creates a DecompressPublicKeyOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "public_key": ECCPublicKey.from_dict(d["public_key"]),
        }

        return DecompressPublicKeyOutput(**kwargs)

    def __repr__(self) -> str:
        result = "DecompressPublicKeyOutput("
        if self.public_key is not None:
            result += f"public_key={repr(self.public_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DecompressPublicKeyOutput):
            return False
        attributes: list[str] = [
            "public_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class ECCPrivateKey:
    pem: bytes | bytearray

    def __init__(
        self,
        *,
        pem: bytes | bytearray,
    ):
        self.pem = pem

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ECCPrivateKey to a dictionary."""
        return {
            "pem": self.pem,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ECCPrivateKey":
        """Creates a ECCPrivateKey from a dictionary."""
        kwargs: Dict[str, Any] = {
            "pem": d["pem"],
        }

        return ECCPrivateKey(**kwargs)

    def __repr__(self) -> str:
        result = "ECCPrivateKey("
        if self.pem is not None:
            result += f"pem={repr(self.pem)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ECCPrivateKey):
            return False
        attributes: list[str] = [
            "pem",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class DeriveSharedSecretInput:
    ecc_curve: str
    private_key: ECCPrivateKey
    public_key: ECCPublicKey

    def __init__(
        self,
        *,
        ecc_curve: str,
        private_key: ECCPrivateKey,
        public_key: ECCPublicKey,
    ):
        self.ecc_curve = ecc_curve
        self.private_key = private_key
        self.public_key = public_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DeriveSharedSecretInput to a dictionary."""
        return {
            "ecc_curve": self.ecc_curve,
            "private_key": self.private_key.as_dict(),
            "public_key": self.public_key.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DeriveSharedSecretInput":
        """Creates a DeriveSharedSecretInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "ecc_curve": d["ecc_curve"],
            "private_key": ECCPrivateKey.from_dict(d["private_key"]),
            "public_key": ECCPublicKey.from_dict(d["public_key"]),
        }

        return DeriveSharedSecretInput(**kwargs)

    def __repr__(self) -> str:
        result = "DeriveSharedSecretInput("
        if self.ecc_curve is not None:
            result += f"ecc_curve={repr(self.ecc_curve)}, "

        if self.private_key is not None:
            result += f"private_key={repr(self.private_key)}, "

        if self.public_key is not None:
            result += f"public_key={repr(self.public_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DeriveSharedSecretInput):
            return False
        attributes: list[str] = [
            "ecc_curve",
            "private_key",
            "public_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class DeriveSharedSecretOutput:
    shared_secret: bytes | bytearray

    def __init__(
        self,
        *,
        shared_secret: bytes | bytearray,
    ):
        self.shared_secret = shared_secret

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DeriveSharedSecretOutput to a dictionary."""
        return {
            "shared_secret": self.shared_secret,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DeriveSharedSecretOutput":
        """Creates a DeriveSharedSecretOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "shared_secret": d["shared_secret"],
        }

        return DeriveSharedSecretOutput(**kwargs)

    def __repr__(self) -> str:
        result = "DeriveSharedSecretOutput("
        if self.shared_secret is not None:
            result += f"shared_secret={repr(self.shared_secret)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DeriveSharedSecretOutput):
            return False
        attributes: list[str] = [
            "shared_secret",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class DigestAlgorithm:
    SHA_512 = "SHA_512"

    SHA_384 = "SHA_384"

    SHA_256 = "SHA_256"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset({"SHA_512", "SHA_384", "SHA_256"})


class DigestInput:
    digest_algorithm: str
    message: bytes | bytearray

    def __init__(
        self,
        *,
        digest_algorithm: str,
        message: bytes | bytearray,
    ):
        self.digest_algorithm = digest_algorithm
        self.message = message

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DigestInput to a dictionary."""
        return {
            "digest_algorithm": self.digest_algorithm,
            "message": self.message,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DigestInput":
        """Creates a DigestInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "digest_algorithm": d["digest_algorithm"],
            "message": d["message"],
        }

        return DigestInput(**kwargs)

    def __repr__(self) -> str:
        result = "DigestInput("
        if self.digest_algorithm is not None:
            result += f"digest_algorithm={repr(self.digest_algorithm)}, "

        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DigestInput):
            return False
        attributes: list[str] = [
            "digest_algorithm",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class ECDSASignatureAlgorithm:
    ECDSA_P384 = "ECDSA_P384"

    ECDSA_P256 = "ECDSA_P256"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset({"ECDSA_P384", "ECDSA_P256"})


class ECDSASignInput:
    signature_algorithm: str
    signing_key: bytes | bytearray
    message: bytes | bytearray

    def __init__(
        self,
        *,
        signature_algorithm: str,
        signing_key: bytes | bytearray,
        message: bytes | bytearray,
    ):
        self.signature_algorithm = signature_algorithm
        self.signing_key = signing_key
        self.message = message

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ECDSASignInput to a dictionary."""
        return {
            "signature_algorithm": self.signature_algorithm,
            "signing_key": self.signing_key,
            "message": self.message,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ECDSASignInput":
        """Creates a ECDSASignInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "signature_algorithm": d["signature_algorithm"],
            "signing_key": d["signing_key"],
            "message": d["message"],
        }

        return ECDSASignInput(**kwargs)

    def __repr__(self) -> str:
        result = "ECDSASignInput("
        if self.signature_algorithm is not None:
            result += f"signature_algorithm={repr(self.signature_algorithm)}, "

        if self.signing_key is not None:
            result += f"signing_key={repr(self.signing_key)}, "

        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ECDSASignInput):
            return False
        attributes: list[str] = [
            "signature_algorithm",
            "signing_key",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class ECDSAVerifyInput:
    signature_algorithm: str
    verification_key: bytes | bytearray
    message: bytes | bytearray
    signature: bytes | bytearray

    def __init__(
        self,
        *,
        signature_algorithm: str,
        verification_key: bytes | bytearray,
        message: bytes | bytearray,
        signature: bytes | bytearray,
    ):
        self.signature_algorithm = signature_algorithm
        self.verification_key = verification_key
        self.message = message
        self.signature = signature

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ECDSAVerifyInput to a dictionary."""
        return {
            "signature_algorithm": self.signature_algorithm,
            "verification_key": self.verification_key,
            "message": self.message,
            "signature": self.signature,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ECDSAVerifyInput":
        """Creates a ECDSAVerifyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "signature_algorithm": d["signature_algorithm"],
            "verification_key": d["verification_key"],
            "message": d["message"],
            "signature": d["signature"],
        }

        return ECDSAVerifyInput(**kwargs)

    def __repr__(self) -> str:
        result = "ECDSAVerifyInput("
        if self.signature_algorithm is not None:
            result += f"signature_algorithm={repr(self.signature_algorithm)}, "

        if self.verification_key is not None:
            result += f"verification_key={repr(self.verification_key)}, "

        if self.message is not None:
            result += f"message={repr(self.message)}, "

        if self.signature is not None:
            result += f"signature={repr(self.signature)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ECDSAVerifyInput):
            return False
        attributes: list[str] = [
            "signature_algorithm",
            "verification_key",
            "message",
            "signature",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GenerateECCKeyPairInput:
    ecc_curve: str

    def __init__(
        self,
        *,
        ecc_curve: str,
    ):
        self.ecc_curve = ecc_curve

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GenerateECCKeyPairInput to a dictionary."""
        return {
            "ecc_curve": self.ecc_curve,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GenerateECCKeyPairInput":
        """Creates a GenerateECCKeyPairInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "ecc_curve": d["ecc_curve"],
        }

        return GenerateECCKeyPairInput(**kwargs)

    def __repr__(self) -> str:
        result = "GenerateECCKeyPairInput("
        if self.ecc_curve is not None:
            result += f"ecc_curve={repr(self.ecc_curve)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GenerateECCKeyPairInput):
            return False
        attributes: list[str] = [
            "ecc_curve",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GenerateECCKeyPairOutput:
    ecc_curve: str
    private_key: ECCPrivateKey
    public_key: ECCPublicKey

    def __init__(
        self,
        *,
        ecc_curve: str,
        private_key: ECCPrivateKey,
        public_key: ECCPublicKey,
    ):
        self.ecc_curve = ecc_curve
        self.private_key = private_key
        self.public_key = public_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GenerateECCKeyPairOutput to a dictionary."""
        return {
            "ecc_curve": self.ecc_curve,
            "private_key": self.private_key.as_dict(),
            "public_key": self.public_key.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GenerateECCKeyPairOutput":
        """Creates a GenerateECCKeyPairOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "ecc_curve": d["ecc_curve"],
            "private_key": ECCPrivateKey.from_dict(d["private_key"]),
            "public_key": ECCPublicKey.from_dict(d["public_key"]),
        }

        return GenerateECCKeyPairOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GenerateECCKeyPairOutput("
        if self.ecc_curve is not None:
            result += f"ecc_curve={repr(self.ecc_curve)}, "

        if self.private_key is not None:
            result += f"private_key={repr(self.private_key)}, "

        if self.public_key is not None:
            result += f"public_key={repr(self.public_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GenerateECCKeyPairOutput):
            return False
        attributes: list[str] = [
            "ecc_curve",
            "private_key",
            "public_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GenerateECDSASignatureKeyInput:
    signature_algorithm: str

    def __init__(
        self,
        *,
        signature_algorithm: str,
    ):
        self.signature_algorithm = signature_algorithm

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GenerateECDSASignatureKeyInput to a dictionary."""
        return {
            "signature_algorithm": self.signature_algorithm,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GenerateECDSASignatureKeyInput":
        """Creates a GenerateECDSASignatureKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "signature_algorithm": d["signature_algorithm"],
        }

        return GenerateECDSASignatureKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "GenerateECDSASignatureKeyInput("
        if self.signature_algorithm is not None:
            result += f"signature_algorithm={repr(self.signature_algorithm)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GenerateECDSASignatureKeyInput):
            return False
        attributes: list[str] = [
            "signature_algorithm",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GenerateECDSASignatureKeyOutput:
    signature_algorithm: str
    verification_key: bytes | bytearray
    signing_key: bytes | bytearray

    def __init__(
        self,
        *,
        signature_algorithm: str,
        verification_key: bytes | bytearray,
        signing_key: bytes | bytearray,
    ):
        self.signature_algorithm = signature_algorithm
        self.verification_key = verification_key
        self.signing_key = signing_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GenerateECDSASignatureKeyOutput to a dictionary."""
        return {
            "signature_algorithm": self.signature_algorithm,
            "verification_key": self.verification_key,
            "signing_key": self.signing_key,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GenerateECDSASignatureKeyOutput":
        """Creates a GenerateECDSASignatureKeyOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "signature_algorithm": d["signature_algorithm"],
            "verification_key": d["verification_key"],
            "signing_key": d["signing_key"],
        }

        return GenerateECDSASignatureKeyOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GenerateECDSASignatureKeyOutput("
        if self.signature_algorithm is not None:
            result += f"signature_algorithm={repr(self.signature_algorithm)}, "

        if self.verification_key is not None:
            result += f"verification_key={repr(self.verification_key)}, "

        if self.signing_key is not None:
            result += f"signing_key={repr(self.signing_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GenerateECDSASignatureKeyOutput):
            return False
        attributes: list[str] = [
            "signature_algorithm",
            "verification_key",
            "signing_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GenerateRandomBytesInput:
    length: int

    def __init__(
        self,
        *,
        length: int = 0,
    ):
        if (length is not None) and (length < 0):
            raise ValueError("length must be greater than or equal to 0")

        self.length = length

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GenerateRandomBytesInput to a dictionary."""
        d: Dict[str, Any] = {}

        if self.length is not None:
            d["length"] = self.length

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GenerateRandomBytesInput":
        """Creates a GenerateRandomBytesInput from a dictionary."""
        kwargs: Dict[str, Any] = {}

        if "length" in d:
            kwargs["length"] = d["length"]

        return GenerateRandomBytesInput(**kwargs)

    def __repr__(self) -> str:
        result = "GenerateRandomBytesInput("
        if self.length is not None:
            result += f"length={repr(self.length)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GenerateRandomBytesInput):
            return False
        attributes: list[str] = [
            "length",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GenerateRSAKeyPairInput:
    length_bits: int

    def __init__(
        self,
        *,
        length_bits: int = 0,
    ):
        if (length_bits is not None) and (length_bits < 81):
            raise ValueError("length_bits must be greater than or equal to 81")

        if (length_bits is not None) and (length_bits > 4096):
            raise ValueError("length_bits must be less than or equal to 4096")

        self.length_bits = length_bits

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GenerateRSAKeyPairInput to a dictionary."""
        d: Dict[str, Any] = {}

        if self.length_bits is not None:
            d["length_bits"] = self.length_bits

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GenerateRSAKeyPairInput":
        """Creates a GenerateRSAKeyPairInput from a dictionary."""
        kwargs: Dict[str, Any] = {}

        if "length_bits" in d:
            kwargs["length_bits"] = d["length_bits"]

        return GenerateRSAKeyPairInput(**kwargs)

    def __repr__(self) -> str:
        result = "GenerateRSAKeyPairInput("
        if self.length_bits is not None:
            result += f"length_bits={repr(self.length_bits)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GenerateRSAKeyPairInput):
            return False
        attributes: list[str] = [
            "length_bits",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class RSAPrivateKey:
    length_bits: int
    pem: bytes | bytearray

    def __init__(
        self,
        *,
        pem: bytes | bytearray,
        length_bits: int = 0,
    ):
        self.pem = pem
        if (length_bits is not None) and (length_bits < 81):
            raise ValueError("length_bits must be greater than or equal to 81")

        self.length_bits = length_bits

    def as_dict(self) -> Dict[str, Any]:
        """Converts the RSAPrivateKey to a dictionary."""
        d: Dict[str, Any] = {
            "pem": self.pem,
        }

        if self.length_bits is not None:
            d["length_bits"] = self.length_bits

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RSAPrivateKey":
        """Creates a RSAPrivateKey from a dictionary."""
        kwargs: Dict[str, Any] = {
            "pem": d["pem"],
        }

        if "length_bits" in d:
            kwargs["length_bits"] = d["length_bits"]

        return RSAPrivateKey(**kwargs)

    def __repr__(self) -> str:
        result = "RSAPrivateKey("
        if self.length_bits is not None:
            result += f"length_bits={repr(self.length_bits)}, "

        if self.pem is not None:
            result += f"pem={repr(self.pem)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, RSAPrivateKey):
            return False
        attributes: list[str] = [
            "length_bits",
            "pem",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class RSAPublicKey:
    length_bits: int
    pem: bytes | bytearray

    def __init__(
        self,
        *,
        pem: bytes | bytearray,
        length_bits: int = 0,
    ):
        self.pem = pem
        if (length_bits is not None) and (length_bits < 81):
            raise ValueError("length_bits must be greater than or equal to 81")

        self.length_bits = length_bits

    def as_dict(self) -> Dict[str, Any]:
        """Converts the RSAPublicKey to a dictionary."""
        d: Dict[str, Any] = {
            "pem": self.pem,
        }

        if self.length_bits is not None:
            d["length_bits"] = self.length_bits

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RSAPublicKey":
        """Creates a RSAPublicKey from a dictionary."""
        kwargs: Dict[str, Any] = {
            "pem": d["pem"],
        }

        if "length_bits" in d:
            kwargs["length_bits"] = d["length_bits"]

        return RSAPublicKey(**kwargs)

    def __repr__(self) -> str:
        result = "RSAPublicKey("
        if self.length_bits is not None:
            result += f"length_bits={repr(self.length_bits)}, "

        if self.pem is not None:
            result += f"pem={repr(self.pem)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, RSAPublicKey):
            return False
        attributes: list[str] = [
            "length_bits",
            "pem",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GenerateRSAKeyPairOutput:
    public_key: RSAPublicKey
    private_key: RSAPrivateKey

    def __init__(
        self,
        *,
        public_key: RSAPublicKey,
        private_key: RSAPrivateKey,
    ):
        self.public_key = public_key
        self.private_key = private_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GenerateRSAKeyPairOutput to a dictionary."""
        return {
            "public_key": self.public_key.as_dict(),
            "private_key": self.private_key.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GenerateRSAKeyPairOutput":
        """Creates a GenerateRSAKeyPairOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "public_key": RSAPublicKey.from_dict(d["public_key"]),
            "private_key": RSAPrivateKey.from_dict(d["private_key"]),
        }

        return GenerateRSAKeyPairOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GenerateRSAKeyPairOutput("
        if self.public_key is not None:
            result += f"public_key={repr(self.public_key)}, "

        if self.private_key is not None:
            result += f"private_key={repr(self.private_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GenerateRSAKeyPairOutput):
            return False
        attributes: list[str] = [
            "public_key",
            "private_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetPublicKeyFromPrivateKeyInput:
    ecc_curve: str
    private_key: ECCPrivateKey

    def __init__(
        self,
        *,
        ecc_curve: str,
        private_key: ECCPrivateKey,
    ):
        self.ecc_curve = ecc_curve
        self.private_key = private_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetPublicKeyFromPrivateKeyInput to a dictionary."""
        return {
            "ecc_curve": self.ecc_curve,
            "private_key": self.private_key.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetPublicKeyFromPrivateKeyInput":
        """Creates a GetPublicKeyFromPrivateKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "ecc_curve": d["ecc_curve"],
            "private_key": ECCPrivateKey.from_dict(d["private_key"]),
        }

        return GetPublicKeyFromPrivateKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "GetPublicKeyFromPrivateKeyInput("
        if self.ecc_curve is not None:
            result += f"ecc_curve={repr(self.ecc_curve)}, "

        if self.private_key is not None:
            result += f"private_key={repr(self.private_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetPublicKeyFromPrivateKeyInput):
            return False
        attributes: list[str] = [
            "ecc_curve",
            "private_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetPublicKeyFromPrivateKeyOutput:
    ecc_curve: str
    private_key: ECCPrivateKey
    public_key: bytes | bytearray

    def __init__(
        self,
        *,
        ecc_curve: str,
        private_key: ECCPrivateKey,
        public_key: bytes | bytearray,
    ):
        self.ecc_curve = ecc_curve
        self.private_key = private_key
        self.public_key = public_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetPublicKeyFromPrivateKeyOutput to a dictionary."""
        return {
            "ecc_curve": self.ecc_curve,
            "private_key": self.private_key.as_dict(),
            "public_key": self.public_key,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetPublicKeyFromPrivateKeyOutput":
        """Creates a GetPublicKeyFromPrivateKeyOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "ecc_curve": d["ecc_curve"],
            "private_key": ECCPrivateKey.from_dict(d["private_key"]),
            "public_key": d["public_key"],
        }

        return GetPublicKeyFromPrivateKeyOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GetPublicKeyFromPrivateKeyOutput("
        if self.ecc_curve is not None:
            result += f"ecc_curve={repr(self.ecc_curve)}, "

        if self.private_key is not None:
            result += f"private_key={repr(self.private_key)}, "

        if self.public_key is not None:
            result += f"public_key={repr(self.public_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetPublicKeyFromPrivateKeyOutput):
            return False
        attributes: list[str] = [
            "ecc_curve",
            "private_key",
            "public_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetRSAKeyModulusLengthInput:
    public_key: bytes | bytearray

    def __init__(
        self,
        *,
        public_key: bytes | bytearray,
    ):
        self.public_key = public_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetRSAKeyModulusLengthInput to a dictionary."""
        return {
            "public_key": self.public_key,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetRSAKeyModulusLengthInput":
        """Creates a GetRSAKeyModulusLengthInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "public_key": d["public_key"],
        }

        return GetRSAKeyModulusLengthInput(**kwargs)

    def __repr__(self) -> str:
        result = "GetRSAKeyModulusLengthInput("
        if self.public_key is not None:
            result += f"public_key={repr(self.public_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetRSAKeyModulusLengthInput):
            return False
        attributes: list[str] = [
            "public_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetRSAKeyModulusLengthOutput:
    length: int

    def __init__(
        self,
        *,
        length: int = 0,
    ):
        if (length is not None) and (length < 81):
            raise ValueError("length must be greater than or equal to 81")

        self.length = length

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetRSAKeyModulusLengthOutput to a dictionary."""
        d: Dict[str, Any] = {}

        if self.length is not None:
            d["length"] = self.length

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetRSAKeyModulusLengthOutput":
        """Creates a GetRSAKeyModulusLengthOutput from a dictionary."""
        kwargs: Dict[str, Any] = {}

        if "length" in d:
            kwargs["length"] = d["length"]

        return GetRSAKeyModulusLengthOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GetRSAKeyModulusLengthOutput("
        if self.length is not None:
            result += f"length={repr(self.length)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetRSAKeyModulusLengthOutput):
            return False
        attributes: list[str] = [
            "length",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class HkdfInput:
    digest_algorithm: str
    salt: Optional[bytes | bytearray]
    ikm: bytes | bytearray
    info: bytes | bytearray
    expected_length: int

    def __init__(
        self,
        *,
        digest_algorithm: str,
        ikm: bytes | bytearray,
        info: bytes | bytearray,
        salt: Optional[bytes | bytearray] = None,
        expected_length: int = 0,
    ):
        self.digest_algorithm = digest_algorithm
        self.ikm = ikm
        self.info = info
        self.salt = salt
        if (expected_length is not None) and (expected_length < 0):
            raise ValueError("expected_length must be greater than or equal to 0")

        self.expected_length = expected_length

    def as_dict(self) -> Dict[str, Any]:
        """Converts the HkdfInput to a dictionary."""
        d: Dict[str, Any] = {
            "digest_algorithm": self.digest_algorithm,
            "ikm": self.ikm,
            "info": self.info,
        }

        if self.salt is not None:
            d["salt"] = self.salt

        if self.expected_length is not None:
            d["expected_length"] = self.expected_length

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "HkdfInput":
        """Creates a HkdfInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "digest_algorithm": d["digest_algorithm"],
            "ikm": d["ikm"],
            "info": d["info"],
        }

        if "salt" in d:
            kwargs["salt"] = d["salt"]

        if "expected_length" in d:
            kwargs["expected_length"] = d["expected_length"]

        return HkdfInput(**kwargs)

    def __repr__(self) -> str:
        result = "HkdfInput("
        if self.digest_algorithm is not None:
            result += f"digest_algorithm={repr(self.digest_algorithm)}, "

        if self.salt is not None:
            result += f"salt={repr(self.salt)}, "

        if self.ikm is not None:
            result += f"ikm={repr(self.ikm)}, "

        if self.info is not None:
            result += f"info={repr(self.info)}, "

        if self.expected_length is not None:
            result += f"expected_length={repr(self.expected_length)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, HkdfInput):
            return False
        attributes: list[str] = [
            "digest_algorithm",
            "salt",
            "ikm",
            "info",
            "expected_length",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class HkdfExpandInput:
    digest_algorithm: str
    prk: bytes | bytearray
    info: bytes | bytearray
    expected_length: int

    def __init__(
        self,
        *,
        digest_algorithm: str,
        prk: bytes | bytearray,
        info: bytes | bytearray,
        expected_length: int = 0,
    ):
        self.digest_algorithm = digest_algorithm
        self.prk = prk
        self.info = info
        if (expected_length is not None) and (expected_length < 0):
            raise ValueError("expected_length must be greater than or equal to 0")

        self.expected_length = expected_length

    def as_dict(self) -> Dict[str, Any]:
        """Converts the HkdfExpandInput to a dictionary."""
        d: Dict[str, Any] = {
            "digest_algorithm": self.digest_algorithm,
            "prk": self.prk,
            "info": self.info,
        }

        if self.expected_length is not None:
            d["expected_length"] = self.expected_length

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "HkdfExpandInput":
        """Creates a HkdfExpandInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "digest_algorithm": d["digest_algorithm"],
            "prk": d["prk"],
            "info": d["info"],
        }

        if "expected_length" in d:
            kwargs["expected_length"] = d["expected_length"]

        return HkdfExpandInput(**kwargs)

    def __repr__(self) -> str:
        result = "HkdfExpandInput("
        if self.digest_algorithm is not None:
            result += f"digest_algorithm={repr(self.digest_algorithm)}, "

        if self.prk is not None:
            result += f"prk={repr(self.prk)}, "

        if self.info is not None:
            result += f"info={repr(self.info)}, "

        if self.expected_length is not None:
            result += f"expected_length={repr(self.expected_length)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, HkdfExpandInput):
            return False
        attributes: list[str] = [
            "digest_algorithm",
            "prk",
            "info",
            "expected_length",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class HkdfExtractInput:
    digest_algorithm: str
    salt: Optional[bytes | bytearray]
    ikm: bytes | bytearray

    def __init__(
        self,
        *,
        digest_algorithm: str,
        ikm: bytes | bytearray,
        salt: Optional[bytes | bytearray] = None,
    ):
        self.digest_algorithm = digest_algorithm
        self.ikm = ikm
        self.salt = salt

    def as_dict(self) -> Dict[str, Any]:
        """Converts the HkdfExtractInput to a dictionary."""
        d: Dict[str, Any] = {
            "digest_algorithm": self.digest_algorithm,
            "ikm": self.ikm,
        }

        if self.salt is not None:
            d["salt"] = self.salt

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "HkdfExtractInput":
        """Creates a HkdfExtractInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "digest_algorithm": d["digest_algorithm"],
            "ikm": d["ikm"],
        }

        if "salt" in d:
            kwargs["salt"] = d["salt"]

        return HkdfExtractInput(**kwargs)

    def __repr__(self) -> str:
        result = "HkdfExtractInput("
        if self.digest_algorithm is not None:
            result += f"digest_algorithm={repr(self.digest_algorithm)}, "

        if self.salt is not None:
            result += f"salt={repr(self.salt)}, "

        if self.ikm is not None:
            result += f"ikm={repr(self.ikm)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, HkdfExtractInput):
            return False
        attributes: list[str] = [
            "digest_algorithm",
            "salt",
            "ikm",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class HMacInput:
    digest_algorithm: str
    key: bytes | bytearray
    message: bytes | bytearray

    def __init__(
        self,
        *,
        digest_algorithm: str,
        key: bytes | bytearray,
        message: bytes | bytearray,
    ):
        self.digest_algorithm = digest_algorithm
        self.key = key
        self.message = message

    def as_dict(self) -> Dict[str, Any]:
        """Converts the HMacInput to a dictionary."""
        return {
            "digest_algorithm": self.digest_algorithm,
            "key": self.key,
            "message": self.message,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "HMacInput":
        """Creates a HMacInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "digest_algorithm": d["digest_algorithm"],
            "key": d["key"],
            "message": d["message"],
        }

        return HMacInput(**kwargs)

    def __repr__(self) -> str:
        result = "HMacInput("
        if self.digest_algorithm is not None:
            result += f"digest_algorithm={repr(self.digest_algorithm)}, "

        if self.key is not None:
            result += f"key={repr(self.key)}, "

        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, HMacInput):
            return False
        attributes: list[str] = [
            "digest_algorithm",
            "key",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class KdfCtrInput:
    digest_algorithm: str
    ikm: bytes | bytearray
    expected_length: int
    purpose: Optional[bytes | bytearray]
    nonce: Optional[bytes | bytearray]

    def __init__(
        self,
        *,
        digest_algorithm: str,
        ikm: bytes | bytearray,
        expected_length: int = 0,
        purpose: Optional[bytes | bytearray] = None,
        nonce: Optional[bytes | bytearray] = None,
    ):
        self.digest_algorithm = digest_algorithm
        self.ikm = ikm
        if (expected_length is not None) and (expected_length < 0):
            raise ValueError("expected_length must be greater than or equal to 0")

        self.expected_length = expected_length
        self.purpose = purpose
        self.nonce = nonce

    def as_dict(self) -> Dict[str, Any]:
        """Converts the KdfCtrInput to a dictionary."""
        d: Dict[str, Any] = {
            "digest_algorithm": self.digest_algorithm,
            "ikm": self.ikm,
        }

        if self.expected_length is not None:
            d["expected_length"] = self.expected_length

        if self.purpose is not None:
            d["purpose"] = self.purpose

        if self.nonce is not None:
            d["nonce"] = self.nonce

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KdfCtrInput":
        """Creates a KdfCtrInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "digest_algorithm": d["digest_algorithm"],
            "ikm": d["ikm"],
        }

        if "expected_length" in d:
            kwargs["expected_length"] = d["expected_length"]

        if "purpose" in d:
            kwargs["purpose"] = d["purpose"]

        if "nonce" in d:
            kwargs["nonce"] = d["nonce"]

        return KdfCtrInput(**kwargs)

    def __repr__(self) -> str:
        result = "KdfCtrInput("
        if self.digest_algorithm is not None:
            result += f"digest_algorithm={repr(self.digest_algorithm)}, "

        if self.ikm is not None:
            result += f"ikm={repr(self.ikm)}, "

        if self.expected_length is not None:
            result += f"expected_length={repr(self.expected_length)}, "

        if self.purpose is not None:
            result += f"purpose={repr(self.purpose)}, "

        if self.nonce is not None:
            result += f"nonce={repr(self.nonce)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KdfCtrInput):
            return False
        attributes: list[str] = [
            "digest_algorithm",
            "ikm",
            "expected_length",
            "purpose",
            "nonce",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class ParsePublicKeyInput:
    public_key: bytes | bytearray

    def __init__(
        self,
        *,
        public_key: bytes | bytearray,
    ):
        self.public_key = public_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ParsePublicKeyInput to a dictionary."""
        return {
            "public_key": self.public_key,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ParsePublicKeyInput":
        """Creates a ParsePublicKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "public_key": d["public_key"],
        }

        return ParsePublicKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "ParsePublicKeyInput("
        if self.public_key is not None:
            result += f"public_key={repr(self.public_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ParsePublicKeyInput):
            return False
        attributes: list[str] = [
            "public_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class ParsePublicKeyOutput:
    public_key: ECCPublicKey

    def __init__(
        self,
        *,
        public_key: ECCPublicKey,
    ):
        self.public_key = public_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ParsePublicKeyOutput to a dictionary."""
        return {
            "public_key": self.public_key.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ParsePublicKeyOutput":
        """Creates a ParsePublicKeyOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "public_key": ECCPublicKey.from_dict(d["public_key"]),
        }

        return ParsePublicKeyOutput(**kwargs)

    def __repr__(self) -> str:
        result = "ParsePublicKeyOutput("
        if self.public_key is not None:
            result += f"public_key={repr(self.public_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ParsePublicKeyOutput):
            return False
        attributes: list[str] = [
            "public_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class RSAPaddingMode:
    PKCS1 = "PKCS1"

    OAEP_SHA1 = "OAEP_SHA1"

    OAEP_SHA256 = "OAEP_SHA256"

    OAEP_SHA384 = "OAEP_SHA384"

    OAEP_SHA512 = "OAEP_SHA512"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset(
        {"PKCS1", "OAEP_SHA1", "OAEP_SHA256", "OAEP_SHA384", "OAEP_SHA512"}
    )


class RSADecryptInput:
    padding: str
    private_key: bytes | bytearray
    cipher_text: bytes | bytearray

    def __init__(
        self,
        *,
        padding: str,
        private_key: bytes | bytearray,
        cipher_text: bytes | bytearray,
    ):
        self.padding = padding
        self.private_key = private_key
        self.cipher_text = cipher_text

    def as_dict(self) -> Dict[str, Any]:
        """Converts the RSADecryptInput to a dictionary."""
        return {
            "padding": self.padding,
            "private_key": self.private_key,
            "cipher_text": self.cipher_text,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RSADecryptInput":
        """Creates a RSADecryptInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "padding": d["padding"],
            "private_key": d["private_key"],
            "cipher_text": d["cipher_text"],
        }

        return RSADecryptInput(**kwargs)

    def __repr__(self) -> str:
        result = "RSADecryptInput("
        if self.padding is not None:
            result += f"padding={repr(self.padding)}, "

        if self.private_key is not None:
            result += f"private_key={repr(self.private_key)}, "

        if self.cipher_text is not None:
            result += f"cipher_text={repr(self.cipher_text)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, RSADecryptInput):
            return False
        attributes: list[str] = [
            "padding",
            "private_key",
            "cipher_text",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class RSAEncryptInput:
    padding: str
    public_key: bytes | bytearray
    plaintext: bytes | bytearray

    def __init__(
        self,
        *,
        padding: str,
        public_key: bytes | bytearray,
        plaintext: bytes | bytearray,
    ):
        self.padding = padding
        self.public_key = public_key
        self.plaintext = plaintext

    def as_dict(self) -> Dict[str, Any]:
        """Converts the RSAEncryptInput to a dictionary."""
        return {
            "padding": self.padding,
            "public_key": self.public_key,
            "plaintext": self.plaintext,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RSAEncryptInput":
        """Creates a RSAEncryptInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "padding": d["padding"],
            "public_key": d["public_key"],
            "plaintext": d["plaintext"],
        }

        return RSAEncryptInput(**kwargs)

    def __repr__(self) -> str:
        result = "RSAEncryptInput("
        if self.padding is not None:
            result += f"padding={repr(self.padding)}, "

        if self.public_key is not None:
            result += f"public_key={repr(self.public_key)}, "

        if self.plaintext is not None:
            result += f"plaintext={repr(self.plaintext)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, RSAEncryptInput):
            return False
        attributes: list[str] = [
            "padding",
            "public_key",
            "plaintext",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class ValidatePublicKeyInput:
    ecc_curve: str
    public_key: bytes | bytearray

    def __init__(
        self,
        *,
        ecc_curve: str,
        public_key: bytes | bytearray,
    ):
        self.ecc_curve = ecc_curve
        self.public_key = public_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ValidatePublicKeyInput to a dictionary."""
        return {
            "ecc_curve": self.ecc_curve,
            "public_key": self.public_key,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ValidatePublicKeyInput":
        """Creates a ValidatePublicKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "ecc_curve": d["ecc_curve"],
            "public_key": d["public_key"],
        }

        return ValidatePublicKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "ValidatePublicKeyInput("
        if self.ecc_curve is not None:
            result += f"ecc_curve={repr(self.ecc_curve)}, "

        if self.public_key is not None:
            result += f"public_key={repr(self.public_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ValidatePublicKeyInput):
            return False
        attributes: list[str] = [
            "ecc_curve",
            "public_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class ValidatePublicKeyOutput:
    success: bool

    def __init__(
        self,
        *,
        success: bool,
    ):
        self.success = success

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ValidatePublicKeyOutput to a dictionary."""
        return {
            "success": self.success,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ValidatePublicKeyOutput":
        """Creates a ValidatePublicKeyOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "success": d["success"],
        }

        return ValidatePublicKeyOutput(**kwargs)

    def __repr__(self) -> str:
        result = "ValidatePublicKeyOutput("
        if self.success is not None:
            result += f"success={repr(self.success)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ValidatePublicKeyOutput):
            return False
        attributes: list[str] = [
            "success",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class AES_CTR:
    key_length: int
    nonce_length: int

    def __init__(
        self,
        *,
        key_length: int = 0,
        nonce_length: int = 0,
    ):
        if (key_length is not None) and (key_length < 1):
            raise ValueError("key_length must be greater than or equal to 1")

        if (key_length is not None) and (key_length > 32):
            raise ValueError("key_length must be less than or equal to 32")

        self.key_length = key_length
        if (nonce_length is not None) and (nonce_length < 0):
            raise ValueError("nonce_length must be greater than or equal to 0")

        if (nonce_length is not None) and (nonce_length > 255):
            raise ValueError("nonce_length must be less than or equal to 255")

        self.nonce_length = nonce_length

    def as_dict(self) -> Dict[str, Any]:
        """Converts the AES_CTR to a dictionary."""
        d: Dict[str, Any] = {}

        if self.key_length is not None:
            d["key_length"] = self.key_length

        if self.nonce_length is not None:
            d["nonce_length"] = self.nonce_length

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AES_CTR":
        """Creates a AES_CTR from a dictionary."""
        kwargs: Dict[str, Any] = {}

        if "key_length" in d:
            kwargs["key_length"] = d["key_length"]

        if "nonce_length" in d:
            kwargs["nonce_length"] = d["nonce_length"]

        return AES_CTR(**kwargs)

    def __repr__(self) -> str:
        result = "AES_CTR("
        if self.key_length is not None:
            result += f"key_length={repr(self.key_length)}, "

        if self.nonce_length is not None:
            result += f"nonce_length={repr(self.nonce_length)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AES_CTR):
            return False
        attributes: list[str] = [
            "key_length",
            "nonce_length",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class Unit:
    pass
