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

# Module: JSON_ZeroCopy_Deserializer_Strings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StringBody(cs):
        pr: Wrappers.Result = Wrappers.Result.default(JSON_Utils_Cursors.Cursor.default)()
        d_737_escaped_: bool
        d_737_escaped_ = False
        hi11_ = (cs).end
        for d_738_point_k_ in range((cs).point, hi11_):
            d_739_byte_: int
            d_739_byte_ = ((cs).s)[d_738_point_k_]
            if ((d_739_byte_) == (ord('\"'))) and (not(d_737_escaped_)):
                pr = Wrappers.Result_Success(JSON_Utils_Cursors.Cursor___Cursor((cs).s, (cs).beg, d_738_point_k_, (cs).end))
                return pr
            elif (d_739_byte_) == (ord('\\')):
                d_737_escaped_ = not(d_737_escaped_)
            elif True:
                d_737_escaped_ = False
        pr = Wrappers.Result_Failure(JSON_Utils_Cursors.CursorError_EOF())
        return pr
        return pr

    @staticmethod
    def Quote(cs):
        d_740_valueOrError0_ = (cs).AssertChar('\"')
        if (d_740_valueOrError0_).IsFailure():
            return (d_740_valueOrError0_).PropagateFailure()
        elif True:
            d_741_cs_ = (d_740_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_741_cs_).Split())

    @staticmethod
    def String(cs):
        d_742_valueOrError0_ = default__.Quote(cs)
        if (d_742_valueOrError0_).IsFailure():
            return (d_742_valueOrError0_).PropagateFailure()
        elif True:
            let_tmp_rhs14_ = (d_742_valueOrError0_).Extract()
            d_743_lq_ = let_tmp_rhs14_.t
            d_744_cs_ = let_tmp_rhs14_.cs
            d_745_valueOrError1_ = default__.StringBody(d_744_cs_)
            if (d_745_valueOrError1_).IsFailure():
                return (d_745_valueOrError1_).PropagateFailure()
            elif True:
                d_746_contents_ = (d_745_valueOrError1_).Extract()
                let_tmp_rhs15_ = (d_746_contents_).Split()
                d_747_contents_ = let_tmp_rhs15_.t
                d_748_cs_ = let_tmp_rhs15_.cs
                d_749_valueOrError2_ = default__.Quote(d_748_cs_)
                if (d_749_valueOrError2_).IsFailure():
                    return (d_749_valueOrError2_).PropagateFailure()
                elif True:
                    let_tmp_rhs16_ = (d_749_valueOrError2_).Extract()
                    d_750_rq_ = let_tmp_rhs16_.t
                    d_751_cs_ = let_tmp_rhs16_.cs
                    return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.jstring_JString(d_743_lq_, d_747_contents_, d_750_rq_), d_751_cs_))

