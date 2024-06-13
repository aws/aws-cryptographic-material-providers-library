"""
Wrapper file for executing Dafny tests from pytest.
This allows us to import modules required by Dafny-generated tests
before executing Dafny-generated tests.
pytest will find and execute the `test_dafny` method below,
which will execute the `internaldafny_test_executor.py` file in the `dafny` directory.
"""

import sys

internaldafny_dir = '/'.join(__file__.split("/")[:-1])

sys.path.append(internaldafny_dir + "/extern")
sys.path.append(internaldafny_dir + "/generated")

# Override the StormTracker implementation to allow fanOut>1 ONLY for Dafny tests.
# fanOut is enforced to be 1 as fanOut>1 will use boto3 in multiple threads.
# boto3 is not thread safe, so this is not OK.
# However, the generated Dafny tests do not use boto3.
import aws_cryptographic_materialproviders.internaldafny.extern.StormTrackerEnforcesOneFanOut as StormTrackerEnforcesOneFanOutExtern
StormTrackerEnforcesOneFanOutExtern.StormTracker.ctor__ = StormTrackerEnforcesOneFanOutExtern.StormTracker.base_ctor

def test_dafny():
  from .generated import __main__