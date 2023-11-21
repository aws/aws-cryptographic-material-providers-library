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

assert "TestTime" == __name__
TestTime = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestNonDecreasing():
        d_130_t1_: BoundedInts.int64
        out0_: BoundedInts.int64
        out0_ = Time.default__.CurrentRelativeTime()
        d_130_t1_ = out0_
        d_131_t2_: BoundedInts.int64
        out1_: BoundedInts.int64
        out1_ = Time.default__.CurrentRelativeTime()
        d_131_t2_ = out1_
        if not((d_131_t2_) >= (d_130_t1_)):
            raise _dafny.HaltException("test/Time.dfy(13,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestPositiveValues():
        d_132_t1_: BoundedInts.int64
        out2_: BoundedInts.int64
        out2_ = Time.default__.CurrentRelativeTime()
        d_132_t1_ = out2_
        d_133_t2_: BoundedInts.int64
        out3_: BoundedInts.int64
        out3_ = Time.default__.CurrentRelativeTime()
        d_133_t2_ = out3_
        if not(((d_133_t2_) - (d_132_t1_)) >= (0)):
            raise _dafny.HaltException("test/Time.dfy(19,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

