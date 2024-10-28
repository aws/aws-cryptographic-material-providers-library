# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes import (
    CryptoConfig_CryptoConfig as DafnyCryptoConfig,
)
import aws_cryptography_primitives.internaldafny.generated.module_
import aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy
import aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny
from dataclasses import dataclass
from typing import Any, Callable, Dict, TypeAlias

from .dafnyImplInterface import DafnyImplInterface
from smithy_python._private.retries import SimpleRetryStrategy
from smithy_python.interfaces.retries import RetryStrategy


_ServiceInterceptor = Any


@dataclass(init=False)
class Config:
    """Configuration for AwsCryptographicPrimitives."""

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


class CryptoConfig(Config):
    def __init__(
        self,
    ):
        """Constructor for CryptoConfig."""
        super().__init__()

    def as_dict(self) -> Dict[str, Any]:
        """Converts the CryptoConfig to a dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CryptoConfig":
        """Creates a CryptoConfig from a dictionary."""
        return CryptoConfig()

    def __repr__(self) -> str:
        result = "CryptoConfig("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, CryptoConfig)


def dafny_config_to_smithy_config(dafny_config) -> CryptoConfig:
    """Converts the provided Dafny shape for this localService's config into
    the corresponding Smithy-modelled shape."""
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_CryptoConfig(
        dafny_config
    )


def smithy_config_to_dafny_config(smithy_config) -> DafnyCryptoConfig:
    """Converts the provided Smithy-modelled shape for this localService's
    config into the corresponding Dafny shape."""
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_CryptoConfig(
        smithy_config
    )
