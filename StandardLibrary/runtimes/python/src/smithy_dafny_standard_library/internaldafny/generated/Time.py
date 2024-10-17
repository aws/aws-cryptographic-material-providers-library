import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import smithy_dafny_standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8

# Module: Time

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def FormatMilli(diff):
        d_0_whole_ = StandardLibrary_String.default__.Base10Int2String(_dafny.euclidian_division(diff, 1000))
        d_1_frac_ = StandardLibrary_String.default__.Base10Int2String(_dafny.euclidian_modulus(diff, 1000))
        if (len(d_1_frac_)) == (1):
            return ((d_0_whole_) + (_dafny.Seq(".00"))) + (d_1_frac_)
        elif (len(d_1_frac_)) == (2):
            return ((d_0_whole_) + (_dafny.Seq(".0"))) + (d_1_frac_)
        elif True:
            return ((d_0_whole_) + (_dafny.Seq("."))) + (d_1_frac_)

    @staticmethod
    def FormatMilliDiff(start, end):
        if (start) <= (end):
            return default__.FormatMilli((end) - (start))
        elif True:
            return (_dafny.Seq("-")) + (default__.FormatMilli((start) - (end)))

    @staticmethod
    def CreateGetCurrentTimeStampSuccess(value):
        return Wrappers.Result_Success(value)

    @staticmethod
    def CreateGetCurrentTimeStampFailure(error):
        return Wrappers.Result_Failure(error)

