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

assert "CompleteVectors" == __name__
CompleteVectors = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetCompatableCommitmentPolicy(algorithmSuite):
        source55_ = (algorithmSuite).id
        if source55_.is_ESDK:
            d_1797___mcc_h0_ = source55_.ESDK
            if ((algorithmSuite).commitment).is_None:
                return software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT())
            elif True:
                return software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT())
        elif True:
            d_1798___mcc_h1_ = source55_.DBE
            return software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT())

    @staticmethod
    def WriteStuff():
        d_1799_tests_: _dafny.Seq
        d_1799_tests_ = SortedSets.default__.SetToSequence((CompleteVectors.default__).AllPositiveKeyringTests)
        d_1800_testsJSON_: _dafny.Seq
        d_1800_testsJSON_ = _dafny.Seq([])
        hi17_: int = len(d_1799_tests_)
        for d_1801_i_ in range(0, hi17_):
            d_1802_name_: _dafny.Seq
            d_1803_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
            out334_: Wrappers.Result
            out334_ = UUID.default__.GenerateUUID()
            d_1803_valueOrError0_ = out334_
            if not(not((d_1803_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CompleteVectors.dfy(281,15): " + _dafny.string_of(d_1803_valueOrError0_))
            d_1802_name_ = (d_1803_valueOrError0_).Extract()
            d_1800_testsJSON_ = (d_1800_testsJSON_) + (_dafny.Seq([(d_1802_name_, (d_1799_tests_)[d_1801_i_])]))
        d_1804_mplEncryptManifies_: JSON_mValues.JSON
        d_1804_mplEncryptManifies_ = JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("tests"), JSON_mValues.JSON_Object(d_1800_testsJSON_))]))
        d_1805_mplEncryptManifiesBytes_: _dafny.Seq
        d_1806_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1806_valueOrError1_ = JSON_mAPI.default__.Serialize(d_1804_mplEncryptManifies_)
        if not(not((d_1806_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CompleteVectors.dfy(290,32): " + _dafny.string_of(d_1806_valueOrError1_))
        d_1805_mplEncryptManifiesBytes_ = (d_1806_valueOrError1_).Extract()
        d_1807_mplEncryptManifiesBv_: _dafny.Seq
        d_1807_mplEncryptManifiesBv_ = JSONHelpers.default__.BytesBv(d_1805_mplEncryptManifiesBytes_)
        d_1808___v3_: tuple
        d_1809_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out335_: Wrappers.Result
        out335_ = FileIO.default__.WriteBytesToFile(_dafny.Seq("dafny/TestVectorsAwsCryptographicMaterialProviders/test/test.json"), d_1807_mplEncryptManifiesBv_)
        d_1809_valueOrError2_ = out335_
        if not(not((d_1809_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CompleteVectors.dfy(293,10): " + _dafny.string_of(d_1809_valueOrError2_))
        d_1808___v3_ = (d_1809_valueOrError2_).Extract()

    @_dafny.classproperty
    def ESDKAlgorithmSuites(instance):
        def iife83_():
            coll9_ = _dafny.Set()
            compr_9_: software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId
            for compr_9_ in software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId.AllSingletonConstructors:
                d_1810_id_: software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId = compr_9_
                if True:
                    coll9_ = coll9_.union(_dafny.Set([AlgorithmSuites.default__.GetESDKSuite(d_1810_id_)]))
            return _dafny.Set(coll9_)
        return iife83_()
        
    @_dafny.classproperty
    def DBEAlgorithmSuites(instance):
        def iife84_():
            coll10_ = _dafny.Set()
            compr_10_: software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId
            for compr_10_ in software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId.AllSingletonConstructors:
                d_1811_id_: software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId = compr_10_
                if True:
                    coll10_ = coll10_.union(_dafny.Set([AlgorithmSuites.default__.GetDBESuite(d_1811_id_)]))
            return _dafny.Set(coll10_)
        return iife84_()
        
    @_dafny.classproperty
    def aesPersistentKeyNames(instance):
        return _dafny.Seq([_dafny.Seq("aes-128"), _dafny.Seq("aes-192"), _dafny.Seq("aes-256")])
    @_dafny.classproperty
    def AllRawAES(instance):
        def iife85_():
            coll11_ = _dafny.Set()
            compr_11_: _dafny.Seq
            for compr_11_ in ((CompleteVectors.default__).aesPersistentKeyNames).Elements:
                d_1812_key_: _dafny.Seq = compr_11_
                if (d_1812_key_) in ((CompleteVectors.default__).aesPersistentKeyNames):
                    def iife86_(_pat_let37_0):
                        def iife87_(d_1813_keyDescription_):
                            return CompleteVectors.PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((_dafny.Seq("Generated RawAES ")) + (d_1812_key_), d_1813_keyDescription_, d_1813_keyDescription_)
                        return iife87_(_pat_let37_0)
                    coll11_ = coll11_.union(_dafny.Set([iife86_(JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("raw"))), (_dafny.Seq("encryption-algorithm"), JSON_mValues.JSON_String(_dafny.Seq("aes"))), (_dafny.Seq("provider-id"), JSON_mValues.JSON_String((_dafny.Seq("aws-raw-vectors-persistent-")) + (d_1812_key_))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1812_key_))])))]))
            return _dafny.Set(coll11_)
        return iife85_()
        
    @_dafny.classproperty
    def rsaPersistentKeyNamesWithoutPublicPrivate(instance):
        return _dafny.Seq([_dafny.Seq("rsa-4096")])
    @_dafny.classproperty
    def AllRawRSA(instance):
        def iife88_():
            coll12_ = _dafny.Set()
            compr_12_: _dafny.Seq
            for compr_12_ in ((CompleteVectors.default__).rsaPersistentKeyNamesWithoutPublicPrivate).Elements:
                d_1814_key_: _dafny.Seq = compr_12_
                compr_13_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme
                for compr_13_ in software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme.AllSingletonConstructors:
                    d_1815_padding_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme = compr_13_
                    if (d_1814_key_) in ((CompleteVectors.default__).rsaPersistentKeyNamesWithoutPublicPrivate):
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

                        def iife89_(_pat_let38_0):
                            def iife90_(d_1816_sharedOptions_):
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

                                return CompleteVectors.PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((((_dafny.Seq("Generated RawRSA ")) + (d_1814_key_)) + (_dafny.Seq(" "))) + (lambda121_(d_1815_padding_)), JSON_mValues.JSON_Object((d_1816_sharedOptions_) + (_dafny.Seq([(_dafny.Seq("key"), JSON_mValues.JSON_String((d_1814_key_) + (_dafny.Seq("-public"))))]))), JSON_mValues.JSON_Object((d_1816_sharedOptions_) + (_dafny.Seq([(_dafny.Seq("key"), JSON_mValues.JSON_String((d_1814_key_) + (_dafny.Seq("-private"))))]))))
                            return iife90_(_pat_let38_0)
                        coll12_ = coll12_.union(_dafny.Set([iife89_(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("raw"))), (_dafny.Seq("encryption-algorithm"), JSON_mValues.JSON_String(_dafny.Seq("rsa"))), (_dafny.Seq("provider-id"), JSON_mValues.JSON_String((_dafny.Seq("aws-raw-vectors-persistent-")) + (d_1814_key_))), (_dafny.Seq("padding-algorithm"), JSON_mValues.JSON_String(lambda119_(d_1815_padding_))), (_dafny.Seq("padding-hash"), JSON_mValues.JSON_String(lambda120_(d_1815_padding_)))]))]))
            return _dafny.Set(coll12_)
        return iife88_()
        
    @_dafny.classproperty
    def AllAwsKMSKeys(instance):
        return _dafny.Seq([_dafny.Seq("us-west-2-decryptable"), _dafny.Seq("us-west-2-mrk")])
    @_dafny.classproperty
    def AllKMSInfo(instance):
        def iife91_():
            coll13_ = _dafny.Set()
            compr_14_: _dafny.Seq
            for compr_14_ in ((CompleteVectors.default__).AllAwsKMSKeys).Elements:
                d_1817_key_: _dafny.Seq = compr_14_
                if (d_1817_key_) in ((CompleteVectors.default__).AllAwsKMSKeys):
                    def iife92_(_pat_let39_0):
                        def iife93_(d_1818_keyDescription_):
                            return CompleteVectors.PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((_dafny.Seq("Generated KMS ")) + (d_1817_key_), d_1818_keyDescription_, d_1818_keyDescription_)
                        return iife93_(_pat_let39_0)
                    coll13_ = coll13_.union(_dafny.Set([iife92_(JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1817_key_))])))]))
            return _dafny.Set(coll13_)
        return iife91_()
        
    @_dafny.classproperty
    def AllAwsKMSMrkKeys(instance):
        return _dafny.Seq([_dafny.Seq("us-west-2-mrk"), _dafny.Seq("us-east-1-mrk")])
    @_dafny.classproperty
    def AllKmsMrkAware(instance):
        def iife94_():
            coll14_ = _dafny.Set()
            compr_15_: _dafny.Seq
            for compr_15_ in ((CompleteVectors.default__).AllAwsKMSMrkKeys).Elements:
                d_1819_encryptKey_: _dafny.Seq = compr_15_
                compr_16_: _dafny.Seq
                for compr_16_ in ((CompleteVectors.default__).AllAwsKMSMrkKeys).Elements:
                    d_1820_decryptKey_: _dafny.Seq = compr_16_
                    if ((d_1819_encryptKey_) in ((CompleteVectors.default__).AllAwsKMSMrkKeys)) and ((d_1820_decryptKey_) in ((CompleteVectors.default__).AllAwsKMSMrkKeys)):
                        coll14_ = coll14_.union(_dafny.Set([CompleteVectors.PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((((_dafny.Seq("Generated KMS MRK ")) + (d_1819_encryptKey_)) + (_dafny.Seq("->"))) + (d_1820_decryptKey_), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-mrk-aware"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1819_encryptKey_))])), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-mrk-aware"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1820_decryptKey_))])))]))
            return _dafny.Set(coll14_)
        return iife94_()
        
    @_dafny.classproperty
    def AllDiscoveryFilters(instance):
        return _dafny.Set({Wrappers.Option_Some(software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter_DiscoveryFilter(_dafny.Seq([_dafny.Seq("658956600833")]), _dafny.Seq("aws"))), Wrappers.Option_None()})
    @_dafny.classproperty
    def AllKmsMrkAwareDiscovery(instance):
        def iife95_():
            coll15_ = _dafny.Set()
            compr_17_: _dafny.Seq
            for compr_17_ in ((CompleteVectors.default__).AllAwsKMSMrkKeys).Elements:
                d_1821_keyId_: _dafny.Seq = compr_17_
                compr_18_: Wrappers.Option
                for compr_18_ in ((CompleteVectors.default__).AllDiscoveryFilters).Elements:
                    d_1822_filter_: Wrappers.Option = compr_18_
                    if ((d_1821_keyId_) in ((CompleteVectors.default__).AllAwsKMSMrkKeys)) and ((d_1822_filter_) in ((CompleteVectors.default__).AllDiscoveryFilters)):
                        def lambda122_(d_1823_s_):
                            return JSON_mValues.JSON_String(d_1823_s_)

                        coll15_ = coll15_.union(_dafny.Set([CompleteVectors.PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((((_dafny.Seq("Discovery KMS MRK ")) + (d_1821_keyId_)) + (_dafny.Seq("->"))) + (((((_dafny.Seq("Filter ")) + (((d_1822_filter_).value).partition)) + (_dafny.Seq(" "))) + (Seq.default__.Flatten(((d_1822_filter_).value).accountIds)) if (d_1822_filter_).is_Some else _dafny.Seq("No Filter"))), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-mrk-aware"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1821_keyId_))])), (JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-mrk-aware-discovery"))), (_dafny.Seq("default-mrk-region"), JSON_mValues.JSON_String(_dafny.Seq("us-west-2"))), (_dafny.Seq("aws-kms-discovery-filter"), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("partition"), JSON_mValues.JSON_String(((d_1822_filter_).value).partition)), (_dafny.Seq("account-ids"), JSON_mValues.JSON_Array(Seq.default__.Map(lambda122_, ((d_1822_filter_).value).accountIds)))])))])) if (d_1822_filter_).is_Some else JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-mrk-aware-discovery"))), (_dafny.Seq("default-mrk-region"), JSON_mValues.JSON_String(_dafny.Seq("us-west-2")))]))))]))
            return _dafny.Set(coll15_)
        return iife95_()
        
    @_dafny.classproperty
    def AllHierarchy(instance):
        def iife96_():
            coll16_ = _dafny.Set()
            compr_19_: _dafny.Seq
            for compr_19_ in (_dafny.Seq([_dafny.Seq("static-branch-key-1")])).Elements:
                d_1824_keyId_: _dafny.Seq = compr_19_
                if (d_1824_keyId_) in (_dafny.Seq([_dafny.Seq("static-branch-key-1")])):
                    coll16_ = coll16_.union(_dafny.Set([CompleteVectors.PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((_dafny.Seq("Hierarchy KMS ")) + (d_1824_keyId_), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-hierarchy"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1824_keyId_))])), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-hierarchy"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1824_keyId_))])))]))
            return _dafny.Set(coll16_)
        return iife96_()
        
    @_dafny.classproperty
    def AllKmsRsaKeys(instance):
        return _dafny.Seq([_dafny.Seq("us-west-2-rsa-mrk")])
    @_dafny.classproperty
    def AllEncryptionAlgorithmSpec(instance):
        def iife97_():
            coll17_ = _dafny.Set()
            compr_20_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec
            for compr_20_ in software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec.AllSingletonConstructors:
                d_1825_e_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = compr_20_
                if not((d_1825_e_).is_SYMMETRIC__DEFAULT):
                    def lambda123_(source59_):
                        if source59_.is_RSAES__OAEP__SHA__1:
                            return _dafny.Seq("RSAES_OAEP_SHA_1")
                        elif True:
                            return _dafny.Seq("RSAES_OAEP_SHA_256")

                    coll17_ = coll17_.union(_dafny.Set([lambda123_(d_1825_e_)]))
            return _dafny.Set(coll17_)
        return iife97_()
        
    @_dafny.classproperty
    def KmsRsa(instance):
        return _dafny.Seq("KMS RSA ")
    @_dafny.classproperty
    def AllKmsRsa(instance):
        def iife98_():
            coll18_ = _dafny.Set()
            compr_21_: _dafny.Seq
            for compr_21_ in ((CompleteVectors.default__).AllKmsRsaKeys).Elements:
                d_1826_keyId_: _dafny.Seq = compr_21_
                compr_22_: _dafny.Seq
                for compr_22_ in ((CompleteVectors.default__).AllEncryptionAlgorithmSpec).Elements:
                    d_1827_algorithmSpec_: _dafny.Seq = compr_22_
                    if ((d_1826_keyId_) in ((CompleteVectors.default__).AllKmsRsaKeys)) and ((d_1827_algorithmSpec_) in ((CompleteVectors.default__).AllEncryptionAlgorithmSpec)):
                        coll18_ = coll18_.union(_dafny.Set([CompleteVectors.PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON(((CompleteVectors.default__).KmsRsa) + (d_1826_keyId_), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-rsa"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1826_keyId_)), (_dafny.Seq("encryption-algorithm"), JSON_mValues.JSON_String(d_1827_algorithmSpec_))])), JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("aws-kms-rsa"))), (_dafny.Seq("key"), JSON_mValues.JSON_String(d_1826_keyId_)), (_dafny.Seq("encryption-algorithm"), JSON_mValues.JSON_String(d_1827_algorithmSpec_))])))]))
            return _dafny.Set(coll18_)
        return iife98_()
        
    @_dafny.classproperty
    def AllPositiveKeyringTests(instance):
        def iife99_():
            coll19_ = _dafny.Set()
            compr_23_: CompleteVectors.PositiveKeyDescriptionJSON
            for compr_23_ in ((((((((CompleteVectors.default__).AllKMSInfo) | ((CompleteVectors.default__).AllKmsMrkAware)) | ((CompleteVectors.default__).AllKmsMrkAwareDiscovery)) | ((CompleteVectors.default__).AllRawAES)) | ((CompleteVectors.default__).AllRawRSA)) | ((CompleteVectors.default__).AllHierarchy)) | ((CompleteVectors.default__).AllKmsRsa)).Elements:
                d_1828_postiveKeyDescription_: CompleteVectors.PositiveKeyDescriptionJSON = compr_23_
                compr_24_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
                for compr_24_ in (((CompleteVectors.default__).ESDKAlgorithmSuites) | ((CompleteVectors.default__).DBEAlgorithmSuites)).Elements:
                    d_1829_algorithmSuite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo = compr_24_
                    if (((d_1828_postiveKeyDescription_) in ((((((((CompleteVectors.default__).AllKMSInfo) | ((CompleteVectors.default__).AllKmsMrkAware)) | ((CompleteVectors.default__).AllKmsMrkAwareDiscovery)) | ((CompleteVectors.default__).AllRawAES)) | ((CompleteVectors.default__).AllRawRSA)) | ((CompleteVectors.default__).AllHierarchy)) | ((CompleteVectors.default__).AllKmsRsa))) and ((d_1829_algorithmSuite_) in (((CompleteVectors.default__).ESDKAlgorithmSuites) | ((CompleteVectors.default__).DBEAlgorithmSuites)))) and (not(((_dafny.Seq(((d_1828_postiveKeyDescription_).description)[:len((CompleteVectors.default__).KmsRsa):])) == ((CompleteVectors.default__).KmsRsa)) and (((d_1829_algorithmSuite_).signature).is_ECDSA))):
                        def iife100_(_pat_let40_0):
                            def iife101_(d_1830_id_):
                                return JSON_mValues.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_mValues.JSON_String(_dafny.Seq("positive-keyring"))), (_dafny.Seq("description"), JSON_mValues.JSON_String((((d_1828_postiveKeyDescription_).description) + (_dafny.Seq(" "))) + (d_1830_id_))), (_dafny.Seq("algorithmSuiteId"), JSON_mValues.JSON_String(d_1830_id_)), (_dafny.Seq("encryptionContext"), JSON_mValues.JSON_Object(_dafny.Seq([]))), (_dafny.Seq("requiredEncryptionContextKeys"), JSON_mValues.JSON_Array(_dafny.Seq([]))), (_dafny.Seq("encryptKeyDescription"), (d_1828_postiveKeyDescription_).encrypt), (_dafny.Seq("decryptKeyDescription"), (d_1828_postiveKeyDescription_).decrypt)]))
                            return iife101_(_pat_let40_0)
                        coll19_ = coll19_.union(_dafny.Set([iife100_(HexStrings.default__.ToHexString((d_1829_algorithmSuite_).binaryId))]))
            return _dafny.Set(coll19_)
        return iife99_()
        
    @_dafny.classproperty
    def AwsPartitions(instance):
        return _dafny.Seq([_dafny.Seq("aws")])
    @_dafny.classproperty
    def AWSAccounts(instance):
        return _dafny.Seq([_dafny.Seq("658956600833")])

class PositiveKeyDescriptionJSON:
    @classmethod
    def default(cls, ):
        return lambda: PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON(_dafny.Seq({}), JSON_mValues.JSON_Null.default()(), JSON_mValues.JSON_Null.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PositiveKeyDescriptionJSON(self) -> bool:
        return isinstance(self, CompleteVectors.PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON)

class PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON(PositiveKeyDescriptionJSON, NamedTuple('PositiveKeyDescriptionJSON', [('description', Any), ('encrypt', Any), ('decrypt', Any)])):
    def __dafnystr__(self) -> str:
        return f'CompleteVectors.PositiveKeyDescriptionJSON.PositiveKeyDescriptionJSON({_dafny.string_of(self.description)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.decrypt)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CompleteVectors.PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON) and self.description == __o.description and self.encrypt == __o.encrypt and self.decrypt == __o.decrypt
    def __hash__(self) -> int:
        return super().__hash__()

