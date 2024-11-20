# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import _dafny
import aws_cryptographic_material_providers.internaldafny.generated
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes
from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.errors import (
    _smithy_error_to_dafny_error as aws_cryptography_keystore_smithy_error_to_dafny_error,
)
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.errors
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


class AwsCryptographicMaterialProvidersException(
    ApiError[Literal["AwsCryptographicMaterialProvidersException"]]
):
    code: Literal["AwsCryptographicMaterialProvidersException"] = (
        "AwsCryptographicMaterialProvidersException"
    )
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the AwsCryptographicMaterialProvidersException to a
        dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AwsCryptographicMaterialProvidersException":
        """Creates a AwsCryptographicMaterialProvidersException from a
        dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return AwsCryptographicMaterialProvidersException(**kwargs)

    def __repr__(self) -> str:
        result = "AwsCryptographicMaterialProvidersException("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AwsCryptographicMaterialProvidersException):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class InvalidDecryptionMaterials(ApiError[Literal["InvalidDecryptionMaterials"]]):
    code: Literal["InvalidDecryptionMaterials"] = "InvalidDecryptionMaterials"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the InvalidDecryptionMaterials to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InvalidDecryptionMaterials":
        """Creates a InvalidDecryptionMaterials from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return InvalidDecryptionMaterials(**kwargs)

    def __repr__(self) -> str:
        result = "InvalidDecryptionMaterials("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, InvalidDecryptionMaterials):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class InvalidEncryptionMaterials(ApiError[Literal["InvalidEncryptionMaterials"]]):
    code: Literal["InvalidEncryptionMaterials"] = "InvalidEncryptionMaterials"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the InvalidEncryptionMaterials to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InvalidEncryptionMaterials":
        """Creates a InvalidEncryptionMaterials from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return InvalidEncryptionMaterials(**kwargs)

    def __repr__(self) -> str:
        result = "InvalidEncryptionMaterials("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, InvalidEncryptionMaterials):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class InvalidAlgorithmSuiteInfo(ApiError[Literal["InvalidAlgorithmSuiteInfo"]]):
    code: Literal["InvalidAlgorithmSuiteInfo"] = "InvalidAlgorithmSuiteInfo"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the InvalidAlgorithmSuiteInfo to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InvalidAlgorithmSuiteInfo":
        """Creates a InvalidAlgorithmSuiteInfo from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return InvalidAlgorithmSuiteInfo(**kwargs)

    def __repr__(self) -> str:
        result = "InvalidAlgorithmSuiteInfo("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, InvalidAlgorithmSuiteInfo):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class InvalidAlgorithmSuiteInfoOnDecrypt(
    ApiError[Literal["InvalidAlgorithmSuiteInfoOnDecrypt"]]
):
    code: Literal["InvalidAlgorithmSuiteInfoOnDecrypt"] = (
        "InvalidAlgorithmSuiteInfoOnDecrypt"
    )
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the InvalidAlgorithmSuiteInfoOnDecrypt to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InvalidAlgorithmSuiteInfoOnDecrypt":
        """Creates a InvalidAlgorithmSuiteInfoOnDecrypt from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return InvalidAlgorithmSuiteInfoOnDecrypt(**kwargs)

    def __repr__(self) -> str:
        result = "InvalidAlgorithmSuiteInfoOnDecrypt("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, InvalidAlgorithmSuiteInfoOnDecrypt):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class InvalidAlgorithmSuiteInfoOnEncrypt(
    ApiError[Literal["InvalidAlgorithmSuiteInfoOnEncrypt"]]
):
    code: Literal["InvalidAlgorithmSuiteInfoOnEncrypt"] = (
        "InvalidAlgorithmSuiteInfoOnEncrypt"
    )
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the InvalidAlgorithmSuiteInfoOnEncrypt to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InvalidAlgorithmSuiteInfoOnEncrypt":
        """Creates a InvalidAlgorithmSuiteInfoOnEncrypt from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return InvalidAlgorithmSuiteInfoOnEncrypt(**kwargs)

    def __repr__(self) -> str:
        result = "InvalidAlgorithmSuiteInfoOnEncrypt("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, InvalidAlgorithmSuiteInfoOnEncrypt):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class InvalidDecryptionMaterialsTransition(
    ApiError[Literal["InvalidDecryptionMaterialsTransition"]]
):
    code: Literal["InvalidDecryptionMaterialsTransition"] = (
        "InvalidDecryptionMaterialsTransition"
    )
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the InvalidDecryptionMaterialsTransition to a
        dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InvalidDecryptionMaterialsTransition":
        """Creates a InvalidDecryptionMaterialsTransition from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return InvalidDecryptionMaterialsTransition(**kwargs)

    def __repr__(self) -> str:
        result = "InvalidDecryptionMaterialsTransition("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, InvalidDecryptionMaterialsTransition):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class InvalidEncryptionMaterialsTransition(
    ApiError[Literal["InvalidEncryptionMaterialsTransition"]]
):
    code: Literal["InvalidEncryptionMaterialsTransition"] = (
        "InvalidEncryptionMaterialsTransition"
    )
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the InvalidEncryptionMaterialsTransition to a
        dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InvalidEncryptionMaterialsTransition":
        """Creates a InvalidEncryptionMaterialsTransition from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return InvalidEncryptionMaterialsTransition(**kwargs)

    def __repr__(self) -> str:
        result = "InvalidEncryptionMaterialsTransition("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, InvalidEncryptionMaterialsTransition):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class EntryAlreadyExists(ApiError[Literal["EntryAlreadyExists"]]):
    code: Literal["EntryAlreadyExists"] = "EntryAlreadyExists"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the EntryAlreadyExists to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EntryAlreadyExists":
        """Creates a EntryAlreadyExists from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return EntryAlreadyExists(**kwargs)

    def __repr__(self) -> str:
        result = "EntryAlreadyExists("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EntryAlreadyExists):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class EntryDoesNotExist(ApiError[Literal["EntryDoesNotExist"]]):
    code: Literal["EntryDoesNotExist"] = "EntryDoesNotExist"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the EntryDoesNotExist to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "EntryDoesNotExist":
        """Creates a EntryDoesNotExist from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return EntryDoesNotExist(**kwargs)

    def __repr__(self) -> str:
        result = "EntryDoesNotExist("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EntryDoesNotExist):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class InFlightTTLExceeded(ApiError[Literal["InFlightTTLExceeded"]]):
    code: Literal["InFlightTTLExceeded"] = "InFlightTTLExceeded"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the InFlightTTLExceeded to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InFlightTTLExceeded":
        """Creates a InFlightTTLExceeded from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return InFlightTTLExceeded(**kwargs)

    def __repr__(self) -> str:
        result = "InFlightTTLExceeded("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, InFlightTTLExceeded):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class AwsCryptographicMaterialProvidersException(
    ApiError[Literal["AwsCryptographicMaterialProvidersException"]]
):
    code: Literal["AwsCryptographicMaterialProvidersException"] = (
        "AwsCryptographicMaterialProvidersException"
    )
    message: str


class EntryAlreadyExists(ApiError[Literal["EntryAlreadyExists"]]):
    code: Literal["EntryAlreadyExists"] = "EntryAlreadyExists"
    message: str


class EntryDoesNotExist(ApiError[Literal["EntryDoesNotExist"]]):
    code: Literal["EntryDoesNotExist"] = "EntryDoesNotExist"
    message: str


class InFlightTTLExceeded(ApiError[Literal["InFlightTTLExceeded"]]):
    code: Literal["InFlightTTLExceeded"] = "InFlightTTLExceeded"
    message: str


class InvalidAlgorithmSuiteInfo(ApiError[Literal["InvalidAlgorithmSuiteInfo"]]):
    code: Literal["InvalidAlgorithmSuiteInfo"] = "InvalidAlgorithmSuiteInfo"
    message: str


class InvalidAlgorithmSuiteInfoOnDecrypt(
    ApiError[Literal["InvalidAlgorithmSuiteInfoOnDecrypt"]]
):
    code: Literal["InvalidAlgorithmSuiteInfoOnDecrypt"] = (
        "InvalidAlgorithmSuiteInfoOnDecrypt"
    )
    message: str


class InvalidAlgorithmSuiteInfoOnEncrypt(
    ApiError[Literal["InvalidAlgorithmSuiteInfoOnEncrypt"]]
):
    code: Literal["InvalidAlgorithmSuiteInfoOnEncrypt"] = (
        "InvalidAlgorithmSuiteInfoOnEncrypt"
    )
    message: str


class InvalidDecryptionMaterials(ApiError[Literal["InvalidDecryptionMaterials"]]):
    code: Literal["InvalidDecryptionMaterials"] = "InvalidDecryptionMaterials"
    message: str


class InvalidDecryptionMaterialsTransition(
    ApiError[Literal["InvalidDecryptionMaterialsTransition"]]
):
    code: Literal["InvalidDecryptionMaterialsTransition"] = (
        "InvalidDecryptionMaterialsTransition"
    )
    message: str


class InvalidEncryptionMaterials(ApiError[Literal["InvalidEncryptionMaterials"]]):
    code: Literal["InvalidEncryptionMaterials"] = "InvalidEncryptionMaterials"
    message: str


class InvalidEncryptionMaterialsTransition(
    ApiError[Literal["InvalidEncryptionMaterialsTransition"]]
):
    code: Literal["InvalidEncryptionMaterialsTransition"] = (
        "InvalidEncryptionMaterialsTransition"
    )
    message: str


class AwsCryptographicPrimitives(ApiError[Literal["AwsCryptographicPrimitives"]]):
    AwsCryptographicPrimitives: Any


class ComAmazonawsDynamodb(ApiError[Literal["ComAmazonawsDynamodb"]]):
    ComAmazonawsDynamodb: Any


class ComAmazonawsKms(ApiError[Literal["ComAmazonawsKms"]]):
    ComAmazonawsKms: Any


class KeyStore(ApiError[Literal["KeyStore"]]):
    KeyStore: Any


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
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.errors.AwsCryptographicMaterialProvidersException,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.errors.EntryAlreadyExists,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_EntryAlreadyExists(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.errors.EntryDoesNotExist,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_EntryDoesNotExist(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.errors.InFlightTTLExceeded,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_InFlightTTLExceeded(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.errors.InvalidAlgorithmSuiteInfo,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_InvalidAlgorithmSuiteInfo(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.errors.InvalidAlgorithmSuiteInfoOnDecrypt,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_InvalidAlgorithmSuiteInfoOnDecrypt(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.errors.InvalidAlgorithmSuiteInfoOnEncrypt,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_InvalidAlgorithmSuiteInfoOnEncrypt(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.errors.InvalidDecryptionMaterials,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterials(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.errors.InvalidDecryptionMaterialsTransition,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterialsTransition(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.errors.InvalidEncryptionMaterials,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterials(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.errors.InvalidEncryptionMaterialsTransition,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(
            message=_dafny.Seq(e.message)
        )

    if isinstance(e, AwsCryptographicPrimitives):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(
            aws_cryptography_primitives_smithy_error_to_dafny_error(e.message)
        )

    if isinstance(e, ComAmazonawsDynamodb):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_ComAmazonawsDynamodb(
            com_amazonaws_dynamodb_sdk_error_to_dafny_error(e.message)
        )

    if isinstance(e, ComAmazonawsKms):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_ComAmazonawsKms(
            com_amazonaws_kms_sdk_error_to_dafny_error(e.message)
        )

    if isinstance(e, KeyStore):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyKeyStore(
            aws_cryptography_keystore_smithy_error_to_dafny_error(e.message)
        )

    if isinstance(e, CollectionOfErrors):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(
            message=_dafny.Seq(e.message),
            list=_dafny.Seq(
                _smithy_error_to_dafny_error(native_err) for native_err in e.list
            ),
        )

    if isinstance(e, OpaqueError):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_Opaque(
            obj=e.obj
        )

    if isinstance(e, OpaqueWithTextError):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_OpaqueWithText(
            obj=e.obj, objMessage=e.obj_message
        )

    else:
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.Error_Opaque(
            obj=e
        )
