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
            d_250_ch_: str = forall_var_3_
            return not ((d_250_ch_) in (s)) or (default__.IsHexChar(d_250_ch_))

        return _dafny.quantifier((s).UniqueElements, True, lambda21_)

    @staticmethod
    def IsLooseHexString(s):
        def lambda22_(forall_var_4_):
            d_251_ch_: str = forall_var_4_
            return not ((d_251_ch_) in (s)) or (default__.IsLooseHexChar(d_251_ch_))

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
            d_252_res_ = _dafny.Seq(['0', default__.HexChar(x)])
            return d_252_res_
        elif True:
            d_253_res_ = _dafny.Seq([default__.HexChar(_dafny.euclidian_division(x, 16)), default__.HexChar(_dafny.euclidian_modulus(x, 16))])
            return d_253_res_

    @staticmethod
    def HexValue(x):
        return ((default__.HexVal((x)[0])) * (16)) + (default__.HexVal((x)[1]))

    @staticmethod
    def ToHexString(val):
        d_254___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(val)) == (0):
                    return (d_254___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_254___accumulator_ = (d_254___accumulator_) + (default__.HexStr((val)[0]))
                    in66_ = _dafny.Seq((val)[1::])
                    val = in66_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FromHexString(data):
        d_255___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(data)) == (0):
                    return (d_255___accumulator_) + (_dafny.Seq([]))
                elif (_dafny.euclidian_modulus(len(data), 2)) == (1):
                    d_255___accumulator_ = (d_255___accumulator_) + (_dafny.Seq([default__.HexVal((data)[0])]))
                    in67_ = _dafny.Seq((data)[1::])
                    data = in67_
                    raise _dafny.TailCall()
                elif True:
                    d_255___accumulator_ = (d_255___accumulator_) + (_dafny.Seq([default__.HexValue(_dafny.Seq((data)[:2:]))]))
                    in68_ = _dafny.Seq((data)[2::])
                    data = in68_
                    raise _dafny.TailCall()
                break


class HexString:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})

class LooseHexString:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
