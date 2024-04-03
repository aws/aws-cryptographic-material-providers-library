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

# Module: TestTime

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestNonDecreasing():
        d_57_t1_: int
        out0_: int
        out0_ = Time.default__.CurrentRelativeTime()
        d_57_t1_ = out0_
        d_58_t2_: int
        out1_: int
        out1_ = Time.default__.CurrentRelativeTime()
        d_58_t2_ = out1_
        if not((d_58_t2_) >= (d_57_t1_)):
            raise _dafny.HaltException("test/Time.dfy(13,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestPositiveValues():
        d_59_t1_: int
        out2_: int
        out2_ = Time.default__.CurrentRelativeTime()
        d_59_t1_ = out2_
        d_60_t2_: int
        out3_: int
        out3_ = Time.default__.CurrentRelativeTime()
        d_60_t2_ = out3_
        if not(((d_60_t2_) - (d_59_t1_)) >= (0)):
            raise _dafny.HaltException("test/Time.dfy(19,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

