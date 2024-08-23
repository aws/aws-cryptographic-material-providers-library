import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.UTF8 as UTF8
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import TestUTF8 as TestUTF8
import TestTime as TestTime
import TestComputeSetToOrderedSequenceCharLess as TestComputeSetToOrderedSequenceCharLess

# Module: Sets

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ExtractFromSingleton(s):
        def iife0_(_let_dummy_0):
            d_92_x_: TypeVar('T__') = None
            with _dafny.label("_ASSIGN_SUCH_THAT_d_0"):
                assign_such_that_0_: TypeVar('T__')
                for assign_such_that_0_ in (s).Elements:
                    d_92_x_ = assign_such_that_0_
                    if (d_92_x_) in (s):
                        raise _dafny.Break("_ASSIGN_SUCH_THAT_d_0")
                raise Exception("assign-such-that search produced no value (line 120)")
                pass
            return d_92_x_
        return iife0_(0)
        

    @staticmethod
    def Map(xs, f):
        def iife1_():
            coll0_ = _dafny.Set()
            compr_0_: TypeVar('X__')
            for compr_0_ in (xs).Elements:
                d_94_x_: TypeVar('X__') = compr_0_
                if (d_94_x_) in (xs):
                    coll0_ = coll0_.union(_dafny.Set([f(d_94_x_)]))
            return _dafny.Set(coll0_)
        d_93_ys_ = iife1_()

        return d_93_ys_

    @staticmethod
    def Filter(xs, f):
        def iife2_():
            coll1_ = _dafny.Set()
            compr_1_: TypeVar('X__')
            for compr_1_ in (xs).Elements:
                d_96_x_: TypeVar('X__') = compr_1_
                if ((d_96_x_) in (xs)) and (f(d_96_x_)):
                    coll1_ = coll1_.union(_dafny.Set([d_96_x_]))
            return _dafny.Set(coll1_)
        d_95_ys_ = iife2_()

        return d_95_ys_

    @staticmethod
    def SetRange(a, b):
        d_97___accumulator_ = _dafny.Set({})
        while True:
            with _dafny.label():
                if (a) == (b):
                    return (_dafny.Set({})) | (d_97___accumulator_)
                elif True:
                    d_97___accumulator_ = (d_97___accumulator_) | (_dafny.Set({a}))
                    in0_ = (a) + (1)
                    in1_ = b
                    a = in0_
                    b = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SetRangeZeroBound(n):
        return default__.SetRange(0, n)

