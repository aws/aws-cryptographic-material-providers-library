# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.client
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references
import botocore.client
from typing import Any, Dict, List, Optional, Union

from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models import (
    AES_GCM,
)

from ..aws_cryptography_keystore.models import BeaconKeyMaterials, BranchKeyMaterials


class AesWrappingAlg:
    ALG_AES128_GCM_IV12_TAG16 = "ALG_AES128_GCM_IV12_TAG16"

    ALG_AES192_GCM_IV12_TAG16 = "ALG_AES192_GCM_IV12_TAG16"

    ALG_AES256_GCM_IV12_TAG16 = "ALG_AES256_GCM_IV12_TAG16"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset({"ALG_AES128_GCM_IV12_TAG16", "ALG_AES192_GCM_IV12_TAG16", "ALG_AES256_GCM_IV12_TAG16"})

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
    values = frozenset({"0x0014", "0x0046", "0x0078", "0x0114", "0x0146", "0x0178", "0x0214", "0x0346", "0x0378", "0x0478", "0x0578"})

class AlgorithmSuiteIdESDK():
    def __init__(self, value: str):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"ESDK": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AlgorithmSuiteIdESDK":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return AlgorithmSuiteIdESDK(d["ESDK"])

    def __repr__(self) -> str:
        return f"AlgorithmSuiteIdESDK(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AlgorithmSuiteIdESDK):
            return False
        return self.value == other.value

class AlgorithmSuiteIdDBE():
    def __init__(self, value: str):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"DBE": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AlgorithmSuiteIdDBE":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return AlgorithmSuiteIdDBE(d["DBE"])

    def __repr__(self) -> str:
        return f"AlgorithmSuiteIdDBE(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AlgorithmSuiteIdDBE):
            return False
        return self.value == other.value

class AlgorithmSuiteId():
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to receive the
    parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AlgorithmSuiteId":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return AlgorithmSuiteId(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"AlgorithmSuiteId(tag={self.tag})"

AlgorithmSuiteId = Union[AlgorithmSuiteIdESDK, AlgorithmSuiteIdDBE, AlgorithmSuiteId]
def _algorithm_suite_id_from_dict(d: Dict[str, Any]) -> AlgorithmSuiteId:
    if "ESDK" in d:
        return AlgorithmSuiteIdESDK.from_dict(d)

    if "DBE" in d:
        return AlgorithmSuiteIdDBE.from_dict(d)

    raise TypeError(f'Unions may have exactly 1 value, but found {len(d)}')

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
        """Converts the HKDF to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "hmac": self.hmac,
        }

        if self.salt_length is not None:
            d["saltLength"] = self.salt_length

        if self.input_key_length is not None:
            d["inputKeyLength"] = self.input_key_length

        if self.output_key_length is not None:
            d["outputKeyLength"] = self.output_key_length

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "HKDF":
        """Creates a HKDF from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "hmac": d["hmac"],
        }

        if "saltLength" in d:
            kwargs["salt_length"] = d["saltLength"]

        if "inputKeyLength" in d:
            kwargs["input_key_length"] = d["inputKeyLength"]

        if "outputKeyLength" in d:
            kwargs["output_key_length"] = d["outputKeyLength"]

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
        attributes: list[str] = ['hmac','salt_length','input_key_length','output_key_length',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class IDENTITY:
    def as_dict(self) -> Dict[str, Any]:
        """Converts the IDENTITY to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "IDENTITY":
        """Creates a IDENTITY from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        return IDENTITY()

    def __repr__(self) -> str:
        result = "IDENTITY("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, IDENTITY)

class None_:
    def as_dict(self) -> Dict[str, Any]:
        """Converts the None_ to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "None_":
        """Creates a None_ from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        return None_()

    def __repr__(self) -> str:
        result = "None_("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, None_)

class DerivationAlgorithmHKDF():
    def __init__(self, value: HKDF):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"HKDF": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DerivationAlgorithmHKDF":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return DerivationAlgorithmHKDF(HKDF.from_dict(d["HKDF"]))

    def __repr__(self) -> str:
        return f"DerivationAlgorithmHKDF(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DerivationAlgorithmHKDF):
            return False
        return self.value == other.value

class DerivationAlgorithmIDENTITY():
    def __init__(self, value: IDENTITY):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"IDENTITY": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DerivationAlgorithmIDENTITY":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return DerivationAlgorithmIDENTITY(IDENTITY.from_dict(d["IDENTITY"]))

    def __repr__(self) -> str:
        return f"DerivationAlgorithmIDENTITY(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DerivationAlgorithmIDENTITY):
            return False
        return self.value == other.value

class DerivationAlgorithmNone():
    def __init__(self, value: None_):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"None": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DerivationAlgorithmNone":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return DerivationAlgorithmNone(None_.from_dict(d["None"]))

    def __repr__(self) -> str:
        return f"DerivationAlgorithmNone(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DerivationAlgorithmNone):
            return False
        return self.value == other.value

class DerivationAlgorithm():
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to receive the
    parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DerivationAlgorithm":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return DerivationAlgorithm(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"DerivationAlgorithm(tag={self.tag})"

DerivationAlgorithm = Union[DerivationAlgorithmHKDF, DerivationAlgorithmIDENTITY, DerivationAlgorithmNone, DerivationAlgorithm]
def _derivation_algorithm_from_dict(d: Dict[str, Any]) -> DerivationAlgorithm:
    if "HKDF" in d:
        return DerivationAlgorithmHKDF.from_dict(d)

    if "IDENTITY" in d:
        return DerivationAlgorithmIDENTITY.from_dict(d)

    if "None" in d:
        return DerivationAlgorithmNone.from_dict(d)

    raise TypeError(f'Unions may have exactly 1 value, but found {len(d)}')

class DIRECT_KEY_WRAPPING:
    def as_dict(self) -> Dict[str, Any]:
        """Converts the DIRECT_KEY_WRAPPING to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DIRECT_KEY_WRAPPING":
        """Creates a DIRECT_KEY_WRAPPING from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        return DIRECT_KEY_WRAPPING()

    def __repr__(self) -> str:
        result = "DIRECT_KEY_WRAPPING("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, DIRECT_KEY_WRAPPING)

class EncryptAES_GCM():
    def __init__(self, value: AES_GCM):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"AES_GCM": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EncryptAES_GCM":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return EncryptAES_GCM(AES_GCM.from_dict(d["AES_GCM"]))

    def __repr__(self) -> str:
        return f"EncryptAES_GCM(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EncryptAES_GCM):
            return False
        return self.value == other.value

class Encrypt():
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to receive the
    parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Encrypt":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return Encrypt(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"Encrypt(tag={self.tag})"

Encrypt = Union[EncryptAES_GCM, Encrypt]
def _encrypt_from_dict(d: Dict[str, Any]) -> Encrypt:
    if "AES_GCM" in d:
        return EncryptAES_GCM.from_dict(d)

    raise TypeError(f'Unions may have exactly 1 value, but found {len(d)}')

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
        """Converts the IntermediateKeyWrapping to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyEncryptionKeyKdf": self.key_encryption_key_kdf.as_dict(),
            "macKeyKdf": self.mac_key_kdf.as_dict(),
            "pdkEncryptAlgorithm": self.pdk_encrypt_algorithm.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "IntermediateKeyWrapping":
        """Creates a IntermediateKeyWrapping from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_encryption_key_kdf": _derivation_algorithm_from_dict(d["keyEncryptionKeyKdf"]),
            "mac_key_kdf": _derivation_algorithm_from_dict(d["macKeyKdf"]),
            "pdk_encrypt_algorithm": _encrypt_from_dict(d["pdkEncryptAlgorithm"]),
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
        attributes: list[str] = ['key_encryption_key_kdf','mac_key_kdf','pdk_encrypt_algorithm',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class EdkWrappingAlgorithmDIRECT_KEY_WRAPPING():
    def __init__(self, value: DIRECT_KEY_WRAPPING):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"DIRECT_KEY_WRAPPING": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EdkWrappingAlgorithmDIRECT_KEY_WRAPPING":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return EdkWrappingAlgorithmDIRECT_KEY_WRAPPING(DIRECT_KEY_WRAPPING.from_dict(d["DIRECT_KEY_WRAPPING"]))

    def __repr__(self) -> str:
        return f"EdkWrappingAlgorithmDIRECT_KEY_WRAPPING(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EdkWrappingAlgorithmDIRECT_KEY_WRAPPING):
            return False
        return self.value == other.value

class EdkWrappingAlgorithmIntermediateKeyWrapping():
    def __init__(self, value: IntermediateKeyWrapping):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"IntermediateKeyWrapping": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EdkWrappingAlgorithmIntermediateKeyWrapping":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return EdkWrappingAlgorithmIntermediateKeyWrapping(IntermediateKeyWrapping.from_dict(d["IntermediateKeyWrapping"]))

    def __repr__(self) -> str:
        return f"EdkWrappingAlgorithmIntermediateKeyWrapping(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EdkWrappingAlgorithmIntermediateKeyWrapping):
            return False
        return self.value == other.value

class EdkWrappingAlgorithm():
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to receive the
    parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EdkWrappingAlgorithm":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return EdkWrappingAlgorithm(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"EdkWrappingAlgorithm(tag={self.tag})"

EdkWrappingAlgorithm = Union[EdkWrappingAlgorithmDIRECT_KEY_WRAPPING, EdkWrappingAlgorithmIntermediateKeyWrapping, EdkWrappingAlgorithm]
def _edk_wrapping_algorithm_from_dict(d: Dict[str, Any]) -> EdkWrappingAlgorithm:
    if "DIRECT_KEY_WRAPPING" in d:
        return EdkWrappingAlgorithmDIRECT_KEY_WRAPPING.from_dict(d)

    if "IntermediateKeyWrapping" in d:
        return EdkWrappingAlgorithmIntermediateKeyWrapping.from_dict(d)

    raise TypeError(f'Unions may have exactly 1 value, but found {len(d)}')

class ECDSA:
    curve: str
    def __init__(
        self,
        *,
        curve: str,
    ):
        self.curve = curve

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ECDSA to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "curve": self.curve,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ECDSA":
        """Creates a ECDSA from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
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
        attributes: list[str] = ['curve',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class SignatureAlgorithmECDSA():
    def __init__(self, value: ECDSA):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"ECDSA": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SignatureAlgorithmECDSA":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return SignatureAlgorithmECDSA(ECDSA.from_dict(d["ECDSA"]))

    def __repr__(self) -> str:
        return f"SignatureAlgorithmECDSA(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SignatureAlgorithmECDSA):
            return False
        return self.value == other.value

class SignatureAlgorithmNone():
    def __init__(self, value: None_):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"None": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SignatureAlgorithmNone":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return SignatureAlgorithmNone(None_.from_dict(d["None"]))

    def __repr__(self) -> str:
        return f"SignatureAlgorithmNone(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SignatureAlgorithmNone):
            return False
        return self.value == other.value

class SignatureAlgorithm():
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to receive the
    parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SignatureAlgorithm":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return SignatureAlgorithm(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"SignatureAlgorithm(tag={self.tag})"

SignatureAlgorithm = Union[SignatureAlgorithmECDSA, SignatureAlgorithmNone, SignatureAlgorithm]
def _signature_algorithm_from_dict(d: Dict[str, Any]) -> SignatureAlgorithm:
    if "ECDSA" in d:
        return SignatureAlgorithmECDSA.from_dict(d)

    if "None" in d:
        return SignatureAlgorithmNone.from_dict(d)

    raise TypeError(f'Unions may have exactly 1 value, but found {len(d)}')

class SymmetricSignatureAlgorithmHMAC():
    def __init__(self, value: str):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"HMAC": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SymmetricSignatureAlgorithmHMAC":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return SymmetricSignatureAlgorithmHMAC(d["HMAC"])

    def __repr__(self) -> str:
        return f"SymmetricSignatureAlgorithmHMAC(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SymmetricSignatureAlgorithmHMAC):
            return False
        return self.value == other.value

class SymmetricSignatureAlgorithmNone():
    def __init__(self, value: None_):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"None": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SymmetricSignatureAlgorithmNone":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return SymmetricSignatureAlgorithmNone(None_.from_dict(d["None"]))

    def __repr__(self) -> str:
        return f"SymmetricSignatureAlgorithmNone(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SymmetricSignatureAlgorithmNone):
            return False
        return self.value == other.value

class SymmetricSignatureAlgorithm():
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to receive the
    parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SymmetricSignatureAlgorithm":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return SymmetricSignatureAlgorithm(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"SymmetricSignatureAlgorithm(tag={self.tag})"

SymmetricSignatureAlgorithm = Union[SymmetricSignatureAlgorithmHMAC, SymmetricSignatureAlgorithmNone, SymmetricSignatureAlgorithm]
def _symmetric_signature_algorithm_from_dict(d: Dict[str, Any]) -> SymmetricSignatureAlgorithm:
    if "HMAC" in d:
        return SymmetricSignatureAlgorithmHMAC.from_dict(d)

    if "None" in d:
        return SymmetricSignatureAlgorithmNone.from_dict(d)

    raise TypeError(f'Unions may have exactly 1 value, but found {len(d)}')

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
        """Converts the AlgorithmSuiteInfo to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "id": self.id.as_dict(),
            "binaryId": self.binary_id,
            "messageVersion": self.message_version,
            "encrypt": self.encrypt.as_dict(),
            "kdf": self.kdf.as_dict(),
            "commitment": self.commitment.as_dict(),
            "signature": self.signature.as_dict(),
            "symmetricSignature": self.symmetric_signature.as_dict(),
            "edkWrapping": self.edk_wrapping.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AlgorithmSuiteInfo":
        """Creates a AlgorithmSuiteInfo from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "id": _algorithm_suite_id_from_dict(d["id"]),
            "binary_id": d["binaryId"],
            "message_version": d["messageVersion"],
            "encrypt": _encrypt_from_dict(d["encrypt"]),
            "kdf": _derivation_algorithm_from_dict(d["kdf"]),
            "commitment": _derivation_algorithm_from_dict(d["commitment"]),
            "signature": _signature_algorithm_from_dict(d["signature"]),
            "symmetric_signature": _symmetric_signature_algorithm_from_dict(d["symmetricSignature"]),
            "edk_wrapping": _edk_wrapping_algorithm_from_dict(d["edkWrapping"]),
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
        attributes: list[str] = ['id','binary_id','message_version','encrypt','kdf','commitment','signature','symmetric_signature','edk_wrapping',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class GetBranchKeyIdInput:
    encryption_context: dict[str, str]
    def __init__(
        self,
        *,
        encryption_context: dict[str, str],
    ):
        """Inputs for determining the Branch Key which should be used to wrap or unwrap the
        data key for this encryption or decryption

        :param encryption_context: The Encryption Context used with this encryption or
        decryption.
        """
        self.encryption_context = encryption_context

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetBranchKeyIdInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "encryptionContext": self.encryption_context,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetBranchKeyIdInput":
        """Creates a GetBranchKeyIdInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "encryption_context": d["encryptionContext"],
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
        attributes: list[str] = ['encryption_context',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class GetBranchKeyIdOutput:
    branch_key_id: str
    def __init__(
        self,
        *,
        branch_key_id: str,
    ):
        """Outputs for the Branch Key responsible for wrapping or unwrapping the data key
        in this encryption or decryption.

        :param branch_key_id: The identifier of the Branch Key that should be
        responsible for wrapping or unwrapping the data key in this encryption or
        decryption.
        """
        self.branch_key_id = branch_key_id

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetBranchKeyIdOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "branchKeyId": self.branch_key_id,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetBranchKeyIdOutput":
        """Creates a GetBranchKeyIdOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "branch_key_id": d["branchKeyId"],
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
        attributes: list[str] = ['branch_key_id',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the GetClientInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "region": self.region,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetClientInput":
        """Creates a GetClientInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
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
        attributes: list[str] = ['region',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class DiscoveryFilter:
    account_ids: list[str]
    partition: str
    def __init__(
        self,
        *,
        account_ids: list[str],
        partition: str,
    ):
        """A filter which defines what AWS partition and AWS accounts a KMS Key may be in
        for a Keyring to be allowed to attempt to decrypt it.

        :param account_ids: A list of allowed AWS account IDs.
        :param partition: The AWS partition which is allowed.
        """
        self.account_ids = account_ids
        self.partition = partition

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DiscoveryFilter to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "accountIds": self.account_ids,
            "partition": self.partition,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DiscoveryFilter":
        """Creates a DiscoveryFilter from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "account_ids": d["accountIds"],
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
        attributes: list[str] = ['account_ids','partition',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class CreateAwsKmsDiscoveryKeyringInput:
    kms_client: 'botocore.client.BaseClient'
    discovery_filter: Optional[DiscoveryFilter]
    grant_tokens: Optional[list[str]]
    def __init__(
        self,
        *,
        kms_client: 'botocore.client.BaseClient',
        discovery_filter: Optional[DiscoveryFilter] = None,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating a AWS KMS Discovery Keyring.

        :param kms_client: The KMS Client this Keyring will use to call KMS.
        :param discovery_filter: A filter which restricts which KMS Keys this Keyring
        may attempt to decrypt with by AWS partition and account.
        :param grant_tokens: A list of grant tokens to be used when calling KMS.
        """
        self.kms_client = kms_client
        self.discovery_filter = discovery_filter
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsDiscoveryKeyringInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "kmsClient": self.kms_client.as_dict(),
        }

        if self.discovery_filter is not None:
            d["discoveryFilter"] = self.discovery_filter.as_dict()

        if self.grant_tokens is not None:
            d["grantTokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsDiscoveryKeyringInput":
        """Creates a CreateAwsKmsDiscoveryKeyringInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        from botocore.client import BaseClient
        kwargs: Dict[str, Any] = {
            "kms_client": BaseClient.from_dict(d["kmsClient"]),
        }

        if "discoveryFilter" in d:
            kwargs["discovery_filter"] = DiscoveryFilter.from_dict(d["discoveryFilter"])

        if "grantTokens" in d:
            kwargs["grant_tokens"] = d["grantTokens"]

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
        attributes: list[str] = ['kms_client','discovery_filter','grant_tokens',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class CreateAwsKmsDiscoveryMultiKeyringInput:
    regions: list[str]
    discovery_filter: Optional[DiscoveryFilter]
    client_supplier: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier']
    grant_tokens: Optional[list[str]]
    def __init__(
        self,
        *,
        regions: list[str],
        discovery_filter: Optional[DiscoveryFilter] = None,
        client_supplier: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier'] = None,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating an AWS KMS Discovery Multi-Keyring.

        :param regions: The list of regions this Keyring will creates KMS clients for.
        :param discovery_filter: A filter which restricts which KMS Keys this Keyring
        may attempt to decrypt with by AWS partition and account.
        :param client_supplier: The Client Supplier which will be used to get KMS
        Clients for use with this Keyring. If not specified on input, a Default Client
        Supplier is created which creates a KMS Client for each region in the 'regions'
        input.
        :param grant_tokens: A list of grant tokens to be used when calling KMS.
        """
        self.regions = regions
        self.discovery_filter = discovery_filter
        self.client_supplier = client_supplier
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsDiscoveryMultiKeyringInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "regions": self.regions,
        }

        if self.discovery_filter is not None:
            d["discoveryFilter"] = self.discovery_filter.as_dict()

        if self.client_supplier is not None:
            d["clientSupplier"] = self.client_supplier.as_dict()

        if self.grant_tokens is not None:
            d["grantTokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsDiscoveryMultiKeyringInput":
        """Creates a CreateAwsKmsDiscoveryMultiKeyringInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        from aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references import ClientSupplier
        kwargs: Dict[str, Any] = {
            "regions": d["regions"],
        }

        if "discoveryFilter" in d:
            kwargs["discovery_filter"] = DiscoveryFilter.from_dict(d["discoveryFilter"])

        if "clientSupplier" in d:
            kwargs["client_supplier"] = ClientSupplier.from_dict(d["clientSupplier"])

        if "grantTokens" in d:
            kwargs["grant_tokens"] = d["grantTokens"]

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
        attributes: list[str] = ['regions','discovery_filter','client_supplier','grant_tokens',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the DefaultCache to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {}

        if self.entry_capacity is not None:
            d["entryCapacity"] = self.entry_capacity

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DefaultCache":
        """Creates a DefaultCache from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {}

        if "entryCapacity" in d:
            kwargs["entry_capacity"] = d["entryCapacity"]

        return DefaultCache(**kwargs)

    def __repr__(self) -> str:
        result = "DefaultCache("
        if self.entry_capacity is not None:
            result += f"entry_capacity={repr(self.entry_capacity)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DefaultCache):
            return False
        attributes: list[str] = ['entry_capacity',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class MultiThreadedCache:
    entry_capacity: int
    entry_pruning_tail_size: int
    def __init__(
        self,
        *,
        entry_capacity: int = 0,
        entry_pruning_tail_size: int = 0,
    ):
        """A cache that is safe for use in a multi threaded environment, but no extra
        functionality.

        :param entry_capacity: Maximum number of entries cached.
        :param entry_pruning_tail_size: Number of entries to prune at a time.
        """
        if (entry_capacity is not None) and (entry_capacity < 1):
            raise ValueError("entry_capacity must be greater than or equal to 1")

        self.entry_capacity = entry_capacity
        if (entry_pruning_tail_size is not None) and (entry_pruning_tail_size < 1):
            raise ValueError("entry_pruning_tail_size must be greater than or equal to 1")

        self.entry_pruning_tail_size = entry_pruning_tail_size

    def as_dict(self) -> Dict[str, Any]:
        """Converts the MultiThreadedCache to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {}

        if self.entry_capacity is not None:
            d["entryCapacity"] = self.entry_capacity

        if self.entry_pruning_tail_size is not None:
            d["entryPruningTailSize"] = self.entry_pruning_tail_size

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MultiThreadedCache":
        """Creates a MultiThreadedCache from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {}

        if "entryCapacity" in d:
            kwargs["entry_capacity"] = d["entryCapacity"]

        if "entryPruningTailSize" in d:
            kwargs["entry_pruning_tail_size"] = d["entryPruningTailSize"]

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
        attributes: list[str] = ['entry_capacity','entry_pruning_tail_size',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class NoCache:
    """Nothing should ever be cached.
    """
    def as_dict(self) -> Dict[str, Any]:
        """Converts the NoCache to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "NoCache":
        """Creates a NoCache from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
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
        :param entry_pruning_tail_size: Number of entries to prune at a time.
        """
        if (entry_capacity is not None) and (entry_capacity < 1):
            raise ValueError("entry_capacity must be greater than or equal to 1")

        self.entry_capacity = entry_capacity
        if (entry_pruning_tail_size is not None) and (entry_pruning_tail_size < 1):
            raise ValueError("entry_pruning_tail_size must be greater than or equal to 1")

        self.entry_pruning_tail_size = entry_pruning_tail_size

    def as_dict(self) -> Dict[str, Any]:
        """Converts the SingleThreadedCache to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {}

        if self.entry_capacity is not None:
            d["entryCapacity"] = self.entry_capacity

        if self.entry_pruning_tail_size is not None:
            d["entryPruningTailSize"] = self.entry_pruning_tail_size

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SingleThreadedCache":
        """Creates a SingleThreadedCache from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {}

        if "entryCapacity" in d:
            kwargs["entry_capacity"] = d["entryCapacity"]

        if "entryPruningTailSize" in d:
            kwargs["entry_pruning_tail_size"] = d["entryPruningTailSize"]

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
        attributes: list[str] = ['entry_capacity','entry_pruning_tail_size',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class StormTrackingCache:
    entry_capacity: int
    entry_pruning_tail_size: int
    grace_period: int
    grace_interval: int
    fan_out: int
    in_flight_ttl: int
    sleep_milli: int
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
    ):
        """A cache that is safe for use in a multi threaded environment,
        and tries to
        prevent redundant or overly parallel backend calls.

        :param entry_capacity: Maximum number of entries cached.
        :param entry_pruning_tail_size: Number of entries to prune at a time.
        :param grace_period: How many seconds before expiration should an attempt be
        made to refresh the materials.
          If zero, use a simple cache with no storm
        tracking.
        :param grace_interval: How many seconds between attempts to refresh the
        materials.
        :param fan_out: How many simultaneous attempts to refresh the materials.
        :param in_flight_ttl: How many seconds until an attempt to refresh the materials
        should be forgotten.
        :param sleep_milli: How many milliseconds should a thread sleep if fanOut is
        exceeded.
        """
        if (entry_capacity is not None) and (entry_capacity < 1):
            raise ValueError("entry_capacity must be greater than or equal to 1")

        self.entry_capacity = entry_capacity
        if (entry_pruning_tail_size is not None) and (entry_pruning_tail_size < 1):
            raise ValueError("entry_pruning_tail_size must be greater than or equal to 1")

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

    def as_dict(self) -> Dict[str, Any]:
        """Converts the StormTrackingCache to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {}

        if self.entry_capacity is not None:
            d["entryCapacity"] = self.entry_capacity

        if self.entry_pruning_tail_size is not None:
            d["entryPruningTailSize"] = self.entry_pruning_tail_size

        if self.grace_period is not None:
            d["gracePeriod"] = self.grace_period

        if self.grace_interval is not None:
            d["graceInterval"] = self.grace_interval

        if self.fan_out is not None:
            d["fanOut"] = self.fan_out

        if self.in_flight_ttl is not None:
            d["inFlightTTL"] = self.in_flight_ttl

        if self.sleep_milli is not None:
            d["sleepMilli"] = self.sleep_milli

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "StormTrackingCache":
        """Creates a StormTrackingCache from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {}

        if "entryCapacity" in d:
            kwargs["entry_capacity"] = d["entryCapacity"]

        if "entryPruningTailSize" in d:
            kwargs["entry_pruning_tail_size"] = d["entryPruningTailSize"]

        if "gracePeriod" in d:
            kwargs["grace_period"] = d["gracePeriod"]

        if "graceInterval" in d:
            kwargs["grace_interval"] = d["graceInterval"]

        if "fanOut" in d:
            kwargs["fan_out"] = d["fanOut"]

        if "inFlightTTL" in d:
            kwargs["in_flight_ttl"] = d["inFlightTTL"]

        if "sleepMilli" in d:
            kwargs["sleep_milli"] = d["sleepMilli"]

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
            result += f"sleep_milli={repr(self.sleep_milli)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, StormTrackingCache):
            return False
        attributes: list[str] = ['entry_capacity','entry_pruning_tail_size','grace_period','grace_interval','fan_out','in_flight_ttl','sleep_milli',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class CacheTypeDefault():
    """The best choice for most situations. Probably a StormTrackingCache.
    """
    def __init__(self, value: DefaultCache):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"Default": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CacheTypeDefault":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return CacheTypeDefault(DefaultCache.from_dict(d["Default"]))

    def __repr__(self) -> str:
        return f"CacheTypeDefault(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CacheTypeDefault):
            return False
        return self.value == other.value

class CacheTypeNo():
    """Nothing should ever be cached.
    """
    def __init__(self, value: NoCache):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"No": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CacheTypeNo":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return CacheTypeNo(NoCache.from_dict(d["No"]))

    def __repr__(self) -> str:
        return f"CacheTypeNo(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CacheTypeNo):
            return False
        return self.value == other.value

class CacheTypeSingleThreaded():
    """A cache that is NOT safe for use in a multi threaded environment.
    """
    def __init__(self, value: SingleThreadedCache):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"SingleThreaded": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CacheTypeSingleThreaded":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return CacheTypeSingleThreaded(SingleThreadedCache.from_dict(d["SingleThreaded"]))

    def __repr__(self) -> str:
        return f"CacheTypeSingleThreaded(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CacheTypeSingleThreaded):
            return False
        return self.value == other.value

class CacheTypeMultiThreaded():
    """A cache that is safe for use in a multi threaded environment, but no extra
    functionality.
    """
    def __init__(self, value: MultiThreadedCache):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"MultiThreaded": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CacheTypeMultiThreaded":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return CacheTypeMultiThreaded(MultiThreadedCache.from_dict(d["MultiThreaded"]))

    def __repr__(self) -> str:
        return f"CacheTypeMultiThreaded(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CacheTypeMultiThreaded):
            return False
        return self.value == other.value

class CacheTypeStormTracking():
    """A cache that is safe for use in a multi threaded environment,
    and tries to
    prevent redundant or overly parallel backend calls.
    """
    def __init__(self, value: StormTrackingCache):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"StormTracking": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CacheTypeStormTracking":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return CacheTypeStormTracking(StormTrackingCache.from_dict(d["StormTracking"]))

    def __repr__(self) -> str:
        return f"CacheTypeStormTracking(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CacheTypeStormTracking):
            return False
        return self.value == other.value

class CacheType():
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to receive the
    parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CacheType":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return CacheType(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"CacheType(tag={self.tag})"

CacheType = Union[CacheTypeDefault, CacheTypeNo, CacheTypeSingleThreaded, CacheTypeMultiThreaded, CacheTypeStormTracking, CacheType]
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

    raise TypeError(f'Unions may have exactly 1 value, but found {len(d)}')

class CreateAwsKmsHierarchicalKeyringInput:
    branch_key_id: Optional[str]
    branch_key_id_supplier: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.BranchKeyIdSupplier']
    key_store: 'aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.client.KeyStore'
    ttl_seconds: int
    cache: Optional[CacheType]
    def __init__(
        self,
        *,
        key_store: 'aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.client.KeyStore',
        branch_key_id: Optional[str] = None,
        branch_key_id_supplier: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.BranchKeyIdSupplier'] = None,
        ttl_seconds: int = 0,
        cache: Optional[CacheType] = None,
    ):
        """Inputs for creating a Hierarchical Keyring.

        :param key_store: The Key Store which contains the Branch Key(s) responsible for
        wrapping and unwrapping data keys.
        :param branch_key_id: The identifier for the single Branch Key responsible for
        wrapping and unwrapping the data key. Either a Branch Key ID or Branch Key
        Supplier must be specified.
        :param branch_key_id_supplier: A Branch Key Supplier which determines what
        Branch Key to use to wrap and unwrap the data key. Either a Branch Key ID or
        Branch Key Supplier must be specified.
        :param ttl_seconds: How many seconds the Branch Key material is allowed to be
        reused within the local cache before it is re-retrieved from Amazon DynamoDB and
        re-authenticated with AWS KMS.
        :param cache: Which type of local cache to use.
        """
        self.key_store = key_store
        self.branch_key_id = branch_key_id
        self.branch_key_id_supplier = branch_key_id_supplier
        if (ttl_seconds is not None) and (ttl_seconds < 0):
            raise ValueError("ttl_seconds must be greater than or equal to 0")

        self.ttl_seconds = ttl_seconds
        self.cache = cache

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsHierarchicalKeyringInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "keyStore": self.key_store.as_dict(),
        }

        if self.branch_key_id is not None:
            d["branchKeyId"] = self.branch_key_id

        if self.branch_key_id_supplier is not None:
            d["branchKeyIdSupplier"] = self.branch_key_id_supplier.as_dict()

        if self.ttl_seconds is not None:
            d["ttlSeconds"] = self.ttl_seconds

        if self.cache is not None:
            d["cache"] = self.cache.as_dict()

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsHierarchicalKeyringInput":
        """Creates a CreateAwsKmsHierarchicalKeyringInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        from aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references import BranchKeyIdSupplier
        from aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.client import KeyStore
        kwargs: Dict[str, Any] = {
            "key_store": KeyStore.from_dict(d["keyStore"]),
        }

        if "branchKeyId" in d:
            kwargs["branch_key_id"] = d["branchKeyId"]

        if "branchKeyIdSupplier" in d:
            kwargs["branch_key_id_supplier"] = BranchKeyIdSupplier.from_dict(d["branchKeyIdSupplier"])

        if "ttlSeconds" in d:
            kwargs["ttl_seconds"] = d["ttlSeconds"]

        if "cache" in d:
            kwargs["cache"] = _cache_type_from_dict(d["cache"]),

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
            result += f"cache={repr(self.cache)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateAwsKmsHierarchicalKeyringInput):
            return False
        attributes: list[str] = ['branch_key_id','branch_key_id_supplier','key_store','ttl_seconds','cache',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class CreateAwsKmsKeyringInput:
    kms_key_id: str
    kms_client: 'botocore.client.BaseClient'
    grant_tokens: Optional[list[str]]
    def __init__(
        self,
        *,
        kms_key_id: str,
        kms_client: 'botocore.client.BaseClient',
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating a AWS KMS Keyring.

        :param kms_key_id: The identifier for the symmetric AWS KMS Key responsible for
        wrapping and unwrapping data keys. This should not be a AWS KMS Multi-Region
        Key.
        :param kms_client: The KMS Client this Keyring will use to call KMS.
        :param grant_tokens: A list of grant tokens to be used when calling KMS.
        """
        self.kms_key_id = kms_key_id
        self.kms_client = kms_client
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsKeyringInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "kmsKeyId": self.kms_key_id,
            "kmsClient": self.kms_client.as_dict(),
        }

        if self.grant_tokens is not None:
            d["grantTokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsKeyringInput":
        """Creates a CreateAwsKmsKeyringInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        from botocore.client import BaseClient
        kwargs: Dict[str, Any] = {
            "kms_key_id": d["kmsKeyId"],
            "kms_client": BaseClient.from_dict(d["kmsClient"]),
        }

        if "grantTokens" in d:
            kwargs["grant_tokens"] = d["grantTokens"]

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
        attributes: list[str] = ['kms_key_id','kms_client','grant_tokens',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class CreateAwsKmsMrkDiscoveryKeyringInput:
    kms_client: 'botocore.client.BaseClient'
    discovery_filter: Optional[DiscoveryFilter]
    grant_tokens: Optional[list[str]]
    region: str
    def __init__(
        self,
        *,
        kms_client: 'botocore.client.BaseClient',
        region: str,
        discovery_filter: Optional[DiscoveryFilter] = None,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating a AWS KMS MRK Discovery Keyring.

        :param kms_client: The KMS Client this Keyring will use to call KMS.
        :param region: The region the input 'kmsClient' is in.
        :param discovery_filter: A filter which restricts which KMS Keys this Keyring
        may attempt to decrypt with by AWS partition and account.
        :param grant_tokens: A list of grant tokens to be used when calling KMS.
        """
        self.kms_client = kms_client
        self.region = region
        self.discovery_filter = discovery_filter
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsMrkDiscoveryKeyringInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "kmsClient": self.kms_client.as_dict(),
            "region": self.region,
        }

        if self.discovery_filter is not None:
            d["discoveryFilter"] = self.discovery_filter.as_dict()

        if self.grant_tokens is not None:
            d["grantTokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsMrkDiscoveryKeyringInput":
        """Creates a CreateAwsKmsMrkDiscoveryKeyringInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        from botocore.client import BaseClient
        kwargs: Dict[str, Any] = {
            "kms_client": BaseClient.from_dict(d["kmsClient"]),
            "region": d["region"],
        }

        if "discoveryFilter" in d:
            kwargs["discovery_filter"] = DiscoveryFilter.from_dict(d["discoveryFilter"])

        if "grantTokens" in d:
            kwargs["grant_tokens"] = d["grantTokens"]

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
        attributes: list[str] = ['kms_client','discovery_filter','grant_tokens','region',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class CreateAwsKmsMrkDiscoveryMultiKeyringInput:
    regions: list[str]
    discovery_filter: Optional[DiscoveryFilter]
    client_supplier: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier']
    grant_tokens: Optional[list[str]]
    def __init__(
        self,
        *,
        regions: list[str],
        discovery_filter: Optional[DiscoveryFilter] = None,
        client_supplier: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier'] = None,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating a AWS KMS MRK Discovery Multi-Keyring.

        :param regions: The list of regions this Keyring will creates KMS clients for.
        :param discovery_filter: A filter which restricts which KMS Keys this Keyring
        may attempt to decrypt with by AWS partition and account.
        :param client_supplier: The Client Supplier which will be used to get KMS
        Clients for use with this Keyring. If not specified on input, a Default Client
        Supplier is created which creates a KMS Client for each region in the 'regions'
        input.
        :param grant_tokens: A list of grant tokens to be used when calling KMS.
        """
        self.regions = regions
        self.discovery_filter = discovery_filter
        self.client_supplier = client_supplier
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsMrkDiscoveryMultiKeyringInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "regions": self.regions,
        }

        if self.discovery_filter is not None:
            d["discoveryFilter"] = self.discovery_filter.as_dict()

        if self.client_supplier is not None:
            d["clientSupplier"] = self.client_supplier.as_dict()

        if self.grant_tokens is not None:
            d["grantTokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsMrkDiscoveryMultiKeyringInput":
        """Creates a CreateAwsKmsMrkDiscoveryMultiKeyringInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        from aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references import ClientSupplier
        kwargs: Dict[str, Any] = {
            "regions": d["regions"],
        }

        if "discoveryFilter" in d:
            kwargs["discovery_filter"] = DiscoveryFilter.from_dict(d["discoveryFilter"])

        if "clientSupplier" in d:
            kwargs["client_supplier"] = ClientSupplier.from_dict(d["clientSupplier"])

        if "grantTokens" in d:
            kwargs["grant_tokens"] = d["grantTokens"]

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
        attributes: list[str] = ['regions','discovery_filter','client_supplier','grant_tokens',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class CreateAwsKmsMrkKeyringInput:
    kms_key_id: str
    kms_client: 'botocore.client.BaseClient'
    grant_tokens: Optional[list[str]]
    def __init__(
        self,
        *,
        kms_key_id: str,
        kms_client: 'botocore.client.BaseClient',
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating an AWS KMS MRK Keyring.

        :param kms_key_id: The identifier for the symmetric AWS KMS Key or AWS KMS
        Multi-Region Key responsible for wrapping and unwrapping data keys.
        :param kms_client: The KMS Client this Keyring will use to call KMS.
        :param grant_tokens: A list of grant tokens to be used when calling KMS.
        """
        self.kms_key_id = kms_key_id
        self.kms_client = kms_client
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsMrkKeyringInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "kmsKeyId": self.kms_key_id,
            "kmsClient": self.kms_client.as_dict(),
        }

        if self.grant_tokens is not None:
            d["grantTokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsMrkKeyringInput":
        """Creates a CreateAwsKmsMrkKeyringInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        from botocore.client import BaseClient
        kwargs: Dict[str, Any] = {
            "kms_key_id": d["kmsKeyId"],
            "kms_client": BaseClient.from_dict(d["kmsClient"]),
        }

        if "grantTokens" in d:
            kwargs["grant_tokens"] = d["grantTokens"]

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
        attributes: list[str] = ['kms_key_id','kms_client','grant_tokens',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class CreateAwsKmsMrkMultiKeyringInput:
    generator: Optional[str]
    kms_key_ids: Optional[list[str]]
    client_supplier: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier']
    grant_tokens: Optional[list[str]]
    def __init__(
        self,
        *,
        generator: Optional[str] = None,
        kms_key_ids: Optional[list[str]] = None,
        client_supplier: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier'] = None,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating a AWS KMS MRK Multi-Keyring.

        :param generator: A symmetric AWS KMS Key or AWS KMS Multi-Region Key
        responsible for wrapping and unwrapping data keys. KMS.GenerateDataKey may be
        called with this key if the data key has not already been generated by another
        Keyring.
        :param kms_key_ids: A list of identifiers for the symmetric AWS KMS Keys and/or
        AWS KMS Multi-Region Keys (other than the generator) responsible for wrapping
        and unwrapping data keys.
        :param client_supplier: The Client Supplier which will be used to get KMS
        Clients for use with this Keyring. The Client Supplier will create a client for
        each region specified in the generator and kmsKeyIds ARNs. If not specified on
        input, the Default Client Supplier is used.
        :param grant_tokens: A list of grant tokens to be used when calling KMS.
        """
        self.generator = generator
        self.kms_key_ids = kms_key_ids
        self.client_supplier = client_supplier
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsMrkMultiKeyringInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {}

        if self.generator is not None:
            d["generator"] = self.generator

        if self.kms_key_ids is not None:
            d["kmsKeyIds"] = self.kms_key_ids

        if self.client_supplier is not None:
            d["clientSupplier"] = self.client_supplier.as_dict()

        if self.grant_tokens is not None:
            d["grantTokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsMrkMultiKeyringInput":
        """Creates a CreateAwsKmsMrkMultiKeyringInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        from aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references import ClientSupplier
        kwargs: Dict[str, Any] = {}

        if "generator" in d:
            kwargs["generator"] = d["generator"]

        if "kmsKeyIds" in d:
            kwargs["kms_key_ids"] = d["kmsKeyIds"]

        if "clientSupplier" in d:
            kwargs["client_supplier"] = ClientSupplier.from_dict(d["clientSupplier"])

        if "grantTokens" in d:
            kwargs["grant_tokens"] = d["grantTokens"]

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
        attributes: list[str] = ['generator','kms_key_ids','client_supplier','grant_tokens',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class CreateAwsKmsMultiKeyringInput:
    generator: Optional[str]
    kms_key_ids: Optional[list[str]]
    client_supplier: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier']
    grant_tokens: Optional[list[str]]
    def __init__(
        self,
        *,
        generator: Optional[str] = None,
        kms_key_ids: Optional[list[str]] = None,
        client_supplier: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier'] = None,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for for creating a AWS KMS Multi-Keyring.

        :param generator: A identifier for a symmetric AWS KMS Key responsible for
        wrapping and unwrapping data keys. KMS.GenerateDataKey may be called with this
        key if the data key has not already been generated by another Keyring. This
        should not be a AWS KMS Multi-Region Key.
        :param kms_key_ids: A list of identifiers for the symmetric AWS KMS Keys (other
        than the generator) responsible for wrapping and unwrapping data keys. This list
        should not contain AWS KMS Multi-Region Keys.
        :param client_supplier: The Client Supplier which will be used to get KMS
        Clients for use with this Keyring. The Client Supplier will create a client for
        each region specified in the generator and kmsKeyIds ARNs. If not specified on
        input, the Default Client Supplier is used.
        :param grant_tokens: A list of grant tokens to be used when calling KMS.
        """
        self.generator = generator
        self.kms_key_ids = kms_key_ids
        self.client_supplier = client_supplier
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsMultiKeyringInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {}

        if self.generator is not None:
            d["generator"] = self.generator

        if self.kms_key_ids is not None:
            d["kmsKeyIds"] = self.kms_key_ids

        if self.client_supplier is not None:
            d["clientSupplier"] = self.client_supplier.as_dict()

        if self.grant_tokens is not None:
            d["grantTokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsMultiKeyringInput":
        """Creates a CreateAwsKmsMultiKeyringInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        from aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references import ClientSupplier
        kwargs: Dict[str, Any] = {}

        if "generator" in d:
            kwargs["generator"] = d["generator"]

        if "kmsKeyIds" in d:
            kwargs["kms_key_ids"] = d["kmsKeyIds"]

        if "clientSupplier" in d:
            kwargs["client_supplier"] = ClientSupplier.from_dict(d["clientSupplier"])

        if "grantTokens" in d:
            kwargs["grant_tokens"] = d["grantTokens"]

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
        attributes: list[str] = ['generator','kms_key_ids','client_supplier','grant_tokens',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class CreateAwsKmsRsaKeyringInput:
    public_key: Optional[bytes | bytearray]
    kms_key_id: str
    encryption_algorithm: str
    kms_client: Optional['botocore.client.BaseClient']
    grant_tokens: Optional[list[str]]
    def __init__(
        self,
        *,
        kms_key_id: str,
        encryption_algorithm: str,
        public_key: Optional[bytes | bytearray] = None,
        kms_client: Optional['botocore.client.BaseClient'] = None,
        grant_tokens: Optional[list[str]] = None,
    ):
        """Inputs for creating a AWS KMS RSA Keyring.

        :param kms_key_id: The ARN for the asymmetric AWS KMS Key for RSA responsible
        for wrapping and unwrapping data keys.
        :param encryption_algorithm: The RSA algorithm used to wrap and unwrap data
        keys.
        :param public_key: The public RSA Key responsible for wrapping data keys, as a
        UTF8 encoded, PEM encoded X.509 SubjectPublicKeyInfo structure. This should be
        the public key as exported from KMS. If not specified, this Keyring cannot be
        used on encrypt.
        :param kms_client: The KMS Client this Keyring will use to call KMS.
        :param grant_tokens: A list of grant tokens to be used when calling KMS.
        """
        self.kms_key_id = kms_key_id
        self.encryption_algorithm = encryption_algorithm
        self.public_key = public_key
        self.kms_client = kms_client
        self.grant_tokens = grant_tokens

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateAwsKmsRsaKeyringInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "kmsKeyId": self.kms_key_id,
            "encryptionAlgorithm": self.encryption_algorithm,
        }

        if self.public_key is not None:
            d["publicKey"] = self.public_key

        if self.kms_client is not None:
            d["kmsClient"] = self.kms_client.as_dict()

        if self.grant_tokens is not None:
            d["grantTokens"] = self.grant_tokens

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateAwsKmsRsaKeyringInput":
        """Creates a CreateAwsKmsRsaKeyringInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        from botocore.client import BaseClient
        kwargs: Dict[str, Any] = {
            "kms_key_id": d["kmsKeyId"],
            "encryption_algorithm": d["encryptionAlgorithm"],
        }

        if "publicKey" in d:
            kwargs["public_key"] = d["publicKey"]

        if "kmsClient" in d:
            kwargs["kms_client"] = BaseClient.from_dict(d["kmsClient"])

        if "grantTokens" in d:
            kwargs["grant_tokens"] = d["grantTokens"]

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
        attributes: list[str] = ['public_key','kms_key_id','encryption_algorithm','kms_client','grant_tokens',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the CreateCryptographicMaterialsCacheInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "cache": self.cache.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateCryptographicMaterialsCacheInput":
        """Creates a CreateCryptographicMaterialsCacheInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
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
        attributes: list[str] = ['cache',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class CreateDefaultClientSupplierInput:
    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateDefaultClientSupplierInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateDefaultClientSupplierInput":
        """Creates a CreateDefaultClientSupplierInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        return CreateDefaultClientSupplierInput()

    def __repr__(self) -> str:
        result = "CreateDefaultClientSupplierInput("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, CreateDefaultClientSupplierInput)

class CreateDefaultCryptographicMaterialsManagerInput:
    keyring: 'aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.Keyring'
    def __init__(
        self,
        *,
        keyring: 'aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.Keyring',
    ):
        """Inputs for creating a Default Cryptographic Materials Manager.

        :param keyring: The Keyring that the created Default Cryprographic Materials
        Manager will use to wrap data keys.
        """
        self.keyring = keyring

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateDefaultCryptographicMaterialsManagerInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyring": self.keyring.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateDefaultCryptographicMaterialsManagerInput":
        """Creates a CreateDefaultCryptographicMaterialsManagerInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        from aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references import Keyring
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
        attributes: list[str] = ['keyring',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class CreateMultiKeyringInput:
    generator: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.Keyring']
    child_keyrings: list['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.Keyring']
    def __init__(
        self,
        *,
        child_keyrings: list['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.Keyring'],
        generator: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.Keyring'] = None,
    ):
        """Inputs for creating a Multi-Keyring.

        :param child_keyrings: A list of keyrings (other than the generator) responsible
        for wrapping and unwrapping the data key.
        :param generator: A keyring responsible for wrapping and unwrapping the data
        key. This is the first keyring that will be used to wrap the data key, and may
        be responsible for additionally generating the data key.
        """
        self.child_keyrings = child_keyrings
        self.generator = generator

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateMultiKeyringInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "childKeyrings": self.child_keyrings,
        }

        if self.generator is not None:
            d["generator"] = self.generator.as_dict()

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateMultiKeyringInput":
        """Creates a CreateMultiKeyringInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        from aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references import Keyring
        kwargs: Dict[str, Any] = {
            "child_keyrings": d["childKeyrings"],
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
        attributes: list[str] = ['generator','child_keyrings',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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

        :param key_namespace: A namespace associated with this wrapping key.
        :param key_name: A name associated with this wrapping key.
        :param wrapping_key: The AES key used with AES_GCM encryption and decryption.
        :param wrapping_alg: The AES_GCM algorithm this Keyring uses to wrap and unwrap
        data keys.
        """
        self.key_namespace = key_namespace
        self.key_name = key_name
        self.wrapping_key = wrapping_key
        self.wrapping_alg = wrapping_alg

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateRawAesKeyringInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyNamespace": self.key_namespace,
            "keyName": self.key_name,
            "wrappingKey": self.wrapping_key,
            "wrappingAlg": self.wrapping_alg,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateRawAesKeyringInput":
        """Creates a CreateRawAesKeyringInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_namespace": d["keyNamespace"],
            "key_name": d["keyName"],
            "wrapping_key": d["wrappingKey"],
            "wrapping_alg": d["wrappingAlg"],
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
        attributes: list[str] = ['key_namespace','key_name','wrapping_key','wrapping_alg',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class PaddingScheme:
    PKCS1 = "PKCS1"

    OAEP_SHA1_MGF1 = "OAEP_SHA1_MGF1"

    OAEP_SHA256_MGF1 = "OAEP_SHA256_MGF1"

    OAEP_SHA384_MGF1 = "OAEP_SHA384_MGF1"

    OAEP_SHA512_MGF1 = "OAEP_SHA512_MGF1"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset({"PKCS1", "OAEP_SHA1_MGF1", "OAEP_SHA256_MGF1", "OAEP_SHA384_MGF1", "OAEP_SHA512_MGF1"})

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

        :param key_namespace: A namespace associated with this wrapping key.
        :param key_name: A name associated with this wrapping key.
        :param padding_scheme: The RSA padding scheme to use with this keyring.
        :param public_key: The public RSA Key responsible for wrapping data keys, as a
        UTF8 encoded, PEM encoded X.509 SubjectPublicKeyInfo structure. If not
        specified, this Keyring cannot be used on encrypt. A public key and/or a private
        key must be specified.
        :param private_key: The private RSA Key responsible for wrapping data keys, as a
        UTF8 encoded, PEM encoded PKCS #8 PrivateKeyInfo structure. If not specified,
        this Keyring cannot be used on decrypt. A public key and/or a private key must
        be specified.
        """
        self.key_namespace = key_namespace
        self.key_name = key_name
        self.padding_scheme = padding_scheme
        self.public_key = public_key
        self.private_key = private_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateRawRsaKeyringInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "keyNamespace": self.key_namespace,
            "keyName": self.key_name,
            "paddingScheme": self.padding_scheme,
        }

        if self.public_key is not None:
            d["publicKey"] = self.public_key

        if self.private_key is not None:
            d["privateKey"] = self.private_key

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateRawRsaKeyringInput":
        """Creates a CreateRawRsaKeyringInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_namespace": d["keyNamespace"],
            "key_name": d["keyName"],
            "padding_scheme": d["paddingScheme"],
        }

        if "publicKey" in d:
            kwargs["public_key"] = d["publicKey"]

        if "privateKey" in d:
            kwargs["private_key"] = d["privateKey"]

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
        attributes: list[str] = ['key_namespace','key_name','padding_scheme','public_key','private_key',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class CreateRequiredEncryptionContextCMMInput:
    underlying_cmm: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.CryptographicMaterialsManager']
    keyring: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.Keyring']
    required_encryption_context_keys: list[str]
    def __init__(
        self,
        *,
        required_encryption_context_keys: list[str],
        underlying_cmm: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.CryptographicMaterialsManager'] = None,
        keyring: Optional['aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references.Keyring'] = None,
    ):
        """Inputs for creating an Required Encryption Context Cryptographic Materials
        Manager.

        :param required_encryption_context_keys: A list of Encryption Context keys which
        are required to be supplied during encryption and decryption, and correspond to
        Encryption Context key-value pairs which are not stored on the resulting
        message.
        :param underlying_cmm: The Cryprographic Materials Manager that the created
        Required Encryption Context Cryptographic Materials Manager will delegate to.
        Either a Keyring or underlying Cryprographic Materials Manager must be
        specified.
        :param keyring: The Keyring that the created Cryprographic Materials Manager
        will use to wrap data keys. The created Required Encryption Context CMM will
        delegate to a Default Cryptographic Materials Manager created with this Keyring.
        Either a Keyring or an underlying Cryprographic Materials Manager must be
        specified as input.
        """
        self.required_encryption_context_keys = required_encryption_context_keys
        self.underlying_cmm = underlying_cmm
        self.keyring = keyring

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateRequiredEncryptionContextCMMInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "requiredEncryptionContextKeys": self.required_encryption_context_keys,
        }

        if self.underlying_cmm is not None:
            d["underlyingCMM"] = self.underlying_cmm.as_dict()

        if self.keyring is not None:
            d["keyring"] = self.keyring.as_dict()

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateRequiredEncryptionContextCMMInput":
        """Creates a CreateRequiredEncryptionContextCMMInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        from aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references import CryptographicMaterialsManager
        from aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.references import Keyring
        kwargs: Dict[str, Any] = {
            "required_encryption_context_keys": d["requiredEncryptionContextKeys"],
        }

        if "underlyingCMM" in d:
            kwargs["underlying_cmm"] = CryptographicMaterialsManager.from_dict(d["underlyingCMM"])

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
        attributes: list[str] = ['underlying_cmm','keyring','required_encryption_context_keys',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class DeleteCacheEntryInput:
    identifier: bytes | bytearray
    def __init__(
        self,
        *,
        identifier: bytes | bytearray,
    ):
        self.identifier = identifier

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DeleteCacheEntryInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "identifier": self.identifier,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DeleteCacheEntryInput":
        """Creates a DeleteCacheEntryInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
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
        attributes: list[str] = ['identifier',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the GetCacheEntryInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "identifier": self.identifier,
        }

        if self.bytes_used is not None:
            d["bytesUsed"] = self.bytes_used

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetCacheEntryInput":
        """Creates a GetCacheEntryInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
        }

        if "bytesUsed" in d:
            kwargs["bytes_used"] = d["bytesUsed"]

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
        attributes: list[str] = ['identifier','bytes_used',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the DecryptionMaterials to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "algorithmSuite": self.algorithm_suite.as_dict(),
            "encryptionContext": self.encryption_context,
            "requiredEncryptionContextKeys": self.required_encryption_context_keys,
        }

        if self.plaintext_data_key is not None:
            d["plaintextDataKey"] = self.plaintext_data_key

        if self.verification_key is not None:
            d["verificationKey"] = self.verification_key

        if self.symmetric_signing_key is not None:
            d["symmetricSigningKey"] = self.symmetric_signing_key

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DecryptionMaterials":
        """Creates a DecryptionMaterials from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "algorithm_suite": AlgorithmSuiteInfo.from_dict(d["algorithmSuite"]),
            "encryption_context": d["encryptionContext"],
            "required_encryption_context_keys": d["requiredEncryptionContextKeys"],
        }

        if "plaintextDataKey" in d:
            kwargs["plaintext_data_key"] = d["plaintextDataKey"]

        if "verificationKey" in d:
            kwargs["verification_key"] = d["verificationKey"]

        if "symmetricSigningKey" in d:
            kwargs["symmetric_signing_key"] = d["symmetricSigningKey"]

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
        attributes: list[str] = ['algorithm_suite','encryption_context','required_encryption_context_keys','plaintext_data_key','verification_key','symmetric_signing_key',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the EncryptedDataKey to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyProviderId": self.key_provider_id,
            "keyProviderInfo": self.key_provider_info,
            "ciphertext": self.ciphertext,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EncryptedDataKey":
        """Creates a EncryptedDataKey from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_provider_id": d["keyProviderId"],
            "key_provider_info": d["keyProviderInfo"],
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
        attributes: list[str] = ['key_provider_id','key_provider_info','ciphertext',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the EncryptionMaterials to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "algorithmSuite": self.algorithm_suite.as_dict(),
            "encryptionContext": self.encryption_context,
            "encryptedDataKeys": _encrypted_data_key_list_as_dict(self.encrypted_data_keys),
            "requiredEncryptionContextKeys": self.required_encryption_context_keys,
        }

        if self.plaintext_data_key is not None:
            d["plaintextDataKey"] = self.plaintext_data_key

        if self.signing_key is not None:
            d["signingKey"] = self.signing_key

        if self.symmetric_signing_keys is not None:
            d["symmetricSigningKeys"] = self.symmetric_signing_keys

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EncryptionMaterials":
        """Creates a EncryptionMaterials from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "algorithm_suite": AlgorithmSuiteInfo.from_dict(d["algorithmSuite"]),
            "encryption_context": d["encryptionContext"],
            "encrypted_data_keys": _encrypted_data_key_list_from_dict(d["encryptedDataKeys"]),
            "required_encryption_context_keys": d["requiredEncryptionContextKeys"],
        }

        if "plaintextDataKey" in d:
            kwargs["plaintext_data_key"] = d["plaintextDataKey"]

        if "signingKey" in d:
            kwargs["signing_key"] = d["signingKey"]

        if "symmetricSigningKeys" in d:
            kwargs["symmetric_signing_keys"] = d["symmetricSigningKeys"]

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
        attributes: list[str] = ['algorithm_suite','encryption_context','encrypted_data_keys','required_encryption_context_keys','plaintext_data_key','signing_key','symmetric_signing_keys',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class MaterialsEncryption():
    def __init__(self, value: EncryptionMaterials):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"Encryption": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MaterialsEncryption":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return MaterialsEncryption(EncryptionMaterials.from_dict(d["Encryption"]))

    def __repr__(self) -> str:
        return f"MaterialsEncryption(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MaterialsEncryption):
            return False
        return self.value == other.value

class MaterialsDecryption():
    def __init__(self, value: DecryptionMaterials):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"Decryption": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MaterialsDecryption":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return MaterialsDecryption(DecryptionMaterials.from_dict(d["Decryption"]))

    def __repr__(self) -> str:
        return f"MaterialsDecryption(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MaterialsDecryption):
            return False
        return self.value == other.value

class MaterialsBranchKey():
    def __init__(self, value: BranchKeyMaterials):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"BranchKey": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MaterialsBranchKey":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return MaterialsBranchKey(BranchKeyMaterials.from_dict(d["BranchKey"]))

    def __repr__(self) -> str:
        return f"MaterialsBranchKey(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MaterialsBranchKey):
            return False
        return self.value == other.value

class MaterialsBeaconKey():
    def __init__(self, value: BeaconKeyMaterials):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"BeaconKey": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MaterialsBeaconKey":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return MaterialsBeaconKey(BeaconKeyMaterials.from_dict(d["BeaconKey"]))

    def __repr__(self) -> str:
        return f"MaterialsBeaconKey(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MaterialsBeaconKey):
            return False
        return self.value == other.value

class Materials():
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to receive the
    parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Materials":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return Materials(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"Materials(tag={self.tag})"

Materials = Union[MaterialsEncryption, MaterialsDecryption, MaterialsBranchKey, MaterialsBeaconKey, Materials]
def _materials_from_dict(d: Dict[str, Any]) -> Materials:
    if "Encryption" in d:
        return MaterialsEncryption.from_dict(d)

    if "Decryption" in d:
        return MaterialsDecryption.from_dict(d)

    if "BranchKey" in d:
        return MaterialsBranchKey.from_dict(d)

    if "BeaconKey" in d:
        return MaterialsBeaconKey.from_dict(d)

    raise TypeError(f'Unions may have exactly 1 value, but found {len(d)}')

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
        """Converts the GetCacheEntryOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "materials": self.materials.as_dict(),
        }

        if self.creation_time is not None:
            d["creationTime"] = self.creation_time

        if self.expiry_time is not None:
            d["expiryTime"] = self.expiry_time

        if self.messages_used is not None:
            d["messagesUsed"] = self.messages_used

        if self.bytes_used is not None:
            d["bytesUsed"] = self.bytes_used

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetCacheEntryOutput":
        """Creates a GetCacheEntryOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "materials": _materials_from_dict(d["materials"]),
        }

        if "creationTime" in d:
            kwargs["creation_time"] = d["creationTime"]

        if "expiryTime" in d:
            kwargs["expiry_time"] = d["expiryTime"]

        if "messagesUsed" in d:
            kwargs["messages_used"] = d["messagesUsed"]

        if "bytesUsed" in d:
            kwargs["bytes_used"] = d["bytesUsed"]

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
        attributes: list[str] = ['materials','creation_time','expiry_time','messages_used','bytes_used',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the PutCacheEntryInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "identifier": self.identifier,
            "materials": self.materials.as_dict(),
        }

        if self.creation_time is not None:
            d["creationTime"] = self.creation_time

        if self.expiry_time is not None:
            d["expiryTime"] = self.expiry_time

        if self.messages_used is not None:
            d["messagesUsed"] = self.messages_used

        if self.bytes_used is not None:
            d["bytesUsed"] = self.bytes_used

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "PutCacheEntryInput":
        """Creates a PutCacheEntryInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
            "materials": _materials_from_dict(d["materials"]),
        }

        if "creationTime" in d:
            kwargs["creation_time"] = d["creationTime"]

        if "expiryTime" in d:
            kwargs["expiry_time"] = d["expiryTime"]

        if "messagesUsed" in d:
            kwargs["messages_used"] = d["messagesUsed"]

        if "bytesUsed" in d:
            kwargs["bytes_used"] = d["bytesUsed"]

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
        attributes: list[str] = ['identifier','materials','creation_time','expiry_time','messages_used','bytes_used',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the UpdateUsageMetadataInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "identifier": self.identifier,
        }

        if self.bytes_used is not None:
            d["bytesUsed"] = self.bytes_used

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "UpdateUsageMetadataInput":
        """Creates a UpdateUsageMetadataInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
        }

        if "bytesUsed" in d:
            kwargs["bytes_used"] = d["bytesUsed"]

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
        attributes: list[str] = ['identifier','bytes_used',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
    values = frozenset({"FORBID_ENCRYPT_ALLOW_DECRYPT", "REQUIRE_ENCRYPT_ALLOW_DECRYPT", "REQUIRE_ENCRYPT_REQUIRE_DECRYPT"})

class CommitmentPolicyESDK():
    def __init__(self, value: str):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"ESDK": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CommitmentPolicyESDK":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return CommitmentPolicyESDK(d["ESDK"])

    def __repr__(self) -> str:
        return f"CommitmentPolicyESDK(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CommitmentPolicyESDK):
            return False
        return self.value == other.value

class CommitmentPolicyDBE():
    def __init__(self, value: str):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"DBE": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CommitmentPolicyDBE":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return CommitmentPolicyDBE(d["DBE"])

    def __repr__(self) -> str:
        return f"CommitmentPolicyDBE(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CommitmentPolicyDBE):
            return False
        return self.value == other.value

class CommitmentPolicy():
    """Represents an unknown variant.

    If you receive this value, you will need to update your library to receive the
    parsed value.

    This value may not be deliberately sent.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def as_dict(self) -> Dict[str, Any]:
        return {"SDK_UNKNOWN_MEMBER": {"name": self.tag}}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CommitmentPolicy":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return CommitmentPolicy(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"CommitmentPolicy(tag={self.tag})"

CommitmentPolicy = Union[CommitmentPolicyESDK, CommitmentPolicyDBE, CommitmentPolicy]
def _commitment_policy_from_dict(d: Dict[str, Any]) -> CommitmentPolicy:
    if "ESDK" in d:
        return CommitmentPolicyESDK.from_dict(d)

    if "DBE" in d:
        return CommitmentPolicyDBE.from_dict(d)

    raise TypeError(f'Unions may have exactly 1 value, but found {len(d)}')

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
        """Converts the DecryptMaterialsInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "algorithmSuiteId": self.algorithm_suite_id.as_dict(),
            "commitmentPolicy": self.commitment_policy.as_dict(),
            "encryptedDataKeys": _encrypted_data_key_list_as_dict(self.encrypted_data_keys),
            "encryptionContext": self.encryption_context,
        }

        if self.reproduced_encryption_context is not None:
            d["reproducedEncryptionContext"] = self.reproduced_encryption_context

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DecryptMaterialsInput":
        """Creates a DecryptMaterialsInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "algorithm_suite_id": _algorithm_suite_id_from_dict(d["algorithmSuiteId"]),
            "commitment_policy": _commitment_policy_from_dict(d["commitmentPolicy"]),
            "encrypted_data_keys": _encrypted_data_key_list_from_dict(d["encryptedDataKeys"]),
            "encryption_context": d["encryptionContext"],
        }

        if "reproducedEncryptionContext" in d:
            kwargs["reproduced_encryption_context"] = d["reproducedEncryptionContext"]

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
        attributes: list[str] = ['algorithm_suite_id','commitment_policy','encrypted_data_keys','encryption_context','reproduced_encryption_context',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class DecryptMaterialsOutput:
    decryption_materials: DecryptionMaterials
    def __init__(
        self,
        *,
        decryption_materials: DecryptionMaterials,
    ):
        self.decryption_materials = decryption_materials

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DecryptMaterialsOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "decryptionMaterials": self.decryption_materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DecryptMaterialsOutput":
        """Creates a DecryptMaterialsOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "decryption_materials": DecryptionMaterials.from_dict(d["decryptionMaterials"]),
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
        attributes: list[str] = ['decryption_materials',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the GetEncryptionMaterialsInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "encryptionContext": self.encryption_context,
            "commitmentPolicy": self.commitment_policy.as_dict(),
        }

        if self.algorithm_suite_id is not None:
            d["algorithmSuiteId"] = self.algorithm_suite_id.as_dict()

        if self.max_plaintext_length is not None:
            d["maxPlaintextLength"] = self.max_plaintext_length

        if self.required_encryption_context_keys is not None:
            d["requiredEncryptionContextKeys"] = self.required_encryption_context_keys

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetEncryptionMaterialsInput":
        """Creates a GetEncryptionMaterialsInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "encryption_context": d["encryptionContext"],
            "commitment_policy": _commitment_policy_from_dict(d["commitmentPolicy"]),
        }

        if "algorithmSuiteId" in d:
            kwargs["algorithm_suite_id"] = _algorithm_suite_id_from_dict(d["algorithmSuiteId"]),

        if "maxPlaintextLength" in d:
            kwargs["max_plaintext_length"] = d["maxPlaintextLength"]

        if "requiredEncryptionContextKeys" in d:
            kwargs["required_encryption_context_keys"] = d["requiredEncryptionContextKeys"]

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
        attributes: list[str] = ['encryption_context','commitment_policy','algorithm_suite_id','max_plaintext_length','required_encryption_context_keys',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class GetEncryptionMaterialsOutput:
    encryption_materials: EncryptionMaterials
    def __init__(
        self,
        *,
        encryption_materials: EncryptionMaterials,
    ):
        self.encryption_materials = encryption_materials

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetEncryptionMaterialsOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "encryptionMaterials": self.encryption_materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetEncryptionMaterialsOutput":
        """Creates a GetEncryptionMaterialsOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "encryption_materials": EncryptionMaterials.from_dict(d["encryptionMaterials"]),
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
        attributes: list[str] = ['encryption_materials',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the InitializeDecryptionMaterialsInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "algorithmSuiteId": self.algorithm_suite_id.as_dict(),
            "encryptionContext": self.encryption_context,
            "requiredEncryptionContextKeys": self.required_encryption_context_keys,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InitializeDecryptionMaterialsInput":
        """Creates a InitializeDecryptionMaterialsInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "algorithm_suite_id": _algorithm_suite_id_from_dict(d["algorithmSuiteId"]),
            "encryption_context": d["encryptionContext"],
            "required_encryption_context_keys": d["requiredEncryptionContextKeys"],
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
        attributes: list[str] = ['algorithm_suite_id','encryption_context','required_encryption_context_keys',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the InitializeEncryptionMaterialsInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "algorithmSuiteId": self.algorithm_suite_id.as_dict(),
            "encryptionContext": self.encryption_context,
            "requiredEncryptionContextKeys": self.required_encryption_context_keys,
        }

        if self.signing_key is not None:
            d["signingKey"] = self.signing_key

        if self.verification_key is not None:
            d["verificationKey"] = self.verification_key

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InitializeEncryptionMaterialsInput":
        """Creates a InitializeEncryptionMaterialsInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "algorithm_suite_id": _algorithm_suite_id_from_dict(d["algorithmSuiteId"]),
            "encryption_context": d["encryptionContext"],
            "required_encryption_context_keys": d["requiredEncryptionContextKeys"],
        }

        if "signingKey" in d:
            kwargs["signing_key"] = d["signingKey"]

        if "verificationKey" in d:
            kwargs["verification_key"] = d["verificationKey"]

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
        attributes: list[str] = ['algorithm_suite_id','encryption_context','required_encryption_context_keys','signing_key','verification_key',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the OnDecryptInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "materials": self.materials.as_dict(),
            "encryptedDataKeys": _encrypted_data_key_list_as_dict(self.encrypted_data_keys),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "OnDecryptInput":
        """Creates a OnDecryptInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "materials": DecryptionMaterials.from_dict(d["materials"]),
            "encrypted_data_keys": _encrypted_data_key_list_from_dict(d["encryptedDataKeys"]),
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
        attributes: list[str] = ['materials','encrypted_data_keys',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class OnDecryptOutput:
    materials: DecryptionMaterials
    def __init__(
        self,
        *,
        materials: DecryptionMaterials,
    ):
        self.materials = materials

    def as_dict(self) -> Dict[str, Any]:
        """Converts the OnDecryptOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "materials": self.materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "OnDecryptOutput":
        """Creates a OnDecryptOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
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
        attributes: list[str] = ['materials',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class OnEncryptInput:
    materials: EncryptionMaterials
    def __init__(
        self,
        *,
        materials: EncryptionMaterials,
    ):
        self.materials = materials

    def as_dict(self) -> Dict[str, Any]:
        """Converts the OnEncryptInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "materials": self.materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "OnEncryptInput":
        """Creates a OnEncryptInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
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
        attributes: list[str] = ['materials',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class OnEncryptOutput:
    materials: EncryptionMaterials
    def __init__(
        self,
        *,
        materials: EncryptionMaterials,
    ):
        self.materials = materials

    def as_dict(self) -> Dict[str, Any]:
        """Converts the OnEncryptOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "materials": self.materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "OnEncryptOutput":
        """Creates a OnEncryptOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
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
        attributes: list[str] = ['materials',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the ValidateCommitmentPolicyOnDecryptInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "algorithm": self.algorithm.as_dict(),
            "commitmentPolicy": self.commitment_policy.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ValidateCommitmentPolicyOnDecryptInput":
        """Creates a ValidateCommitmentPolicyOnDecryptInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "algorithm": _algorithm_suite_id_from_dict(d["algorithm"]),
            "commitment_policy": _commitment_policy_from_dict(d["commitmentPolicy"]),
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
        attributes: list[str] = ['algorithm','commitment_policy',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the ValidateCommitmentPolicyOnEncryptInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "algorithm": self.algorithm.as_dict(),
            "commitmentPolicy": self.commitment_policy.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ValidateCommitmentPolicyOnEncryptInput":
        """Creates a ValidateCommitmentPolicyOnEncryptInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "algorithm": _algorithm_suite_id_from_dict(d["algorithm"]),
            "commitment_policy": _commitment_policy_from_dict(d["commitmentPolicy"]),
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
        attributes: list[str] = ['algorithm','commitment_policy',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the ValidDecryptionMaterialsTransitionInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "start": self.start.as_dict(),
            "stop": self.stop.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ValidDecryptionMaterialsTransitionInput":
        """Creates a ValidDecryptionMaterialsTransitionInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
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
        attributes: list[str] = ['start','stop',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the ValidEncryptionMaterialsTransitionInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "start": self.start.as_dict(),
            "stop": self.stop.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ValidEncryptionMaterialsTransitionInput":
        """Creates a ValidEncryptionMaterialsTransitionInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
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
        attributes: list[str] = ['start','stop',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

def _encrypted_data_key_list_as_dict(given: list[EncryptedDataKey]) -> List[Any]:
    return [v.as_dict() for v in given]

def _encrypted_data_key_list_from_dict(given: List[Any]) -> list[EncryptedDataKey]:
    return [EncryptedDataKey.from_dict(v) for v in given]

class Unit:
    pass
