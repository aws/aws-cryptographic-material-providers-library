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

# Module: JSON_Utils_Parsers

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ParserWitness():
        def lambda27_(d_481___v0_):
            return Wrappers.Result_Failure(JSON_Utils_Cursors.CursorError_EOF())

        return Parser___Parser(lambda27_)

    @staticmethod
    def SubParserWitness():
        def lambda28_(d_482_cs_):
            return Wrappers.Result_Failure(JSON_Utils_Cursors.CursorError_EOF())

        return SubParser___SubParser(lambda28_)


class Parser:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return default__.ParserWitness()

class Parser__:
    @classmethod
    def default(cls, default_T):
        return lambda: Parser___Parser((lambda x0: Wrappers.Result.default(JSON_Utils_Cursors.Split.default(default_T))()))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Parser(self) -> bool:
        return isinstance(self, Parser___Parser)

class Parser___Parser(Parser__, NamedTuple('Parser', [('fn', Any)])):
    def __dafnystr__(self) -> str:
        return f'Parsers.Parser_.Parser({_dafny.string_of(self.fn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Parser___Parser) and self.fn == __o.fn
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
        return isinstance(self, SubParser___SubParser)

class SubParser___SubParser(SubParser__, NamedTuple('SubParser', [('fn', Any)])):
    def __dafnystr__(self) -> str:
        return f'Parsers.SubParser_.SubParser({_dafny.string_of(self.fn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SubParser___SubParser) and self.fn == __o.fn
    def __hash__(self) -> int:
        return super().__hash__()


class SubParser:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return default__.SubParserWitness()
