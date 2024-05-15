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

# Module: standard_library.internaldafny.generated.JSON_Utils_Parsers

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
