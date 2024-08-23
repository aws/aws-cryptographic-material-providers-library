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

    @staticmethod
    def TestGetCurrentTimeStamp():
        d_61_CurrentTime_: _dafny.Seq
        d_62_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out4_: Wrappers.Result
        out4_ = Time.default__.GetCurrentTimeStamp()
        d_62_valueOrError0_ = out4_
        if not(not((d_62_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/Time.dfy(24,23): " + _dafny.string_of(d_62_valueOrError0_))
        d_61_CurrentTime_ = (d_62_valueOrError0_).Extract()
        if not(default__.ISO8601_q(d_61_CurrentTime_)):
            raise _dafny.HaltException("test/Time.dfy(25,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def ISO8601_q(CreateTime):
        return ((((((((len(CreateTime)) == (27)) and (((CreateTime)[4]) == ('-'))) and (((CreateTime)[7]) == ('-'))) and (((CreateTime)[10]) == ('T'))) and (((CreateTime)[13]) == (':'))) and (((CreateTime)[16]) == (':'))) and (((CreateTime)[19]) == ('.'))) and (((CreateTime)[26]) == ('Z'))

