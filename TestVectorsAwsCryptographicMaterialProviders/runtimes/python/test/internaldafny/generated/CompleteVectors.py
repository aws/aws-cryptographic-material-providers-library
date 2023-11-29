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
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types
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
import JSONHelpers
import KeyDescription
import KeyMaterial
import CreateStaticKeyrings
import CreateStaticKeyStores
import KeyringFromKeyDescription
import KeysVectorOperations
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny
import TestVectors

# Module: CompleteVectors

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetCompatableCommitmentPolicy(algorithmSuite):
        source55_ = (algorithmSuite).id
        if source55_.is_ESDK:
            d_1799___mcc_h0_ = source55_.ESDK
            if ((algorithmSuite).commitment).is_None:
                return software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT())
            elif True:
                return software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT())
        elif True:
            d_1800___mcc_h1_ = source55_.DBE
            return software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT())

    @staticmethod
    def WriteStuff():
        d_1801_tests_: _dafny.Seq
        d_1801_tests_ = SortedSets.default__.SetToSequence(default__.AllPositiveKeyringTests)
        d_1802_testsJSON_: _dafny.Seq
        d_1802_testsJSON_ = _dafny.Seq([])
        hi17_ = len(d_1801_tests_)
        for d_1803_i_ in range(0, hi17_):
            d_1804_name_: _dafny.Seq
            d_1805_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out334_: Wrappers.Result
            out334_ = UUID.default__.GenerateUUID()
            d_1805_valueOrError0_ = out334_
            if not(not((d_1805_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CompleteVectors.dfy(281,15): " + _dafny.string_of(d_1805_valueOrError0_))
            d_1804_name_ = (d_1805_valueOrError0_).Extract()
            d_1802_testsJSON_ = (d_1802_testsJSON_) + (_dafny.Seq([(d_1804_name_, (d_1801_tests_)[d_1803_i_])]))
        d_1806_mplEncryptManifies_: JSON_mValues.JSON
        d_1806_mplEncryptManifies_ = JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("tests"), JSON_mValues.JSON_Object(d_1802_testsJSON_))]))
        d_1807_mplEncryptManifiesBytes_: _dafny.Seq
        d_1808_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1808_valueOrError1_ = JSON_mAPI.default__.Serialize(d_1806_mplEncryptManifies_)
        if not(not((d_1808_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CompleteVectors.dfy(290,32): " + _dafny.string_of(d_1808_valueOrError1_))
        d_1807_mplEncryptManifiesBytes_ = (d_1808_valueOrError1_).Extract()
        d_1809_mplEncryptManifiesBv_: _dafny.Seq
        d_1809_mplEncryptManifiesBv_ = JSONHelpers.default__.BytesBv(d_1807_mplEncryptManifiesBytes_)
        d_1810___v3_: tuple
        d_1811_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out335_: Wrappers.Result
        out335_ = FileIO.default__.WriteBytesToFile(_dafny.Seq("dafny/TestVectorsAwsCryptographicMaterialProviders/test/test.json"), d_1809_mplEncryptManifiesBv_)
        d_1811_valueOrError2_ = out335_
        if not(not((d_1811_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CompleteVectors.dfy(293,10): " + _dafny.string_of(d_1811_valueOrError2_))
        d_1810___v3_ = (d_1811_valueOrError2_).Extract()

    @_dafny.classproperty
    def ESDKAlgorithmSuites(instance):
        def iife87_():
            coll9_ = _dafny.Set()
            compr_9_: software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId
            for compr_9_ in software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId.AllSingletonConstructors:
                d_1812_id_: software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId = compr_9_
                if True:
                    coll9_ = coll9_.union(_dafny.Set([AlgorithmSuites.default__.GetESDKSuite(d_1812_id_)]))
            return _dafny.Set(coll9_)
        return iife87_()
        
    @_dafny.classproperty
    def DBEAlgorithmSuites(instance):
        def iife88_():
            coll10_ = _dafny.Set()
            compr_10_: software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId
            for compr_10_ in software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId.AllSingletonConstructors:
                d_1813_id_: software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId = compr_10_
                if True:
                    coll10_ = coll10_.union(_dafny.Set([AlgorithmSuites.default__.GetDBESuite(d_1813_id_)]))
            return _dafny.Set(coll10_)
        return iife88_()
        
    @_dafny.classproperty
    def aesPersistentKeyNames(instance):
        return _dafny.Seq([_dafny.Seq("aes-128"), _dafny.Seq("aes-192"), _dafny.Seq("aes-256")])
    @_dafny.classproperty
    def AllRawAES(instance):
        def iife89_():
            coll11_ = _dafny.Set()
            compr_11_: _dafny.Seq
            for compr_11_ in (default__.aesPersistentKeyNames).Elements:
                d_1814_key_: _dafny.Seq = compr_11_
                if (d_1814_key_) in (default__.aesPersistentKeyNames):
                    def iife90_(_pat_let39_0):
                        def iife91_(d_1815_keyDescription_):
                            return PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((_dafny.Seq("Generated RawAES ")) + (d_1814_key_), d_1815_keyDescription_, d_1815_keyDescription_)
                        return iife91_(_pat_let39_0)
                    coll11_ = coll11_.union(_dafny.Set([iife90_(JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("raw"))), (_dafny.Seq("encryption-algorithm"), JSON_mValues.JSON_String(_dafny.Seq("aes"))), (_dafny.Seq("provider-id"), JSON_mValues.JSON_String((_dafny.Seq("aws-raw-vectors-persistent-")) + (d_1814_key_))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1814_key_))])))]))
            return _dafny.Set(coll11_)
        return iife89_()
        
    @_dafny.classproperty
    def rsaPersistentKeyNamesWithoutPublicPrivate(instance):
        return _dafny.Seq([_dafny.Seq("rsa-4096")])
    @_dafny.classproperty
    def AllRawRSA(instance):
        def iife92_():
            coll12_ = _dafny.Set()
            compr_12_: _dafny.Seq
            for compr_12_ in (default__.rsaPersistentKeyNamesWithoutPublicPrivate).Elements:
                d_1816_key_: _dafny.Seq = compr_12_
                compr_13_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme
                for compr_13_ in software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme.AllSingletonConstructors:
                    d_1817_padding_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme = compr_13_
                    if (d_1816_key_) in (default__.rsaPersistentKeyNamesWithoutPublicPrivate):
                        def lambda119_(source56_):
                            if source56_.is_PKCS1:
                                return _dafny.Seq("pkcs1")
                            elif source56_.is_OAEP__SHA1__MGF1:
                                return _dafny.Seq("oaep-mgf1")
                            elif source56_.is_OAEP__SHA256__MGF1:
                                return _dafny.Seq("oaep-mgf1")
                            elif source56_.is_OAEP__SHA384__MGF1:
                                return _dafny.Seq("oaep-mgf1")
                            elif True:
                                return _dafny.Seq("oaep-mgf1")

                        def lambda120_(source57_):
                            if source57_.is_PKCS1:
                                return _dafny.Seq("sha1")
                            elif source57_.is_OAEP__SHA1__MGF1:
                                return _dafny.Seq("sha1")
                            elif source57_.is_OAEP__SHA256__MGF1:
                                return _dafny.Seq("sha256")
                            elif source57_.is_OAEP__SHA384__MGF1:
                                return _dafny.Seq("sha384")
                            elif True:
                                return _dafny.Seq("sha512")

                        def iife93_(_pat_let40_0):
                            def iife94_(d_1818_sharedOptions_):
                                def lambda121_(source58_):
                                    if source58_.is_PKCS1:
                                        return _dafny.Seq("pkcs1-sha1")
                                    elif source58_.is_OAEP__SHA1__MGF1:
                                        return _dafny.Seq("oaep-mgf1-sha1")
                                    elif source58_.is_OAEP__SHA256__MGF1:
                                        return _dafny.Seq("oaep-mgf1-sha256")
                                    elif source58_.is_OAEP__SHA384__MGF1:
                                        return _dafny.Seq("oaep-mgf1-sha384")
                                    elif True:
                                        return _dafny.Seq("oaep-mgf1-sha512")

                                return PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((((_dafny.Seq("Generated RawRSA ")) + (d_1816_key_)) + (_dafny.Seq(" "))) + (lambda121_(d_1817_padding_)), JSON_mValues.JSON_Object((d_1818_sharedOptions_) + (_dafny.Seq([(_dafny.Seq("key"), JSON_mValues.JSON_String((d_1816_key_) + (_dafny.Seq("-public"))))]))), JSON_mValues.JSON_Object((d_1818_sharedOptions_) + (_dafny.Seq([(_dafny.Seq("key"), JSON_mValues.JSON_String((d_1816_key_) + (_dafny.Seq("-private"))))]))))
                            return iife94_(_pat_let40_0)
                        coll12_ = coll12_.union(_dafny.Set([iife93_(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("raw"))), (_dafny.Seq("encryption-algorithm"), JSON_mValues.JSON_String(_dafny.Seq("rsa"))), (_dafny.Seq("provider-id"), JSON_mValues.JSON_String((_dafny.Seq("aws-raw-vectors-persistent-")) + (d_1816_key_))), (_dafny.Seq("padding-algorithm"), JSON_mValues.JSON_String(lambda119_(d_1817_padding_))), (_dafny.Seq("padding-hash"), JSON_mValues.JSON_String(lambda120_(d_1817_padding_)))]))]))
            return _dafny.Set(coll12_)
        return iife92_()
        
    @_dafny.classproperty
    def AllAwsKMSKeys(instance):
        return _dafny.Seq([_dafny.Seq("us-west-2-decryptable"), _dafny.Seq("us-west-2-mrk")])
    @_dafny.classproperty
    def AllKMSInfo(instance):
        def iife95_():
            coll13_ = _dafny.Set()
            compr_14_: _dafny.Seq
            for compr_14_ in (default__.AllAwsKMSKeys).Elements:
                d_1819_key_: _dafny.Seq = compr_14_
                if (d_1819_key_) in (default__.AllAwsKMSKeys):
                    def iife96_(_pat_let41_0):
                        def iife97_(d_1820_keyDescription_):
                            return PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((_dafny.Seq("Generated KMS ")) + (d_1819_key_), d_1820_keyDescription_, d_1820_keyDescription_)
                        return iife97_(_pat_let41_0)
                    coll13_ = coll13_.union(_dafny.Set([iife96_(JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1819_key_))])))]))
            return _dafny.Set(coll13_)
        return iife95_()
        
    @_dafny.classproperty
    def AllAwsKMSMrkKeys(instance):
        return _dafny.Seq([_dafny.Seq("us-west-2-mrk"), _dafny.Seq("us-east-1-mrk")])
    @_dafny.classproperty
    def AllKmsMrkAware(instance):
        def iife98_():
            coll14_ = _dafny.Set()
            compr_15_: _dafny.Seq
            for compr_15_ in (default__.AllAwsKMSMrkKeys).Elements:
                d_1821_encryptKey_: _dafny.Seq = compr_15_
                compr_16_: _dafny.Seq
                for compr_16_ in (default__.AllAwsKMSMrkKeys).Elements:
                    d_1822_decryptKey_: _dafny.Seq = compr_16_
                    if ((d_1821_encryptKey_) in (default__.AllAwsKMSMrkKeys)) and ((d_1822_decryptKey_) in (default__.AllAwsKMSMrkKeys)):
                        coll14_ = coll14_.union(_dafny.Set([PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((((_dafny.Seq("Generated KMS MRK ")) + (d_1821_encryptKey_)) + (_dafny.Seq("->"))) + (d_1822_decryptKey_), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-mrk-aware"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1821_encryptKey_))])), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-mrk-aware"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1822_decryptKey_))])))]))
            return _dafny.Set(coll14_)
        return iife98_()
        
    @_dafny.classproperty
    def AllDiscoveryFilters(instance):
        return _dafny.Set({Wrappers.Option_Some(software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter_DiscoveryFilter(_dafny.Seq([_dafny.Seq("658956600833")]), _dafny.Seq("aws"))), Wrappers.Option_None()})
    @_dafny.classproperty
    def AllKmsMrkAwareDiscovery(instance):
        def iife99_():
            coll15_ = _dafny.Set()
            compr_17_: _dafny.Seq
            for compr_17_ in (default__.AllAwsKMSMrkKeys).Elements:
                d_1823_keyId_: _dafny.Seq = compr_17_
                compr_18_: Wrappers.Option
                for compr_18_ in (default__.AllDiscoveryFilters).Elements:
                    d_1824_filter_: Wrappers.Option = compr_18_
                    if ((d_1823_keyId_) in (default__.AllAwsKMSMrkKeys)) and ((d_1824_filter_) in (default__.AllDiscoveryFilters)):
                        def lambda122_(d_1825_s_):
                            return JSON_mValues.JSON_String(d_1825_s_)

                        coll15_ = coll15_.union(_dafny.Set([PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((((_dafny.Seq("Discovery KMS MRK ")) + (d_1823_keyId_)) + (_dafny.Seq("->"))) + (((((_dafny.Seq("Filter ")) + (((d_1824_filter_).value).partition)) + (_dafny.Seq(" "))) + (Seq.default__.Flatten(((d_1824_filter_).value).accountIds)) if (d_1824_filter_).is_Some else _dafny.Seq("No Filter"))), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-mrk-aware"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1823_keyId_))])), (JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-mrk-aware-discovery"))), (_dafny.Seq("default-mrk-region"), JSON_mValues.JSON_String(_dafny.Seq("us-west-2"))), (_dafny.Seq("aws-kms-discovery-filter"), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("partition"), JSON_mValues.JSON_String(((d_1824_filter_).value).partition)), (_dafny.Seq("account-ids"), JSON_mValues.JSON_Array(Seq.default__.Map(lambda122_, ((d_1824_filter_).value).accountIds)))])))])) if (d_1824_filter_).is_Some else JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-mrk-aware-discovery"))), (_dafny.Seq("default-mrk-region"), JSON_mValues.JSON_String(_dafny.Seq("us-west-2")))]))))]))
            return _dafny.Set(coll15_)
        return iife99_()
        
    @_dafny.classproperty
    def AllHierarchy(instance):
        def iife100_():
            coll16_ = _dafny.Set()
            compr_19_: _dafny.Seq
            for compr_19_ in (_dafny.Seq([_dafny.Seq("static-branch-key-1")])).Elements:
                d_1826_keyId_: _dafny.Seq = compr_19_
                if (d_1826_keyId_) in (_dafny.Seq([_dafny.Seq("static-branch-key-1")])):
                    coll16_ = coll16_.union(_dafny.Set([PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((_dafny.Seq("Hierarchy KMS ")) + (d_1826_keyId_), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-hierarchy"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1826_keyId_))])), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-hierarchy"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1826_keyId_))])))]))
            return _dafny.Set(coll16_)
        return iife100_()
        
    @_dafny.classproperty
    def AllKmsRsaKeys(instance):
        return _dafny.Seq([_dafny.Seq("us-west-2-rsa-mrk")])
    @_dafny.classproperty
    def AllEncryptionAlgorithmSpec(instance):
        def iife101_():
            coll17_ = _dafny.Set()
            compr_20_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec
            for compr_20_ in software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec.AllSingletonConstructors:
                d_1827_e_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = compr_20_
                if not((d_1827_e_).is_SYMMETRIC__DEFAULT):
                    def lambda123_(source59_):
                        if source59_.is_RSAES__OAEP__SHA__1:
                            return _dafny.Seq("RSAES_OAEP_SHA_1")
                        elif True:
                            return _dafny.Seq("RSAES_OAEP_SHA_256")

                    coll17_ = coll17_.union(_dafny.Set([lambda123_(d_1827_e_)]))
            return _dafny.Set(coll17_)
        return iife101_()
        
    @_dafny.classproperty
    def KmsRsa(instance):
        return _dafny.Seq("KMS RSA ")
    @_dafny.classproperty
    def AllKmsRsa(instance):
        def iife102_():
            coll18_ = _dafny.Set()
            compr_21_: _dafny.Seq
            for compr_21_ in (default__.AllKmsRsaKeys).Elements:
                d_1828_keyId_: _dafny.Seq = compr_21_
                compr_22_: _dafny.Seq
                for compr_22_ in (default__.AllEncryptionAlgorithmSpec).Elements:
                    d_1829_algorithmSpec_: _dafny.Seq = compr_22_
                    if ((d_1828_keyId_) in (default__.AllKmsRsaKeys)) and ((d_1829_algorithmSpec_) in (default__.AllEncryptionAlgorithmSpec)):
                        coll18_ = coll18_.union(_dafny.Set([PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((default__.KmsRsa) + (d_1828_keyId_), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-rsa"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1828_keyId_)), (_dafny.Seq("encryption-algorithm"), JSON_mValues.JSON_String(d_1829_algorithmSpec_))])), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-rsa"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1828_keyId_)), (_dafny.Seq("encryption-algorithm"), JSON_mValues.JSON_String(d_1829_algorithmSpec_))])))]))
            return _dafny.Set(coll18_)
        return iife102_()
        
    @_dafny.classproperty
    def AllPositiveKeyringTests(instance):
        def iife103_():
            coll19_ = _dafny.Set()
            compr_23_: PositiveKeyDescriptionJSON
            for compr_23_ in (((((((default__.AllKMSInfo) | (default__.AllKmsMrkAware)) | (default__.AllKmsMrkAwareDiscovery)) | (default__.AllRawAES)) | (default__.AllRawRSA)) | (default__.AllHierarchy)) | (default__.AllKmsRsa)).Elements:
                d_1830_postiveKeyDescription_: PositiveKeyDescriptionJSON = compr_23_
                compr_24_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
                for compr_24_ in ((default__.ESDKAlgorithmSuites) | (default__.DBEAlgorithmSuites)).Elements:
                    d_1831_algorithmSuite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo = compr_24_
                    if (((d_1830_postiveKeyDescription_) in (((((((default__.AllKMSInfo) | (default__.AllKmsMrkAware)) | (default__.AllKmsMrkAwareDiscovery)) | (default__.AllRawAES)) | (default__.AllRawRSA)) | (default__.AllHierarchy)) | (default__.AllKmsRsa))) and ((d_1831_algorithmSuite_) in ((default__.ESDKAlgorithmSuites) | (default__.DBEAlgorithmSuites)))) and (not(((_dafny.Seq(((d_1830_postiveKeyDescription_).description)[:len(default__.KmsRsa):])) == (default__.KmsRsa)) and (((d_1831_algorithmSuite_).signature).is_ECDSA))):
                        def iife104_(_pat_let42_0):
                            def iife105_(d_1832_id_):
                                return JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("positive-keyring"))), (_dafny.Seq("description"), JSON_mValues.JSON_String((((d_1830_postiveKeyDescription_).description) + (_dafny.Seq(" "))) + (d_1832_id_))), (_dafny.Seq("algorithmSuiteId"), JSON_mValues.JSON_String(d_1832_id_)), (_dafny.Seq("encryptionContext"), JSON_mValues.JSON_Object(_dafny.Seq([]))), (_dafny.Seq("requiredEncryptionContextKeys"), JSON_mValues.JSON_Array(_dafny.Seq([]))), (_dafny.Seq("encryptKeyDescription"), (d_1830_postiveKeyDescription_).encrypt), (_dafny.Seq("decryptKeyDescription"), (d_1830_postiveKeyDescription_).decrypt)]))
                            return iife105_(_pat_let42_0)
                        coll19_ = coll19_.union(_dafny.Set([iife104_(HexStrings.default__.ToHexString((d_1831_algorithmSuite_).binaryId))]))
            return _dafny.Set(coll19_)
        return iife103_()
        
    @_dafny.classproperty
    def AwsPartitions(instance):
        return _dafny.Seq([_dafny.Seq("aws")])
    @_dafny.classproperty
    def AWSAccounts(instance):
        return _dafny.Seq([_dafny.Seq("658956600833")])

class PositiveKeyDescriptionJSON:
    @classmethod
    def default(cls, ):
        return lambda: PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON(_dafny.Seq({}), JSON_mValues.JSON.default()(), JSON_mValues.JSON.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PositiveKeyDescriptionJSON(self) -> bool:
        return isinstance(self, PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON)

class PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON(PositiveKeyDescriptionJSON, NamedTuple('PositiveKeyDescriptionJSON', [('description', Any), ('encrypt', Any), ('decrypt', Any)])):
    def __dafnystr__(self) -> str:
        return f'CompleteVectors.PositiveKeyDescriptionJSON.PositiveKeyDescriptionJSON({_dafny.string_of(self.description)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.decrypt)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON) and self.description == __o.description and self.encrypt == __o.encrypt and self.decrypt == __o.decrypt
    def __hash__(self) -> int:
        return super().__hash__()

