# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes import (
    KeyStoreConfig_KeyStoreConfig as DafnyKeyStoreConfig,
)
import aws_cryptographic_material_providers.internaldafny.generated.module_
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny
from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional, TypeAlias

from .dafnyImplInterface import DafnyImplInterface
from botocore.client import BaseClient
from smithy_python._private.retries import SimpleRetryStrategy
from smithy_python.interfaces.retries import RetryStrategy

from .models import KMSConfiguration, _kms_configuration_from_dict


_ServiceInterceptor = Any


@dataclass(init=False)
class Config:
    """Configuration for KeyStore."""

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


class KeyStoreConfig(Config):
    ddb_table_name: dict[str, Any]
    kms_configuration: KMSConfiguration
    logical_key_store_name: str
    id: Optional[str]
    grant_tokens: Optional[list[str]]
    ddb_client: Optional[BaseClient]
    kms_client: Optional[BaseClient]

    def __init__(
        self,
        *,
        ddb_table_name: dict[str, Any],
        kms_configuration: KMSConfiguration,
        logical_key_store_name: str,
        id: Optional[str] = None,
        grant_tokens: Optional[list[str]] = None,
        ddb_client: Optional[BaseClient] = None,
        kms_client: Optional[BaseClient] = None,
    ):
        """Constructor for KeyStoreConfig.

        :param ddb_table_name: The DynamoDB table name that backs this Key Store.
        :param kms_configuration: Configures Key Store's KMS Key ARN restrictions.
        :param logical_key_store_name: The logical name for this Key Store, which is
        cryptographically bound to the keys it holds. This appears in the Encryption
        Context of KMS requests as `tablename`.
        :param id: An identifier for this Key Store.
        :param grant_tokens: The AWS KMS grant tokens that are used when this Key Store
        calls to AWS KMS.
        :param ddb_client: The DynamoDB client this Key Store uses to call Amazon
        DynamoDB. If None is provided and the KMS ARN is, the KMS ARN is used to
        determine the Region of the default client.
        :param kms_client: The KMS client this Key Store uses to call AWS KMS.  If None
        is provided and the KMS ARN is, the KMS ARN is used to determine the Region of
        the default client.
        """
        super().__init__()
        if (ddb_table_name is not None) and (len(ddb_table_name) < 3):
            raise ValueError(
                "The size of ddb_table_name must be greater than or equal to 3"
            )

        if (ddb_table_name is not None) and (len(ddb_table_name) > 255):
            raise ValueError(
                "The size of ddb_table_name must be less than or equal to 255"
            )

        self.ddb_table_name = ddb_table_name
        self.kms_configuration = kms_configuration
        self.logical_key_store_name = logical_key_store_name
        self.id = id
        self.grant_tokens = grant_tokens
        self.ddb_client = ddb_client
        self.kms_client = kms_client

    def as_dict(self) -> Dict[str, Any]:
        """Converts the KeyStoreConfig to a dictionary."""
        d: Dict[str, Any] = {
            "ddb_table_name": self.ddb_table_name,
            "kms_configuration": self.kms_configuration.as_dict(),
            "logical_key_store_name": self.logical_key_store_name,
        }

        if self.id is not None:
            d["id"] = self.id

        if self.grant_tokens is not None:
            d["grant_tokens"] = self.grant_tokens

        if self.ddb_client is not None:
            d["ddb_client"] = self.ddb_client

        if self.kms_client is not None:
            d["kms_client"] = self.kms_client

        return d

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyStoreConfig":
        """Creates a KeyStoreConfig from a dictionary."""
        kwargs: Dict[str, Any] = {
            "ddb_table_name": d["ddb_table_name"],
            "kms_configuration": _kms_configuration_from_dict(d["kms_configuration"]),
            "logical_key_store_name": d["logical_key_store_name"],
        }

        if "id" in d:
            kwargs["id"] = d["id"]

        if "grant_tokens" in d:
            kwargs["grant_tokens"] = d["grant_tokens"]

        if "ddb_client" in d:
            kwargs["ddb_client"] = d["ddb_client"]

        if "kms_client" in d:
            kwargs["kms_client"] = d["kms_client"]

        return KeyStoreConfig(**kwargs)

    def __repr__(self) -> str:
        result = "KeyStoreConfig("
        if self.ddb_table_name is not None:
            result += f"ddb_table_name={repr(self.ddb_table_name)}, "

        if self.kms_configuration is not None:
            result += f"kms_configuration={repr(self.kms_configuration)}, "

        if self.logical_key_store_name is not None:
            result += f"logical_key_store_name={repr(self.logical_key_store_name)}, "

        if self.id is not None:
            result += f"id={repr(self.id)}, "

        if self.grant_tokens is not None:
            result += f"grant_tokens={repr(self.grant_tokens)}, "

        if self.ddb_client is not None:
            result += f"ddb_client={repr(self.ddb_client)}, "

        if self.kms_client is not None:
            result += f"kms_client={repr(self.kms_client)}"

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KeyStoreConfig):
            return False
        attributes: list[str] = [
            "ddb_table_name",
            "kms_configuration",
            "logical_key_store_name",
            "id",
            "grant_tokens",
            "ddb_client",
            "kms_client",
        ]
        return all(getattr(self, a) == getattr(other, a) for a in attributes)


def dafny_config_to_smithy_config(dafny_config) -> KeyStoreConfig:
    """Converts the provided Dafny shape for this localService's config into
    the corresponding Smithy-modelled shape."""
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_KeyStoreConfig(
        dafny_config
    )


def smithy_config_to_dafny_config(smithy_config) -> DafnyKeyStoreConfig:
    """Converts the provided Smithy-modelled shape for this localService's
    config into the corresponding Dafny shape."""
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_KeyStoreConfig(
        smithy_config
    )
