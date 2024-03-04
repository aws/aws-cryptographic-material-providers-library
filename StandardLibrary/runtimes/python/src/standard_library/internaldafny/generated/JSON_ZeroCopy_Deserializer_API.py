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
import JSON_Errors
import JSON_Values
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer
import JSON_Deserializer_Uint16StrConversion
import JSON_Deserializer_ByteStrConversion
import JSON_Deserializer
import JSON_ConcreteSyntax_Spec
import JSON_ConcreteSyntax_SpecProperties
import JSON_ConcreteSyntax
import JSON_ZeroCopy_Serializer
import JSON_ZeroCopy_Deserializer_Core
import JSON_ZeroCopy_Deserializer_Strings
import JSON_ZeroCopy_Deserializer_Numbers
import JSON_ZeroCopy_Deserializer_ObjectParams
import JSON_ZeroCopy_Deserializer_Objects
import JSON_ZeroCopy_Deserializer_ArrayParams
import JSON_ZeroCopy_Deserializer_Arrays
import JSON_ZeroCopy_Deserializer_Constants
import JSON_ZeroCopy_Deserializer_Values

# Module: JSON_ZeroCopy_Deserializer_API

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def LiftCursorError(err):
        source20_ = err
        if source20_.is_EOF:
            return JSON_Errors.DeserializationError_ReachedEOF()
        elif source20_.is_ExpectingByte:
            d_883___mcc_h0_ = source20_.expected
            d_884___mcc_h1_ = source20_.b
            d_885_b_ = d_884___mcc_h1_
            d_886_expected_ = d_883___mcc_h0_
            return JSON_Errors.DeserializationError_ExpectingByte(d_886_expected_, d_885_b_)
        elif source20_.is_ExpectingAnyByte:
            d_887___mcc_h2_ = source20_.expected__sq
            d_888___mcc_h3_ = source20_.b
            d_889_b_ = d_888___mcc_h3_
            d_890_expected__sq_ = d_887___mcc_h2_
            return JSON_Errors.DeserializationError_ExpectingAnyByte(d_890_expected__sq_, d_889_b_)
        elif True:
            d_891___mcc_h4_ = source20_.err
            d_892_err_ = d_891___mcc_h4_
            return d_892_err_

    @staticmethod
    def JSON(cs):
        return (JSON_ZeroCopy_Deserializer_Core.default__.Structural(cs, JSON_Utils_Parsers.Parser___Parser(JSON_ZeroCopy_Deserializer_Values.default__.Value))).MapFailure(default__.LiftCursorError)

    @staticmethod
    def Text(v):
        d_893_valueOrError0_ = default__.JSON(JSON_Utils_Cursors.Cursor__.OfView(v))
        if (d_893_valueOrError0_).IsFailure():
            return (d_893_valueOrError0_).PropagateFailure()
        elif True:
            let_tmp_rhs29_ = (d_893_valueOrError0_).Extract()
            d_894_text_ = let_tmp_rhs29_.t
            d_895_cs_ = let_tmp_rhs29_.cs
            d_896_valueOrError1_ = Wrappers.default__.Need((d_895_cs_).EOF_q, JSON_Errors.DeserializationError_ExpectingEOF())
            if (d_896_valueOrError1_).IsFailure():
                return (d_896_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_894_text_)

    @staticmethod
    def OfBytes(bs):
        d_897_valueOrError0_ = Wrappers.default__.Need((len(bs)) < (BoundedInts.default__.TWO__TO__THE__32), JSON_Errors.DeserializationError_IntOverflow())
        if (d_897_valueOrError0_).IsFailure():
            return (d_897_valueOrError0_).PropagateFailure()
        elif True:
            return default__.Text(JSON_Utils_Views_Core.View__.OfBytes(bs))

