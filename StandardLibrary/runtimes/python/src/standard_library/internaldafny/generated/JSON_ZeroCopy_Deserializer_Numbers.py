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

# Module: JSON_ZeroCopy_Deserializer_Numbers

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

