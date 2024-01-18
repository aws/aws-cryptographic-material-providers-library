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
import Fixtures
import TestCreateKeyStore
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
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

# Module: module_

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Test____Main____(noArgsParameter__):
        d_781_success_: bool
        d_781_success_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeyStore.TestCreateKeyStore: ")))
        try:
            if True:
                TestCreateKeyStore.default__.TestCreateKeyStore()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_782_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_782_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestConfig.TestInvalidKmsKeyArnConfig: ")))
        try:
            if True:
                TestConfig.default__.TestInvalidKmsKeyArnConfig()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_783_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_783_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestConfig.TestValidConfig: ")))
        try:
            if True:
                TestConfig.default__.TestValidConfig()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_784_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_784_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestConfig.TestValidConfigNoClients: ")))
        try:
            if True:
                TestConfig.default__.TestValidConfigNoClients()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_785_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_785_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetBeaconKey: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetBeaconKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_786_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_786_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKey: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_787_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_787_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetBranchKeyVersion: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetBranchKeyVersion()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_788_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_788_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKeyWithIncorrectKmsKeyArn: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKeyWithIncorrectKmsKeyArn()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_789_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_789_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKeyWrongLogicalKeyStoreName: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKeyWrongLogicalKeyStoreName()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_790_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_790_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKeyWithNoClients: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKeyWithNoClients()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_791_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_791_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.TestCreateBranchAndBeaconKeys: ")))
        try:
            if True:
                TestCreateKeys.default__.TestCreateBranchAndBeaconKeys()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_792_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_792_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.TestCreateOptions: ")))
        try:
            if True:
                TestCreateKeys.default__.TestCreateOptions()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_793_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_793_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.TestCreateDuplicate: ")))
        try:
            if True:
                TestCreateKeys.default__.TestCreateDuplicate()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_794_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_794_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.InsertingADuplicateWillFail: ")))
        try:
            if True:
                TestCreateKeys.default__.InsertingADuplicateWillFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_795_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_795_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.InsertingADuplicateWillWithADifferentVersionFail: ")))
        try:
            if True:
                TestCreateKeys.default__.InsertingADuplicateWillWithADifferentVersionFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_796_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_796_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.TestVersionKey: ")))
        try:
            if True:
                TestVersionKey.default__.TestVersionKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_797_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_797_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.InsertingADuplicateVersionWillFail: ")))
        try:
            if True:
                TestVersionKey.default__.InsertingADuplicateVersionWillFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_798_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_798_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.VersioningANonexistentBranchKeyWillFail: ")))
        try:
            if True:
                TestVersionKey.default__.VersioningANonexistentBranchKeyWillFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_799_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_799_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestIntermediateKeyWrapping.IntermediateWrapUnwrapTest: ")))
        try:
            if True:
                TestIntermediateKeyWrapping.default__.IntermediateWrapUnwrapTest()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_800_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_800_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestIntermediateKeyWrapping.IntermediateGenerateAndWrapUnwrapTest: ")))
        try:
            if True:
                TestIntermediateKeyWrapping.default__.IntermediateGenerateAndWrapUnwrapTest()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_801_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_801_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDefaultClientProvider.GetUsWestTwo: ")))
        try:
            if True:
                TestDefaultClientProvider.default__.GetUsWestTwo()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_802_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_802_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnEncryptOnDecryptGenerateDataKey: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnEncryptOnDecryptGenerateDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_803_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_803_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnEncryptOnDecryptSuppliedDataKey: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnEncryptOnDecryptSuppliedDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_804_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_804_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptKeyNameMismatch: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptKeyNameMismatch()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_805_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_805_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptBadAndGoodEdkSucceeds: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptBadAndGoodEdkSucceeds()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_806_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_806_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptNoEDKs: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptNoEDKs()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_807_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_807_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnEncryptUnserializableEC: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnEncryptUnserializableEC()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_808_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_808_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptUnserializableEC: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptUnserializableEC()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_809_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_809_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestHappyCase: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestHappyCase()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_810_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_810_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestChildKeyringFailureEncrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestChildKeyringFailureEncrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_811_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_811_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorKeyringFails: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorKeyringFails()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_812_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_812_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorKeyringDoesNotReturnPlaintextDataKey: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorKeyringDoesNotReturnPlaintextDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_813_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_813_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorAbleToDecrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorAbleToDecrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_814_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_814_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorUnableToDecrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorUnableToDecrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_815_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_815_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestCollectFailuresDecrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestCollectFailuresDecrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_816_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_816_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnEncryptOnDecryptSuppliedDataKey: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnEncryptOnDecryptSuppliedDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_817_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_817_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnDecryptKeyNameMismatch: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnDecryptKeyNameMismatch()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_818_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_818_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnDecryptFailure: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnDecryptFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_819_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_819_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnDecryptBadAndGoodEdkSucceeds: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnDecryptBadAndGoodEdkSucceeds()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_820_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_820_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsRsaKeyring.TestKmsRsaRoundtrip: ")))
        try:
            if True:
                TestAwsKmsRsaKeyring.default__.TestKmsRsaRoundtrip()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_821_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_821_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsRsaKeyring.TestKmsRsaWithAsymmetricSignatureFails: ")))
        try:
            if True:
                TestAwsKmsRsaKeyring.default__.TestKmsRsaWithAsymmetricSignatureFails()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_822_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_822_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsHierarchicalKeyring.TestHierarchyClientESDKSuite: ")))
        try:
            if True:
                TestAwsKmsHierarchicalKeyring.default__.TestHierarchyClientESDKSuite()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_823_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_823_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsHierarchicalKeyring.TestHierarchyClientDBESuite: ")))
        try:
            if True:
                TestAwsKmsHierarchicalKeyring.default__.TestHierarchyClientDBESuite()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_824_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_824_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsHierarchicalKeyring.TestBranchKeyIdSupplier: ")))
        try:
            if True:
                TestAwsKmsHierarchicalKeyring.default__.TestBranchKeyIdSupplier()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_825_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_825_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEncryptedDataKeyFilter.TestFailsNonKeyResource: ")))
        try:
            if True:
                TestAwsKmsEncryptedDataKeyFilter.default__.TestFailsNonKeyResource()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_826_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_826_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEncryptedDataKeyFilter.TestMatchesKeyringsConfiguration: ")))
        try:
            if True:
                TestAwsKmsEncryptedDataKeyFilter.default__.TestMatchesKeyringsConfiguration()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_827_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_827_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestLocalCMC.LocalCMCBasics: ")))
        try:
            if True:
                TestLocalCMC.default__.LocalCMCBasics()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_828_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_828_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerBasics: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerBasics()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_829_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_829_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerFanOut: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerFanOut()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_830_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_830_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerTTL: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerTTL()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_831_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_831_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerGraceInterval: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerGraceInterval()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_832_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_832_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerGracePeriod: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerGracePeriod()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_833_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_833_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_781_success_ = False
        if not(d_781_success_):
            raise _dafny.HaltException("<stdin>(1,0): " + _dafny.string_of(_dafny.Seq("Test failures occurred: see above.\n")))

