# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from typing import Any, Dict, List, Optional, Union

from aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models import (
    DiscoveryFilter,
)


class CmmOperation:
    ENCRYPT = "ENCRYPT"

    DECRYPT = "DECRYPT"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset({"ENCRYPT", "DECRYPT"})

class RawAES:
    key_id: str
    provider_id: str
    def __init__(
        self,
        *,
        key_id: str,
        provider_id: str,
    ):
        self.key_id = key_id
        self.provider_id = provider_id

    def as_dict(self) -> Dict[str, Any]:
        """Converts the RawAES to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyId": self.key_id,
            "providerId": self.provider_id,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RawAES":
        """Creates a RawAES from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_id": d["keyId"],
            "provider_id": d["providerId"],
        }

        return RawAES(**kwargs)

    def __repr__(self) -> str:
        result = "RawAES("
        if self.key_id is not None:
            result += f"key_id={repr(self.key_id)}, "

        if self.provider_id is not None:
            result += f"provider_id={repr(self.provider_id)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, RawAES):
            return False
        attributes: list[str] = ['key_id','provider_id',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class HierarchyKeyring:
    key_id: str
    def __init__(
        self,
        *,
        key_id: str,
    ):
        self.key_id = key_id

    def as_dict(self) -> Dict[str, Any]:
        """Converts the HierarchyKeyring to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyId": self.key_id,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "HierarchyKeyring":
        """Creates a HierarchyKeyring from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_id": d["keyId"],
        }

        return HierarchyKeyring(**kwargs)

    def __repr__(self) -> str:
        result = "HierarchyKeyring("
        if self.key_id is not None:
            result += f"key_id={repr(self.key_id)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, HierarchyKeyring):
            return False
        attributes: list[str] = ['key_id',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class KMSInfo:
    key_id: str
    def __init__(
        self,
        *,
        key_id: str,
    ):
        self.key_id = key_id

    def as_dict(self) -> Dict[str, Any]:
        """Converts the KMSInfo to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyId": self.key_id,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KMSInfo":
        """Creates a KMSInfo from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_id": d["keyId"],
        }

        return KMSInfo(**kwargs)

    def __repr__(self) -> str:
        result = "KMSInfo("
        if self.key_id is not None:
            result += f"key_id={repr(self.key_id)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KMSInfo):
            return False
        attributes: list[str] = ['key_id',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class KmsMrkAware:
    key_id: str
    def __init__(
        self,
        *,
        key_id: str,
    ):
        self.key_id = key_id

    def as_dict(self) -> Dict[str, Any]:
        """Converts the KmsMrkAware to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyId": self.key_id,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KmsMrkAware":
        """Creates a KmsMrkAware from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_id": d["keyId"],
        }

        return KmsMrkAware(**kwargs)

    def __repr__(self) -> str:
        result = "KmsMrkAware("
        if self.key_id is not None:
            result += f"key_id={repr(self.key_id)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KmsMrkAware):
            return False
        attributes: list[str] = ['key_id',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class KmsMrkAwareDiscovery:
    key_id: str
    default_mrk_region: str
    aws_kms_discovery_filter: Optional[DiscoveryFilter]
    def __init__(
        self,
        *,
        key_id: str,
        default_mrk_region: str,
        aws_kms_discovery_filter: Optional[DiscoveryFilter] = None,
    ):
        """
        :param aws_kms_discovery_filter: A filter which defines what AWS partition and
        AWS accounts a KMS Key may be in for a Keyring to be allowed to attempt to
        decrypt it.
        """
        self.key_id = key_id
        self.default_mrk_region = default_mrk_region
        self.aws_kms_discovery_filter = aws_kms_discovery_filter

    def as_dict(self) -> Dict[str, Any]:
        """Converts the KmsMrkAwareDiscovery to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "keyId": self.key_id,
            "defaultMrkRegion": self.default_mrk_region,
        }

        if self.aws_kms_discovery_filter is not None:
            d["awsKmsDiscoveryFilter"] = self.aws_kms_discovery_filter.as_dict()

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KmsMrkAwareDiscovery":
        """Creates a KmsMrkAwareDiscovery from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_id": d["keyId"],
            "default_mrk_region": d["defaultMrkRegion"],
        }

        if "awsKmsDiscoveryFilter" in d:
            kwargs["aws_kms_discovery_filter"] = DiscoveryFilter.from_dict(d["awsKmsDiscoveryFilter"])

        return KmsMrkAwareDiscovery(**kwargs)

    def __repr__(self) -> str:
        result = "KmsMrkAwareDiscovery("
        if self.key_id is not None:
            result += f"key_id={repr(self.key_id)}, "

        if self.default_mrk_region is not None:
            result += f"default_mrk_region={repr(self.default_mrk_region)}, "

        if self.aws_kms_discovery_filter is not None:
            result += f"aws_kms_discovery_filter={repr(self.aws_kms_discovery_filter)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KmsMrkAwareDiscovery):
            return False
        attributes: list[str] = ['key_id','default_mrk_region','aws_kms_discovery_filter',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class KmsRsaKeyring:
    key_id: str
    encryption_algorithm: str
    def __init__(
        self,
        *,
        key_id: str,
        encryption_algorithm: str,
    ):
        self.key_id = key_id
        self.encryption_algorithm = encryption_algorithm

    def as_dict(self) -> Dict[str, Any]:
        """Converts the KmsRsaKeyring to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyId": self.key_id,
            "encryptionAlgorithm": self.encryption_algorithm,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KmsRsaKeyring":
        """Creates a KmsRsaKeyring from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_id": d["keyId"],
            "encryption_algorithm": d["encryptionAlgorithm"],
        }

        return KmsRsaKeyring(**kwargs)

    def __repr__(self) -> str:
        result = "KmsRsaKeyring("
        if self.key_id is not None:
            result += f"key_id={repr(self.key_id)}, "

        if self.encryption_algorithm is not None:
            result += f"encryption_algorithm={repr(self.encryption_algorithm)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KmsRsaKeyring):
            return False
        attributes: list[str] = ['key_id','encryption_algorithm',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class RawRSA:
    key_id: str
    provider_id: str
    padding: str
    def __init__(
        self,
        *,
        key_id: str,
        provider_id: str,
        padding: str,
    ):
        self.key_id = key_id
        self.provider_id = provider_id
        self.padding = padding

    def as_dict(self) -> Dict[str, Any]:
        """Converts the RawRSA to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyId": self.key_id,
            "providerId": self.provider_id,
            "padding": self.padding,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RawRSA":
        """Creates a RawRSA from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_id": d["keyId"],
            "provider_id": d["providerId"],
            "padding": d["padding"],
        }

        return RawRSA(**kwargs)

    def __repr__(self) -> str:
        result = "RawRSA("
        if self.key_id is not None:
            result += f"key_id={repr(self.key_id)}, "

        if self.provider_id is not None:
            result += f"provider_id={repr(self.provider_id)}, "

        if self.padding is not None:
            result += f"padding={repr(self.padding)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, RawRSA):
            return False
        attributes: list[str] = ['key_id','provider_id','padding',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class StaticKeyring:
    key_id: str
    def __init__(
        self,
        *,
        key_id: str,
    ):
        self.key_id = key_id

    def as_dict(self) -> Dict[str, Any]:
        """Converts the StaticKeyring to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyId": self.key_id,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "StaticKeyring":
        """Creates a StaticKeyring from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_id": d["keyId"],
        }

        return StaticKeyring(**kwargs)

    def __repr__(self) -> str:
        result = "StaticKeyring("
        if self.key_id is not None:
            result += f"key_id={repr(self.key_id)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, StaticKeyring):
            return False
        attributes: list[str] = ['key_id',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class GetKeyDescriptionInput:
    json: bytes | bytearray
    def __init__(
        self,
        *,
        json: bytes | bytearray,
    ):
        self.json = json

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetKeyDescriptionInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "json": self.json,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetKeyDescriptionInput":
        """Creates a GetKeyDescriptionInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "json": d["json"],
        }

        return GetKeyDescriptionInput(**kwargs)

    def __repr__(self) -> str:
        result = "GetKeyDescriptionInput("
        if self.json is not None:
            result += f"json={repr(self.json)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetKeyDescriptionInput):
            return False
        attributes: list[str] = ['json',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class SerializeKeyDescriptionOutput:
    json: bytes | bytearray
    def __init__(
        self,
        *,
        json: bytes | bytearray,
    ):
        self.json = json

    def as_dict(self) -> Dict[str, Any]:
        """Converts the SerializeKeyDescriptionOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "json": self.json,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SerializeKeyDescriptionOutput":
        """Creates a SerializeKeyDescriptionOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "json": d["json"],
        }

        return SerializeKeyDescriptionOutput(**kwargs)

    def __repr__(self) -> str:
        result = "SerializeKeyDescriptionOutput("
        if self.json is not None:
            result += f"json={repr(self.json)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SerializeKeyDescriptionOutput):
            return False
        attributes: list[str] = ['json',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class KeyDescriptionKms():
    def __init__(self, value: 'KMSInfo'):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"Kms": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyDescriptionKms":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KeyDescriptionKms(KMSInfo.from_dict(d["Kms"]))

    def __repr__(self) -> str:
        return f"KeyDescriptionKms(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyDescriptionKms):
            return False
        return self.value == other.value

class KeyDescriptionKmsMrk():
    def __init__(self, value: 'KmsMrkAware'):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"KmsMrk": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyDescriptionKmsMrk":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KeyDescriptionKmsMrk(KmsMrkAware.from_dict(d["KmsMrk"]))

    def __repr__(self) -> str:
        return f"KeyDescriptionKmsMrk(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyDescriptionKmsMrk):
            return False
        return self.value == other.value

class KeyDescriptionKmsMrkDiscovery():
    def __init__(self, value: 'KmsMrkAwareDiscovery'):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"KmsMrkDiscovery": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyDescriptionKmsMrkDiscovery":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KeyDescriptionKmsMrkDiscovery(KmsMrkAwareDiscovery.from_dict(d["KmsMrkDiscovery"]))

    def __repr__(self) -> str:
        return f"KeyDescriptionKmsMrkDiscovery(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyDescriptionKmsMrkDiscovery):
            return False
        return self.value == other.value

class KeyDescriptionRSA():
    def __init__(self, value: 'RawRSA'):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"RSA": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyDescriptionRSA":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KeyDescriptionRSA(RawRSA.from_dict(d["RSA"]))

    def __repr__(self) -> str:
        return f"KeyDescriptionRSA(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyDescriptionRSA):
            return False
        return self.value == other.value

class KeyDescriptionAES():
    def __init__(self, value: 'RawAES'):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"AES": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyDescriptionAES":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KeyDescriptionAES(RawAES.from_dict(d["AES"]))

    def __repr__(self) -> str:
        return f"KeyDescriptionAES(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyDescriptionAES):
            return False
        return self.value == other.value

class KeyDescriptionStatic():
    def __init__(self, value: 'StaticKeyring'):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"Static": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyDescriptionStatic":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KeyDescriptionStatic(StaticKeyring.from_dict(d["Static"]))

    def __repr__(self) -> str:
        return f"KeyDescriptionStatic(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyDescriptionStatic):
            return False
        return self.value == other.value

class KeyDescriptionKmsRsa():
    def __init__(self, value: 'KmsRsaKeyring'):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"KmsRsa": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyDescriptionKmsRsa":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KeyDescriptionKmsRsa(KmsRsaKeyring.from_dict(d["KmsRsa"]))

    def __repr__(self) -> str:
        return f"KeyDescriptionKmsRsa(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyDescriptionKmsRsa):
            return False
        return self.value == other.value

class KeyDescriptionHierarchy():
    def __init__(self, value: 'HierarchyKeyring'):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"Hierarchy": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyDescriptionHierarchy":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KeyDescriptionHierarchy(HierarchyKeyring.from_dict(d["Hierarchy"]))

    def __repr__(self) -> str:
        return f"KeyDescriptionHierarchy(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyDescriptionHierarchy):
            return False
        return self.value == other.value

class KeyDescriptionMulti():
    def __init__(self, value: 'MultiKeyring'):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"Multi": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyDescriptionMulti":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KeyDescriptionMulti(MultiKeyring.from_dict(d["Multi"]))

    def __repr__(self) -> str:
        return f"KeyDescriptionMulti(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyDescriptionMulti):
            return False
        return self.value == other.value

class KeyDescriptionRequiredEncryptionContext():
    def __init__(self, value: 'RequiredEncryptionContextCMM'):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"RequiredEncryptionContext": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyDescriptionRequiredEncryptionContext":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KeyDescriptionRequiredEncryptionContext(RequiredEncryptionContextCMM.from_dict(d["RequiredEncryptionContext"]))

    def __repr__(self) -> str:
        return f"KeyDescriptionRequiredEncryptionContext(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyDescriptionRequiredEncryptionContext):
            return False
        return self.value == other.value

class KeyDescription():
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
    def from_dict(d: Dict[str, Any]) -> "KeyDescription":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return KeyDescription(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"KeyDescription(tag={self.tag})"

KeyDescription = Union[KeyDescriptionKms, KeyDescriptionKmsMrk, KeyDescriptionKmsMrkDiscovery, KeyDescriptionRSA, KeyDescriptionAES, KeyDescriptionStatic, KeyDescriptionKmsRsa, KeyDescriptionHierarchy, KeyDescriptionMulti, KeyDescriptionRequiredEncryptionContext, KeyDescription]
def _key_description_from_dict(d: Dict[str, Any]) -> KeyDescription:
    if "Kms" in d:
        return KeyDescriptionKms.from_dict(d)

    if "KmsMrk" in d:
        return KeyDescriptionKmsMrk.from_dict(d)

    if "KmsMrkDiscovery" in d:
        return KeyDescriptionKmsMrkDiscovery.from_dict(d)

    if "RSA" in d:
        return KeyDescriptionRSA.from_dict(d)

    if "AES" in d:
        return KeyDescriptionAES.from_dict(d)

    if "Static" in d:
        return KeyDescriptionStatic.from_dict(d)

    if "KmsRsa" in d:
        return KeyDescriptionKmsRsa.from_dict(d)

    if "Hierarchy" in d:
        return KeyDescriptionHierarchy.from_dict(d)

    if "Multi" in d:
        return KeyDescriptionMulti.from_dict(d)

    if "RequiredEncryptionContext" in d:
        return KeyDescriptionRequiredEncryptionContext.from_dict(d)

    raise TypeError(f'Unions may have exactly 1 value, but found {len(d)}')

class RequiredEncryptionContextCMM:
    underlying: 'KeyDescription'
    required_encryption_context_keys: list[str]
    def __init__(
        self,
        *,
        underlying: 'KeyDescription',
        required_encryption_context_keys: list[str],
    ):
        self.underlying = underlying
        self.required_encryption_context_keys = required_encryption_context_keys

    def as_dict(self) -> Dict[str, Any]:
        """Converts the RequiredEncryptionContextCMM to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "underlying": self.underlying.as_dict(),
            "requiredEncryptionContextKeys": self.required_encryption_context_keys,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RequiredEncryptionContextCMM":
        """Creates a RequiredEncryptionContextCMM from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "underlying": _key_description_from_dict(d["underlying"]),
            "required_encryption_context_keys": d["requiredEncryptionContextKeys"],
        }

        return RequiredEncryptionContextCMM(**kwargs)

    def __repr__(self) -> str:
        result = "RequiredEncryptionContextCMM("
        if self.underlying is not None:
            result += f"underlying={repr(self.underlying)}, "

        if self.required_encryption_context_keys is not None:
            result += f"required_encryption_context_keys={repr(self.required_encryption_context_keys)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, RequiredEncryptionContextCMM):
            return False
        attributes: list[str] = ['underlying','required_encryption_context_keys',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class GetKeyDescriptionOutput:
    key_description: 'KeyDescription'
    def __init__(
        self,
        *,
        key_description: 'KeyDescription',
    ):
        self.key_description = key_description

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetKeyDescriptionOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyDescription": self.key_description.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetKeyDescriptionOutput":
        """Creates a GetKeyDescriptionOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_description": _key_description_from_dict(d["keyDescription"]),
        }

        return GetKeyDescriptionOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GetKeyDescriptionOutput("
        if self.key_description is not None:
            result += f"key_description={repr(self.key_description)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetKeyDescriptionOutput):
            return False
        attributes: list[str] = ['key_description',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class SerializeKeyDescriptionInput:
    key_description: 'KeyDescription'
    def __init__(
        self,
        *,
        key_description: 'KeyDescription',
    ):
        self.key_description = key_description

    def as_dict(self) -> Dict[str, Any]:
        """Converts the SerializeKeyDescriptionInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyDescription": self.key_description.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SerializeKeyDescriptionInput":
        """Creates a SerializeKeyDescriptionInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_description": _key_description_from_dict(d["keyDescription"]),
        }

        return SerializeKeyDescriptionInput(**kwargs)

    def __repr__(self) -> str:
        result = "SerializeKeyDescriptionInput("
        if self.key_description is not None:
            result += f"key_description={repr(self.key_description)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SerializeKeyDescriptionInput):
            return False
        attributes: list[str] = ['key_description',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class TestVectorCmmInput:
    key_description: 'KeyDescription'
    for_operation: str
    def __init__(
        self,
        *,
        key_description: 'KeyDescription',
        for_operation: str,
    ):
        self.key_description = key_description
        self.for_operation = for_operation

    def as_dict(self) -> Dict[str, Any]:
        """Converts the TestVectorCmmInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyDescription": self.key_description.as_dict(),
            "forOperation": self.for_operation,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "TestVectorCmmInput":
        """Creates a TestVectorCmmInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_description": _key_description_from_dict(d["keyDescription"]),
            "for_operation": d["forOperation"],
        }

        return TestVectorCmmInput(**kwargs)

    def __repr__(self) -> str:
        result = "TestVectorCmmInput("
        if self.key_description is not None:
            result += f"key_description={repr(self.key_description)}, "

        if self.for_operation is not None:
            result += f"for_operation={repr(self.for_operation)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, TestVectorCmmInput):
            return False
        attributes: list[str] = ['key_description','for_operation',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class TestVectorKeyringInput:
    key_description: 'KeyDescription'
    def __init__(
        self,
        *,
        key_description: 'KeyDescription',
    ):
        self.key_description = key_description

    def as_dict(self) -> Dict[str, Any]:
        """Converts the TestVectorKeyringInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyDescription": self.key_description.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "TestVectorKeyringInput":
        """Creates a TestVectorKeyringInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_description": _key_description_from_dict(d["keyDescription"]),
        }

        return TestVectorKeyringInput(**kwargs)

    def __repr__(self) -> str:
        result = "TestVectorKeyringInput("
        if self.key_description is not None:
            result += f"key_description={repr(self.key_description)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, TestVectorKeyringInput):
            return False
        attributes: list[str] = ['key_description',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class MultiKeyring:
    generator: Optional['KeyDescription']
    child_keyrings: 'list[KeyDescription]'
    def __init__(
        self,
        *,
        child_keyrings: 'list[KeyDescription]',
        generator: Optional['KeyDescription'] = None,
    ):
        self.child_keyrings = child_keyrings
        self.generator = generator

    def as_dict(self) -> Dict[str, Any]:
        """Converts the MultiKeyring to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "childKeyrings": _key_description_list_as_dict(self.child_keyrings),
        }

        if self.generator is not None:
            d["generator"] = self.generator.as_dict()

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MultiKeyring":
        """Creates a MultiKeyring from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "child_keyrings": _key_description_list_from_dict(d["childKeyrings"]),
        }

        if "generator" in d:
            kwargs["generator"] = _key_description_from_dict(d["generator"]),

        return MultiKeyring(**kwargs)

    def __repr__(self) -> str:
        result = "MultiKeyring("
        if self.generator is not None:
            result += f"generator={repr(self.generator)}, "

        if self.child_keyrings is not None:
            result += f"child_keyrings={repr(self.child_keyrings)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MultiKeyring):
            return False
        attributes: list[str] = ['generator','child_keyrings',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

def _key_description_list_as_dict(given: list[KeyDescription]) -> List[Any]:
    return [v.as_dict() for v in given]

def _key_description_list_from_dict(given: List[Any]) -> list[KeyDescription]:
    return [KeyDescription.from_dict(v) for v in given]

class Unit:
    pass
