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

# Module: JSON_Utils_Lexers_Core


class LexerResult:
    @classmethod
    def default(cls, ):
        return lambda: LexerResult_Accept()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Accept(self) -> bool:
        return isinstance(self, LexerResult_Accept)
    @property
    def is_Reject(self) -> bool:
        return isinstance(self, LexerResult_Reject)
    @property
    def is_Partial(self) -> bool:
        return isinstance(self, LexerResult_Partial)

class LexerResult_Accept(LexerResult, NamedTuple('Accept', [])):
    def __dafnystr__(self) -> str:
        return f'Core.LexerResult.Accept'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, LexerResult_Accept)
    def __hash__(self) -> int:
        return super().__hash__()

class LexerResult_Reject(LexerResult, NamedTuple('Reject', [('err', Any)])):
    def __dafnystr__(self) -> str:
        return f'Core.LexerResult.Reject({_dafny.string_of(self.err)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, LexerResult_Reject) and self.err == __o.err
    def __hash__(self) -> int:
        return super().__hash__()

class LexerResult_Partial(LexerResult, NamedTuple('Partial', [('st', Any)])):
    def __dafnystr__(self) -> str:
        return f'Core.LexerResult.Partial({_dafny.string_of(self.st)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, LexerResult_Partial) and self.st == __o.st
    def __hash__(self) -> int:
        return super().__hash__()

