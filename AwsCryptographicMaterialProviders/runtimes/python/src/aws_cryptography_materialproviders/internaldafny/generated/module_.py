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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
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
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
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
import TestUtils
import TestIntermediateKeyWrapping
import TestDefaultClientProvider
import TestRawAESKeyring
import TestMultiKeyring
import TestRawRSAKeying
import TestAwsKmsRsaKeyring
import TestAwsKmsHierarchicalKeyring
import TestAwsKmsEncryptedDataKeyFilter
import TestLocalCMC
import TestStormTracker
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

assert "module_" == __name__
module_ = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Test____Main____(noArgsParameter__):
        d_2202_success_: bool
        d_2202_success_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeyStore.TestCreateKeyStore: ")))
        try:
            if True:
                TestCreateKeyStore.default__.TestCreateKeyStore()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2203_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2203_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestConfig.TestInvalidKmsKeyArnConfig: ")))
        try:
            if True:
                TestConfig.default__.TestInvalidKmsKeyArnConfig()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2204_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2204_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestConfig.TestValidConfig: ")))
        try:
            if True:
                TestConfig.default__.TestValidConfig()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2205_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2205_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestConfig.TestValidConfigNoClients: ")))
        try:
            if True:
                TestConfig.default__.TestValidConfigNoClients()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2206_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2206_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetBeaconKey: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetBeaconKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2207_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2207_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKey: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2208_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2208_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetBranchKeyVersion: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetBranchKeyVersion()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2209_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2209_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKeyWithIncorrectKmsKeyArn: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKeyWithIncorrectKmsKeyArn()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2210_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2210_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKeyWrongLogicalKeyStoreName: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKeyWrongLogicalKeyStoreName()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2211_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2211_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKeyWithNoClients: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKeyWithNoClients()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2212_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2212_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.TestCreateBranchAndBeaconKeys: ")))
        try:
            if True:
                TestCreateKeys.default__.TestCreateBranchAndBeaconKeys()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2213_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2213_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.TestCreateOptions: ")))
        try:
            if True:
                TestCreateKeys.default__.TestCreateOptions()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2214_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2214_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.TestCreateDuplicate: ")))
        try:
            if True:
                TestCreateKeys.default__.TestCreateDuplicate()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2215_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2215_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.InsertingADuplicateWillFail: ")))
        try:
            if True:
                TestCreateKeys.default__.InsertingADuplicateWillFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2216_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2216_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.InsertingADuplicateWillWithADifferentVersionFail: ")))
        try:
            if True:
                TestCreateKeys.default__.InsertingADuplicateWillWithADifferentVersionFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2217_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2217_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.TestVersionKey: ")))
        try:
            if True:
                TestVersionKey.default__.TestVersionKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2218_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2218_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.InsertingADuplicateVersionWillFail: ")))
        try:
            if True:
                TestVersionKey.default__.InsertingADuplicateVersionWillFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2219_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2219_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.VersioningANonexistentBranchKeyWillFail: ")))
        try:
            if True:
                TestVersionKey.default__.VersioningANonexistentBranchKeyWillFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2220_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2220_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestIntermediateKeyWrapping.IntermediateWrapUnwrapTest: ")))
        try:
            if True:
                TestIntermediateKeyWrapping.default__.IntermediateWrapUnwrapTest()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2221_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2221_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestIntermediateKeyWrapping.IntermediateGenerateAndWrapUnwrapTest: ")))
        try:
            if True:
                TestIntermediateKeyWrapping.default__.IntermediateGenerateAndWrapUnwrapTest()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2222_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2222_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDefaultClientProvider.GetUsWestTwo: ")))
        try:
            if True:
                TestDefaultClientProvider.default__.GetUsWestTwo()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2223_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2223_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnEncryptOnDecryptGenerateDataKey: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnEncryptOnDecryptGenerateDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2224_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2224_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnEncryptOnDecryptSuppliedDataKey: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnEncryptOnDecryptSuppliedDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2225_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2225_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptKeyNameMismatch: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptKeyNameMismatch()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2226_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2226_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptBadAndGoodEdkSucceeds: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptBadAndGoodEdkSucceeds()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2227_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2227_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptNoEDKs: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptNoEDKs()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2228_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2228_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnEncryptUnserializableEC: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnEncryptUnserializableEC()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2229_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2229_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptUnserializableEC: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptUnserializableEC()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2230_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2230_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestHappyCase: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestHappyCase()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2231_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2231_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestChildKeyringFailureEncrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestChildKeyringFailureEncrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2232_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2232_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorKeyringFails: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorKeyringFails()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2233_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2233_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorKeyringDoesNotReturnPlaintextDataKey: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorKeyringDoesNotReturnPlaintextDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2234_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2234_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorAbleToDecrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorAbleToDecrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2235_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2235_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorUnableToDecrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorUnableToDecrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2236_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2236_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestCollectFailuresDecrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestCollectFailuresDecrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2237_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2237_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnEncryptOnDecryptSuppliedDataKey: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnEncryptOnDecryptSuppliedDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2238_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2238_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnDecryptKeyNameMismatch: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnDecryptKeyNameMismatch()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2239_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2239_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnDecryptFailure: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnDecryptFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2240_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2240_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnDecryptBadAndGoodEdkSucceeds: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnDecryptBadAndGoodEdkSucceeds()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2241_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2241_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsRsaKeyring.TestKmsRsaRoundtrip: ")))
        try:
            if True:
                TestAwsKmsRsaKeyring.default__.TestKmsRsaRoundtrip()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2242_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2242_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsRsaKeyring.TestKmsRsaWithAsymmetricSignatureFails: ")))
        try:
            if True:
                TestAwsKmsRsaKeyring.default__.TestKmsRsaWithAsymmetricSignatureFails()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2243_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2243_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsHierarchicalKeyring.TestHierarchyClientESDKSuite: ")))
        try:
            if True:
                TestAwsKmsHierarchicalKeyring.default__.TestHierarchyClientESDKSuite()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2244_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2244_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsHierarchicalKeyring.TestHierarchyClientDBESuite: ")))
        try:
            if True:
                TestAwsKmsHierarchicalKeyring.default__.TestHierarchyClientDBESuite()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2245_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2245_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsHierarchicalKeyring.TestBranchKeyIdSupplier: ")))
        try:
            if True:
                TestAwsKmsHierarchicalKeyring.default__.TestBranchKeyIdSupplier()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2246_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2246_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEncryptedDataKeyFilter.TestFailsNonKeyResource: ")))
        try:
            if True:
                TestAwsKmsEncryptedDataKeyFilter.default__.TestFailsNonKeyResource()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2247_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2247_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEncryptedDataKeyFilter.TestMatchesKeyringsConfiguration: ")))
        try:
            if True:
                TestAwsKmsEncryptedDataKeyFilter.default__.TestMatchesKeyringsConfiguration()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2248_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2248_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestLocalCMC.LocalCMCBasics: ")))
        try:
            if True:
                TestLocalCMC.default__.LocalCMCBasics()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2249_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2249_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerBasics: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerBasics()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2250_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2250_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerFanOut: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerFanOut()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2251_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2251_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerTTL: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerTTL()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2252_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2252_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerGraceInterval: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerGraceInterval()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2253_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2253_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerGracePeriod: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerGracePeriod()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2254_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2254_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_2202_success_ = False
        if not(d_2202_success_):
            raise _dafny.HaltException("<stdin>(1,0): " + _dafny.string_of(_dafny.Seq("Test failures occurred: see above.\n")))

