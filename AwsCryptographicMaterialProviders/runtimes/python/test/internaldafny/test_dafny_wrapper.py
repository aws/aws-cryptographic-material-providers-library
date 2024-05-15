"""
Wrapper file for executing Dafny tests from pytest.
This allows us to import modules required by Dafny-generated tests
before executing Dafny-generated tests.
pytest will find and execute the `test_dafny` method below,
which will execute the `internaldafny_test_executor.py` file in the `dafny` directory.
"""

# TODO-Python-PYTHONPATH: Remove all sys.path.append logic from this file
import sys

internaldafny_dir = '/'.join(__file__.split("/")[:-1])

sys.path.append(internaldafny_dir + "/extern")
sys.path.append(internaldafny_dir + "/generated")

def test_dafny():
  # Dafny tests are executed when importing `internaldafny_test_executor`
  # TODO-Python-PYTHONPATH: Qualify import
  from .generated import __main__