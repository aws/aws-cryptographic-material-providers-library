# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes import (
    KeyStoreConfig_KeyStoreConfig as DafnyKeyStoreConfig,
)
import aws_cryptographic_materialproviders.internaldafny.generated.module_
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny
from dataclasses import dataclass
from typing import Any, Callable, Optional, TypeAlias

from .dafnyImplInterface import DafnyImplInterface
from botocore.client import BaseClient
from smithy_python._private.retries import SimpleRetryStrategy
from smithy_python.interfaces.retries import RetryStrategy

from .models import KMSConfiguration


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
    """Smithy-modelled localService Config shape for this localService."""

    ddb_table_name: str
    kms_configuration: KMSConfiguration
    logical_key_store_name: str
    id: Optional[str]
    grant_tokens: Optional[list[str]]
    ddb_client: Optional[BaseClient]
    kms_client: Optional[BaseClient]

    def __init__(
        self,
        ddb_table_name: str,
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
        self.ddb_table_name = ddb_table_name
        self.kms_configuration = kms_configuration
        self.logical_key_store_name = logical_key_store_name
        self.id = id
        self.grant_tokens = grant_tokens
        self.ddb_client = ddb_client
        self.kms_client = kms_client


def dafny_config_to_smithy_config(dafny_config) -> KeyStoreConfig:
    """Converts the provided Dafny shape for this localService's config into
    the corresponding Smithy-modelled shape."""
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_KeyStoreConfig(
        dafny_config
    )


def smithy_config_to_dafny_config(smithy_config) -> DafnyKeyStoreConfig:
    """Converts the provided Smithy-modelled shape for this localService's
    config into the corresponding Dafny shape."""
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_KeyStoreConfig(
        smithy_config
    )
