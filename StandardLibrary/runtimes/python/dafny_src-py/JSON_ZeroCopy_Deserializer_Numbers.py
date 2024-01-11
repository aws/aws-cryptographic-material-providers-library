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
        d_667_sp_ = default__.Digits(cs)
        d_668_valueOrError0_ = Wrappers.default__.Need(not(((d_667_sp_).t).Empty_q), JSON_Utils_Cursors.CursorError_OtherError(JSON_Errors.DeserializationError_EmptyNumber()))
        if (d_668_valueOrError0_).IsFailure():
            return (d_668_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(d_667_sp_)

    @staticmethod
    def NonZeroInt(cs):
        return default__.NonEmptyDigits(cs)

    @staticmethod
    def OptionalMinus(cs):
        def lambda50_(d_669_c_):
            return (d_669_c_) == (ord('-'))

        return ((cs).SkipIf(lambda50_)).Split()

    @staticmethod
    def OptionalSign(cs):
        def lambda51_(d_670_c_):
            return ((d_670_c_) == (ord('-'))) or ((d_670_c_) == (ord('+')))

        return ((cs).SkipIf(lambda51_)).Split()

    @staticmethod
    def TrimmedInt(cs):
        def lambda52_(d_672_c_):
            return (d_672_c_) == (ord('0'))

        d_671_sp_ = ((cs).SkipIf(lambda52_)).Split()
        if ((d_671_sp_).t).Empty_q:
            return default__.NonZeroInt((d_671_sp_).cs)
        elif True:
            return Wrappers.Result_Success(d_671_sp_)

    @staticmethod
    def Exp(cs):
        def lambda53_(d_673_c_):
            return ((d_673_c_) == (ord('e'))) or ((d_673_c_) == (ord('E')))

        let_tmp_rhs11_ = ((cs).SkipIf(lambda53_)).Split()
        d_674_e_ = let_tmp_rhs11_.t
        d_675_cs_ = let_tmp_rhs11_.cs
        if (d_674_e_).Empty_q:
            return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_Empty(), d_675_cs_))
        elif True:
            let_tmp_rhs12_ = default__.OptionalSign(d_675_cs_)
            d_676_sign_ = let_tmp_rhs12_.t
            d_677_cs_ = let_tmp_rhs12_.cs
            d_678_valueOrError0_ = default__.NonEmptyDigits(d_677_cs_)
            if (d_678_valueOrError0_).IsFailure():
                return (d_678_valueOrError0_).PropagateFailure()
            elif True:
                let_tmp_rhs13_ = (d_678_valueOrError0_).Extract()
                d_679_num_ = let_tmp_rhs13_.t
                d_680_cs_ = let_tmp_rhs13_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_NonEmpty(JSON_Grammar.jexp_JExp(d_674_e_, d_676_sign_, d_679_num_)), d_680_cs_))

    @staticmethod
    def Frac(cs):
        def lambda54_(d_681_c_):
            return (d_681_c_) == (ord('.'))

        let_tmp_rhs14_ = ((cs).SkipIf(lambda54_)).Split()
        d_682_period_ = let_tmp_rhs14_.t
        d_683_cs_ = let_tmp_rhs14_.cs
        if (d_682_period_).Empty_q:
            return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_Empty(), d_683_cs_))
        elif True:
            d_684_valueOrError0_ = default__.NonEmptyDigits(d_683_cs_)
            if (d_684_valueOrError0_).IsFailure():
                return (d_684_valueOrError0_).PropagateFailure()
            elif True:
                let_tmp_rhs15_ = (d_684_valueOrError0_).Extract()
                d_685_num_ = let_tmp_rhs15_.t
                d_686_cs_ = let_tmp_rhs15_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_NonEmpty(JSON_Grammar.jfrac_JFrac(d_682_period_, d_685_num_)), d_686_cs_))

    @staticmethod
    def NumberFromParts(minus, num, frac, exp):
        d_687_sp_ = JSON_Utils_Cursors.Split_SP(JSON_Grammar.jnumber_JNumber((minus).t, (num).t, (frac).t, (exp).t), (exp).cs)
        return d_687_sp_

    @staticmethod
    def Number(cs):
        d_688_minus_ = default__.OptionalMinus(cs)
        d_689_valueOrError0_ = default__.TrimmedInt((d_688_minus_).cs)
        if (d_689_valueOrError0_).IsFailure():
            return (d_689_valueOrError0_).PropagateFailure()
        elif True:
            d_690_num_ = (d_689_valueOrError0_).Extract()
            d_691_valueOrError1_ = default__.Frac((d_690_num_).cs)
            if (d_691_valueOrError1_).IsFailure():
                return (d_691_valueOrError1_).PropagateFailure()
            elif True:
                d_692_frac_ = (d_691_valueOrError1_).Extract()
                d_693_valueOrError2_ = default__.Exp((d_692_frac_).cs)
                if (d_693_valueOrError2_).IsFailure():
                    return (d_693_valueOrError2_).PropagateFailure()
                elif True:
                    d_694_exp_ = (d_693_valueOrError2_).Extract()
                    return Wrappers.Result_Success(default__.NumberFromParts(d_688_minus_, d_690_num_, d_692_frac_, d_694_exp_))

