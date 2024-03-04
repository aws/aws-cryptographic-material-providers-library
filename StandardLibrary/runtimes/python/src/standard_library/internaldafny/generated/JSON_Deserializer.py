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

# Module: JSON_Deserializer

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Bool(js):
        return ((js).At(0)) == (ord('t'))

    @staticmethod
    def UnsupportedEscape16(code):
        return JSON_Errors.DeserializationError_UnsupportedEscape((UnicodeStrings.default__.FromUTF16Checked(code)).UnwrapOr(_dafny.Seq("Couldn't decode UTF-16")))

    @staticmethod
    def ToNat16(str):
        d_597_hd_ = JSON_Deserializer_Uint16StrConversion.default__.ToNat__any(str, 16, default__.HEX__TABLE__16)
        return d_597_hd_

    @staticmethod
    def Unescape(str, start, prefix):
        while True:
            with _dafny.label():
                if (start) >= (len(str)):
                    return Wrappers.Result_Success(prefix)
                elif ((str)[start]) == (ord('\\')):
                    if (len(str)) == ((start) + (1)):
                        return Wrappers.Result_Failure(JSON_Errors.DeserializationError_EscapeAtEOS())
                    elif True:
                        d_598_c_ = (str)[(start) + (1)]
                        if (d_598_c_) == (ord('u')):
                            if (len(str)) <= ((start) + (6)):
                                return Wrappers.Result_Failure(JSON_Errors.DeserializationError_EscapeAtEOS())
                            elif True:
                                d_599_code_ = _dafny.Seq((str)[(start) + (2):(start) + (6):])
                                def lambda39_(exists_var_1_):
                                    d_600_c_: int = exists_var_1_
                                    return ((d_600_c_) in (d_599_code_)) and ((d_600_c_) not in (default__.HEX__TABLE__16))

                                if _dafny.quantifier((d_599_code_).UniqueElements, False, lambda39_):
                                    return Wrappers.Result_Failure(default__.UnsupportedEscape16(d_599_code_))
                                elif True:
                                    d_601_hd_ = default__.ToNat16(d_599_code_)
                                    in215_ = str
                                    in216_ = (start) + (6)
                                    in217_ = (prefix) + (_dafny.Seq([d_601_hd_]))
                                    str = in215_
                                    start = in216_
                                    prefix = in217_
                                    raise _dafny.TailCall()
                        elif True:
                            d_602_unescaped_ = (34 if (d_598_c_) == (34) else (92 if (d_598_c_) == (92) else (8 if (d_598_c_) == (98) else (12 if (d_598_c_) == (102) else (10 if (d_598_c_) == (110) else (13 if (d_598_c_) == (114) else (9 if (d_598_c_) == (116) else 0)))))))
                            if (d_602_unescaped_) == (0):
                                return Wrappers.Result_Failure(default__.UnsupportedEscape16(_dafny.Seq((str)[start:(start) + (2):])))
                            elif True:
                                in218_ = str
                                in219_ = (start) + (2)
                                in220_ = (prefix) + (_dafny.Seq([d_602_unescaped_]))
                                str = in218_
                                start = in219_
                                prefix = in220_
                                raise _dafny.TailCall()
                elif True:
                    in221_ = str
                    in222_ = (start) + (1)
                    in223_ = (prefix) + (_dafny.Seq([(str)[start]]))
                    str = in221_
                    start = in222_
                    prefix = in223_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def String(js):
        d_603_valueOrError0_ = (UnicodeStrings.default__.FromUTF8Checked(((js).contents).Bytes())).ToResult_k(JSON_Errors.DeserializationError_InvalidUnicode())
        if (d_603_valueOrError0_).IsFailure():
            return (d_603_valueOrError0_).PropagateFailure()
        elif True:
            d_604_asUtf32_ = (d_603_valueOrError0_).Extract()
            d_605_valueOrError1_ = (UnicodeStrings.default__.ToUTF16Checked(d_604_asUtf32_)).ToResult_k(JSON_Errors.DeserializationError_InvalidUnicode())
            if (d_605_valueOrError1_).IsFailure():
                return (d_605_valueOrError1_).PropagateFailure()
            elif True:
                d_606_asUint16_ = (d_605_valueOrError1_).Extract()
                d_607_valueOrError2_ = default__.Unescape(d_606_asUint16_, 0, _dafny.Seq([]))
                if (d_607_valueOrError2_).IsFailure():
                    return (d_607_valueOrError2_).PropagateFailure()
                elif True:
                    d_608_unescaped_ = (d_607_valueOrError2_).Extract()
                    return (UnicodeStrings.default__.FromUTF16Checked(d_608_unescaped_)).ToResult_k(JSON_Errors.DeserializationError_InvalidUnicode())

    @staticmethod
    def ToInt(sign, n):
        d_609_n_ = JSON_Deserializer_ByteStrConversion.default__.ToNat__any((n).Bytes(), 10, default__.DIGITS)
        return Wrappers.Result_Success(((0) - (d_609_n_) if (sign).Char_q('-') else d_609_n_))

    @staticmethod
    def Number(js):
        let_tmp_rhs7_ = js
        d_610_minus_ = let_tmp_rhs7_.minus
        d_611_num_ = let_tmp_rhs7_.num
        d_612_frac_ = let_tmp_rhs7_.frac
        d_613_exp_ = let_tmp_rhs7_.exp
        d_614_valueOrError0_ = default__.ToInt(d_610_minus_, d_611_num_)
        if (d_614_valueOrError0_).IsFailure():
            return (d_614_valueOrError0_).PropagateFailure()
        elif True:
            d_615_n_ = (d_614_valueOrError0_).Extract()
            def lambda40_(source13_):
                if source13_.is_Empty:
                    return Wrappers.Result_Success(0)
                elif True:
                    d_617___mcc_h0_ = source13_.t
                    source14_ = d_617___mcc_h0_
                    d_618___mcc_h1_ = source14_.e
                    d_619___mcc_h2_ = source14_.sign
                    d_620___mcc_h3_ = source14_.num
                    d_621_num_ = d_620___mcc_h3_
                    d_622_sign_ = d_619___mcc_h2_
                    return default__.ToInt(d_622_sign_, d_621_num_)

            d_616_valueOrError1_ = lambda40_(d_613_exp_)
            if (d_616_valueOrError1_).IsFailure():
                return (d_616_valueOrError1_).PropagateFailure()
            elif True:
                d_623_e10_ = (d_616_valueOrError1_).Extract()
                source15_ = d_612_frac_
                if source15_.is_Empty:
                    return Wrappers.Result_Success(JSON_Values.Decimal_Decimal(d_615_n_, d_623_e10_))
                elif True:
                    d_624___mcc_h4_ = source15_.t
                    source16_ = d_624___mcc_h4_
                    d_625___mcc_h5_ = source16_.period
                    d_626___mcc_h6_ = source16_.num
                    d_627_num_ = d_626___mcc_h6_
                    d_628_pow10_ = (d_627_num_).Length()
                    d_629_valueOrError2_ = default__.ToInt(d_610_minus_, d_627_num_)
                    if (d_629_valueOrError2_).IsFailure():
                        return (d_629_valueOrError2_).PropagateFailure()
                    elif True:
                        d_630_frac_ = (d_629_valueOrError2_).Extract()
                        return Wrappers.Result_Success(JSON_Values.Decimal_Decimal(((d_615_n_) * (Power.default__.Pow(10, d_628_pow10_))) + (d_630_frac_), (d_623_e10_) - (d_628_pow10_)))

    @staticmethod
    def KeyValue(js):
        d_631_valueOrError0_ = default__.String((js).k)
        if (d_631_valueOrError0_).IsFailure():
            return (d_631_valueOrError0_).PropagateFailure()
        elif True:
            d_632_k_ = (d_631_valueOrError0_).Extract()
            d_633_valueOrError1_ = default__.Value((js).v)
            if (d_633_valueOrError1_).IsFailure():
                return (d_633_valueOrError1_).PropagateFailure()
            elif True:
                d_634_v_ = (d_633_valueOrError1_).Extract()
                return Wrappers.Result_Success((d_632_k_, d_634_v_))

    @staticmethod
    def Object(js):
        def lambda41_(d_635_js_):
            def lambda42_(d_636_d_):
                return default__.KeyValue((d_636_d_).t)

            return lambda42_

        return Seq.default__.MapWithResult(lambda41_(js), (js).data)

    @staticmethod
    def Array(js):
        def lambda43_(d_637_js_):
            def lambda44_(d_638_d_):
                return default__.Value((d_638_d_).t)

            return lambda44_

        return Seq.default__.MapWithResult(lambda43_(js), (js).data)

    @staticmethod
    def Value(js):
        source17_ = js
        if source17_.is_Null:
            d_639___mcc_h0_ = source17_.n
            return Wrappers.Result_Success(JSON_Values.JSON_Null())
        elif source17_.is_Bool:
            d_640___mcc_h1_ = source17_.b
            d_641_b_ = d_640___mcc_h1_
            return Wrappers.Result_Success(JSON_Values.JSON_Bool(default__.Bool(d_641_b_)))
        elif source17_.is_String:
            d_642___mcc_h2_ = source17_.str
            d_643_str_ = d_642___mcc_h2_
            d_644_valueOrError0_ = default__.String(d_643_str_)
            if (d_644_valueOrError0_).IsFailure():
                return (d_644_valueOrError0_).PropagateFailure()
            elif True:
                d_645_s_ = (d_644_valueOrError0_).Extract()
                return Wrappers.Result_Success(JSON_Values.JSON_String(d_645_s_))
        elif source17_.is_Number:
            d_646___mcc_h3_ = source17_.num
            d_647_dec_ = d_646___mcc_h3_
            d_648_valueOrError1_ = default__.Number(d_647_dec_)
            if (d_648_valueOrError1_).IsFailure():
                return (d_648_valueOrError1_).PropagateFailure()
            elif True:
                d_649_n_ = (d_648_valueOrError1_).Extract()
                return Wrappers.Result_Success(JSON_Values.JSON_Number(d_649_n_))
        elif source17_.is_Object:
            d_650___mcc_h4_ = source17_.obj
            d_651_obj_ = d_650___mcc_h4_
            d_652_valueOrError2_ = default__.Object(d_651_obj_)
            if (d_652_valueOrError2_).IsFailure():
                return (d_652_valueOrError2_).PropagateFailure()
            elif True:
                d_653_o_ = (d_652_valueOrError2_).Extract()
                return Wrappers.Result_Success(JSON_Values.JSON_Object(d_653_o_))
        elif True:
            d_654___mcc_h5_ = source17_.arr
            d_655_arr_ = d_654___mcc_h5_
            d_656_valueOrError3_ = default__.Array(d_655_arr_)
            if (d_656_valueOrError3_).IsFailure():
                return (d_656_valueOrError3_).PropagateFailure()
            elif True:
                d_657_a_ = (d_656_valueOrError3_).Extract()
                return Wrappers.Result_Success(JSON_Values.JSON_Array(d_657_a_))

    @staticmethod
    def JSON(js):
        return default__.Value((js).t)

    @_dafny.classproperty
    def HEX__TABLE__16(instance):
        return _dafny.Map({ord('0'): 0, ord('1'): 1, ord('2'): 2, ord('3'): 3, ord('4'): 4, ord('5'): 5, ord('6'): 6, ord('7'): 7, ord('8'): 8, ord('9'): 9, ord('a'): 10, ord('b'): 11, ord('c'): 12, ord('d'): 13, ord('e'): 14, ord('f'): 15, ord('A'): 10, ord('B'): 11, ord('C'): 12, ord('D'): 13, ord('E'): 14, ord('F'): 15})
    @_dafny.classproperty
    def DIGITS(instance):
        return _dafny.Map({ord('0'): 0, ord('1'): 1, ord('2'): 2, ord('3'): 3, ord('4'): 4, ord('5'): 5, ord('6'): 6, ord('7'): 7, ord('8'): 8, ord('9'): 9})
    @_dafny.classproperty
    def MINUS(instance):
        return ord('-')
