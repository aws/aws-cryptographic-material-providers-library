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

# Module: StandardLibrary_String

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Int2Digits(n, base):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (n) == (0):
                    return (_dafny.Seq([])) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (_dafny.Seq([_dafny.euclidian_modulus(n, base)])) + (d_0___accumulator_)
                    in0_ = _dafny.euclidian_division(n, base)
                    in1_ = base
                    n = in0_
                    base = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Digits2String(digits, chars):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (digits) == (_dafny.Seq([])):
                    return (d_0___accumulator_) + (_dafny.Seq(""))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.Seq([(chars)[(digits)[0]]]))
                    in0_ = _dafny.Seq((digits)[1::])
                    in1_ = chars
                    digits = in0_
                    chars = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Int2String(n, chars):
        d_0_base_ = len(chars)
        if (n) == (0):
            return _dafny.Seq("0")
        elif (n) > (0):
            return default__.Digits2String(default__.Int2Digits(n, d_0_base_), chars)
        elif True:
            return (_dafny.Seq("-")) + (default__.Digits2String(default__.Int2Digits((0) - (n), d_0_base_), chars))

    @staticmethod
    def Base10Int2String(n):
        return default__.Int2String(n, default__.Base10)

    @_dafny.classproperty
    def Base10(instance):
        return _dafny.Seq(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
