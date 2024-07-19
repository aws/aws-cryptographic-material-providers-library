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

# Module: JSON_Utils_Lexers_Strings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StringBody(escaped, byte):
        if (byte) == (ord('\\')):
            return JSON_Utils_Lexers_Core.LexerResult_Partial(not(escaped))
        elif ((byte) == (ord('\"'))) and (not(escaped)):
            return JSON_Utils_Lexers_Core.LexerResult_Accept()
        elif True:
            return JSON_Utils_Lexers_Core.LexerResult_Partial(False)

    @staticmethod
    def String(st, byte):
        source6_ = st
        if True:
            if source6_.is_Start:
                if (byte) == (ord('\"')):
                    return JSON_Utils_Lexers_Core.LexerResult_Partial(StringLexerState_Body(False))
                elif True:
                    return JSON_Utils_Lexers_Core.LexerResult_Reject(_dafny.Seq("String must start with double quote"))
        if True:
            if source6_.is_End:
                return JSON_Utils_Lexers_Core.LexerResult_Accept()
        if True:
            d_435_escaped_ = source6_.escaped
            if (byte) == (ord('\\')):
                return JSON_Utils_Lexers_Core.LexerResult_Partial(StringLexerState_Body(not(d_435_escaped_)))
            elif ((byte) == (ord('\"'))) and (not(d_435_escaped_)):
                return JSON_Utils_Lexers_Core.LexerResult_Partial(StringLexerState_End())
            elif True:
                return JSON_Utils_Lexers_Core.LexerResult_Partial(StringLexerState_Body(False))

    @_dafny.classproperty
    def StringBodyLexerStart(instance):
        return False
    @_dafny.classproperty
    def StringLexerStart(instance):
        return StringLexerState_Start()

class StringLexerState:
    @classmethod
    def default(cls, ):
        return lambda: StringLexerState_Start()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Start(self) -> bool:
        return isinstance(self, StringLexerState_Start)
    @property
    def is_Body(self) -> bool:
        return isinstance(self, StringLexerState_Body)
    @property
    def is_End(self) -> bool:
        return isinstance(self, StringLexerState_End)

class StringLexerState_Start(StringLexerState, NamedTuple('Start', [])):
    def __dafnystr__(self) -> str:
        return f'Strings.StringLexerState.Start'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StringLexerState_Start)
    def __hash__(self) -> int:
        return super().__hash__()

class StringLexerState_Body(StringLexerState, NamedTuple('Body', [('escaped', Any)])):
    def __dafnystr__(self) -> str:
        return f'Strings.StringLexerState.Body({_dafny.string_of(self.escaped)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StringLexerState_Body) and self.escaped == __o.escaped
    def __hash__(self) -> int:
        return super().__hash__()

class StringLexerState_End(StringLexerState, NamedTuple('End', [])):
    def __dafnystr__(self) -> str:
        return f'Strings.StringLexerState.End'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StringLexerState_End)
    def __hash__(self) -> int:
        return super().__hash__()

