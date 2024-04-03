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
import StandardLibraryInterop
import StandardLibrary_UInt

# Module: StandardLibrary_String

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Int2Digits(n, base):
        d_223___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (n) == (0):
                    return (_dafny.Seq([])) + (d_223___accumulator_)
                elif True:
                    d_223___accumulator_ = (_dafny.Seq([_dafny.euclidian_modulus(n, base)])) + (d_223___accumulator_)
                    in38_ = _dafny.euclidian_division(n, base)
                    in39_ = base
                    n = in38_
                    base = in39_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Digits2String(digits, chars):
        d_224___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (digits) == (_dafny.Seq([])):
                    return (d_224___accumulator_) + (_dafny.Seq(""))
                elif True:
                    d_224___accumulator_ = (d_224___accumulator_) + (_dafny.Seq([(chars)[(digits)[0]]]))
                    in40_ = _dafny.Seq((digits)[1::])
                    in41_ = chars
                    digits = in40_
                    chars = in41_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Int2String(n, chars):
        d_225_base_ = len(chars)
        if (n) == (0):
            return _dafny.Seq("0")
        elif (n) > (0):
            return default__.Digits2String(default__.Int2Digits(n, d_225_base_), chars)
        elif True:
            return (_dafny.Seq("-")) + (default__.Digits2String(default__.Int2Digits((0) - (n), d_225_base_), chars))

    @staticmethod
    def Base10Int2String(n):
        return default__.Int2String(n, default__.Base10)

    @_dafny.classproperty
    def Base10(instance):
        return _dafny.Seq(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
