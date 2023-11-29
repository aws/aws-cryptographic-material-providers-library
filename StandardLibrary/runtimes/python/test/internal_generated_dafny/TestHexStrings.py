import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import TestUUID
import ConcurrentCall
import TestCallMany
import FloatCompare
import FloatCompareTest
import Relations
import Seq_mMergeSort
import Math
import Seq
import SortedSets
import TestSeqReaderReadElements
import HexStrings

# assert "TestHexStrings" == __name__
TestHexStrings = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BasicTests():
        if not((HexStrings.default__.ToHexString(_dafny.Seq([1, 2, 255]))) == (_dafny.Seq("0102ff"))):
            raise _dafny.HaltException("test/HexStrings.dfy(11,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((HexStrings.default__.FromHexString(_dafny.Seq("0102ff"))) == (_dafny.Seq([1, 2, 255]))):
            raise _dafny.HaltException("test/HexStrings.dfy(12,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

