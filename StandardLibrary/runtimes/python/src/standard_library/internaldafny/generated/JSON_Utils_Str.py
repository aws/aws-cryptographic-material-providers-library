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
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import standard_library.internaldafny.generated.JSON_Utils_Views as JSON_Utils_Views
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Lexers as JSON_Utils_Lexers
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping

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
            raise _dafny.HaltException("/Users/justplaz/workspace/amazon-s3-encryption-client-dafny/submodules/MaterialProviders/libraries/src/JSON/Utils/Str.dfy(229,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((default__.OfInt(3, 10)) == (_dafny.Seq("3"))):
            raise _dafny.HaltException("/Users/justplaz/workspace/amazon-s3-encryption-client-dafny/submodules/MaterialProviders/libraries/src/JSON/Utils/Str.dfy(230,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((default__.OfInt(302, 10)) == (_dafny.Seq("302"))):
            raise _dafny.HaltException("/Users/justplaz/workspace/amazon-s3-encryption-client-dafny/submodules/MaterialProviders/libraries/src/JSON/Utils/Str.dfy(231,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((default__.OfInt(-3, 10)) == (_dafny.Seq("-3"))):
            raise _dafny.HaltException("/Users/justplaz/workspace/amazon-s3-encryption-client-dafny/submodules/MaterialProviders/libraries/src/JSON/Utils/Str.dfy(232,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((default__.OfInt(-302, 10)) == (_dafny.Seq("-302"))):
            raise _dafny.HaltException("/Users/justplaz/workspace/amazon-s3-encryption-client-dafny/submodules/MaterialProviders/libraries/src/JSON/Utils/Str.dfy(233,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

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
        d_476___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(strs)) == (0):
                    return (d_476___accumulator_) + (_dafny.Seq(""))
                elif (len(strs)) == (1):
                    return (d_476___accumulator_) + ((strs)[0])
                elif True:
                    d_476___accumulator_ = (d_476___accumulator_) + (((strs)[0]) + (sep))
                    in201_ = sep
                    in202_ = _dafny.Seq((strs)[1::])
                    sep = in201_
                    strs = in202_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Concat(strs):
        d_477___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(strs)) == (0):
                    return (d_477___accumulator_) + (_dafny.Seq(""))
                elif True:
                    d_477___accumulator_ = (d_477___accumulator_) + ((strs)[0])
                    in203_ = _dafny.Seq((strs)[1::])
                    strs = in203_
                    raise _dafny.TailCall()
                break

    @_dafny.classproperty
    def HEX__DIGITS(instance):
        return _dafny.Seq("0123456789ABCDEF")
    @_dafny.classproperty
    def HEX__TABLE(instance):
        return _dafny.Map({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15})
