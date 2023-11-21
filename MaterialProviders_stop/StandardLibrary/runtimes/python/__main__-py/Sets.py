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

assert "Sets" == __name__
Sets = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ExtractFromSingleton(s):
        def iife3_(_let_dummy_1):
            d_193_x_: TypeVar('T__') = None
            with _dafny.label("_ASSIGN_SUCH_THAT_d_2"):
                assign_such_that_2_: TypeVar('T__')
                for assign_such_that_2_ in (s).Elements:
                    d_193_x_ = assign_such_that_2_
                    if (d_193_x_) in (s):
                        raise _dafny.Break("_ASSIGN_SUCH_THAT_d_2")
                raise Exception("assign-such-that search produced no value (line 120)")
                pass
            return d_193_x_
        return iife3_(0)
        

    @staticmethod
    def Map(xs, f):
        def iife4_():
            coll2_ = _dafny.Set()
            compr_2_: TypeVar('X__')
            for compr_2_ in (xs).Elements:
                d_195_x_: TypeVar('X__') = compr_2_
                if (d_195_x_) in (xs):
                    coll2_ = coll2_.union(_dafny.Set([f(d_195_x_)]))
            return _dafny.Set(coll2_)
        d_194_ys_ = iife4_()

        return d_194_ys_

    @staticmethod
    def Filter(xs, f):
        def iife5_():
            coll3_ = _dafny.Set()
            compr_3_: TypeVar('X__')
            for compr_3_ in (xs).Elements:
                d_197_x_: TypeVar('X__') = compr_3_
                if ((d_197_x_) in (xs)) and (f(d_197_x_)):
                    coll3_ = coll3_.union(_dafny.Set([d_197_x_]))
            return _dafny.Set(coll3_)
        d_196_ys_ = iife5_()

        return d_196_ys_

    @staticmethod
    def SetRange(a, b):
        d_198___accumulator_ = _dafny.Set({})
        while True:
            with _dafny.label():
                if (a) == (b):
                    return (_dafny.Set({})) | (d_198___accumulator_)
                elif True:
                    d_198___accumulator_ = (d_198___accumulator_) | (_dafny.Set({a}))
                    in51_ = (a) + (1)
                    in52_ = b
                    a = in51_
                    b = in52_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SetRangeZeroBound(n):
        return Sets.default__.SetRange(0, n)

