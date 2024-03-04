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
        d_752_sp_ = default__.Digits(cs)
        d_753_valueOrError0_ = Wrappers.default__.Need(not(((d_752_sp_).t).Empty_q), JSON_Utils_Cursors.CursorError_OtherError(JSON_Errors.DeserializationError_EmptyNumber()))
        if (d_753_valueOrError0_).IsFailure():
            return (d_753_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(d_752_sp_)

    @staticmethod
    def NonZeroInt(cs):
        return default__.NonEmptyDigits(cs)

    @staticmethod
    def OptionalMinus(cs):
        def lambda52_(d_754_c_):
            return (d_754_c_) == (ord('-'))

        return ((cs).SkipIf(lambda52_)).Split()

    @staticmethod
    def OptionalSign(cs):
        def lambda53_(d_755_c_):
            return ((d_755_c_) == (ord('-'))) or ((d_755_c_) == (ord('+')))

        return ((cs).SkipIf(lambda53_)).Split()

    @staticmethod
    def TrimmedInt(cs):
        def lambda54_(d_757_c_):
            return (d_757_c_) == (ord('0'))

        d_756_sp_ = ((cs).SkipIf(lambda54_)).Split()
        if ((d_756_sp_).t).Empty_q:
            return default__.NonZeroInt((d_756_sp_).cs)
        elif True:
            return Wrappers.Result_Success(d_756_sp_)

    @staticmethod
    def Exp(cs):
        def lambda55_(d_758_c_):
            return ((d_758_c_) == (ord('e'))) or ((d_758_c_) == (ord('E')))

        let_tmp_rhs17_ = ((cs).SkipIf(lambda55_)).Split()
        d_759_e_ = let_tmp_rhs17_.t
        d_760_cs_ = let_tmp_rhs17_.cs
        if (d_759_e_).Empty_q:
            return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_Empty(), d_760_cs_))
        elif True:
            let_tmp_rhs18_ = default__.OptionalSign(d_760_cs_)
            d_761_sign_ = let_tmp_rhs18_.t
            d_762_cs_ = let_tmp_rhs18_.cs
            d_763_valueOrError0_ = default__.NonEmptyDigits(d_762_cs_)
            if (d_763_valueOrError0_).IsFailure():
                return (d_763_valueOrError0_).PropagateFailure()
            elif True:
                let_tmp_rhs19_ = (d_763_valueOrError0_).Extract()
                d_764_num_ = let_tmp_rhs19_.t
                d_765_cs_ = let_tmp_rhs19_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_NonEmpty(JSON_Grammar.jexp_JExp(d_759_e_, d_761_sign_, d_764_num_)), d_765_cs_))

    @staticmethod
    def Frac(cs):
        def lambda56_(d_766_c_):
            return (d_766_c_) == (ord('.'))

        let_tmp_rhs20_ = ((cs).SkipIf(lambda56_)).Split()
        d_767_period_ = let_tmp_rhs20_.t
        d_768_cs_ = let_tmp_rhs20_.cs
        if (d_767_period_).Empty_q:
            return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_Empty(), d_768_cs_))
        elif True:
            d_769_valueOrError0_ = default__.NonEmptyDigits(d_768_cs_)
            if (d_769_valueOrError0_).IsFailure():
                return (d_769_valueOrError0_).PropagateFailure()
            elif True:
                let_tmp_rhs21_ = (d_769_valueOrError0_).Extract()
                d_770_num_ = let_tmp_rhs21_.t
                d_771_cs_ = let_tmp_rhs21_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_NonEmpty(JSON_Grammar.jfrac_JFrac(d_767_period_, d_770_num_)), d_771_cs_))

    @staticmethod
    def NumberFromParts(minus, num, frac, exp):
        d_772_sp_ = JSON_Utils_Cursors.Split_SP(JSON_Grammar.jnumber_JNumber((minus).t, (num).t, (frac).t, (exp).t), (exp).cs)
        return d_772_sp_

    @staticmethod
    def Number(cs):
        d_773_minus_ = default__.OptionalMinus(cs)
        d_774_valueOrError0_ = default__.TrimmedInt((d_773_minus_).cs)
        if (d_774_valueOrError0_).IsFailure():
            return (d_774_valueOrError0_).PropagateFailure()
        elif True:
            d_775_num_ = (d_774_valueOrError0_).Extract()
            d_776_valueOrError1_ = default__.Frac((d_775_num_).cs)
            if (d_776_valueOrError1_).IsFailure():
                return (d_776_valueOrError1_).PropagateFailure()
            elif True:
                d_777_frac_ = (d_776_valueOrError1_).Extract()
                d_778_valueOrError2_ = default__.Exp((d_777_frac_).cs)
                if (d_778_valueOrError2_).IsFailure():
                    return (d_778_valueOrError2_).PropagateFailure()
                elif True:
                    d_779_exp_ = (d_778_valueOrError2_).Extract()
                    return Wrappers.Result_Success(default__.NumberFromParts(d_773_minus_, d_775_num_, d_777_frac_, d_779_exp_))

