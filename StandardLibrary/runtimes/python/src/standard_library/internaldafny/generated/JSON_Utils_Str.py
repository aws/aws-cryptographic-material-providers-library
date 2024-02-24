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
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
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

# Module: JSON_Utils_Str

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def OfNat(n, base):
        return JSON_Utils_Str_CharStrConversion.default__.OfNat__any(n, _dafny.Seq((default__.HEX__DIGITS)[:base:]))

    @staticmethod
    def OfInt(n, base):
        return JSON_Utils_Str_CharStrConversion.default__.OfInt__any(n, _dafny.Seq((default__.HEX__DIGITS)[:base:]), '-')

    @staticmethod
    def ToNat(str, base):
        return JSON_Utils_Str_CharStrConversion.default__.ToNat__any(str, base, default__.HEX__TABLE)

    @staticmethod
    def ToInt(str, base):
        return JSON_Utils_Str_CharStrConversion.default__.ToInt__any(str, '-', base, default__.HEX__TABLE)

    @staticmethod
    def EscapeQuotes(str):
        return JSON_Utils_Str_CharStrEscaping.default__.Escape(str, _dafny.Set({'\"', '\''}), '\\')

    @staticmethod
    def UnescapeQuotes(str):
        return JSON_Utils_Str_CharStrEscaping.default__.Unescape(str, '\\')

    @staticmethod
    def Test():
        if not((default__.OfInt(0, 10)) == (_dafny.Seq("0"))):
            raise _dafny.HaltException("/Users/lucmcdon/Desktop/workplace/aws-database-encryption-sdk-dynamodb-java/submodules/MaterialProviders/libraries/src/JSON/Utils/Str.dfy(229,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((default__.OfInt(3, 10)) == (_dafny.Seq("3"))):
            raise _dafny.HaltException("/Users/lucmcdon/Desktop/workplace/aws-database-encryption-sdk-dynamodb-java/submodules/MaterialProviders/libraries/src/JSON/Utils/Str.dfy(230,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((default__.OfInt(302, 10)) == (_dafny.Seq("302"))):
            raise _dafny.HaltException("/Users/lucmcdon/Desktop/workplace/aws-database-encryption-sdk-dynamodb-java/submodules/MaterialProviders/libraries/src/JSON/Utils/Str.dfy(231,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((default__.OfInt(-3, 10)) == (_dafny.Seq("-3"))):
            raise _dafny.HaltException("/Users/lucmcdon/Desktop/workplace/aws-database-encryption-sdk-dynamodb-java/submodules/MaterialProviders/libraries/src/JSON/Utils/Str.dfy(232,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((default__.OfInt(-302, 10)) == (_dafny.Seq("-302"))):
            raise _dafny.HaltException("/Users/lucmcdon/Desktop/workplace/aws-database-encryption-sdk-dynamodb-java/submodules/MaterialProviders/libraries/src/JSON/Utils/Str.dfy(233,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def OfBool(b):
        if b:
            return _dafny.Seq("true")
        elif True:
            return _dafny.Seq("false")

    @staticmethod
    def OfChar(c):
        return _dafny.Seq([c])

    @staticmethod
    def Join(sep, strs):
        d_384___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(strs)) == (0):
                    return (d_384___accumulator_) + (_dafny.Seq(""))
                elif (len(strs)) == (1):
                    return (d_384___accumulator_) + ((strs)[0])
                elif True:
                    d_384___accumulator_ = (d_384___accumulator_) + (((strs)[0]) + (sep))
                    in98_ = sep
                    in99_ = _dafny.Seq((strs)[1::])
                    sep = in98_
                    strs = in99_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Concat(strs):
        d_385___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(strs)) == (0):
                    return (d_385___accumulator_) + (_dafny.Seq(""))
                elif True:
                    d_385___accumulator_ = (d_385___accumulator_) + ((strs)[0])
                    in100_ = _dafny.Seq((strs)[1::])
                    strs = in100_
                    raise _dafny.TailCall()
                break

    @_dafny.classproperty
    def HEX__DIGITS(instance):
        return _dafny.Seq("0123456789ABCDEF")
    @_dafny.classproperty
    def HEX__TABLE(instance):
        return _dafny.Map({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15})
