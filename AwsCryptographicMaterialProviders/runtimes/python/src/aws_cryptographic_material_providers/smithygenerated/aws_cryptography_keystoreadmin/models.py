# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from typing import Any, Dict, List, Optional, Union

from ..aws_cryptography_keystore.models import AwsKms


class MutationToken:
    identifier: str
    uuid: str
    create_time: str

    def __init__(
        self,
        *,
        identifier: str,
        uuid: str,
        create_time: str,
    ):
        """
        :param identifier: The identifier for the Branch Key being mutated.
        :param uuid: UUID of the Mutation.
        :param create_time: ISO 8601 time when the mutation was initialized.
        """
        self.identifier = identifier
        self.uuid = uuid
        self.create_time = create_time

    def as_dict(self) -> Dict[str, Any]:
        """Converts the MutationToken to a dictionary."""
        return {
            "identifier": self.identifier,
            "uuid": self.uuid,
            "create_time": self.create_time,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MutationToken":
        """Creates a MutationToken from a dictionary."""
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
            "uuid": d["uuid"],
            "create_time": d["create_time"],
        }

        return MutationToken(**kwargs)

    def __repr__(self) -> str:
        result = "MutationToken("
        if self.identifier is not None:
            result += f"identifier={repr(self.identifier)}, "

        if self.uuid is not None:
            result += f"uuid={repr(self.uuid)}, "

        if self.create_time is not None:
            result += f"create_time={repr(self.create_time)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MutationToken):
            return False
        attributes: list[str] = [
            "identifier",
            "uuid",
            "create_time",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class AwsKmsDecryptEncrypt:
    decrypt: Optional[AwsKms]
    encrypt: Optional[AwsKms]

    def __init__(
        self,
        *,
        decrypt: Optional[AwsKms] = None,
        encrypt: Optional[AwsKms] = None,
    ):
        """Key Store Items are authenticated and re-wrapped via a Decrypt and
        then Encrypt request. This is two separate requests to Key Management,
        as compared to one. This is primarily intended for Branch Key Mutations
        that need to use separate credentials to change the KMS Key that
        protects a Branch Key.

        Branch Key Items in the original state will be Decrypted by the
        Decrypt KMS Client, and then Encrypted to the terminal state via
        the Encrypt KMS Client.

        Generation of a new Branch Key Version is done via
        GenerateDataKeyWithoutPlaintext, and then Decrypt and Encrypt
        requests against the Encrypt Client.

        :param decrypt: The KMS Client (and Grant Tokens) used to
            Decrypt Branch Key Store Items.
        :param encrypt: The KMS Client (and Grant Tokens) used to
            Encrypt Branch Key Store Items and to Generate new
            Cryptographic Material.
        """
        self.decrypt = decrypt
        self.encrypt = encrypt

    def as_dict(self) -> Dict[str, Any]:
        """Converts the AwsKmsDecryptEncrypt to a dictionary."""
        d: Dict[str, Any] = {}

        if self.decrypt is not None:
            d["decrypt"] = self.decrypt.as_dict()

        if self.encrypt is not None:
            d["encrypt"] = self.encrypt.as_dict()

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AwsKmsDecryptEncrypt":
        """Creates a AwsKmsDecryptEncrypt from a dictionary."""
        kwargs: Dict[str, Any] = {}

        if "decrypt" in d:
            kwargs["decrypt"] = AwsKms.from_dict(d["decrypt"])

        if "encrypt" in d:
            kwargs["encrypt"] = AwsKms.from_dict(d["encrypt"])

        return AwsKmsDecryptEncrypt(**kwargs)

    def __repr__(self) -> str:
        result = "AwsKmsDecryptEncrypt("
        if self.decrypt is not None:
            result += f"decrypt={repr(self.decrypt)}, "

        if self.encrypt is not None:
            result += f"encrypt={repr(self.encrypt)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AwsKmsDecryptEncrypt):
            return False
        attributes: list[str] = [
            "decrypt",
            "encrypt",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class KeyManagementStrategyAwsKmsReEncrypt:
    """Branch Key Store Items are authenticated and re-wrapped via KMS
    ReEncrypt,

    executed with the provided Grant Tokens and KMS Client.
      This is one request to
    Key Management, as compared to two.
      But only one set of credentials can be
    used.
      At this time, this strategy can only be used with hierarchy-version-1
    (HV-1) branch keys for:
      - Creating new HV-1 branch keys
      - Versioning
    existing HV-1 branch keys
    """

    def __init__(self, value: AwsKms):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"AwsKmsReEncrypt": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyManagementStrategyAwsKmsReEncrypt":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KeyManagementStrategyAwsKmsReEncrypt(
            AwsKms.from_dict(d["AwsKmsReEncrypt"])
        )

    def __repr__(self) -> str:
        return f"KeyManagementStrategyAwsKmsReEncrypt(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyManagementStrategyAwsKmsReEncrypt):
            return False
        return self.value == other.value


class KeyManagementStrategyAwsKmsDecryptEncrypt:
    """Key Store Items are authenticated and re-wrapped via a Decrypt and then
    Encrypt request. This is two separate requests to Key Management, as
    compared to one. This is primarily intended for Branch Key Mutations that
    need to use separate credentials to change the KMS Key that protects a
    Branch Key.

    Branch Key Items in the original state will be Decrypted by the
    Decrypt KMS Client, and then Encrypted to the terminal state via the
    Encrypt KMS Client.

    Generation of a new Branch Key Version is done via
    GenerateDataKeyWithoutPlaintext, and then Decrypt and Encrypt
    requests against the Encrypt Client.
    """

    def __init__(self, value: AwsKmsDecryptEncrypt):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"AwsKmsDecryptEncrypt": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyManagementStrategyAwsKmsDecryptEncrypt":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KeyManagementStrategyAwsKmsDecryptEncrypt(
            AwsKmsDecryptEncrypt.from_dict(d["AwsKmsDecryptEncrypt"])
        )

    def __repr__(self) -> str:
        return f"KeyManagementStrategyAwsKmsDecryptEncrypt(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyManagementStrategyAwsKmsDecryptEncrypt):
            return False
        return self.value == other.value


class KeyManagementStrategyAwsKmsSimple:
    """This is the simple option, that uses one KMS Client (and Grant Token
    list) and supports both hierarchy-versions.

    For HV-1, kms:GenerateDataKeyWithoutPlaintext followed by
    kms:ReEncrypt is used to create branch keys.   For HV-2,
    kms:GenerateDataKey followed by kms:Encrypt is used to create branch
    keys.   For HV-1, to validate a branch key item, kms:ReEncrypt is
    used.   For HV-2, to validate a branch key item, kms:Decrypt un-
    wraps the branch key context and data key tuple,   and the client
    verifies the read branch key context against the protected branch
    key context.
    """

    def __init__(self, value: AwsKms):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"AwsKmsSimple": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyManagementStrategyAwsKmsSimple":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KeyManagementStrategyAwsKmsSimple(AwsKms.from_dict(d["AwsKmsSimple"]))

    def __repr__(self) -> str:
        return f"KeyManagementStrategyAwsKmsSimple(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyManagementStrategyAwsKmsSimple):
            return False
        return self.value == other.value


class KeyManagementStrategyUnknown:
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
    def from_dict(d: Dict[str, Any]) -> "KeyManagementStrategyUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return KeyManagementStrategyUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"KeyManagementStrategyUnknown(tag={self.tag})"


# This configures which Key Management Operations will be used    AND the Key
# Management Clients (and Grant Tokens) used to invoke those Operations.
KeyManagementStrategy = Union[
    KeyManagementStrategyAwsKmsReEncrypt,
    KeyManagementStrategyAwsKmsDecryptEncrypt,
    KeyManagementStrategyAwsKmsSimple,
    KeyManagementStrategyUnknown,
]


def _key_management_strategy_from_dict(d: Dict[str, Any]) -> KeyManagementStrategy:
    if "AwsKmsReEncrypt" in d:
        return KeyManagementStrategyAwsKmsReEncrypt.from_dict(d)

    if "AwsKmsDecryptEncrypt" in d:
        return KeyManagementStrategyAwsKmsDecryptEncrypt.from_dict(d)

    if "AwsKmsSimple" in d:
        return KeyManagementStrategyAwsKmsSimple.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class KmsSymmetricEncryption:
    kms_arn: str
    aws_kms: AwsKms

    def __init__(
        self,
        *,
        kms_arn: str,
        aws_kms: AwsKms,
    ):
        """Items of a non-cryptographic material nature are protected by KMS.

        This is done by including all attributes of an item as
        Encryption Context in a KMS Encrypt or Decrypt call, effectively
        signing the attributes. As a best practice, this KMS Key should
        be distinct from those used to protect Branch Keys.
        """
        if (kms_arn is not None) and (len(kms_arn) < 1):
            raise ValueError("The size of kms_arn must be greater than or equal to 1")

        if (kms_arn is not None) and (len(kms_arn) > 2048):
            raise ValueError("The size of kms_arn must be less than or equal to 2048")

        self.kms_arn = kms_arn
        self.aws_kms = aws_kms

    def as_dict(self) -> Dict[str, Any]:
        """Converts the KmsSymmetricEncryption to a dictionary."""
        return {
            "kms_arn": self.kms_arn,
            "aws_kms": self.aws_kms.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KmsSymmetricEncryption":
        """Creates a KmsSymmetricEncryption from a dictionary."""
        kwargs: Dict[str, Any] = {
            "kms_arn": d["kms_arn"],
            "aws_kms": AwsKms.from_dict(d["aws_kms"]),
        }

        return KmsSymmetricEncryption(**kwargs)

    def __repr__(self) -> str:
        result = "KmsSymmetricEncryption("
        if self.kms_arn is not None:
            result += f"kms_arn={repr(self.kms_arn)}, "

        if self.aws_kms is not None:
            result += f"aws_kms={repr(self.aws_kms)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KmsSymmetricEncryption):
            return False
        attributes: list[str] = [
            "kms_arn",
            "aws_kms",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class TrustStorage:
    """The Storage is trusted enough for items of non-cryptographic material
    nature, even if those items can affect the cryptographic materials.

    Thus, permissions to modify the Key Store's storage is sufficient to
    influence the properties of mutations in flight without needing a
    KMS key permission, which would otherwise be needed to do the same.
    As an extreme example, an actor with only write access to the
    storage could modify an in-flight Mutation's terminal KMS Key ARN.
    Thus, AWS Crypto Tools recommends using 'KMS Symmetric Encryption'
    instead of 'Trust Storage' to ensure that Branch Keys are only
    modified via actors with KMS key permissions.
    """

    def as_dict(self) -> Dict[str, Any]:
        """Converts the TrustStorage to a dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "TrustStorage":
        """Creates a TrustStorage from a dictionary."""
        return TrustStorage()

    def __repr__(self) -> str:
        result = "TrustStorage("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, TrustStorage)


class SystemKeyKmsSymmetricEncryption:
    """Items of a non-cryptographic material nature are protected by KMS.

    This is done by including all attributes of an item as Encryption
    Context in a KMS Encrypt or Decrypt call, effectively signing the
    attributes. As a best practice, this KMS Key should be distinct from
    those used to protect Branch Keys.
    """

    def __init__(self, value: KmsSymmetricEncryption):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"kmsSymmetricEncryption": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SystemKeyKmsSymmetricEncryption":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return SystemKeyKmsSymmetricEncryption(
            KmsSymmetricEncryption.from_dict(d["kmsSymmetricEncryption"])
        )

    def __repr__(self) -> str:
        return f"SystemKeyKmsSymmetricEncryption(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SystemKeyKmsSymmetricEncryption):
            return False
        return self.value == other.value


class SystemKeyTrustStorage:
    """The Storage is trusted enough for items of non-cryptographic material
    nature, even if those items can affect the cryptographic materials.

    Thus, permissions to modify the Key Store's storage is sufficient to
    influence the properties of mutations in flight without needing a
    KMS key permission, which would otherwise be needed to do the same.
    As an extreme example, an actor with only write access to the
    storage could modify an in-flight Mutation's terminal KMS Key ARN.
    Thus, AWS Crypto Tools recommends using 'KMS Symmetric Encryption'
    instead of 'Trust Storage' to ensure that Branch Keys are only
    modified via actors with KMS key permissions.
    """

    def __init__(self, value: TrustStorage):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"trustStorage": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "SystemKeyTrustStorage":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return SystemKeyTrustStorage(TrustStorage.from_dict(d["trustStorage"]))

    def __repr__(self) -> str:
        return f"SystemKeyTrustStorage(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SystemKeyTrustStorage):
            return False
        return self.value == other.value


class SystemKeyUnknown:
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
    def from_dict(d: Dict[str, Any]) -> "SystemKeyUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return SystemKeyUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"SystemKeyUnknown(tag={self.tag})"


# Key Store Admin protects any non-cryptographic items stored with this Key. Using
# 'KMS Symmetric Encryption' is a best practice, as it prevents actors with only
# write access to the Key Store's storage from tampering with Mutations. For a
# Mutation, the System Key setting MUST be consistent across the Initialize
# Mutation and all the Apply Mutation calls.
SystemKey = Union[
    SystemKeyKmsSymmetricEncryption, SystemKeyTrustStorage, SystemKeyUnknown
]


def _system_key_from_dict(d: Dict[str, Any]) -> SystemKey:
    if "kmsSymmetricEncryption" in d:
        return SystemKeyKmsSymmetricEncryption.from_dict(d)

    if "trustStorage" in d:
        return SystemKeyTrustStorage.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class ApplyMutationInput:
    mutation_token: MutationToken
    page_size: Optional[int]
    strategy: Optional[KeyManagementStrategy]
    system_key: SystemKey

    def __init__(
        self,
        *,
        mutation_token: MutationToken,
        system_key: SystemKey,
        page_size: Optional[int] = None,
        strategy: Optional[KeyManagementStrategy] = None,
    ):
        """
        :param system_key: Key Store Admin protects any non-cryptographic
        items stored
        with this Key.
        Using 'KMS Symmetric Encryption' is a best practice,
        as it
        prevents actors with only write access to the Key Store's storage
        from tampering
        with Mutations.
        For a Mutation, the System Key setting MUST be consistent across
        the Initialize Mutation and all the Apply Mutation calls.
        :param page_size: Optional. Defaults to 3 if not set.
          For Default DynamoDB
        Table Storage, the maximum page size is 98.
          At most, Apply Mutation will
        mutate pageSize Items.
          Note that, at least for Storage:DynamoDBTable,
          two
        additional "item" are consumed by the Mutation Commitment and Mutation Index
        verification.
          Thus, if the pageSize is 24, 26 requests will be sent in the
        Transact Write Request.
        :param strategy: Optional. Defaults to reEncrypt with a default KMS Client.

        However, if the Branch Key's 'hierarchy-version' is HV-2,
          or the Branch Key is
        being mutated to HV-2,
          the Strategy MUST be AwsKmsDecryptEncrypt or
        AwsKmsSimple.
        """
        self.mutation_token = mutation_token
        self.system_key = system_key
        self.page_size = page_size
        self.strategy = strategy

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ApplyMutationInput to a dictionary."""
        d: Dict[str, Any] = {
            "mutation_token": self.mutation_token.as_dict(),
            "system_key": self.system_key.as_dict(),
        }

        if self.page_size is not None:
            d["page_size"] = self.page_size

        if self.strategy is not None:
            d["strategy"] = self.strategy.as_dict()

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ApplyMutationInput":
        """Creates a ApplyMutationInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "mutation_token": MutationToken.from_dict(d["mutation_token"]),
            "system_key": _system_key_from_dict(d["system_key"]),
        }

        if "page_size" in d:
            kwargs["page_size"] = d["page_size"]

        if "strategy" in d:
            kwargs["strategy"] = (_key_management_strategy_from_dict(d["strategy"]),)

        return ApplyMutationInput(**kwargs)

    def __repr__(self) -> str:
        result = "ApplyMutationInput("
        if self.mutation_token is not None:
            result += f"mutation_token={repr(self.mutation_token)}, "

        if self.page_size is not None:
            result += f"page_size={repr(self.page_size)}, "

        if self.strategy is not None:
            result += f"strategy={repr(self.strategy)}, "

        if self.system_key is not None:
            result += f"system_key={repr(self.system_key)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ApplyMutationInput):
            return False
        attributes: list[str] = [
            "mutation_token",
            "page_size",
            "strategy",
            "system_key",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class MutatedBranchKeyItem:
    item_type: str
    description: str

    def __init__(
        self,
        *,
        item_type: str,
        description: str,
    ):
        """
        :param item_type: The item type changed. i.e: branch:version:<uuid> or
        branch:MUTATION_COMMITMENT.
        :param description: Brief description of what occurred. i.e: Mutation Applied,
        New Active Created, Mutation Commitment Created, Mutation Commitment Removed.
        """
        self.item_type = item_type
        self.description = description

    def as_dict(self) -> Dict[str, Any]:
        """Converts the MutatedBranchKeyItem to a dictionary."""
        return {
            "item_type": self.item_type,
            "description": self.description,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MutatedBranchKeyItem":
        """Creates a MutatedBranchKeyItem from a dictionary."""
        kwargs: Dict[str, Any] = {
            "item_type": d["item_type"],
            "description": d["description"],
        }

        return MutatedBranchKeyItem(**kwargs)

    def __repr__(self) -> str:
        result = "MutatedBranchKeyItem("
        if self.item_type is not None:
            result += f"item_type={repr(self.item_type)}, "

        if self.description is not None:
            result += f"description={repr(self.description)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MutatedBranchKeyItem):
            return False
        attributes: list[str] = [
            "item_type",
            "description",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class MutationComplete:
    def as_dict(self) -> Dict[str, Any]:
        """Converts the MutationComplete to a dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MutationComplete":
        """Creates a MutationComplete from a dictionary."""
        return MutationComplete()

    def __repr__(self) -> str:
        result = "MutationComplete("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, MutationComplete)


class ApplyMutationResultContinueMutation:
    """Continue applying the mutation.

    Invoke Apply Mutation with this Mutation Token.
    """

    def __init__(self, value: MutationToken):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"ContinueMutation": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ApplyMutationResultContinueMutation":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return ApplyMutationResultContinueMutation(
            MutationToken.from_dict(d["ContinueMutation"])
        )

    def __repr__(self) -> str:
        return f"ApplyMutationResultContinueMutation(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ApplyMutationResultContinueMutation):
            return False
        return self.value == other.value


class ApplyMutationResultCompleteMutation:
    """All items have been mutated.

    The mutation is complete.
    """

    def __init__(self, value: MutationComplete):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"CompleteMutation": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ApplyMutationResultCompleteMutation":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return ApplyMutationResultCompleteMutation(
            MutationComplete.from_dict(d["CompleteMutation"])
        )

    def __repr__(self) -> str:
        return f"ApplyMutationResultCompleteMutation(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ApplyMutationResultCompleteMutation):
            return False
        return self.value == other.value


class ApplyMutationResultUnknown:
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
    def from_dict(d: Dict[str, Any]) -> "ApplyMutationResultUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return ApplyMutationResultUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"ApplyMutationResultUnknown(tag={self.tag})"


ApplyMutationResult = Union[
    ApplyMutationResultContinueMutation,
    ApplyMutationResultCompleteMutation,
    ApplyMutationResultUnknown,
]


def _apply_mutation_result_from_dict(d: Dict[str, Any]) -> ApplyMutationResult:
    if "ContinueMutation" in d:
        return ApplyMutationResultContinueMutation.from_dict(d)

    if "CompleteMutation" in d:
        return ApplyMutationResultCompleteMutation.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class ApplyMutationOutput:
    mutation_result: ApplyMutationResult
    mutated_branch_key_items: list[MutatedBranchKeyItem]

    def __init__(
        self,
        *,
        mutation_result: ApplyMutationResult,
        mutated_branch_key_items: list[MutatedBranchKeyItem],
    ):
        """
        :param mutated_branch_key_items: Details what items of the Branch Key ID were
        changed on this invocation.
        """
        self.mutation_result = mutation_result
        self.mutated_branch_key_items = mutated_branch_key_items

    def as_dict(self) -> Dict[str, Any]:
        """Converts the ApplyMutationOutput to a dictionary."""
        return {
            "mutation_result": self.mutation_result.as_dict(),
            "mutated_branch_key_items": _mutated_branch_key_items_as_dict(
                self.mutated_branch_key_items
            ),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ApplyMutationOutput":
        """Creates a ApplyMutationOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "mutation_result": _apply_mutation_result_from_dict(d["mutation_result"]),
            "mutated_branch_key_items": _mutated_branch_key_items_from_dict(
                d["mutated_branch_key_items"]
            ),
        }

        return ApplyMutationOutput(**kwargs)

    def __repr__(self) -> str:
        result = "ApplyMutationOutput("
        if self.mutation_result is not None:
            result += f"mutation_result={repr(self.mutation_result)}, "

        if self.mutated_branch_key_items is not None:
            result += f"mutated_branch_key_items={repr(self.mutated_branch_key_items)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ApplyMutationOutput):
            return False
        attributes: list[str] = [
            "mutation_result",
            "mutated_branch_key_items",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class KmsSymmetricKeyArnKmsKeyArn:
    """Key Store is restricted to only this KMS Key ARN.

    If a different KMS Key ARN is encountered   when creating,
    versioning, or getting a Branch Key or Beacon Key,   KMS is never
    called and an exception is thrown.   While a Multi-Region Key (MKR)
    may be provided,   the whole ARN, including the Region,   is
    persisted in Branch Keys and   MUST strictly equal this value to be
    considered valid.
    """

    def __init__(self, value: str):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"KmsKeyArn": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KmsSymmetricKeyArnKmsKeyArn":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return KmsSymmetricKeyArnKmsKeyArn(d["KmsKeyArn"])

    def __repr__(self) -> str:
        return f"KmsSymmetricKeyArnKmsKeyArn(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KmsSymmetricKeyArnKmsKeyArn):
            return False
        return self.value == other.value


class KmsSymmetricKeyArnUnknown:
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
    def from_dict(d: Dict[str, Any]) -> "KmsSymmetricKeyArnUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return KmsSymmetricKeyArnUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"KmsSymmetricKeyArnUnknown(tag={self.tag})"


KmsSymmetricKeyArn = Union[KmsSymmetricKeyArnKmsKeyArn, KmsSymmetricKeyArnUnknown]


def _kms_symmetric_key_arn_from_dict(d: Dict[str, Any]) -> KmsSymmetricKeyArn:
    if "KmsKeyArn" in d:
        return KmsSymmetricKeyArnKmsKeyArn.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class CreateKeyInput:
    identifier: Optional[str]
    encryption_context: Optional[dict[str, str]]
    kms_arn: KmsSymmetricKeyArn
    strategy: Optional[KeyManagementStrategy]
    hierarchy_version: Optional[str]

    def __init__(
        self,
        *,
        kms_arn: KmsSymmetricKeyArn,
        identifier: Optional[str] = None,
        encryption_context: Optional[dict[str, str]] = None,
        strategy: Optional[KeyManagementStrategy] = None,
        hierarchy_version: Optional[str] = None,
    ):
        """
        :param kms_arn: Multi-Region or Single Region AWS KMS Key
          used to protect the
        Branch Key, but not aliases!
        :param identifier: The identifier for the created Branch Key.
        :param encryption_context: Encryption context for the Branch Key.
          Required if
        branchKeyIdentifier is set.
        :param strategy: For 'hierarchy-version-1' (HV-1), only AwsKmsReEncrypt or
        AwsKmsSimple are supported.
          For 'hierarchy-version-2' (HV-2), only
        AwsKmsSimple is supported.
        :param hierarchy_version: The hierarchy-version of a Branch Key;
          all items of
        the same Branch Key SHOULD
          have the same hierarchy-version.
          The
        hierarchy-version determines how the Branch Key Store
          protects and validates
        the branch key context (BKC).
        """
        self.kms_arn = kms_arn
        self.identifier = identifier
        self.encryption_context = encryption_context
        self.strategy = strategy
        self.hierarchy_version = hierarchy_version

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateKeyInput to a dictionary."""
        d: Dict[str, Any] = {
            "kms_arn": self.kms_arn.as_dict(),
        }

        if self.identifier is not None:
            d["identifier"] = self.identifier

        if self.encryption_context is not None:
            d["encryption_context"] = self.encryption_context

        if self.strategy is not None:
            d["strategy"] = self.strategy.as_dict()

        if self.hierarchy_version is not None:
            d["hierarchy_version"] = self.hierarchy_version

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateKeyInput":
        """Creates a CreateKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "kms_arn": _kms_symmetric_key_arn_from_dict(d["kms_arn"]),
        }

        if "identifier" in d:
            kwargs["identifier"] = d["identifier"]

        if "encryption_context" in d:
            kwargs["encryption_context"] = d["encryption_context"]

        if "strategy" in d:
            kwargs["strategy"] = (_key_management_strategy_from_dict(d["strategy"]),)

        if "hierarchy_version" in d:
            kwargs["hierarchy_version"] = d["hierarchy_version"]

        return CreateKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateKeyInput("
        if self.identifier is not None:
            result += f"identifier={repr(self.identifier)}, "

        if self.encryption_context is not None:
            result += f"encryption_context={repr(self.encryption_context)}, "

        if self.kms_arn is not None:
            result += f"kms_arn={repr(self.kms_arn)}, "

        if self.strategy is not None:
            result += f"strategy={repr(self.strategy)}, "

        if self.hierarchy_version is not None:
            result += f"hierarchy_version={repr(self.hierarchy_version)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateKeyInput):
            return False
        attributes: list[str] = [
            "identifier",
            "encryption_context",
            "kms_arn",
            "strategy",
            "hierarchy_version",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class CreateKeyOutput:
    identifier: str
    hierarchy_version: str

    def __init__(
        self,
        *,
        identifier: str,
        hierarchy_version: str,
    ):
        """
        :param identifier: A identifier for the created Branch Key.
        :param hierarchy_version: The hierarchy-version of a Branch Key;
          all items of
        the same Branch Key SHOULD
          have the same hierarchy-version.
          The
        hierarchy-version determines how the Branch Key Store
          protects and validates
        the branch key context (BKC).
        """
        self.identifier = identifier
        self.hierarchy_version = hierarchy_version

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CreateKeyOutput to a dictionary."""
        return {
            "identifier": self.identifier,
            "hierarchy_version": self.hierarchy_version,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CreateKeyOutput":
        """Creates a CreateKeyOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
            "hierarchy_version": d["hierarchy_version"],
        }

        return CreateKeyOutput(**kwargs)

    def __repr__(self) -> str:
        result = "CreateKeyOutput("
        if self.identifier is not None:
            result += f"identifier={repr(self.identifier)}, "

        if self.hierarchy_version is not None:
            result += f"hierarchy_version={repr(self.hierarchy_version)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CreateKeyOutput):
            return False
        attributes: list[str] = [
            "identifier",
            "hierarchy_version",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class DescribeMutationInput:
    identifier: str

    def __init__(
        self,
        *,
        identifier: str,
    ):
        """
        :param identifier: The identifier for the Branch Key.
        """
        self.identifier = identifier

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DescribeMutationInput to a dictionary."""
        return {
            "identifier": self.identifier,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DescribeMutationInput":
        """Creates a DescribeMutationInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
        }

        return DescribeMutationInput(**kwargs)

    def __repr__(self) -> str:
        result = "DescribeMutationInput("
        if self.identifier is not None:
            result += f"identifier={repr(self.identifier)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DescribeMutationInput):
            return False
        attributes: list[str] = [
            "identifier",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class Mutations:
    terminal_kms_arn: Optional[str]
    terminal_encryption_context: Optional[dict[str, str]]
    terminal_hierarchy_version: Optional[str]

    def __init__(
        self,
        *,
        terminal_kms_arn: Optional[str] = None,
        terminal_encryption_context: Optional[dict[str, str]] = None,
        terminal_hierarchy_version: Optional[str] = None,
    ):
        """Define the Mutation in terms of the terminal, or end state, value
        for a particular Branch Key property. The original value will be
        REPLACED with this value.

        As of v<HV-2>, a Mutation can either:
        - replace the KmsArn protecting the
        Branch Key
        - replace the encryption context
        - change the 'hierarchy-version'
        -
        any combination of the above

        :param terminal_kms_arn: Optional. If not set, there will be no change to the
        KMS ARN.
          If set, ReEncrypt all Items of the Branch Key
          to be authorized by
        this
          AWS Key Management Service Key.
          A Multi-Region or Single Region AWS KMS
        Key are permitted,
          but not aliases!
        :param terminal_encryption_context: Optional. If not set, there will be no
        change to the Encryption Context.
          ReEncrypt all Items of the Branch Key
          to
        be authorized with this encryption context.
          An empty Encryption Context is not
        allowed.
        :param terminal_hierarchy_version: Optional. If set, changes the
        hierarchy-version of the Branch Key.
          At this time, only '2' is allowed; there
        is no operation that faciliates HV-2 -> HV-1.
        """
        self.terminal_kms_arn = terminal_kms_arn
        self.terminal_encryption_context = terminal_encryption_context
        self.terminal_hierarchy_version = terminal_hierarchy_version

    def as_dict(self) -> Dict[str, Any]:
        """Converts the Mutations to a dictionary."""
        d: Dict[str, Any] = {}

        if self.terminal_kms_arn is not None:
            d["terminal_kms_arn"] = self.terminal_kms_arn

        if self.terminal_encryption_context is not None:
            d["terminal_encryption_context"] = self.terminal_encryption_context

        if self.terminal_hierarchy_version is not None:
            d["terminal_hierarchy_version"] = self.terminal_hierarchy_version

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Mutations":
        """Creates a Mutations from a dictionary."""
        kwargs: Dict[str, Any] = {}

        if "terminal_kms_arn" in d:
            kwargs["terminal_kms_arn"] = d["terminal_kms_arn"]

        if "terminal_encryption_context" in d:
            kwargs["terminal_encryption_context"] = d["terminal_encryption_context"]

        if "terminal_hierarchy_version" in d:
            kwargs["terminal_hierarchy_version"] = d["terminal_hierarchy_version"]

        return Mutations(**kwargs)

    def __repr__(self) -> str:
        result = "Mutations("
        if self.terminal_kms_arn is not None:
            result += f"terminal_kms_arn={repr(self.terminal_kms_arn)}, "

        if self.terminal_encryption_context is not None:
            result += f"terminal_encryption_context={repr(self.terminal_encryption_context)}, "

        if self.terminal_hierarchy_version is not None:
            result += (
                f"terminal_hierarchy_version={repr(self.terminal_hierarchy_version)}"
            )

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Mutations):
            return False
        attributes: list[str] = [
            "terminal_kms_arn",
            "terminal_encryption_context",
            "terminal_hierarchy_version",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class MutableBranchKeyContext:
    kms_arn: str
    encryption_context: dict[str, str]
    hierarchy_version: str

    def __init__(
        self,
        *,
        kms_arn: str,
        encryption_context: dict[str, str],
        hierarchy_version: str,
    ):
        """Define the Mutable Context of a Branch Key. As of v1.9.0, the
        Mutable Context.

        are:
        - The KmsArn protecting the Branch Key
        - The encryption context of a Branch
        Key

        :param kms_arn: The KmsArn protecting the Branch Key.
        :param encryption_context: The Encryption Context authenticated with this Branch
        Key.
        :param hierarchy_version: The 'hierarchy-version' of the Branch Key.
        """
        self.kms_arn = kms_arn
        self.encryption_context = encryption_context
        self.hierarchy_version = hierarchy_version

    def as_dict(self) -> Dict[str, Any]:
        """Converts the MutableBranchKeyContext to a dictionary."""
        return {
            "kms_arn": self.kms_arn,
            "encryption_context": self.encryption_context,
            "hierarchy_version": self.hierarchy_version,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MutableBranchKeyContext":
        """Creates a MutableBranchKeyContext from a dictionary."""
        kwargs: Dict[str, Any] = {
            "kms_arn": d["kms_arn"],
            "encryption_context": d["encryption_context"],
            "hierarchy_version": d["hierarchy_version"],
        }

        return MutableBranchKeyContext(**kwargs)

    def __repr__(self) -> str:
        result = "MutableBranchKeyContext("
        if self.kms_arn is not None:
            result += f"kms_arn={repr(self.kms_arn)}, "

        if self.encryption_context is not None:
            result += f"encryption_context={repr(self.encryption_context)}, "

        if self.hierarchy_version is not None:
            result += f"hierarchy_version={repr(self.hierarchy_version)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MutableBranchKeyContext):
            return False
        attributes: list[str] = [
            "kms_arn",
            "encryption_context",
            "hierarchy_version",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class MutationDetails:
    original: MutableBranchKeyContext
    terminal: MutableBranchKeyContext
    input: Mutations
    system_key: str
    create_time: str
    uuid: str

    def __init__(
        self,
        *,
        original: MutableBranchKeyContext,
        terminal: MutableBranchKeyContext,
        input: Mutations,
        system_key: str,
        create_time: str,
        uuid: str,
    ):
        """
        :param original: The original properties of the Branch Key.
        :param terminal: The terminal properties of the Branch Key.
        :param input: The input for this mutation.
        :param system_key: String description of the System Key.
        :param create_time: ISO 8601 time when the mutation was initialized.
        :param uuid: UUID of the Mutation.
        """
        self.original = original
        self.terminal = terminal
        self.input = input
        self.system_key = system_key
        self.create_time = create_time
        self.uuid = uuid

    def as_dict(self) -> Dict[str, Any]:
        """Converts the MutationDetails to a dictionary."""
        return {
            "original": self.original.as_dict(),
            "terminal": self.terminal.as_dict(),
            "input": self.input.as_dict(),
            "system_key": self.system_key,
            "create_time": self.create_time,
            "uuid": self.uuid,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MutationDetails":
        """Creates a MutationDetails from a dictionary."""
        kwargs: Dict[str, Any] = {
            "original": MutableBranchKeyContext.from_dict(d["original"]),
            "terminal": MutableBranchKeyContext.from_dict(d["terminal"]),
            "input": Mutations.from_dict(d["input"]),
            "system_key": d["system_key"],
            "create_time": d["create_time"],
            "uuid": d["uuid"],
        }

        return MutationDetails(**kwargs)

    def __repr__(self) -> str:
        result = "MutationDetails("
        if self.original is not None:
            result += f"original={repr(self.original)}, "

        if self.terminal is not None:
            result += f"terminal={repr(self.terminal)}, "

        if self.input is not None:
            result += f"input={repr(self.input)}, "

        if self.system_key is not None:
            result += f"system_key={repr(self.system_key)}, "

        if self.create_time is not None:
            result += f"create_time={repr(self.create_time)}, "

        if self.uuid is not None:
            result += f"uuid={repr(self.uuid)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MutationDetails):
            return False
        attributes: list[str] = [
            "original",
            "terminal",
            "input",
            "system_key",
            "create_time",
            "uuid",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class MutationDescription:
    mutation_details: MutationDetails
    mutation_token: MutationToken

    def __init__(
        self,
        *,
        mutation_details: MutationDetails,
        mutation_token: MutationToken,
    ):
        """
        :param mutation_details: Detailed description of the Mutation for this Branch
        Key.
        :param mutation_token: This token can be passed to Apply Mutation to continue
        the Mutation.
        """
        self.mutation_details = mutation_details
        self.mutation_token = mutation_token

    def as_dict(self) -> Dict[str, Any]:
        """Converts the MutationDescription to a dictionary."""
        return {
            "mutation_details": self.mutation_details.as_dict(),
            "mutation_token": self.mutation_token.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MutationDescription":
        """Creates a MutationDescription from a dictionary."""
        kwargs: Dict[str, Any] = {
            "mutation_details": MutationDetails.from_dict(d["mutation_details"]),
            "mutation_token": MutationToken.from_dict(d["mutation_token"]),
        }

        return MutationDescription(**kwargs)

    def __repr__(self) -> str:
        result = "MutationDescription("
        if self.mutation_details is not None:
            result += f"mutation_details={repr(self.mutation_details)}, "

        if self.mutation_token is not None:
            result += f"mutation_token={repr(self.mutation_token)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MutationDescription):
            return False
        attributes: list[str] = [
            "mutation_details",
            "mutation_token",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class MutationInFlightYes:
    def __init__(self, value: MutationDescription):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"Yes": self.value.as_dict()}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MutationInFlightYes":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return MutationInFlightYes(MutationDescription.from_dict(d["Yes"]))

    def __repr__(self) -> str:
        return f"MutationInFlightYes(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MutationInFlightYes):
            return False
        return self.value == other.value


class MutationInFlightNo:
    def __init__(self, value: str):
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {"No": self.value}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MutationInFlightNo":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")

        return MutationInFlightNo(d["No"])

    def __repr__(self) -> str:
        return f"MutationInFlightNo(value=repr(self.value))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MutationInFlightNo):
            return False
        return self.value == other.value


class MutationInFlightUnknown:
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
    def from_dict(d: Dict[str, Any]) -> "MutationInFlightUnknown":
        if len(d) != 1:
            raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")
        return MutationInFlightUnknown(d["SDK_UNKNOWN_MEMBER"]["name"])

    def __repr__(self) -> str:
        return f"MutationInFlightUnknown(tag={self.tag})"


# If a Mutation is In Flight for this Branch Key.
MutationInFlight = Union[
    MutationInFlightYes, MutationInFlightNo, MutationInFlightUnknown
]


def _mutation_in_flight_from_dict(d: Dict[str, Any]) -> MutationInFlight:
    if "Yes" in d:
        return MutationInFlightYes.from_dict(d)

    if "No" in d:
        return MutationInFlightNo.from_dict(d)

    raise TypeError(f"Unions may have exactly 1 value, but found {len(d)}")


class DescribeMutationOutput:
    mutation_in_flight: MutationInFlight

    def __init__(
        self,
        *,
        mutation_in_flight: MutationInFlight,
    ):
        """
        :param mutation_in_flight: If a Mutation is In Flight for this Branch Key.
        """
        self.mutation_in_flight = mutation_in_flight

    def as_dict(self) -> Dict[str, Any]:
        """Converts the DescribeMutationOutput to a dictionary."""
        return {
            "mutation_in_flight": self.mutation_in_flight.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "DescribeMutationOutput":
        """Creates a DescribeMutationOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "mutation_in_flight": _mutation_in_flight_from_dict(
                d["mutation_in_flight"]
            ),
        }

        return DescribeMutationOutput(**kwargs)

    def __repr__(self) -> str:
        result = "DescribeMutationOutput("
        if self.mutation_in_flight is not None:
            result += f"mutation_in_flight={repr(self.mutation_in_flight)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DescribeMutationOutput):
            return False
        attributes: list[str] = [
            "mutation_in_flight",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class InitializeMutationInput:
    identifier: str
    mutations: Mutations
    strategy: Optional[KeyManagementStrategy]
    system_key: SystemKey
    do_not_version: Optional[bool]

    def __init__(
        self,
        *,
        identifier: str,
        mutations: Mutations,
        system_key: SystemKey,
        strategy: Optional[KeyManagementStrategy] = None,
        do_not_version: Optional[bool] = None,
    ):
        """
        :param identifier: The identifier for the Branch Key to be mutated.
        :param mutations: Describes the Mutation that will be applied to all Items of
        the Branch Key.
        :param system_key: Key Store Admin protects any non-cryptographic
        items stored
        with this Key.
        Using 'KMS Symmetric Encryption' is a best practice,
        as it
        prevents actors with only write access to the Key Store's storage
        from tampering
        with Mutations.
        For a Mutation, the System Key setting MUST be consistent across
        the Initialize Mutation and all the Apply Mutation calls.
        :param strategy: Optional. Defaults to reEncrypt with a default KMS Client.

        However, if the Branch Key's 'hierarchy-version' is HV-2,
          or the Branch Key is
        being mutated to HV-2,
          the Strategy MUST be AwsKmsDecryptEncrypt or
        AwsKmsSimple.
        :param do_not_version: Optional. Defaults to False, which Versions (or Rotates)
        the Branch Key,
          creating a new Version that has only ever been in the terminal
        state.
          Setting this value to True disables the rotation.
          This is a Security
        vs Performance trade off.
          Mutating a Branch Key can change the security domain
        of the Branch Key.
          Some application's Threat Models benefit from ensuring a
        new Version
          is created whenever a Mutation occurs,
          allowing the application
        to track under which security domain data
          was protected.
          However, not all
        Threat Models call for this.
          Particularly if Mutations are triggered in
        response to external actors,
          creating a new Version for every Mutation request
        can needlessly grow
          the item count of a Branch Key.
        """
        self.identifier = identifier
        self.mutations = mutations
        self.system_key = system_key
        self.strategy = strategy
        self.do_not_version = do_not_version

    def as_dict(self) -> Dict[str, Any]:
        """Converts the InitializeMutationInput to a dictionary."""
        d: Dict[str, Any] = {
            "identifier": self.identifier,
            "mutations": self.mutations.as_dict(),
            "system_key": self.system_key.as_dict(),
        }

        if self.strategy is not None:
            d["strategy"] = self.strategy.as_dict()

        if self.do_not_version is not None:
            d["do_not_version"] = self.do_not_version

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InitializeMutationInput":
        """Creates a InitializeMutationInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
            "mutations": Mutations.from_dict(d["mutations"]),
            "system_key": _system_key_from_dict(d["system_key"]),
        }

        if "strategy" in d:
            kwargs["strategy"] = (_key_management_strategy_from_dict(d["strategy"]),)

        if "do_not_version" in d:
            kwargs["do_not_version"] = d["do_not_version"]

        return InitializeMutationInput(**kwargs)

    def __repr__(self) -> str:
        result = "InitializeMutationInput("
        if self.identifier is not None:
            result += f"identifier={repr(self.identifier)}, "

        if self.mutations is not None:
            result += f"mutations={repr(self.mutations)}, "

        if self.strategy is not None:
            result += f"strategy={repr(self.strategy)}, "

        if self.system_key is not None:
            result += f"system_key={repr(self.system_key)}, "

        if self.do_not_version is not None:
            result += f"do_not_version={repr(self.do_not_version)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, InitializeMutationInput):
            return False
        attributes: list[str] = [
            "identifier",
            "mutations",
            "strategy",
            "system_key",
            "do_not_version",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class InitializeMutationFlag:
    CREATED = "Created"

    RESUMED = "Resumed"

    RESUMED_WITHOUT_INDEX = "ResumedWithoutIndex"

    # This set contains every possible value known at the time this was generated. New
    # values may be added in the future.
    values = frozenset({"Created", "Resumed", "ResumedWithoutIndex"})


class InitializeMutationOutput:
    mutation_token: MutationToken
    mutated_branch_key_items: list[MutatedBranchKeyItem]
    initialize_mutation_flag: str

    def __init__(
        self,
        *,
        mutation_token: MutationToken,
        mutated_branch_key_items: list[MutatedBranchKeyItem],
        initialize_mutation_flag: str,
    ):
        """
        :param mutation_token: Pass the Mutation Token to the Apply Mutation operation
        to continue the Mutation.
        :param mutated_branch_key_items: Details what items of the Branch Key ID were
        changed on this invocation.
        """
        self.mutation_token = mutation_token
        self.mutated_branch_key_items = mutated_branch_key_items
        self.initialize_mutation_flag = initialize_mutation_flag

    def as_dict(self) -> Dict[str, Any]:
        """Converts the InitializeMutationOutput to a dictionary."""
        return {
            "mutation_token": self.mutation_token.as_dict(),
            "mutated_branch_key_items": _mutated_branch_key_items_as_dict(
                self.mutated_branch_key_items
            ),
            "initialize_mutation_flag": self.initialize_mutation_flag,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InitializeMutationOutput":
        """Creates a InitializeMutationOutput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "mutation_token": MutationToken.from_dict(d["mutation_token"]),
            "mutated_branch_key_items": _mutated_branch_key_items_from_dict(
                d["mutated_branch_key_items"]
            ),
            "initialize_mutation_flag": d["initialize_mutation_flag"],
        }

        return InitializeMutationOutput(**kwargs)

    def __repr__(self) -> str:
        result = "InitializeMutationOutput("
        if self.mutation_token is not None:
            result += f"mutation_token={repr(self.mutation_token)}, "

        if self.mutated_branch_key_items is not None:
            result += (
                f"mutated_branch_key_items={repr(self.mutated_branch_key_items)}, "
            )

        if self.initialize_mutation_flag is not None:
            result += f"initialize_mutation_flag={repr(self.initialize_mutation_flag)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, InitializeMutationOutput):
            return False
        attributes: list[str] = [
            "mutation_token",
            "mutated_branch_key_items",
            "initialize_mutation_flag",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class VersionKeyInput:
    identifier: str
    kms_arn: KmsSymmetricKeyArn
    strategy: Optional[KeyManagementStrategy]

    def __init__(
        self,
        *,
        identifier: str,
        kms_arn: KmsSymmetricKeyArn,
        strategy: Optional[KeyManagementStrategy] = None,
    ):
        """
        :param identifier: The identifier for the Branch Key to be versioned.
        :param kms_arn: Multi-Region or Single Region AWS KMS Key ARN used to protect
        the Branch Key, but not aliases!
        :param strategy: For 'hierarchy-version-1' (HV-1), only AwsKmsReEncrypt or
        AwsKmsSimple are supported.
          For 'hierarchy-version-2' (HV-2), only
        AwsKmsSimple is supported.
        """
        self.identifier = identifier
        self.kms_arn = kms_arn
        self.strategy = strategy

    def as_dict(self) -> Dict[str, Any]:
        """Converts the VersionKeyInput to a dictionary."""
        d: Dict[str, Any] = {
            "identifier": self.identifier,
            "kms_arn": self.kms_arn.as_dict(),
        }

        if self.strategy is not None:
            d["strategy"] = self.strategy.as_dict()

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "VersionKeyInput":
        """Creates a VersionKeyInput from a dictionary."""
        kwargs: Dict[str, Any] = {
            "identifier": d["identifier"],
            "kms_arn": _kms_symmetric_key_arn_from_dict(d["kms_arn"]),
        }

        if "strategy" in d:
            kwargs["strategy"] = (_key_management_strategy_from_dict(d["strategy"]),)

        return VersionKeyInput(**kwargs)

    def __repr__(self) -> str:
        result = "VersionKeyInput("
        if self.identifier is not None:
            result += f"identifier={repr(self.identifier)}, "

        if self.kms_arn is not None:
            result += f"kms_arn={repr(self.kms_arn)}, "

        if self.strategy is not None:
            result += f"strategy={repr(self.strategy)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, VersionKeyInput):
            return False
        attributes: list[str] = [
            "identifier",
            "kms_arn",
            "strategy",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class VersionKeyOutput:
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


def _mutated_branch_key_items_as_dict(given: list[MutatedBranchKeyItem]) -> List[Any]:
    return [v.as_dict() for v in given]


def _mutated_branch_key_items_from_dict(given: List[Any]) -> list[MutatedBranchKeyItem]:
    return [MutatedBranchKeyItem.from_dict(v) for v in given]


class Unit:
    pass
