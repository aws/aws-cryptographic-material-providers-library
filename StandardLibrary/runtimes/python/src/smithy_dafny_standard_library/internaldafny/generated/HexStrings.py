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
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets

# Module: HexStrings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def HexChar(x):
        if (x) < (10):
            return _dafny.plus_char('0', chr(x))
        elif True:
            return _dafny.plus_char('a', chr((x) - (10)))

    @staticmethod
    def IsLooseHexChar(ch):
        return (((('0') <= (ch)) and ((ch) <= ('9'))) or ((('a') <= (ch)) and ((ch) <= ('f')))) or ((('A') <= (ch)) and ((ch) <= ('F')))

    @staticmethod
    def IsHexChar(ch):
        return ((('0') <= (ch)) and ((ch) <= ('9'))) or ((('a') <= (ch)) and ((ch) <= ('f')))

    @staticmethod
    def IsHexString(s):
        def lambda0_(forall_var_0_):
            d_0_ch_: str = forall_var_0_
            return not ((d_0_ch_) in (s)) or (default__.IsHexChar(d_0_ch_))

        return _dafny.quantifier((s).UniqueElements, True, lambda0_)

    @staticmethod
    def IsLooseHexString(s):
        def lambda0_(forall_var_0_):
            d_0_ch_: str = forall_var_0_
            return not ((d_0_ch_) in (s)) or (default__.IsLooseHexChar(d_0_ch_))

        return _dafny.quantifier((s).UniqueElements, True, lambda0_)

    @staticmethod
    def HexVal(ch):
        if (('0') <= (ch)) and ((ch) <= ('9')):
            return (ord(ch)) - (ord('0'))
        elif (('a') <= (ch)) and ((ch) <= ('f')):
            return ((ord(ch)) - (ord('a'))) + (10)
        elif True:
            return ((ord(ch)) - (ord('A'))) + (10)

    @staticmethod
    def HexStr(x):
        if (x) < (16):
            d_0_res_ = _dafny.Seq(['0', default__.HexChar(x)])
            return d_0_res_
        elif True:
            d_1_res_ = _dafny.Seq([default__.HexChar(_dafny.euclidian_division(x, 16)), default__.HexChar(_dafny.euclidian_modulus(x, 16))])
            return d_1_res_

    @staticmethod
    def HexValue(x):
        return ((default__.HexVal((x)[0])) * (16)) + (default__.HexVal((x)[1]))

    @staticmethod
    def ToHexString(val):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(val)) == (0):
                    return (d_0___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (default__.HexStr((val)[0]))
                    in0_ = _dafny.Seq((val)[1::])
                    val = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FromHexString(data):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(data)) == (0):
                    return (d_0___accumulator_) + (_dafny.Seq([]))
                elif (_dafny.euclidian_modulus(len(data), 2)) == (1):
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.Seq([default__.HexVal((data)[0])]))
                    in0_ = _dafny.Seq((data)[1::])
                    data = in0_
                    raise _dafny.TailCall()
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.Seq([default__.HexValue(_dafny.Seq((data)[:2:]))]))
                    in1_ = _dafny.Seq((data)[2::])
                    data = in1_
                    raise _dafny.TailCall()
                break


class HexString:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_0_x_: _dafny.Seq = source__
        return default__.IsHexString(d_0_x_)

class LooseHexString:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_1_x_: _dafny.Seq = source__
        return default__.IsLooseHexString(d_1_x_)
