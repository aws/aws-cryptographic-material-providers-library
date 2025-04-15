# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.client
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references
from typing import Any, Dict, List, Optional, Union

from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models import (
    AES_GCM,
)
from botocore.client import BaseClient

from ..aws_cryptography_keystore.models import BeaconKeyMaterials, BranchKeyMaterials


class AesWrappingAlg:
    ALG_AES128_GCM_IV12_TAG16 = "ALG_AES128_GCM_IV12_TAG16"

    ALG_AES192_GCM_IV12_TAG16 = "ALG_AES192_GCM_IV12_TAG16"

    ALG_AES256_GCM_IV12_TAG16 = "ALG_AES256_GCM_IV12_TAG16"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset(
        {
            "ALG_AES128_GCM_IV12_TAG16",
            "ALG_AES192_GCM_IV12_TAG16",
            "ALG_AES256_GCM_IV12_TAG16",
        }
    )


class DBEAlgorithmSuiteId:
    ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_SYMSIG_HMAC_SHA384 = "0x6700"

    ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_ECDSA_P384_SYMSIG_HMAC_SHA384 = "0x6701"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset({"0x6700", "0x6701"})


class ESDKAlgorithmSuiteId:
    ALG_AES_128_GCM_IV12_TAG16_NO_KDF = "0x0014"

    ALG_AES_192_GCM_IV12_TAG16_NO_KDF = "0x0046"

    ALG_AES_256_GCM_IV12_TAG16_NO_KDF = "0x0078"

    ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256 = "0x0114"

    ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA256 = "0x0146"

    ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA256 = "0x0178"

    ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256_ECDSA_P256 = "0x0214"

    ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384 = "0x0346"

    ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384 = "0x0378"

    ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY = "0x0478"

    ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_ECDSA_P384 = "0x0578"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset(
        {
            "0x0014",
            "0x0046",
            "0x0078",
            "0x0114",
            "0x0146",
            "0x0178",
            "0x0214",
            "0x0346",
            "0x0378",
            "0x0478",
            "0x0578",
        }
    )


class AlgorithmSuiteIdESDK:
    def __init__(self, value: str):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"ESDK": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AlgorithmSuiteIdESDK":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return AlgorithmSuiteIdESDK(d["ESDK"])

    def __repr__(self) -> str:
        return f"AlgorithmSuiteIdESDK(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AlgorithmSuiteIdESDK):
            return False
        return self.value == other.value


class AlgorithmSuiteIdDBE:
    def __init__(self, value: str):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"DBE": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AlgorithmSuiteIdDBE":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return AlgorithmSuiteIdDBE(d["DBE"])

    def __repr__(self) -> str:
        return f"AlgorithmSuiteIdDBE(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AlgorithmSuiteIdDBE):
            return False
        return self.value == other.value


class AlgorithmSuiteIdUnknown:
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to
    receive the parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AlgorithmSuiteIdUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return AlgorithmSuiteIdUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"AlgorithmSuiteIdUnknown(tag={self.tag})"


AlgorithmSuiteId = Union[
    AlgorithmSuiteIdESDK, AlgorithmSuiteIdDBE, AlgorithmSuiteIdUnknown
]


def _algorithm_suite_id_from_dict(d: Dict[str, Any]) -> AlgorithmSuiteId:
    if "ESDK" in d:
        return AlgorithmSuiteIdESDK.from_dict(d)

    if "DBE" in d:
        return AlgorithmSuiteIdDBE.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class HKDF:
    hmac: str
    salt_length: int
    input_key_length: int
    output_key_length: int

    def __init__(
        self,
        *,
        hmac: str,
        salt_length: int = 0,
        input_key_length: int = 0,
        output_key_length: int = 0,
    ):
        self.hmac = hmac
        if (salt_length is not None) and (salt_length < 0):
            raise ValueError("salt_length must be greater than or equal to 0")

        self.salt_length = salt_length
        if (input_key_length is not None) and (input_key_length < 1):
            raise ValueError("input_key_length must be greater than or equal to 1")

        if (input_key_length is not None) and (input_key_length > 32):
            raise ValueError("input_key_length must be less than or equal to 32")

        self.input_key_length = input_key_length
        if (output_key_length is not None) and (output_key_length < 1):
            raise ValueError("output_key_length must be greater than or equal to 1")

        if (output_key_length is not None) and (output_key_length > 32):
            raise ValueError("output_key_length must be less than or equal to 32")

        self.output_key_length = output_key_length

    def as_dict(self) -> Dict[str, Any]:
        """Converts the HKDF to a dictionary."""
        d: Dict[str, Any] = {
            "hmac": self.hmac,
        }

        if self.salt_length is not None:
            d["salt_length"] = self.salt_length

        if self.input_key_length is not None:
            d["input_key_length"] = self.input_key_length

        if self.output_key_length is not None:
            d["output_key_length"] = self.output_key_length

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "HKDF":
        """Creates a HKDF from a dictionary."""
        kwargs: Dict[str, Any] = {
            "hmac": d["hmac"],
        }

        if "salt_length" in d:
            kwargs["salt_length"] = d["salt_length"]

        if "input_key_length" in d:
            kwargs["input_key_length"] = d["input_key_length"]

        if "output_key_length" in d:
            kwargs["output_key_length"] = d["output_key_length"]

        return HKDF(**kwargs)

    def __repr__(self) -> str:
        result = "HKDF("
        if self.hmac is not None:
            result += f"hmac={repr(self.hmac)}, "

        if self.salt_length is not None:
            result += f"salt_length={repr(self.salt_length)}, "

        if self.input_key_length is not None:
            result += f"input_key_length={repr(self.input_key_length)}, "

        if self.output_key_length is not None:
            result += f"output_key_length={repr(self.output_key_length)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, HKDF):
            return False
        attributes: list[str] = [
            "hmac",
            "salt_length",
            "input_key_length",
            "output_key_length",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class IDENTITY:
    def as_dict(self) -> Dict[str, Any]:
        """Converts the IDENTITY to a dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "IDENTITY":
        """Creates a IDENTITY from a dictionary."""
        return IDENTITY()

    def __repr__(self) -> str:
        result = "IDENTITY("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, IDENTITY)


class None_:
    def as_dict(self) -> Dict[str, Any]:
        """Converts the None_ to a dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "None_":
        """Creates a None_ from a dictionary."""
        return None_()

    def __repr__(self) -> str:
        result = "None_("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, None_)


class DerivationAlgorithmHKDF:
    def __init__(self, value: HKDF):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"HKDF": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DerivationAlgorithmHKDF":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return DerivationAlgorithmHKDF(HKDF.from_dict(d["HKDF"]))

    def __repr__(self) -> str:
        return f"DerivationAlgorithmHKDF(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DerivationAlgorithmHKDF):
            return False
        return self.value == other.value


class DerivationAlgorithmIDENTITY:
    def __init__(self, value: IDENTITY):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"IDENTITY": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DerivationAlgorithmIDENTITY":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return DerivationAlgorithmIDENTITY(IDENTITY.from_dict(d["IDENTITY"]))

    def __repr__(self) -> str:
        return f"DerivationAlgorithmIDENTITY(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DerivationAlgorithmIDENTITY):
            return False
        return self.value == other.value


class DerivationAlgorithmNone:
    def __init__(self, value: None_):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"None": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DerivationAlgorithmNone":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return DerivationAlgorithmNone(None_.from_dict(d["None"]))

    def __repr__(self) -> str:
        return f"DerivationAlgorithmNone(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DerivationAlgorithmNone):
            return False
        return self.value == other.value


class DerivationAlgorithmUnknown:
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to
    receive the parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DerivationAlgorithmUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return DerivationAlgorithmUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"DerivationAlgorithmUnknown(tag={self.tag})"


DerivationAlgorithm = Union[
    DerivationAlgorithmHKDF,
    DerivationAlgorithmIDENTITY,
    DerivationAlgorithmNone,
    DerivationAlgorithmUnknown,
]


def _derivation_algorithm_from_dict(d: Dict[str, Any]) -> DerivationAlgorithm:
    if "HKDF" in d:
        return DerivationAlgorithmHKDF.from_dict(d)

    if "IDENTITY" in d:
        return DerivationAlgorithmIDENTITY.from_dict(d)

    if "None" in d:
        return DerivationAlgorithmNone.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class DIRECT_KEY_WRAPPING:
    def as_dict(self) -> Dict[str, Any]:
        """Converts the DIRECT_KEY_WRAPPING to a dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DIRECT_KEY_WRAPPING":
        """Creates a DIRECT_KEY_WRAPPING from a dictionary."""
        return DIRECT_KEY_WRAPPING()

    def __repr__(self) -> str:
        result = "DIRECT_KEY_WRAPPING("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, DIRECT_KEY_WRAPPING)


class EncryptAES_GCM:
    def __init__(self, value: AES_GCM):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"AES_GCM": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EncryptAES_GCM":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return EncryptAES_GCM(AES_GCM.from_dict(d["AES_GCM"]))

    def __repr__(self) -> str:
        return f"EncryptAES_GCM(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EncryptAES_GCM):
            return False
        return self.value == other.value


class EncryptUnknown:
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to
    receive the parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EncryptUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return EncryptUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"EncryptUnknown(tag={self.tag})"


Encrypt = Union[EncryptAES_GCM, EncryptUnknown]


def _encrypt_from_dict(d: Dict[str, Any]) -> Encrypt:
    if "AES_GCM" in d:
        return EncryptAES_GCM.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class IntermediateKeyWrapping:
    key_encryption_key_kdf: DerivationAlgorithm
    mac_key_kdf: DerivationAlgorithm
    pdk_encrypt_algorithm: Encrypt

    def __init__(
        self,
        *,
        key_encryption_key_kdf: DerivationAlgorithm,
        mac_key_kdf: DerivationAlgorithm,
        pdk_encrypt_algorithm: Encrypt,
    ):
        self.key_encryption_key_kdf = key_encryption_key_kdf
        self.mac_key_kdf = mac_key_kdf
        self.pdk_encrypt_algorithm = pdk_encrypt_algorithm

    def as_dict(self) -> Dict[str, Any]:
        """Converts the IntermediateKeyWrapping to a dictionary."""
        return {
            "key_encryption_key_kdf": self.key_encryption_key_kdf.as_dict(),
            "mac_key_kdf": self.mac_key_kdf.as_dict(),
            "pdk_encrypt_algorithm": self.pdk_encrypt_algorithm.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "IntermediateKeyWrapping":
        """Creates a IntermediateKeyWrapping from a dictionary."""
        kwargs: Dict[str, Any] = {
            "key_encryption_key_kdf": _derivation_algorithm_from_dict(
                d["key_encryption_key_kdf"]
            ),
            "mac_key_kdf": _derivation_algorithm_from_dict(d["mac_key_kdf"]),
            "pdk_encrypt_algorithm": _encrypt_from_dict(d["pdk_encrypt_algorithm"]),
        }

        return IntermediateKeyWrapping(**kwargs)

    def __repr__(self) -> str:
        result = "IntermediateKeyWrapping("
        if self.key_encryption_key_kdf is not None:
            result += f"key_encryption_key_kdf={repr(self.key_encryption_key_kdf)}, "

        if self.mac_key_kdf is not None:
            result += f"mac_key_kdf={repr(self.mac_key_kdf)}, "

        if self.pdk_encrypt_algorithm is not None:
            result += f"pdk_encrypt_algorithm={repr(self.pdk_encrypt_algorithm)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, IntermediateKeyWrapping):
            return False
        attributes: list[str] = [
            "key_encryption_key_kdf",
            "mac_key_kdf",
            "pdk_encrypt_algorithm",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class EdkWrappingAlgorithmDIRECT_KEY_WRAPPING:
    def __init__(self, value: DIRECT_KEY_WRAPPING):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"DIRECT_KEY_WRAPPING": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EdkWrappingAlgorithmDIRECT_KEY_WRAPPING":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return EdkWrappingAlgorithmDIRECT_KEY_WRAPPING(
            DIRECT_KEY_WRAPPING.from_dict(d["DIRECT_KEY_WRAPPING"])
        )

    def __repr__(self) -> str:
        return f"EdkWrappingAlgorithmDIRECT_KEY_WRAPPING(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EdkWrappingAlgorithmDIRECT_KEY_WRAPPING):
            return False
        return self.value == other.value


class EdkWrappingAlgorithmIntermediateKeyWrapping:
    def __init__(self, value: IntermediateKeyWrapping):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"IntermediateKeyWrapping": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EdkWrappingAlgorithmIntermediateKeyWrapping":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return EdkWrappingAlgorithmIntermediateKeyWrapping(
            IntermediateKeyWrapping.from_dict(d["IntermediateKeyWrapping"])
        )

    def __repr__(self) -> str:
        return f"EdkWrappingAlgorithmIntermediateKeyWrapping(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EdkWrappingAlgorithmIntermediateKeyWrapping):
            return False
        return self.value == other.value


class EdkWrappingAlgorithmUnknown:
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to
    receive the parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EdkWrappingAlgorithmUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return EdkWrappingAlgorithmUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"EdkWrappingAlgorithmUnknown(tag={self.tag})"


EdkWrappingAlgorithm = Union[
    EdkWrappingAlgorithmDIRECT_KEY_WRAPPING,
    EdkWrappingAlgorithmIntermediateKeyWrapping,
    EdkWrappingAlgorithmUnknown,
]


def _edk_wrapping_algorithm_from_dict(d: Dict[str, Any]) -> EdkWrappingAlgorithm:
    if "DIRECT_KEY_WRAPPING" in d:
        return EdkWrappingAlgorithmDIRECT_KEY_WRAPPING.from_dict(d)

    if "IntermediateKeyWrapping" in d:
        return EdkWrappingAlgorithmIntermediateKeyWrapping.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class ECDSA:
    curve: str

    def __init__(
        self,
        *,
        curve: str,
    ):
        self.curve = curve

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ECDSA to a dictionary."""
        return {
            "curve": self.curve,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ECDSA":
        """Creates a ECDSA from a dictionary."""
        kwargs: Dict[str, Any] = {
            "curve": d["curve"],
        }

        return ECDSA(**kwargs)

    def __repr__(self) -> str:
        result = "ECDSA("
        if self.curve is not None:
            result += f"curve={repr(self.curve)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ECDSA):
            return False
        attributes: list[str] = [
            "curve",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class SignatureAlgorithmECDSA:
    def __init__(self, value: ECDSA):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"ECDSA": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SignatureAlgorithmECDSA":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return SignatureAlgorithmECDSA(ECDSA.from_dict(d["ECDSA"]))

    def __repr__(self) -> str:
        return f"SignatureAlgorithmECDSA(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SignatureAlgorithmECDSA):
            return False
        return self.value == other.value


class SignatureAlgorithmNone:
    def __init__(self, value: None_):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"None": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SignatureAlgorithmNone":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return SignatureAlgorithmNone(None_.from_dict(d["None"]))

    def __repr__(self) -> str:
        return f"SignatureAlgorithmNone(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SignatureAlgorithmNone):
            return False
        return self.value == other.value


class SignatureAlgorithmUnknown:
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to
    receive the parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SignatureAlgorithmUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return SignatureAlgorithmUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"SignatureAlgorithmUnknown(tag={self.tag})"


SignatureAlgorithm = Union[
    SignatureAlgorithmECDSA, SignatureAlgorithmNone, SignatureAlgorithmUnknown
]


def _signature_algorithm_from_dict(d: Dict[str, Any]) -> SignatureAlgorithm:
    if "ECDSA" in d:
        return SignatureAlgorithmECDSA.from_dict(d)

    if "None" in d:
        return SignatureAlgorithmNone.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class SymmetricSignatureAlgorithmHMAC:
    def __init__(self, value: str):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"HMAC": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SymmetricSignatureAlgorithmHMAC":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return SymmetricSignatureAlgorithmHMAC(d["HMAC"])

    def __repr__(self) -> str:
        return f"SymmetricSignatureAlgorithmHMAC(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SymmetricSignatureAlgorithmHMAC):
            return False
        return self.value == other.value


class SymmetricSignatureAlgorithmNone:
    def __init__(self, value: None_):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"None": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SymmetricSignatureAlgorithmNone":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return SymmetricSignatureAlgorithmNone(None_.from_dict(d["None"]))

    def __repr__(self) -> str:
        return f"SymmetricSignatureAlgorithmNone(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SymmetricSignatureAlgorithmNone):
            return False
        return self.value == other.value


class SymmetricSignatureAlgorithmUnknown:
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to
    receive the parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SymmetricSignatureAlgorithmUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return SymmetricSignatureAlgorithmUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"SymmetricSignatureAlgorithmUnknown(tag={self.tag})"


SymmetricSignatureAlgorithm = Union[
    SymmetricSignatureAlgorithmHMAC,
    SymmetricSignatureAlgorithmNone,
    SymmetricSignatureAlgorithmUnknown,
]


def _symmetric_signature_algorithm_from_dict(
    d: Dict[str, Any],
) -> SymmetricSignatureAlgorithm:
    if "HMAC" in d:
        return SymmetricSignatureAlgorithmHMAC.from_dict(d)

    if "None" in d:
        return SymmetricSignatureAlgorithmNone.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class AlgorithmSuiteInfo:
    id: AlgorithmSuiteId
    binary_id: bytes | bytearray
    message_version: int
    encrypt: Encrypt
    kdf: DerivationAlgorithm
    commitment: DerivationAlgorithm
    signature: SignatureAlgorithm
    symmetric_signature: SymmetricSignatureAlgorithm
    edk_wrapping: EdkWrappingAlgorithm

    def __init__(
        self,
        *,
        id: AlgorithmSuiteId,
        binary_id: bytes | bytearray,
        message_version: int,
        encrypt: Encrypt,
        kdf: DerivationAlgorithm,
        commitment: DerivationAlgorithm,
        signature: SignatureAlgorithm,
        symmetric_signature: SymmetricSignatureAlgorithm,
        edk_wrapping: EdkWrappingAlgorithm,
    ):
        self.id = id
        self.binary_id = binary_id
        self.message_version = message_version
        self.encrypt = encrypt
        self.kdf = kdf
        self.commitment = commitment
        self.signature = signature
        self.symmetric_signature = symmetric_signature
        self.edk_wrapping = edk_wrapping

    def as_dict(self) -> Dict[str, Any]:
        """Converts the AlgorithmSuiteInfo to a dictionary."""
        return {
            "id": self.id.as_dict(),
            "binary_id": self.binary_id,
            "message_version": self.message_version,
            "encrypt": self.encrypt.as_dict(),
            "kdf": self.kdf.as_dict(),
            "commitment": self.commitment.as_dict(),
            "signature": self.signature.as_dict(),
            "symmetric_signature": self.symmetric_signature.as_dict(),
            "edk_wrapping": self.edk_wrapping.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AlgorithmSuiteInfo":
        """Creates a AlgorithmSuiteInfo from a dictionary."""
        kwargs: Dict[str, Any] = {
            "id": _algorithm_suite_id_from_dict(d["id"]),
            "binary_id": d["binary_id"],
            "message_version": d["message_version"],
            "encrypt": _encrypt_from_dict(d["encrypt"]),
            "kdf": _derivation_algorithm_from_dict(d["kdf"]),
            "commitment": _derivation_algorithm_from_dict(d["commitment"]),
            "signature": _signature_algorithm_from_dict(d["signature"]),
            "symmetric_signature": _symmetric_signature_algorithm_from_dict(
                d["symmetric_signature"]
            ),
            "edk_wrapping": _edk_wrapping_algorithm_from_dict(d["edk_wrapping"]),
        }

        return AlgorithmSuiteInfo(**kwargs)

    def __repr__(self) -> str:
        result = "AlgorithmSuiteInfo("
        if self.id is not None:
            result += f"id={repr(self.id)}, "

        if self.binary_id is not None:
            result += f"binary_id={repr(self.binary_id)}, "

        if self.message_version is not None:
            result += f"message_version={repr(self.message_version)}, "

        if self.encrypt is not None:
            result += f"encrypt={repr(self.encrypt)}, "

        if self.kdf is not None:
            result += f"kdf={repr(self.kdf)}, "

        if self.commitment is not None:
            result += f"commitment={repr(self.commitment)}, "

        if self.signature is not None:
            result += f"signature={repr(self.signature)}, "

        if self.symmetric_signature is not None:
            result += f"symmetric_signature={repr(self.symmetric_signature)}, "

        if self.edk_wrapping is not None:
            result += f"edk_wrapping={repr(self.edk_wrapping)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AlgorithmSuiteInfo):
            return False
        attributes: list[str] = [
            "id",
            "binary_id",
            "message_version",
            "encrypt",
            "kdf",
            "commitment",
            "signature",
            "symmetric_signature",
            "edk_wrapping",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetBranchKeyIdInput:
    encryption_context: dict[str, str]

    def __init__(
        self,
        *,
        encryption_context: dict[str, str],
    ):
        """Inputs for determining the Branch Key which should be used to wrap
        or unwrap the data key for this encryption or decryption.

        :param encryption_context: The Encryption Context used with this
            encryption or decryption.
        """
        self.encryption_context = encryption_context

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetBranchKeyIdInput to a dictionary."""
        return {
            "encryption_context": self.encryption_context,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetBranchKeyIdInput":
        """Creates a GetBranchKeyIdInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "encryption_context": d["encryption_context"],
        }

        return GetBranchKeyIdInput(**kwargs)

    def __repr__(self) -> str:
        result = "GetBranchKeyIdInput("
        if self.encryption_context is not None:
            result += f"encryption_context={repr(self.encryption_context)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetBranchKeyIdInput):
            return False
        attributes: list[str] = [
            "encryption_context",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetBranchKeyIdOutput:
    branch_key_id: str

    def __init__(
        self,
        *,
        branch_key_id: str,
    ):
        """Outputs for the Branch Key responsible for wrapping or unwrapping
        the data key in this encryption or decryption.

        :param branch_key_id: The identifier of the Branch Key that
            should be responsible for wrapping or unwrapping the data
            key in this encryption or decryption.
        """
        self.branch_key_id = branch_key_id

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetBranchKeyIdOutput to a dictionary."""
        return {
            "branch_key_id": self.branch_key_id,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetBranchKeyIdOutput":
        """Creates a GetBranchKeyIdOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "branch_key_id": d["branch_key_id"],
        }

        return GetBranchKeyIdOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GetBranchKeyIdOutput("
        if self.branch_key_id is not None:
            result += f"branch_key_id={repr(self.branch_key_id)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetBranchKeyIdOutput):
            return False
        attributes: list[str] = [
            "branch_key_id",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetClientInput:
    region: str

    def __init__(
        self,
        *,
        region: str,
    ):
        """Inputs for getting a AWS KMS Client.

        :param region: The region the client should be created in.
        """
        self.region = region

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetClientInput to a dictionary."""
        return {
            "region": self.region,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetClientInput":
        """Creates a GetClientInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "region": d["region"],
        }

        return GetClientInput(**kwargs)

    def __repr__(self) -> str:
        result = "GetClientInput("
        if self.region is not None:
            result += f"region={repr(self.region)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetClientInput):
            return False
        attributes: list[str] = [
            "region",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class DiscoveryFilter:
    account_ids: list[str]
    partition: str

    def __init__(
        self,
        *,
        account_ids: list[str],
        partition: str,
    ):
        """A filter which defines what AWS partition and AWS accounts a KMS Key
        may be in for a Keyring to be allowed to attempt to decrypt it.

        :param account_ids: A list of allowed AWS account IDs.
        :param partition: The AWS partition which is allowed.
        """
        self.account_ids = account_ids
        self.partition = partition

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DiscoveryFilter to a dictionary."""
        return {
            "account_ids": self.account_ids,
            "partition": self.partition,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DiscoveryFilter":
        """Creates a DiscoveryFilter from a dictionary."""
        kwargs: Dict[str, Any] = {
            "account_ids": d["account_ids"],
            "partition": d["partition"],
        }

        return DiscoveryFilter(**kwargs)

    def __repr__(self) -> str:
        result = "DiscoveryFilter("
        if self.account_ids is not None:
            result += f"account_ids={repr(self.account_ids)}, "

        if self.partition is not None:
            result += f"partition={repr(self.partition)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DiscoveryFilter):
            return False
        attributes: list[str] = [
            "account_ids",
            "partition",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateAwsKmsDiscoveryKeyringInput:
    kms_client: BaseClient
    discovery_filter: Optional[DiscoveryFilter]
    grant_tokens: Optional[list[str]]

    def __init__(
        self,
        *,
        kms_client: BaseClient,
        discovery_filter: Optional[DiscoveryFilter] = None,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating a AWS KMS Discovery Keyring.

        :param kms_client: The KMS Client this Keyring will use to call
            KMS.
        :param discovery_filter: A filter which restricts which KMS Keys
            this Keyring may attempt to decrypt with by AWS partition
            and account.
        :param grant_tokens: A list of grant tokens to be used when
            calling KMS.
        """
        self.kms_client = kms_client
        self.discovery_filter = discovery_filter
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsDiscoveryKeyringInput to a dictionary."""
        d: Dict[str, Any] = {
            "kms_client": self.kms_client,
        }

        if self.discovery_filter is not None:
            d["discovery_filter"] = self.discovery_filter.as_dict()

        if self.grant_tokens is not None:
            d["grant_tokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsDiscoveryKeyringInput":
        """Creates a CreateAwsKmsDiscoveryKeyringInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "kms_client": d["kms_client"],
        }

        if "discovery_filter" in d:
            kwargs["discovery_filter"] = DiscoveryFilter.from_dict(
                d["discovery_filter"]
            )

        if "grant_tokens" in d:
            kwargs["grant_tokens"] = d["grant_tokens"]

        return CreateAwsKmsDiscoveryKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateAwsKmsDiscoveryKeyringInput("
        if self.kms_client is not None:
            result += f"kms_client={repr(self.kms_client)}, "

        if self.discovery_filter is not None:
            result += f"discovery_filter={repr(self.discovery_filter)}, "

        if self.grant_tokens is not None:
            result += f"grant_tokens={repr(self.grant_tokens)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateAwsKmsDiscoveryKeyringInput):
            return False
        attributes: list[str] = [
            "kms_client",
            "discovery_filter",
            "grant_tokens",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateAwsKmsDiscoveryMultiKeyringInput:
    regions: list[str]
    discovery_filter: Optional[DiscoveryFilter]
    client_supplier: Optional[
        "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier"
    ]
    grant_tokens: Optional[list[str]]

    def __init__(
        self,
        *,
        regions: list[str],
        discovery_filter: Optional[DiscoveryFilter] = None,
        client_supplier: Optional[
            "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier"
        ] = None,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating an AWS KMS Discovery Multi-Keyring.

        :param regions: The list of regions this Keyring will creates
            KMS clients for.
        :param discovery_filter: A filter which restricts which KMS Keys
            this Keyring may attempt to decrypt with by AWS partition
            and account.
        :param client_supplier: The Client Supplier which will be used
            to get KMS Clients for use with this Keyring. If not
            specified on input, a Default Client Supplier is created
            which creates a KMS Client for each region in the 'regions'
            input.
        :param grant_tokens: A list of grant tokens to be used when
            calling KMS.
        """
        self.regions = regions
        self.discovery_filter = discovery_filter
        self.client_supplier = client_supplier
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsDiscoveryMultiKeyringInput to a
        dictionary."""
        d: Dict[str, Any] = {
            "regions": self.regions,
        }

        if self.discovery_filter is not None:
            d["discovery_filter"] = self.discovery_filter.as_dict()

        if self.client_supplier is not None:
            d["client_supplier"] = self.client_supplier.as_dict()

        if self.grant_tokens is not None:
            d["grant_tokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsDiscoveryMultiKeyringInput":
        """Creates a CreateAwsKmsDiscoveryMultiKeyringInput from a
        dictionary."""
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references import (
            ClientSupplier,
        )

        kwargs: Dict[str, Any] = {
            "regions": d["regions"],
        }

        if "discovery_filter" in d:
            kwargs["discovery_filter"] = DiscoveryFilter.from_dict(
                d["discovery_filter"]
            )

        if "client_supplier" in d:
            kwargs["client_supplier"] = ClientSupplier.from_dict(d["client_supplier"])

        if "grant_tokens" in d:
            kwargs["grant_tokens"] = d["grant_tokens"]

        return CreateAwsKmsDiscoveryMultiKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateAwsKmsDiscoveryMultiKeyringInput("
        if self.regions is not None:
            result += f"regions={repr(self.regions)}, "

        if self.discovery_filter is not None:
            result += f"discovery_filter={repr(self.discovery_filter)}, "

        if self.client_supplier is not None:
            result += f"client_supplier={repr(self.client_supplier)}, "

        if self.grant_tokens is not None:
            result += f"grant_tokens={repr(self.grant_tokens)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateAwsKmsDiscoveryMultiKeyringInput):
            return False
        attributes: list[str] = [
            "regions",
            "discovery_filter",
            "client_supplier",
            "grant_tokens",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class KmsPrivateKeyToStaticPublicKeyInput:
    sender_kms_identifier: str
    sender_public_key: Optional[bytes | bytearray]
    recipient_public_key: bytes | bytearray

    def __init__(
        self,
        *,
        sender_kms_identifier: str,
        recipient_public_key: bytes | bytearray,
        sender_public_key: Optional[bytes | bytearray] = None,
    ):
        """Inputs for creating a KmsPrivateKeyToStaticPublicKey Configuration.

        :param sender_kms_identifier: AWS KMS Key Identifier belonging
            to the sender.
        :param recipient_public_key: Recipient Public Key. This MUST be
            a raw public ECC key in DER format.
        :param sender_public_key: Sender Public Key. This is the raw
            public ECC key in DER format that belongs to the
            senderKmsIdentifier.
        """
        self.sender_kms_identifier = sender_kms_identifier
        self.recipient_public_key = recipient_public_key
        self.sender_public_key = sender_public_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the KmsPrivateKeyToStaticPublicKeyInput to a dictionary."""
        d: Dict[str, Any] = {
            "sender_kms_identifier": self.sender_kms_identifier,
            "recipient_public_key": self.recipient_public_key,
        }

        if self.sender_public_key is not None:
            d["sender_public_key"] = self.sender_public_key

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KmsPrivateKeyToStaticPublicKeyInput":
        """Creates a KmsPrivateKeyToStaticPublicKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "sender_kms_identifier": d["sender_kms_identifier"],
            "recipient_public_key": d["recipient_public_key"],
        }

        if "sender_public_key" in d:
            kwargs["sender_public_key"] = d["sender_public_key"]

        return KmsPrivateKeyToStaticPublicKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "KmsPrivateKeyToStaticPublicKeyInput("
        if self.sender_kms_identifier is not None:
            result += f"sender_kms_identifier={repr(self.sender_kms_identifier)}, "

        if self.sender_public_key is not None:
            result += f"sender_public_key={repr(self.sender_public_key)}, "

        if self.recipient_public_key is not None:
            result += f"recipient_public_key={repr(self.recipient_public_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KmsPrivateKeyToStaticPublicKeyInput):
            return False
        attributes: list[str] = [
            "sender_kms_identifier",
            "sender_public_key",
            "recipient_public_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class KmsPublicKeyDiscoveryInput:
    recipient_kms_identifier: str

    def __init__(
        self,
        *,
        recipient_kms_identifier: str,
    ):
        """Inputs for creating a KmsPublicKeyDiscovery Configuration. This is a
        DECRYPT ONLY configuration.

        :param recipient_kms_identifier: AWS KMS key identifier
            belonging to the recipient.
        """
        self.recipient_kms_identifier = recipient_kms_identifier

    def as_dict(self) -> Dict[str, Any]:
        """Converts the KmsPublicKeyDiscoveryInput to a dictionary."""
        return {
            "recipient_kms_identifier": self.recipient_kms_identifier,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KmsPublicKeyDiscoveryInput":
        """Creates a KmsPublicKeyDiscoveryInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "recipient_kms_identifier": d["recipient_kms_identifier"],
        }

        return KmsPublicKeyDiscoveryInput(**kwargs)

    def __repr__(self) -> str:
        result = "KmsPublicKeyDiscoveryInput("
        if self.recipient_kms_identifier is not None:
            result += f"recipient_kms_identifier={repr(self.recipient_kms_identifier)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KmsPublicKeyDiscoveryInput):
            return False
        attributes: list[str] = [
            "recipient_kms_identifier",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class KmsEcdhStaticConfigurationsKmsPublicKeyDiscovery:
    """Inputs for creating a KmsPublicKeyDiscovery Configuration.

    This is a DECRYPT ONLY configuration.
    """

    def __init__(self, value: KmsPublicKeyDiscoveryInput):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"KmsPublicKeyDiscovery": self.value.as_dict()}

    @staticmethod
    def from_dict(
        d: Dict[str, Any],
    ) -> "KmsEcdhStaticConfigurationsKmsPublicKeyDiscovery":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KmsEcdhStaticConfigurationsKmsPublicKeyDiscovery(
            KmsPublicKeyDiscoveryInput.from_dict(d["KmsPublicKeyDiscovery"])
        )

    def __repr__(self) -> str:
        return (
            f"KmsEcdhStaticConfigurationsKmsPublicKeyDiscovery(value=repr(self.value))"
        )

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KmsEcdhStaticConfigurationsKmsPublicKeyDiscovery):
            return False
        return self.value == other.value


class KmsEcdhStaticConfigurationsKmsPrivateKeyToStaticPublicKey:
    """Inputs for creating a KmsPrivateKeyToStaticPublicKey Configuration."""

    def __init__(self, value: KmsPrivateKeyToStaticPublicKeyInput):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"KmsPrivateKeyToStaticPublicKey": self.value.as_dict()}

    @staticmethod
    def from_dict(
        d: Dict[str, Any],
    ) -> "KmsEcdhStaticConfigurationsKmsPrivateKeyToStaticPublicKey":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KmsEcdhStaticConfigurationsKmsPrivateKeyToStaticPublicKey(
            KmsPrivateKeyToStaticPublicKeyInput.from_dict(
                d["KmsPrivateKeyToStaticPublicKey"]
            )
        )

    def __repr__(self) -> str:
        return f"KmsEcdhStaticConfigurationsKmsPrivateKeyToStaticPublicKey(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(
            other, KmsEcdhStaticConfigurationsKmsPrivateKeyToStaticPublicKey
        ):
            return False
        return self.value == other.value


class KmsEcdhStaticConfigurationsUnknown:
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to
    receive the parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KmsEcdhStaticConfigurationsUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return KmsEcdhStaticConfigurationsUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"KmsEcdhStaticConfigurationsUnknown(tag={self.tag})"


# Allowed configurations when using KmsEcdhStaticConfigurations.
KmsEcdhStaticConfigurations = Union[
    KmsEcdhStaticConfigurationsKmsPublicKeyDiscovery,
    KmsEcdhStaticConfigurationsKmsPrivateKeyToStaticPublicKey,
    KmsEcdhStaticConfigurationsUnknown,
]


def _kms_ecdh_static_configurations_from_dict(
    d: Dict[str, Any],
) -> KmsEcdhStaticConfigurations:
    if "KmsPublicKeyDiscovery" in d:
        return KmsEcdhStaticConfigurationsKmsPublicKeyDiscovery.from_dict(d)

    if "KmsPrivateKeyToStaticPublicKey" in d:
        return KmsEcdhStaticConfigurationsKmsPrivateKeyToStaticPublicKey.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class CreateAwsKmsEcdhKeyringInput:
    key_agreement_scheme: KmsEcdhStaticConfigurations
    curve_spec: str
    kms_client: BaseClient
    grant_tokens: Optional[list[str]]

    def __init__(
        self,
        *,
        key_agreement_scheme: KmsEcdhStaticConfigurations,
        curve_spec: str,
        kms_client: BaseClient,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for creating an AWS KMS ECDH Keyring.

        :param key_agreement_scheme: The Key Agreement Scheme
            configuration that is responsible for how the shared secret
            is calculated.
        :param curve_spec: The named curve that corresponds to the curve
            on which the sender's private and recipient's public key
            lie.
        :param kms_client: The KMS Client this Keyring will use to call
            KMS.
        :param grant_tokens: A list of grant tokens to be used when
            calling KMS.
        """
        self.key_agreement_scheme = key_agreement_scheme
        self.curve_spec = curve_spec
        self.kms_client = kms_client
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsEcdhKeyringInput to a dictionary."""
        d: Dict[str, Any] = {
            "key_agreement_scheme": self.key_agreement_scheme.as_dict(),
            "curve_spec": self.curve_spec,
            "kms_client": self.kms_client,
        }

        if self.grant_tokens is not None:
            d["grant_tokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsEcdhKeyringInput":
        """Creates a CreateAwsKmsEcdhKeyringInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "key_agreement_scheme": _kms_ecdh_static_configurations_from_dict(
                d["key_agreement_scheme"]
            ),
            "curve_spec": d["curve_spec"],
            "kms_client": d["kms_client"],
        }

        if "grant_tokens" in d:
            kwargs["grant_tokens"] = d["grant_tokens"]

        return CreateAwsKmsEcdhKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateAwsKmsEcdhKeyringInput("
        if self.key_agreement_scheme is not None:
            result += f"key_agreement_scheme={repr(self.key_agreement_scheme)}, "

        if self.curve_spec is not None:
            result += f"curve_spec={repr(self.curve_spec)}, "

        if self.kms_client is not None:
            result += f"kms_client={repr(self.kms_client)}, "

        if self.grant_tokens is not None:
            result += f"grant_tokens={repr(self.grant_tokens)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateAwsKmsEcdhKeyringInput):
            return False
        attributes: list[str] = [
            "key_agreement_scheme",
            "curve_spec",
            "kms_client",
            "grant_tokens",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class DefaultCache:
    entry_capacity: int

    def __init__(
        self,
        *,
        entry_capacity: int = 0,
    ):
        """The best choice for most situations. Probably a StormTrackingCache.

        :param entry_capacity: Maximum number of entries cached.
        """
        if (entry_capacity is not None) and (entry_capacity < 1):
            raise ValueError("entry_capacity must be greater than or equal to 1")

        self.entry_capacity = entry_capacity

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DefaultCache to a dictionary."""
        d: Dict[str, Any] = {}

        if self.entry_capacity is not None:
            d["entry_capacity"] = self.entry_capacity

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DefaultCache":
        """Creates a DefaultCache from a dictionary."""
        kwargs: Dict[str, Any] = {}

        if "entry_capacity" in d:
            kwargs["entry_capacity"] = d["entry_capacity"]

        return DefaultCache(**kwargs)

    def __repr__(self) -> str:
        result = "DefaultCache("
        if self.entry_capacity is not None:
            result += f"entry_capacity={repr(self.entry_capacity)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DefaultCache):
            return False
        attributes: list[str] = [
            "entry_capacity",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class MultiThreadedCache:
    entry_capacity: int
    entry_pruning_tail_size: int

    def __init__(
        self,
        *,
        entry_capacity: int = 0,
        entry_pruning_tail_size: int = 0,
    ):
        """A cache that is safe for use in a multi threaded environment, but no
        extra functionality.

        :param entry_capacity: Maximum number of entries cached.
        :param entry_pruning_tail_size: Number of entries to prune at a
            time.
        """
        if (entry_capacity is not None) and (entry_capacity < 1):
            raise ValueError("entry_capacity must be greater than or equal to 1")

        self.entry_capacity = entry_capacity
        if (entry_pruning_tail_size is not None) and (entry_pruning_tail_size < 1):
            raise ValueError(
                "entry_pruning_tail_size must be greater than or equal to 1"
            )

        self.entry_pruning_tail_size = entry_pruning_tail_size

    def as_dict(self) -> Dict[str, Any]:
        """Converts the MultiThreadedCache to a dictionary."""
        d: Dict[str, Any] = {}

        if self.entry_capacity is not None:
            d["entry_capacity"] = self.entry_capacity

        if self.entry_pruning_tail_size is not None:
            d["entry_pruning_tail_size"] = self.entry_pruning_tail_size

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MultiThreadedCache":
        """Creates a MultiThreadedCache from a dictionary."""
        kwargs: Dict[str, Any] = {}

        if "entry_capacity" in d:
            kwargs["entry_capacity"] = d["entry_capacity"]

        if "entry_pruning_tail_size" in d:
            kwargs["entry_pruning_tail_size"] = d["entry_pruning_tail_size"]

        return MultiThreadedCache(**kwargs)

    def __repr__(self) -> str:
        result = "MultiThreadedCache("
        if self.entry_capacity is not None:
            result += f"entry_capacity={repr(self.entry_capacity)}, "

        if self.entry_pruning_tail_size is not None:
            result += f"entry_pruning_tail_size={repr(self.entry_pruning_tail_size)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MultiThreadedCache):
            return False
        attributes: list[str] = [
            "entry_capacity",
            "entry_pruning_tail_size",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class NoCache:
    """Nothing should ever be cached."""

    def as_dict(self) -> Dict[str, Any]:
        """Converts the NoCache to a dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "NoCache":
        """Creates a NoCache from a dictionary."""
        return NoCache()

    def __repr__(self) -> str:
        result = "NoCache("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, NoCache)


class SingleThreadedCache:
    entry_capacity: int
    entry_pruning_tail_size: int

    def __init__(
        self,
        *,
        entry_capacity: int = 0,
        entry_pruning_tail_size: int = 0,
    ):
        """A cache that is NOT safe for use in a multi threaded environment.

        :param entry_capacity: Maximum number of entries cached.
        :param entry_pruning_tail_size: Number of entries to prune at a
            time.
        """
        if (entry_capacity is not None) and (entry_capacity < 1):
            raise ValueError("entry_capacity must be greater than or equal to 1")

        self.entry_capacity = entry_capacity
        if (entry_pruning_tail_size is not None) and (entry_pruning_tail_size < 1):
            raise ValueError(
                "entry_pruning_tail_size must be greater than or equal to 1"
            )

        self.entry_pruning_tail_size = entry_pruning_tail_size

    def as_dict(self) -> Dict[str, Any]:
        """Converts the SingleThreadedCache to a dictionary."""
        d: Dict[str, Any] = {}

        if self.entry_capacity is not None:
            d["entry_capacity"] = self.entry_capacity

        if self.entry_pruning_tail_size is not None:
            d["entry_pruning_tail_size"] = self.entry_pruning_tail_size

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SingleThreadedCache":
        """Creates a SingleThreadedCache from a dictionary."""
        kwargs: Dict[str, Any] = {}

        if "entry_capacity" in d:
            kwargs["entry_capacity"] = d["entry_capacity"]

        if "entry_pruning_tail_size" in d:
            kwargs["entry_pruning_tail_size"] = d["entry_pruning_tail_size"]

        return SingleThreadedCache(**kwargs)

    def __repr__(self) -> str:
        result = "SingleThreadedCache("
        if self.entry_capacity is not None:
            result += f"entry_capacity={repr(self.entry_capacity)}, "

        if self.entry_pruning_tail_size is not None:
            result += f"entry_pruning_tail_size={repr(self.entry_pruning_tail_size)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SingleThreadedCache):
            return False
        attributes: list[str] = [
            "entry_capacity",
            "entry_pruning_tail_size",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class TimeUnits:
    SECONDS = "Seconds"

    MILLISECONDS = "Milliseconds"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset({"Seconds", "Milliseconds"})


class StormTrackingCache:
    entry_capacity: int
    entry_pruning_tail_size: int
    grace_period: int
    grace_interval: int
    fan_out: int
    in_flight_ttl: int
    sleep_milli: int
    time_units: Optional[str]

    def __init__(
        self,
        *,
        entry_capacity: int = 0,
        entry_pruning_tail_size: int = 0,
        grace_period: int = 0,
        grace_interval: int = 0,
        fan_out: int = 0,
        in_flight_ttl: int = 0,
        sleep_milli: int = 0,
        time_units: Optional[str] = None,
    ):
        """A cache that is safe for use in a multi threaded environment, and
        tries to prevent redundant or overly parallel backend calls.

        :param entry_capacity: Maximum number of entries cached.
        :param entry_pruning_tail_size: Number of entries to prune at a
            time.
        :param grace_period: How much time before expiration should an
            attempt be made to refresh the materials. If zero, use a
            simple cache with no storm tracking.
        :param grace_interval: How much time between attempts to refresh
            the materials.
        :param fan_out: How many simultaneous attempts to refresh the
            materials.
        :param in_flight_ttl: How much time until an attempt to refresh
            the materials should be forgotten.
        :param sleep_milli: How many milliseconds should a thread sleep
            if fanOut is exceeded.
        :param time_units: The time unit for gracePeriod, graceInterval,
            and inFlightTTL. The default is seconds. If this is set to
            milliseconds, then these values will be treated as
            milliseconds.
        """
        if (entry_capacity is not None) and (entry_capacity < 1):
            raise ValueError("entry_capacity must be greater than or equal to 1")

        self.entry_capacity = entry_capacity
        if (entry_pruning_tail_size is not None) and (entry_pruning_tail_size < 1):
            raise ValueError(
                "entry_pruning_tail_size must be greater than or equal to 1"
            )

        self.entry_pruning_tail_size = entry_pruning_tail_size
        if (grace_period is not None) and (grace_period < 1):
            raise ValueError("grace_period must be greater than or equal to 1")

        self.grace_period = grace_period
        if (grace_interval is not None) and (grace_interval < 1):
            raise ValueError("grace_interval must be greater than or equal to 1")

        self.grace_interval = grace_interval
        if (fan_out is not None) and (fan_out < 1):
            raise ValueError("fan_out must be greater than or equal to 1")

        self.fan_out = fan_out
        if (in_flight_ttl is not None) and (in_flight_ttl < 1):
            raise ValueError("in_flight_ttl must be greater than or equal to 1")

        self.in_flight_ttl = in_flight_ttl
        if (sleep_milli is not None) and (sleep_milli < 1):
            raise ValueError("sleep_milli must be greater than or equal to 1")

        self.sleep_milli = sleep_milli
        self.time_units = time_units

    def as_dict(self) -> Dict[str, Any]:
        """Converts the StormTrackingCache to a dictionary."""
        d: Dict[str, Any] = {}

        if self.entry_capacity is not None:
            d["entry_capacity"] = self.entry_capacity

        if self.entry_pruning_tail_size is not None:
            d["entry_pruning_tail_size"] = self.entry_pruning_tail_size

        if self.grace_period is not None:
            d["grace_period"] = self.grace_period

        if self.grace_interval is not None:
            d["grace_interval"] = self.grace_interval

        if self.fan_out is not None:
            d["fan_out"] = self.fan_out

        if self.in_flight_ttl is not None:
            d["in_flight_ttl"] = self.in_flight_ttl

        if self.sleep_milli is not None:
            d["sleep_milli"] = self.sleep_milli

        if self.time_units is not None:
            d["time_units"] = self.time_units

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "StormTrackingCache":
        """Creates a StormTrackingCache from a dictionary."""
        kwargs: Dict[str, Any] = {}

        if "entry_capacity" in d:
            kwargs["entry_capacity"] = d["entry_capacity"]

        if "entry_pruning_tail_size" in d:
            kwargs["entry_pruning_tail_size"] = d["entry_pruning_tail_size"]

        if "grace_period" in d:
            kwargs["grace_period"] = d["grace_period"]

        if "grace_interval" in d:
            kwargs["grace_interval"] = d["grace_interval"]

        if "fan_out" in d:
            kwargs["fan_out"] = d["fan_out"]

        if "in_flight_ttl" in d:
            kwargs["in_flight_ttl"] = d["in_flight_ttl"]

        if "sleep_milli" in d:
            kwargs["sleep_milli"] = d["sleep_milli"]

        if "time_units" in d:
            kwargs["time_units"] = d["time_units"]

        return StormTrackingCache(**kwargs)

    def __repr__(self) -> str:
        result = "StormTrackingCache("
        if self.entry_capacity is not None:
            result += f"entry_capacity={repr(self.entry_capacity)}, "

        if self.entry_pruning_tail_size is not None:
            result += f"entry_pruning_tail_size={repr(self.entry_pruning_tail_size)}, "

        if self.grace_period is not None:
            result += f"grace_period={repr(self.grace_period)}, "

        if self.grace_interval is not None:
            result += f"grace_interval={repr(self.grace_interval)}, "

        if self.fan_out is not None:
            result += f"fan_out={repr(self.fan_out)}, "

        if self.in_flight_ttl is not None:
            result += f"in_flight_ttl={repr(self.in_flight_ttl)}, "

        if self.sleep_milli is not None:
            result += f"sleep_milli={repr(self.sleep_milli)}, "

        if self.time_units is not None:
            result += f"time_units={repr(self.time_units)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, StormTrackingCache):
            return False
        attributes: list[str] = [
            "entry_capacity",
            "entry_pruning_tail_size",
            "grace_period",
            "grace_interval",
            "fan_out",
            "in_flight_ttl",
            "sleep_milli",
            "time_units",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CacheTypeDefault:
    """The best choice for most situations.

    Probably a StormTrackingCache.
    """

    def __init__(self, value: DefaultCache):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"Default": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CacheTypeDefault":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return CacheTypeDefault(DefaultCache.from_dict(d["Default"]))

    def __repr__(self) -> str:
        return f"CacheTypeDefault(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CacheTypeDefault):
            return False
        return self.value == other.value


class CacheTypeNo:
    """Nothing should ever be cached."""

    def __init__(self, value: NoCache):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"No": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CacheTypeNo":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return CacheTypeNo(NoCache.from_dict(d["No"]))

    def __repr__(self) -> str:
        return f"CacheTypeNo(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CacheTypeNo):
            return False
        return self.value == other.value


class CacheTypeSingleThreaded:
    """A cache that is NOT safe for use in a multi threaded environment."""

    def __init__(self, value: SingleThreadedCache):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"SingleThreaded": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CacheTypeSingleThreaded":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return CacheTypeSingleThreaded(
            SingleThreadedCache.from_dict(d["SingleThreaded"])
        )

    def __repr__(self) -> str:
        return f"CacheTypeSingleThreaded(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CacheTypeSingleThreaded):
            return False
        return self.value == other.value


class CacheTypeMultiThreaded:
    """A cache that is safe for use in a multi threaded environment, but no
    extra functionality."""

    def __init__(self, value: MultiThreadedCache):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"MultiThreaded": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CacheTypeMultiThreaded":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return CacheTypeMultiThreaded(MultiThreadedCache.from_dict(d["MultiThreaded"]))

    def __repr__(self) -> str:
        return f"CacheTypeMultiThreaded(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CacheTypeMultiThreaded):
            return False
        return self.value == other.value


class CacheTypeStormTracking:
    """A cache that is safe for use in a multi threaded environment, and tries
    to prevent redundant or overly parallel backend calls."""

    def __init__(self, value: StormTrackingCache):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"StormTracking": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CacheTypeStormTracking":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return CacheTypeStormTracking(StormTrackingCache.from_dict(d["StormTracking"]))

    def __repr__(self) -> str:
        return f"CacheTypeStormTracking(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CacheTypeStormTracking):
            return False
        return self.value == other.value


class CacheTypeShared:
    """Shared cache across multiple Hierarchical Keyrings.

    For this cache type, the user should provide an already constructed
    CryptographicMaterialsCache to the Hierarchical Keyring at
    initialization.
    """

    def __init__(
        self,
        value: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.CryptographicMaterialsCache",
    ):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"Shared": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CacheTypeShared":
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references import (
            CryptographicMaterialsCache,
        )

        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return CacheTypeShared(CryptographicMaterialsCache.from_dict(d["Shared"]))

    def __repr__(self) -> str:
        return f"CacheTypeShared(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CacheTypeShared):
            return False
        return self.value == other.value


class CacheTypeUnknown:
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to
    receive the parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CacheTypeUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return CacheTypeUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"CacheTypeUnknown(tag={self.tag})"


CacheType = Union[
    CacheTypeDefault,
    CacheTypeNo,
    CacheTypeSingleThreaded,
    CacheTypeMultiThreaded,
    CacheTypeStormTracking,
    CacheTypeShared,
    CacheTypeUnknown,
]


def _cache_type_from_dict(d: Dict[str, Any]) -> CacheType:
    if "Default" in d:
        return CacheTypeDefault.from_dict(d)

    if "No" in d:
        return CacheTypeNo.from_dict(d)

    if "SingleThreaded" in d:
        return CacheTypeSingleThreaded.from_dict(d)

    if "MultiThreaded" in d:
        return CacheTypeMultiThreaded.from_dict(d)

    if "StormTracking" in d:
        return CacheTypeStormTracking.from_dict(d)

    if "Shared" in d:
        return CacheTypeShared.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class CreateAwsKmsHierarchicalKeyringInput:
    branch_key_id: Optional[str]
    branch_key_id_supplier: Optional[
        "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.BranchKeyIdSupplier"
    ]
    key_store: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.client.KeyStore"
    ttl_seconds: int
    cache: Optional[CacheType]
    partition_id: Optional[str]

    def __init__(
        self,
        *,
        key_store: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.client.KeyStore",
        branch_key_id: Optional[str] = None,
        branch_key_id_supplier: Optional[
            "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.BranchKeyIdSupplier"
        ] = None,
        ttl_seconds: int = 0,
        cache: Optional[CacheType] = None,
        partition_id: Optional[str] = None,
    ):
        """Inputs for creating a Hierarchical Keyring.

        :param key_store: The Key Store which contains the Branch Key(s)
            responsible for wrapping and unwrapping data keys.
        :param branch_key_id: The identifier for the single Branch Key
            responsible for wrapping and unwrapping the data key. Either
            a Branch Key ID or Branch Key Supplier must be specified.
        :param branch_key_id_supplier: A Branch Key Supplier which
            determines what Branch Key to use to wrap and unwrap the
            data key. Either a Branch Key ID or Branch Key Supplier must
            be specified.
        :param ttl_seconds: How many seconds the Branch Key material is
            allowed to be reused within the local cache before it is re-
            retrieved from Amazon DynamoDB and re-authenticated with AWS
            KMS.
        :param cache: Sets the type of cache for this Hierarchical
            Keyring. By providing an already initialized 'Shared' cache,
            users can determine the scope of the cache. That is, if the
            cache is shared across other Cryptographic Material
            Providers, for instance other Hierarchical Keyrings or
            Caching Cryptographic Materials Managers (Caching CMMs). If
            any other type of cache in the CacheType union is provided,
            the Hierarchical Keyring will initialize a cache of that
            type, to be used with only this Hierarchical Keyring. If not
            set, a DefaultCache is initialized to be used with only this
            Hierarchical Keyring with entryCapacity = 1000.
        :param partition_id: Partition ID to distinguish Cryptographic
            Material Providers (i.e: Keyrings) writing to a cache. If
            the Partition ID is the same for two Hierarchical Keyrings
            (or another Material Provider), they can share the same
            cache entries in the cache.
        """
        self.key_store = key_store
        self.branch_key_id = branch_key_id
        self.branch_key_id_supplier = branch_key_id_supplier
        if (ttl_seconds is not None) and (ttl_seconds < 0):
            raise ValueError("ttl_seconds must be greater than or equal to 0")

        self.ttl_seconds = ttl_seconds
        self.cache = cache
        self.partition_id = partition_id

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsHierarchicalKeyringInput to a
        dictionary."""
        d: Dict[str, Any] = {
            "key_store": self.key_store.as_dict(),
        }

        if self.branch_key_id is not None:
            d["branch_key_id"] = self.branch_key_id

        if self.branch_key_id_supplier is not None:
            d["branch_key_id_supplier"] = self.branch_key_id_supplier.as_dict()

        if self.ttl_seconds is not None:
            d["ttl_seconds"] = self.ttl_seconds

        if self.cache is not None:
            d["cache"] = self.cache.as_dict()

        if self.partition_id is not None:
            d["partition_id"] = self.partition_id

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsHierarchicalKeyringInput":
        """Creates a CreateAwsKmsHierarchicalKeyringInput from a dictionary."""
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references import (
            BranchKeyIdSupplier,
        )
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.client import (
            KeyStore,
        )

        kwargs: Dict[str, Any] = {
            "key_store": KeyStore.from_dict(d["key_store"]),
        }

        if "branch_key_id" in d:
            kwargs["branch_key_id"] = d["branch_key_id"]

        if "branch_key_id_supplier" in d:
            kwargs["branch_key_id_supplier"] = BranchKeyIdSupplier.from_dict(
                d["branch_key_id_supplier"]
            )

        if "ttl_seconds" in d:
            kwargs["ttl_seconds"] = d["ttl_seconds"]

        if "cache" in d:
            kwargs["cache"] = (_cache_type_from_dict(d["cache"]),)

        if "partition_id" in d:
            kwargs["partition_id"] = d["partition_id"]

        return CreateAwsKmsHierarchicalKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateAwsKmsHierarchicalKeyringInput("
        if self.branch_key_id is not None:
            result += f"branch_key_id={repr(self.branch_key_id)}, "

        if self.branch_key_id_supplier is not None:
            result += f"branch_key_id_supplier={repr(self.branch_key_id_supplier)}, "

        if self.key_store is not None:
            result += f"key_store={repr(self.key_store)}, "

        if self.ttl_seconds is not None:
            result += f"ttl_seconds={repr(self.ttl_seconds)}, "

        if self.cache is not None:
            result += f"cache={repr(self.cache)}, "

        if self.partition_id is not None:
            result += f"partition_id={repr(self.partition_id)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateAwsKmsHierarchicalKeyringInput):
            return False
        attributes: list[str] = [
            "branch_key_id",
            "branch_key_id_supplier",
            "key_store",
            "ttl_seconds",
            "cache",
            "partition_id",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateAwsKmsKeyringInput:
    kms_key_id: str
    kms_client: BaseClient
    grant_tokens: Optional[list[str]]

    def __init__(
        self,
        *,
        kms_key_id: str,
        kms_client: BaseClient,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating a AWS KMS Keyring.

        :param kms_key_id: The identifier for the symmetric AWS KMS Key
            responsible for wrapping and unwrapping data keys. This
            should not be a AWS KMS Multi-Region Key.
        :param kms_client: The KMS Client this Keyring will use to call
            KMS.
        :param grant_tokens: A list of grant tokens to be used when
            calling KMS.
        """
        self.kms_key_id = kms_key_id
        self.kms_client = kms_client
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsKeyringInput to a dictionary."""
        d: Dict[str, Any] = {
            "kms_key_id": self.kms_key_id,
            "kms_client": self.kms_client,
        }

        if self.grant_tokens is not None:
            d["grant_tokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsKeyringInput":
        """Creates a CreateAwsKmsKeyringInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "kms_key_id": d["kms_key_id"],
            "kms_client": d["kms_client"],
        }

        if "grant_tokens" in d:
            kwargs["grant_tokens"] = d["grant_tokens"]

        return CreateAwsKmsKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateAwsKmsKeyringInput("
        if self.kms_key_id is not None:
            result += f"kms_key_id={repr(self.kms_key_id)}, "

        if self.kms_client is not None:
            result += f"kms_client={repr(self.kms_client)}, "

        if self.grant_tokens is not None:
            result += f"grant_tokens={repr(self.grant_tokens)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateAwsKmsKeyringInput):
            return False
        attributes: list[str] = [
            "kms_key_id",
            "kms_client",
            "grant_tokens",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateAwsKmsMrkDiscoveryKeyringInput:
    kms_client: BaseClient
    discovery_filter: Optional[DiscoveryFilter]
    grant_tokens: Optional[list[str]]
    region: str

    def __init__(
        self,
        *,
        kms_client: BaseClient,
        region: str,
        discovery_filter: Optional[DiscoveryFilter] = None,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating a AWS KMS MRK Discovery Keyring.

        :param kms_client: The KMS Client this Keyring will use to call
            KMS.
        :param region: The region the input 'kmsClient' is in.
        :param discovery_filter: A filter which restricts which KMS Keys
            this Keyring may attempt to decrypt with by AWS partition
            and account.
        :param grant_tokens: A list of grant tokens to be used when
            calling KMS.
        """
        self.kms_client = kms_client
        self.region = region
        self.discovery_filter = discovery_filter
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsMrkDiscoveryKeyringInput to a
        dictionary."""
        d: Dict[str, Any] = {
            "kms_client": self.kms_client,
            "region": self.region,
        }

        if self.discovery_filter is not None:
            d["discovery_filter"] = self.discovery_filter.as_dict()

        if self.grant_tokens is not None:
            d["grant_tokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsMrkDiscoveryKeyringInput":
        """Creates a CreateAwsKmsMrkDiscoveryKeyringInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "kms_client": d["kms_client"],
            "region": d["region"],
        }

        if "discovery_filter" in d:
            kwargs["discovery_filter"] = DiscoveryFilter.from_dict(
                d["discovery_filter"]
            )

        if "grant_tokens" in d:
            kwargs["grant_tokens"] = d["grant_tokens"]

        return CreateAwsKmsMrkDiscoveryKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateAwsKmsMrkDiscoveryKeyringInput("
        if self.kms_client is not None:
            result += f"kms_client={repr(self.kms_client)}, "

        if self.discovery_filter is not None:
            result += f"discovery_filter={repr(self.discovery_filter)}, "

        if self.grant_tokens is not None:
            result += f"grant_tokens={repr(self.grant_tokens)}, "

        if self.region is not None:
            result += f"region={repr(self.region)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateAwsKmsMrkDiscoveryKeyringInput):
            return False
        attributes: list[str] = [
            "kms_client",
            "discovery_filter",
            "grant_tokens",
            "region",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateAwsKmsMrkDiscoveryMultiKeyringInput:
    regions: list[str]
    discovery_filter: Optional[DiscoveryFilter]
    client_supplier: Optional[
        "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier"
    ]
    grant_tokens: Optional[list[str]]

    def __init__(
        self,
        *,
        regions: list[str],
        discovery_filter: Optional[DiscoveryFilter] = None,
        client_supplier: Optional[
            "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier"
        ] = None,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating a AWS KMS MRK Discovery Multi-Keyring.

        :param regions: The list of regions this Keyring will creates
            KMS clients for.
        :param discovery_filter: A filter which restricts which KMS Keys
            this Keyring may attempt to decrypt with by AWS partition
            and account.
        :param client_supplier: The Client Supplier which will be used
            to get KMS Clients for use with this Keyring. If not
            specified on input, a Default Client Supplier is created
            which creates a KMS Client for each region in the 'regions'
            input.
        :param grant_tokens: A list of grant tokens to be used when
            calling KMS.
        """
        self.regions = regions
        self.discovery_filter = discovery_filter
        self.client_supplier = client_supplier
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsMrkDiscoveryMultiKeyringInput to a
        dictionary."""
        d: Dict[str, Any] = {
            "regions": self.regions,
        }

        if self.discovery_filter is not None:
            d["discovery_filter"] = self.discovery_filter.as_dict()

        if self.client_supplier is not None:
            d["client_supplier"] = self.client_supplier.as_dict()

        if self.grant_tokens is not None:
            d["grant_tokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsMrkDiscoveryMultiKeyringInput":
        """Creates a CreateAwsKmsMrkDiscoveryMultiKeyringInput from a
        dictionary."""
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references import (
            ClientSupplier,
        )

        kwargs: Dict[str, Any] = {
            "regions": d["regions"],
        }

        if "discovery_filter" in d:
            kwargs["discovery_filter"] = DiscoveryFilter.from_dict(
                d["discovery_filter"]
            )

        if "client_supplier" in d:
            kwargs["client_supplier"] = ClientSupplier.from_dict(d["client_supplier"])

        if "grant_tokens" in d:
            kwargs["grant_tokens"] = d["grant_tokens"]

        return CreateAwsKmsMrkDiscoveryMultiKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateAwsKmsMrkDiscoveryMultiKeyringInput("
        if self.regions is not None:
            result += f"regions={repr(self.regions)}, "

        if self.discovery_filter is not None:
            result += f"discovery_filter={repr(self.discovery_filter)}, "

        if self.client_supplier is not None:
            result += f"client_supplier={repr(self.client_supplier)}, "

        if self.grant_tokens is not None:
            result += f"grant_tokens={repr(self.grant_tokens)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateAwsKmsMrkDiscoveryMultiKeyringInput):
            return False
        attributes: list[str] = [
            "regions",
            "discovery_filter",
            "client_supplier",
            "grant_tokens",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateAwsKmsMrkKeyringInput:
    kms_key_id: str
    kms_client: BaseClient
    grant_tokens: Optional[list[str]]

    def __init__(
        self,
        *,
        kms_key_id: str,
        kms_client: BaseClient,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating an AWS KMS MRK Keyring.

        :param kms_key_id: The identifier for the symmetric AWS KMS Key
            or AWS KMS Multi-Region Key responsible for wrapping and
            unwrapping data keys.
        :param kms_client: The KMS Client this Keyring will use to call
            KMS.
        :param grant_tokens: A list of grant tokens to be used when
            calling KMS.
        """
        self.kms_key_id = kms_key_id
        self.kms_client = kms_client
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsMrkKeyringInput to a dictionary."""
        d: Dict[str, Any] = {
            "kms_key_id": self.kms_key_id,
            "kms_client": self.kms_client,
        }

        if self.grant_tokens is not None:
            d["grant_tokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsMrkKeyringInput":
        """Creates a CreateAwsKmsMrkKeyringInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "kms_key_id": d["kms_key_id"],
            "kms_client": d["kms_client"],
        }

        if "grant_tokens" in d:
            kwargs["grant_tokens"] = d["grant_tokens"]

        return CreateAwsKmsMrkKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateAwsKmsMrkKeyringInput("
        if self.kms_key_id is not None:
            result += f"kms_key_id={repr(self.kms_key_id)}, "

        if self.kms_client is not None:
            result += f"kms_client={repr(self.kms_client)}, "

        if self.grant_tokens is not None:
            result += f"grant_tokens={repr(self.grant_tokens)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateAwsKmsMrkKeyringInput):
            return False
        attributes: list[str] = [
            "kms_key_id",
            "kms_client",
            "grant_tokens",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateAwsKmsMrkMultiKeyringInput:
    generator: Optional[str]
    kms_key_ids: Optional[list[str]]
    client_supplier: Optional[
        "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier"
    ]
    grant_tokens: Optional[list[str]]

    def __init__(
        self,
        *,
        generator: Optional[str] = None,
        kms_key_ids: Optional[list[str]] = None,
        client_supplier: Optional[
            "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier"
        ] = None,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating a AWS KMS MRK Multi-Keyring.

        :param generator: A symmetric AWS KMS Key or AWS KMS Multi-
            Region Key responsible for wrapping and unwrapping data
            keys. KMS.GenerateDataKey may be called with this key if the
            data key has not already been generated by another Keyring.
        :param kms_key_ids: A list of identifiers for the symmetric AWS
            KMS Keys and/or AWS KMS Multi-Region Keys (other than the
            generator) responsible for wrapping and unwrapping data
            keys.
        :param client_supplier: The Client Supplier which will be used
            to get KMS Clients for use with this Keyring. The Client
            Supplier will create a client for each region specified in
            the generator and kmsKeyIds ARNs. If not specified on input,
            the Default Client Supplier is used.
        :param grant_tokens: A list of grant tokens to be used when
            calling KMS.
        """
        self.generator = generator
        self.kms_key_ids = kms_key_ids
        self.client_supplier = client_supplier
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsMrkMultiKeyringInput to a dictionary."""
        d: Dict[str, Any] = {}

        if self.generator is not None:
            d["generator"] = self.generator

        if self.kms_key_ids is not None:
            d["kms_key_ids"] = self.kms_key_ids

        if self.client_supplier is not None:
            d["client_supplier"] = self.client_supplier.as_dict()

        if self.grant_tokens is not None:
            d["grant_tokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsMrkMultiKeyringInput":
        """Creates a CreateAwsKmsMrkMultiKeyringInput from a dictionary."""
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references import (
            ClientSupplier,
        )

        kwargs: Dict[str, Any] = {}

        if "generator" in d:
            kwargs["generator"] = d["generator"]

        if "kms_key_ids" in d:
            kwargs["kms_key_ids"] = d["kms_key_ids"]

        if "client_supplier" in d:
            kwargs["client_supplier"] = ClientSupplier.from_dict(d["client_supplier"])

        if "grant_tokens" in d:
            kwargs["grant_tokens"] = d["grant_tokens"]

        return CreateAwsKmsMrkMultiKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateAwsKmsMrkMultiKeyringInput("
        if self.generator is not None:
            result += f"generator={repr(self.generator)}, "

        if self.kms_key_ids is not None:
            result += f"kms_key_ids={repr(self.kms_key_ids)}, "

        if self.client_supplier is not None:
            result += f"client_supplier={repr(self.client_supplier)}, "

        if self.grant_tokens is not None:
            result += f"grant_tokens={repr(self.grant_tokens)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateAwsKmsMrkMultiKeyringInput):
            return False
        attributes: list[str] = [
            "generator",
            "kms_key_ids",
            "client_supplier",
            "grant_tokens",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateAwsKmsMultiKeyringInput:
    generator: Optional[str]
    kms_key_ids: Optional[list[str]]
    client_supplier: Optional[
        "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier"
    ]
    grant_tokens: Optional[list[str]]

    def __init__(
        self,
        *,
        generator: Optional[str] = None,
        kms_key_ids: Optional[list[str]] = None,
        client_supplier: Optional[
            "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier"
        ] = None,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating a AWS KMS Multi-Keyring.

        :param generator: A identifier for a symmetric AWS KMS Key
            responsible for wrapping and unwrapping data keys.
            KMS.GenerateDataKey may be called with this key if the data
            key has not already been generated by another Keyring. This
            should not be a AWS KMS Multi-Region Key.
        :param kms_key_ids: A list of identifiers for the symmetric AWS
            KMS Keys (other than the generator) responsible for wrapping
            and unwrapping data keys. This list should not contain AWS
            KMS Multi-Region Keys.
        :param client_supplier: The Client Supplier which will be used
            to get KMS Clients for use with this Keyring. The Client
            Supplier will create a client for each region specified in
            the generator and kmsKeyIds ARNs. If not specified on input,
            the Default Client Supplier is used.
        :param grant_tokens: A list of grant tokens to be used when
            calling KMS.
        """
        self.generator = generator
        self.kms_key_ids = kms_key_ids
        self.client_supplier = client_supplier
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsMultiKeyringInput to a dictionary."""
        d: Dict[str, Any] = {}

        if self.generator is not None:
            d["generator"] = self.generator

        if self.kms_key_ids is not None:
            d["kms_key_ids"] = self.kms_key_ids

        if self.client_supplier is not None:
            d["client_supplier"] = self.client_supplier.as_dict()

        if self.grant_tokens is not None:
            d["grant_tokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsMultiKeyringInput":
        """Creates a CreateAwsKmsMultiKeyringInput from a dictionary."""
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references import (
            ClientSupplier,
        )

        kwargs: Dict[str, Any] = {}

        if "generator" in d:
            kwargs["generator"] = d["generator"]

        if "kms_key_ids" in d:
            kwargs["kms_key_ids"] = d["kms_key_ids"]

        if "client_supplier" in d:
            kwargs["client_supplier"] = ClientSupplier.from_dict(d["client_supplier"])

        if "grant_tokens" in d:
            kwargs["grant_tokens"] = d["grant_tokens"]

        return CreateAwsKmsMultiKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateAwsKmsMultiKeyringInput("
        if self.generator is not None:
            result += f"generator={repr(self.generator)}, "

        if self.kms_key_ids is not None:
            result += f"kms_key_ids={repr(self.kms_key_ids)}, "

        if self.client_supplier is not None:
            result += f"client_supplier={repr(self.client_supplier)}, "

        if self.grant_tokens is not None:
            result += f"grant_tokens={repr(self.grant_tokens)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateAwsKmsMultiKeyringInput):
            return False
        attributes: list[str] = [
            "generator",
            "kms_key_ids",
            "client_supplier",
            "grant_tokens",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateAwsKmsRsaKeyringInput:
    public_key: Optional[bytes | bytearray]
    kms_key_id: str
    encryption_algorithm: dict[str, Any]
    kms_client: Optional[BaseClient]
    grant_tokens: Optional[list[str]]

    def __init__(
        self,
        *,
        kms_key_id: str,
        encryption_algorithm: dict[str, Any],
        public_key: Optional[bytes | bytearray] = None,
        kms_client: Optional[BaseClient] = None,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for creating a AWS KMS RSA Keyring.

        :param kms_key_id: The ARN for the asymmetric AWS KMS Key for
            RSA responsible for wrapping and unwrapping data keys.
        :param encryption_algorithm: The RSA algorithm used to wrap and
            unwrap data keys.
        :param public_key: The public RSA Key responsible for wrapping
            data keys, as a UTF8 encoded, PEM encoded X.509
            SubjectPublicKeyInfo structure. This should be the public
            key as exported from KMS. If not specified, this Keyring
            cannot be used on encrypt.
        :param kms_client: The KMS Client this Keyring will use to call
            KMS.
        :param grant_tokens: A list of grant tokens to be used when
            calling KMS.
        """
        self.kms_key_id = kms_key_id
        self.encryption_algorithm = encryption_algorithm
        self.public_key = public_key
        self.kms_client = kms_client
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsRsaKeyringInput to a dictionary."""
        d: Dict[str, Any] = {
            "kms_key_id": self.kms_key_id,
            "encryption_algorithm": self.encryption_algorithm,
        }

        if self.public_key is not None:
            d["public_key"] = self.public_key

        if self.kms_client is not None:
            d["kms_client"] = self.kms_client

        if self.grant_tokens is not None:
            d["grant_tokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsRsaKeyringInput":
        """Creates a CreateAwsKmsRsaKeyringInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "kms_key_id": d["kms_key_id"],
            "encryption_algorithm": d["encryption_algorithm"],
        }

        if "public_key" in d:
            kwargs["public_key"] = d["public_key"]

        if "kms_client" in d:
            kwargs["kms_client"] = d["kms_client"]

        if "grant_tokens" in d:
            kwargs["grant_tokens"] = d["grant_tokens"]

        return CreateAwsKmsRsaKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateAwsKmsRsaKeyringInput("
        if self.public_key is not None:
            result += f"public_key={repr(self.public_key)}, "

        if self.kms_key_id is not None:
            result += f"kms_key_id={repr(self.kms_key_id)}, "

        if self.encryption_algorithm is not None:
            result += f"encryption_algorithm={repr(self.encryption_algorithm)}, "

        if self.kms_client is not None:
            result += f"kms_client={repr(self.kms_client)}, "

        if self.grant_tokens is not None:
            result += f"grant_tokens={repr(self.grant_tokens)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateAwsKmsRsaKeyringInput):
            return False
        attributes: list[str] = [
            "public_key",
            "kms_key_id",
            "encryption_algorithm",
            "kms_client",
            "grant_tokens",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateCryptographicMaterialsCacheInput:
    cache: CacheType

    def __init__(
        self,
        *,
        cache: CacheType,
    ):
        """
        :param cache: Which type of local cache to use.
        """
        self.cache = cache

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateCryptographicMaterialsCacheInput to a
        dictionary."""
        return {
            "cache": self.cache.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateCryptographicMaterialsCacheInput":
        """Creates a CreateCryptographicMaterialsCacheInput from a
        dictionary."""
        kwargs: Dict[str, Any] = {
            "cache": _cache_type_from_dict(d["cache"]),
        }

        return CreateCryptographicMaterialsCacheInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateCryptographicMaterialsCacheInput("
        if self.cache is not None:
            result += f"cache={repr(self.cache)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateCryptographicMaterialsCacheInput):
            return False
        attributes: list[str] = [
            "cache",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateDefaultClientSupplierInput:
    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateDefaultClientSupplierInput to a dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateDefaultClientSupplierInput":
        """Creates a CreateDefaultClientSupplierInput from a dictionary."""
        return CreateDefaultClientSupplierInput()

    def __repr__(self) -> str:
        result = "CreateDefaultClientSupplierInput("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, CreateDefaultClientSupplierInput)


class CreateDefaultCryptographicMaterialsManagerInput:
    keyring: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring"

    def __init__(
        self,
        *,
        keyring: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring",
    ):
        """Inputs for creating a Default Cryptographic Materials Manager.

        :param keyring: The Keyring that the created Default
            Cryptographic Materials Manager will use to wrap data keys.
        """
        self.keyring = keyring

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateDefaultCryptographicMaterialsManagerInput to a
        dictionary."""
        return {
            "keyring": self.keyring.as_dict(),
        }

    @staticmethod
    def from_dict(
        d: Dict[str, Any],
    ) -> "CreateDefaultCryptographicMaterialsManagerInput":
        """Creates a CreateDefaultCryptographicMaterialsManagerInput from a
        dictionary."""
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references import (
            Keyring,
        )

        kwargs: Dict[str, Any] = {
            "keyring": Keyring.from_dict(d["keyring"]),
        }

        return CreateDefaultCryptographicMaterialsManagerInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateDefaultCryptographicMaterialsManagerInput("
        if self.keyring is not None:
            result += f"keyring={repr(self.keyring)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateDefaultCryptographicMaterialsManagerInput):
            return False
        attributes: list[str] = [
            "keyring",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateMultiKeyringInput:
    generator: Optional[
        "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring"
    ]
    child_keyrings: list[
        "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring"
    ]

    def __init__(
        self,
        *,
        child_keyrings: list[
            "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring"
        ],
        generator: Optional[
            "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring"
        ] = None,
    ):
        """Inputs for creating a Multi-Keyring.

        :param child_keyrings: A list of keyrings (other than the
            generator) responsible for wrapping and unwrapping the data
            key.
        :param generator: A keyring responsible for wrapping and
            unwrapping the data key. This is the first keyring that will
            be used to wrap the data key, and may be responsible for
            additionally generating the data key.
        """
        self.child_keyrings = child_keyrings
        self.generator = generator

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateMultiKeyringInput to a dictionary."""
        d: Dict[str, Any] = {
            "child_keyrings": self.child_keyrings,
        }

        if self.generator is not None:
            d["generator"] = self.generator.as_dict()

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateMultiKeyringInput":
        """Creates a CreateMultiKeyringInput from a dictionary."""
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references import (
            Keyring,
        )

        kwargs: Dict[str, Any] = {
            "child_keyrings": d["child_keyrings"],
        }

        if "generator" in d:
            kwargs["generator"] = Keyring.from_dict(d["generator"])

        return CreateMultiKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateMultiKeyringInput("
        if self.generator is not None:
            result += f"generator={repr(self.generator)}, "

        if self.child_keyrings is not None:
            result += f"child_keyrings={repr(self.child_keyrings)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateMultiKeyringInput):
            return False
        attributes: list[str] = [
            "generator",
            "child_keyrings",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateRawAesKeyringInput:
    key_namespace: str
    key_name: str
    wrapping_key: bytes | bytearray
    wrapping_alg: str

    def __init__(
        self,
        *,
        key_namespace: str,
        key_name: str,
        wrapping_key: bytes | bytearray,
        wrapping_alg: str,
    ):
        """Inputs for creating a Raw AES Keyring.

        :param key_namespace: A namespace associated with this wrapping
            key.
        :param key_name: A name associated with this wrapping key.
        :param wrapping_key: The AES key used with AES_GCM encryption
            and decryption.
        :param wrapping_alg: The AES_GCM algorithm this Keyring uses to
            wrap and unwrap data keys.
        """
        self.key_namespace = key_namespace
        self.key_name = key_name
        self.wrapping_key = wrapping_key
        self.wrapping_alg = wrapping_alg

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateRawAesKeyringInput to a dictionary."""
        return {
            "key_namespace": self.key_namespace,
            "key_name": self.key_name,
            "wrapping_key": self.wrapping_key,
            "wrapping_alg": self.wrapping_alg,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateRawAesKeyringInput":
        """Creates a CreateRawAesKeyringInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "key_namespace": d["key_namespace"],
            "key_name": d["key_name"],
            "wrapping_key": d["wrapping_key"],
            "wrapping_alg": d["wrapping_alg"],
        }

        return CreateRawAesKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateRawAesKeyringInput("
        if self.key_namespace is not None:
            result += f"key_namespace={repr(self.key_namespace)}, "

        if self.key_name is not None:
            result += f"key_name={repr(self.key_name)}, "

        if self.wrapping_key is not None:
            result += f"wrapping_key={repr(self.wrapping_key)}, "

        if self.wrapping_alg is not None:
            result += f"wrapping_alg={repr(self.wrapping_alg)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateRawAesKeyringInput):
            return False
        attributes: list[str] = [
            "key_namespace",
            "key_name",
            "wrapping_key",
            "wrapping_alg",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class EphemeralPrivateKeyToStaticPublicKeyInput:
    recipient_public_key: bytes | bytearray

    def __init__(
        self,
        *,
        recipient_public_key: bytes | bytearray,
    ):
        """Inputs for creating a EphemeralPrivateKeyToStaticPublicKey
        Configuration.

        :param recipient_public_key: The recipient's public key. MUST be
            DER encoded.
        """
        self.recipient_public_key = recipient_public_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the EphemeralPrivateKeyToStaticPublicKeyInput to a
        dictionary."""
        return {
            "recipient_public_key": self.recipient_public_key,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EphemeralPrivateKeyToStaticPublicKeyInput":
        """Creates a EphemeralPrivateKeyToStaticPublicKeyInput from a
        dictionary."""
        kwargs: Dict[str, Any] = {
            "recipient_public_key": d["recipient_public_key"],
        }

        return EphemeralPrivateKeyToStaticPublicKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "EphemeralPrivateKeyToStaticPublicKeyInput("
        if self.recipient_public_key is not None:
            result += f"recipient_public_key={repr(self.recipient_public_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EphemeralPrivateKeyToStaticPublicKeyInput):
            return False
        attributes: list[str] = [
            "recipient_public_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class PublicKeyDiscoveryInput:
    recipient_static_private_key: bytes | bytearray

    def __init__(
        self,
        *,
        recipient_static_private_key: bytes | bytearray,
    ):
        """Inputs for creating a PublicKeyDiscovery Configuration.

        :param recipient_static_private_key: The sender's private key.
            MUST be PEM encoded.
        """
        self.recipient_static_private_key = recipient_static_private_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the PublicKeyDiscoveryInput to a dictionary."""
        return {
            "recipient_static_private_key": self.recipient_static_private_key,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "PublicKeyDiscoveryInput":
        """Creates a PublicKeyDiscoveryInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "recipient_static_private_key": d["recipient_static_private_key"],
        }

        return PublicKeyDiscoveryInput(**kwargs)

    def __repr__(self) -> str:
        result = "PublicKeyDiscoveryInput("
        if self.recipient_static_private_key is not None:
            result += f"recipient_static_private_key={repr(self.recipient_static_private_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, PublicKeyDiscoveryInput):
            return False
        attributes: list[str] = [
            "recipient_static_private_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class RawPrivateKeyToStaticPublicKeyInput:
    sender_static_private_key: bytes | bytearray
    recipient_public_key: bytes | bytearray

    def __init__(
        self,
        *,
        sender_static_private_key: bytes | bytearray,
        recipient_public_key: bytes | bytearray,
    ):
        """Inputs for creating a RawPrivateKeyToStaticPublicKey Configuration.

        :param sender_static_private_key: The sender's private key. MUST
            be PEM encoded.
        :param recipient_public_key: The recipient's public key. MUST be
            DER encoded.
        """
        self.sender_static_private_key = sender_static_private_key
        self.recipient_public_key = recipient_public_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the RawPrivateKeyToStaticPublicKeyInput to a dictionary."""
        return {
            "sender_static_private_key": self.sender_static_private_key,
            "recipient_public_key": self.recipient_public_key,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RawPrivateKeyToStaticPublicKeyInput":
        """Creates a RawPrivateKeyToStaticPublicKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "sender_static_private_key": d["sender_static_private_key"],
            "recipient_public_key": d["recipient_public_key"],
        }

        return RawPrivateKeyToStaticPublicKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "RawPrivateKeyToStaticPublicKeyInput("
        if self.sender_static_private_key is not None:
            result += (
                f"sender_static_private_key={repr(self.sender_static_private_key)}, "
            )

        if self.recipient_public_key is not None:
            result += f"recipient_public_key={repr(self.recipient_public_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, RawPrivateKeyToStaticPublicKeyInput):
            return False
        attributes: list[str] = [
            "sender_static_private_key",
            "recipient_public_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class RawEcdhStaticConfigurationsPublicKeyDiscovery:
    """Inputs for creating a PublicKeyDiscovery Configuration."""

    def __init__(self, value: PublicKeyDiscoveryInput):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"PublicKeyDiscovery": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RawEcdhStaticConfigurationsPublicKeyDiscovery":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return RawEcdhStaticConfigurationsPublicKeyDiscovery(
            PublicKeyDiscoveryInput.from_dict(d["PublicKeyDiscovery"])
        )

    def __repr__(self) -> str:
        return f"RawEcdhStaticConfigurationsPublicKeyDiscovery(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, RawEcdhStaticConfigurationsPublicKeyDiscovery):
            return False
        return self.value == other.value


class RawEcdhStaticConfigurationsRawPrivateKeyToStaticPublicKey:
    """Inputs for creating a RawPrivateKeyToStaticPublicKey Configuration."""

    def __init__(self, value: RawPrivateKeyToStaticPublicKeyInput):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"RawPrivateKeyToStaticPublicKey": self.value.as_dict()}

    @staticmethod
    def from_dict(
        d: Dict[str, Any],
    ) -> "RawEcdhStaticConfigurationsRawPrivateKeyToStaticPublicKey":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return RawEcdhStaticConfigurationsRawPrivateKeyToStaticPublicKey(
            RawPrivateKeyToStaticPublicKeyInput.from_dict(
                d["RawPrivateKeyToStaticPublicKey"]
            )
        )

    def __repr__(self) -> str:
        return f"RawEcdhStaticConfigurationsRawPrivateKeyToStaticPublicKey(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(
            other, RawEcdhStaticConfigurationsRawPrivateKeyToStaticPublicKey
        ):
            return False
        return self.value == other.value


class RawEcdhStaticConfigurationsEphemeralPrivateKeyToStaticPublicKey:
    """Inputs for creating a EphemeralPrivateKeyToStaticPublicKey
    Configuration."""

    def __init__(self, value: EphemeralPrivateKeyToStaticPublicKeyInput):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"EphemeralPrivateKeyToStaticPublicKey": self.value.as_dict()}

    @staticmethod
    def from_dict(
        d: Dict[str, Any],
    ) -> "RawEcdhStaticConfigurationsEphemeralPrivateKeyToStaticPublicKey":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return RawEcdhStaticConfigurationsEphemeralPrivateKeyToStaticPublicKey(
            EphemeralPrivateKeyToStaticPublicKeyInput.from_dict(
                d["EphemeralPrivateKeyToStaticPublicKey"]
            )
        )

    def __repr__(self) -> str:
        return f"RawEcdhStaticConfigurationsEphemeralPrivateKeyToStaticPublicKey(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(
            other, RawEcdhStaticConfigurationsEphemeralPrivateKeyToStaticPublicKey
        ):
            return False
        return self.value == other.value


class RawEcdhStaticConfigurationsUnknown:
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to
    receive the parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RawEcdhStaticConfigurationsUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return RawEcdhStaticConfigurationsUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"RawEcdhStaticConfigurationsUnknown(tag={self.tag})"


# List of configurations when using RawEcdhStaticConfigurations.
RawEcdhStaticConfigurations = Union[
    RawEcdhStaticConfigurationsPublicKeyDiscovery,
    RawEcdhStaticConfigurationsRawPrivateKeyToStaticPublicKey,
    RawEcdhStaticConfigurationsEphemeralPrivateKeyToStaticPublicKey,
    RawEcdhStaticConfigurationsUnknown,
]


def _raw_ecdh_static_configurations_from_dict(
    d: Dict[str, Any],
) -> RawEcdhStaticConfigurations:
    if "PublicKeyDiscovery" in d:
        return RawEcdhStaticConfigurationsPublicKeyDiscovery.from_dict(d)

    if "RawPrivateKeyToStaticPublicKey" in d:
        return RawEcdhStaticConfigurationsRawPrivateKeyToStaticPublicKey.from_dict(d)

    if "EphemeralPrivateKeyToStaticPublicKey" in d:
        return (
            RawEcdhStaticConfigurationsEphemeralPrivateKeyToStaticPublicKey.from_dict(d)
        )

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class CreateRawEcdhKeyringInput:
    key_agreement_scheme: RawEcdhStaticConfigurations
    curve_spec: str

    def __init__(
        self,
        *,
        key_agreement_scheme: RawEcdhStaticConfigurations,
        curve_spec: str,
    ):
        """Inputs for creating a raw ECDH Keyring.

        :param key_agreement_scheme: The Key Agreement Scheme
            configuration that is responsible for how the shared secret
            is calculated.
        :param curve_spec: The the curve on which the points for the
            sender's private and recipient's public key lie.
        """
        self.key_agreement_scheme = key_agreement_scheme
        self.curve_spec = curve_spec

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateRawEcdhKeyringInput to a dictionary."""
        return {
            "key_agreement_scheme": self.key_agreement_scheme.as_dict(),
            "curve_spec": self.curve_spec,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateRawEcdhKeyringInput":
        """Creates a CreateRawEcdhKeyringInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "key_agreement_scheme": _raw_ecdh_static_configurations_from_dict(
                d["key_agreement_scheme"]
            ),
            "curve_spec": d["curve_spec"],
        }

        return CreateRawEcdhKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateRawEcdhKeyringInput("
        if self.key_agreement_scheme is not None:
            result += f"key_agreement_scheme={repr(self.key_agreement_scheme)}, "

        if self.curve_spec is not None:
            result += f"curve_spec={repr(self.curve_spec)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateRawEcdhKeyringInput):
            return False
        attributes: list[str] = [
            "key_agreement_scheme",
            "curve_spec",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class PaddingScheme:
    PKCS1 = "PKCS1"

    OAEP_SHA1_MGF1 = "OAEP_SHA1_MGF1"

    OAEP_SHA256_MGF1 = "OAEP_SHA256_MGF1"

    OAEP_SHA384_MGF1 = "OAEP_SHA384_MGF1"

    OAEP_SHA512_MGF1 = "OAEP_SHA512_MGF1"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset(
        {
            "PKCS1",
            "OAEP_SHA1_MGF1",
            "OAEP_SHA256_MGF1",
            "OAEP_SHA384_MGF1",
            "OAEP_SHA512_MGF1",
        }
    )


class CreateRawRsaKeyringInput:
    key_namespace: str
    key_name: str
    padding_scheme: str
    public_key: Optional[bytes | bytearray]
    private_key: Optional[bytes | bytearray]

    def __init__(
        self,
        *,
        key_namespace: str,
        key_name: str,
        padding_scheme: str,
        public_key: Optional[bytes | bytearray] = None,
        private_key: Optional[bytes | bytearray] = None,
    ):
        """Inputs for creating a Raw RAW Keyring.

        :param key_namespace: A namespace associated with this wrapping
            key.
        :param key_name: A name associated with this wrapping key.
        :param padding_scheme: The RSA padding scheme to use with this
            keyring.
        :param public_key: The public RSA Key responsible for wrapping
            data keys, as a UTF8 encoded, PEM encoded X.509
            SubjectPublicKeyInfo structure. If not specified, this
            Keyring cannot be used on encrypt. A public key and/or a
            private key must be specified.
        :param private_key: The private RSA Key responsible for wrapping
            data keys, as a UTF8 encoded, PEM encoded PKCS #8
            PrivateKeyInfo structure. If not specified, this Keyring
            cannot be used on decrypt. A public key and/or a private key
            must be specified.
        """
        self.key_namespace = key_namespace
        self.key_name = key_name
        self.padding_scheme = padding_scheme
        self.public_key = public_key
        self.private_key = private_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateRawRsaKeyringInput to a dictionary."""
        d: Dict[str, Any] = {
            "key_namespace": self.key_namespace,
            "key_name": self.key_name,
            "padding_scheme": self.padding_scheme,
        }

        if self.public_key is not None:
            d["public_key"] = self.public_key

        if self.private_key is not None:
            d["private_key"] = self.private_key

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateRawRsaKeyringInput":
        """Creates a CreateRawRsaKeyringInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "key_namespace": d["key_namespace"],
            "key_name": d["key_name"],
            "padding_scheme": d["padding_scheme"],
        }

        if "public_key" in d:
            kwargs["public_key"] = d["public_key"]

        if "private_key" in d:
            kwargs["private_key"] = d["private_key"]

        return CreateRawRsaKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateRawRsaKeyringInput("
        if self.key_namespace is not None:
            result += f"key_namespace={repr(self.key_namespace)}, "

        if self.key_name is not None:
            result += f"key_name={repr(self.key_name)}, "

        if self.padding_scheme is not None:
            result += f"padding_scheme={repr(self.padding_scheme)}, "

        if self.public_key is not None:
            result += f"public_key={repr(self.public_key)}, "

        if self.private_key is not None:
            result += f"private_key={repr(self.private_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateRawRsaKeyringInput):
            return False
        attributes: list[str] = [
            "key_namespace",
            "key_name",
            "padding_scheme",
            "public_key",
            "private_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateRequiredEncryptionContextCMMInput:
    underlying_cmm: Optional[
        "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.CryptographicMaterialsManager"
    ]
    keyring: Optional[
        "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring"
    ]
    required_encryption_context_keys: list[str]

    def __init__(
        self,
        *,
        required_encryption_context_keys: list[str],
        underlying_cmm: Optional[
            "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.CryptographicMaterialsManager"
        ] = None,
        keyring: Optional[
            "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring"
        ] = None,
    ):
        """Inputs for creating an Required Encryption Context Cryptographic
        Materials Manager.

        :param required_encryption_context_keys: A list of Encryption
            Context keys which are required to be supplied during
            encryption and decryption, and correspond to Encryption
            Context key-value pairs which are not stored on the
            resulting message.
        :param underlying_cmm: The Cryptographic Materials Manager that
            the created Required Encryption Context Cryptographic
            Materials Manager will delegate to. Either a Keyring or
            underlying Cryptographic Materials Manager must be
            specified.
        :param keyring: The Keyring that the created Cryptographic
            Materials Manager will use to wrap data keys. The created
            Required Encryption Context CMM will delegate to a Default
            Cryptographic Materials Manager created with this Keyring.
            Either a Keyring or an underlying Cryptographic Materials
            Manager must be specified as input.
        """
        self.required_encryption_context_keys = required_encryption_context_keys
        self.underlying_cmm = underlying_cmm
        self.keyring = keyring

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateRequiredEncryptionContextCMMInput to a
        dictionary."""
        d: Dict[str, Any] = {
            "required_encryption_context_keys": self.required_encryption_context_keys,
        }

        if self.underlying_cmm is not None:
            d["underlying_cmm"] = self.underlying_cmm.as_dict()

        if self.keyring is not None:
            d["keyring"] = self.keyring.as_dict()

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateRequiredEncryptionContextCMMInput":
        """Creates a CreateRequiredEncryptionContextCMMInput from a
        dictionary."""
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references import (
            CryptographicMaterialsManager,
        )
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references import (
            Keyring,
        )

        kwargs: Dict[str, Any] = {
            "required_encryption_context_keys": d["required_encryption_context_keys"],
        }

        if "underlying_cmm" in d:
            kwargs["underlying_cmm"] = CryptographicMaterialsManager.from_dict(
                d["underlying_cmm"]
            )

        if "keyring" in d:
            kwargs["keyring"] = Keyring.from_dict(d["keyring"])

        return CreateRequiredEncryptionContextCMMInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateRequiredEncryptionContextCMMInput("
        if self.underlying_cmm is not None:
            result += f"underlying_cmm={repr(self.underlying_cmm)}, "

        if self.keyring is not None:
            result += f"keyring={repr(self.keyring)}, "

        if self.required_encryption_context_keys is not None:
            result += f"required_encryption_context_keys={repr(self.required_encryption_context_keys)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateRequiredEncryptionContextCMMInput):
            return False
        attributes: list[str] = [
            "underlying_cmm",
            "keyring",
            "required_encryption_context_keys",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class DeleteCacheEntryInput:
    identifier: bytes | bytearray

    def __init__(
        self,
        *,
        identifier: bytes | bytearray,
    ):
        self.identifier = identifier

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DeleteCacheEntryInput to a dictionary."""
        return {
            "identifier": self.identifier,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DeleteCacheEntryInput":
        """Creates a DeleteCacheEntryInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
        }

        return DeleteCacheEntryInput(**kwargs)

    def __repr__(self) -> str:
        result = "DeleteCacheEntryInput("
        if self.identifier is not None:
            result += f"identifier={repr(self.identifier)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DeleteCacheEntryInput):
            return False
        attributes: list[str] = [
            "identifier",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetCacheEntryInput:
    identifier: bytes | bytearray
    bytes_used: Optional[int]

    def __init__(
        self,
        *,
        identifier: bytes | bytearray,
        bytes_used: Optional[int] = None,
    ):
        self.identifier = identifier
        self.bytes_used = bytes_used

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetCacheEntryInput to a dictionary."""
        d: Dict[str, Any] = {
            "identifier": self.identifier,
        }

        if self.bytes_used is not None:
            d["bytes_used"] = self.bytes_used

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetCacheEntryInput":
        """Creates a GetCacheEntryInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
        }

        if "bytes_used" in d:
            kwargs["bytes_used"] = d["bytes_used"]

        return GetCacheEntryInput(**kwargs)

    def __repr__(self) -> str:
        result = "GetCacheEntryInput("
        if self.identifier is not None:
            result += f"identifier={repr(self.identifier)}, "

        if self.bytes_used is not None:
            result += f"bytes_used={repr(self.bytes_used)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetCacheEntryInput):
            return False
        attributes: list[str] = [
            "identifier",
            "bytes_used",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class DecryptionMaterials:
    algorithm_suite: AlgorithmSuiteInfo
    encryption_context: dict[str, str]
    required_encryption_context_keys: list[str]
    plaintext_data_key: Optional[bytes | bytearray]
    verification_key: Optional[bytes | bytearray]
    symmetric_signing_key: Optional[bytes | bytearray]

    def __init__(
        self,
        *,
        algorithm_suite: AlgorithmSuiteInfo,
        encryption_context: dict[str, str],
        required_encryption_context_keys: list[str],
        plaintext_data_key: Optional[bytes | bytearray] = None,
        verification_key: Optional[bytes | bytearray] = None,
        symmetric_signing_key: Optional[bytes | bytearray] = None,
    ):
        self.algorithm_suite = algorithm_suite
        self.encryption_context = encryption_context
        self.required_encryption_context_keys = required_encryption_context_keys
        self.plaintext_data_key = plaintext_data_key
        self.verification_key = verification_key
        self.symmetric_signing_key = symmetric_signing_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DecryptionMaterials to a dictionary."""
        d: Dict[str, Any] = {
            "algorithm_suite": self.algorithm_suite.as_dict(),
            "encryption_context": self.encryption_context,
            "required_encryption_context_keys": self.required_encryption_context_keys,
        }

        if self.plaintext_data_key is not None:
            d["plaintext_data_key"] = self.plaintext_data_key

        if self.verification_key is not None:
            d["verification_key"] = self.verification_key

        if self.symmetric_signing_key is not None:
            d["symmetric_signing_key"] = self.symmetric_signing_key

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DecryptionMaterials":
        """Creates a DecryptionMaterials from a dictionary."""
        kwargs: Dict[str, Any] = {
            "algorithm_suite": AlgorithmSuiteInfo.from_dict(d["algorithm_suite"]),
            "encryption_context": d["encryption_context"],
            "required_encryption_context_keys": d["required_encryption_context_keys"],
        }

        if "plaintext_data_key" in d:
            kwargs["plaintext_data_key"] = d["plaintext_data_key"]

        if "verification_key" in d:
            kwargs["verification_key"] = d["verification_key"]

        if "symmetric_signing_key" in d:
            kwargs["symmetric_signing_key"] = d["symmetric_signing_key"]

        return DecryptionMaterials(**kwargs)

    def __repr__(self) -> str:
        result = "DecryptionMaterials("
        if self.algorithm_suite is not None:
            result += f"algorithm_suite={repr(self.algorithm_suite)}, "

        if self.encryption_context is not None:
            result += f"encryption_context={repr(self.encryption_context)}, "

        if self.required_encryption_context_keys is not None:
            result += f"required_encryption_context_keys={repr(self.required_encryption_context_keys)}, "

        if self.plaintext_data_key is not None:
            result += f"plaintext_data_key={repr(self.plaintext_data_key)}, "

        if self.verification_key is not None:
            result += f"verification_key={repr(self.verification_key)}, "

        if self.symmetric_signing_key is not None:
            result += f"symmetric_signing_key={repr(self.symmetric_signing_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DecryptionMaterials):
            return False
        attributes: list[str] = [
            "algorithm_suite",
            "encryption_context",
            "required_encryption_context_keys",
            "plaintext_data_key",
            "verification_key",
            "symmetric_signing_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class EncryptedDataKey:
    key_provider_id: str
    key_provider_info: bytes | bytearray
    ciphertext: bytes | bytearray

    def __init__(
        self,
        *,
        key_provider_id: str,
        key_provider_info: bytes | bytearray,
        ciphertext: bytes | bytearray,
    ):
        self.key_provider_id = key_provider_id
        self.key_provider_info = key_provider_info
        self.ciphertext = ciphertext

    def as_dict(self) -> Dict[str, Any]:
        """Converts the EncryptedDataKey to a dictionary."""
        return {
            "key_provider_id": self.key_provider_id,
            "key_provider_info": self.key_provider_info,
            "ciphertext": self.ciphertext,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EncryptedDataKey":
        """Creates a EncryptedDataKey from a dictionary."""
        kwargs: Dict[str, Any] = {
            "key_provider_id": d["key_provider_id"],
            "key_provider_info": d["key_provider_info"],
            "ciphertext": d["ciphertext"],
        }

        return EncryptedDataKey(**kwargs)

    def __repr__(self) -> str:
        result = "EncryptedDataKey("
        if self.key_provider_id is not None:
            result += f"key_provider_id={repr(self.key_provider_id)}, "

        if self.key_provider_info is not None:
            result += f"key_provider_info={repr(self.key_provider_info)}, "

        if self.ciphertext is not None:
            result += f"ciphertext={repr(self.ciphertext)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EncryptedDataKey):
            return False
        attributes: list[str] = [
            "key_provider_id",
            "key_provider_info",
            "ciphertext",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class EncryptionMaterials:
    algorithm_suite: AlgorithmSuiteInfo
    encryption_context: dict[str, str]
    encrypted_data_keys: list[EncryptedDataKey]
    required_encryption_context_keys: list[str]
    plaintext_data_key: Optional[bytes | bytearray]
    signing_key: Optional[bytes | bytearray]
    symmetric_signing_keys: Optional[list[bytes | bytearray]]

    def __init__(
        self,
        *,
        algorithm_suite: AlgorithmSuiteInfo,
        encryption_context: dict[str, str],
        encrypted_data_keys: list[EncryptedDataKey],
        required_encryption_context_keys: list[str],
        plaintext_data_key: Optional[bytes | bytearray] = None,
        signing_key: Optional[bytes | bytearray] = None,
        symmetric_signing_keys: Optional[list[bytes | bytearray]] = None,
    ):
        self.algorithm_suite = algorithm_suite
        self.encryption_context = encryption_context
        self.encrypted_data_keys = encrypted_data_keys
        self.required_encryption_context_keys = required_encryption_context_keys
        self.plaintext_data_key = plaintext_data_key
        self.signing_key = signing_key
        self.symmetric_signing_keys = symmetric_signing_keys

    def as_dict(self) -> Dict[str, Any]:
        """Converts the EncryptionMaterials to a dictionary."""
        d: Dict[str, Any] = {
            "algorithm_suite": self.algorithm_suite.as_dict(),
            "encryption_context": self.encryption_context,
            "encrypted_data_keys": _encrypted_data_key_list_as_dict(
                self.encrypted_data_keys
            ),
            "required_encryption_context_keys": self.required_encryption_context_keys,
        }

        if self.plaintext_data_key is not None:
            d["plaintext_data_key"] = self.plaintext_data_key

        if self.signing_key is not None:
            d["signing_key"] = self.signing_key

        if self.symmetric_signing_keys is not None:
            d["symmetric_signing_keys"] = self.symmetric_signing_keys

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EncryptionMaterials":
        """Creates a EncryptionMaterials from a dictionary."""
        kwargs: Dict[str, Any] = {
            "algorithm_suite": AlgorithmSuiteInfo.from_dict(d["algorithm_suite"]),
            "encryption_context": d["encryption_context"],
            "encrypted_data_keys": _encrypted_data_key_list_from_dict(
                d["encrypted_data_keys"]
            ),
            "required_encryption_context_keys": d["required_encryption_context_keys"],
        }

        if "plaintext_data_key" in d:
            kwargs["plaintext_data_key"] = d["plaintext_data_key"]

        if "signing_key" in d:
            kwargs["signing_key"] = d["signing_key"]

        if "symmetric_signing_keys" in d:
            kwargs["symmetric_signing_keys"] = d["symmetric_signing_keys"]

        return EncryptionMaterials(**kwargs)

    def __repr__(self) -> str:
        result = "EncryptionMaterials("
        if self.algorithm_suite is not None:
            result += f"algorithm_suite={repr(self.algorithm_suite)}, "

        if self.encryption_context is not None:
            result += f"encryption_context={repr(self.encryption_context)}, "

        if self.encrypted_data_keys is not None:
            result += f"encrypted_data_keys={repr(self.encrypted_data_keys)}, "

        if self.required_encryption_context_keys is not None:
            result += f"required_encryption_context_keys={repr(self.required_encryption_context_keys)}, "

        if self.plaintext_data_key is not None:
            result += f"plaintext_data_key={repr(self.plaintext_data_key)}, "

        if self.signing_key is not None:
            result += f"signing_key={repr(self.signing_key)}, "

        if self.symmetric_signing_keys is not None:
            result += f"symmetric_signing_keys={repr(self.symmetric_signing_keys)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EncryptionMaterials):
            return False
        attributes: list[str] = [
            "algorithm_suite",
            "encryption_context",
            "encrypted_data_keys",
            "required_encryption_context_keys",
            "plaintext_data_key",
            "signing_key",
            "symmetric_signing_keys",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class MaterialsEncryption:
    def __init__(self, value: EncryptionMaterials):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"Encryption": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MaterialsEncryption":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return MaterialsEncryption(EncryptionMaterials.from_dict(d["Encryption"]))

    def __repr__(self) -> str:
        return f"MaterialsEncryption(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MaterialsEncryption):
            return False
        return self.value == other.value


class MaterialsDecryption:
    def __init__(self, value: DecryptionMaterials):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"Decryption": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MaterialsDecryption":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return MaterialsDecryption(DecryptionMaterials.from_dict(d["Decryption"]))

    def __repr__(self) -> str:
        return f"MaterialsDecryption(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MaterialsDecryption):
            return False
        return self.value == other.value


class MaterialsBranchKey:
    def __init__(self, value: BranchKeyMaterials):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"BranchKey": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MaterialsBranchKey":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return MaterialsBranchKey(BranchKeyMaterials.from_dict(d["BranchKey"]))

    def __repr__(self) -> str:
        return f"MaterialsBranchKey(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MaterialsBranchKey):
            return False
        return self.value == other.value


class MaterialsBeaconKey:
    def __init__(self, value: BeaconKeyMaterials):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"BeaconKey": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MaterialsBeaconKey":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return MaterialsBeaconKey(BeaconKeyMaterials.from_dict(d["BeaconKey"]))

    def __repr__(self) -> str:
        return f"MaterialsBeaconKey(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MaterialsBeaconKey):
            return False
        return self.value == other.value


class MaterialsUnknown:
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to
    receive the parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MaterialsUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return MaterialsUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"MaterialsUnknown(tag={self.tag})"


Materials = Union[
    MaterialsEncryption,
    MaterialsDecryption,
    MaterialsBranchKey,
    MaterialsBeaconKey,
    MaterialsUnknown,
]


def _materials_from_dict(d: Dict[str, Any]) -> Materials:
    if "Encryption" in d:
        return MaterialsEncryption.from_dict(d)

    if "Decryption" in d:
        return MaterialsDecryption.from_dict(d)

    if "BranchKey" in d:
        return MaterialsBranchKey.from_dict(d)

    if "BeaconKey" in d:
        return MaterialsBeaconKey.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class GetCacheEntryOutput:
    materials: Materials
    creation_time: int
    expiry_time: int
    messages_used: int
    bytes_used: int

    def __init__(
        self,
        *,
        materials: Materials,
        creation_time: int = 0,
        expiry_time: int = 0,
        messages_used: int = 0,
        bytes_used: int = 0,
    ):
        self.materials = materials
        if (creation_time is not None) and (creation_time < 0):
            raise ValueError("creation_time must be greater than or equal to 0")

        self.creation_time = creation_time
        if (expiry_time is not None) and (expiry_time < 0):
            raise ValueError("expiry_time must be greater than or equal to 0")

        self.expiry_time = expiry_time
        if (messages_used is not None) and (messages_used < 0):
            raise ValueError("messages_used must be greater than or equal to 0")

        self.messages_used = messages_used
        if (bytes_used is not None) and (bytes_used < 0):
            raise ValueError("bytes_used must be greater than or equal to 0")

        self.bytes_used = bytes_used

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetCacheEntryOutput to a dictionary."""
        d: Dict[str, Any] = {
            "materials": self.materials.as_dict(),
        }

        if self.creation_time is not None:
            d["creation_time"] = self.creation_time

        if self.expiry_time is not None:
            d["expiry_time"] = self.expiry_time

        if self.messages_used is not None:
            d["messages_used"] = self.messages_used

        if self.bytes_used is not None:
            d["bytes_used"] = self.bytes_used

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetCacheEntryOutput":
        """Creates a GetCacheEntryOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "materials": _materials_from_dict(d["materials"]),
        }

        if "creation_time" in d:
            kwargs["creation_time"] = d["creation_time"]

        if "expiry_time" in d:
            kwargs["expiry_time"] = d["expiry_time"]

        if "messages_used" in d:
            kwargs["messages_used"] = d["messages_used"]

        if "bytes_used" in d:
            kwargs["bytes_used"] = d["bytes_used"]

        return GetCacheEntryOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GetCacheEntryOutput("
        if self.materials is not None:
            result += f"materials={repr(self.materials)}, "

        if self.creation_time is not None:
            result += f"creation_time={repr(self.creation_time)}, "

        if self.expiry_time is not None:
            result += f"expiry_time={repr(self.expiry_time)}, "

        if self.messages_used is not None:
            result += f"messages_used={repr(self.messages_used)}, "

        if self.bytes_used is not None:
            result += f"bytes_used={repr(self.bytes_used)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetCacheEntryOutput):
            return False
        attributes: list[str] = [
            "materials",
            "creation_time",
            "expiry_time",
            "messages_used",
            "bytes_used",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class PutCacheEntryInput:
    identifier: bytes | bytearray
    materials: Materials
    creation_time: int
    expiry_time: int
    messages_used: int
    bytes_used: int

    def __init__(
        self,
        *,
        identifier: bytes | bytearray,
        materials: Materials,
        creation_time: int = 0,
        expiry_time: int = 0,
        messages_used: int = 0,
        bytes_used: int = 0,
    ):
        self.identifier = identifier
        self.materials = materials
        if (creation_time is not None) and (creation_time < 0):
            raise ValueError("creation_time must be greater than or equal to 0")

        self.creation_time = creation_time
        if (expiry_time is not None) and (expiry_time < 0):
            raise ValueError("expiry_time must be greater than or equal to 0")

        self.expiry_time = expiry_time
        if (messages_used is not None) and (messages_used < 0):
            raise ValueError("messages_used must be greater than or equal to 0")

        self.messages_used = messages_used
        if (bytes_used is not None) and (bytes_used < 0):
            raise ValueError("bytes_used must be greater than or equal to 0")

        self.bytes_used = bytes_used

    def as_dict(self) -> Dict[str, Any]:
        """Converts the PutCacheEntryInput to a dictionary."""
        d: Dict[str, Any] = {
            "identifier": self.identifier,
            "materials": self.materials.as_dict(),
        }

        if self.creation_time is not None:
            d["creation_time"] = self.creation_time

        if self.expiry_time is not None:
            d["expiry_time"] = self.expiry_time

        if self.messages_used is not None:
            d["messages_used"] = self.messages_used

        if self.bytes_used is not None:
            d["bytes_used"] = self.bytes_used

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "PutCacheEntryInput":
        """Creates a PutCacheEntryInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
            "materials": _materials_from_dict(d["materials"]),
        }

        if "creation_time" in d:
            kwargs["creation_time"] = d["creation_time"]

        if "expiry_time" in d:
            kwargs["expiry_time"] = d["expiry_time"]

        if "messages_used" in d:
            kwargs["messages_used"] = d["messages_used"]

        if "bytes_used" in d:
            kwargs["bytes_used"] = d["bytes_used"]

        return PutCacheEntryInput(**kwargs)

    def __repr__(self) -> str:
        result = "PutCacheEntryInput("
        if self.identifier is not None:
            result += f"identifier={repr(self.identifier)}, "

        if self.materials is not None:
            result += f"materials={repr(self.materials)}, "

        if self.creation_time is not None:
            result += f"creation_time={repr(self.creation_time)}, "

        if self.expiry_time is not None:
            result += f"expiry_time={repr(self.expiry_time)}, "

        if self.messages_used is not None:
            result += f"messages_used={repr(self.messages_used)}, "

        if self.bytes_used is not None:
            result += f"bytes_used={repr(self.bytes_used)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, PutCacheEntryInput):
            return False
        attributes: list[str] = [
            "identifier",
            "materials",
            "creation_time",
            "expiry_time",
            "messages_used",
            "bytes_used",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class UpdateUsageMetadataInput:
    identifier: bytes | bytearray
    bytes_used: int

    def __init__(
        self,
        *,
        identifier: bytes | bytearray,
        bytes_used: int = 0,
    ):
        self.identifier = identifier
        if (bytes_used is not None) and (bytes_used < 0):
            raise ValueError("bytes_used must be greater than or equal to 0")

        self.bytes_used = bytes_used

    def as_dict(self) -> Dict[str, Any]:
        """Converts the UpdateUsageMetadataInput to a dictionary."""
        d: Dict[str, Any] = {
            "identifier": self.identifier,
        }

        if self.bytes_used is not None:
            d["bytes_used"] = self.bytes_used

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "UpdateUsageMetadataInput":
        """Creates a UpdateUsageMetadataInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
        }

        if "bytes_used" in d:
            kwargs["bytes_used"] = d["bytes_used"]

        return UpdateUsageMetadataInput(**kwargs)

    def __repr__(self) -> str:
        result = "UpdateUsageMetadataInput("
        if self.identifier is not None:
            result += f"identifier={repr(self.identifier)}, "

        if self.bytes_used is not None:
            result += f"bytes_used={repr(self.bytes_used)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, UpdateUsageMetadataInput):
            return False
        attributes: list[str] = [
            "identifier",
            "bytes_used",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class DBECommitmentPolicy:
    REQUIRE_ENCRYPT_REQUIRE_DECRYPT = "REQUIRE_ENCRYPT_REQUIRE_DECRYPT"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset({"REQUIRE_ENCRYPT_REQUIRE_DECRYPT"})


class ESDKCommitmentPolicy:
    FORBID_ENCRYPT_ALLOW_DECRYPT = "FORBID_ENCRYPT_ALLOW_DECRYPT"

    REQUIRE_ENCRYPT_ALLOW_DECRYPT = "REQUIRE_ENCRYPT_ALLOW_DECRYPT"

    REQUIRE_ENCRYPT_REQUIRE_DECRYPT = "REQUIRE_ENCRYPT_REQUIRE_DECRYPT"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset(
        {
            "FORBID_ENCRYPT_ALLOW_DECRYPT",
            "REQUIRE_ENCRYPT_ALLOW_DECRYPT",
            "REQUIRE_ENCRYPT_REQUIRE_DECRYPT",
        }
    )


class CommitmentPolicyESDK:
    def __init__(self, value: str):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"ESDK": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CommitmentPolicyESDK":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return CommitmentPolicyESDK(d["ESDK"])

    def __repr__(self) -> str:
        return f"CommitmentPolicyESDK(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CommitmentPolicyESDK):
            return False
        return self.value == other.value


class CommitmentPolicyDBE:
    def __init__(self, value: str):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"DBE": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CommitmentPolicyDBE":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return CommitmentPolicyDBE(d["DBE"])

    def __repr__(self) -> str:
        return f"CommitmentPolicyDBE(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CommitmentPolicyDBE):
            return False
        return self.value == other.value


class CommitmentPolicyUnknown:
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to
    receive the parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CommitmentPolicyUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return CommitmentPolicyUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"CommitmentPolicyUnknown(tag={self.tag})"


CommitmentPolicy = Union[
    CommitmentPolicyESDK, CommitmentPolicyDBE, CommitmentPolicyUnknown
]


def _commitment_policy_from_dict(d: Dict[str, Any]) -> CommitmentPolicy:
    if "ESDK" in d:
        return CommitmentPolicyESDK.from_dict(d)

    if "DBE" in d:
        return CommitmentPolicyDBE.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class DecryptMaterialsInput:
    algorithm_suite_id: AlgorithmSuiteId
    commitment_policy: CommitmentPolicy
    encrypted_data_keys: list[EncryptedDataKey]
    encryption_context: dict[str, str]
    reproduced_encryption_context: Optional[dict[str, str]]

    def __init__(
        self,
        *,
        algorithm_suite_id: AlgorithmSuiteId,
        commitment_policy: CommitmentPolicy,
        encrypted_data_keys: list[EncryptedDataKey],
        encryption_context: dict[str, str],
        reproduced_encryption_context: Optional[dict[str, str]] = None,
    ):
        self.algorithm_suite_id = algorithm_suite_id
        self.commitment_policy = commitment_policy
        self.encrypted_data_keys = encrypted_data_keys
        self.encryption_context = encryption_context
        self.reproduced_encryption_context = reproduced_encryption_context

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DecryptMaterialsInput to a dictionary."""
        d: Dict[str, Any] = {
            "algorithm_suite_id": self.algorithm_suite_id.as_dict(),
            "commitment_policy": self.commitment_policy.as_dict(),
            "encrypted_data_keys": _encrypted_data_key_list_as_dict(
                self.encrypted_data_keys
            ),
            "encryption_context": self.encryption_context,
        }

        if self.reproduced_encryption_context is not None:
            d["reproduced_encryption_context"] = self.reproduced_encryption_context

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DecryptMaterialsInput":
        """Creates a DecryptMaterialsInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "algorithm_suite_id": _algorithm_suite_id_from_dict(
                d["algorithm_suite_id"]
            ),
            "commitment_policy": _commitment_policy_from_dict(d["commitment_policy"]),
            "encrypted_data_keys": _encrypted_data_key_list_from_dict(
                d["encrypted_data_keys"]
            ),
            "encryption_context": d["encryption_context"],
        }

        if "reproduced_encryption_context" in d:
            kwargs["reproduced_encryption_context"] = d["reproduced_encryption_context"]

        return DecryptMaterialsInput(**kwargs)

    def __repr__(self) -> str:
        result = "DecryptMaterialsInput("
        if self.algorithm_suite_id is not None:
            result += f"algorithm_suite_id={repr(self.algorithm_suite_id)}, "

        if self.commitment_policy is not None:
            result += f"commitment_policy={repr(self.commitment_policy)}, "

        if self.encrypted_data_keys is not None:
            result += f"encrypted_data_keys={repr(self.encrypted_data_keys)}, "

        if self.encryption_context is not None:
            result += f"encryption_context={repr(self.encryption_context)}, "

        if self.reproduced_encryption_context is not None:
            result += f"reproduced_encryption_context={repr(self.reproduced_encryption_context)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DecryptMaterialsInput):
            return False
        attributes: list[str] = [
            "algorithm_suite_id",
            "commitment_policy",
            "encrypted_data_keys",
            "encryption_context",
            "reproduced_encryption_context",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class DecryptMaterialsOutput:
    decryption_materials: DecryptionMaterials

    def __init__(
        self,
        *,
        decryption_materials: DecryptionMaterials,
    ):
        self.decryption_materials = decryption_materials

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DecryptMaterialsOutput to a dictionary."""
        return {
            "decryption_materials": self.decryption_materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DecryptMaterialsOutput":
        """Creates a DecryptMaterialsOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "decryption_materials": DecryptionMaterials.from_dict(
                d["decryption_materials"]
            ),
        }

        return DecryptMaterialsOutput(**kwargs)

    def __repr__(self) -> str:
        result = "DecryptMaterialsOutput("
        if self.decryption_materials is not None:
            result += f"decryption_materials={repr(self.decryption_materials)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DecryptMaterialsOutput):
            return False
        attributes: list[str] = [
            "decryption_materials",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetEncryptionMaterialsInput:
    encryption_context: dict[str, str]
    commitment_policy: CommitmentPolicy
    algorithm_suite_id: Optional[AlgorithmSuiteId]
    max_plaintext_length: Optional[int]
    required_encryption_context_keys: Optional[list[str]]

    def __init__(
        self,
        *,
        encryption_context: dict[str, str],
        commitment_policy: CommitmentPolicy,
        algorithm_suite_id: Optional[AlgorithmSuiteId] = None,
        max_plaintext_length: Optional[int] = None,
        required_encryption_context_keys: Optional[list[str]] = None,
    ):
        self.encryption_context = encryption_context
        self.commitment_policy = commitment_policy
        self.algorithm_suite_id = algorithm_suite_id
        self.max_plaintext_length = max_plaintext_length
        self.required_encryption_context_keys = required_encryption_context_keys

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetEncryptionMaterialsInput to a dictionary."""
        d: Dict[str, Any] = {
            "encryption_context": self.encryption_context,
            "commitment_policy": self.commitment_policy.as_dict(),
        }

        if self.algorithm_suite_id is not None:
            d["algorithm_suite_id"] = self.algorithm_suite_id.as_dict()

        if self.max_plaintext_length is not None:
            d["max_plaintext_length"] = self.max_plaintext_length

        if self.required_encryption_context_keys is not None:
            d["required_encryption_context_keys"] = (
                self.required_encryption_context_keys
            )

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetEncryptionMaterialsInput":
        """Creates a GetEncryptionMaterialsInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "encryption_context": d["encryption_context"],
            "commitment_policy": _commitment_policy_from_dict(d["commitment_policy"]),
        }

        if "algorithm_suite_id" in d:
            kwargs["algorithm_suite_id"] = (
                _algorithm_suite_id_from_dict(d["algorithm_suite_id"]),
            )

        if "max_plaintext_length" in d:
            kwargs["max_plaintext_length"] = d["max_plaintext_length"]

        if "required_encryption_context_keys" in d:
            kwargs["required_encryption_context_keys"] = d[
                "required_encryption_context_keys"
            ]

        return GetEncryptionMaterialsInput(**kwargs)

    def __repr__(self) -> str:
        result = "GetEncryptionMaterialsInput("
        if self.encryption_context is not None:
            result += f"encryption_context={repr(self.encryption_context)}, "

        if self.commitment_policy is not None:
            result += f"commitment_policy={repr(self.commitment_policy)}, "

        if self.algorithm_suite_id is not None:
            result += f"algorithm_suite_id={repr(self.algorithm_suite_id)}, "

        if self.max_plaintext_length is not None:
            result += f"max_plaintext_length={repr(self.max_plaintext_length)}, "

        if self.required_encryption_context_keys is not None:
            result += f"required_encryption_context_keys={repr(self.required_encryption_context_keys)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetEncryptionMaterialsInput):
            return False
        attributes: list[str] = [
            "encryption_context",
            "commitment_policy",
            "algorithm_suite_id",
            "max_plaintext_length",
            "required_encryption_context_keys",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetEncryptionMaterialsOutput:
    encryption_materials: EncryptionMaterials

    def __init__(
        self,
        *,
        encryption_materials: EncryptionMaterials,
    ):
        self.encryption_materials = encryption_materials

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetEncryptionMaterialsOutput to a dictionary."""
        return {
            "encryption_materials": self.encryption_materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetEncryptionMaterialsOutput":
        """Creates a GetEncryptionMaterialsOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "encryption_materials": EncryptionMaterials.from_dict(
                d["encryption_materials"]
            ),
        }

        return GetEncryptionMaterialsOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GetEncryptionMaterialsOutput("
        if self.encryption_materials is not None:
            result += f"encryption_materials={repr(self.encryption_materials)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetEncryptionMaterialsOutput):
            return False
        attributes: list[str] = [
            "encryption_materials",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class InitializeDecryptionMaterialsInput:
    algorithm_suite_id: AlgorithmSuiteId
    encryption_context: dict[str, str]
    required_encryption_context_keys: list[str]

    def __init__(
        self,
        *,
        algorithm_suite_id: AlgorithmSuiteId,
        encryption_context: dict[str, str],
        required_encryption_context_keys: list[str],
    ):
        self.algorithm_suite_id = algorithm_suite_id
        self.encryption_context = encryption_context
        self.required_encryption_context_keys = required_encryption_context_keys

    def as_dict(self) -> Dict[str, Any]:
        """Converts the InitializeDecryptionMaterialsInput to a dictionary."""
        return {
            "algorithm_suite_id": self.algorithm_suite_id.as_dict(),
            "encryption_context": self.encryption_context,
            "required_encryption_context_keys": self.required_encryption_context_keys,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InitializeDecryptionMaterialsInput":
        """Creates a InitializeDecryptionMaterialsInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "algorithm_suite_id": _algorithm_suite_id_from_dict(
                d["algorithm_suite_id"]
            ),
            "encryption_context": d["encryption_context"],
            "required_encryption_context_keys": d["required_encryption_context_keys"],
        }

        return InitializeDecryptionMaterialsInput(**kwargs)

    def __repr__(self) -> str:
        result = "InitializeDecryptionMaterialsInput("
        if self.algorithm_suite_id is not None:
            result += f"algorithm_suite_id={repr(self.algorithm_suite_id)}, "

        if self.encryption_context is not None:
            result += f"encryption_context={repr(self.encryption_context)}, "

        if self.required_encryption_context_keys is not None:
            result += f"required_encryption_context_keys={repr(self.required_encryption_context_keys)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, InitializeDecryptionMaterialsInput):
            return False
        attributes: list[str] = [
            "algorithm_suite_id",
            "encryption_context",
            "required_encryption_context_keys",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class InitializeEncryptionMaterialsInput:
    algorithm_suite_id: AlgorithmSuiteId
    encryption_context: dict[str, str]
    required_encryption_context_keys: list[str]
    signing_key: Optional[bytes | bytearray]
    verification_key: Optional[bytes | bytearray]

    def __init__(
        self,
        *,
        algorithm_suite_id: AlgorithmSuiteId,
        encryption_context: dict[str, str],
        required_encryption_context_keys: list[str],
        signing_key: Optional[bytes | bytearray] = None,
        verification_key: Optional[bytes | bytearray] = None,
    ):
        self.algorithm_suite_id = algorithm_suite_id
        self.encryption_context = encryption_context
        self.required_encryption_context_keys = required_encryption_context_keys
        self.signing_key = signing_key
        self.verification_key = verification_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the InitializeEncryptionMaterialsInput to a dictionary."""
        d: Dict[str, Any] = {
            "algorithm_suite_id": self.algorithm_suite_id.as_dict(),
            "encryption_context": self.encryption_context,
            "required_encryption_context_keys": self.required_encryption_context_keys,
        }

        if self.signing_key is not None:
            d["signing_key"] = self.signing_key

        if self.verification_key is not None:
            d["verification_key"] = self.verification_key

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InitializeEncryptionMaterialsInput":
        """Creates a InitializeEncryptionMaterialsInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "algorithm_suite_id": _algorithm_suite_id_from_dict(
                d["algorithm_suite_id"]
            ),
            "encryption_context": d["encryption_context"],
            "required_encryption_context_keys": d["required_encryption_context_keys"],
        }

        if "signing_key" in d:
            kwargs["signing_key"] = d["signing_key"]

        if "verification_key" in d:
            kwargs["verification_key"] = d["verification_key"]

        return InitializeEncryptionMaterialsInput(**kwargs)

    def __repr__(self) -> str:
        result = "InitializeEncryptionMaterialsInput("
        if self.algorithm_suite_id is not None:
            result += f"algorithm_suite_id={repr(self.algorithm_suite_id)}, "

        if self.encryption_context is not None:
            result += f"encryption_context={repr(self.encryption_context)}, "

        if self.required_encryption_context_keys is not None:
            result += f"required_encryption_context_keys={repr(self.required_encryption_context_keys)}, "

        if self.signing_key is not None:
            result += f"signing_key={repr(self.signing_key)}, "

        if self.verification_key is not None:
            result += f"verification_key={repr(self.verification_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, InitializeEncryptionMaterialsInput):
            return False
        attributes: list[str] = [
            "algorithm_suite_id",
            "encryption_context",
            "required_encryption_context_keys",
            "signing_key",
            "verification_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class OnDecryptInput:
    materials: DecryptionMaterials
    encrypted_data_keys: list[EncryptedDataKey]

    def __init__(
        self,
        *,
        materials: DecryptionMaterials,
        encrypted_data_keys: list[EncryptedDataKey],
    ):
        self.materials = materials
        self.encrypted_data_keys = encrypted_data_keys

    def as_dict(self) -> Dict[str, Any]:
        """Converts the OnDecryptInput to a dictionary."""
        return {
            "materials": self.materials.as_dict(),
            "encrypted_data_keys": _encrypted_data_key_list_as_dict(
                self.encrypted_data_keys
            ),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "OnDecryptInput":
        """Creates a OnDecryptInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "materials": DecryptionMaterials.from_dict(d["materials"]),
            "encrypted_data_keys": _encrypted_data_key_list_from_dict(
                d["encrypted_data_keys"]
            ),
        }

        return OnDecryptInput(**kwargs)

    def __repr__(self) -> str:
        result = "OnDecryptInput("
        if self.materials is not None:
            result += f"materials={repr(self.materials)}, "

        if self.encrypted_data_keys is not None:
            result += f"encrypted_data_keys={repr(self.encrypted_data_keys)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, OnDecryptInput):
            return False
        attributes: list[str] = [
            "materials",
            "encrypted_data_keys",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class OnDecryptOutput:
    materials: DecryptionMaterials

    def __init__(
        self,
        *,
        materials: DecryptionMaterials,
    ):
        self.materials = materials

    def as_dict(self) -> Dict[str, Any]:
        """Converts the OnDecryptOutput to a dictionary."""
        return {
            "materials": self.materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "OnDecryptOutput":
        """Creates a OnDecryptOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "materials": DecryptionMaterials.from_dict(d["materials"]),
        }

        return OnDecryptOutput(**kwargs)

    def __repr__(self) -> str:
        result = "OnDecryptOutput("
        if self.materials is not None:
            result += f"materials={repr(self.materials)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, OnDecryptOutput):
            return False
        attributes: list[str] = [
            "materials",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class OnEncryptInput:
    materials: EncryptionMaterials

    def __init__(
        self,
        *,
        materials: EncryptionMaterials,
    ):
        self.materials = materials

    def as_dict(self) -> Dict[str, Any]:
        """Converts the OnEncryptInput to a dictionary."""
        return {
            "materials": self.materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "OnEncryptInput":
        """Creates a OnEncryptInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "materials": EncryptionMaterials.from_dict(d["materials"]),
        }

        return OnEncryptInput(**kwargs)

    def __repr__(self) -> str:
        result = "OnEncryptInput("
        if self.materials is not None:
            result += f"materials={repr(self.materials)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, OnEncryptInput):
            return False
        attributes: list[str] = [
            "materials",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class OnEncryptOutput:
    materials: EncryptionMaterials

    def __init__(
        self,
        *,
        materials: EncryptionMaterials,
    ):
        self.materials = materials

    def as_dict(self) -> Dict[str, Any]:
        """Converts the OnEncryptOutput to a dictionary."""
        return {
            "materials": self.materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "OnEncryptOutput":
        """Creates a OnEncryptOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "materials": EncryptionMaterials.from_dict(d["materials"]),
        }

        return OnEncryptOutput(**kwargs)

    def __repr__(self) -> str:
        result = "OnEncryptOutput("
        if self.materials is not None:
            result += f"materials={repr(self.materials)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, OnEncryptOutput):
            return False
        attributes: list[str] = [
            "materials",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class ValidateCommitmentPolicyOnDecryptInput:
    algorithm: AlgorithmSuiteId
    commitment_policy: CommitmentPolicy

    def __init__(
        self,
        *,
        algorithm: AlgorithmSuiteId,
        commitment_policy: CommitmentPolicy,
    ):
        self.algorithm = algorithm
        self.commitment_policy = commitment_policy

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ValidateCommitmentPolicyOnDecryptInput to a
        dictionary."""
        return {
            "algorithm": self.algorithm.as_dict(),
            "commitment_policy": self.commitment_policy.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ValidateCommitmentPolicyOnDecryptInput":
        """Creates a ValidateCommitmentPolicyOnDecryptInput from a
        dictionary."""
        kwargs: Dict[str, Any] = {
            "algorithm": _algorithm_suite_id_from_dict(d["algorithm"]),
            "commitment_policy": _commitment_policy_from_dict(d["commitment_policy"]),
        }

        return ValidateCommitmentPolicyOnDecryptInput(**kwargs)

    def __repr__(self) -> str:
        result = "ValidateCommitmentPolicyOnDecryptInput("
        if self.algorithm is not None:
            result += f"algorithm={repr(self.algorithm)}, "

        if self.commitment_policy is not None:
            result += f"commitment_policy={repr(self.commitment_policy)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ValidateCommitmentPolicyOnDecryptInput):
            return False
        attributes: list[str] = [
            "algorithm",
            "commitment_policy",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class ValidateCommitmentPolicyOnEncryptInput:
    algorithm: AlgorithmSuiteId
    commitment_policy: CommitmentPolicy

    def __init__(
        self,
        *,
        algorithm: AlgorithmSuiteId,
        commitment_policy: CommitmentPolicy,
    ):
        self.algorithm = algorithm
        self.commitment_policy = commitment_policy

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ValidateCommitmentPolicyOnEncryptInput to a
        dictionary."""
        return {
            "algorithm": self.algorithm.as_dict(),
            "commitment_policy": self.commitment_policy.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ValidateCommitmentPolicyOnEncryptInput":
        """Creates a ValidateCommitmentPolicyOnEncryptInput from a
        dictionary."""
        kwargs: Dict[str, Any] = {
            "algorithm": _algorithm_suite_id_from_dict(d["algorithm"]),
            "commitment_policy": _commitment_policy_from_dict(d["commitment_policy"]),
        }

        return ValidateCommitmentPolicyOnEncryptInput(**kwargs)

    def __repr__(self) -> str:
        result = "ValidateCommitmentPolicyOnEncryptInput("
        if self.algorithm is not None:
            result += f"algorithm={repr(self.algorithm)}, "

        if self.commitment_policy is not None:
            result += f"commitment_policy={repr(self.commitment_policy)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ValidateCommitmentPolicyOnEncryptInput):
            return False
        attributes: list[str] = [
            "algorithm",
            "commitment_policy",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class ValidDecryptionMaterialsTransitionInput:
    start: DecryptionMaterials
    stop: DecryptionMaterials

    def __init__(
        self,
        *,
        start: DecryptionMaterials,
        stop: DecryptionMaterials,
    ):
        self.start = start
        self.stop = stop

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ValidDecryptionMaterialsTransitionInput to a
        dictionary."""
        return {
            "start": self.start.as_dict(),
            "stop": self.stop.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ValidDecryptionMaterialsTransitionInput":
        """Creates a ValidDecryptionMaterialsTransitionInput from a
        dictionary."""
        kwargs: Dict[str, Any] = {
            "start": DecryptionMaterials.from_dict(d["start"]),
            "stop": DecryptionMaterials.from_dict(d["stop"]),
        }

        return ValidDecryptionMaterialsTransitionInput(**kwargs)

    def __repr__(self) -> str:
        result = "ValidDecryptionMaterialsTransitionInput("
        if self.start is not None:
            result += f"start={repr(self.start)}, "

        if self.stop is not None:
            result += f"stop={repr(self.stop)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ValidDecryptionMaterialsTransitionInput):
            return False
        attributes: list[str] = [
            "start",
            "stop",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class ValidEncryptionMaterialsTransitionInput:
    start: EncryptionMaterials
    stop: EncryptionMaterials

    def __init__(
        self,
        *,
        start: EncryptionMaterials,
        stop: EncryptionMaterials,
    ):
        self.start = start
        self.stop = stop

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ValidEncryptionMaterialsTransitionInput to a
        dictionary."""
        return {
            "start": self.start.as_dict(),
            "stop": self.stop.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ValidEncryptionMaterialsTransitionInput":
        """Creates a ValidEncryptionMaterialsTransitionInput from a
        dictionary."""
        kwargs: Dict[str, Any] = {
            "start": EncryptionMaterials.from_dict(d["start"]),
            "stop": EncryptionMaterials.from_dict(d["stop"]),
        }

        return ValidEncryptionMaterialsTransitionInput(**kwargs)

    def __repr__(self) -> str:
        result = "ValidEncryptionMaterialsTransitionInput("
        if self.start is not None:
            result += f"start={repr(self.start)}, "

        if self.stop is not None:
            result += f"stop={repr(self.stop)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ValidEncryptionMaterialsTransitionInput):
            return False
        attributes: list[str] = [
            "start",
            "stop",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class StaticConfigurationsAWS_KMS_ECDH:
    """Allowed configurations when using KmsEcdhStaticConfigurations."""

    def __init__(self, value: KmsEcdhStaticConfigurations):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"AWS_KMS_ECDH": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "StaticConfigurationsAWS_KMS_ECDH":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return StaticConfigurationsAWS_KMS_ECDH(
            _kms_ecdh_static_configurations_from_dict(d["AWS_KMS_ECDH"])
        )

    def __repr__(self) -> str:
        return f"StaticConfigurationsAWS_KMS_ECDH(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, StaticConfigurationsAWS_KMS_ECDH):
            return False
        return self.value == other.value


class StaticConfigurationsRAW_ECDH:
    """List of configurations when using RawEcdhStaticConfigurations."""

    def __init__(self, value: RawEcdhStaticConfigurations):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"RAW_ECDH": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "StaticConfigurationsRAW_ECDH":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return StaticConfigurationsRAW_ECDH(
            _raw_ecdh_static_configurations_from_dict(d["RAW_ECDH"])
        )

    def __repr__(self) -> str:
        return f"StaticConfigurationsRAW_ECDH(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, StaticConfigurationsRAW_ECDH):
            return False
        return self.value == other.value


class StaticConfigurationsUnknown:
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to
    receive the parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "StaticConfigurationsUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return StaticConfigurationsUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"StaticConfigurationsUnknown(tag={self.tag})"


# Supported configurations for the StaticConfiguration Key Agreement Scheme.
StaticConfigurations = Union[
    StaticConfigurationsAWS_KMS_ECDH,
    StaticConfigurationsRAW_ECDH,
    StaticConfigurationsUnknown,
]


def _static_configurations_from_dict(d: Dict[str, Any]) -> StaticConfigurations:
    if "AWS_KMS_ECDH" in d:
        return StaticConfigurationsAWS_KMS_ECDH.from_dict(d)

    if "RAW_ECDH" in d:
        return StaticConfigurationsRAW_ECDH.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class KeyAgreementSchemeStaticConfiguration:
    """Supported configurations for the StaticConfiguration Key Agreement
    Scheme."""

    def __init__(self, value: StaticConfigurations):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"StaticConfiguration": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyAgreementSchemeStaticConfiguration":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KeyAgreementSchemeStaticConfiguration(
            _static_configurations_from_dict(d["StaticConfiguration"])
        )

    def __repr__(self) -> str:
        return f"KeyAgreementSchemeStaticConfiguration(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyAgreementSchemeStaticConfiguration):
            return False
        return self.value == other.value


class KeyAgreementSchemeUnknown:
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to
    receive the parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyAgreementSchemeUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return KeyAgreementSchemeUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"KeyAgreementSchemeUnknown(tag={self.tag})"


# Supported ECDH Key Agreement Schemes.
KeyAgreementScheme = Union[
    KeyAgreementSchemeStaticConfiguration, KeyAgreementSchemeUnknown
]


def _key_agreement_scheme_from_dict(d: Dict[str, Any]) -> KeyAgreementScheme:
    if "StaticConfiguration" in d:
        return KeyAgreementSchemeStaticConfiguration.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


def _encrypted_data_key_list_as_dict(given: list[EncryptedDataKey]) -> List[Any]:
    return [v.as_dict() for v in given]


def _encrypted_data_key_list_from_dict(given: List[Any]) -> list[EncryptedDataKey]:
    return [EncryptedDataKey.from_dict(v) for v in given]


class Unit:
    pass
