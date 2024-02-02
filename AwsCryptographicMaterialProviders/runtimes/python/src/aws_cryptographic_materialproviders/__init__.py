# __init__.py for a Smithy-Dafny generated Python project

# TODO-Python: Remove PYTHONPATH workaround, use fully-qualified module names via dfyproject.toml.
# Import project dependencies.
# TODO-Python-PYTHONPATH: Remove dependency imports to initialize PYTHONPATH with their modules

from . import internaldafny
import standard_library
import com_amazonaws_kms
import com_amazonaws_dynamodb
import aws_cryptography_primitives

# Add internaldafny code to PYTHONPATH (TODO-Python-PYTHONPATH: Remove)
import sys

module_root_dir = '/'.join(__file__.split("/")[:-1])

sys.path.append(module_root_dir + "/internaldafny/extern")
sys.path.append(module_root_dir + "/internaldafny/generated")

# Export user-friendly access paths
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders as mpl
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders as keystore

__all__ = [
    mpl,
    keystore
]