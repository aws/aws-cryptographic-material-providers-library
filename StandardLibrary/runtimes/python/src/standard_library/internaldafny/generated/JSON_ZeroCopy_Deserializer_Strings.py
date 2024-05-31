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
import standard_library.internaldafny.generated.JSON_Values as JSON_Values
import standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import standard_library.internaldafny.generated.JSON_ConcreteSyntax as JSON_ConcreteSyntax
import standard_library.internaldafny.generated.JSON_ZeroCopy_Serializer as JSON_ZeroCopy_Serializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Core as JSON_ZeroCopy_Deserializer_Core

# Module: JSON_ZeroCopy_Deserializer_Strings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StringBody(cs):
        pr: Wrappers.Result = Wrappers.Result.default(JSON_Utils_Cursors.Cursor.default)()
        d_763_escaped_: bool
        d_763_escaped_ = False
        hi11_ = (cs).end
        for d_764_point_k_ in range((cs).point, hi11_):
            d_765_byte_: int
            d_765_byte_ = ((cs).s)[d_764_point_k_]
            if ((d_765_byte_) == (ord('\"'))) and (not(d_763_escaped_)):
                pr = Wrappers.Result_Success(JSON_Utils_Cursors.Cursor___Cursor((cs).s, (cs).beg, d_764_point_k_, (cs).end))
                return pr
            elif (d_765_byte_) == (ord('\\')):
                d_763_escaped_ = not(d_763_escaped_)
            elif True:
                d_763_escaped_ = False
        pr = Wrappers.Result_Failure(JSON_Utils_Cursors.CursorError_EOF())
        return pr
        return pr

    @staticmethod
    def Quote(cs):
        d_766_valueOrError0_ = (cs).AssertChar('\"')
        if (d_766_valueOrError0_).IsFailure():
            return (d_766_valueOrError0_).PropagateFailure()
        elif True:
            d_767_cs_ = (d_766_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_767_cs_).Split())

    @staticmethod
    def String(cs):
        d_768_valueOrError0_ = default__.Quote(cs)
        if (d_768_valueOrError0_).IsFailure():
            return (d_768_valueOrError0_).PropagateFailure()
        elif True:
            let_tmp_rhs14_ = (d_768_valueOrError0_).Extract()
            d_769_lq_ = let_tmp_rhs14_.t
            d_770_cs_ = let_tmp_rhs14_.cs
            d_771_valueOrError1_ = default__.StringBody(d_770_cs_)
            if (d_771_valueOrError1_).IsFailure():
                return (d_771_valueOrError1_).PropagateFailure()
            elif True:
                d_772_contents_ = (d_771_valueOrError1_).Extract()
                let_tmp_rhs15_ = (d_772_contents_).Split()
                d_773_contents_ = let_tmp_rhs15_.t
                d_774_cs_ = let_tmp_rhs15_.cs
                d_775_valueOrError2_ = default__.Quote(d_774_cs_)
                if (d_775_valueOrError2_).IsFailure():
                    return (d_775_valueOrError2_).PropagateFailure()
                elif True:
                    let_tmp_rhs16_ = (d_775_valueOrError2_).Extract()
                    d_776_rq_ = let_tmp_rhs16_.t
                    d_777_cs_ = let_tmp_rhs16_.cs
                    return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.jstring_JString(d_769_lq_, d_773_contents_, d_776_rq_), d_777_cs_))

