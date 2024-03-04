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

# Module: JSON_ZeroCopy_Deserializer_Core

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Get(cs, err):
        d_719_valueOrError0_ = (cs).Get(err)
        if (d_719_valueOrError0_).IsFailure():
            return (d_719_valueOrError0_).PropagateFailure()
        elif True:
            d_720_cs_ = (d_719_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_720_cs_).Split())

    @staticmethod
    def WS(cs):
        sp: JSON_Utils_Cursors.Split = JSON_Utils_Cursors.Split.default(JSON_Grammar.jblanks.default)()
        d_721_point_k_: int
        d_721_point_k_ = (cs).point
        d_722_end_: int
        d_722_end_ = (cs).end
        while ((d_721_point_k_) < (d_722_end_)) and (JSON_Grammar.default__.Blank_q(((cs).s)[d_721_point_k_])):
            d_721_point_k_ = (d_721_point_k_) + (1)
        sp = (JSON_Utils_Cursors.Cursor___Cursor((cs).s, (cs).beg, d_721_point_k_, (cs).end)).Split()
        return sp
        return sp

    @staticmethod
    def Structural(cs, parser):
        let_tmp_rhs8_ = default__.WS(cs)
        d_723_before_ = let_tmp_rhs8_.t
        d_724_cs_ = let_tmp_rhs8_.cs
        d_725_valueOrError0_ = (parser).fn(d_724_cs_)
        if (d_725_valueOrError0_).IsFailure():
            return (d_725_valueOrError0_).PropagateFailure()
        elif True:
            let_tmp_rhs9_ = (d_725_valueOrError0_).Extract()
            d_726_val_ = let_tmp_rhs9_.t
            d_727_cs_ = let_tmp_rhs9_.cs
            let_tmp_rhs10_ = default__.WS(d_727_cs_)
            d_728_after_ = let_tmp_rhs10_.t
            d_729_cs_ = let_tmp_rhs10_.cs
            return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Structural_Structural(d_723_before_, d_726_val_, d_728_after_), d_729_cs_))

    @staticmethod
    def TryStructural(cs):
        let_tmp_rhs11_ = default__.WS(cs)
        d_730_before_ = let_tmp_rhs11_.t
        d_731_cs_ = let_tmp_rhs11_.cs
        let_tmp_rhs12_ = ((d_731_cs_).SkipByte()).Split()
        d_732_val_ = let_tmp_rhs12_.t
        d_733_cs_ = let_tmp_rhs12_.cs
        let_tmp_rhs13_ = default__.WS(d_733_cs_)
        d_734_after_ = let_tmp_rhs13_.t
        d_735_cs_ = let_tmp_rhs13_.cs
        return JSON_Utils_Cursors.Split_SP(JSON_Grammar.Structural_Structural(d_730_before_, d_732_val_, d_734_after_), d_735_cs_)

    @_dafny.classproperty
    def SpecView(instance):
        def lambda51_(d_736_v_):
            return JSON_ConcreteSyntax_Spec.default__.View(d_736_v_)

        return lambda51_

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
