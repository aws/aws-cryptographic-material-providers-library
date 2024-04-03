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

# Module: JSON_Utils_Str_CharStrEscaping

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Escape(str, special, escape):
        d_488___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (str) == (_dafny.Seq([])):
                    return (d_488___accumulator_) + (str)
                elif ((str)[0]) in (special):
                    d_488___accumulator_ = (d_488___accumulator_) + (_dafny.Seq([escape, (str)[0]]))
                    in195_ = _dafny.Seq((str)[1::])
                    in196_ = special
                    in197_ = escape
                    str = in195_
                    special = in196_
                    escape = in197_
                    raise _dafny.TailCall()
                elif True:
                    d_488___accumulator_ = (d_488___accumulator_) + (_dafny.Seq([(str)[0]]))
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
                d_489_valueOrError0_ = default__.Unescape(_dafny.Seq((str)[2::]), escape)
                if (d_489_valueOrError0_).IsFailure():
                    return (d_489_valueOrError0_).PropagateFailure()
                elif True:
                    d_490_tl_ = (d_489_valueOrError0_).Extract()
                    return Wrappers.Result_Success((_dafny.Seq([(str)[1]])) + (d_490_tl_))
            elif True:
                return Wrappers.Result_Failure(UnescapeError_EscapeAtEOS())
        elif True:
            d_491_valueOrError1_ = default__.Unescape(_dafny.Seq((str)[1::]), escape)
            if (d_491_valueOrError1_).IsFailure():
                return (d_491_valueOrError1_).PropagateFailure()
            elif True:
                d_492_tl_ = (d_491_valueOrError1_).Extract()
                return Wrappers.Result_Success((_dafny.Seq([(str)[0]])) + (d_492_tl_))


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

