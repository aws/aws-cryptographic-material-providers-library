# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AwsCryptographyMaterialProvidersTestVectorKeysTypes import (
    KeyVectorsConfig_KeyVectorsConfig as DafnyKeyVectorsConfig,
)
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.module_
import aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy
import aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny
from dataclasses import dataclass
from typing import Any, Callable, TypeAlias

from .dafnyImplInterface import DafnyImplInterface
from smithy_python._private.retries import SimpleRetryStrategy
from smithy_python.interfaces.retries import RetryStrategy


_ServiceInterceptor = Any


@dataclass(init=False)
class Config:
    """Configuration for KeyVectors."""

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


class KeyVectorsConfig(Config):
    """Smithy-modelled localService Config shape for this localService."""

    key_manifest_path: str

    def __init__(
        self,
        key_manifest_path: str,
    ):
        """Constructor for KeyVectorsConfig."""
        super().__init__()
        self.key_manifest_path = key_manifest_path


def dafny_config_to_smithy_config(dafny_config) -> KeyVectorsConfig:
    """Converts the provided Dafny shape for this localService's config into
    the corresponding Smithy-modelled shape."""
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_KeyVectorsConfig(
        dafny_config
    )


def smithy_config_to_dafny_config(smithy_config) -> DafnyKeyVectorsConfig:
    """Converts the provided Smithy-modelled shape for this localService's
    config into the corresponding Dafny shape."""
    return aws_cryptography_materialproviders_test_vectors.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.smithy_to_dafny.aws_cryptography_materialproviderstestvectorkeys_KeyVectorsConfig(
        smithy_config
    )
