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

# assert "TestCallMany" == __name__
TestCallMany = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestBasic():
        d_28_c_: TestCallMany.MyCallee
        nw0_ = TestCallMany.MyCallee()
        nw0_.ctor__()
        d_28_c_ = nw0_
        ConcurrentCall.default__.ConcurrentCall(d_28_c_, 2, 3)
        if not((d_28_c_.count) == (6)):
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

