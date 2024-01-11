import sys

"""
Wrapper file for executing Dafny tests from pytest.
This allows us to import modules required by Dafny-generated tests
before executing Dafny-generated tests.
pytest will find and execute the `test_dafny` method below,
which will execute the `test.py` file in the `dafny` directory.
"""

internaldafny_dir = '/'.join(__file__.split("/")[:-1])

sys.path.append(internaldafny_dir + "/extern")
sys.path.append(internaldafny_dir + "/generated")

# Import modules required for Dafny-generated tests.
# This is not generated; these must be manually added.

import aws_cryptographic_materialproviders
# import aws_cryptography_primitives
# print(f"{sys.path=}")
from aws_cryptography_materialproviderstestvectorkeys.internaldafny.extern import wrapped_mpl

# End import modules required for Dafny-generated tests



def test_dafny():
  # Dafny tests are executed when importing `internaldafny_test_executor`
  import internaldafny_test_executor