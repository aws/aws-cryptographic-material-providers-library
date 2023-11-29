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
import TestTime
import UTF8
import TestUTF8
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
import Streams
import Sorting
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries

# assert "Sets" == __name__
Sets = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ExtractFromSingleton(s):
        def iife1_(_let_dummy_0):
            d_139_x_: TypeVar('T__') = None
            with _dafny.label("_ASSIGN_SUCH_THAT_d_0"):
                assign_such_that_0_: TypeVar('T__')
                for assign_such_that_0_ in (s).Elements:
                    d_139_x_ = assign_such_that_0_
                    if (d_139_x_) in (s):
                        raise _dafny.Break("_ASSIGN_SUCH_THAT_d_0")
                raise Exception("assign-such-that search produced no value (line 120)")
                pass
            return d_139_x_
        return iife1_(0)
        

    @staticmethod
    def Map(xs, f):
        def iife2_():
            coll1_ = _dafny.Set()
            compr_1_: TypeVar('X__')
            for compr_1_ in (xs).Elements:
                d_141_x_: TypeVar('X__') = compr_1_
                if (d_141_x_) in (xs):
                    coll1_ = coll1_.union(_dafny.Set([f(d_141_x_)]))
            return _dafny.Set(coll1_)
        d_140_ys_ = iife2_()

        return d_140_ys_

    @staticmethod
    def Filter(xs, f):
        def iife3_():
            coll2_ = _dafny.Set()
            compr_2_: TypeVar('X__')
            for compr_2_ in (xs).Elements:
                d_143_x_: TypeVar('X__') = compr_2_
                if ((d_143_x_) in (xs)) and (f(d_143_x_)):
                    coll2_ = coll2_.union(_dafny.Set([d_143_x_]))
            return _dafny.Set(coll2_)
        d_142_ys_ = iife3_()

        return d_142_ys_

    @staticmethod
    def SetRange(a, b):
        d_144___accumulator_ = _dafny.Set({})
        while True:
            with _dafny.label():
                if (a) == (b):
                    return (_dafny.Set({})) | (d_144___accumulator_)
                elif True:
                    d_144___accumulator_ = (d_144___accumulator_) | (_dafny.Set({a}))
                    in0_ = (a) + (1)
                    in1_ = b
                    a = in0_
                    b = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SetRangeZeroBound(n):
        return Sets.default__.SetRange(0, n)

