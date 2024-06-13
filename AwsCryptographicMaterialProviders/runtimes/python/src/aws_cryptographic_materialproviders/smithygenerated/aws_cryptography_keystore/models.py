# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from typing import Any, Dict, Optional, Union


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
        """Converts the BeaconKeyMaterials to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {
            "beaconKeyIdentifier": self.beacon_key_identifier,
            "encryptionContext": self.encryption_context,
        }

        if self.beacon_key is not None:
            d["beaconKey"] = self.beacon_key

        if self.hmac_keys is not None:
            d["hmacKeys"] = self.hmac_keys

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "BeaconKeyMaterials":
        """Creates a BeaconKeyMaterials from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "beacon_key_identifier": d["beaconKeyIdentifier"],
            "encryption_context": d["encryptionContext"],
        }

        if "beaconKey" in d:
            kwargs["beacon_key"] = d["beaconKey"]

        if "hmacKeys" in d:
            kwargs["hmac_keys"] = d["hmacKeys"]

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
        attributes: list[str] = ['beacon_key_identifier','encryption_context','beacon_key','hmac_keys',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the BranchKeyMaterials to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "branchKeyIdentifier": self.branch_key_identifier,
            "branchKeyVersion": self.branch_key_version,
            "encryptionContext": self.encryption_context,
            "branchKey": self.branch_key,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "BranchKeyMaterials":
        """Creates a BranchKeyMaterials from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "branch_key_identifier": d["branchKeyIdentifier"],
            "branch_key_version": d["branchKeyVersion"],
            "encryption_context": d["encryptionContext"],
            "branch_key": d["branchKey"],
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
        attributes: list[str] = ['branch_key_identifier','branch_key_version','encryption_context','branch_key',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the CreateKeyInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        d: Dict[str, Any] = {}

        if self.branch_key_identifier is not None:
            d["branchKeyIdentifier"] = self.branch_key_identifier

        if self.encryption_context is not None:
            d["encryptionContext"] = self.encryption_context

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateKeyInput":
        """Creates a CreateKeyInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {}

        if "branchKeyIdentifier" in d:
            kwargs["branch_key_identifier"] = d["branchKeyIdentifier"]

        if "encryptionContext" in d:
            kwargs["encryption_context"] = d["encryptionContext"]

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
        attributes: list[str] = ['branch_key_identifier','encryption_context',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class CreateKeyOutput:
    branch_key_identifier: str
    def __init__(
        self,
        *,
        branch_key_identifier: str,
    ):
        """Outputs for Branch Key creation.

        :param branch_key_identifier: A identifier for the created Branch Key.
        """
        self.branch_key_identifier = branch_key_identifier

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateKeyOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "branchKeyIdentifier": self.branch_key_identifier,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateKeyOutput":
        """Creates a CreateKeyOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "branch_key_identifier": d["branchKeyIdentifier"],
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
        attributes: list[str] = ['branch_key_identifier',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class CreateKeyStoreInput:
    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateKeyStoreInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateKeyStoreInput":
        """Creates a CreateKeyStoreInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
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

        :param table_arn: The ARN of the DynamoDB table that backs this Key Store.
        """
        self.table_arn = table_arn

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateKeyStoreOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "tableArn": self.table_arn,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateKeyStoreOutput":
        """Creates a CreateKeyStoreOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "table_arn": d["tableArn"],
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
        attributes: list[str] = ['table_arn',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class Discovery:
    def as_dict(self) -> Dict[str, Any]:
        """Converts the Discovery to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Discovery":
        """Creates a Discovery from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        return Discovery()

    def __repr__(self) -> str:
        result = "Discovery("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Discovery)

class GetActiveBranchKeyInput:
    branch_key_identifier: str
    def __init__(
        self,
        *,
        branch_key_identifier: str,
    ):
        """Inputs for getting a Branch Key's ACTIVE version.

        :param branch_key_identifier: The identifier for the Branch Key to get the
        ACTIVE version for.
        """
        self.branch_key_identifier = branch_key_identifier

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetActiveBranchKeyInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "branchKeyIdentifier": self.branch_key_identifier,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetActiveBranchKeyInput":
        """Creates a GetActiveBranchKeyInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "branch_key_identifier": d["branchKeyIdentifier"],
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
        attributes: list[str] = ['branch_key_identifier',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the GetActiveBranchKeyOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "branchKeyMaterials": self.branch_key_materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetActiveBranchKeyOutput":
        """Creates a GetActiveBranchKeyOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "branch_key_materials": BranchKeyMaterials.from_dict(d["branchKeyMaterials"]),
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
        attributes: list[str] = ['branch_key_materials',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class GetBeaconKeyInput:
    branch_key_identifier: str
    def __init__(
        self,
        *,
        branch_key_identifier: str,
    ):
        """Inputs for getting a Beacon Key

        :param branch_key_identifier: The identifier of the Branch Key the Beacon Key is
        associated with.
        """
        self.branch_key_identifier = branch_key_identifier

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetBeaconKeyInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "branchKeyIdentifier": self.branch_key_identifier,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetBeaconKeyInput":
        """Creates a GetBeaconKeyInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "branch_key_identifier": d["branchKeyIdentifier"],
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
        attributes: list[str] = ['branch_key_identifier',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class GetBeaconKeyOutput:
    beacon_key_materials: BeaconKeyMaterials
    def __init__(
        self,
        *,
        beacon_key_materials: BeaconKeyMaterials,
    ):
        """Outputs for getting a Beacon Key

        :param beacon_key_materials: The materials for the Beacon Key.
        """
        self.beacon_key_materials = beacon_key_materials

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetBeaconKeyOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "beaconKeyMaterials": self.beacon_key_materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetBeaconKeyOutput":
        """Creates a GetBeaconKeyOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "beacon_key_materials": BeaconKeyMaterials.from_dict(d["beaconKeyMaterials"]),
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
        attributes: list[str] = ['beacon_key_materials',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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

        :param branch_key_identifier: The identifier for the Branch Key to get a
        particular version for.
        :param branch_key_version: The version to get.
        """
        self.branch_key_identifier = branch_key_identifier
        self.branch_key_version = branch_key_version

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetBranchKeyVersionInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "branchKeyIdentifier": self.branch_key_identifier,
            "branchKeyVersion": self.branch_key_version,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetBranchKeyVersionInput":
        """Creates a GetBranchKeyVersionInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "branch_key_identifier": d["branchKeyIdentifier"],
            "branch_key_version": d["branchKeyVersion"],
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
        attributes: list[str] = ['branch_key_identifier','branch_key_version',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the GetBranchKeyVersionOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "branchKeyMaterials": self.branch_key_materials.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetBranchKeyVersionOutput":
        """Creates a GetBranchKeyVersionOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "branch_key_materials": BranchKeyMaterials.from_dict(d["branchKeyMaterials"]),
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
        attributes: list[str] = ['branch_key_materials',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

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
        """Converts the MRDiscovery to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "region": self.region,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MRDiscovery":
        """Creates a MRDiscovery from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
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
        attributes: list[str] = ['region',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class KMSConfigurationKmsKeyArn():
    """Key Store is restricted to only this KMS Key ARN. If a different KMS Key ARN is
    encountered when creating, versioning, or getting a Branch Key or Beacon Key,
    KMS is never called and an exception is thrown. While a Multi-Region Key (MKR)
    may be provided, the whole ARN, including the Region, is persisted in Branch
    Keys and MUST strictly equal this value to be considered valid.
    """
    def __init__(self, value: str):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"kmsKeyArn": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KMSConfigurationKmsKeyArn":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KMSConfigurationKmsKeyArn(d["kmsKeyArn"])

    def __repr__(self) -> str:
        return f"KMSConfigurationKmsKeyArn(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KMSConfigurationKmsKeyArn):
            return False
        return self.value == other.value

class KMSConfigurationKmsMRKeyArn():
    """If an MRK ARN is provided, and the Key Store table holds an MRK ARN, then those
    two ARNs may differ in region, although they must be otherwise equal. If either
    ARN is not an MRK ARN, then mrkKmsKeyArn behaves exactly as kmsKeyArn.
    """
    def __init__(self, value: str):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"kmsMRKeyArn": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KMSConfigurationKmsMRKeyArn":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KMSConfigurationKmsMRKeyArn(d["kmsMRKeyArn"])

    def __repr__(self) -> str:
        return f"KMSConfigurationKmsMRKeyArn(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KMSConfigurationKmsMRKeyArn):
            return False
        return self.value == other.value

class KMSConfigurationDiscovery():
    """The Key Store can use the KMS Key ARNs already persisted in the Backing Table.
    The VersionKey and CreateKey Operations are NOT supported and will fail with a
    runtime exception. There is no Multi-Region logic with this configuration; if a
    Multi-Region Key is encountered, and the region in the ARN is not the region of
    the KMS Client, requests will Fail with KMS Exceptions.
    """
    def __init__(self, value: Discovery):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"discovery": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KMSConfigurationDiscovery":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KMSConfigurationDiscovery(Discovery.from_dict(d["discovery"]))

    def __repr__(self) -> str:
        return f"KMSConfigurationDiscovery(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KMSConfigurationDiscovery):
            return False
        return self.value == other.value

class KMSConfigurationMrDiscovery():
    """The Key Store can use the KMS Key ARNs already persisted in the Backing Table.
    The VersionKey and CreateKey Operations are NOT supported and will fail with a
    runtime exception. If a Multi-Region Key is encountered, the region in the ARN
    is changed to the configured region.
    """
    def __init__(self, value: MRDiscovery):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"mrDiscovery": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KMSConfigurationMrDiscovery":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KMSConfigurationMrDiscovery(MRDiscovery.from_dict(d["mrDiscovery"]))

    def __repr__(self) -> str:
        return f"KMSConfigurationMrDiscovery(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KMSConfigurationMrDiscovery):
            return False
        return self.value == other.value

class KMSConfiguration():
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
    def from_dict(d: Dict[str, Any]) -> "KMSConfiguration":
        if (len(d) != 1):
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return KMSConfiguration(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"KMSConfiguration(tag={self.tag})"

# Configures Key Store's KMS Key ARN restrictions.
KMSConfiguration = Union[KMSConfigurationKmsKeyArn, KMSConfigurationKmsMRKeyArn, KMSConfigurationDiscovery, KMSConfigurationMrDiscovery, KMSConfiguration]
def _kms_configuration_from_dict(d: Dict[str, Any]) -> KMSConfiguration:
    if "kmsKeyArn" in d:
        return KMSConfigurationKmsKeyArn.from_dict(d)

    if "kmsMRKeyArn" in d:
        return KMSConfigurationKmsMRKeyArn.from_dict(d)

    if "discovery" in d:
        return KMSConfigurationDiscovery.from_dict(d)

    if "mrDiscovery" in d:
        return KMSConfigurationMrDiscovery.from_dict(d)

    raise TypeError(f'Unions may have exactly 1 value, but found {len(d)}')

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
        :param key_store_name: The DynamoDB table name that backs this Key Store.
        :param logical_key_store_name: The logical name for this Key Store, which is
        cryptographically bound to the keys it holds.
        :param grant_tokens: The AWS KMS grant tokens that are used when this Key Store
        calls to AWS KMS.
        :param kms_configuration: Configures Key Store's KMS Key ARN restrictions.
        """
        self.key_store_id = key_store_id
        if (key_store_name is not None) and (len(key_store_name) < 3):
            raise ValueError("The size of key_store_name must be greater than or equal to 3")

        if (key_store_name is not None) and (len(key_store_name) > 255):
            raise ValueError("The size of key_store_name must be less than or equal to 255")

        self.key_store_name = key_store_name
        self.logical_key_store_name = logical_key_store_name
        self.grant_tokens = grant_tokens
        self.kms_configuration = kms_configuration

    def as_dict(self) -> Dict[str, Any]:
        """Converts the GetKeyStoreInfoOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "keyStoreId": self.key_store_id,
            "keyStoreName": self.key_store_name,
            "logicalKeyStoreName": self.logical_key_store_name,
            "grantTokens": self.grant_tokens,
            "kmsConfiguration": self.kms_configuration.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GetKeyStoreInfoOutput":
        """Creates a GetKeyStoreInfoOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "key_store_id": d["keyStoreId"],
            "key_store_name": d["keyStoreName"],
            "logical_key_store_name": d["logicalKeyStoreName"],
            "grant_tokens": d["grantTokens"],
            "kms_configuration": _kms_configuration_from_dict(d["kmsConfiguration"]),
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
        attributes: list[str] = ['key_store_id','key_store_name','logical_key_store_name','grant_tokens','kms_configuration',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class VersionKeyInput:
    branch_key_identifier: str
    def __init__(
        self,
        *,
        branch_key_identifier: str,
    ):
        """Inputs for versioning a Branch Key.

        :param branch_key_identifier: The identifier for the Branch Key to be versioned.
        """
        self.branch_key_identifier = branch_key_identifier

    def as_dict(self) -> Dict[str, Any]:
        """Converts the VersionKeyInput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            "branchKeyIdentifier": self.branch_key_identifier,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "VersionKeyInput":
        """Creates a VersionKeyInput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            "branch_key_identifier": d["branchKeyIdentifier"],
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
        attributes: list[str] = ['branch_key_identifier',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class VersionKeyOutput:
    """Outputs for versioning a Branch Key.
    """
    def as_dict(self) -> Dict[str, Any]:
        """Converts the VersionKeyOutput to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "VersionKeyOutput":
        """Creates a VersionKeyOutput from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        return VersionKeyOutput()

    def __repr__(self) -> str:
        result = "VersionKeyOutput("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, VersionKeyOutput)

class Unit:
    pass
