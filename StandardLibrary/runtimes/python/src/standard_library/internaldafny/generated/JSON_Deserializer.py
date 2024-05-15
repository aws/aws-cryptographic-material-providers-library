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

# Module: standard_library.internaldafny.generated.JSON_Deserializer

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
        d_623_hd_ = JSON_Deserializer_Uint16StrConversion.default__.ToNat__any(str, 16, default__.HEX__TABLE__16)
        return d_623_hd_

    @staticmethod
    def Unescape(str, start, prefix):
        while True:
            with _dafny.label():
                def lambda40_(exists_var_1_):
                    d_626_c_: int = exists_var_1_
                    if True:
                        return ((d_626_c_) in (d_625_code_)) and ((d_626_c_) not in (default__.HEX__TABLE__16))
                    elif True:
                        return False

                if (start) >= (len(str)):
                    return Wrappers.Result_Success(prefix)
                elif ((str)[start]) == (ord('\\')):
                    if (len(str)) == ((start) + (1)):
                        return Wrappers.Result_Failure(JSON_Errors.DeserializationError_EscapeAtEOS())
                    elif True:
                        d_624_c_ = (str)[(start) + (1)]
                        if (d_624_c_) == (ord('u')):
                            if (len(str)) <= ((start) + (6)):
                                return Wrappers.Result_Failure(JSON_Errors.DeserializationError_EscapeAtEOS())
                            elif True:
                                d_625_code_ = _dafny.Seq((str)[(start) + (2):(start) + (6):])
                                if _dafny.quantifier((d_625_code_).UniqueElements, False, lambda40_):
                                    return Wrappers.Result_Failure(default__.UnsupportedEscape16(d_625_code_))
                                elif True:
                                    d_627_hd_ = default__.ToNat16(d_625_code_)
                                    in215_ = str
                                    in216_ = (start) + (6)
                                    in217_ = (prefix) + (_dafny.Seq([d_627_hd_]))
                                    str = in215_
                                    start = in216_
                                    prefix = in217_
                                    raise _dafny.TailCall()
                        elif True:
                            d_628_unescaped_ = (34 if (d_624_c_) == (34) else (92 if (d_624_c_) == (92) else (8 if (d_624_c_) == (98) else (12 if (d_624_c_) == (102) else (10 if (d_624_c_) == (110) else (13 if (d_624_c_) == (114) else (9 if (d_624_c_) == (116) else 0)))))))
                            if (d_628_unescaped_) == (0):
                                return Wrappers.Result_Failure(default__.UnsupportedEscape16(_dafny.Seq((str)[start:(start) + (2):])))
                            elif True:
                                in218_ = str
                                in219_ = (start) + (2)
                                in220_ = (prefix) + (_dafny.Seq([d_628_unescaped_]))
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
        d_629_valueOrError0_ = (UnicodeStrings.default__.FromUTF8Checked(((js).contents).Bytes())).ToResult_k(JSON_Errors.DeserializationError_InvalidUnicode())
        if (d_629_valueOrError0_).IsFailure():
            return (d_629_valueOrError0_).PropagateFailure()
        elif True:
            d_630_asUtf32_ = (d_629_valueOrError0_).Extract()
            d_631_valueOrError1_ = (UnicodeStrings.default__.ToUTF16Checked(d_630_asUtf32_)).ToResult_k(JSON_Errors.DeserializationError_InvalidUnicode())
            if (d_631_valueOrError1_).IsFailure():
                return (d_631_valueOrError1_).PropagateFailure()
            elif True:
                d_632_asUint16_ = (d_631_valueOrError1_).Extract()
                d_633_valueOrError2_ = default__.Unescape(d_632_asUint16_, 0, _dafny.Seq([]))
                if (d_633_valueOrError2_).IsFailure():
                    return (d_633_valueOrError2_).PropagateFailure()
                elif True:
                    d_634_unescaped_ = (d_633_valueOrError2_).Extract()
                    return (UnicodeStrings.default__.FromUTF16Checked(d_634_unescaped_)).ToResult_k(JSON_Errors.DeserializationError_InvalidUnicode())

    @staticmethod
    def ToInt(sign, n):
        d_635_n_ = JSON_Deserializer_ByteStrConversion.default__.ToNat__any((n).Bytes(), 10, default__.DIGITS)
        return Wrappers.Result_Success(((0) - (d_635_n_) if (sign).Char_q('-') else d_635_n_))

    @staticmethod
    def Number(js):
        let_tmp_rhs7_ = js
        d_636_minus_ = let_tmp_rhs7_.minus
        d_637_num_ = let_tmp_rhs7_.num
        d_638_frac_ = let_tmp_rhs7_.frac
        d_639_exp_ = let_tmp_rhs7_.exp
        d_640_valueOrError0_ = default__.ToInt(d_636_minus_, d_637_num_)
        if (d_640_valueOrError0_).IsFailure():
            return (d_640_valueOrError0_).PropagateFailure()
        elif True:
            d_641_n_ = (d_640_valueOrError0_).Extract()
            def lambda41_(source13_):
                if source13_.is_Empty:
                    return Wrappers.Result_Success(0)
                elif True:
                    d_643___mcc_h0_ = source13_.t
                    source14_ = d_643___mcc_h0_
                    d_644___mcc_h1_ = source14_.e
                    d_645___mcc_h2_ = source14_.sign
                    d_646___mcc_h3_ = source14_.num
                    d_647_num_ = d_646___mcc_h3_
                    d_648_sign_ = d_645___mcc_h2_
                    return default__.ToInt(d_648_sign_, d_647_num_)

            d_642_valueOrError1_ = lambda41_(d_639_exp_)
            if (d_642_valueOrError1_).IsFailure():
                return (d_642_valueOrError1_).PropagateFailure()
            elif True:
                d_649_e10_ = (d_642_valueOrError1_).Extract()
                source15_ = d_638_frac_
                if source15_.is_Empty:
                    return Wrappers.Result_Success(JSON_Values.Decimal_Decimal(d_641_n_, d_649_e10_))
                elif True:
                    d_650___mcc_h4_ = source15_.t
                    source16_ = d_650___mcc_h4_
                    d_651___mcc_h5_ = source16_.period
                    d_652___mcc_h6_ = source16_.num
                    d_653_num_ = d_652___mcc_h6_
                    d_654_pow10_ = (d_653_num_).Length()
                    d_655_valueOrError2_ = default__.ToInt(d_636_minus_, d_653_num_)
                    if (d_655_valueOrError2_).IsFailure():
                        return (d_655_valueOrError2_).PropagateFailure()
                    elif True:
                        d_656_frac_ = (d_655_valueOrError2_).Extract()
                        return Wrappers.Result_Success(JSON_Values.Decimal_Decimal(((d_641_n_) * (Power.default__.Pow(10, d_654_pow10_))) + (d_656_frac_), (d_649_e10_) - (d_654_pow10_)))

    @staticmethod
    def KeyValue(js):
        d_657_valueOrError0_ = default__.String((js).k)
        if (d_657_valueOrError0_).IsFailure():
            return (d_657_valueOrError0_).PropagateFailure()
        elif True:
            d_658_k_ = (d_657_valueOrError0_).Extract()
            d_659_valueOrError1_ = default__.Value((js).v)
            if (d_659_valueOrError1_).IsFailure():
                return (d_659_valueOrError1_).PropagateFailure()
            elif True:
                d_660_v_ = (d_659_valueOrError1_).Extract()
                return Wrappers.Result_Success((d_658_k_, d_660_v_))

    @staticmethod
    def Object(js):
        def lambda42_(d_661_js_):
            def lambda43_(d_662_d_):
                return default__.KeyValue((d_662_d_).t)

            return lambda43_

        return Seq.default__.MapWithResult(lambda42_(js), (js).data)

    @staticmethod
    def Array(js):
        def lambda44_(d_663_js_):
            def lambda45_(d_664_d_):
                return default__.Value((d_664_d_).t)

            return lambda45_

        return Seq.default__.MapWithResult(lambda44_(js), (js).data)

    @staticmethod
    def Value(js):
        source17_ = js
        if source17_.is_Null:
            d_665___mcc_h0_ = source17_.n
            return Wrappers.Result_Success(JSON_Values.JSON_Null())
        elif source17_.is_Bool:
            d_666___mcc_h1_ = source17_.b
            d_667_b_ = d_666___mcc_h1_
            return Wrappers.Result_Success(JSON_Values.JSON_Bool(default__.Bool(d_667_b_)))
        elif source17_.is_String:
            d_668___mcc_h2_ = source17_.str
            d_669_str_ = d_668___mcc_h2_
            d_670_valueOrError0_ = default__.String(d_669_str_)
            if (d_670_valueOrError0_).IsFailure():
                return (d_670_valueOrError0_).PropagateFailure()
            elif True:
                d_671_s_ = (d_670_valueOrError0_).Extract()
                return Wrappers.Result_Success(JSON_Values.JSON_String(d_671_s_))
        elif source17_.is_Number:
            d_672___mcc_h3_ = source17_.num
            d_673_dec_ = d_672___mcc_h3_
            d_674_valueOrError1_ = default__.Number(d_673_dec_)
            if (d_674_valueOrError1_).IsFailure():
                return (d_674_valueOrError1_).PropagateFailure()
            elif True:
                d_675_n_ = (d_674_valueOrError1_).Extract()
                return Wrappers.Result_Success(JSON_Values.JSON_Number(d_675_n_))
        elif source17_.is_Object:
            d_676___mcc_h4_ = source17_.obj
            d_677_obj_ = d_676___mcc_h4_
            d_678_valueOrError2_ = default__.Object(d_677_obj_)
            if (d_678_valueOrError2_).IsFailure():
                return (d_678_valueOrError2_).PropagateFailure()
            elif True:
                d_679_o_ = (d_678_valueOrError2_).Extract()
                return Wrappers.Result_Success(JSON_Values.JSON_Object(d_679_o_))
        elif True:
            d_680___mcc_h5_ = source17_.arr
            d_681_arr_ = d_680___mcc_h5_
            d_682_valueOrError3_ = default__.Array(d_681_arr_)
            if (d_682_valueOrError3_).IsFailure():
                return (d_682_valueOrError3_).PropagateFailure()
            elif True:
                d_683_a_ = (d_682_valueOrError3_).Extract()
                return Wrappers.Result_Success(JSON_Values.JSON_Array(d_683_a_))

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
