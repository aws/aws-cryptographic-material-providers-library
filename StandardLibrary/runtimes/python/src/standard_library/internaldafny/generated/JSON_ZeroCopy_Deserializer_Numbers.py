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
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Strings as JSON_ZeroCopy_Deserializer_Strings

# Module: standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Numbers

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Digits(cs):
        return ((cs).SkipWhile(JSON_Grammar.default__.Digit_q)).Split()

    @staticmethod
    def NonEmptyDigits(cs):
        d_778_sp_ = default__.Digits(cs)
        d_779_valueOrError0_ = Wrappers.default__.Need(not(((d_778_sp_).t).Empty_q), JSON_Utils_Cursors.CursorError_OtherError(JSON_Errors.DeserializationError_EmptyNumber()))
        if (d_779_valueOrError0_).IsFailure():
            return (d_779_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(d_778_sp_)

    @staticmethod
    def NonZeroInt(cs):
        return default__.NonEmptyDigits(cs)

    @staticmethod
    def OptionalMinus(cs):
        def lambda53_(d_780_c_):
            return (d_780_c_) == (ord('-'))

        return ((cs).SkipIf(lambda53_)).Split()

    @staticmethod
    def OptionalSign(cs):
        def lambda54_(d_781_c_):
            return ((d_781_c_) == (ord('-'))) or ((d_781_c_) == (ord('+')))

        return ((cs).SkipIf(lambda54_)).Split()

    @staticmethod
    def TrimmedInt(cs):
        def lambda55_(d_783_c_):
            return (d_783_c_) == (ord('0'))

        d_782_sp_ = ((cs).SkipIf(lambda55_)).Split()
        if ((d_782_sp_).t).Empty_q:
            return default__.NonZeroInt((d_782_sp_).cs)
        elif True:
            return Wrappers.Result_Success(d_782_sp_)

    @staticmethod
    def Exp(cs):
        def lambda56_(d_784_c_):
            return ((d_784_c_) == (ord('e'))) or ((d_784_c_) == (ord('E')))

        let_tmp_rhs17_ = ((cs).SkipIf(lambda56_)).Split()
        d_785_e_ = let_tmp_rhs17_.t
        d_786_cs_ = let_tmp_rhs17_.cs
        if (d_785_e_).Empty_q:
            return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_Empty(), d_786_cs_))
        elif True:
            let_tmp_rhs18_ = default__.OptionalSign(d_786_cs_)
            d_787_sign_ = let_tmp_rhs18_.t
            d_788_cs_ = let_tmp_rhs18_.cs
            d_789_valueOrError0_ = default__.NonEmptyDigits(d_788_cs_)
            if (d_789_valueOrError0_).IsFailure():
                return (d_789_valueOrError0_).PropagateFailure()
            elif True:
                let_tmp_rhs19_ = (d_789_valueOrError0_).Extract()
                d_790_num_ = let_tmp_rhs19_.t
                d_791_cs_ = let_tmp_rhs19_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_NonEmpty(JSON_Grammar.jexp_JExp(d_785_e_, d_787_sign_, d_790_num_)), d_791_cs_))

    @staticmethod
    def Frac(cs):
        def lambda57_(d_792_c_):
            return (d_792_c_) == (ord('.'))

        let_tmp_rhs20_ = ((cs).SkipIf(lambda57_)).Split()
        d_793_period_ = let_tmp_rhs20_.t
        d_794_cs_ = let_tmp_rhs20_.cs
        if (d_793_period_).Empty_q:
            return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_Empty(), d_794_cs_))
        elif True:
            d_795_valueOrError0_ = default__.NonEmptyDigits(d_794_cs_)
            if (d_795_valueOrError0_).IsFailure():
                return (d_795_valueOrError0_).PropagateFailure()
            elif True:
                let_tmp_rhs21_ = (d_795_valueOrError0_).Extract()
                d_796_num_ = let_tmp_rhs21_.t
                d_797_cs_ = let_tmp_rhs21_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_NonEmpty(JSON_Grammar.jfrac_JFrac(d_793_period_, d_796_num_)), d_797_cs_))

    @staticmethod
    def NumberFromParts(minus, num, frac, exp):
        d_798_sp_ = JSON_Utils_Cursors.Split_SP(JSON_Grammar.jnumber_JNumber((minus).t, (num).t, (frac).t, (exp).t), (exp).cs)
        return d_798_sp_

    @staticmethod
    def Number(cs):
        d_799_minus_ = default__.OptionalMinus(cs)
        d_800_valueOrError0_ = default__.TrimmedInt((d_799_minus_).cs)
        if (d_800_valueOrError0_).IsFailure():
            return (d_800_valueOrError0_).PropagateFailure()
        elif True:
            d_801_num_ = (d_800_valueOrError0_).Extract()
            d_802_valueOrError1_ = default__.Frac((d_801_num_).cs)
            if (d_802_valueOrError1_).IsFailure():
                return (d_802_valueOrError1_).PropagateFailure()
            elif True:
                d_803_frac_ = (d_802_valueOrError1_).Extract()
                d_804_valueOrError2_ = default__.Exp((d_803_frac_).cs)
                if (d_804_valueOrError2_).IsFailure():
                    return (d_804_valueOrError2_).PropagateFailure()
                elif True:
                    d_805_exp_ = (d_804_valueOrError2_).Extract()
                    return Wrappers.Result_Success(default__.NumberFromParts(d_799_minus_, d_801_num_, d_803_frac_, d_805_exp_))

