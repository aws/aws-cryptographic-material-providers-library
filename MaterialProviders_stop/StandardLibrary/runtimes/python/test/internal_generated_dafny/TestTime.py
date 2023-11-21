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
import TestHexStrings
import Time

assert "TestTime" == __name__
TestTime = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestNonDecreasing():
        d_78_t1_: BoundedInts.int64
        out8_: BoundedInts.int64
        out8_ = Time.default__.CurrentRelativeTime()
        d_78_t1_ = out8_
        d_79_t2_: BoundedInts.int64
        out9_: BoundedInts.int64
        out9_ = Time.default__.CurrentRelativeTime()
        d_79_t2_ = out9_
        if not((d_79_t2_) >= (d_78_t1_)):
            raise _dafny.HaltException("test/Time.dfy(13,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestPositiveValues():
        d_80_t1_: BoundedInts.int64
        out10_: BoundedInts.int64
        out10_ = Time.default__.CurrentRelativeTime()
        d_80_t1_ = out10_
        d_81_t2_: BoundedInts.int64
        out11_: BoundedInts.int64
        out11_ = Time.default__.CurrentRelativeTime()
        d_81_t2_ = out11_
        if not(((d_81_t2_) - (d_80_t1_)) >= (0)):
            raise _dafny.HaltException("test/Time.dfy(19,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

