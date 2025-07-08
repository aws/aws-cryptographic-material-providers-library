# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import _dafny
import aws_cryptographic_material_providers.internaldafny.generated
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.errors
from aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.shim import (
    _sdk_error_to_dafny_error as com_amazonaws_dynamodb_sdk_error_to_dafny_error,
)
from aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.shim import (
    _sdk_error_to_dafny_error as com_amazonaws_kms_sdk_error_to_dafny_error,
)
from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.errors import (
    _smithy_error_to_dafny_error as aws_cryptography_primitives_smithy_error_to_dafny_error,
)
from typing import Any, Dict, Generic, List, Literal, TypeVar


class ServiceError(Exception):
    """Base error for all errors in the service."""

    pass


T = TypeVar("T")


class ApiError(ServiceError, Generic[T]):
    """Base error for all api errors in the service."""

    code: T

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class UnknownApiError(ApiError[Literal["Unknown"]]):
    """Error representing any unknown api errors."""

    code: Literal["Unknown"] = "Unknown"


class BranchKeyCiphertextException(ApiError[Literal["BranchKeyCiphertextException"]]):
    code: Literal["BranchKeyCiphertextException"] = "BranchKeyCiphertextException"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        """The cipher-text or branch key materials incorporated into the
        cipher-text, such as the encryption context, is corrupted, missing, or
        otherwise invalid. For branch keys,

        the branch key materials is a combination of:
        - the encryption
        context
        - storage identifiers (partition key, sort key, logical name)
        - metadata
        that binds the Branch Key to encrypted data (version)
        - create-time
        -
        hierarchy-version

        If any of the above are modified without calling KMS,
        the
        branch key's cipher-text becomes invalid.

        :param message: A message associated with the specific error.
        """
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the BranchKeyCiphertextException to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "BranchKeyCiphertextException":
        """Creates a BranchKeyCiphertextException from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return BranchKeyCiphertextException(**kwargs)

    def __repr__(self) -> str:
        result = "BranchKeyCiphertextException("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, BranchKeyCiphertextException):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class KeyStoreException(ApiError[Literal["KeyStoreException"]]):
    code: Literal["KeyStoreException"] = "KeyStoreException"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the KeyStoreException to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyStoreException":
        """Creates a KeyStoreException from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return KeyStoreException(**kwargs)

    def __repr__(self) -> str:
        result = "KeyStoreException("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyStoreException):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class BranchKeyCiphertextException(ApiError[Literal["BranchKeyCiphertextException"]]):
    code: Literal["BranchKeyCiphertextException"] = "BranchKeyCiphertextException"
    message: str


class KeyStoreException(ApiError[Literal["KeyStoreException"]]):
    code: Literal["KeyStoreException"] = "KeyStoreException"
    message: str


class ComAmazonawsDynamodb(ApiError[Literal["ComAmazonawsDynamodb"]]):
    ComAmazonawsDynamodb: Any


class ComAmazonawsKms(ApiError[Literal["ComAmazonawsKms"]]):
    ComAmazonawsKms: Any


class AwsCryptographicPrimitives(ApiError[Literal["AwsCryptographicPrimitives"]]):
    AwsCryptographicPrimitives: Any


class CollectionOfErrors(ApiError[Literal["CollectionOfErrors"]]):
    code: Literal["CollectionOfErrors"] = "CollectionOfErrors"
    message: str
    list: List[ServiceError]

    def __init__(self, *, message: str, list):
        super().__init__(message)
        self.list = list

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CollectionOfErrors to a dictionary.

        The dictionary uses the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        return {
            "message": self.message,
            "code": self.code,
            "list": self.list,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CollectionOfErrors":
        """Creates a CollectionOfErrors from a dictionary.

        The dictionary is expected to use the modeled shape names rather
        than the parameter names as keys to be mostly compatible with
        boto3.
        """
        kwargs: Dict[str, Any] = {"message": d["message"], "list": d["list"]}

        return CollectionOfErrors(**kwargs)

    def __repr__(self) -> str:
        result = "CollectionOfErrors("
        result += f"message={self.message},"
        if self.message is not None:
            result += f"message={repr(self.message)}"
        result += f"list={self.list}"
        result += ")"
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CollectionOfErrors):
            return False
        if not (self.list == other.list):
            return False
        attributes: list[str] = ["message", "message"]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class OpaqueError(ApiError[Literal["OpaqueError"]]):
    code: Literal["OpaqueError"] = "OpaqueError"
    obj: Any  # As an OpaqueError, type of obj is unknown

    def __init__(self, *, obj):
        super().__init__("")
        self.obj = obj

    def as_dict(self) -> Dict[str, Any]:
        """Converts the OpaqueError to a dictionary.

        The dictionary uses the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        return {
            "message": self.message,
            "code": self.code,
            "obj": self.obj,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "OpaqueError":
        """Creates a OpaqueError from a dictionary.

        The dictionary is expected to use the modeled shape names rather
        than the parameter names as keys to be mostly compatible with
        boto3.
        """
        kwargs: Dict[str, Any] = {"message": d["message"], "obj": d["obj"]}

        return OpaqueError(**kwargs)

    def __repr__(self) -> str:
        result = "OpaqueError("
        result += f"message={self.message},"
        if self.message is not None:
            result += f"message={repr(self.message)}"
        result += f"obj={self.obj}"
        result += ")"
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, OpaqueError):
            return False
        if not (self.obj == other.obj):
            return False
        attributes: list[str] = ["message", "message"]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class OpaqueWithTextError(ApiError[Literal["OpaqueWithTextError"]]):
    code: Literal["OpaqueWithTextError"] = "OpaqueWithTextError"
    obj: Any  # As an OpaqueWithTextError, type of obj is unknown
    obj_message: str  # obj_message is a message representing the details of obj

    def __init__(self, *, obj, obj_message):
        super().__init__("")
        self.obj = obj
        self.obj_message = obj_message

    def as_dict(self) -> Dict[str, Any]:
        """Converts the OpaqueWithTextError to a dictionary.

        The dictionary uses the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        return {
            "message": self.message,
            "code": self.code,
            "obj": self.obj,
            "obj_message": self.obj_message,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "OpaqueWithTextError":
        """Creates a OpaqueWithTextError from a dictionary.

        The dictionary is expected to use the modeled shape names rather
        than the parameter names as keys to be mostly compatible with
        boto3.
        """
        kwargs: Dict[str, Any] = {
            "message": d["message"],
            "obj": d["obj"],
            "obj_message": d["obj_message"],
        }

        return OpaqueWithTextError(**kwargs)

    def __repr__(self) -> str:
        result = "OpaqueWithTextError("
        result += f"message={self.message},"
        if self.message is not None:
            result += f"message={repr(self.message)}"
        result += f"obj={self.obj}"
        result += f"obj_message={self.obj_message}"
        result += ")"
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, OpaqueWithTextError):
            return False
        if not (self.obj == other.obj):
            return False
        attributes: list[str] = ["message", "message"]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


def _smithy_error_to_dafny_error(e: ServiceError):
    """Converts the provided native Smithy-modeled error into the corresponding
    Dafny error."""
    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.errors.BranchKeyCiphertextException,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes.Error_BranchKeyCiphertextException(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.errors.KeyStoreException,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes.Error_KeyStoreException(
            message=_dafny.Seq(e.message)
        )

    if isinstance(e, ComAmazonawsDynamodb):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(
            com_amazonaws_dynamodb_sdk_error_to_dafny_error(e.message)
        )

    if isinstance(e, ComAmazonawsKms):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes.Error_ComAmazonawsKms(
            com_amazonaws_kms_sdk_error_to_dafny_error(e.message)
        )

    if isinstance(e, AwsCryptographicPrimitives):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes.Error_AwsCryptographyPrimitives(
            aws_cryptography_primitives_smithy_error_to_dafny_error(e.message)
        )

    if isinstance(e, CollectionOfErrors):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes.Error_CollectionOfErrors(
            message=_dafny.Seq(e.message),
            list=_dafny.Seq(
                _smithy_error_to_dafny_error(native_err) for native_err in e.list
            ),
        )

    if isinstance(e, OpaqueError):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes.Error_Opaque(
            obj=e.obj
        )

    if isinstance(e, OpaqueWithTextError):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes.Error_OpaqueWithText(
            obj=e.obj, objMessage=e.obj_message
        )

    else:
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes.Error_Opaque(
            obj=e
        )
