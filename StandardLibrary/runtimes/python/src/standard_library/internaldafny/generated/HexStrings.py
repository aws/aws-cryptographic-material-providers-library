import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import standard_library.internaldafny.generated.module_ as module_
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
        def lambda21_(forall_var_3_):
            d_267_ch_: str = forall_var_3_
            return not ((d_267_ch_) in (s)) or (default__.IsHexChar(d_267_ch_))

        return _dafny.quantifier((s).UniqueElements, True, lambda21_)

    @staticmethod
    def IsLooseHexString(s):
        def lambda22_(forall_var_4_):
            d_268_ch_: str = forall_var_4_
            return not ((d_268_ch_) in (s)) or (default__.IsLooseHexChar(d_268_ch_))

        return _dafny.quantifier((s).UniqueElements, True, lambda22_)

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
            d_269_res_ = _dafny.Seq(['0', default__.HexChar(x)])
            return d_269_res_
        elif True:
            d_270_res_ = _dafny.Seq([default__.HexChar(_dafny.euclidian_division(x, 16)), default__.HexChar(_dafny.euclidian_modulus(x, 16))])
            return d_270_res_

    @staticmethod
    def HexValue(x):
        return ((default__.HexVal((x)[0])) * (16)) + (default__.HexVal((x)[1]))

    @staticmethod
    def ToHexString(val):
        d_271___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(val)) == (0):
                    return (d_271___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_271___accumulator_ = (d_271___accumulator_) + (default__.HexStr((val)[0]))
                    in66_ = _dafny.Seq((val)[1::])
                    val = in66_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FromHexString(data):
        d_272___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(data)) == (0):
                    return (d_272___accumulator_) + (_dafny.Seq([]))
                elif (_dafny.euclidian_modulus(len(data), 2)) == (1):
                    d_272___accumulator_ = (d_272___accumulator_) + (_dafny.Seq([default__.HexVal((data)[0])]))
                    in67_ = _dafny.Seq((data)[1::])
                    data = in67_
                    raise _dafny.TailCall()
                elif True:
                    d_272___accumulator_ = (d_272___accumulator_) + (_dafny.Seq([default__.HexValue(_dafny.Seq((data)[:2:]))]))
                    in68_ = _dafny.Seq((data)[2::])
                    data = in68_
                    raise _dafny.TailCall()
                break


class HexString:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_273_x_: _dafny.Seq = source__
        return default__.IsHexString(d_273_x_)

class LooseHexString:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_274_x_: _dafny.Seq = source__
        return default__.IsLooseHexString(d_274_x_)
