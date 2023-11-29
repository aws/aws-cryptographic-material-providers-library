import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers

# assert "Relations" == __name__
Relations = sys.modules[__name__]

