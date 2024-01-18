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
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors

# Module: JSON_Values

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Int(n):
        return Decimal_Decimal(n, 0)


class Decimal:
    @classmethod
    def default(cls, ):
        return lambda: Decimal_Decimal(int(0), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Decimal(self) -> bool:
        return isinstance(self, Decimal_Decimal)

class Decimal_Decimal(Decimal, NamedTuple('Decimal', [('n', Any), ('e10', Any)])):
    def __dafnystr__(self) -> str:
        return f'Values.Decimal.Decimal({_dafny.string_of(self.n)}, {_dafny.string_of(self.e10)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Decimal_Decimal) and self.n == __o.n and self.e10 == __o.e10
    def __hash__(self) -> int:
        return super().__hash__()


class JSON:
    @classmethod
    def default(cls, ):
        return lambda: JSON_Null()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Null(self) -> bool:
        return isinstance(self, JSON_Null)
    @property
    def is_Bool(self) -> bool:
        return isinstance(self, JSON_Bool)
    @property
    def is_String(self) -> bool:
        return isinstance(self, JSON_String)
    @property
    def is_Number(self) -> bool:
        return isinstance(self, JSON_Number)
    @property
    def is_Object(self) -> bool:
        return isinstance(self, JSON_Object)
    @property
    def is_Array(self) -> bool:
        return isinstance(self, JSON_Array)

class JSON_Null(JSON, NamedTuple('Null', [])):
    def __dafnystr__(self) -> str:
        return f'Values.JSON.Null'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_Null)
    def __hash__(self) -> int:
        return super().__hash__()

class JSON_Bool(JSON, NamedTuple('Bool', [('b', Any)])):
    def __dafnystr__(self) -> str:
        return f'Values.JSON.Bool({_dafny.string_of(self.b)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_Bool) and self.b == __o.b
    def __hash__(self) -> int:
        return super().__hash__()

class JSON_String(JSON, NamedTuple('String', [('str', Any)])):
    def __dafnystr__(self) -> str:
        return f'Values.JSON.String({_dafny.string_of(self.str)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_String) and self.str == __o.str
    def __hash__(self) -> int:
        return super().__hash__()

class JSON_Number(JSON, NamedTuple('Number', [('num', Any)])):
    def __dafnystr__(self) -> str:
        return f'Values.JSON.Number({_dafny.string_of(self.num)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_Number) and self.num == __o.num
    def __hash__(self) -> int:
        return super().__hash__()

class JSON_Object(JSON, NamedTuple('Object', [('obj', Any)])):
    def __dafnystr__(self) -> str:
        return f'Values.JSON.Object({_dafny.string_of(self.obj)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_Object) and self.obj == __o.obj
    def __hash__(self) -> int:
        return super().__hash__()

class JSON_Array(JSON, NamedTuple('Array', [('arr', Any)])):
    def __dafnystr__(self) -> str:
        return f'Values.JSON.Array({_dafny.string_of(self.arr)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_Array) and self.arr == __o.arr
    def __hash__(self) -> int:
        return super().__hash__()

