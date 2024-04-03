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
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils

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
        if source9_.is_UnterminatedSequence:
            return _dafny.Seq("Unterminated sequence")
        elif source9_.is_UnsupportedEscape:
            d_503___mcc_h0_ = source9_.str
            d_504_str_ = d_503___mcc_h0_
            return (_dafny.Seq("Unsupported escape sequence: ")) + (d_504_str_)
        elif source9_.is_EscapeAtEOS:
            return _dafny.Seq("Escape character at end of string")
        elif source9_.is_EmptyNumber:
            return _dafny.Seq("Number must contain at least one digit")
        elif source9_.is_ExpectingEOF:
            return _dafny.Seq("Expecting EOF")
        elif source9_.is_IntOverflow:
            return _dafny.Seq("Input length does not fit in a 32-bit counter")
        elif source9_.is_ReachedEOF:
            return _dafny.Seq("Reached EOF")
        elif source9_.is_ExpectingByte:
            d_505___mcc_h1_ = source9_.expected
            d_506___mcc_h2_ = source9_.b
            d_507_b_ = d_506___mcc_h2_
            d_508_b0_ = d_505___mcc_h1_
            d_509_c_ = (((_dafny.Seq("'")) + (_dafny.Seq([chr(d_507_b_)]))) + (_dafny.Seq("'")) if (d_507_b_) > (0) else _dafny.Seq("EOF"))
            return (((_dafny.Seq("Expecting '")) + (_dafny.Seq([chr(d_508_b0_)]))) + (_dafny.Seq("', read "))) + (d_509_c_)
        elif source9_.is_ExpectingAnyByte:
            d_510___mcc_h3_ = source9_.expected__sq
            d_511___mcc_h4_ = source9_.b
            d_512_b_ = d_511___mcc_h4_
            d_513_bs0_ = d_510___mcc_h3_
            d_514_c_ = (((_dafny.Seq("'")) + (_dafny.Seq([chr(d_512_b_)]))) + (_dafny.Seq("'")) if (d_512_b_) > (0) else _dafny.Seq("EOF"))
            d_515_c0s_ = _dafny.Seq([chr((d_513_bs0_)[d_516_idx_]) for d_516_idx_ in range(len(d_513_bs0_))])
            return (((_dafny.Seq("Expecting one of '")) + (d_515_c0s_)) + (_dafny.Seq("', read "))) + (d_514_c_)
        elif True:
            return _dafny.Seq("Invalid Unicode sequence")


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
        if source10_.is_OutOfMemory:
            return _dafny.Seq("Out of memory")
        elif source10_.is_IntTooLarge:
            d_517___mcc_h0_ = source10_.i
            d_518_i_ = d_517___mcc_h0_
            return (_dafny.Seq("Integer too large: ")) + (JSON_Utils_Str.default__.OfInt(d_518_i_, 10))
        elif source10_.is_StringTooLong:
            d_519___mcc_h1_ = source10_.s
            d_520_s_ = d_519___mcc_h1_
            return (_dafny.Seq("String too long: ")) + (d_520_s_)
        elif True:
            return _dafny.Seq("Invalid Unicode sequence")


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

