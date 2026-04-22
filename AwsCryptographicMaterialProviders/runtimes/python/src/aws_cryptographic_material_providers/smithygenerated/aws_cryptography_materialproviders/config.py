# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes import (
    MaterialProvidersConfig_MaterialProvidersConfig as DafnyMaterialProvidersConfig,
)
import aws_cryptographic_material_providers.internaldafny.generated.module_
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny
from dataclasses import dataclass
from typing import Any, Callable, Dict, TypeAlias

from .dafnyImplInterface import DafnyImplInterface
from smithy_python._private.retries import SimpleRetryStrategy
from smithy_python.interfaces.retries import RetryStrategy


_ServiceInterceptor = Any


@dataclass(init=False)
class Config:
    """Configuration for AwsCryptographicMaterialProviders."""

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


class MaterialProvidersConfig(Config):
    def __init__(
        self,
    ):
        """Constructor for MaterialProvidersConfig."""
        super().__init__()

    def as_dict(self) -> Dict[str, Any]:
        """Converts the MaterialProvidersConfig to a dictionary."""
        return {}

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MaterialProvidersConfig":
        """Creates a MaterialProvidersConfig from a dictionary."""
        return MaterialProvidersConfig()

    def __repr__(self) -> str:
        result = "MaterialProvidersConfig("

        return result + ")"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, MaterialProvidersConfig)


def dafny_config_to_smithy_config(dafny_config) -> MaterialProvidersConfig:
    """Converts the provided Dafny shape for this localService's config into
    the corresponding Smithy-modelled shape."""
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_MaterialProvidersConfig(
        dafny_config
    )


def smithy_config_to_dafny_config(smithy_config) -> DafnyMaterialProvidersConfig:
    """Converts the provided Smithy-modelled shape for this localService's
    config into the corresponding Dafny shape."""
    return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_MaterialProvidersConfig(
        smithy_config
    )
