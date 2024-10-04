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
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views as JSON_Utils_Views
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers as JSON_Utils_Lexers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion

# Module: JSON_Utils_Str_CharStrEscaping

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Escape(str, special, escape):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (str) == (_dafny.Seq([])):
                    return (d_0___accumulator_) + (str)
                elif ((str)[0]) in (special):
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.Seq([escape, (str)[0]]))
                    in0_ = _dafny.Seq((str)[1::])
                    in1_ = special
                    in2_ = escape
                    str = in0_
                    special = in1_
                    escape = in2_
                    raise _dafny.TailCall()
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.Seq([(str)[0]]))
                    in3_ = _dafny.Seq((str)[1::])
                    in4_ = special
                    in5_ = escape
                    str = in3_
                    special = in4_
                    escape = in5_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Unescape(str, escape):
        if (str) == (_dafny.Seq([])):
            return Wrappers.Result_Success(str)
        elif ((str)[0]) == (escape):
            if (len(str)) > (1):
                d_0_valueOrError0_ = default__.Unescape(_dafny.Seq((str)[2::]), escape)
                if (d_0_valueOrError0_).IsFailure():
                    return (d_0_valueOrError0_).PropagateFailure()
                elif True:
                    d_1_tl_ = (d_0_valueOrError0_).Extract()
                    return Wrappers.Result_Success((_dafny.Seq([(str)[1]])) + (d_1_tl_))
            elif True:
                return Wrappers.Result_Failure(UnescapeError_EscapeAtEOS())
        elif True:
            d_2_valueOrError1_ = default__.Unescape(_dafny.Seq((str)[1::]), escape)
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_tl_ = (d_2_valueOrError1_).Extract()
                return Wrappers.Result_Success((_dafny.Seq([(str)[0]])) + (d_3_tl_))


class UnescapeError:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [UnescapeError_EscapeAtEOS()]
    @classmethod
    def default(cls, ):
        return lambda: UnescapeError_EscapeAtEOS()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EscapeAtEOS(self) -> bool:
        return isinstance(self, UnescapeError_EscapeAtEOS)

class UnescapeError_EscapeAtEOS(UnescapeError, NamedTuple('EscapeAtEOS', [])):
    def __dafnystr__(self) -> str:
        return f'CharStrEscaping.UnescapeError.EscapeAtEOS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UnescapeError_EscapeAtEOS)
    def __hash__(self) -> int:
        return super().__hash__()

