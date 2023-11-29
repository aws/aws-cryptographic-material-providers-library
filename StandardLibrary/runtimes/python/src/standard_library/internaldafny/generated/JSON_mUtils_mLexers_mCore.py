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

# assert "JSON_mUtils_mLexers_mCore" == __name__
JSON_mUtils_mLexers_mCore = sys.modules[__name__]


class LexerResult:
    @classmethod
    def default(cls, ):
        return lambda: LexerResult_Accept()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Accept(self) -> bool:
        return isinstance(self, JSON_mUtils_mLexers_mCore.LexerResult_Accept)
    @property
    def is_Reject(self) -> bool:
        return isinstance(self, JSON_mUtils_mLexers_mCore.LexerResult_Reject)
    @property
    def is_Partial(self) -> bool:
        return isinstance(self, JSON_mUtils_mLexers_mCore.LexerResult_Partial)

class LexerResult_Accept(LexerResult, NamedTuple('Accept', [])):
    def __dafnystr__(self) -> str:
        return f'Core.LexerResult.Accept'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mUtils_mLexers_mCore.LexerResult_Accept)
    def __hash__(self) -> int:
        return super().__hash__()

class LexerResult_Reject(LexerResult, NamedTuple('Reject', [('err', Any)])):
    def __dafnystr__(self) -> str:
        return f'Core.LexerResult.Reject({_dafny.string_of(self.err)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mUtils_mLexers_mCore.LexerResult_Reject) and self.err == __o.err
    def __hash__(self) -> int:
        return super().__hash__()

class LexerResult_Partial(LexerResult, NamedTuple('Partial', [('st', Any)])):
    def __dafnystr__(self) -> str:
        return f'Core.LexerResult.Partial({_dafny.string_of(self.st)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mUtils_mLexers_mCore.LexerResult_Partial) and self.st == __o.st
    def __hash__(self) -> int:
        return super().__hash__()

