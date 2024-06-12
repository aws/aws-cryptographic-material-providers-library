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

# Module: JSON_Utils_Str_CharStrEscaping

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Escape(str, special, escape):
        d_471___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (str) == (_dafny.Seq([])):
                    return (d_471___accumulator_) + (str)
                elif ((str)[0]) in (special):
                    d_471___accumulator_ = (d_471___accumulator_) + (_dafny.Seq([escape, (str)[0]]))
                    in195_ = _dafny.Seq((str)[1::])
                    in196_ = special
                    in197_ = escape
                    str = in195_
                    special = in196_
                    escape = in197_
                    raise _dafny.TailCall()
                elif True:
                    d_471___accumulator_ = (d_471___accumulator_) + (_dafny.Seq([(str)[0]]))
                    in198_ = _dafny.Seq((str)[1::])
                    in199_ = special
                    in200_ = escape
                    str = in198_
                    special = in199_
                    escape = in200_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Unescape(str, escape):
        if (str) == (_dafny.Seq([])):
            return Wrappers.Result_Success(str)
        elif ((str)[0]) == (escape):
            if (len(str)) > (1):
                d_472_valueOrError0_ = default__.Unescape(_dafny.Seq((str)[2::]), escape)
                if (d_472_valueOrError0_).IsFailure():
                    return (d_472_valueOrError0_).PropagateFailure()
                elif True:
                    d_473_tl_ = (d_472_valueOrError0_).Extract()
                    return Wrappers.Result_Success((_dafny.Seq([(str)[1]])) + (d_473_tl_))
            elif True:
                return Wrappers.Result_Failure(UnescapeError_EscapeAtEOS())
        elif True:
            d_474_valueOrError1_ = default__.Unescape(_dafny.Seq((str)[1::]), escape)
            if (d_474_valueOrError1_).IsFailure():
                return (d_474_valueOrError1_).PropagateFailure()
            elif True:
                d_475_tl_ = (d_474_valueOrError1_).Extract()
                return Wrappers.Result_Success((_dafny.Seq([(str)[0]])) + (d_475_tl_))


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

