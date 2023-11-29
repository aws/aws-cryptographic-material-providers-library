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

# assert "JSON_mUtils_mParsers" == __name__
JSON_mUtils_mParsers = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ParserWitness():
        def lambda24_(d_372___v0_):
            return Wrappers.Result_Failure(JSON_mUtils_mCursors.CursorError_EOF())

        return JSON_mUtils_mParsers.Parser___Parser(lambda24_)

    @staticmethod
    def SubParserWitness():
        def lambda25_(d_373_cs_):
            return Wrappers.Result_Failure(JSON_mUtils_mCursors.CursorError_EOF())

        return JSON_mUtils_mParsers.SubParser___SubParser(lambda25_)


class Parser:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mParsers.default__.ParserWitness()

class Parser__:
    @classmethod
    def default(cls, default_T):
        return lambda: Parser___Parser((lambda x0: Wrappers.Result_Success.default(JSON_mUtils_mCursors.Split.default(default_T))()))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Parser(self) -> bool:
        return isinstance(self, JSON_mUtils_mParsers.Parser___Parser)

class Parser___Parser(Parser__, NamedTuple('Parser', [('fn', Any)])):
    def __dafnystr__(self) -> str:
        return f'Parsers.Parser_.Parser({_dafny.string_of(self.fn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mUtils_mParsers.Parser___Parser) and self.fn == __o.fn
    def __hash__(self) -> int:
        return super().__hash__()


class SubParser__:
    @classmethod
    def default(cls, ):
        return lambda: SubParser___SubParser(None)
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SubParser(self) -> bool:
        return isinstance(self, JSON_mUtils_mParsers.SubParser___SubParser)

class SubParser___SubParser(SubParser__, NamedTuple('SubParser', [('fn', Any)])):
    def __dafnystr__(self) -> str:
        return f'Parsers.SubParser_.SubParser({_dafny.string_of(self.fn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mUtils_mParsers.SubParser___SubParser) and self.fn == __o.fn
    def __hash__(self) -> int:
        return super().__hash__()


class SubParser:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mParsers.default__.SubParserWitness()
