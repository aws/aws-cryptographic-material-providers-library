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
        """Converts the AES_GCM to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {}

        if self.key_length is not None:
            d["keyLength"] = self.key_length

        if self.tag_length is not None:
            d["tagLength"] = self.tag_length

        if self.iv_length is not None:
            d["ivLength"] = self.iv_length

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AES_GCM":
        """Creates a AES_GCM from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {}

        if "keyLength" in d:
            kwargs["key_length"] = d["keyLength"]

        if "tagLength" in d:
            kwargs["tag_length"] = d["tagLength"]

        if "ivLength" in d:
            kwargs["iv_length"] = d["ivLength"]

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
        attributes: list[str] = ['key_length','tag_length','iv_length',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the AESDecryptInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "encAlg": self.enc_alg.as_dict(),
            "key": self.key,
            "cipherTxt": self.cipher_txt,
            "authTag": self.auth_tag,
            "iv": self.iv,
            "aad": self.aad,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AESDecryptInput":
        """Creates a AESDecryptInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "enc_alg": AES_GCM.from_dict(d["encAlg"]),
            "key": d["key"],
            "cipher_txt": d["cipherTxt"],
            "auth_tag": d["authTag"],
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
        attributes: list[str] = ['enc_alg','key','cipher_txt','auth_tag','iv','aad',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the AESEncryptInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "encAlg": self.enc_alg.as_dict(),
            "iv": self.iv,
            "key": self.key,
            "msg": self.msg,
            "aad": self.aad,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AESEncryptInput":
        """Creates a AESEncryptInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "enc_alg": AES_GCM.from_dict(d["encAlg"]),
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
        attributes: list[str] = ['enc_alg','iv','key','msg','aad',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the AESEncryptOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "cipherText": self.cipher_text,
            "authTag": self.auth_tag,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AESEncryptOutput":
        """Creates a AESEncryptOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "cipher_text": d["cipherText"],
            "auth_tag": d["authTag"],
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
        attributes: list[str] = ['cipher_text','auth_tag',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the AesKdfCtrInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "ikm": self.ikm,
        }

        if self.expected_length is not None:
            d["expectedLength"] = self.expected_length

        if self.nonce is not None:
            d["nonce"] = self.nonce

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AesKdfCtrInput":
        """Creates a AesKdfCtrInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "ikm": d["ikm"],
        }

        if "expectedLength" in d:
            kwargs["expected_length"] = d["expectedLength"]

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
        attributes: list[str] = ['ikm','expected_length','nonce',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the DigestInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "digestAlgorithm": self.digest_algorithm,
            "message": self.message,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DigestInput":
        """Creates a DigestInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "digest_algorithm": d["digestAlgorithm"],
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
        attributes: list[str] = ['digest_algorithm','message',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the ECDSASignInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "signatureAlgorithm": self.signature_algorithm,
            "signingKey": self.signing_key,
            "message": self.message,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ECDSASignInput":
        """Creates a ECDSASignInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "signature_algorithm": d["signatureAlgorithm"],
            "signing_key": d["signingKey"],
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
        attributes: list[str] = ['signature_algorithm','signing_key','message',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the ECDSAVerifyInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "signatureAlgorithm": self.signature_algorithm,
            "verificationKey": self.verification_key,
            "message": self.message,
            "signature": self.signature,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ECDSAVerifyInput":
        """Creates a ECDSAVerifyInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "signature_algorithm": d["signatureAlgorithm"],
            "verification_key": d["verificationKey"],
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
        attributes: list[str] = ['signature_algorithm','verification_key','message','signature',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class GenerateECDSASignatureKeyInput:
    signature_algorithm: str
    def __init__(
        self,
        *,
        signature_algorithm: str,
    ):
        self.signature_algorithm = signature_algorithm

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GenerateECDSASignatureKeyInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "signatureAlgorithm": self.signature_algorithm,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GenerateECDSASignatureKeyInput":
        """Creates a GenerateECDSASignatureKeyInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "signature_algorithm": d["signatureAlgorithm"],
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
        attributes: list[str] = ['signature_algorithm',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the GenerateECDSASignatureKeyOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "signatureAlgorithm": self.signature_algorithm,
            "verificationKey": self.verification_key,
            "signingKey": self.signing_key,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GenerateECDSASignatureKeyOutput":
        """Creates a GenerateECDSASignatureKeyOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "signature_algorithm": d["signatureAlgorithm"],
            "verification_key": d["verificationKey"],
            "signing_key": d["signingKey"],
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
        attributes: list[str] = ['signature_algorithm','verification_key','signing_key',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the GenerateRandomBytesInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {}

        if self.length is not None:
            d["length"] = self.length

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GenerateRandomBytesInput":
        """Creates a GenerateRandomBytesInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
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
        attributes: list[str] = ['length',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the GenerateRSAKeyPairInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {}

        if self.length_bits is not None:
            d["lengthBits"] = self.length_bits

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GenerateRSAKeyPairInput":
        """Creates a GenerateRSAKeyPairInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {}

        if "lengthBits" in d:
            kwargs["length_bits"] = d["lengthBits"]

        return GenerateRSAKeyPairInput(**kwargs)

    def __repr__(self) -> str:
        result = "GenerateRSAKeyPairInput("
        if self.length_bits is not None:
            result += f"length_bits={repr(self.length_bits)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GenerateRSAKeyPairInput):
            return False
        attributes: list[str] = ['length_bits',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the RSAPrivateKey to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "pem": self.pem,
        }

        if self.length_bits is not None:
            d["lengthBits"] = self.length_bits

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RSAPrivateKey":
        """Creates a RSAPrivateKey from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "pem": d["pem"],
        }

        if "lengthBits" in d:
            kwargs["length_bits"] = d["lengthBits"]

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
        attributes: list[str] = ['length_bits','pem',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the RSAPublicKey to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "pem": self.pem,
        }

        if self.length_bits is not None:
            d["lengthBits"] = self.length_bits

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RSAPublicKey":
        """Creates a RSAPublicKey from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "pem": d["pem"],
        }

        if "lengthBits" in d:
            kwargs["length_bits"] = d["lengthBits"]

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
        attributes: list[str] = ['length_bits','pem',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the GenerateRSAKeyPairOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "publicKey": self.public_key.as_dict(),
            "privateKey": self.private_key.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GenerateRSAKeyPairOutput":
        """Creates a GenerateRSAKeyPairOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "public_key": RSAPublicKey.from_dict(d["publicKey"]),
            "private_key": RSAPrivateKey.from_dict(d["privateKey"]),
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
        attributes: list[str] = ['public_key','private_key',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class GetRSAKeyModulusLengthInput:
    public_key: bytes | bytearray
    def __init__(
        self,
        *,
        public_key: bytes | bytearray,
    ):
        self.public_key = public_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetRSAKeyModulusLengthInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "publicKey": self.public_key,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetRSAKeyModulusLengthInput":
        """Creates a GetRSAKeyModulusLengthInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "public_key": d["publicKey"],
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
        attributes: list[str] = ['public_key',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the GetRSAKeyModulusLengthOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {}

        if self.length is not None:
            d["length"] = self.length

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetRSAKeyModulusLengthOutput":
        """Creates a GetRSAKeyModulusLengthOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
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
        attributes: list[str] = ['length',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the HkdfInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "digestAlgorithm": self.digest_algorithm,
            "ikm": self.ikm,
            "info": self.info,
        }

        if self.salt is not None:
            d["salt"] = self.salt

        if self.expected_length is not None:
            d["expectedLength"] = self.expected_length

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "HkdfInput":
        """Creates a HkdfInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "digest_algorithm": d["digestAlgorithm"],
            "ikm": d["ikm"],
            "info": d["info"],
        }

        if "salt" in d:
            kwargs["salt"] = d["salt"]

        if "expectedLength" in d:
            kwargs["expected_length"] = d["expectedLength"]

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
        attributes: list[str] = ['digest_algorithm','salt','ikm','info','expected_length',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the HkdfExpandInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "digestAlgorithm": self.digest_algorithm,
            "prk": self.prk,
            "info": self.info,
        }

        if self.expected_length is not None:
            d["expectedLength"] = self.expected_length

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "HkdfExpandInput":
        """Creates a HkdfExpandInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "digest_algorithm": d["digestAlgorithm"],
            "prk": d["prk"],
            "info": d["info"],
        }

        if "expectedLength" in d:
            kwargs["expected_length"] = d["expectedLength"]

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
        attributes: list[str] = ['digest_algorithm','prk','info','expected_length',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the HkdfExtractInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "digestAlgorithm": self.digest_algorithm,
            "ikm": self.ikm,
        }

        if self.salt is not None:
            d["salt"] = self.salt

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "HkdfExtractInput":
        """Creates a HkdfExtractInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "digest_algorithm": d["digestAlgorithm"],
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
        attributes: list[str] = ['digest_algorithm','salt','ikm',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the HMacInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "digestAlgorithm": self.digest_algorithm,
            "key": self.key,
            "message": self.message,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "HMacInput":
        """Creates a HMacInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "digest_algorithm": d["digestAlgorithm"],
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
        attributes: list[str] = ['digest_algorithm','key','message',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the KdfCtrInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "digestAlgorithm": self.digest_algorithm,
            "ikm": self.ikm,
        }

        if self.expected_length is not None:
            d["expectedLength"] = self.expected_length

        if self.purpose is not None:
            d["purpose"] = self.purpose

        if self.nonce is not None:
            d["nonce"] = self.nonce

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KdfCtrInput":
        """Creates a KdfCtrInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "digest_algorithm": d["digestAlgorithm"],
            "ikm": d["ikm"],
        }

        if "expectedLength" in d:
            kwargs["expected_length"] = d["expectedLength"]

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
        attributes: list[str] = ['digest_algorithm','ikm','expected_length','purpose','nonce',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class RSAPaddingMode:
    PKCS1 = "PKCS1"

    OAEP_SHA1 = "OAEP_SHA1"

    OAEP_SHA256 = "OAEP_SHA256"

    OAEP_SHA384 = "OAEP_SHA384"

    OAEP_SHA512 = "OAEP_SHA512"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset({"PKCS1", "OAEP_SHA1", "OAEP_SHA256", "OAEP_SHA384", "OAEP_SHA512"})

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
        """Converts the RSADecryptInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "padding": self.padding,
            "privateKey": self.private_key,
            "cipherText": self.cipher_text,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RSADecryptInput":
        """Creates a RSADecryptInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "padding": d["padding"],
            "private_key": d["privateKey"],
            "cipher_text": d["cipherText"],
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
        attributes: list[str] = ['padding','private_key','cipher_text',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the RSAEncryptInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "padding": self.padding,
            "publicKey": self.public_key,
            "plaintext": self.plaintext,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RSAEncryptInput":
        """Creates a RSAEncryptInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "padding": d["padding"],
            "public_key": d["publicKey"],
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
        attributes: list[str] = ['padding','public_key','plaintext',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class Unit:
    pass
