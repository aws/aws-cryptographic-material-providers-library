# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# Initialize generated Dafny
from .internaldafny.generated import module_

# Initialize externs
from .internaldafny import extern

# If this is the first Dafny module_ to load,
# set this as the main module for the DafnyRuntime package
try:
    import module_
except ImportError:
    import sys
    sys.modules["module_"] = module_

# Export user-friendly access paths
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders as mpl
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders as keystore

__all__ = [
    mpl,
    keystore
]