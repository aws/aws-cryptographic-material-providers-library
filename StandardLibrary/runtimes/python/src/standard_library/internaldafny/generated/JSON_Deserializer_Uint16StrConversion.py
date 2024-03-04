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
import StandardLibrary_String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer

# Module: JSON_Deserializer_Uint16StrConversion

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Digits(n, base):
        if (n) == (0):
            return _dafny.Seq([])
        elif True:
            d_587_digits_k_ = default__.Digits(_dafny.euclidian_division(n, base), base)
            d_588_digits_ = (d_587_digits_k_) + (_dafny.Seq([_dafny.euclidian_modulus(n, base)]))
            return d_588_digits_

    @staticmethod
    def OfDigits(digits, chars):
        d_589___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (digits) == (_dafny.Seq([])):
                    return (d_589___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_589___accumulator_ = (d_589___accumulator_) + (_dafny.Seq([(chars)[(digits)[0]]]))
                    in211_ = _dafny.Seq((digits)[1::])
                    in212_ = chars
                    digits = in211_
                    chars = in212_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def OfNat__any(n, chars):
        d_590_base_ = len(chars)
        if (n) == (0):
            return _dafny.Seq([(chars)[0]])
        elif True:
            return default__.OfDigits(default__.Digits(n, d_590_base_), chars)

    @staticmethod
    def NumberStr(str, minus, is__digit):
        def lambda37_(forall_var_8_):
            d_591_c_: int = forall_var_8_
            return not ((d_591_c_) in (_dafny.Seq((str)[1::]))) or (is__digit(d_591_c_))

        return not ((str) != (_dafny.Seq([]))) or (((((str)[0]) == (minus)) or (is__digit((str)[0]))) and (_dafny.quantifier((_dafny.Seq((str)[1::])).UniqueElements, True, lambda37_)))

    @staticmethod
    def OfInt__any(n, chars, minus):
        if (n) >= (0):
            return default__.OfNat__any(n, chars)
        elif True:
            return (_dafny.Seq([minus])) + (default__.OfNat__any((0) - (n), chars))

    @staticmethod
    def ToNat__any(str, base, digits):
        if (str) == (_dafny.Seq([])):
            return 0
        elif True:
            return ((default__.ToNat__any(_dafny.Seq((str)[:(len(str)) - (1):]), base, digits)) * (base)) + ((digits)[(str)[(len(str)) - (1)]])

    @staticmethod
    def ToInt__any(str, minus, base, digits):
        if (_dafny.Seq([minus])) <= (str):
            return (0) - (default__.ToNat__any(_dafny.Seq((str)[1::]), base, digits))
        elif True:
            return default__.ToNat__any(str, base, digits)

