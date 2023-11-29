import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_mUInt
import String
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import Base64
import AlgorithmSuites
import Materials
import Keyring
import Relations
import Seq_mMergeSort
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
import Aws_mCryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
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
import Streams
import Sorting
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64Lemmas
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import TestVectorsUtils
import TestVectorConstants
import KeyringExpectations
import CreateAwsKmsKeyrings
import CreateAwsKmsMultiKeyrings
import CreateAwsKmsMrkKeyrings
import CreateAwsKmsMrkMultiKeyrings
import CreateRawAesKeyrings
import CreateRawRsaKeyrings
import CreateKeyrings
import software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types
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
import JSON_mZeroCopy_mDeserializer_mNumbers
import JSON_mZeroCopy_mDeserializer_mObjectParams
import JSON_mZeroCopy_mDeserializer_mObjects
import JSON_mZeroCopy_mDeserializer_mArrayParams
import JSON_mZeroCopy_mDeserializer_mArrays
import JSON_mZeroCopy_mDeserializer_mConstants
import JSON_mZeroCopy_mDeserializer_mValues
import JSON_mZeroCopy_mDeserializer_mAPI
import JSON_mZeroCopy_mDeserializer
import JSON_mZeroCopy_mAPI
import JSON_mZeroCopy
import JSON_mAPI
import JSON

# Module: JSONHelpers

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BvToBytes(bits):
        return _dafny.Seq([(bits)[d_124_i_] for d_124_i_ in range(len(bits))])

    @staticmethod
    def BytesBv(bits):
        return _dafny.Seq([(bits)[d_125_i_] for d_125_i_ in range(len(bits))])

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
        d_126_valueOrError0_ = default__.Get(key, obj)
        if (d_126_valueOrError0_).IsFailure():
            return (d_126_valueOrError0_).PropagateFailure()
        elif True:
            d_127_obj_ = (d_126_valueOrError0_).Extract()
            d_128_valueOrError1_ = Wrappers.default__.Need((d_127_obj_).is_String, _dafny.Seq("Not a string"))
            if (d_128_valueOrError1_).IsFailure():
                return (d_128_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_127_obj_).str)

    @staticmethod
    def GetBool(key, obj):
        d_129_valueOrError0_ = default__.Get(key, obj)
        if (d_129_valueOrError0_).IsFailure():
            return (d_129_valueOrError0_).PropagateFailure()
        elif True:
            d_130_obj_ = (d_129_valueOrError0_).Extract()
            d_131_valueOrError1_ = Wrappers.default__.Need((d_130_obj_).is_Bool, _dafny.Seq("Not a bool"))
            if (d_131_valueOrError1_).IsFailure():
                return (d_131_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_130_obj_).b)

    @staticmethod
    def GetNat(key, obj):
        d_132_valueOrError0_ = default__.Get(key, obj)
        if (d_132_valueOrError0_).IsFailure():
            return (d_132_valueOrError0_).PropagateFailure()
        elif True:
            d_133_obj_ = (d_132_valueOrError0_).Extract()
            d_134_valueOrError1_ = Wrappers.default__.Need((d_133_obj_).is_Number, _dafny.Seq("Not a number"))
            if (d_134_valueOrError1_).IsFailure():
                return (d_134_valueOrError1_).PropagateFailure()
            elif True:
                d_135_valueOrError2_ = Wrappers.default__.Need((0) < (((d_133_obj_).num).n), _dafny.Seq("Not a nat"))
                if (d_135_valueOrError2_).IsFailure():
                    return (d_135_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(((d_133_obj_).num).n)

    @staticmethod
    def GetOptionalString(key, obj):
        d_136_obj_ = (default__.Get(key, obj)).ToOption()
        if (d_136_obj_).is_Some:
            d_137_valueOrError0_ = Wrappers.default__.Need(((d_136_obj_).value).is_String, _dafny.Seq("Not a string"))
            if (d_137_valueOrError0_).IsFailure():
                return (d_137_valueOrError0_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(Wrappers.Option_Some(((d_136_obj_).value).str))
        elif True:
            return Wrappers.Result_Success(Wrappers.Option_None())

    @staticmethod
    def GetObject(key, obj):
        d_138_valueOrError0_ = default__.Get(key, obj)
        if (d_138_valueOrError0_).IsFailure():
            return (d_138_valueOrError0_).PropagateFailure()
        elif True:
            d_139_obj_ = (d_138_valueOrError0_).Extract()
            d_140_valueOrError1_ = Wrappers.default__.Need((d_139_obj_).is_Object, _dafny.Seq("Not an object"))
            if (d_140_valueOrError1_).IsFailure():
                return (d_140_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_139_obj_).obj)

    @staticmethod
    def GetArray(key, obj):
        d_141_valueOrError0_ = default__.Get(key, obj)
        if (d_141_valueOrError0_).IsFailure():
            return (d_141_valueOrError0_).PropagateFailure()
        elif True:
            d_142_obj_ = (d_141_valueOrError0_).Extract()
            d_143_valueOrError1_ = Wrappers.default__.Need((d_142_obj_).is_Array, _dafny.Seq("Not an array"))
            if (d_143_valueOrError1_).IsFailure():
                return (d_143_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_142_obj_).arr)

    @staticmethod
    def GetArrayString(key, obj):
        d_144_valueOrError0_ = default__.Get(key, obj)
        if (d_144_valueOrError0_).IsFailure():
            return (d_144_valueOrError0_).PropagateFailure()
        elif True:
            d_145_obj_ = (d_144_valueOrError0_).Extract()
            def lambda1_(forall_var_0_):
                d_147_s_: JSON_mValues.JSON = forall_var_0_
                return not ((d_147_s_) in ((d_145_obj_).arr)) or ((d_147_s_).is_String)

            d_146_valueOrError1_ = Wrappers.default__.Need(((d_145_obj_).is_Array) and (_dafny.quantifier(((d_145_obj_).arr).UniqueElements, True, lambda1_)), _dafny.Seq("Not an array of strings"))
            if (d_146_valueOrError1_).IsFailure():
                return (d_146_valueOrError1_).PropagateFailure()
            elif True:
                d_148_arr_ = (d_145_obj_).arr
                return Wrappers.Result_Success(_dafny.Seq([((d_148_arr_)[d_149_n_]).str for d_149_n_ in range(len(d_148_arr_))]))

    @staticmethod
    def GetArrayObject(key, obj):
        d_150_valueOrError0_ = default__.Get(key, obj)
        if (d_150_valueOrError0_).IsFailure():
            return (d_150_valueOrError0_).PropagateFailure()
        elif True:
            d_151_obj_ = (d_150_valueOrError0_).Extract()
            def lambda2_(forall_var_1_):
                d_153_s_: JSON_mValues.JSON = forall_var_1_
                return not ((d_153_s_) in ((d_151_obj_).arr)) or ((d_153_s_).is_Object)

            d_152_valueOrError1_ = Wrappers.default__.Need(((d_151_obj_).is_Array) and (_dafny.quantifier(((d_151_obj_).arr).UniqueElements, True, lambda2_)), _dafny.Seq("Not an array of objects"))
            if (d_152_valueOrError1_).IsFailure():
                return (d_152_valueOrError1_).PropagateFailure()
            elif True:
                d_154_arr_ = (d_151_obj_).arr
                return Wrappers.Result_Success(_dafny.Seq([((d_154_arr_)[d_155_n_]).obj for d_155_n_ in range(len(d_154_arr_))]))

    @staticmethod
    def SmallObjectToStringStringMap(key, obj):
        d_156_valueOrError0_ = default__.Get(key, obj)
        if (d_156_valueOrError0_).IsFailure():
            return (d_156_valueOrError0_).PropagateFailure()
        elif True:
            d_157_item_ = (d_156_valueOrError0_).Extract()
            d_158_valueOrError1_ = Wrappers.default__.Need((d_157_item_).is_Object, _dafny.Seq("Not an object"))
            if (d_158_valueOrError1_).IsFailure():
                return (d_158_valueOrError1_).PropagateFailure()
            elif True:
                d_159_obj_ = (d_157_item_).obj
                def lambda3_(forall_var_2_):
                    d_161_t_: tuple = forall_var_2_
                    return not ((d_161_t_) in (d_159_obj_)) or (((d_161_t_)[1]).is_String)

                d_160_valueOrError2_ = Wrappers.default__.Need(_dafny.quantifier((d_159_obj_).UniqueElements, True, lambda3_), _dafny.Seq("Not a string string object"))
                if (d_160_valueOrError2_).IsFailure():
                    return (d_160_valueOrError2_).PropagateFailure()
                elif True:
                    def lambda4_(forall_var_3_):
                        def lambda5_(forall_var_4_):
                            d_164_j_: int = forall_var_4_
                            return not ((((0) <= (d_163_i_)) and ((d_163_i_) < (d_164_j_))) and ((d_164_j_) < (len(d_159_obj_)))) or ((((d_159_obj_)[d_163_i_])[0]) != (((d_159_obj_)[d_164_j_])[0]))

                        d_163_i_: int = forall_var_3_
                        return _dafny.quantifier(_dafny.IntegerRange((d_163_i_) + (1), len(d_159_obj_)), True, lambda5_)

                    d_162_valueOrError3_ = Wrappers.default__.Need(_dafny.quantifier(_dafny.IntegerRange(0, len(d_159_obj_)), True, lambda4_), _dafny.Seq("JSON serialization Error"))
                    if (d_162_valueOrError3_).IsFailure():
                        return (d_162_valueOrError3_).PropagateFailure()
                    elif True:
                        def iife2_():
                            coll2_ = _dafny.Map()
                            compr_2_: tuple
                            for compr_2_ in (d_159_obj_).Elements:
                                d_165_t_: tuple = compr_2_
                                if (d_165_t_) in (d_159_obj_):
                                    coll2_[(d_165_t_)[0]] = ((d_165_t_)[1]).str
                            return _dafny.Map(coll2_)
                        return Wrappers.Result_Success(iife2_()
)

    @staticmethod
    def utf8EncodePair(key, value):
        d_166_valueOrError0_ = UTF8.default__.Encode(key)
        if (d_166_valueOrError0_).IsFailure():
            return (d_166_valueOrError0_).PropagateFailure()
        elif True:
            d_167_utf8Key_ = (d_166_valueOrError0_).Extract()
            d_168_valueOrError1_ = UTF8.default__.Encode(value)
            if (d_168_valueOrError1_).IsFailure():
                return (d_168_valueOrError1_).PropagateFailure()
            elif True:
                d_169_utf8Value_ = (d_168_valueOrError1_).Extract()
                return Wrappers.Result_Success((d_167_utf8Key_, d_169_utf8Value_))

    @staticmethod
    def utf8EncodeMap(mapStringString):
        if (len(mapStringString)) == (0):
            return Wrappers.Result_Success(_dafny.Map({}))
        elif True:
            def iife3_():
                coll3_ = _dafny.Map()
                compr_3_: _dafny.Seq
                for compr_3_ in (mapStringString).keys.Elements:
                    d_171_key_: _dafny.Seq = compr_3_
                    if (d_171_key_) in (mapStringString):
                        coll3_[d_171_key_] = default__.utf8EncodePair(d_171_key_, (mapStringString)[d_171_key_])
                return _dafny.Map(coll3_)
            d_170_encodedResults_ = iife3_()

            def lambda6_(forall_var_5_):
                d_173_r_: Wrappers.Result = forall_var_5_
                return not ((d_173_r_) in ((d_170_encodedResults_).values)) or ((d_173_r_).is_Success)

            d_172_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier(((d_170_encodedResults_).values).Elements, True, lambda6_), _dafny.Seq("String can not be UTF8 Encoded?"))
            if (d_172_valueOrError0_).IsFailure():
                return (d_172_valueOrError0_).PropagateFailure()
            elif True:
                def iife4_():
                    coll4_ = _dafny.Map()
                    compr_4_: Wrappers.Result
                    for compr_4_ in ((d_170_encodedResults_).values).Elements:
                        d_174_r_: Wrappers.Result = compr_4_
                        if (d_174_r_) in ((d_170_encodedResults_).values):
                            coll4_[((d_174_r_).value)[0]] = ((d_174_r_).value)[1]
                    return _dafny.Map(coll4_)
                return Wrappers.Result_Success(iife4_()
)

    @staticmethod
    def utf8EncodeSeq(seqOfStrings):
        d_175_encodedResults_ = _dafny.Seq([UTF8.default__.Encode((seqOfStrings)[d_176_i_]) for d_176_i_ in range(len(seqOfStrings))])
        def lambda7_(forall_var_6_):
            d_178_r_: Wrappers.Result = forall_var_6_
            return not ((d_178_r_) in (d_175_encodedResults_)) or ((d_178_r_).is_Success)

        d_177_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier((d_175_encodedResults_).UniqueElements, True, lambda7_), _dafny.Seq("String can not be UTF8 Encoded?"))
        if (d_177_valueOrError0_).IsFailure():
            return (d_177_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(_dafny.Seq([((d_175_encodedResults_)[d_179_i_]).value for d_179_i_ in range(len(d_175_encodedResults_))]))

