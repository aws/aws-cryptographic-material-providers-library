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
        d_745_valueOrError0_ = (cs).Get(err)
        if (d_745_valueOrError0_).IsFailure():
            return (d_745_valueOrError0_).PropagateFailure()
        elif True:
            d_746_cs_ = (d_745_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_746_cs_).Split())

    @staticmethod
    def WS(cs):
        sp: JSON_Utils_Cursors.Split = JSON_Utils_Cursors.Split.default(JSON_Grammar.jblanks.default)()
        d_747_point_k_: int
        d_747_point_k_ = (cs).point
        d_748_end_: int
        d_748_end_ = (cs).end
        while ((d_747_point_k_) < (d_748_end_)) and (JSON_Grammar.default__.Blank_q(((cs).s)[d_747_point_k_])):
            d_747_point_k_ = (d_747_point_k_) + (1)
        sp = (JSON_Utils_Cursors.Cursor___Cursor((cs).s, (cs).beg, d_747_point_k_, (cs).end)).Split()
        return sp
        return sp

    @staticmethod
    def Structural(cs, parser):
        let_tmp_rhs8_ = default__.WS(cs)
        d_749_before_ = let_tmp_rhs8_.t
        d_750_cs_ = let_tmp_rhs8_.cs
        d_751_valueOrError0_ = (parser).fn(d_750_cs_)
        if (d_751_valueOrError0_).IsFailure():
            return (d_751_valueOrError0_).PropagateFailure()
        elif True:
            let_tmp_rhs9_ = (d_751_valueOrError0_).Extract()
            d_752_val_ = let_tmp_rhs9_.t
            d_753_cs_ = let_tmp_rhs9_.cs
            let_tmp_rhs10_ = default__.WS(d_753_cs_)
            d_754_after_ = let_tmp_rhs10_.t
            d_755_cs_ = let_tmp_rhs10_.cs
            return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Structural_Structural(d_749_before_, d_752_val_, d_754_after_), d_755_cs_))

    @staticmethod
    def TryStructural(cs):
        let_tmp_rhs11_ = default__.WS(cs)
        d_756_before_ = let_tmp_rhs11_.t
        d_757_cs_ = let_tmp_rhs11_.cs
        let_tmp_rhs12_ = ((d_757_cs_).SkipByte()).Split()
        d_758_val_ = let_tmp_rhs12_.t
        d_759_cs_ = let_tmp_rhs12_.cs
        let_tmp_rhs13_ = default__.WS(d_759_cs_)
        d_760_after_ = let_tmp_rhs13_.t
        d_761_cs_ = let_tmp_rhs13_.cs
        return JSON_Utils_Cursors.Split_SP(JSON_Grammar.Structural_Structural(d_756_before_, d_758_val_, d_760_after_), d_761_cs_)

    @_dafny.classproperty
    def SpecView(instance):
        def lambda52_(d_762_v_):
            return JSON_ConcreteSyntax_Spec.default__.View(d_762_v_)

        return lambda52_

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
