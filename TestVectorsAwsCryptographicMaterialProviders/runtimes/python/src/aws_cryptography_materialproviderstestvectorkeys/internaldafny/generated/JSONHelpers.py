import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import Base64
import AlgorithmSuites
import Materials
import Keyring
import Relations
import Seq_MergeSort
import Math
import Seq
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import Actions
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Constants
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import DafnyLibraries
import Time
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import UUID
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring
import CMM
import Defaults
import Commitment
import DefaultCMM
import DefaultClientSupplier
import RequiredEncryptionContextCMM
import AwsCryptographyMaterialProvidersOperations
import software_amazon_cryptography_materialproviders_internaldafny
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import AesKdfCtr
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
import Streams
import Sorting
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64Lemmas
import MplManifestOptions
import AllAlgorithmSuites
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types
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
import JSON_ZeroCopy_Deserializer_Numbers
import JSON_ZeroCopy_Deserializer_ObjectParams
import JSON_ZeroCopy_Deserializer_Objects
import JSON_ZeroCopy_Deserializer_ArrayParams
import JSON_ZeroCopy_Deserializer_Arrays
import JSON_ZeroCopy_Deserializer_Constants
import JSON_ZeroCopy_Deserializer_Values
import JSON_ZeroCopy_Deserializer_API
import JSON_ZeroCopy_Deserializer
import JSON_ZeroCopy_API
import JSON_ZeroCopy
import JSON_API
import JSON

# Module: JSONHelpers

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BvToBytes(bits):
        return _dafny.Seq([(bits)[d_5_i_] for d_5_i_ in range(len(bits))])

    @staticmethod
    def BytesBv(bits):
        return _dafny.Seq([(bits)[d_6_i_] for d_6_i_ in range(len(bits))])

    @staticmethod
    def Get(key, obj):
        while True:
            with _dafny.label():
                if (len(obj)) == (0):
                    return Wrappers.Result_Failure(((_dafny.Seq("Key: ")) + (key)) + (_dafny.Seq(" does not exist")))
                elif (((obj)[0])[0]) == (key):
                    return Wrappers.Result_Success(((obj)[0])[1])
                elif True:
                    in0_ = key
                    in1_ = _dafny.Seq((obj)[1::])
                    key = in0_
                    obj = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetString(key, obj):
        d_7_valueOrError0_ = default__.Get(key, obj)
        if (d_7_valueOrError0_).IsFailure():
            return (d_7_valueOrError0_).PropagateFailure()
        elif True:
            d_8_obj_ = (d_7_valueOrError0_).Extract()
            d_9_valueOrError1_ = Wrappers.default__.Need((d_8_obj_).is_String, _dafny.Seq("Not a string"))
            if (d_9_valueOrError1_).IsFailure():
                return (d_9_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_8_obj_).str)

    @staticmethod
    def GetBool(key, obj):
        d_10_valueOrError0_ = default__.Get(key, obj)
        if (d_10_valueOrError0_).IsFailure():
            return (d_10_valueOrError0_).PropagateFailure()
        elif True:
            d_11_obj_ = (d_10_valueOrError0_).Extract()
            d_12_valueOrError1_ = Wrappers.default__.Need((d_11_obj_).is_Bool, _dafny.Seq("Not a bool"))
            if (d_12_valueOrError1_).IsFailure():
                return (d_12_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_11_obj_).b)

    @staticmethod
    def GetNat(key, obj):
        d_13_valueOrError0_ = default__.Get(key, obj)
        if (d_13_valueOrError0_).IsFailure():
            return (d_13_valueOrError0_).PropagateFailure()
        elif True:
            d_14_obj_ = (d_13_valueOrError0_).Extract()
            d_15_valueOrError1_ = Wrappers.default__.Need((d_14_obj_).is_Number, _dafny.Seq("Not a number"))
            if (d_15_valueOrError1_).IsFailure():
                return (d_15_valueOrError1_).PropagateFailure()
            elif True:
                d_16_valueOrError2_ = Wrappers.default__.Need((0) < (((d_14_obj_).num).n), _dafny.Seq("Not a nat"))
                if (d_16_valueOrError2_).IsFailure():
                    return (d_16_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(((d_14_obj_).num).n)

    @staticmethod
    def GetPositiveLong(key, obj):
        d_17_valueOrError0_ = default__.GetNat(key, obj)
        if (d_17_valueOrError0_).IsFailure():
            return (d_17_valueOrError0_).PropagateFailure()
        elif True:
            d_18_n_ = (d_17_valueOrError0_).Extract()
            d_19_valueOrError1_ = Wrappers.default__.Need((d_18_n_) <= (BoundedInts.default__.INT64__MAX), _dafny.Seq("Int64 Overflow"))
            if (d_19_valueOrError1_).IsFailure():
                return (d_19_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_18_n_)

    @staticmethod
    def GetPositiveInteger(key, obj):
        d_20_valueOrError0_ = default__.GetNat(key, obj)
        if (d_20_valueOrError0_).IsFailure():
            return (d_20_valueOrError0_).PropagateFailure()
        elif True:
            d_21_n_ = (d_20_valueOrError0_).Extract()
            d_22_valueOrError1_ = Wrappers.default__.Need((d_21_n_) <= (BoundedInts.default__.INT32__MAX), _dafny.Seq("Int32 Overflow"))
            if (d_22_valueOrError1_).IsFailure():
                return (d_22_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_21_n_)

    @staticmethod
    def GetOptionalString(key, obj):
        d_23_obj_ = (default__.Get(key, obj)).ToOption()
        if (d_23_obj_).is_Some:
            d_24_valueOrError0_ = Wrappers.default__.Need(((d_23_obj_).value).is_String, _dafny.Seq("Not a string"))
            if (d_24_valueOrError0_).IsFailure():
                return (d_24_valueOrError0_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(Wrappers.Option_Some(((d_23_obj_).value).str))
        elif True:
            return Wrappers.Result_Success(Wrappers.Option_None())

    @staticmethod
    def GetOptionalPositiveLong(key, obj):
        d_25_obj_ = (default__.Get(key, obj)).ToOption()
        if (d_25_obj_).is_Some:
            d_26_valueOrError0_ = Wrappers.default__.Need(((d_25_obj_).value).is_Number, _dafny.Seq("Not a number"))
            if (d_26_valueOrError0_).IsFailure():
                return (d_26_valueOrError0_).PropagateFailure()
            elif True:
                d_27_valueOrError1_ = Wrappers.default__.Need(((0) <= ((((d_25_obj_).value).num).n)) and (((((d_25_obj_).value).num).n) <= (BoundedInts.default__.INT64__MAX)), _dafny.Seq("Int64 Overflow"))
                if (d_27_valueOrError1_).IsFailure():
                    return (d_27_valueOrError1_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(Wrappers.Option_Some((((d_25_obj_).value).num).n))
        elif True:
            return Wrappers.Result_Success(Wrappers.Option_None())

    @staticmethod
    def GetObject(key, obj):
        d_28_valueOrError0_ = default__.Get(key, obj)
        if (d_28_valueOrError0_).IsFailure():
            return (d_28_valueOrError0_).PropagateFailure()
        elif True:
            d_29_obj_ = (d_28_valueOrError0_).Extract()
            d_30_valueOrError1_ = Wrappers.default__.Need((d_29_obj_).is_Object, _dafny.Seq("Not an object"))
            if (d_30_valueOrError1_).IsFailure():
                return (d_30_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_29_obj_).obj)

    @staticmethod
    def GetArray(key, obj):
        d_31_valueOrError0_ = default__.Get(key, obj)
        if (d_31_valueOrError0_).IsFailure():
            return (d_31_valueOrError0_).PropagateFailure()
        elif True:
            d_32_obj_ = (d_31_valueOrError0_).Extract()
            d_33_valueOrError1_ = Wrappers.default__.Need((d_32_obj_).is_Array, _dafny.Seq("Not an array"))
            if (d_33_valueOrError1_).IsFailure():
                return (d_33_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_32_obj_).arr)

    @staticmethod
    def GetArrayString(key, obj):
        d_34_valueOrError0_ = default__.Get(key, obj)
        if (d_34_valueOrError0_).IsFailure():
            return (d_34_valueOrError0_).PropagateFailure()
        elif True:
            d_35_obj_ = (d_34_valueOrError0_).Extract()
            def lambda0_(forall_var_0_):
                d_37_s_: JSON_Values.JSON = forall_var_0_
                return not ((d_37_s_) in ((d_35_obj_).arr)) or ((d_37_s_).is_String)

            d_36_valueOrError1_ = Wrappers.default__.Need(((d_35_obj_).is_Array) and (_dafny.quantifier(((d_35_obj_).arr).UniqueElements, True, lambda0_)), _dafny.Seq("Not an array of strings"))
            if (d_36_valueOrError1_).IsFailure():
                return (d_36_valueOrError1_).PropagateFailure()
            elif True:
                d_38_arr_ = (d_35_obj_).arr
                return Wrappers.Result_Success(_dafny.Seq([((d_38_arr_)[d_39_n_]).str for d_39_n_ in range(len(d_38_arr_))]))

    @staticmethod
    def GetArrayObject(key, obj):
        d_40_valueOrError0_ = default__.Get(key, obj)
        if (d_40_valueOrError0_).IsFailure():
            return (d_40_valueOrError0_).PropagateFailure()
        elif True:
            d_41_obj_ = (d_40_valueOrError0_).Extract()
            def lambda1_(forall_var_1_):
                d_43_s_: JSON_Values.JSON = forall_var_1_
                return not ((d_43_s_) in ((d_41_obj_).arr)) or ((d_43_s_).is_Object)

            d_42_valueOrError1_ = Wrappers.default__.Need(((d_41_obj_).is_Array) and (_dafny.quantifier(((d_41_obj_).arr).UniqueElements, True, lambda1_)), _dafny.Seq("Not an array of objects"))
            if (d_42_valueOrError1_).IsFailure():
                return (d_42_valueOrError1_).PropagateFailure()
            elif True:
                d_44_arr_ = (d_41_obj_).arr
                return Wrappers.Result_Success(_dafny.Seq([((d_44_arr_)[d_45_n_]).obj for d_45_n_ in range(len(d_44_arr_))]))

    @staticmethod
    def SmallObjectToStringStringMap(key, obj):
        d_46_valueOrError0_ = default__.Get(key, obj)
        if (d_46_valueOrError0_).IsFailure():
            return (d_46_valueOrError0_).PropagateFailure()
        elif True:
            d_47_item_ = (d_46_valueOrError0_).Extract()
            return default__.JsonObjectToStringStringMap(d_47_item_)

    @staticmethod
    def GetOptionalSmallObjectToStringStringMap(key, obj):
        d_48_item_ = (default__.Get(key, obj)).ToOption()
        if (d_48_item_).is_Some:
            d_49_valueOrError0_ = default__.JsonObjectToStringStringMap((d_48_item_).value)
            if (d_49_valueOrError0_).IsFailure():
                return (d_49_valueOrError0_).PropagateFailure()
            elif True:
                d_50_m_ = (d_49_valueOrError0_).Extract()
                return Wrappers.Result_Success(Wrappers.Option_Some(d_50_m_))
        elif True:
            return Wrappers.Result_Success(Wrappers.Option_None())

    @staticmethod
    def printJson(j):
        hresult_: tuple = ()
        _dafny.print(_dafny.string_of(j))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        hresult_ = ()
        return hresult_
        return hresult_

    @staticmethod
    def JsonObjectToStringStringMap(item):
        d_51_valueOrError0_ = Wrappers.default__.Need((item).is_Object, _dafny.Seq("Not an object"))
        if (d_51_valueOrError0_).IsFailure():
            return (d_51_valueOrError0_).PropagateFailure()
        elif True:
            d_52_obj_ = (item).obj
            def lambda2_(forall_var_2_):
                d_54_t_: tuple = forall_var_2_
                return not ((d_54_t_) in (d_52_obj_)) or (((d_54_t_)[1]).is_String)

            d_53_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier((d_52_obj_).UniqueElements, True, lambda2_), _dafny.Seq("Not a string string object"))
            if (d_53_valueOrError1_).IsFailure():
                return (d_53_valueOrError1_).PropagateFailure()
            elif True:
                def lambda3_(forall_var_3_):
                    def lambda4_(forall_var_4_):
                        d_57_j_: int = forall_var_4_
                        return not ((((0) <= (d_56_i_)) and ((d_56_i_) < (d_57_j_))) and ((d_57_j_) < (len(d_52_obj_)))) or ((((d_52_obj_)[d_56_i_])[0]) != (((d_52_obj_)[d_57_j_])[0]))

                    d_56_i_: int = forall_var_3_
                    return _dafny.quantifier(_dafny.IntegerRange((d_56_i_) + (1), len(d_52_obj_)), True, lambda4_)

                d_55_valueOrError2_ = Wrappers.default__.Need(_dafny.quantifier(_dafny.IntegerRange(0, len(d_52_obj_)), True, lambda3_), _dafny.Seq("JSON serialization Error"))
                if (d_55_valueOrError2_).IsFailure():
                    return (d_55_valueOrError2_).PropagateFailure()
                elif True:
                    def iife2_():
                        coll2_ = _dafny.Map()
                        compr_2_: tuple
                        for compr_2_ in (d_52_obj_).Elements:
                            d_58_t_: tuple = compr_2_
                            if (d_58_t_) in (d_52_obj_):
                                coll2_[(d_58_t_)[0]] = ((d_58_t_)[1]).str
                        return _dafny.Map(coll2_)
                    return Wrappers.Result_Success(iife2_()
)

    @staticmethod
    def utf8EncodePair(key, value):
        d_59_valueOrError0_ = UTF8.default__.Encode(key)
        if (d_59_valueOrError0_).IsFailure():
            return (d_59_valueOrError0_).PropagateFailure()
        elif True:
            d_60_utf8Key_ = (d_59_valueOrError0_).Extract()
            d_61_valueOrError1_ = UTF8.default__.Encode(value)
            if (d_61_valueOrError1_).IsFailure():
                return (d_61_valueOrError1_).PropagateFailure()
            elif True:
                d_62_utf8Value_ = (d_61_valueOrError1_).Extract()
                return Wrappers.Result_Success((d_60_utf8Key_, d_62_utf8Value_))

    @staticmethod
    def utf8EncodeMap(mapStringString):
        if (len(mapStringString)) == (0):
            return Wrappers.Result_Success(_dafny.Map({}))
        elif True:
            def iife3_():
                coll3_ = _dafny.Map()
                compr_3_: _dafny.Seq
                for compr_3_ in (mapStringString).keys.Elements:
                    d_64_key_: _dafny.Seq = compr_3_
                    if (d_64_key_) in (mapStringString):
                        coll3_[d_64_key_] = default__.utf8EncodePair(d_64_key_, (mapStringString)[d_64_key_])
                return _dafny.Map(coll3_)
            d_63_encodedResults_ = iife3_()

            def lambda5_(forall_var_5_):
                d_66_r_: Wrappers.Result = forall_var_5_
                return not ((d_66_r_) in ((d_63_encodedResults_).values)) or ((d_66_r_).is_Success)

            d_65_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier(((d_63_encodedResults_).values).Elements, True, lambda5_), _dafny.Seq("String can not be UTF8 Encoded?"))
            if (d_65_valueOrError0_).IsFailure():
                return (d_65_valueOrError0_).PropagateFailure()
            elif True:
                def iife4_():
                    coll4_ = _dafny.Map()
                    compr_4_: Wrappers.Result
                    for compr_4_ in ((d_63_encodedResults_).values).Elements:
                        d_67_r_: Wrappers.Result = compr_4_
                        if (d_67_r_) in ((d_63_encodedResults_).values):
                            coll4_[((d_67_r_).value)[0]] = ((d_67_r_).value)[1]
                    return _dafny.Map(coll4_)
                return Wrappers.Result_Success(iife4_()
)

    @staticmethod
    def utf8EncodeSeq(seqOfStrings):
        d_68_encodedResults_ = _dafny.Seq([UTF8.default__.Encode((seqOfStrings)[d_69_i_]) for d_69_i_ in range(len(seqOfStrings))])
        def lambda6_(forall_var_6_):
            d_71_r_: Wrappers.Result = forall_var_6_
            return not ((d_71_r_) in (d_68_encodedResults_)) or ((d_71_r_).is_Success)

        d_70_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier((d_68_encodedResults_).UniqueElements, True, lambda6_), _dafny.Seq("String can not be UTF8 Encoded?"))
        if (d_70_valueOrError0_).IsFailure():
            return (d_70_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(_dafny.Seq([((d_68_encodedResults_)[d_72_i_]).value for d_72_i_ in range(len(d_68_encodedResults_))]))

