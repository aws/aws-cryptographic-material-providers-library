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

# Module: JSON_ZeroCopy_Deserializer_Core

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Get(cs, err):
        d_686_valueOrError0_ = (cs).Get(err)
        if (d_686_valueOrError0_).IsFailure():
            return (d_686_valueOrError0_).PropagateFailure()
        elif True:
            d_687_cs_ = (d_686_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_687_cs_).Split())

    @staticmethod
    def WS(cs):
        sp: JSON_Utils_Cursors.Split = JSON_Utils_Cursors.Split.default(JSON_Grammar.jblanks.default)()
        d_688_point_k_: int
        d_688_point_k_ = (cs).point
        d_689_end_: int
        d_689_end_ = (cs).end
        while ((d_688_point_k_) < (d_689_end_)) and (JSON_Grammar.default__.Blank_q(((cs).s)[d_688_point_k_])):
            d_688_point_k_ = (d_688_point_k_) + (1)
        sp = (JSON_Utils_Cursors.Cursor___Cursor((cs).s, (cs).beg, d_688_point_k_, (cs).end)).Split()
        return sp
        return sp

    @staticmethod
    def Structural(cs, parser):
        let_tmp_rhs8_ = default__.WS(cs)
        d_690_before_ = let_tmp_rhs8_.t
        d_691_cs_ = let_tmp_rhs8_.cs
        d_692_valueOrError0_ = (parser).fn(d_691_cs_)
        if (d_692_valueOrError0_).IsFailure():
            return (d_692_valueOrError0_).PropagateFailure()
        elif True:
            let_tmp_rhs9_ = (d_692_valueOrError0_).Extract()
            d_693_val_ = let_tmp_rhs9_.t
            d_694_cs_ = let_tmp_rhs9_.cs
            let_tmp_rhs10_ = default__.WS(d_694_cs_)
            d_695_after_ = let_tmp_rhs10_.t
            d_696_cs_ = let_tmp_rhs10_.cs
            return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Structural_Structural(d_690_before_, d_693_val_, d_695_after_), d_696_cs_))

    @staticmethod
    def TryStructural(cs):
        let_tmp_rhs11_ = default__.WS(cs)
        d_697_before_ = let_tmp_rhs11_.t
        d_698_cs_ = let_tmp_rhs11_.cs
        let_tmp_rhs12_ = ((d_698_cs_).SkipByte()).Split()
        d_699_val_ = let_tmp_rhs12_.t
        d_700_cs_ = let_tmp_rhs12_.cs
        let_tmp_rhs13_ = default__.WS(d_700_cs_)
        d_701_after_ = let_tmp_rhs13_.t
        d_702_cs_ = let_tmp_rhs13_.cs
        return JSON_Utils_Cursors.Split_SP(JSON_Grammar.Structural_Structural(d_697_before_, d_699_val_, d_701_after_), d_702_cs_)

    @_dafny.classproperty
    def SpecView(instance):
        def lambda54_(d_703_v_):
            return JSON_ConcreteSyntax_Spec.default__.View(d_703_v_)

        return lambda54_

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
