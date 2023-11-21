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
import StandardLibrary
import UTF8
import TestUTF8
import Time
import TestTime
import HexStrings
import TestHexStrings
import Relations
import Seq_mMergeSort
import Math
import Seq
import SortedSets
import TestSeqReaderReadElements
import Functions
import Sets
import FloatCompare
import FloatCompareTest
import ConcurrentCall

assert "TestCallMany" == __name__
TestCallMany = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestBasic():
        d_241_c_: TestCallMany.MyCallee
        nw2_ = TestCallMany.MyCallee()
        nw2_.ctor__()
        d_241_c_ = nw2_
        ConcurrentCall.default__.ConcurrentCall(d_241_c_, 2, 3)
        if not((d_241_c_.count) == (6)):
            raise _dafny.HaltException("test/ConcurrentCall.dfy(43,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))


class MyCallee(ConcurrentCall.Callee):
    def  __init__(self):
        self.count: BoundedInts.uint32 = int(0)
        pass

    def __dafnystr__(self) -> str:
        return "TestCallMany.MyCallee"
    def ctor__(self):
        (self).count = 0

    def call(self, serialPos, concurrentPos):
        if (self.count) < ((BoundedInts.default__).UINT32__MAX):
            (self).count = (self.count) + (1)

