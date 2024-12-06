# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreAdminTypes import (
    KeyStoreAdminConfig_KeyStoreAdminConfig as DafnyKeyStoreAdminConfig,
)
import aws_cryptographic_material_providers.internaldafny.generated.module_
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny
from dataclasses import dataclass
from typing import Any, Callable, Dict, TypeAlias

from .dafnyImplInterface import DafnyImplInterface
from smithy_python._private.retries import SimpleRetryStrategy
from smithy_python.interfaces.retries import RetryStrategy

from ..aws_cryptography_keystore.models import Storage, _storage_from_dict


_ServiceInterceptor = Any


@dataclass(init=False)
class Config:
    """Configuration for KeyStoreAdmin."""

    interceptors: list[_ServiceInterceptor]
    retry_strategy: RetryStrategy
    dafnyImplInterface: DafnyImplInterface | None

    def __init__(
        self,
        *,
        interceptors: list[_ServiceInterceptor] | None = None,
        retry_strategy: RetryStrategy | None = None,
        dafnyImplInterface: DafnyImplInterface | None = None,
    ):
        """Constructor.

        :param interceptors: The list of interceptors, which are hooks
            that are called during the execution of a request.
        :param retry_strategy: The retry strategy for issuing retry
            tokens and computing retry delays.
        :param dafnyImplInterface:
        """
        self.interceptors = interceptors or []
        self.retry_strategy = retry_strategy or SimpleRetryStrategy()
        self.dafnyImplInterface = dafnyImplInterface


# A callable that allows customizing the config object on each request.
Plugin: TypeAlias = Callable[[Config], None]


class KeyStoreAdminConfig(Config):
    logical_key_store_name: str
    storage: Storage

    def __init__(
        self,
        *,
        logical_key_store_name: str,
        storage: Storage,
    ):
        """Constructor for KeyStoreAdminConfig.

        :param logical_key_store_name: The logical name for this Key Store,
          which is
        cryptographically bound to the keys it holds.
          This appears in the Encryption
        Context of KMS requests as `tablename`.

          There SHOULD be a one to one mapping
        between the Storage's physical name,
          i.e: DynamoDB Table Names,
          and the
        Logical KeyStore Name.
          This value can be set to the DynamoDB table name
        itself
          (Storage's physical name),
          but does not need to.

          Controlling this
        value independently enables restoring from DDB table backups
          even when the
        table name after restoration is not exactly the same.
        :param storage: The storage configuration for this Key Store.
        """
        super().__init__()
        self.logical_key_store_name = logical_key_store_name
        self.storage = storage

    def as_dict(self) -> Dict[str, Any]:
        """Converts the KeyStoreAdminConfig to a dictionary."""
        return {
            "logical_key_store_name": self.logical_key_store_name,
            "storage": self.storage.as_dict(),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyStoreAdminConfig":
        """Creates a KeyStoreAdminConfig from a dictionary."""
        kwargs: Dict[str, Any] = {
            "logical_key_store_name": d["logical_key_store_name"],
            "storage": _storage_from_dict(d["storage"]),
        }

        return KeyStoreAdminConfig(**kwargs)

    def __repr__(self) -> str:
        result = "KeyStoreAdminConfig("
        if self.logical_key_store_name is not None:
            result += f"logical_key_store_name={repr(self.logical_key_store_name)}, "

        if self.storage is not None:
            result += f"storage={repr(self.storage)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyStoreAdminConfig):
            return False
        attributes: list[str] = [
            "logical_key_store_name",
            "storage",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


def dafny_config_to_smithy_config(dafny_config) -> KeyStoreAdminConfig:
    """Converts the provided Dafny shape for this localService's config into
    the corresponding Smithy-modelled shape."""
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.dafny_to_smithy.aws_cryptography_keystoreadmin_KeyStoreAdminConfig(
        dafny_config
    )


def smithy_config_to_dafny_config(smithy_config) -> DafnyKeyStoreAdminConfig:
    """Converts the provided Smithy-modelled shape for this localService's
    config into the corresponding Dafny shape."""
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystoreadmin.smithy_to_dafny.aws_cryptography_keystoreadmin_KeyStoreAdminConfig(
        smithy_config
    )
