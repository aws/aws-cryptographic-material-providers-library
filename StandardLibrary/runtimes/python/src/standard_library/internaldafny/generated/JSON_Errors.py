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

# Module: JSON_Errors


class DeserializationError:
    @classmethod
    def default(cls, ):
        return lambda: DeserializationError_UnterminatedSequence()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UnterminatedSequence(self) -> bool:
        return isinstance(self, DeserializationError_UnterminatedSequence)
    @property
    def is_UnsupportedEscape(self) -> bool:
        return isinstance(self, DeserializationError_UnsupportedEscape)
    @property
    def is_EscapeAtEOS(self) -> bool:
        return isinstance(self, DeserializationError_EscapeAtEOS)
    @property
    def is_EmptyNumber(self) -> bool:
        return isinstance(self, DeserializationError_EmptyNumber)
    @property
    def is_ExpectingEOF(self) -> bool:
        return isinstance(self, DeserializationError_ExpectingEOF)
    @property
    def is_IntOverflow(self) -> bool:
        return isinstance(self, DeserializationError_IntOverflow)
    @property
    def is_ReachedEOF(self) -> bool:
        return isinstance(self, DeserializationError_ReachedEOF)
    @property
    def is_ExpectingByte(self) -> bool:
        return isinstance(self, DeserializationError_ExpectingByte)
    @property
    def is_ExpectingAnyByte(self) -> bool:
        return isinstance(self, DeserializationError_ExpectingAnyByte)
    @property
    def is_InvalidUnicode(self) -> bool:
        return isinstance(self, DeserializationError_InvalidUnicode)
    def ToString(self):
        source9_ = self
        unmatched9 = True
        if unmatched9:
            if source9_.is_UnterminatedSequence:
                unmatched9 = False
                return _dafny.Seq("Unterminated sequence")
        if unmatched9:
            if source9_.is_UnsupportedEscape:
                d_486_str_ = source9_.str
                unmatched9 = False
                return (_dafny.Seq("Unsupported escape sequence: ")) + (d_486_str_)
        if unmatched9:
            if source9_.is_EscapeAtEOS:
                unmatched9 = False
                return _dafny.Seq("Escape character at end of string")
        if unmatched9:
            if source9_.is_EmptyNumber:
                unmatched9 = False
                return _dafny.Seq("Number must contain at least one digit")
        if unmatched9:
            if source9_.is_ExpectingEOF:
                unmatched9 = False
                return _dafny.Seq("Expecting EOF")
        if unmatched9:
            if source9_.is_IntOverflow:
                unmatched9 = False
                return _dafny.Seq("Input length does not fit in a 32-bit counter")
        if unmatched9:
            if source9_.is_ReachedEOF:
                unmatched9 = False
                return _dafny.Seq("Reached EOF")
        if unmatched9:
            if source9_.is_ExpectingByte:
                d_487_b0_ = source9_.expected
                d_488_b_ = source9_.b
                unmatched9 = False
                d_489_c_ = (((_dafny.Seq("'")) + (_dafny.Seq([chr(d_488_b_)]))) + (_dafny.Seq("'")) if (d_488_b_) > (0) else _dafny.Seq("EOF"))
                return (((_dafny.Seq("Expecting '")) + (_dafny.Seq([chr(d_487_b0_)]))) + (_dafny.Seq("', read "))) + (d_489_c_)
        if unmatched9:
            if source9_.is_ExpectingAnyByte:
                d_490_bs0_ = source9_.expected__sq
                d_491_b_ = source9_.b
                unmatched9 = False
                d_492_c_ = (((_dafny.Seq("'")) + (_dafny.Seq([chr(d_491_b_)]))) + (_dafny.Seq("'")) if (d_491_b_) > (0) else _dafny.Seq("EOF"))
                d_493_c0s_ = _dafny.Seq([chr((d_490_bs0_)[d_494_idx_]) for d_494_idx_ in range(len(d_490_bs0_))])
                return (((_dafny.Seq("Expecting one of '")) + (d_493_c0s_)) + (_dafny.Seq("', read "))) + (d_492_c_)
        if unmatched9:
            unmatched9 = False
            return _dafny.Seq("Invalid Unicode sequence")
        raise Exception("unexpected control point")


class DeserializationError_UnterminatedSequence(DeserializationError, NamedTuple('UnterminatedSequence', [])):
    def __dafnystr__(self) -> str:
        return f'Errors.DeserializationError.UnterminatedSequence'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeserializationError_UnterminatedSequence)
    def __hash__(self) -> int:
        return super().__hash__()

class DeserializationError_UnsupportedEscape(DeserializationError, NamedTuple('UnsupportedEscape', [('str', Any)])):
    def __dafnystr__(self) -> str:
        return f'Errors.DeserializationError.UnsupportedEscape({_dafny.string_of(self.str)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeserializationError_UnsupportedEscape) and self.str == __o.str
    def __hash__(self) -> int:
        return super().__hash__()

class DeserializationError_EscapeAtEOS(DeserializationError, NamedTuple('EscapeAtEOS', [])):
    def __dafnystr__(self) -> str:
        return f'Errors.DeserializationError.EscapeAtEOS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeserializationError_EscapeAtEOS)
    def __hash__(self) -> int:
        return super().__hash__()

class DeserializationError_EmptyNumber(DeserializationError, NamedTuple('EmptyNumber', [])):
    def __dafnystr__(self) -> str:
        return f'Errors.DeserializationError.EmptyNumber'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeserializationError_EmptyNumber)
    def __hash__(self) -> int:
        return super().__hash__()

class DeserializationError_ExpectingEOF(DeserializationError, NamedTuple('ExpectingEOF', [])):
    def __dafnystr__(self) -> str:
        return f'Errors.DeserializationError.ExpectingEOF'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeserializationError_ExpectingEOF)
    def __hash__(self) -> int:
        return super().__hash__()

class DeserializationError_IntOverflow(DeserializationError, NamedTuple('IntOverflow', [])):
    def __dafnystr__(self) -> str:
        return f'Errors.DeserializationError.IntOverflow'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeserializationError_IntOverflow)
    def __hash__(self) -> int:
        return super().__hash__()

class DeserializationError_ReachedEOF(DeserializationError, NamedTuple('ReachedEOF', [])):
    def __dafnystr__(self) -> str:
        return f'Errors.DeserializationError.ReachedEOF'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeserializationError_ReachedEOF)
    def __hash__(self) -> int:
        return super().__hash__()

class DeserializationError_ExpectingByte(DeserializationError, NamedTuple('ExpectingByte', [('expected', Any), ('b', Any)])):
    def __dafnystr__(self) -> str:
        return f'Errors.DeserializationError.ExpectingByte({_dafny.string_of(self.expected)}, {_dafny.string_of(self.b)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeserializationError_ExpectingByte) and self.expected == __o.expected and self.b == __o.b
    def __hash__(self) -> int:
        return super().__hash__()

class DeserializationError_ExpectingAnyByte(DeserializationError, NamedTuple('ExpectingAnyByte', [('expected__sq', Any), ('b', Any)])):
    def __dafnystr__(self) -> str:
        return f'Errors.DeserializationError.ExpectingAnyByte({_dafny.string_of(self.expected__sq)}, {_dafny.string_of(self.b)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeserializationError_ExpectingAnyByte) and self.expected__sq == __o.expected__sq and self.b == __o.b
    def __hash__(self) -> int:
        return super().__hash__()

class DeserializationError_InvalidUnicode(DeserializationError, NamedTuple('InvalidUnicode', [])):
    def __dafnystr__(self) -> str:
        return f'Errors.DeserializationError.InvalidUnicode'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeserializationError_InvalidUnicode)
    def __hash__(self) -> int:
        return super().__hash__()


class SerializationError:
    @classmethod
    def default(cls, ):
        return lambda: SerializationError_OutOfMemory()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_OutOfMemory(self) -> bool:
        return isinstance(self, SerializationError_OutOfMemory)
    @property
    def is_IntTooLarge(self) -> bool:
        return isinstance(self, SerializationError_IntTooLarge)
    @property
    def is_StringTooLong(self) -> bool:
        return isinstance(self, SerializationError_StringTooLong)
    @property
    def is_InvalidUnicode(self) -> bool:
        return isinstance(self, SerializationError_InvalidUnicode)
    def ToString(self):
        source10_ = self
        unmatched10 = True
        if unmatched10:
            if source10_.is_OutOfMemory:
                unmatched10 = False
                return _dafny.Seq("Out of memory")
        if unmatched10:
            if source10_.is_IntTooLarge:
                d_495_i_ = source10_.i
                unmatched10 = False
                return (_dafny.Seq("Integer too large: ")) + (JSON_Utils_Str.default__.OfInt(d_495_i_, 10))
        if unmatched10:
            if source10_.is_StringTooLong:
                d_496_s_ = source10_.s
                unmatched10 = False
                return (_dafny.Seq("String too long: ")) + (d_496_s_)
        if unmatched10:
            unmatched10 = False
            return _dafny.Seq("Invalid Unicode sequence")
        raise Exception("unexpected control point")


class SerializationError_OutOfMemory(SerializationError, NamedTuple('OutOfMemory', [])):
    def __dafnystr__(self) -> str:
        return f'Errors.SerializationError.OutOfMemory'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SerializationError_OutOfMemory)
    def __hash__(self) -> int:
        return super().__hash__()

class SerializationError_IntTooLarge(SerializationError, NamedTuple('IntTooLarge', [('i', Any)])):
    def __dafnystr__(self) -> str:
        return f'Errors.SerializationError.IntTooLarge({_dafny.string_of(self.i)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SerializationError_IntTooLarge) and self.i == __o.i
    def __hash__(self) -> int:
        return super().__hash__()

class SerializationError_StringTooLong(SerializationError, NamedTuple('StringTooLong', [('s', Any)])):
    def __dafnystr__(self) -> str:
        return f'Errors.SerializationError.StringTooLong({_dafny.string_of(self.s)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SerializationError_StringTooLong) and self.s == __o.s
    def __hash__(self) -> int:
        return super().__hash__()

class SerializationError_InvalidUnicode(SerializationError, NamedTuple('InvalidUnicode', [])):
    def __dafnystr__(self) -> str:
        return f'Errors.SerializationError.InvalidUnicode'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SerializationError_InvalidUnicode)
    def __hash__(self) -> int:
        return super().__hash__()

