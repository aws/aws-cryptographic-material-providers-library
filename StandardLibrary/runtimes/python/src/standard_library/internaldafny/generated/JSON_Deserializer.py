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
        d_589_hd_ = JSON_Deserializer_Uint16StrConversion.default__.ToNat__any(str, 16, default__.HEX__TABLE__16)
        return d_589_hd_

    @staticmethod
    def Unescape(str, start, prefix):
        while True:
            with _dafny.label():
                def lambda41_(exists_var_1_):
                    d_592_c_: int = exists_var_1_
                    return ((d_592_c_) in (d_591_code_)) and ((d_592_c_) not in (default__.HEX__TABLE__16))

                if (start) >= (len(str)):
                    return Wrappers.Result_Success(prefix)
                elif ((str)[start]) == (ord('\\')):
                    if (len(str)) == ((start) + (1)):
                        return Wrappers.Result_Failure(JSON_Errors.DeserializationError_EscapeAtEOS())
                    elif True:
                        d_590_c_ = (str)[(start) + (1)]
                        if (d_590_c_) == (ord('u')):
                            if (len(str)) <= ((start) + (6)):
                                return Wrappers.Result_Failure(JSON_Errors.DeserializationError_EscapeAtEOS())
                            elif True:
                                d_591_code_ = _dafny.Seq((str)[(start) + (2):(start) + (6):])
                                if _dafny.quantifier((d_591_code_).UniqueElements, False, lambda41_):
                                    return Wrappers.Result_Failure(default__.UnsupportedEscape16(d_591_code_))
                                elif True:
                                    d_593_hd_ = default__.ToNat16(d_591_code_)
                                    in215_ = str
                                    in216_ = (start) + (6)
                                    in217_ = (prefix) + (_dafny.Seq([d_593_hd_]))
                                    str = in215_
                                    start = in216_
                                    prefix = in217_
                                    raise _dafny.TailCall()
                        elif True:
                            def lambda42_():
                                source14_ = d_590_c_
                                unmatched14 = True
                                if unmatched14:
                                    if (source14_) == (34):
                                        unmatched14 = False
                                        return 34
                                if unmatched14:
                                    if (source14_) == (92):
                                        unmatched14 = False
                                        return 92
                                if unmatched14:
                                    if (source14_) == (98):
                                        unmatched14 = False
                                        return 8
                                if unmatched14:
                                    if (source14_) == (102):
                                        unmatched14 = False
                                        return 12
                                if unmatched14:
                                    if (source14_) == (110):
                                        unmatched14 = False
                                        return 10
                                if unmatched14:
                                    if (source14_) == (114):
                                        unmatched14 = False
                                        return 13
                                if unmatched14:
                                    if (source14_) == (116):
                                        unmatched14 = False
                                        return 9
                                if unmatched14:
                                    d_595___v0_ = source14_
                                    unmatched14 = False
                                    return 0
                                raise Exception("unexpected control point")

                            d_594_unescaped_ = lambda42_()
                            if (d_594_unescaped_) == (0):
                                return Wrappers.Result_Failure(default__.UnsupportedEscape16(_dafny.Seq((str)[start:(start) + (2):])))
                            elif True:
                                in218_ = str
                                in219_ = (start) + (2)
                                in220_ = (prefix) + (_dafny.Seq([d_594_unescaped_]))
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
        d_596_valueOrError0_ = (UnicodeStrings.default__.FromUTF8Checked(((js).contents).Bytes())).ToResult_k(JSON_Errors.DeserializationError_InvalidUnicode())
        if (d_596_valueOrError0_).IsFailure():
            return (d_596_valueOrError0_).PropagateFailure()
        elif True:
            d_597_asUtf32_ = (d_596_valueOrError0_).Extract()
            d_598_valueOrError1_ = (UnicodeStrings.default__.ToUTF16Checked(d_597_asUtf32_)).ToResult_k(JSON_Errors.DeserializationError_InvalidUnicode())
            if (d_598_valueOrError1_).IsFailure():
                return (d_598_valueOrError1_).PropagateFailure()
            elif True:
                d_599_asUint16_ = (d_598_valueOrError1_).Extract()
                d_600_valueOrError2_ = default__.Unescape(d_599_asUint16_, 0, _dafny.Seq([]))
                if (d_600_valueOrError2_).IsFailure():
                    return (d_600_valueOrError2_).PropagateFailure()
                elif True:
                    d_601_unescaped_ = (d_600_valueOrError2_).Extract()
                    return (UnicodeStrings.default__.FromUTF16Checked(d_601_unescaped_)).ToResult_k(JSON_Errors.DeserializationError_InvalidUnicode())

    @staticmethod
    def ToInt(sign, n):
        d_602_n_ = JSON_Deserializer_ByteStrConversion.default__.ToNat__any((n).Bytes(), 10, default__.DIGITS)
        return Wrappers.Result_Success(((0) - (d_602_n_) if (sign).Char_q('-') else d_602_n_))

    @staticmethod
    def Number(js):
        let_tmp_rhs7_ = js
        d_603_minus_ = let_tmp_rhs7_.minus
        d_604_num_ = let_tmp_rhs7_.num
        d_605_frac_ = let_tmp_rhs7_.frac
        d_606_exp_ = let_tmp_rhs7_.exp
        d_607_valueOrError0_ = default__.ToInt(d_603_minus_, d_604_num_)
        if (d_607_valueOrError0_).IsFailure():
            return (d_607_valueOrError0_).PropagateFailure()
        elif True:
            d_608_n_ = (d_607_valueOrError0_).Extract()
            def lambda43_():
                source15_ = d_606_exp_
                unmatched15 = True
                if unmatched15:
                    if source15_.is_Empty:
                        unmatched15 = False
                        return Wrappers.Result_Success(0)
                if unmatched15:
                    t0 = source15_.t
                    d_610___v1_ = t0.e
                    d_611_sign_ = t0.sign
                    d_612_num_ = t0.num
                    unmatched15 = False
                    return default__.ToInt(d_611_sign_, d_612_num_)
                raise Exception("unexpected control point")

            d_609_valueOrError1_ = lambda43_()
            if (d_609_valueOrError1_).IsFailure():
                return (d_609_valueOrError1_).PropagateFailure()
            elif True:
                d_613_e10_ = (d_609_valueOrError1_).Extract()
                source16_ = d_605_frac_
                unmatched16 = True
                if unmatched16:
                    if source16_.is_Empty:
                        unmatched16 = False
                        return Wrappers.Result_Success(JSON_Values.Decimal_Decimal(d_608_n_, d_613_e10_))
                if unmatched16:
                    t1 = source16_.t
                    d_614___v2_ = t1.period
                    d_615_num_ = t1.num
                    unmatched16 = False
                    d_616_pow10_ = (d_615_num_).Length()
                    d_617_valueOrError2_ = default__.ToInt(d_603_minus_, d_615_num_)
                    if (d_617_valueOrError2_).IsFailure():
                        return (d_617_valueOrError2_).PropagateFailure()
                    elif True:
                        d_618_frac_ = (d_617_valueOrError2_).Extract()
                        return Wrappers.Result_Success(JSON_Values.Decimal_Decimal(((d_608_n_) * (Power.default__.Pow(10, d_616_pow10_))) + (d_618_frac_), (d_613_e10_) - (d_616_pow10_)))
                raise Exception("unexpected control point")

    @staticmethod
    def KeyValue(js):
        d_619_valueOrError0_ = default__.String((js).k)
        if (d_619_valueOrError0_).IsFailure():
            return (d_619_valueOrError0_).PropagateFailure()
        elif True:
            d_620_k_ = (d_619_valueOrError0_).Extract()
            d_621_valueOrError1_ = default__.Value((js).v)
            if (d_621_valueOrError1_).IsFailure():
                return (d_621_valueOrError1_).PropagateFailure()
            elif True:
                d_622_v_ = (d_621_valueOrError1_).Extract()
                return Wrappers.Result_Success((d_620_k_, d_622_v_))

    @staticmethod
    def Object(js):
        def lambda44_(d_623_js_):
            def lambda45_(d_624_d_):
                return default__.KeyValue((d_624_d_).t)

            return lambda45_

        return Seq.default__.MapWithResult(lambda44_(js), (js).data)

    @staticmethod
    def Array(js):
        def lambda46_(d_625_js_):
            def lambda47_(d_626_d_):
                return default__.Value((d_626_d_).t)

            return lambda47_

        return Seq.default__.MapWithResult(lambda46_(js), (js).data)

    @staticmethod
    def Value(js):
        source17_ = js
        unmatched17 = True
        if unmatched17:
            if source17_.is_Null:
                d_627___v3_ = source17_.n
                unmatched17 = False
                return Wrappers.Result_Success(JSON_Values.JSON_Null())
        if unmatched17:
            if source17_.is_Bool:
                d_628_b_ = source17_.b
                unmatched17 = False
                return Wrappers.Result_Success(JSON_Values.JSON_Bool(default__.Bool(d_628_b_)))
        if unmatched17:
            if source17_.is_String:
                d_629_str_ = source17_.str
                unmatched17 = False
                d_630_valueOrError0_ = default__.String(d_629_str_)
                if (d_630_valueOrError0_).IsFailure():
                    return (d_630_valueOrError0_).PropagateFailure()
                elif True:
                    d_631_s_ = (d_630_valueOrError0_).Extract()
                    return Wrappers.Result_Success(JSON_Values.JSON_String(d_631_s_))
        if unmatched17:
            if source17_.is_Number:
                d_632_dec_ = source17_.num
                unmatched17 = False
                d_633_valueOrError1_ = default__.Number(d_632_dec_)
                if (d_633_valueOrError1_).IsFailure():
                    return (d_633_valueOrError1_).PropagateFailure()
                elif True:
                    d_634_n_ = (d_633_valueOrError1_).Extract()
                    return Wrappers.Result_Success(JSON_Values.JSON_Number(d_634_n_))
        if unmatched17:
            if source17_.is_Object:
                d_635_obj_ = source17_.obj
                unmatched17 = False
                d_636_valueOrError2_ = default__.Object(d_635_obj_)
                if (d_636_valueOrError2_).IsFailure():
                    return (d_636_valueOrError2_).PropagateFailure()
                elif True:
                    d_637_o_ = (d_636_valueOrError2_).Extract()
                    return Wrappers.Result_Success(JSON_Values.JSON_Object(d_637_o_))
        if unmatched17:
            d_638_arr_ = source17_.arr
            unmatched17 = False
            d_639_valueOrError3_ = default__.Array(d_638_arr_)
            if (d_639_valueOrError3_).IsFailure():
                return (d_639_valueOrError3_).PropagateFailure()
            elif True:
                d_640_a_ = (d_639_valueOrError3_).Extract()
                return Wrappers.Result_Success(JSON_Values.JSON_Array(d_640_a_))
        raise Exception("unexpected control point")

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
