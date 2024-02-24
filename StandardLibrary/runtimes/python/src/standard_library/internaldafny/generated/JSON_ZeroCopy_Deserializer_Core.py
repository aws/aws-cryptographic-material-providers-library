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

# Module: JSON_ZeroCopy_Deserializer_Core

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Get(cs, err):
        d_634_valueOrError0_ = (cs).Get(err)
        if (d_634_valueOrError0_).IsFailure():
            return (d_634_valueOrError0_).PropagateFailure()
        elif True:
            d_635_cs_ = (d_634_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_635_cs_).Split())

    @staticmethod
    def WS(cs):
        sp: JSON_Utils_Cursors.Split = JSON_Utils_Cursors.Split.default(JSON_Grammar.jblanks.default)()
        d_636_point_k_: int
        d_636_point_k_ = (cs).point
        d_637_end_: int
        d_637_end_ = (cs).end
        while ((d_636_point_k_) < (d_637_end_)) and (JSON_Grammar.default__.Blank_q(((cs).s)[d_636_point_k_])):
            d_636_point_k_ = (d_636_point_k_) + (1)
        sp = (JSON_Utils_Cursors.Cursor___Cursor((cs).s, (cs).beg, d_636_point_k_, (cs).end)).Split()
        return sp
        return sp

    @staticmethod
    def Structural(cs, parser):
        let_tmp_rhs2_ = default__.WS(cs)
        d_638_before_ = let_tmp_rhs2_.t
        d_639_cs_ = let_tmp_rhs2_.cs
        d_640_valueOrError0_ = (parser).fn(d_639_cs_)
        if (d_640_valueOrError0_).IsFailure():
            return (d_640_valueOrError0_).PropagateFailure()
        elif True:
            let_tmp_rhs3_ = (d_640_valueOrError0_).Extract()
            d_641_val_ = let_tmp_rhs3_.t
            d_642_cs_ = let_tmp_rhs3_.cs
            let_tmp_rhs4_ = default__.WS(d_642_cs_)
            d_643_after_ = let_tmp_rhs4_.t
            d_644_cs_ = let_tmp_rhs4_.cs
            return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Structural_Structural(d_638_before_, d_641_val_, d_643_after_), d_644_cs_))

    @staticmethod
    def TryStructural(cs):
        let_tmp_rhs5_ = default__.WS(cs)
        d_645_before_ = let_tmp_rhs5_.t
        d_646_cs_ = let_tmp_rhs5_.cs
        let_tmp_rhs6_ = ((d_646_cs_).SkipByte()).Split()
        d_647_val_ = let_tmp_rhs6_.t
        d_648_cs_ = let_tmp_rhs6_.cs
        let_tmp_rhs7_ = default__.WS(d_648_cs_)
        d_649_after_ = let_tmp_rhs7_.t
        d_650_cs_ = let_tmp_rhs7_.cs
        return JSON_Utils_Cursors.Split_SP(JSON_Grammar.Structural_Structural(d_645_before_, d_647_val_, d_649_after_), d_650_cs_)

    @_dafny.classproperty
    def SpecView(instance):
        def lambda49_(d_651_v_):
            return JSON_ConcreteSyntax_Spec.default__.View(d_651_v_)

        return lambda49_

class jopt:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_Utils_Views_Core.View__.OfBytes(_dafny.Seq([]))

class ValueParser:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_Utils_Parsers.SubParser.default()
