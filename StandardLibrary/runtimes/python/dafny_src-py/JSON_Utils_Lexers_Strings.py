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
import JSON_Utils_Lexers_Core

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
        if source6_.is_Start:
            if (byte) == (ord('\"')):
                return JSON_Utils_Lexers_Core.LexerResult_Partial(StringLexerState_Body(False))
            elif True:
                return JSON_Utils_Lexers_Core.LexerResult_Reject(_dafny.Seq("String must start with double quote"))
        elif source6_.is_Body:
            d_335___mcc_h0_ = source6_.escaped
            d_336_escaped_ = d_335___mcc_h0_
            if (byte) == (ord('\\')):
                return JSON_Utils_Lexers_Core.LexerResult_Partial(StringLexerState_Body(not(d_336_escaped_)))
            elif ((byte) == (ord('\"'))) and (not(d_336_escaped_)):
                return JSON_Utils_Lexers_Core.LexerResult_Partial(StringLexerState_End())
            elif True:
                return JSON_Utils_Lexers_Core.LexerResult_Partial(StringLexerState_Body(False))
        elif True:
            return JSON_Utils_Lexers_Core.LexerResult_Accept()

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

