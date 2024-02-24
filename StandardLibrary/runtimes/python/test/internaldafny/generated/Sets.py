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
import DafnyLibraries
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
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import TestUTF8
import TestTime
import TestComputeSetToOrderedSequenceCharLess

# Module: Sets

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ExtractFromSingleton(s):
        def iife0_(_let_dummy_0):
            d_90_x_: TypeVar('T__') = None
            with _dafny.label("_ASSIGN_SUCH_THAT_d_0"):
                assign_such_that_0_: TypeVar('T__')
                for assign_such_that_0_ in (s).Elements:
                    d_90_x_ = assign_such_that_0_
                    if (d_90_x_) in (s):
                        raise _dafny.Break("_ASSIGN_SUCH_THAT_d_0")
                raise Exception("assign-such-that search produced no value (line 120)")
                pass
            return d_90_x_
        return iife0_(0)
        

    @staticmethod
    def Map(xs, f):
        def iife1_():
            coll0_ = _dafny.Set()
            compr_0_: TypeVar('X__')
            for compr_0_ in (xs).Elements:
                d_92_x_: TypeVar('X__') = compr_0_
                if (d_92_x_) in (xs):
                    coll0_ = coll0_.union(_dafny.Set([f(d_92_x_)]))
            return _dafny.Set(coll0_)
        d_91_ys_ = iife1_()

        return d_91_ys_

    @staticmethod
    def Filter(xs, f):
        def iife2_():
            coll1_ = _dafny.Set()
            compr_1_: TypeVar('X__')
            for compr_1_ in (xs).Elements:
                d_94_x_: TypeVar('X__') = compr_1_
                if ((d_94_x_) in (xs)) and (f(d_94_x_)):
                    coll1_ = coll1_.union(_dafny.Set([d_94_x_]))
            return _dafny.Set(coll1_)
        d_93_ys_ = iife2_()

        return d_93_ys_

    @staticmethod
    def SetRange(a, b):
        d_95___accumulator_ = _dafny.Set({})
        while True:
            with _dafny.label():
                if (a) == (b):
                    return (_dafny.Set({})) | (d_95___accumulator_)
                elif True:
                    d_95___accumulator_ = (d_95___accumulator_) | (_dafny.Set({a}))
                    in0_ = (a) + (1)
                    in1_ = b
                    a = in0_
                    b = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SetRangeZeroBound(n):
        return default__.SetRange(0, n)

