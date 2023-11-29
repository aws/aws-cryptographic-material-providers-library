import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
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
import StandardLibrary_mUInt
import String
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
import DafnyLibraries
import JSON_mUtils_mViews_mCore
import JSON_mUtils_mViews_mWriters
import JSON_mUtils_mViews
import JSON_mUtils_mLexers_mCore
import JSON_mUtils_mLexers_mStrings
import JSON_mUtils_mLexers
import JSON_mUtils_mCursors
import JSON_mUtils_mParsers
import JSON_mUtils_mStr_mCharStrConversion
import JSON_mUtils_mStr_mCharStrEscaping
import JSON_mUtils_mStr
import JSON_mUtils_mSeq
import JSON_mUtils_mVectors
import JSON_mUtils
import JSON_mErrors
import JSON_mValues
import JSON_mSpec
import JSON_mGrammar
import JSON_mSerializer_mByteStrConversion
import JSON_mSerializer
import JSON_mDeserializer_mUint16StrConversion
import JSON_mDeserializer_mByteStrConversion
import JSON_mDeserializer
import JSON_mConcreteSyntax_mSpec
import JSON_mConcreteSyntax_mSpecProperties
import JSON_mConcreteSyntax
import JSON_mZeroCopy_mSerializer
import JSON_mZeroCopy_mDeserializer_mCore
import JSON_mZeroCopy_mDeserializer_mStrings

# assert "JSON_mZeroCopy_mDeserializer_mNumbers" == __name__
JSON_mZeroCopy_mDeserializer_mNumbers = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Digits(cs):
        return ((cs).SkipWhile(JSON_mGrammar.default__.Digit_q)).Split()

    @staticmethod
    def NonEmptyDigits(cs):
        d_667_sp_ = JSON_mZeroCopy_mDeserializer_mNumbers.default__.Digits(cs)
        d_668_valueOrError0_ = Wrappers.default__.Need(not(((d_667_sp_).t).Empty_q), JSON_mUtils_mCursors.CursorError_OtherError(JSON_mErrors.DeserializationError_EmptyNumber()))
        if (d_668_valueOrError0_).IsFailure():
            return (d_668_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(d_667_sp_)

    @staticmethod
    def NonZeroInt(cs):
        return JSON_mZeroCopy_mDeserializer_mNumbers.default__.NonEmptyDigits(cs)

    @staticmethod
    def OptionalMinus(cs):
        def lambda51_(d_669_c_):
            return (d_669_c_) == (ord('-'))

        return ((cs).SkipIf(lambda51_)).Split()

    @staticmethod
    def OptionalSign(cs):
        def lambda52_(d_670_c_):
            return ((d_670_c_) == (ord('-'))) or ((d_670_c_) == (ord('+')))

        return ((cs).SkipIf(lambda52_)).Split()

    @staticmethod
    def TrimmedInt(cs):
        def lambda53_(d_672_c_):
            return (d_672_c_) == (ord('0'))

        d_671_sp_ = ((cs).SkipIf(lambda53_)).Split()
        if ((d_671_sp_).t).Empty_q:
            return JSON_mZeroCopy_mDeserializer_mNumbers.default__.NonZeroInt((d_671_sp_).cs)
        elif True:
            return Wrappers.Result_Success(d_671_sp_)

    @staticmethod
    def Exp(cs):
        def lambda54_(d_673_c_):
            return ((d_673_c_) == (ord('e'))) or ((d_673_c_) == (ord('E')))

        let_tmp_rhs11_ = ((cs).SkipIf(lambda54_)).Split()
        d_674_e_ = let_tmp_rhs11_.t
        d_675_cs_ = let_tmp_rhs11_.cs
        if (d_674_e_).Empty_q:
            return Wrappers.Result_Success(JSON_mUtils_mCursors.Split_SP(JSON_mGrammar.Maybe_Empty(), d_675_cs_))
        elif True:
            let_tmp_rhs12_ = JSON_mZeroCopy_mDeserializer_mNumbers.default__.OptionalSign(d_675_cs_)
            d_676_sign_ = let_tmp_rhs12_.t
            d_677_cs_ = let_tmp_rhs12_.cs
            d_678_valueOrError0_ = JSON_mZeroCopy_mDeserializer_mNumbers.default__.NonEmptyDigits(d_677_cs_)
            if (d_678_valueOrError0_).IsFailure():
                return (d_678_valueOrError0_).PropagateFailure()
            elif True:
                let_tmp_rhs13_ = (d_678_valueOrError0_).Extract()
                d_679_num_ = let_tmp_rhs13_.t
                d_680_cs_ = let_tmp_rhs13_.cs
                return Wrappers.Result_Success(JSON_mUtils_mCursors.Split_SP(JSON_mGrammar.Maybe_NonEmpty(JSON_mGrammar.jexp_JExp(d_674_e_, d_676_sign_, d_679_num_)), d_680_cs_))

    @staticmethod
    def Frac(cs):
        def lambda55_(d_681_c_):
            return (d_681_c_) == (ord('.'))

        let_tmp_rhs14_ = ((cs).SkipIf(lambda55_)).Split()
        d_682_period_ = let_tmp_rhs14_.t
        d_683_cs_ = let_tmp_rhs14_.cs
        if (d_682_period_).Empty_q:
            return Wrappers.Result_Success(JSON_mUtils_mCursors.Split_SP(JSON_mGrammar.Maybe_Empty(), d_683_cs_))
        elif True:
            d_684_valueOrError0_ = JSON_mZeroCopy_mDeserializer_mNumbers.default__.NonEmptyDigits(d_683_cs_)
            if (d_684_valueOrError0_).IsFailure():
                return (d_684_valueOrError0_).PropagateFailure()
            elif True:
                let_tmp_rhs15_ = (d_684_valueOrError0_).Extract()
                d_685_num_ = let_tmp_rhs15_.t
                d_686_cs_ = let_tmp_rhs15_.cs
                return Wrappers.Result_Success(JSON_mUtils_mCursors.Split_SP(JSON_mGrammar.Maybe_NonEmpty(JSON_mGrammar.jfrac_JFrac(d_682_period_, d_685_num_)), d_686_cs_))

    @staticmethod
    def NumberFromParts(minus, num, frac, exp):
        d_687_sp_ = JSON_mUtils_mCursors.Split_SP(JSON_mGrammar.jnumber_JNumber((minus).t, (num).t, (frac).t, (exp).t), (exp).cs)
        return d_687_sp_

    @staticmethod
    def Number(cs):
        d_688_minus_ = JSON_mZeroCopy_mDeserializer_mNumbers.default__.OptionalMinus(cs)
        d_689_valueOrError0_ = JSON_mZeroCopy_mDeserializer_mNumbers.default__.TrimmedInt((d_688_minus_).cs)
        if (d_689_valueOrError0_).IsFailure():
            return (d_689_valueOrError0_).PropagateFailure()
        elif True:
            d_690_num_ = (d_689_valueOrError0_).Extract()
            d_691_valueOrError1_ = JSON_mZeroCopy_mDeserializer_mNumbers.default__.Frac((d_690_num_).cs)
            if (d_691_valueOrError1_).IsFailure():
                return (d_691_valueOrError1_).PropagateFailure()
            elif True:
                d_692_frac_ = (d_691_valueOrError1_).Extract()
                d_693_valueOrError2_ = JSON_mZeroCopy_mDeserializer_mNumbers.default__.Exp((d_692_frac_).cs)
                if (d_693_valueOrError2_).IsFailure():
                    return (d_693_valueOrError2_).PropagateFailure()
                elif True:
                    d_694_exp_ = (d_693_valueOrError2_).Extract()
                    return Wrappers.Result_Success(JSON_mZeroCopy_mDeserializer_mNumbers.default__.NumberFromParts(d_688_minus_, d_690_num_, d_692_frac_, d_694_exp_))

