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

# Module: JSON_ZeroCopy_Deserializer_Strings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StringBody(cs):
        pr: Wrappers.Result = Wrappers.Result.default(JSON_Utils_Cursors.Cursor.default)()
        d_652_escaped_: bool
        d_652_escaped_ = False
        hi11_ = (cs).end
        for d_653_point_k_ in range((cs).point, hi11_):
            d_654_byte_: int
            d_654_byte_ = ((cs).s)[d_653_point_k_]
            if ((d_654_byte_) == (ord('\"'))) and (not(d_652_escaped_)):
                pr = Wrappers.Result_Success(JSON_Utils_Cursors.Cursor___Cursor((cs).s, (cs).beg, d_653_point_k_, (cs).end))
                return pr
            elif (d_654_byte_) == (ord('\\')):
                d_652_escaped_ = not(d_652_escaped_)
            elif True:
                d_652_escaped_ = False
        pr = Wrappers.Result_Failure(JSON_Utils_Cursors.CursorError_EOF())
        return pr
        return pr

    @staticmethod
    def Quote(cs):
        d_655_valueOrError0_ = (cs).AssertChar('\"')
        if (d_655_valueOrError0_).IsFailure():
            return (d_655_valueOrError0_).PropagateFailure()
        elif True:
            d_656_cs_ = (d_655_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_656_cs_).Split())

    @staticmethod
    def String(cs):
        d_657_valueOrError0_ = default__.Quote(cs)
        if (d_657_valueOrError0_).IsFailure():
            return (d_657_valueOrError0_).PropagateFailure()
        elif True:
            let_tmp_rhs8_ = (d_657_valueOrError0_).Extract()
            d_658_lq_ = let_tmp_rhs8_.t
            d_659_cs_ = let_tmp_rhs8_.cs
            d_660_valueOrError1_ = default__.StringBody(d_659_cs_)
            if (d_660_valueOrError1_).IsFailure():
                return (d_660_valueOrError1_).PropagateFailure()
            elif True:
                d_661_contents_ = (d_660_valueOrError1_).Extract()
                let_tmp_rhs9_ = (d_661_contents_).Split()
                d_662_contents_ = let_tmp_rhs9_.t
                d_663_cs_ = let_tmp_rhs9_.cs
                d_664_valueOrError2_ = default__.Quote(d_663_cs_)
                if (d_664_valueOrError2_).IsFailure():
                    return (d_664_valueOrError2_).PropagateFailure()
                elif True:
                    let_tmp_rhs10_ = (d_664_valueOrError2_).Extract()
                    d_665_rq_ = let_tmp_rhs10_.t
                    d_666_cs_ = let_tmp_rhs10_.cs
                    return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.jstring_JString(d_658_lq_, d_662_contents_, d_665_rq_), d_666_cs_))

