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
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
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
import software_amazon_cryptography_services_kms_internaldafny
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
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
        return _dafny.Seq([(bits)[d_1358_i_] for d_1358_i_ in range(len(bits))])

    @staticmethod
    def BytesBv(bits):
        return _dafny.Seq([(bits)[d_1359_i_] for d_1359_i_ in range(len(bits))])

    @staticmethod
    def Get(key, obj):
        while True:
            with _dafny.label():
                if (len(obj)) == (0):
                    return Wrappers.Result_Failure(((_dafny.Seq("Key: ")) + (key)) + (_dafny.Seq(" does not exist")))
                elif (((obj)[0])[0]) == (key):
                    return Wrappers.Result_Success(((obj)[0])[1])
                elif True:
                    in2_ = key
                    in3_ = _dafny.Seq((obj)[1::])
                    key = in2_
                    obj = in3_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def GetString(key, obj):
        d_1360_valueOrError0_ = default__.Get(key, obj)
        if (d_1360_valueOrError0_).IsFailure():
            return (d_1360_valueOrError0_).PropagateFailure()
        elif True:
            d_1361_obj_ = (d_1360_valueOrError0_).Extract()
            d_1362_valueOrError1_ = Wrappers.default__.Need((d_1361_obj_).is_String, _dafny.Seq("Not a string"))
            if (d_1362_valueOrError1_).IsFailure():
                return (d_1362_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_1361_obj_).str)

    @staticmethod
    def GetBool(key, obj):
        d_1363_valueOrError0_ = default__.Get(key, obj)
        if (d_1363_valueOrError0_).IsFailure():
            return (d_1363_valueOrError0_).PropagateFailure()
        elif True:
            d_1364_obj_ = (d_1363_valueOrError0_).Extract()
            d_1365_valueOrError1_ = Wrappers.default__.Need((d_1364_obj_).is_Bool, _dafny.Seq("Not a bool"))
            if (d_1365_valueOrError1_).IsFailure():
                return (d_1365_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_1364_obj_).b)

    @staticmethod
    def GetNat(key, obj):
        d_1366_valueOrError0_ = default__.Get(key, obj)
        if (d_1366_valueOrError0_).IsFailure():
            return (d_1366_valueOrError0_).PropagateFailure()
        elif True:
            d_1367_obj_ = (d_1366_valueOrError0_).Extract()
            d_1368_valueOrError1_ = Wrappers.default__.Need((d_1367_obj_).is_Number, _dafny.Seq("Not a number"))
            if (d_1368_valueOrError1_).IsFailure():
                return (d_1368_valueOrError1_).PropagateFailure()
            elif True:
                d_1369_valueOrError2_ = Wrappers.default__.Need((0) < (((d_1367_obj_).num).n), _dafny.Seq("Not a nat"))
                if (d_1369_valueOrError2_).IsFailure():
                    return (d_1369_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(((d_1367_obj_).num).n)

    @staticmethod
    def GetOptionalString(key, obj):
        d_1370_obj_ = (default__.Get(key, obj)).ToOption()
        if (d_1370_obj_).is_Some:
            d_1371_valueOrError0_ = Wrappers.default__.Need(((d_1370_obj_).value).is_String, _dafny.Seq("Not a string"))
            if (d_1371_valueOrError0_).IsFailure():
                return (d_1371_valueOrError0_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(Wrappers.Option_Some(((d_1370_obj_).value).str))
        elif True:
            return Wrappers.Result_Success(Wrappers.Option_None())

    @staticmethod
    def GetObject(key, obj):
        d_1372_valueOrError0_ = default__.Get(key, obj)
        if (d_1372_valueOrError0_).IsFailure():
            return (d_1372_valueOrError0_).PropagateFailure()
        elif True:
            d_1373_obj_ = (d_1372_valueOrError0_).Extract()
            d_1374_valueOrError1_ = Wrappers.default__.Need((d_1373_obj_).is_Object, _dafny.Seq("Not an object"))
            if (d_1374_valueOrError1_).IsFailure():
                return (d_1374_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_1373_obj_).obj)

    @staticmethod
    def GetArray(key, obj):
        d_1375_valueOrError0_ = default__.Get(key, obj)
        if (d_1375_valueOrError0_).IsFailure():
            return (d_1375_valueOrError0_).PropagateFailure()
        elif True:
            d_1376_obj_ = (d_1375_valueOrError0_).Extract()
            d_1377_valueOrError1_ = Wrappers.default__.Need((d_1376_obj_).is_Array, _dafny.Seq("Not an array"))
            if (d_1377_valueOrError1_).IsFailure():
                return (d_1377_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success((d_1376_obj_).arr)

    @staticmethod
    def GetArrayString(key, obj):
        d_1378_valueOrError0_ = default__.Get(key, obj)
        if (d_1378_valueOrError0_).IsFailure():
            return (d_1378_valueOrError0_).PropagateFailure()
        elif True:
            d_1379_obj_ = (d_1378_valueOrError0_).Extract()
            def lambda83_(forall_var_15_):
                d_1381_s_: JSON_mValues.JSON = forall_var_15_
                return not ((d_1381_s_) in ((d_1379_obj_).arr)) or ((d_1381_s_).is_String)

            d_1380_valueOrError1_ = Wrappers.default__.Need(((d_1379_obj_).is_Array) and (_dafny.quantifier(((d_1379_obj_).arr).UniqueElements, True, lambda83_)), _dafny.Seq("Not an array of strings"))
            if (d_1380_valueOrError1_).IsFailure():
                return (d_1380_valueOrError1_).PropagateFailure()
            elif True:
                d_1382_arr_ = (d_1379_obj_).arr
                return Wrappers.Result_Success(_dafny.Seq([((d_1382_arr_)[d_1383_n_]).str for d_1383_n_ in range(len(d_1382_arr_))]))

    @staticmethod
    def GetArrayObject(key, obj):
        d_1384_valueOrError0_ = default__.Get(key, obj)
        if (d_1384_valueOrError0_).IsFailure():
            return (d_1384_valueOrError0_).PropagateFailure()
        elif True:
            d_1385_obj_ = (d_1384_valueOrError0_).Extract()
            def lambda84_(forall_var_16_):
                d_1387_s_: JSON_mValues.JSON = forall_var_16_
                return not ((d_1387_s_) in ((d_1385_obj_).arr)) or ((d_1387_s_).is_Object)

            d_1386_valueOrError1_ = Wrappers.default__.Need(((d_1385_obj_).is_Array) and (_dafny.quantifier(((d_1385_obj_).arr).UniqueElements, True, lambda84_)), _dafny.Seq("Not an array of objects"))
            if (d_1386_valueOrError1_).IsFailure():
                return (d_1386_valueOrError1_).PropagateFailure()
            elif True:
                d_1388_arr_ = (d_1385_obj_).arr
                return Wrappers.Result_Success(_dafny.Seq([((d_1388_arr_)[d_1389_n_]).obj for d_1389_n_ in range(len(d_1388_arr_))]))

    @staticmethod
    def SmallObjectToStringStringMap(key, obj):
        d_1390_valueOrError0_ = default__.Get(key, obj)
        if (d_1390_valueOrError0_).IsFailure():
            return (d_1390_valueOrError0_).PropagateFailure()
        elif True:
            d_1391_item_ = (d_1390_valueOrError0_).Extract()
            d_1392_valueOrError1_ = Wrappers.default__.Need((d_1391_item_).is_Object, _dafny.Seq("Not an object"))
            if (d_1392_valueOrError1_).IsFailure():
                return (d_1392_valueOrError1_).PropagateFailure()
            elif True:
                d_1393_obj_ = (d_1391_item_).obj
                def lambda85_(forall_var_17_):
                    d_1395_t_: tuple = forall_var_17_
                    return not ((d_1395_t_) in (d_1393_obj_)) or (((d_1395_t_)[1]).is_String)

                d_1394_valueOrError2_ = Wrappers.default__.Need(_dafny.quantifier((d_1393_obj_).UniqueElements, True, lambda85_), _dafny.Seq("Not a string string object"))
                if (d_1394_valueOrError2_).IsFailure():
                    return (d_1394_valueOrError2_).PropagateFailure()
                elif True:
                    def lambda86_(forall_var_18_):
                        def lambda87_(forall_var_19_):
                            d_1398_j_: int = forall_var_19_
                            return not ((((0) <= (d_1397_i_)) and ((d_1397_i_) < (d_1398_j_))) and ((d_1398_j_) < (len(d_1393_obj_)))) or ((((d_1393_obj_)[d_1397_i_])[0]) != (((d_1393_obj_)[d_1398_j_])[0]))

                        d_1397_i_: int = forall_var_18_
                        return _dafny.quantifier(_dafny.IntegerRange((d_1397_i_) + (1), len(d_1393_obj_)), True, lambda87_)

                    d_1396_valueOrError3_ = Wrappers.default__.Need(_dafny.quantifier(_dafny.IntegerRange(0, len(d_1393_obj_)), True, lambda86_), _dafny.Seq("JSON serialization Error"))
                    if (d_1396_valueOrError3_).IsFailure():
                        return (d_1396_valueOrError3_).PropagateFailure()
                    elif True:
                        def iife58_():
                            coll6_ = _dafny.Map()
                            compr_6_: tuple
                            for compr_6_ in (d_1393_obj_).Elements:
                                d_1399_t_: tuple = compr_6_
                                if (d_1399_t_) in (d_1393_obj_):
                                    coll6_[(d_1399_t_)[0]] = ((d_1399_t_)[1]).str
                            return _dafny.Map(coll6_)
                        return Wrappers.Result_Success(iife58_()
)

    @staticmethod
    def utf8EncodePair(key, value):
        d_1400_valueOrError0_ = UTF8.default__.Encode(key)
        if (d_1400_valueOrError0_).IsFailure():
            return (d_1400_valueOrError0_).PropagateFailure()
        elif True:
            d_1401_utf8Key_ = (d_1400_valueOrError0_).Extract()
            d_1402_valueOrError1_ = UTF8.default__.Encode(value)
            if (d_1402_valueOrError1_).IsFailure():
                return (d_1402_valueOrError1_).PropagateFailure()
            elif True:
                d_1403_utf8Value_ = (d_1402_valueOrError1_).Extract()
                return Wrappers.Result_Success((d_1401_utf8Key_, d_1403_utf8Value_))

    @staticmethod
    def utf8EncodeMap(mapStringString):
        if (len(mapStringString)) == (0):
            return Wrappers.Result_Success(_dafny.Map({}))
        elif True:
            def iife59_():
                coll7_ = _dafny.Map()
                compr_7_: _dafny.Seq
                for compr_7_ in (mapStringString).keys.Elements:
                    d_1405_key_: _dafny.Seq = compr_7_
                    if (d_1405_key_) in (mapStringString):
                        coll7_[d_1405_key_] = default__.utf8EncodePair(d_1405_key_, (mapStringString)[d_1405_key_])
                return _dafny.Map(coll7_)
            d_1404_encodedResults_ = iife59_()

            def lambda88_(forall_var_20_):
                d_1407_r_: Wrappers.Result = forall_var_20_
                return not ((d_1407_r_) in ((d_1404_encodedResults_).values)) or ((d_1407_r_).is_Success)

            d_1406_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier(((d_1404_encodedResults_).values).Elements, True, lambda88_), _dafny.Seq("String can not be UTF8 Encoded?"))
            if (d_1406_valueOrError0_).IsFailure():
                return (d_1406_valueOrError0_).PropagateFailure()
            elif True:
                def iife60_():
                    coll8_ = _dafny.Map()
                    compr_8_: Wrappers.Result
                    for compr_8_ in ((d_1404_encodedResults_).values).Elements:
                        d_1408_r_: Wrappers.Result = compr_8_
                        if (d_1408_r_) in ((d_1404_encodedResults_).values):
                            coll8_[((d_1408_r_).value)[0]] = ((d_1408_r_).value)[1]
                    return _dafny.Map(coll8_)
                return Wrappers.Result_Success(iife60_()
)

    @staticmethod
    def utf8EncodeSeq(seqOfStrings):
        d_1409_encodedResults_ = _dafny.Seq([UTF8.default__.Encode((seqOfStrings)[d_1410_i_]) for d_1410_i_ in range(len(seqOfStrings))])
        def lambda89_(forall_var_21_):
            d_1412_r_: Wrappers.Result = forall_var_21_
            return not ((d_1412_r_) in (d_1409_encodedResults_)) or ((d_1412_r_).is_Success)

        d_1411_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier((d_1409_encodedResults_).UniqueElements, True, lambda89_), _dafny.Seq("String can not be UTF8 Encoded?"))
        if (d_1411_valueOrError0_).IsFailure():
            return (d_1411_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(_dafny.Seq([((d_1409_encodedResults_)[d_1413_i_]).value for d_1413_i_ in range(len(d_1409_encodedResults_))]))

