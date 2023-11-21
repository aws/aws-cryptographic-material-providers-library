import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
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
import StandardLibrary_mUInt
import String
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
import DafnyLibraries
import JSON_mUtils_mViews_mCore
import JSON_mUtils_mViews_mWriters
import JSON_mUtils_mViews
import JSON_mUtils_mLexers_mCore
import JSON_mUtils_mLexers_mStrings
import JSON_mUtils_mLexers
import JSON_mUtils_mCursors
import JSON_mUtils_mParsers
import JSON_mUtils_mStr_mCharStrConversion

assert "JSON_mUtils_mStr_mCharStrEscaping" == __name__
JSON_mUtils_mStr_mCharStrEscaping = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Escape(str, special, escape):
        d_379___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (str) == (_dafny.Seq([])):
                    return (d_379___accumulator_) + (str)
                elif ((str)[0]) in (special):
                    d_379___accumulator_ = (d_379___accumulator_) + (_dafny.Seq([escape, (str)[0]]))
                    in92_ = _dafny.Seq((str)[1::])
                    in93_ = special
                    in94_ = escape
                    str = in92_
                    special = in93_
                    escape = in94_
                    raise _dafny.TailCall()
                elif True:
                    d_379___accumulator_ = (d_379___accumulator_) + (_dafny.Seq([(str)[0]]))
                    in95_ = _dafny.Seq((str)[1::])
                    in96_ = special
                    in97_ = escape
                    str = in95_
                    special = in96_
                    escape = in97_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Unescape(str, escape):
        if (str) == (_dafny.Seq([])):
            return Wrappers.Result_Success(str)
        elif ((str)[0]) == (escape):
            if (len(str)) > (1):
                d_380_valueOrError0_ = JSON_mUtils_mStr_mCharStrEscaping.default__.Unescape(_dafny.Seq((str)[2::]), escape)
                if (d_380_valueOrError0_).IsFailure():
                    return (d_380_valueOrError0_).PropagateFailure()
                elif True:
                    d_381_tl_ = (d_380_valueOrError0_).Extract()
                    return Wrappers.Result_Success((_dafny.Seq([(str)[1]])) + (d_381_tl_))
            elif True:
                return Wrappers.Result_Failure(JSON_mUtils_mStr_mCharStrEscaping.UnescapeError_EscapeAtEOS())
        elif True:
            d_382_valueOrError1_ = JSON_mUtils_mStr_mCharStrEscaping.default__.Unescape(_dafny.Seq((str)[1::]), escape)
            if (d_382_valueOrError1_).IsFailure():
                return (d_382_valueOrError1_).PropagateFailure()
            elif True:
                d_383_tl_ = (d_382_valueOrError1_).Extract()
                return Wrappers.Result_Success((_dafny.Seq([(str)[0]])) + (d_383_tl_))


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
        return isinstance(self, JSON_mUtils_mStr_mCharStrEscaping.UnescapeError_EscapeAtEOS)

class UnescapeError_EscapeAtEOS(UnescapeError, NamedTuple('EscapeAtEOS', [])):
    def __dafnystr__(self) -> str:
        return f'CharStrEscaping.UnescapeError.EscapeAtEOS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mUtils_mStr_mCharStrEscaping.UnescapeError_EscapeAtEOS)
    def __hash__(self) -> int:
        return super().__hash__()

