# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from typing import Any, Dict, Optional, Union

from botocore.client import BaseClient


class ActiveHierarchicalSymmetric:
    version: str

    def __init__(
        self,
        *,
        version: str,
    ):
        """Information for the active symmetric branch key.

        :param version: The version of this active key.
        """
        self.version = version

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ActiveHierarchicalSymmetric to a dictionary."""
        return {
            "version": self.version,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ActiveHierarchicalSymmetric":
        """Creates a ActiveHierarchicalSymmetric from a dictionary."""
        kwargs: Dict[str, Any] = {
            "version": d["version"],
        }

        return ActiveHierarchicalSymmetric(**kwargs)

    def __repr__(self) -> str:
        result = "ActiveHierarchicalSymmetric("
        if self.version is not None:
            result += f"version={repr(self.version)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ActiveHierarchicalSymmetric):
            return False
        attributes: list[str] = [
            "version",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class ActiveHierarchicalSymmetricBeacon:
    """Information for a symmetric beacon key.

    At this time there is no additional information.
    """

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ActiveHierarchicalSymmetricBeacon to a dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ActiveHierarchicalSymmetricBeacon":
        """Creates a ActiveHierarchicalSymmetricBeacon from a dictionary."""
        return ActiveHierarchicalSymmetricBeacon()

    def __repr__(self) -> str:
        result = "ActiveHierarchicalSymmetricBeacon("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, ActiveHierarchicalSymmetricBeacon)


class BeaconKeyMaterials:
    beacon_key_identifier: str
    encryption_context: dict[str, str]
    beacon_key: Optional[bytes | bytearray]
    hmac_keys: Optional[dict[str, bytes | bytearray]]

    def __init__(
        self,
        *,
        beacon_key_identifier: str,
        encryption_context: dict[str, str],
        beacon_key: Optional[bytes | bytearray] = None,
        hmac_keys: Optional[dict[str, bytes | bytearray]] = None,
    ):
        self.beacon_key_identifier = beacon_key_identifier
        self.encryption_context = encryption_context
        self.beacon_key = beacon_key
        self.hmac_keys = hmac_keys

    def as_dict(self) -> Dict[str, Any]:
        """Converts the BeaconKeyMaterials to a dictionary."""
        d: Dict[str, Any] = {
            "beacon_key_identifier": self.beacon_key_identifier,
            "encryption_context": self.encryption_context,
        }

        if self.beacon_key is not None:
            d["beacon_key"] = self.beacon_key

        if self.hmac_keys is not None:
            d["hmac_keys"] = self.hmac_keys

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "BeaconKeyMaterials":
        """Creates a BeaconKeyMaterials from a dictionary."""
        kwargs: Dict[str, Any] = {
            "beacon_key_identifier": d["beacon_key_identifier"],
            "encryption_context": d["encryption_context"],
        }

        if "beacon_key" in d:
            kwargs["beacon_key"] = d["beacon_key"]

        if "hmac_keys" in d:
            kwargs["hmac_keys"] = d["hmac_keys"]

        return BeaconKeyMaterials(**kwargs)

    def __repr__(self) -> str:
        result = "BeaconKeyMaterials("
        if self.beacon_key_identifier is not None:
            result += f"beacon_key_identifier={repr(self.beacon_key_identifier)}, "

        if self.encryption_context is not None:
            result += f"encryption_context={repr(self.encryption_context)}, "

        if self.beacon_key is not None:
            result += f"beacon_key={repr(self.beacon_key)}, "

        if self.hmac_keys is not None:
            result += f"hmac_keys={repr(self.hmac_keys)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, BeaconKeyMaterials):
            return False
        attributes: list[str] = [
            "beacon_key_identifier",
            "encryption_context",
            "beacon_key",
            "hmac_keys",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class BranchKeyMaterials:
    branch_key_identifier: str
    branch_key_version: str
    encryption_context: dict[str, str]
    branch_key: bytes | bytearray

    def __init__(
        self,
        *,
        branch_key_identifier: str,
        branch_key_version: str,
        encryption_context: dict[str, str],
        branch_key: bytes | bytearray,
    ):
        self.branch_key_identifier = branch_key_identifier
        self.branch_key_version = branch_key_version
        self.encryption_context = encryption_context
        self.branch_key = branch_key

    def as_dict(self) -> Dict[str, Any]:
        """Converts the BranchKeyMaterials to a dictionary."""
        return {
            "branch_key_identifier": self.branch_key_identifier,
            "branch_key_version": self.branch_key_version,
            "encryption_context": self.encryption_context,
            "branch_key": self.branch_key,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "BranchKeyMaterials":
        """Creates a BranchKeyMaterials from a dictionary."""
        kwargs: Dict[str, Any] = {
            "branch_key_identifier": d["branch_key_identifier"],
            "branch_key_version": d["branch_key_version"],
            "encryption_context": d["encryption_context"],
            "branch_key": d["branch_key"],
        }

        return BranchKeyMaterials(**kwargs)

    def __repr__(self) -> str:
        result = "BranchKeyMaterials("
        if self.branch_key_identifier is not None:
            result += f"branch_key_identifier={repr(self.branch_key_identifier)}, "

        if self.branch_key_version is not None:
            result += f"branch_key_version={repr(self.branch_key_version)}, "

        if self.encryption_context is not None:
            result += f"encryption_context={repr(self.encryption_context)}, "

        if self.branch_key is not None:
            result += f"branch_key={repr(self.branch_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, BranchKeyMaterials):
            return False
        attributes: list[str] = [
            "branch_key_identifier",
            "branch_key_version",
            "encryption_context",
            "branch_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateKeyInput:
    branch_key_identifier: Optional[str]
    encryption_context: Optional[dict[str, str]]

    def __init__(
        self,
        *,
        branch_key_identifier: Optional[str] = None,
        encryption_context: Optional[dict[str, str]] = None,
    ):
        """
        :param branch_key_identifier: The identifier for the created Branch Key.
        :param encryption_context: Custom encryption context for the Branch Key.
        Required if branchKeyIdentifier is set.
        """
        self.branch_key_identifier = branch_key_identifier
        self.encryption_context = encryption_context

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateKeyInput to a dictionary."""
        d: Dict[str, Any] = {}

        if self.branch_key_identifier is not None:
            d["branch_key_identifier"] = self.branch_key_identifier

        if self.encryption_context is not None:
            d["encryption_context"] = self.encryption_context

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateKeyInput":
        """Creates a CreateKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {}

        if "branch_key_identifier" in d:
            kwargs["branch_key_identifier"] = d["branch_key_identifier"]

        if "encryption_context" in d:
            kwargs["encryption_context"] = d["encryption_context"]

        return CreateKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateKeyInput("
        if self.branch_key_identifier is not None:
            result += f"branch_key_identifier={repr(self.branch_key_identifier)}, "

        if self.encryption_context is not None:
            result += f"encryption_context={repr(self.encryption_context)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateKeyInput):
            return False
        attributes: list[str] = [
            "branch_key_identifier",
            "encryption_context",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateKeyOutput:
    branch_key_identifier: str

    def __init__(
        self,
        *,
        branch_key_identifier: str,
    ):
        """Outputs for Branch Key creation.

        :param branch_key_identifier: A identifier for the created
            Branch Key.
        """
        self.branch_key_identifier = branch_key_identifier

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateKeyOutput to a dictionary."""
        return {
            "branch_key_identifier": self.branch_key_identifier,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateKeyOutput":
        """Creates a CreateKeyOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "branch_key_identifier": d["branch_key_identifier"],
        }

        return CreateKeyOutput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateKeyOutput("
        if self.branch_key_identifier is not None:
            result += f"branch_key_identifier={repr(self.branch_key_identifier)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateKeyOutput):
            return False
        attributes: list[str] = [
            "branch_key_identifier",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateKeyStoreInput:
    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateKeyStoreInput to a dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateKeyStoreInput":
        """Creates a CreateKeyStoreInput from a dictionary."""
        return CreateKeyStoreInput()

    def __repr__(self) -> str:
        result = "CreateKeyStoreInput("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, CreateKeyStoreInput)


class CreateKeyStoreOutput:
    table_arn: str

    def __init__(
        self,
        *,
        table_arn: str,
    ):
        """Outputs for Key Store DynamoDB table creation.

        :param table_arn: The ARN of the DynamoDB table that backs this
            Key Store.
        """
        if (table_arn is not None) and (len(table_arn) < 1):
            raise ValueError("The size of table_arn must be greater than or equal to 1")

        if (table_arn is not None) and (len(table_arn) > 1024):
            raise ValueError("The size of table_arn must be less than or equal to 1024")

        self.table_arn = table_arn

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateKeyStoreOutput to a dictionary."""
        return {
            "table_arn": self.table_arn,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateKeyStoreOutput":
        """Creates a CreateKeyStoreOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "table_arn": d["table_arn"],
        }

        return CreateKeyStoreOutput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateKeyStoreOutput("
        if self.table_arn is not None:
            result += f"table_arn={repr(self.table_arn)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateKeyStoreOutput):
            return False
        attributes: list[str] = [
            "table_arn",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class Discovery:
    def as_dict(self) -> Dict[str, Any]:
        """Converts the Discovery to a dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Discovery":
        """Creates a Discovery from a dictionary."""
        return Discovery()

    def __repr__(self) -> str:
        result = "Discovery("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Discovery)


class HierarchicalSymmetric:
    version: str

    def __init__(
        self,
        *,
        version: str,
    ):
        """Information for a specific decrypt only branch key version.

        :param version: The version of this key.
        """
        self.version = version

    def as_dict(self) -> Dict[str, Any]:
        """Converts the HierarchicalSymmetric to a dictionary."""
        return {
            "version": self.version,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "HierarchicalSymmetric":
        """Creates a HierarchicalSymmetric from a dictionary."""
        kwargs: Dict[str, Any] = {
            "version": d["version"],
        }

        return HierarchicalSymmetric(**kwargs)

    def __repr__(self) -> str:
        result = "HierarchicalSymmetric("
        if self.version is not None:
            result += f"version={repr(self.version)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, HierarchicalSymmetric):
            return False
        attributes: list[str] = [
            "version",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class HierarchicalKeyTypeActiveHierarchicalSymmetricVersion:
    """The version the active branch key.

    This version is used to encrypt messages.
    """

    def __init__(self, value: ActiveHierarchicalSymmetric):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"ActiveHierarchicalSymmetricVersion": self.value.as_dict()}

    @staticmethod
    def from_dict(
        d: Dict[str, Any],
    ) -> "HierarchicalKeyTypeActiveHierarchicalSymmetricVersion":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return HierarchicalKeyTypeActiveHierarchicalSymmetricVersion(
            ActiveHierarchicalSymmetric.from_dict(
                d["ActiveHierarchicalSymmetricVersion"]
            )
        )

    def __repr__(self) -> str:
        return f"HierarchicalKeyTypeActiveHierarchicalSymmetricVersion(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, HierarchicalKeyTypeActiveHierarchicalSymmetricVersion):
            return False
        return self.value == other.value


class HierarchicalKeyTypeHierarchicalSymmetricVersion:
    """The version for a decrypt only branch key type.

    These are used to decrypt messages. For every ACTIVE that has ever
    been, there exists a Version.
    """

    def __init__(self, value: HierarchicalSymmetric):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"HierarchicalSymmetricVersion": self.value.as_dict()}

    @staticmethod
    def from_dict(
        d: Dict[str, Any],
    ) -> "HierarchicalKeyTypeHierarchicalSymmetricVersion":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return HierarchicalKeyTypeHierarchicalSymmetricVersion(
            HierarchicalSymmetric.from_dict(d["HierarchicalSymmetricVersion"])
        )

    def __repr__(self) -> str:
        return (
            f"HierarchicalKeyTypeHierarchicalSymmetricVersion(value=repr(self.value))"
        )

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, HierarchicalKeyTypeHierarchicalSymmetricVersion):
            return False
        return self.value == other.value


class HierarchicalKeyTypeActiveHierarchicalSymmetricBeacon:
    """The information regarding a symmetric beacon key."""

    def __init__(self, value: ActiveHierarchicalSymmetricBeacon):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"ActiveHierarchicalSymmetricBeacon": self.value.as_dict()}

    @staticmethod
    def from_dict(
        d: Dict[str, Any],
    ) -> "HierarchicalKeyTypeActiveHierarchicalSymmetricBeacon":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return HierarchicalKeyTypeActiveHierarchicalSymmetricBeacon(
            ActiveHierarchicalSymmetricBeacon.from_dict(
                d["ActiveHierarchicalSymmetricBeacon"]
            )
        )

    def __repr__(self) -> str:
        return f"HierarchicalKeyTypeActiveHierarchicalSymmetricBeacon(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, HierarchicalKeyTypeActiveHierarchicalSymmetricBeacon):
            return False
        return self.value == other.value


class HierarchicalKeyTypeUnknown:
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
    def from_dict(d: Dict[str, Any]) -> "HierarchicalKeyTypeUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return HierarchicalKeyTypeUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"HierarchicalKeyTypeUnknown(tag={self.tag})"


# Describes the key that an encrypted blob represents.
HierarchicalKeyType = Union[
    HierarchicalKeyTypeActiveHierarchicalSymmetricVersion,
    HierarchicalKeyTypeHierarchicalSymmetricVersion,
    HierarchicalKeyTypeActiveHierarchicalSymmetricBeacon,
    HierarchicalKeyTypeUnknown,
]


def _hierarchical_key_type_from_dict(d: Dict[str, Any]) -> HierarchicalKeyType:
    if "ActiveHierarchicalSymmetricVersion" in d:
        return HierarchicalKeyTypeActiveHierarchicalSymmetricVersion.from_dict(d)

    if "HierarchicalSymmetricVersion" in d:
        return HierarchicalKeyTypeHierarchicalSymmetricVersion.from_dict(d)

    if "ActiveHierarchicalSymmetricBeacon" in d:
        return HierarchicalKeyTypeActiveHierarchicalSymmetricBeacon.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class EncryptedHierarchicalKey:
    identifier: str
    type: HierarchicalKeyType
    create_time: str
    kms_arn: str
    encryption_context: dict[str, str]
    ciphertext_blob: bytes | bytearray

    def __init__(
        self,
        *,
        identifier: str,
        type: HierarchicalKeyType,
        create_time: str,
        kms_arn: str,
        encryption_context: dict[str, str],
        ciphertext_blob: bytes | bytearray,
    ):
        """Information about an encrypted hierarchical key. This abstracts the
        structure of this information from the underlying storage.

        :param identifier: The identifier for this encrypted key.
        :param type: The type of encrypted key.
        :param create_time: The create time as an ISO 8061 UTC string.
        :param kms_arn: The KMS ARN which protects this encrypted key.
        :param encryption_context: The encryption context needed to
            decrypt this encrypted key. This includes the user the
            provided custom encryption context, as well as the other
            Branch Key attributes.
        :param ciphertext_blob: The ciphertext for this encrypted key.
        """
        self.identifier = identifier
        self.type = type
        self.create_time = create_time
        self.kms_arn = kms_arn
        self.encryption_context = encryption_context
        self.ciphertext_blob = ciphertext_blob

    def as_dict(self) -> Dict[str, Any]:
        """Converts the EncryptedHierarchicalKey to a dictionary."""
        return {
            "identifier": self.identifier,
            "type": self.type.as_dict(),
            "create_time": self.create_time,
            "kms_arn": self.kms_arn,
            "encryption_context": self.encryption_context,
            "ciphertext_blob": self.ciphertext_blob,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EncryptedHierarchicalKey":
        """Creates a EncryptedHierarchicalKey from a dictionary."""
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
            "type": _hierarchical_key_type_from_dict(d["type"]),
            "create_time": d["create_time"],
            "kms_arn": d["kms_arn"],
            "encryption_context": d["encryption_context"],
            "ciphertext_blob": d["ciphertext_blob"],
        }

        return EncryptedHierarchicalKey(**kwargs)

    def __repr__(self) -> str:
        result = "EncryptedHierarchicalKey("
        if self.identifier is not None:
            result += f"identifier={repr(self.identifier)}, "

        if self.type is not None:
            result += f"type={repr(self.type)}, "

        if self.create_time is not None:
            result += f"create_time={repr(self.create_time)}, "

        if self.kms_arn is not None:
            result += f"kms_arn={repr(self.kms_arn)}, "

        if self.encryption_context is not None:
            result += f"encryption_context={repr(self.encryption_context)}, "

        if self.ciphertext_blob is not None:
            result += f"ciphertext_blob={repr(self.ciphertext_blob)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EncryptedHierarchicalKey):
            return False
        attributes: list[str] = [
            "identifier",
            "type",
            "create_time",
            "kms_arn",
            "encryption_context",
            "ciphertext_blob",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetActiveBranchKeyInput:
    branch_key_identifier: str

    def __init__(
        self,
        *,
        branch_key_identifier: str,
    ):
        """Inputs for getting a Branch Key's ACTIVE version.

        :param branch_key_identifier: The identifier for the Branch Key
            to get the ACTIVE version for.
        """
        self.branch_key_identifier = branch_key_identifier

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetActiveBranchKeyInput to a dictionary."""
        return {
            "branch_key_identifier": self.branch_key_identifier,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetActiveBranchKeyInput":
        """Creates a GetActiveBranchKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "branch_key_identifier": d["branch_key_identifier"],
        }

        return GetActiveBranchKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "GetActiveBranchKeyInput("
        if self.branch_key_identifier is not None:
            result += f"branch_key_identifier={repr(self.branch_key_identifier)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetActiveBranchKeyInput):
            return False
        attributes: list[str] = [
            "branch_key_identifier",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetActiveBranchKeyOutput:
    branch_key_materials: BranchKeyMaterials

    def __init__(
        self,
        *,
        branch_key_materials: BranchKeyMaterials,
    ):
        """Outputs for getting a Branch Key's ACTIVE version.

        :param branch_key_materials: The materials for the Branch Key.
        """
        self.branch_key_materials = branch_key_materials

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetActiveBranchKeyOutput to a dictionary."""
        return {
            "branch_key_materials": self.branch_key_materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetActiveBranchKeyOutput":
        """Creates a GetActiveBranchKeyOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "branch_key_materials": BranchKeyMaterials.from_dict(
                d["branch_key_materials"]
            ),
        }

        return GetActiveBranchKeyOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GetActiveBranchKeyOutput("
        if self.branch_key_materials is not None:
            result += f"branch_key_materials={repr(self.branch_key_materials)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetActiveBranchKeyOutput):
            return False
        attributes: list[str] = [
            "branch_key_materials",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetBeaconKeyInput:
    branch_key_identifier: str

    def __init__(
        self,
        *,
        branch_key_identifier: str,
    ):
        """Inputs for getting a Beacon Key.

        :param branch_key_identifier: The identifier of the Branch Key
            the Beacon Key is associated with.
        """
        self.branch_key_identifier = branch_key_identifier

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetBeaconKeyInput to a dictionary."""
        return {
            "branch_key_identifier": self.branch_key_identifier,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetBeaconKeyInput":
        """Creates a GetBeaconKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "branch_key_identifier": d["branch_key_identifier"],
        }

        return GetBeaconKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "GetBeaconKeyInput("
        if self.branch_key_identifier is not None:
            result += f"branch_key_identifier={repr(self.branch_key_identifier)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetBeaconKeyInput):
            return False
        attributes: list[str] = [
            "branch_key_identifier",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetBeaconKeyOutput:
    beacon_key_materials: BeaconKeyMaterials

    def __init__(
        self,
        *,
        beacon_key_materials: BeaconKeyMaterials,
    ):
        """Outputs for getting a Beacon Key.

        :param beacon_key_materials: The materials for the Beacon Key.
        """
        self.beacon_key_materials = beacon_key_materials

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetBeaconKeyOutput to a dictionary."""
        return {
            "beacon_key_materials": self.beacon_key_materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetBeaconKeyOutput":
        """Creates a GetBeaconKeyOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "beacon_key_materials": BeaconKeyMaterials.from_dict(
                d["beacon_key_materials"]
            ),
        }

        return GetBeaconKeyOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GetBeaconKeyOutput("
        if self.beacon_key_materials is not None:
            result += f"beacon_key_materials={repr(self.beacon_key_materials)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetBeaconKeyOutput):
            return False
        attributes: list[str] = [
            "beacon_key_materials",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetBranchKeyVersionInput:
    branch_key_identifier: str
    branch_key_version: str

    def __init__(
        self,
        *,
        branch_key_identifier: str,
        branch_key_version: str,
    ):
        """Inputs for getting a version of a Branch Key.

        :param branch_key_identifier: The identifier for the Branch Key
            to get a particular version for.
        :param branch_key_version: The version to get.
        """
        self.branch_key_identifier = branch_key_identifier
        self.branch_key_version = branch_key_version

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetBranchKeyVersionInput to a dictionary."""
        return {
            "branch_key_identifier": self.branch_key_identifier,
            "branch_key_version": self.branch_key_version,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetBranchKeyVersionInput":
        """Creates a GetBranchKeyVersionInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "branch_key_identifier": d["branch_key_identifier"],
            "branch_key_version": d["branch_key_version"],
        }

        return GetBranchKeyVersionInput(**kwargs)

    def __repr__(self) -> str:
        result = "GetBranchKeyVersionInput("
        if self.branch_key_identifier is not None:
            result += f"branch_key_identifier={repr(self.branch_key_identifier)}, "

        if self.branch_key_version is not None:
            result += f"branch_key_version={repr(self.branch_key_version)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetBranchKeyVersionInput):
            return False
        attributes: list[str] = [
            "branch_key_identifier",
            "branch_key_version",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetBranchKeyVersionOutput:
    branch_key_materials: BranchKeyMaterials

    def __init__(
        self,
        *,
        branch_key_materials: BranchKeyMaterials,
    ):
        """Outputs for getting a version of a Branch Key.

        :param branch_key_materials: The materials for the Branch Key.
        """
        self.branch_key_materials = branch_key_materials

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetBranchKeyVersionOutput to a dictionary."""
        return {
            "branch_key_materials": self.branch_key_materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetBranchKeyVersionOutput":
        """Creates a GetBranchKeyVersionOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "branch_key_materials": BranchKeyMaterials.from_dict(
                d["branch_key_materials"]
            ),
        }

        return GetBranchKeyVersionOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GetBranchKeyVersionOutput("
        if self.branch_key_materials is not None:
            result += f"branch_key_materials={repr(self.branch_key_materials)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetBranchKeyVersionOutput):
            return False
        attributes: list[str] = [
            "branch_key_materials",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetEncryptedActiveBranchKeyInput:
    identifier: str

    def __init__(
        self,
        *,
        identifier: str,
    ):
        """Get the ACTIVE version for a particular Branch Key.

        :param identifier: The identifier for the Branch Key to get the
            ACTIVE version for.
        """
        self.identifier = identifier

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetEncryptedActiveBranchKeyInput to a dictionary."""
        return {
            "identifier": self.identifier,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetEncryptedActiveBranchKeyInput":
        """Creates a GetEncryptedActiveBranchKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
        }

        return GetEncryptedActiveBranchKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "GetEncryptedActiveBranchKeyInput("
        if self.identifier is not None:
            result += f"identifier={repr(self.identifier)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetEncryptedActiveBranchKeyInput):
            return False
        attributes: list[str] = [
            "identifier",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetEncryptedActiveBranchKeyOutput:
    item: EncryptedHierarchicalKey

    def __init__(
        self,
        *,
        item: EncryptedHierarchicalKey,
    ):
        """Outputs for getting a Branch Key's ACTIVE version.

        :param item: The encrypted materials for the ACTIVE Branch Key.
        """
        self.item = item

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetEncryptedActiveBranchKeyOutput to a dictionary."""
        return {
            "item": self.item.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetEncryptedActiveBranchKeyOutput":
        """Creates a GetEncryptedActiveBranchKeyOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "item": EncryptedHierarchicalKey.from_dict(d["item"]),
        }

        return GetEncryptedActiveBranchKeyOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GetEncryptedActiveBranchKeyOutput("
        if self.item is not None:
            result += f"item={repr(self.item)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetEncryptedActiveBranchKeyOutput):
            return False
        attributes: list[str] = [
            "item",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetEncryptedBeaconKeyInput:
    identifier: str

    def __init__(
        self,
        *,
        identifier: str,
    ):
        """Inputs for getting a Beacon Key.

        :param identifier: The identifier of the Branch Key the Beacon
            Key is associated with.
        """
        self.identifier = identifier

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetEncryptedBeaconKeyInput to a dictionary."""
        return {
            "identifier": self.identifier,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetEncryptedBeaconKeyInput":
        """Creates a GetEncryptedBeaconKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
        }

        return GetEncryptedBeaconKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "GetEncryptedBeaconKeyInput("
        if self.identifier is not None:
            result += f"identifier={repr(self.identifier)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetEncryptedBeaconKeyInput):
            return False
        attributes: list[str] = [
            "identifier",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetEncryptedBeaconKeyOutput:
    item: EncryptedHierarchicalKey

    def __init__(
        self,
        *,
        item: EncryptedHierarchicalKey,
    ):
        """Outputs for getting a Beacon Key.

        :param item: The materials for the Beacon Key.
        """
        self.item = item

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetEncryptedBeaconKeyOutput to a dictionary."""
        return {
            "item": self.item.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetEncryptedBeaconKeyOutput":
        """Creates a GetEncryptedBeaconKeyOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "item": EncryptedHierarchicalKey.from_dict(d["item"]),
        }

        return GetEncryptedBeaconKeyOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GetEncryptedBeaconKeyOutput("
        if self.item is not None:
            result += f"item={repr(self.item)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetEncryptedBeaconKeyOutput):
            return False
        attributes: list[str] = [
            "item",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetEncryptedBranchKeyVersionInput:
    identifier: str
    version: str

    def __init__(
        self,
        *,
        identifier: str,
        version: str,
    ):
        """Inputs for getting a version of a Branch Key.

        :param identifier: The identifier for the Branch Key to get a
            particular version for.
        :param version: The version to get.
        """
        self.identifier = identifier
        self.version = version

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetEncryptedBranchKeyVersionInput to a dictionary."""
        return {
            "identifier": self.identifier,
            "version": self.version,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetEncryptedBranchKeyVersionInput":
        """Creates a GetEncryptedBranchKeyVersionInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
            "version": d["version"],
        }

        return GetEncryptedBranchKeyVersionInput(**kwargs)

    def __repr__(self) -> str:
        result = "GetEncryptedBranchKeyVersionInput("
        if self.identifier is not None:
            result += f"identifier={repr(self.identifier)}, "

        if self.version is not None:
            result += f"version={repr(self.version)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetEncryptedBranchKeyVersionInput):
            return False
        attributes: list[str] = [
            "identifier",
            "version",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetEncryptedBranchKeyVersionOutput:
    item: EncryptedHierarchicalKey

    def __init__(
        self,
        *,
        item: EncryptedHierarchicalKey,
    ):
        """Outputs for getting a version of a Branch Key.

        :param item: The materials for the Branch Key.
        """
        self.item = item

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetEncryptedBranchKeyVersionOutput to a dictionary."""
        return {
            "item": self.item.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetEncryptedBranchKeyVersionOutput":
        """Creates a GetEncryptedBranchKeyVersionOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "item": EncryptedHierarchicalKey.from_dict(d["item"]),
        }

        return GetEncryptedBranchKeyVersionOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GetEncryptedBranchKeyVersionOutput("
        if self.item is not None:
            result += f"item={repr(self.item)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetEncryptedBranchKeyVersionOutput):
            return False
        attributes: list[str] = [
            "item",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class GetKeyStorageInfoInput:
    """Input for getting information about the underlying storage."""

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetKeyStorageInfoInput to a dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetKeyStorageInfoInput":
        """Creates a GetKeyStorageInfoInput from a dictionary."""
        return GetKeyStorageInfoInput()

    def __repr__(self) -> str:
        result = "GetKeyStorageInfoInput("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, GetKeyStorageInfoInput)


class GetKeyStorageInfoOutput:
    name: str
    logical_name: str

    def __init__(
        self,
        *,
        name: str,
        logical_name: str,
    ):
        """Output containing information about the underlying storage.

        :param name: The name of the physical resource used for storage.
        :param logical_name: The Logical Key Store Name associated with
            this Storage.
        """
        self.name = name
        self.logical_name = logical_name

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetKeyStorageInfoOutput to a dictionary."""
        return {
            "name": self.name,
            "logical_name": self.logical_name,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetKeyStorageInfoOutput":
        """Creates a GetKeyStorageInfoOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "name": d["name"],
            "logical_name": d["logical_name"],
        }

        return GetKeyStorageInfoOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GetKeyStorageInfoOutput("
        if self.name is not None:
            result += f"name={repr(self.name)}, "

        if self.logical_name is not None:
            result += f"logical_name={repr(self.logical_name)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetKeyStorageInfoOutput):
            return False
        attributes: list[str] = [
            "name",
            "logical_name",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class MRDiscovery:
    region: str

    def __init__(
        self,
        *,
        region: str,
    ):
        """
        :param region: Any MRK ARN discovered will have its region replaced with this.
        """
        if (region is not None) and (len(region) < 1):
            raise ValueError("The size of region must be greater than or equal to 1")

        if (region is not None) and (len(region) > 32):
            raise ValueError("The size of region must be less than or equal to 32")

        self.region = region

    def as_dict(self) -> Dict[str, Any]:
        """Converts the MRDiscovery to a dictionary."""
        return {
            "region": self.region,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MRDiscovery":
        """Creates a MRDiscovery from a dictionary."""
        kwargs: Dict[str, Any] = {
            "region": d["region"],
        }

        return MRDiscovery(**kwargs)

    def __repr__(self) -> str:
        result = "MRDiscovery("
        if self.region is not None:
            result += f"region={repr(self.region)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MRDiscovery):
            return False
        attributes: list[str] = [
            "region",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class KMSConfigurationKmsKeyArn:
    """Key Store is restricted to only this KMS Key ARN.

    If a different KMS Key ARN is encountered when creating, versioning,
    or getting a Branch Key or Beacon Key, KMS is never called and an
    exception is thrown. While a Multi-Region Key (MKR) may be provided,
    the whole ARN, including the Region, is persisted in Branch Keys and
    MUST strictly equal this value to be considered valid.
    """

    def __init__(self, value: str):
        if (value is not None) and (len(value) < 1):
            raise ValueError("The size of value must be greater than or equal to 1")

        if (value is not None) and (len(value) > 2048):
            raise ValueError("The size of value must be less than or equal to 2048")

        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"kmsKeyArn": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KMSConfigurationKmsKeyArn":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KMSConfigurationKmsKeyArn(d["kmsKeyArn"])

    def __repr__(self) -> str:
        return f"KMSConfigurationKmsKeyArn(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KMSConfigurationKmsKeyArn):
            return False
        return self.value == other.value


class KMSConfigurationKmsMRKeyArn:
    """If an MRK ARN is provided, and the Key Store table holds an MRK ARN,
    then those two ARNs may differ in region, although they must be otherwise
    equal.

    If either ARN is not an MRK ARN, then mrkKmsKeyArn behaves exactly
    as kmsKeyArn.
    """

    def __init__(self, value: str):
        if (value is not None) and (len(value) < 1):
            raise ValueError("The size of value must be greater than or equal to 1")

        if (value is not None) and (len(value) > 2048):
            raise ValueError("The size of value must be less than or equal to 2048")

        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"kmsMRKeyArn": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KMSConfigurationKmsMRKeyArn":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KMSConfigurationKmsMRKeyArn(d["kmsMRKeyArn"])

    def __repr__(self) -> str:
        return f"KMSConfigurationKmsMRKeyArn(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KMSConfigurationKmsMRKeyArn):
            return False
        return self.value == other.value


class KMSConfigurationDiscovery:
    """The Key Store can use the KMS Key ARNs already persisted in the Backing
    Table.

    The VersionKey and CreateKey Operations are NOT supported and will
    fail with a runtime exception. There is no Multi-Region logic with
    this configuration; if a Multi-Region Key is encountered, and the
    region in the ARN is not the region of the KMS Client, requests will
    Fail with KMS Exceptions.
    """

    def __init__(self, value: Discovery):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"discovery": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KMSConfigurationDiscovery":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KMSConfigurationDiscovery(Discovery.from_dict(d["discovery"]))

    def __repr__(self) -> str:
        return f"KMSConfigurationDiscovery(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KMSConfigurationDiscovery):
            return False
        return self.value == other.value


class KMSConfigurationMrDiscovery:
    """The Key Store can use the KMS Key ARNs already persisted in the Backing
    Table.

    The VersionKey and CreateKey Operations are NOT supported and will
    fail with a runtime exception. If a Multi-Region Key is encountered,
    the region in the ARN is changed to the configured region.
    """

    def __init__(self, value: MRDiscovery):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"mrDiscovery": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KMSConfigurationMrDiscovery":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KMSConfigurationMrDiscovery(MRDiscovery.from_dict(d["mrDiscovery"]))

    def __repr__(self) -> str:
        return f"KMSConfigurationMrDiscovery(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KMSConfigurationMrDiscovery):
            return False
        return self.value == other.value


class KMSConfigurationUnknown:
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
    def from_dict(d: Dict[str, Any]) -> "KMSConfigurationUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return KMSConfigurationUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"KMSConfigurationUnknown(tag={self.tag})"


# Configures Key Store's KMS Key ARN restrictions.
KMSConfiguration = Union[
    KMSConfigurationKmsKeyArn,
    KMSConfigurationKmsMRKeyArn,
    KMSConfigurationDiscovery,
    KMSConfigurationMrDiscovery,
    KMSConfigurationUnknown,
]


def _kms_configuration_from_dict(d: Dict[str, Any]) -> KMSConfiguration:
    if "kmsKeyArn" in d:
        return KMSConfigurationKmsKeyArn.from_dict(d)

    if "kmsMRKeyArn" in d:
        return KMSConfigurationKmsMRKeyArn.from_dict(d)

    if "discovery" in d:
        return KMSConfigurationDiscovery.from_dict(d)

    if "mrDiscovery" in d:
        return KMSConfigurationMrDiscovery.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class GetKeyStoreInfoOutput:
    key_store_id: str
    key_store_name: str
    logical_key_store_name: str
    grant_tokens: list[str]
    kms_configuration: KMSConfiguration

    def __init__(
        self,
        *,
        key_store_id: str,
        key_store_name: str,
        logical_key_store_name: str,
        grant_tokens: list[str],
        kms_configuration: KMSConfiguration,
    ):
        """The configuration information for a Key Store.

        :param key_store_id: An identifier for this Key Store.
        :param key_store_name: The physical name of the backing storage
            for this Key Store instance.
        :param logical_key_store_name: The logical name for this Key
            Store, which is cryptographically bound to the keys it
            holds.
        :param grant_tokens: The AWS KMS grant tokens that are used when
            this Key Store calls to AWS KMS.
        :param kms_configuration: Configures Key Store's KMS Key ARN
            restrictions.
        """
        self.key_store_id = key_store_id
        self.key_store_name = key_store_name
        self.logical_key_store_name = logical_key_store_name
        self.grant_tokens = grant_tokens
        self.kms_configuration = kms_configuration

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetKeyStoreInfoOutput to a dictionary."""
        return {
            "key_store_id": self.key_store_id,
            "key_store_name": self.key_store_name,
            "logical_key_store_name": self.logical_key_store_name,
            "grant_tokens": self.grant_tokens,
            "kms_configuration": self.kms_configuration.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetKeyStoreInfoOutput":
        """Creates a GetKeyStoreInfoOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "key_store_id": d["key_store_id"],
            "key_store_name": d["key_store_name"],
            "logical_key_store_name": d["logical_key_store_name"],
            "grant_tokens": d["grant_tokens"],
            "kms_configuration": _kms_configuration_from_dict(d["kms_configuration"]),
        }

        return GetKeyStoreInfoOutput(**kwargs)

    def __repr__(self) -> str:
        result = "GetKeyStoreInfoOutput("
        if self.key_store_id is not None:
            result += f"key_store_id={repr(self.key_store_id)}, "

        if self.key_store_name is not None:
            result += f"key_store_name={repr(self.key_store_name)}, "

        if self.logical_key_store_name is not None:
            result += f"logical_key_store_name={repr(self.logical_key_store_name)}, "

        if self.grant_tokens is not None:
            result += f"grant_tokens={repr(self.grant_tokens)}, "

        if self.kms_configuration is not None:
            result += f"kms_configuration={repr(self.kms_configuration)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, GetKeyStoreInfoOutput):
            return False
        attributes: list[str] = [
            "key_store_id",
            "key_store_name",
            "logical_key_store_name",
            "grant_tokens",
            "kms_configuration",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class WriteNewEncryptedBranchKeyInput:
    active: EncryptedHierarchicalKey
    version: EncryptedHierarchicalKey
    beacon: EncryptedHierarchicalKey

    def __init__(
        self,
        *,
        active: EncryptedHierarchicalKey,
        version: EncryptedHierarchicalKey,
        beacon: EncryptedHierarchicalKey,
    ):
        """The information required to atomically write an a new branch key
        into a key store. The identifiers for all keys passed should be the
        same.

        :param active: The active representation of this branch key. The
            plain-text cryptographic material of the Active must be the
            same as the Version.
        :param version: The decrypt representation of this branch key.
            The plain-text cryptographic material of the Version must be
            the same as the Active.
        :param beacon: An HMAC key used to support searchable
            encryption. This should be a different cryptographic
            material from the other two.
        """
        self.active = active
        self.version = version
        self.beacon = beacon

    def as_dict(self) -> Dict[str, Any]:
        """Converts the WriteNewEncryptedBranchKeyInput to a dictionary."""
        return {
            "active": self.active.as_dict(),
            "version": self.version.as_dict(),
            "beacon": self.beacon.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "WriteNewEncryptedBranchKeyInput":
        """Creates a WriteNewEncryptedBranchKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "active": EncryptedHierarchicalKey.from_dict(d["active"]),
            "version": EncryptedHierarchicalKey.from_dict(d["version"]),
            "beacon": EncryptedHierarchicalKey.from_dict(d["beacon"]),
        }

        return WriteNewEncryptedBranchKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "WriteNewEncryptedBranchKeyInput("
        if self.active is not None:
            result += f"active={repr(self.active)}, "

        if self.version is not None:
            result += f"version={repr(self.version)}, "

        if self.beacon is not None:
            result += f"beacon={repr(self.beacon)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, WriteNewEncryptedBranchKeyInput):
            return False
        attributes: list[str] = [
            "active",
            "version",
            "beacon",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class WriteNewEncryptedBranchKeyOutput:
    """The output of writing a new branch key.

    There is currently no additional information returned.
    """

    def as_dict(self) -> Dict[str, Any]:
        """Converts the WriteNewEncryptedBranchKeyOutput to a dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "WriteNewEncryptedBranchKeyOutput":
        """Creates a WriteNewEncryptedBranchKeyOutput from a dictionary."""
        return WriteNewEncryptedBranchKeyOutput()

    def __repr__(self) -> str:
        result = "WriteNewEncryptedBranchKeyOutput("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, WriteNewEncryptedBranchKeyOutput)


class WriteNewEncryptedBranchKeyVersionInput:
    active: EncryptedHierarchicalKey
    version: EncryptedHierarchicalKey
    old_active: EncryptedHierarchicalKey

    def __init__(
        self,
        *,
        active: EncryptedHierarchicalKey,
        version: EncryptedHierarchicalKey,
        old_active: EncryptedHierarchicalKey,
    ):
        """The information required to atomically write a new version for an
        existing branch key into a key store. The identifiers for all keys
        passed should be the same.

        :param active:
          The new active version to be written to the key store.
          The
        plain-text cryptographic material of the Active must be the same as the
        Version.

        :param version:
          The decrypt representation of this branch key version.
          The
        plain-text cryptographic material of the `Version` must be the same as the
        `Active`.

        :param old_active:
          The previous active version.
          This key should be used as
        an optimistic lock on the new version.
          This means that when updating the
        current active record
          the existing active record should be equal to this
        value.
        """
        self.active = active
        self.version = version
        self.old_active = old_active

    def as_dict(self) -> Dict[str, Any]:
        """Converts the WriteNewEncryptedBranchKeyVersionInput to a
        dictionary."""
        return {
            "active": self.active.as_dict(),
            "version": self.version.as_dict(),
            "old_active": self.old_active.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "WriteNewEncryptedBranchKeyVersionInput":
        """Creates a WriteNewEncryptedBranchKeyVersionInput from a
        dictionary."""
        kwargs: Dict[str, Any] = {
            "active": EncryptedHierarchicalKey.from_dict(d["active"]),
            "version": EncryptedHierarchicalKey.from_dict(d["version"]),
            "old_active": EncryptedHierarchicalKey.from_dict(d["old_active"]),
        }

        return WriteNewEncryptedBranchKeyVersionInput(**kwargs)

    def __repr__(self) -> str:
        result = "WriteNewEncryptedBranchKeyVersionInput("
        if self.active is not None:
            result += f"active={repr(self.active)}, "

        if self.version is not None:
            result += f"version={repr(self.version)}, "

        if self.old_active is not None:
            result += f"old_active={repr(self.old_active)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, WriteNewEncryptedBranchKeyVersionInput):
            return False
        attributes: list[str] = [
            "active",
            "version",
            "old_active",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class WriteNewEncryptedBranchKeyVersionOutput:
    """The output of writing a new version for an existing branch key.

    There is currently no additional information returned.
    """

    def as_dict(self) -> Dict[str, Any]:
        """Converts the WriteNewEncryptedBranchKeyVersionOutput to a
        dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "WriteNewEncryptedBranchKeyVersionOutput":
        """Creates a WriteNewEncryptedBranchKeyVersionOutput from a
        dictionary."""
        return WriteNewEncryptedBranchKeyVersionOutput()

    def __repr__(self) -> str:
        result = "WriteNewEncryptedBranchKeyVersionOutput("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, WriteNewEncryptedBranchKeyVersionOutput)


class VersionKeyInput:
    branch_key_identifier: str

    def __init__(
        self,
        *,
        branch_key_identifier: str,
    ):
        """Inputs for versioning a Branch Key.

        :param branch_key_identifier: The identifier for the Branch Key
            to be versioned.
        """
        self.branch_key_identifier = branch_key_identifier

    def as_dict(self) -> Dict[str, Any]:
        """Converts the VersionKeyInput to a dictionary."""
        return {
            "branch_key_identifier": self.branch_key_identifier,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "VersionKeyInput":
        """Creates a VersionKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "branch_key_identifier": d["branch_key_identifier"],
        }

        return VersionKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "VersionKeyInput("
        if self.branch_key_identifier is not None:
            result += f"branch_key_identifier={repr(self.branch_key_identifier)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, VersionKeyInput):
            return False
        attributes: list[str] = [
            "branch_key_identifier",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class VersionKeyOutput:
    """Outputs for versioning a Branch Key."""

    def as_dict(self) -> Dict[str, Any]:
        """Converts the VersionKeyOutput to a dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "VersionKeyOutput":
        """Creates a VersionKeyOutput from a dictionary."""
        return VersionKeyOutput()

    def __repr__(self) -> str:
        result = "VersionKeyOutput("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, VersionKeyOutput)


class AwsKms:
    grant_tokens: Optional[list[str]]
    kms_client: Optional[BaseClient]

    def __init__(
        self,
        *,
        grant_tokens: Optional[list[str]] = None,
        kms_client: Optional[BaseClient] = None,
    ):
        """
        :param grant_tokens: The AWS KMS grant tokens that are used when this Key Store
        calls to AWS KMS.
        :param kms_client: The KMS client this Key Store uses to call AWS KMS.  If None
        is provided and the KMS ARN is, the KMS ARN is used to determine the Region of
        the default client.
        """
        self.grant_tokens = grant_tokens
        self.kms_client = kms_client

    def as_dict(self) -> Dict[str, Any]:
        """Converts the AwsKms to a dictionary."""
        d: Dict[str, Any] = {}

        if self.grant_tokens is not None:
            d["grant_tokens"] = self.grant_tokens

        if self.kms_client is not None:
            d["kms_client"] = self.kms_client

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AwsKms":
        """Creates a AwsKms from a dictionary."""
        kwargs: Dict[str, Any] = {}

        if "grant_tokens" in d:
            kwargs["grant_tokens"] = d["grant_tokens"]

        if "kms_client" in d:
            kwargs["kms_client"] = d["kms_client"]

        return AwsKms(**kwargs)

    def __repr__(self) -> str:
        result = "AwsKms("
        if self.grant_tokens is not None:
            result += f"grant_tokens={repr(self.grant_tokens)}, "

        if self.kms_client is not None:
            result += f"kms_client={repr(self.kms_client)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AwsKms):
            return False
        attributes: list[str] = [
            "grant_tokens",
            "kms_client",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class DynamoDBTable:
    ddb_table_name: str
    ddb_client: Optional[BaseClient]

    def __init__(
        self,
        *,
        ddb_table_name: str,
        ddb_client: Optional[BaseClient] = None,
    ):
        """
        :param ddb_table_name: The DynamoDB table name that backs this Key Store.
        :param ddb_client: The DynamoDB client this Key Store uses to call Amazon
        DynamoDB. If None is provided and the KMS ARN is, the KMS ARN is used to
        determine the Region of the default client.
        """
        if (ddb_table_name is not None) and (len(ddb_table_name) < 3):
            raise ValueError(
                "The size of ddb_table_name must be greater than or equal to 3"
            )

        if (ddb_table_name is not None) and (len(ddb_table_name) > 255):
            raise ValueError(
                "The size of ddb_table_name must be less than or equal to 255"
            )

        self.ddb_table_name = ddb_table_name
        self.ddb_client = ddb_client

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DynamoDBTable to a dictionary."""
        d: Dict[str, Any] = {
            "ddb_table_name": self.ddb_table_name,
        }

        if self.ddb_client is not None:
            d["ddb_client"] = self.ddb_client

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DynamoDBTable":
        """Creates a DynamoDBTable from a dictionary."""
        kwargs: Dict[str, Any] = {
            "ddb_table_name": d["ddb_table_name"],
        }

        if "ddb_client" in d:
            kwargs["ddb_client"] = d["ddb_client"]

        return DynamoDBTable(**kwargs)

    def __repr__(self) -> str:
        result = "DynamoDBTable("
        if self.ddb_table_name is not None:
            result += f"ddb_table_name={repr(self.ddb_table_name)}, "

        if self.ddb_client is not None:
            result += f"ddb_client={repr(self.ddb_client)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DynamoDBTable):
            return False
        attributes: list[str] = [
            "ddb_table_name",
            "ddb_client",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class KeyManagementKms:
    """The AWS KMS configuration this Key Store with use to authenticate branch
    keys."""

    def __init__(self, value: AwsKms):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"kms": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyManagementKms":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KeyManagementKms(AwsKms.from_dict(d["kms"]))

    def __repr__(self) -> str:
        return f"KeyManagementKms(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyManagementKms):
            return False
        return self.value == other.value


class KeyManagementUnknown:
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
    def from_dict(d: Dict[str, Any]) -> "KeyManagementUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return KeyManagementUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"KeyManagementUnknown(tag={self.tag})"


KeyManagement = Union[KeyManagementKms, KeyManagementUnknown]


def _key_management_from_dict(d: Dict[str, Any]) -> KeyManagement:
    if "kms" in d:
        return KeyManagementKms.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class StorageDdb:
    """The DynamoDB configuration that backs this Key Store."""

    def __init__(self, value: DynamoDBTable):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"ddb": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "StorageDdb":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return StorageDdb(DynamoDBTable.from_dict(d["ddb"]))

    def __repr__(self) -> str:
        return f"StorageDdb(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, StorageDdb):
            return False
        return self.value == other.value


class StorageCustom:
    """The custom storage configuration that backs this Key Store."""

    def __init__(
        self,
        value: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.references.KeyStorageInterface",
    ):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"custom": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "StorageCustom":
        from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.references import (
            KeyStorageInterface,
        )

        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return StorageCustom(KeyStorageInterface.from_dict(d["custom"]))

    def __repr__(self) -> str:
        return f"StorageCustom(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, StorageCustom):
            return False
        return self.value == other.value


class StorageUnknown:
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
    def from_dict(d: Dict[str, Any]) -> "StorageUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return StorageUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"StorageUnknown(tag={self.tag})"


Storage = Union[StorageDdb, StorageCustom, StorageUnknown]


def _storage_from_dict(d: Dict[str, Any]) -> Storage:
    if "ddb" in d:
        return StorageDdb.from_dict(d)

    if "custom" in d:
        return StorageCustom.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class Unit:
    pass
