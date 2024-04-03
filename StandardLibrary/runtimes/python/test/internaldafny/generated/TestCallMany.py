import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
import Math
import Seq
import BoundedInts
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibraryInterop
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import TestUTF8
import TestTime
import TestComputeSetToOrderedSequenceCharLess
import Sets
import TestHexStrings
import FloatCompareTest

# Module: TestCallMany

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestBasic():
        d_121_c_: MyCallee
        nw0_ = MyCallee()
        nw0_.ctor__()
        d_121_c_ = nw0_
        ConcurrentCall.default__.ConcurrentCall(d_121_c_, 2, 3)
        if not(((2) <= (d_121_c_.count)) and ((d_121_c_.count) <= (6))):
            raise _dafny.HaltException("test/ConcurrentCall.dfy(45,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))


class MyCallee(ConcurrentCall.Callee):
    def  __init__(self):
        self.count: int = int(0)
        pass

    def __dafnystr__(self) -> str:
        return "TestCallMany.MyCallee"
    def ctor__(self):
        (self).count = 0

    def call(self, serialPos, concurrentPos):
        if (self.count) < (BoundedInts.default__.UINT32__MAX):
            (self).count = (self.count) + (1)

