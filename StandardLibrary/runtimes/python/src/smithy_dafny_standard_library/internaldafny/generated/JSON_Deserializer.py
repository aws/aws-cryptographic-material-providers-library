import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import smithy_dafny_standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views as JSON_Utils_Views
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers as JSON_Utils_Lexers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils as JSON_Utils
import smithy_dafny_standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Values as JSON_Values
import smithy_dafny_standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import smithy_dafny_standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import smithy_dafny_standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion

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
        d_0_hd_ = JSON_Deserializer_Uint16StrConversion.default__.ToNat__any(str, 16, default__.HEX__TABLE__16)
        return d_0_hd_

    @staticmethod
    def Unescape(str, start, prefix):
        while True:
            with _dafny.label():
                def lambda0_(exists_var_0_):
                    d_2_c_: int = exists_var_0_
                    return ((d_2_c_) in (d_1_code_)) and ((d_2_c_) not in (default__.HEX__TABLE__16))

                if (start) >= (len(str)):
                    return Wrappers.Result_Success(prefix)
                elif ((str)[start]) == (ord('\\')):
                    if (len(str)) == ((start) + (1)):
                        return Wrappers.Result_Failure(JSON_Errors.DeserializationError_EscapeAtEOS())
                    elif True:
                        d_0_c_ = (str)[(start) + (1)]
                        if (d_0_c_) == (ord('u')):
                            if (len(str)) <= ((start) + (6)):
                                return Wrappers.Result_Failure(JSON_Errors.DeserializationError_EscapeAtEOS())
                            elif True:
                                d_1_code_ = _dafny.Seq((str)[(start) + (2):(start) + (6):])
                                if _dafny.quantifier((d_1_code_).UniqueElements, False, lambda0_):
                                    return Wrappers.Result_Failure(default__.UnsupportedEscape16(d_1_code_))
                                elif True:
                                    d_3_hd_ = default__.ToNat16(d_1_code_)
                                    in0_ = str
                                    in1_ = (start) + (6)
                                    in2_ = (prefix) + (_dafny.Seq([d_3_hd_]))
                                    str = in0_
                                    start = in1_
                                    prefix = in2_
                                    raise _dafny.TailCall()
                        elif True:
                            def lambda1_():
                                source0_ = d_0_c_
                                if True:
                                    if (source0_) == (34):
                                        return 34
                                if True:
                                    if (source0_) == (92):
                                        return 92
                                if True:
                                    if (source0_) == (98):
                                        return 8
                                if True:
                                    if (source0_) == (102):
                                        return 12
                                if True:
                                    if (source0_) == (110):
                                        return 10
                                if True:
                                    if (source0_) == (114):
                                        return 13
                                if True:
                                    if (source0_) == (116):
                                        return 9
                                if True:
                                    return 0

                            d_4_unescaped_ = lambda1_()
                            if (d_4_unescaped_) == (0):
                                return Wrappers.Result_Failure(default__.UnsupportedEscape16(_dafny.Seq((str)[start:(start) + (2):])))
                            elif True:
                                in3_ = str
                                in4_ = (start) + (2)
                                in5_ = (prefix) + (_dafny.Seq([d_4_unescaped_]))
                                str = in3_
                                start = in4_
                                prefix = in5_
                                raise _dafny.TailCall()
                elif True:
                    in6_ = str
                    in7_ = (start) + (1)
                    in8_ = (prefix) + (_dafny.Seq([(str)[start]]))
                    str = in6_
                    start = in7_
                    prefix = in8_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def String(js):
        d_0_valueOrError0_ = (UnicodeStrings.default__.FromUTF8Checked(((js).contents).Bytes())).ToResult_k(JSON_Errors.DeserializationError_InvalidUnicode())
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_asUtf32_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = (UnicodeStrings.default__.ToUTF16Checked(d_1_asUtf32_)).ToResult_k(JSON_Errors.DeserializationError_InvalidUnicode())
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_asUint16_ = (d_2_valueOrError1_).Extract()
                d_4_valueOrError2_ = default__.Unescape(d_3_asUint16_, 0, _dafny.Seq([]))
                if (d_4_valueOrError2_).IsFailure():
                    return (d_4_valueOrError2_).PropagateFailure()
                elif True:
                    d_5_unescaped_ = (d_4_valueOrError2_).Extract()
                    return (UnicodeStrings.default__.FromUTF16Checked(d_5_unescaped_)).ToResult_k(JSON_Errors.DeserializationError_InvalidUnicode())

    @staticmethod
    def ToInt(sign, n):
        d_0_n_ = JSON_Deserializer_ByteStrConversion.default__.ToNat__any((n).Bytes(), 10, default__.DIGITS)
        return Wrappers.Result_Success(((0) - (d_0_n_) if (sign).Char_q('-') else d_0_n_))

    @staticmethod
    def Number(js):
        let_tmp_rhs0_ = js
        d_0_minus_ = let_tmp_rhs0_.minus
        d_1_num_ = let_tmp_rhs0_.num
        d_2_frac_ = let_tmp_rhs0_.frac
        d_3_exp_ = let_tmp_rhs0_.exp
        d_4_valueOrError0_ = default__.ToInt(d_0_minus_, d_1_num_)
        if (d_4_valueOrError0_).IsFailure():
            return (d_4_valueOrError0_).PropagateFailure()
        elif True:
            d_5_n_ = (d_4_valueOrError0_).Extract()
            def lambda0_():
                source0_ = d_3_exp_
                if True:
                    if source0_.is_Empty:
                        return Wrappers.Result_Success(0)
                if True:
                    t0 = source0_.t
                    d_7_sign_ = t0.sign
                    d_8_num_ = t0.num
                    return default__.ToInt(d_7_sign_, d_8_num_)

            d_6_valueOrError1_ = lambda0_()
            if (d_6_valueOrError1_).IsFailure():
                return (d_6_valueOrError1_).PropagateFailure()
            elif True:
                d_9_e10_ = (d_6_valueOrError1_).Extract()
                source1_ = d_2_frac_
                if True:
                    if source1_.is_Empty:
                        return Wrappers.Result_Success(JSON_Values.Decimal_Decimal(d_5_n_, d_9_e10_))
                if True:
                    t1 = source1_.t
                    d_10_num_ = t1.num
                    d_11_pow10_ = (d_10_num_).Length()
                    d_12_valueOrError2_ = default__.ToInt(d_0_minus_, d_10_num_)
                    if (d_12_valueOrError2_).IsFailure():
                        return (d_12_valueOrError2_).PropagateFailure()
                    elif True:
                        d_13_frac_ = (d_12_valueOrError2_).Extract()
                        return Wrappers.Result_Success(JSON_Values.Decimal_Decimal(((d_5_n_) * (Power.default__.Pow(10, d_11_pow10_))) + (d_13_frac_), (d_9_e10_) - (d_11_pow10_)))

    @staticmethod
    def KeyValue(js):
        d_0_valueOrError0_ = default__.String((js).k)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_k_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = default__.Value((js).v)
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_v_ = (d_2_valueOrError1_).Extract()
                return Wrappers.Result_Success((d_1_k_, d_3_v_))

    @staticmethod
    def Object(js):
        def lambda0_(d_0_js_):
            def lambda1_(d_1_d_):
                return default__.KeyValue((d_1_d_).t)

            return lambda1_

        return Seq.default__.MapWithResult(lambda0_(js), (js).data)

    @staticmethod
    def Array(js):
        def lambda0_(d_0_js_):
            def lambda1_(d_1_d_):
                return default__.Value((d_1_d_).t)

            return lambda1_

        return Seq.default__.MapWithResult(lambda0_(js), (js).data)

    @staticmethod
    def Value(js):
        source0_ = js
        if True:
            if source0_.is_Null:
                return Wrappers.Result_Success(JSON_Values.JSON_Null())
        if True:
            if source0_.is_Bool:
                d_0_b_ = source0_.b
                return Wrappers.Result_Success(JSON_Values.JSON_Bool(default__.Bool(d_0_b_)))
        if True:
            if source0_.is_String:
                d_1_str_ = source0_.str
                d_2_valueOrError0_ = default__.String(d_1_str_)
                if (d_2_valueOrError0_).IsFailure():
                    return (d_2_valueOrError0_).PropagateFailure()
                elif True:
                    d_3_s_ = (d_2_valueOrError0_).Extract()
                    return Wrappers.Result_Success(JSON_Values.JSON_String(d_3_s_))
        if True:
            if source0_.is_Number:
                d_4_dec_ = source0_.num
                d_5_valueOrError1_ = default__.Number(d_4_dec_)
                if (d_5_valueOrError1_).IsFailure():
                    return (d_5_valueOrError1_).PropagateFailure()
                elif True:
                    d_6_n_ = (d_5_valueOrError1_).Extract()
                    return Wrappers.Result_Success(JSON_Values.JSON_Number(d_6_n_))
        if True:
            if source0_.is_Object:
                d_7_obj_ = source0_.obj
                d_8_valueOrError2_ = default__.Object(d_7_obj_)
                if (d_8_valueOrError2_).IsFailure():
                    return (d_8_valueOrError2_).PropagateFailure()
                elif True:
                    d_9_o_ = (d_8_valueOrError2_).Extract()
                    return Wrappers.Result_Success(JSON_Values.JSON_Object(d_9_o_))
        if True:
            d_10_arr_ = source0_.arr
            d_11_valueOrError3_ = default__.Array(d_10_arr_)
            if (d_11_valueOrError3_).IsFailure():
                return (d_11_valueOrError3_).PropagateFailure()
            elif True:
                d_12_a_ = (d_11_valueOrError3_).Extract()
                return Wrappers.Result_Success(JSON_Values.JSON_Array(d_12_a_))

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
