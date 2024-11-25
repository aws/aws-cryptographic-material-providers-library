# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import _dafny
import aws_cryptographic_material_providers.internaldafny.generated
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes
from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.errors import (
    _smithy_error_to_dafny_error as aws_cryptography_keystore_smithy_error_to_dafny_error,
)
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.errors
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


class KeyStoreAdminException(ApiError[Literal["KeyStoreAdminException"]]):
    code: Literal["KeyStoreAdminException"] = "KeyStoreAdminException"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the KeyStoreAdminException to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyStoreAdminException":
        """Creates a KeyStoreAdminException from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return KeyStoreAdminException(**kwargs)

    def __repr__(self) -> str:
        result = "KeyStoreAdminException("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyStoreAdminException):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class MutationFromException(ApiError[Literal["MutationFromException"]]):
    code: Literal["MutationFromException"] = "MutationFromException"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        """Key Management generic error encountered while mutating an item from
        original to terminal.

        Possibly, access to the terminal KMS Key was withdrawn.
        :param message: A message associated with the specific error.
        """
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the MutationFromException to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MutationFromException":
        """Creates a MutationFromException from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return MutationFromException(**kwargs)

    def __repr__(self) -> str:
        result = "MutationFromException("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MutationFromException):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class MutationInvalidException(ApiError[Literal["MutationInvalidException"]]):
    code: Literal["MutationInvalidException"] = "MutationInvalidException"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the MutationInvalidException to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MutationInvalidException":
        """Creates a MutationInvalidException from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return MutationInvalidException(**kwargs)

    def __repr__(self) -> str:
        result = "MutationInvalidException("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MutationInvalidException):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class MutationToException(ApiError[Literal["MutationToException"]]):
    code: Literal["MutationToException"] = "MutationToException"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        """Key Management generic error encountered while mutating an item from
        original to terminal.

        Possibly, access to the terminal KMS Key was withdrawn.
        :param message: A message associated with the specific error.
        """
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the MutationToException to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MutationToException":
        """Creates a MutationToException from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return MutationToException(**kwargs)

    def __repr__(self) -> str:
        result = "MutationToException("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MutationToException):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class MutationVerificationException(ApiError[Literal["MutationVerificationException"]]):
    code: Literal["MutationVerificationException"] = "MutationVerificationException"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        """Key Management generic error encountered while authenticating an
        item already in the terminal state.

        Possibly, access to the terminal KMS Key was withdrawn.
        :param message: A message associated with the specific error.
        """
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the MutationVerificationException to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MutationVerificationException":
        """Creates a MutationVerificationException from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return MutationVerificationException(**kwargs)

    def __repr__(self) -> str:
        result = "MutationVerificationException("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MutationVerificationException):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class UnexpectedStateException(ApiError[Literal["UnexpectedStateException"]]):
    code: Literal["UnexpectedStateException"] = "UnexpectedStateException"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the UnexpectedStateException to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "UnexpectedStateException":
        """Creates a UnexpectedStateException from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return UnexpectedStateException(**kwargs)

    def __repr__(self) -> str:
        result = "UnexpectedStateException("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, UnexpectedStateException):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class UnsupportedFeatureException(ApiError[Literal["UnsupportedFeatureException"]]):
    code: Literal["UnsupportedFeatureException"] = "UnsupportedFeatureException"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        """This feature is not yet implemented.

        :param message: A message associated with the specific error.
        """
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the UnsupportedFeatureException to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "UnsupportedFeatureException":
        """Creates a UnsupportedFeatureException from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return UnsupportedFeatureException(**kwargs)

    def __repr__(self) -> str:
        result = "UnsupportedFeatureException("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, UnsupportedFeatureException):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class MutationConflictException(ApiError[Literal["MutationConflictException"]]):
    code: Literal["MutationConflictException"] = "MutationConflictException"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        """A Mutation for this Branch Key ID is already inflight!

        Nothing was changed. See <link>.
        :param message: A message associated with the specific error.
        """
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the MutationConflictException to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MutationConflictException":
        """Creates a MutationConflictException from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return MutationConflictException(**kwargs)

    def __repr__(self) -> str:
        result = "MutationConflictException("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, MutationConflictException):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class KeyStoreAdminException(ApiError[Literal["KeyStoreAdminException"]]):
    code: Literal["KeyStoreAdminException"] = "KeyStoreAdminException"
    message: str


class MutationConflictException(ApiError[Literal["MutationConflictException"]]):
    code: Literal["MutationConflictException"] = "MutationConflictException"
    message: str


class MutationFromException(ApiError[Literal["MutationFromException"]]):
    code: Literal["MutationFromException"] = "MutationFromException"
    message: str


class MutationInvalidException(ApiError[Literal["MutationInvalidException"]]):
    code: Literal["MutationInvalidException"] = "MutationInvalidException"
    message: str


class MutationToException(ApiError[Literal["MutationToException"]]):
    code: Literal["MutationToException"] = "MutationToException"
    message: str


class MutationVerificationException(ApiError[Literal["MutationVerificationException"]]):
    code: Literal["MutationVerificationException"] = "MutationVerificationException"
    message: str


class UnexpectedStateException(ApiError[Literal["UnexpectedStateException"]]):
    code: Literal["UnexpectedStateException"] = "UnexpectedStateException"
    message: str


class UnsupportedFeatureException(ApiError[Literal["UnsupportedFeatureException"]]):
    code: Literal["UnsupportedFeatureException"] = "UnsupportedFeatureException"
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
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.errors.KeyStoreAdminException,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_KeyStoreAdminException(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.errors.MutationConflictException,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_MutationConflictException(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.errors.MutationFromException,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_MutationFromException(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.errors.MutationInvalidException,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_MutationInvalidException(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.errors.MutationToException,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_MutationToException(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.errors.MutationVerificationException,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_MutationVerificationException(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.errors.UnexpectedStateException,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_UnexpectedStateException(
            message=_dafny.Seq(e.message)
        )

    if isinstance(
        e,
        aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.errors.UnsupportedFeatureException,
    ):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_UnsupportedFeatureException(
            message=_dafny.Seq(e.message)
        )

    if isinstance(e, AwsCryptographicPrimitives):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_AwsCryptographyPrimitives(
            aws_cryptography_primitives_smithy_error_to_dafny_error(e.message)
        )

    if isinstance(e, ComAmazonawsDynamodb):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_ComAmazonawsDynamodb(
            com_amazonaws_dynamodb_sdk_error_to_dafny_error(e.message)
        )

    if isinstance(e, ComAmazonawsKms):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_ComAmazonawsKms(
            com_amazonaws_kms_sdk_error_to_dafny_error(e.message)
        )

    if isinstance(e, KeyStore):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_AwsCryptographyKeyStore(
            aws_cryptography_keystore_smithy_error_to_dafny_error(e.message)
        )

    if isinstance(e, CollectionOfErrors):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_CollectionOfErrors(
            message=_dafny.Seq(e.message),
            list=_dafny.Seq(
                _smithy_error_to_dafny_error(native_err) for native_err in e.list
            ),
        )

    if isinstance(e, OpaqueError):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_Opaque(
            obj=e.obj
        )

    if isinstance(e, OpaqueWithTextError):
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_OpaqueWithText(
            obj=e.obj, objMessage=e.obj_message
        )

    else:
        return aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes.Error_Opaque(
            obj=e
        )
