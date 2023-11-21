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

assert "JSON_mSpec" == __name__
JSON_mSpec = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EscapeUnicode(c):
        d_412_sStr_ = JSON_mUtils_mStr.default__.OfNat(c, 16)
        d_413_s_ = UnicodeStrings.default__.ASCIIToUTF16(d_412_sStr_)
        return (d_413_s_) + (_dafny.Seq([ord(' ') for d_414___v0_ in range((4) - (len(d_413_s_)))]))

    @staticmethod
    def Escape(str, start):
        d_415___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                pat_let_tv2_ = str
                pat_let_tv3_ = start
                if (start) >= (len(str)):
                    return (d_415___accumulator_) + (_dafny.Seq([]))
                elif True:
                    def iife2_(_pat_let1_0):
                        def iife3_(d_416_c_):
                            return ((UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\u"))) + (JSON_mSpec.default__.EscapeUnicode(d_416_c_)) if (d_416_c_) < (31) else _dafny.Seq([(pat_let_tv2_)[pat_let_tv3_]]))
                        return iife3_(_pat_let1_0)
                    d_415___accumulator_ = (d_415___accumulator_) + ((UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\\"")) if ((str)[start]) == (34) else (UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\\\")) if ((str)[start]) == (92) else (UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\b")) if ((str)[start]) == (8) else (UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\f")) if ((str)[start]) == (12) else (UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\n")) if ((str)[start]) == (10) else (UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\r")) if ((str)[start]) == (13) else (UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\t")) if ((str)[start]) == (9) else iife2_((str)[start])))))))))
                    in101_ = str
                    in102_ = (start) + (1)
                    str = in101_
                    start = in102_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def EscapeToUTF8(str, start):
        d_417_valueOrError0_ = (UnicodeStrings.default__.ToUTF16Checked(str)).ToResult_k(JSON_mErrors.SerializationError_InvalidUnicode())
        if (d_417_valueOrError0_).IsFailure():
            return (d_417_valueOrError0_).PropagateFailure()
        elif True:
            d_418_utf16_ = (d_417_valueOrError0_).Extract()
            d_419_escaped_ = JSON_mSpec.default__.Escape(d_418_utf16_, 0)
            d_420_valueOrError1_ = (UnicodeStrings.default__.FromUTF16Checked(d_419_escaped_)).ToResult_k(JSON_mErrors.SerializationError_InvalidUnicode())
            if (d_420_valueOrError1_).IsFailure():
                return (d_420_valueOrError1_).PropagateFailure()
            elif True:
                d_421_utf32_ = (d_420_valueOrError1_).Extract()
                return (UnicodeStrings.default__.ToUTF8Checked(d_421_utf32_)).ToResult_k(JSON_mErrors.SerializationError_InvalidUnicode())

    @staticmethod
    def String(str):
        d_422_valueOrError0_ = JSON_mSpec.default__.EscapeToUTF8(str, 0)
        if (d_422_valueOrError0_).IsFailure():
            return (d_422_valueOrError0_).PropagateFailure()
        elif True:
            d_423_inBytes_ = (d_422_valueOrError0_).Extract()
            return Wrappers.Result_Success(((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("\""))) + (d_423_inBytes_)) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("\""))))

    @staticmethod
    def IntToBytes(n):
        d_424_s_ = JSON_mUtils_mStr.default__.OfInt(n, 10)
        return UnicodeStrings.default__.ASCIIToUTF8(d_424_s_)

    @staticmethod
    def Number(dec):
        return Wrappers.Result_Success((JSON_mSpec.default__.IntToBytes((dec).n)) + ((_dafny.Seq([]) if ((dec).e10) == (0) else (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("e"))) + (JSON_mSpec.default__.IntToBytes((dec).e10)))))

    @staticmethod
    def KeyValue(kv):
        d_425_valueOrError0_ = JSON_mSpec.default__.String((kv)[0])
        if (d_425_valueOrError0_).IsFailure():
            return (d_425_valueOrError0_).PropagateFailure()
        elif True:
            d_426_key_ = (d_425_valueOrError0_).Extract()
            d_427_valueOrError1_ = JSON_mSpec.default__.JSON((kv)[1])
            if (d_427_valueOrError1_).IsFailure():
                return (d_427_valueOrError1_).PropagateFailure()
            elif True:
                d_428_value_ = (d_427_valueOrError1_).Extract()
                return Wrappers.Result_Success(((d_426_key_) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq(":")))) + (d_428_value_))

    @staticmethod
    def Join(sep, items):
        if (len(items)) == (0):
            return Wrappers.Result_Success(_dafny.Seq([]))
        elif True:
            d_429_valueOrError0_ = (items)[0]
            if (d_429_valueOrError0_).IsFailure():
                return (d_429_valueOrError0_).PropagateFailure()
            elif True:
                d_430_first_ = (d_429_valueOrError0_).Extract()
                if (len(items)) == (1):
                    return Wrappers.Result_Success(d_430_first_)
                elif True:
                    d_431_valueOrError1_ = JSON_mSpec.default__.Join(sep, _dafny.Seq((items)[1::]))
                    if (d_431_valueOrError1_).IsFailure():
                        return (d_431_valueOrError1_).PropagateFailure()
                    elif True:
                        d_432_rest_ = (d_431_valueOrError1_).Extract()
                        return Wrappers.Result_Success(((d_430_first_) + (sep)) + (d_432_rest_))

    @staticmethod
    def Object(obj):
        d_433_valueOrError0_ = JSON_mSpec.default__.Join(UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq(",")), _dafny.Seq([JSON_mSpec.default__.KeyValue((obj)[d_434_i_]) for d_434_i_ in range(len(obj))]))
        if (d_433_valueOrError0_).IsFailure():
            return (d_433_valueOrError0_).PropagateFailure()
        elif True:
            d_435_middle_ = (d_433_valueOrError0_).Extract()
            return Wrappers.Result_Success(((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("{"))) + (d_435_middle_)) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("}"))))

    @staticmethod
    def Array(arr):
        d_436_valueOrError0_ = JSON_mSpec.default__.Join(UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq(",")), _dafny.Seq([JSON_mSpec.default__.JSON((arr)[d_437_i_]) for d_437_i_ in range(len(arr))]))
        if (d_436_valueOrError0_).IsFailure():
            return (d_436_valueOrError0_).PropagateFailure()
        elif True:
            d_438_middle_ = (d_436_valueOrError0_).Extract()
            return Wrappers.Result_Success(((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("["))) + (d_438_middle_)) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("]"))))

    @staticmethod
    def JSON(js):
        source11_ = js
        if source11_.is_Null:
            return Wrappers.Result_Success(UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("null")))
        elif source11_.is_Bool:
            d_439___mcc_h0_ = source11_.b
            d_440_b_ = d_439___mcc_h0_
            return Wrappers.Result_Success((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("true")) if d_440_b_ else UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("false"))))
        elif source11_.is_String:
            d_441___mcc_h1_ = source11_.str
            d_442_str_ = d_441___mcc_h1_
            return JSON_mSpec.default__.String(d_442_str_)
        elif source11_.is_Number:
            d_443___mcc_h2_ = source11_.num
            d_444_dec_ = d_443___mcc_h2_
            return JSON_mSpec.default__.Number(d_444_dec_)
        elif source11_.is_Object:
            d_445___mcc_h3_ = source11_.obj
            d_446_obj_ = d_445___mcc_h3_
            return JSON_mSpec.default__.Object(d_446_obj_)
        elif True:
            d_447___mcc_h4_ = source11_.arr
            d_448_arr_ = d_447___mcc_h4_
            return JSON_mSpec.default__.Array(d_448_arr_)

