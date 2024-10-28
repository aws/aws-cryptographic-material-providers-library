# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import _dafny
import aws_cryptography_primitives.internaldafny.generated
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes
import aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.errors
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


class AwsCryptographicPrimitivesError(
    ApiError[Literal["AwsCryptographicPrimitivesError"]]
):
    code: Literal["AwsCryptographicPrimitivesError"] = "AwsCryptographicPrimitivesError"
    message: str

    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self) -> Dict[str, Any]:
        """Converts the AwsCryptographicPrimitivesError to a dictionary."""
        return {
            "message": self.message,
            "code": self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "AwsCryptographicPrimitivesError":
        """Creates a AwsCryptographicPrimitivesError from a dictionary."""
        kwargs: Dict[str, Any] = {
            "message": d["message"],
        }

        return AwsCryptographicPrimitivesError(**kwargs)

    def __repr__(self) -> str:
        result = "AwsCryptographicPrimitivesError("
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AwsCryptographicPrimitivesError):
            return False
        attributes: list[str] = [
            "message",
            "message",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


class AwsCryptographicPrimitivesError(
    ApiError[Literal["AwsCryptographicPrimitivesError"]]
):
    code: Literal["AwsCryptographicPrimitivesError"] = "AwsCryptographicPrimitivesError"
    message: str


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

    def __init__(self, *, obj, alt_text):
        super().__init__("")
        self.obj = obj
        self.alt_text = alt_text

    def as_dict(self) -> Dict[str, Any]:
        """Converts the OpaqueError to a dictionary.

        The dictionary uses the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        return {
            "message": self.message,
            "code": self.code,
            "obj": self.obj,
            "alt_text": self.alt_text,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "OpaqueError":
        """Creates a OpaqueError from a dictionary.

        The dictionary is expected to use the modeled shape names rather
        than the parameter names as keys to be mostly compatible with
        boto3.
        """
        kwargs: Dict[str, Any] = {
            "message": d["message"],
            "obj": d["obj"],
            "alt_text": d["alt_text"],
        }

        return OpaqueError(**kwargs)

    def __repr__(self) -> str:
        result = "OpaqueError("
        result += f"message={self.message},"
        if self.message is not None:
            result += f"message={repr(self.message)}"
        result += f"obj={self.alt_text}"
        result += ")"
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, OpaqueError):
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
        aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.errors.AwsCryptographicPrimitivesError,
    ):
        return aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(
            message=_dafny.Seq(e.message)
        )

    if isinstance(e, CollectionOfErrors):
        return aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes.Error_CollectionOfErrors(
            message=_dafny.Seq(e.message),
            list=_dafny.Seq(
                _smithy_error_to_dafny_error(native_err) for native_err in e.list
            ),
        )

    if isinstance(e, OpaqueError):
        return aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes.Error_Opaque(
            obj=e.obj, alt__text=e.alt_text
        )

    else:
        return aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes.Error_Opaque(
            obj=e,
            alt__text=_dafny.Seq(
                "".join(
                    [
                        chr(int.from_bytes(pair, "big"))
                        for pair in zip(*[iter(repr(e).encode("utf-16-be"))] * 2)
                    ]
                )
            ),
        )
