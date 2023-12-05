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
        source18_ = (algorithmSuite).id
        if source18_.is_ESDK:
            d_565___mcc_h0_ = source18_.ESDK
            if ((algorithmSuite).commitment).is_None:
                return software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT())
            elif True:
                return software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT())
        elif True:
            d_566___mcc_h1_ = source18_.DBE
            return software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT())

    @staticmethod
    def WriteStuff():
        d_567_tests_: _dafny.Seq
        d_567_tests_ = SortedSets.default__.SetToSequence(default__.AllPositiveKeyringTests)
        d_568_testsJSON_: _dafny.Seq
        d_568_testsJSON_ = _dafny.Seq([])
        hi6_ = len(d_567_tests_)
        for d_569_i_ in range(0, hi6_):
            d_570_name_: _dafny.Seq
            d_571_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out78_: Wrappers.Result
            out78_ = UUID.default__.GenerateUUID()
            d_571_valueOrError0_ = out78_
            if not(not((d_571_valueOrError0_).IsFailure())):
                raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CompleteVectors.dfy(281,15): " + _dafny.string_of(d_571_valueOrError0_))
            d_570_name_ = (d_571_valueOrError0_).Extract()
            d_568_testsJSON_ = (d_568_testsJSON_) + (_dafny.Seq([(d_570_name_, (d_567_tests_)[d_569_i_])]))
        d_572_mplEncryptManifies_: JSON_Values.JSON
        d_572_mplEncryptManifies_ = JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("tests"), JSON_Values.JSON_Object(d_568_testsJSON_))]))
        d_573_mplEncryptManifiesBytes_: _dafny.Seq
        d_574_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_574_valueOrError1_ = JSON_API.default__.Serialize(d_572_mplEncryptManifies_)
        if not(not((d_574_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CompleteVectors.dfy(290,32): " + _dafny.string_of(d_574_valueOrError1_))
        d_573_mplEncryptManifiesBytes_ = (d_574_valueOrError1_).Extract()
        d_575_mplEncryptManifiesBv_: _dafny.Seq
        d_575_mplEncryptManifiesBv_ = JSONHelpers.default__.BytesBv(d_573_mplEncryptManifiesBytes_)
        d_576___v3_: tuple
        d_577_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out79_: Wrappers.Result
        out79_ = FileIO.default__.WriteBytesToFile(_dafny.Seq("dafny/TestVectorsAwsCryptographicMaterialProviders/test/test.json"), d_575_mplEncryptManifiesBv_)
        d_577_valueOrError2_ = out79_
        if not(not((d_577_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CompleteVectors.dfy(293,10): " + _dafny.string_of(d_577_valueOrError2_))
        d_576___v3_ = (d_577_valueOrError2_).Extract()

    @_dafny.classproperty
    def ESDKAlgorithmSuites(instance):
        def iife11_():
            coll5_ = _dafny.Set()
            compr_5_: software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId
            for compr_5_ in software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId.AllSingletonConstructors:
                d_578_id_: software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId = compr_5_
                if True:
                    coll5_ = coll5_.union(_dafny.Set([AlgorithmSuites.default__.GetESDKSuite(d_578_id_)]))
            return _dafny.Set(coll5_)
        return iife11_()
        
    @_dafny.classproperty
    def DBEAlgorithmSuites(instance):
        def iife12_():
            coll6_ = _dafny.Set()
            compr_6_: software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId
            for compr_6_ in software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId.AllSingletonConstructors:
                d_579_id_: software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId = compr_6_
                if True:
                    coll6_ = coll6_.union(_dafny.Set([AlgorithmSuites.default__.GetDBESuite(d_579_id_)]))
            return _dafny.Set(coll6_)
        return iife12_()
        
    @_dafny.classproperty
    def aesPersistentKeyNames(instance):
        return _dafny.Seq([_dafny.Seq("aes-128"), _dafny.Seq("aes-192"), _dafny.Seq("aes-256")])
    @_dafny.classproperty
    def AllRawAES(instance):
        def iife13_():
            coll7_ = _dafny.Set()
            compr_7_: _dafny.Seq
            for compr_7_ in (default__.aesPersistentKeyNames).Elements:
                d_580_key_: _dafny.Seq = compr_7_
                if (d_580_key_) in (default__.aesPersistentKeyNames):
                    def iife14_(_pat_let3_0):
                        def iife15_(d_581_keyDescription_):
                            return PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((_dafny.Seq("Generated RawAES ")) + (d_580_key_), d_581_keyDescription_, d_581_keyDescription_)
                        return iife15_(_pat_let3_0)
                    coll7_ = coll7_.union(_dafny.Set([iife14_(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("raw"))), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(_dafny.Seq("aes"))), (_dafny.Seq("provider-id"), JSON_Values.JSON_String((_dafny.Seq("aws-raw-vectors-persistent-")) + (d_580_key_))), (_dafny.Seq("key"), JSON_Values.JSON_String(d_580_key_))])))]))
            return _dafny.Set(coll7_)
        return iife13_()
        
    @_dafny.classproperty
    def rsaPersistentKeyNamesWithoutPublicPrivate(instance):
        return _dafny.Seq([_dafny.Seq("rsa-4096")])
    @_dafny.classproperty
    def AllRawRSA(instance):
        def iife16_():
            coll8_ = _dafny.Set()
            compr_8_: _dafny.Seq
            for compr_8_ in (default__.rsaPersistentKeyNamesWithoutPublicPrivate).Elements:
                d_582_key_: _dafny.Seq = compr_8_
                compr_9_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme
                for compr_9_ in software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme.AllSingletonConstructors:
                    d_583_padding_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme = compr_9_
                    if (d_582_key_) in (default__.rsaPersistentKeyNamesWithoutPublicPrivate):
                        def lambda37_(source19_):
                            if source19_.is_PKCS1:
                                return _dafny.Seq("pkcs1")
                            elif source19_.is_OAEP__SHA1__MGF1:
                                return _dafny.Seq("oaep-mgf1")
                            elif source19_.is_OAEP__SHA256__MGF1:
                                return _dafny.Seq("oaep-mgf1")
                            elif source19_.is_OAEP__SHA384__MGF1:
                                return _dafny.Seq("oaep-mgf1")
                            elif True:
                                return _dafny.Seq("oaep-mgf1")

                        def lambda38_(source20_):
                            if source20_.is_PKCS1:
                                return _dafny.Seq("sha1")
                            elif source20_.is_OAEP__SHA1__MGF1:
                                return _dafny.Seq("sha1")
                            elif source20_.is_OAEP__SHA256__MGF1:
                                return _dafny.Seq("sha256")
                            elif source20_.is_OAEP__SHA384__MGF1:
                                return _dafny.Seq("sha384")
                            elif True:
                                return _dafny.Seq("sha512")

                        def iife17_(_pat_let4_0):
                            def iife18_(d_584_sharedOptions_):
                                def lambda39_(source21_):
                                    if source21_.is_PKCS1:
                                        return _dafny.Seq("pkcs1-sha1")
                                    elif source21_.is_OAEP__SHA1__MGF1:
                                        return _dafny.Seq("oaep-mgf1-sha1")
                                    elif source21_.is_OAEP__SHA256__MGF1:
                                        return _dafny.Seq("oaep-mgf1-sha256")
                                    elif source21_.is_OAEP__SHA384__MGF1:
                                        return _dafny.Seq("oaep-mgf1-sha384")
                                    elif True:
                                        return _dafny.Seq("oaep-mgf1-sha512")

                                return PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((((_dafny.Seq("Generated RawRSA ")) + (d_582_key_)) + (_dafny.Seq(" "))) + (lambda39_(d_583_padding_)), JSON_Values.JSON_Object((d_584_sharedOptions_) + (_dafny.Seq([(_dafny.Seq("key"), JSON_Values.JSON_String((d_582_key_) + (_dafny.Seq("-public"))))]))), JSON_Values.JSON_Object((d_584_sharedOptions_) + (_dafny.Seq([(_dafny.Seq("key"), JSON_Values.JSON_String((d_582_key_) + (_dafny.Seq("-private"))))]))))
                            return iife18_(_pat_let4_0)
                        coll8_ = coll8_.union(_dafny.Set([iife17_(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("raw"))), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(_dafny.Seq("rsa"))), (_dafny.Seq("provider-id"), JSON_Values.JSON_String((_dafny.Seq("aws-raw-vectors-persistent-")) + (d_582_key_))), (_dafny.Seq("padding-algorithm"), JSON_Values.JSON_String(lambda37_(d_583_padding_))), (_dafny.Seq("padding-hash"), JSON_Values.JSON_String(lambda38_(d_583_padding_)))]))]))
            return _dafny.Set(coll8_)
        return iife16_()
        
    @_dafny.classproperty
    def AllAwsKMSKeys(instance):
        return _dafny.Seq([_dafny.Seq("us-west-2-decryptable"), _dafny.Seq("us-west-2-mrk")])
    @_dafny.classproperty
    def AllKMSInfo(instance):
        def iife19_():
            coll9_ = _dafny.Set()
            compr_10_: _dafny.Seq
            for compr_10_ in (default__.AllAwsKMSKeys).Elements:
                d_585_key_: _dafny.Seq = compr_10_
                if (d_585_key_) in (default__.AllAwsKMSKeys):
                    def iife20_(_pat_let5_0):
                        def iife21_(d_586_keyDescription_):
                            return PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((_dafny.Seq("Generated KMS ")) + (d_585_key_), d_586_keyDescription_, d_586_keyDescription_)
                        return iife21_(_pat_let5_0)
                    coll9_ = coll9_.union(_dafny.Set([iife20_(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms"))), (_dafny.Seq("key"), JSON_Values.JSON_String(d_585_key_))])))]))
            return _dafny.Set(coll9_)
        return iife19_()
        
    @_dafny.classproperty
    def AllAwsKMSMrkKeys(instance):
        return _dafny.Seq([_dafny.Seq("us-west-2-mrk"), _dafny.Seq("us-east-1-mrk")])
    @_dafny.classproperty
    def AllKmsMrkAware(instance):
        def iife22_():
            coll10_ = _dafny.Set()
            compr_11_: _dafny.Seq
            for compr_11_ in (default__.AllAwsKMSMrkKeys).Elements:
                d_587_encryptKey_: _dafny.Seq = compr_11_
                compr_12_: _dafny.Seq
                for compr_12_ in (default__.AllAwsKMSMrkKeys).Elements:
                    d_588_decryptKey_: _dafny.Seq = compr_12_
                    if ((d_587_encryptKey_) in (default__.AllAwsKMSMrkKeys)) and ((d_588_decryptKey_) in (default__.AllAwsKMSMrkKeys)):
                        coll10_ = coll10_.union(_dafny.Set([PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((((_dafny.Seq("Generated KMS MRK ")) + (d_587_encryptKey_)) + (_dafny.Seq("->"))) + (d_588_decryptKey_), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-mrk-aware"))), (_dafny.Seq("key"), JSON_Values.JSON_String(d_587_encryptKey_))])), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-mrk-aware"))), (_dafny.Seq("key"), JSON_Values.JSON_String(d_588_decryptKey_))])))]))
            return _dafny.Set(coll10_)
        return iife22_()
        
    @_dafny.classproperty
    def AllDiscoveryFilters(instance):
        return _dafny.Set({Wrappers.Option_Some(software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter_DiscoveryFilter(_dafny.Seq([_dafny.Seq("658956600833")]), _dafny.Seq("aws"))), Wrappers.Option_None()})
    @_dafny.classproperty
    def AllKmsMrkAwareDiscovery(instance):
        def iife23_():
            coll11_ = _dafny.Set()
            compr_13_: _dafny.Seq
            for compr_13_ in (default__.AllAwsKMSMrkKeys).Elements:
                d_589_keyId_: _dafny.Seq = compr_13_
                compr_14_: Wrappers.Option
                for compr_14_ in (default__.AllDiscoveryFilters).Elements:
                    d_590_filter_: Wrappers.Option = compr_14_
                    if ((d_589_keyId_) in (default__.AllAwsKMSMrkKeys)) and ((d_590_filter_) in (default__.AllDiscoveryFilters)):
                        def lambda40_(d_591_s_):
                            return JSON_Values.JSON_String(d_591_s_)

                        coll11_ = coll11_.union(_dafny.Set([PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((((_dafny.Seq("Discovery KMS MRK ")) + (d_589_keyId_)) + (_dafny.Seq("->"))) + (((((_dafny.Seq("Filter ")) + (((d_590_filter_).value).partition)) + (_dafny.Seq(" "))) + (Seq.default__.Flatten(((d_590_filter_).value).accountIds)) if (d_590_filter_).is_Some else _dafny.Seq("No Filter"))), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-mrk-aware"))), (_dafny.Seq("key"), JSON_Values.JSON_String(d_589_keyId_))])), (JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-mrk-aware-discovery"))), (_dafny.Seq("default-mrk-region"), JSON_Values.JSON_String(_dafny.Seq("us-west-2"))), (_dafny.Seq("aws-kms-discovery-filter"), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("partition"), JSON_Values.JSON_String(((d_590_filter_).value).partition)), (_dafny.Seq("account-ids"), JSON_Values.JSON_Array(Seq.default__.Map(lambda40_, ((d_590_filter_).value).accountIds)))])))])) if (d_590_filter_).is_Some else JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-mrk-aware-discovery"))), (_dafny.Seq("default-mrk-region"), JSON_Values.JSON_String(_dafny.Seq("us-west-2")))]))))]))
            return _dafny.Set(coll11_)
        return iife23_()
        
    @_dafny.classproperty
    def AllHierarchy(instance):
        def iife24_():
            coll12_ = _dafny.Set()
            compr_15_: _dafny.Seq
            for compr_15_ in (_dafny.Seq([_dafny.Seq("static-branch-key-1")])).Elements:
                d_592_keyId_: _dafny.Seq = compr_15_
                if (d_592_keyId_) in (_dafny.Seq([_dafny.Seq("static-branch-key-1")])):
                    coll12_ = coll12_.union(_dafny.Set([PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((_dafny.Seq("Hierarchy KMS ")) + (d_592_keyId_), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-hierarchy"))), (_dafny.Seq("key"), JSON_Values.JSON_String(d_592_keyId_))])), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-hierarchy"))), (_dafny.Seq("key"), JSON_Values.JSON_String(d_592_keyId_))])))]))
            return _dafny.Set(coll12_)
        return iife24_()
        
    @_dafny.classproperty
    def AllKmsRsaKeys(instance):
        return _dafny.Seq([_dafny.Seq("us-west-2-rsa-mrk")])
    @_dafny.classproperty
    def AllEncryptionAlgorithmSpec(instance):
        def iife25_():
            coll13_ = _dafny.Set()
            compr_16_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec
            for compr_16_ in software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec.AllSingletonConstructors:
                d_593_e_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = compr_16_
                if not((d_593_e_).is_SYMMETRIC__DEFAULT):
                    def lambda41_(source22_):
                        if source22_.is_RSAES__OAEP__SHA__1:
                            return _dafny.Seq("RSAES_OAEP_SHA_1")
                        elif True:
                            return _dafny.Seq("RSAES_OAEP_SHA_256")

                    coll13_ = coll13_.union(_dafny.Set([lambda41_(d_593_e_)]))
            return _dafny.Set(coll13_)
        return iife25_()
        
    @_dafny.classproperty
    def KmsRsa(instance):
        return _dafny.Seq("KMS RSA ")
    @_dafny.classproperty
    def AllKmsRsa(instance):
        def iife26_():
            coll14_ = _dafny.Set()
            compr_17_: _dafny.Seq
            for compr_17_ in (default__.AllKmsRsaKeys).Elements:
                d_594_keyId_: _dafny.Seq = compr_17_
                compr_18_: _dafny.Seq
                for compr_18_ in (default__.AllEncryptionAlgorithmSpec).Elements:
                    d_595_algorithmSpec_: _dafny.Seq = compr_18_
                    if ((d_594_keyId_) in (default__.AllKmsRsaKeys)) and ((d_595_algorithmSpec_) in (default__.AllEncryptionAlgorithmSpec)):
                        coll14_ = coll14_.union(_dafny.Set([PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON((default__.KmsRsa) + (d_594_keyId_), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-rsa"))), (_dafny.Seq("key"), JSON_Values.JSON_String(d_594_keyId_)), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(d_595_algorithmSpec_))])), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-rsa"))), (_dafny.Seq("key"), JSON_Values.JSON_String(d_594_keyId_)), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(d_595_algorithmSpec_))])))]))
            return _dafny.Set(coll14_)
        return iife26_()
        
    @_dafny.classproperty
    def AllPositiveKeyringTests(instance):
        def iife27_():
            coll15_ = _dafny.Set()
            compr_19_: PositiveKeyDescriptionJSON
            for compr_19_ in (((((((default__.AllKMSInfo) | (default__.AllKmsMrkAware)) | (default__.AllKmsMrkAwareDiscovery)) | (default__.AllRawAES)) | (default__.AllRawRSA)) | (default__.AllHierarchy)) | (default__.AllKmsRsa)).Elements:
                d_596_postiveKeyDescription_: PositiveKeyDescriptionJSON = compr_19_
                compr_20_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
                for compr_20_ in ((default__.ESDKAlgorithmSuites) | (default__.DBEAlgorithmSuites)).Elements:
                    d_597_algorithmSuite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo = compr_20_
                    if (((d_596_postiveKeyDescription_) in (((((((default__.AllKMSInfo) | (default__.AllKmsMrkAware)) | (default__.AllKmsMrkAwareDiscovery)) | (default__.AllRawAES)) | (default__.AllRawRSA)) | (default__.AllHierarchy)) | (default__.AllKmsRsa))) and ((d_597_algorithmSuite_) in ((default__.ESDKAlgorithmSuites) | (default__.DBEAlgorithmSuites)))) and (not(((_dafny.Seq(((d_596_postiveKeyDescription_).description)[:len(default__.KmsRsa):])) == (default__.KmsRsa)) and (((d_597_algorithmSuite_).signature).is_ECDSA))):
                        def iife28_(_pat_let6_0):
                            def iife29_(d_598_id_):
                                return JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("positive-keyring"))), (_dafny.Seq("description"), JSON_Values.JSON_String((((d_596_postiveKeyDescription_).description) + (_dafny.Seq(" "))) + (d_598_id_))), (_dafny.Seq("algorithmSuiteId"), JSON_Values.JSON_String(d_598_id_)), (_dafny.Seq("encryptionContext"), JSON_Values.JSON_Object(_dafny.Seq([]))), (_dafny.Seq("requiredEncryptionContextKeys"), JSON_Values.JSON_Array(_dafny.Seq([]))), (_dafny.Seq("encryptKeyDescription"), (d_596_postiveKeyDescription_).encrypt), (_dafny.Seq("decryptKeyDescription"), (d_596_postiveKeyDescription_).decrypt)]))
                            return iife29_(_pat_let6_0)
                        coll15_ = coll15_.union(_dafny.Set([iife28_(HexStrings.default__.ToHexString((d_597_algorithmSuite_).binaryId))]))
            return _dafny.Set(coll15_)
        return iife27_()
        
    @_dafny.classproperty
    def AwsPartitions(instance):
        return _dafny.Seq([_dafny.Seq("aws")])
    @_dafny.classproperty
    def AWSAccounts(instance):
        return _dafny.Seq([_dafny.Seq("658956600833")])

class PositiveKeyDescriptionJSON:
    @classmethod
    def default(cls, ):
        return lambda: PositiveKeyDescriptionJSON_PositiveKeyDescriptionJSON(_dafny.Seq({}), JSON_Values.JSON.default()(), JSON_Values.JSON.default()())
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

