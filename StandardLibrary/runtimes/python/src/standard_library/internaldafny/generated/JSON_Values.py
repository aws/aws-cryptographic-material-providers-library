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
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import standard_library.internaldafny.generated.JSON_Utils as JSON_Utils
import standard_library.internaldafny.generated.JSON_Errors as JSON_Errors

# Module: standard_library.internaldafny.generated.JSON_Values

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

