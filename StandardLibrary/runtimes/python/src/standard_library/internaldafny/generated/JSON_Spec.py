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

# Module: standard_library.internaldafny.generated.JSON_Spec

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EscapeUnicode(c):
        d_521_sStr_ = JSON_Utils_Str.default__.OfNat(c, 16)
        d_522_s_ = UnicodeStrings.default__.ASCIIToUTF16(d_521_sStr_)
        return (d_522_s_) + (_dafny.Seq([ord(' ') for d_523___v0_ in range((4) - (len(d_522_s_)))]))

    @staticmethod
    def Escape(str, start):
        d_524___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                pat_let_tv4_ = str
                pat_let_tv5_ = start
                def iife12_(_pat_let6_0):
                    def iife13_(d_525_c_):
                        return ((UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\u"))) + (default__.EscapeUnicode(d_525_c_)) if (d_525_c_) < (31) else _dafny.Seq([(pat_let_tv4_)[pat_let_tv5_]]))
                    return iife13_(_pat_let6_0)
                if (start) >= (len(str)):
                    return (d_524___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_524___accumulator_ = (d_524___accumulator_) + ((UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\\"")) if ((str)[start]) == (34) else (UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\\\")) if ((str)[start]) == (92) else (UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\b")) if ((str)[start]) == (8) else (UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\f")) if ((str)[start]) == (12) else (UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\n")) if ((str)[start]) == (10) else (UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\r")) if ((str)[start]) == (13) else (UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\t")) if ((str)[start]) == (9) else iife12_((str)[start])))))))))
                    in204_ = str
                    in205_ = (start) + (1)
                    str = in204_
                    start = in205_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def EscapeToUTF8(str, start):
        d_526_valueOrError0_ = (UnicodeStrings.default__.ToUTF16Checked(str)).ToResult_k(JSON_Errors.SerializationError_InvalidUnicode())
        if (d_526_valueOrError0_).IsFailure():
            return (d_526_valueOrError0_).PropagateFailure()
        elif True:
            d_527_utf16_ = (d_526_valueOrError0_).Extract()
            d_528_escaped_ = default__.Escape(d_527_utf16_, 0)
            d_529_valueOrError1_ = (UnicodeStrings.default__.FromUTF16Checked(d_528_escaped_)).ToResult_k(JSON_Errors.SerializationError_InvalidUnicode())
            if (d_529_valueOrError1_).IsFailure():
                return (d_529_valueOrError1_).PropagateFailure()
            elif True:
                d_530_utf32_ = (d_529_valueOrError1_).Extract()
                return (UnicodeStrings.default__.ToUTF8Checked(d_530_utf32_)).ToResult_k(JSON_Errors.SerializationError_InvalidUnicode())

    @staticmethod
    def String(str):
        d_531_valueOrError0_ = default__.EscapeToUTF8(str, 0)
        if (d_531_valueOrError0_).IsFailure():
            return (d_531_valueOrError0_).PropagateFailure()
        elif True:
            d_532_inBytes_ = (d_531_valueOrError0_).Extract()
            return Wrappers.Result_Success(((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("\""))) + (d_532_inBytes_)) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("\""))))

    @staticmethod
    def IntToBytes(n):
        d_533_s_ = JSON_Utils_Str.default__.OfInt(n, 10)
        return UnicodeStrings.default__.ASCIIToUTF8(d_533_s_)

    @staticmethod
    def Number(dec):
        return Wrappers.Result_Success((default__.IntToBytes((dec).n)) + ((_dafny.Seq([]) if ((dec).e10) == (0) else (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("e"))) + (default__.IntToBytes((dec).e10)))))

    @staticmethod
    def KeyValue(kv):
        d_534_valueOrError0_ = default__.String((kv)[0])
        if (d_534_valueOrError0_).IsFailure():
            return (d_534_valueOrError0_).PropagateFailure()
        elif True:
            d_535_key_ = (d_534_valueOrError0_).Extract()
            d_536_valueOrError1_ = default__.JSON((kv)[1])
            if (d_536_valueOrError1_).IsFailure():
                return (d_536_valueOrError1_).PropagateFailure()
            elif True:
                d_537_value_ = (d_536_valueOrError1_).Extract()
                return Wrappers.Result_Success(((d_535_key_) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq(":")))) + (d_537_value_))

    @staticmethod
    def Join(sep, items):
        if (len(items)) == (0):
            return Wrappers.Result_Success(_dafny.Seq([]))
        elif True:
            d_538_valueOrError0_ = (items)[0]
            if (d_538_valueOrError0_).IsFailure():
                return (d_538_valueOrError0_).PropagateFailure()
            elif True:
                d_539_first_ = (d_538_valueOrError0_).Extract()
                if (len(items)) == (1):
                    return Wrappers.Result_Success(d_539_first_)
                elif True:
                    d_540_valueOrError1_ = default__.Join(sep, _dafny.Seq((items)[1::]))
                    if (d_540_valueOrError1_).IsFailure():
                        return (d_540_valueOrError1_).PropagateFailure()
                    elif True:
                        d_541_rest_ = (d_540_valueOrError1_).Extract()
                        return Wrappers.Result_Success(((d_539_first_) + (sep)) + (d_541_rest_))

    @staticmethod
    def Object(obj):
        d_542_valueOrError0_ = default__.Join(UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq(",")), _dafny.Seq([default__.KeyValue((obj)[d_543_i_]) for d_543_i_ in range(len(obj))]))
        if (d_542_valueOrError0_).IsFailure():
            return (d_542_valueOrError0_).PropagateFailure()
        elif True:
            d_544_middle_ = (d_542_valueOrError0_).Extract()
            return Wrappers.Result_Success(((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("{"))) + (d_544_middle_)) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("}"))))

    @staticmethod
    def Array(arr):
        d_545_valueOrError0_ = default__.Join(UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq(",")), _dafny.Seq([default__.JSON((arr)[d_546_i_]) for d_546_i_ in range(len(arr))]))
        if (d_545_valueOrError0_).IsFailure():
            return (d_545_valueOrError0_).PropagateFailure()
        elif True:
            d_547_middle_ = (d_545_valueOrError0_).Extract()
            return Wrappers.Result_Success(((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("["))) + (d_547_middle_)) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("]"))))

    @staticmethod
    def JSON(js):
        source11_ = js
        if source11_.is_Null:
            return Wrappers.Result_Success(UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("null")))
        elif source11_.is_Bool:
            d_548___mcc_h0_ = source11_.b
            d_549_b_ = d_548___mcc_h0_
            return Wrappers.Result_Success((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("true")) if d_549_b_ else UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("false"))))
        elif source11_.is_String:
            d_550___mcc_h1_ = source11_.str
            d_551_str_ = d_550___mcc_h1_
            return default__.String(d_551_str_)
        elif source11_.is_Number:
            d_552___mcc_h2_ = source11_.num
            d_553_dec_ = d_552___mcc_h2_
            return default__.Number(d_553_dec_)
        elif source11_.is_Object:
            d_554___mcc_h3_ = source11_.obj
            d_555_obj_ = d_554___mcc_h3_
            return default__.Object(d_555_obj_)
        elif True:
            d_556___mcc_h4_ = source11_.arr
            d_557_arr_ = d_556___mcc_h4_
            return default__.Array(d_557_arr_)

