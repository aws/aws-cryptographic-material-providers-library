import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.Actions as Actions
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature
import aws_cryptography_primitives.internaldafny.generated.KdfCtr as KdfCtr
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption as RSAEncryption
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
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
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import Fixtures as Fixtures
import TestCreateKeyStore as TestCreateKeyStore
import TestDiscoveryGetKeys as TestDiscoveryGetKeys
import TestConfig as TestConfig
import TestGetKeys as TestGetKeys
import CleanupItems as CleanupItems
import TestCreateKeys as TestCreateKeys
import TestVersionKey as TestVersionKey
import TestUtils as TestUtils
import TestIntermediateKeyWrapping as TestIntermediateKeyWrapping
import TestErrorMessages as TestErrorMessages
import TestDefaultClientProvider as TestDefaultClientProvider
import TestRawAESKeyring as TestRawAESKeyring
import TestMultiKeyring as TestMultiKeyring
import TestRawRSAKeying as TestRawRSAKeying
import TestAwsKmsRsaKeyring as TestAwsKmsRsaKeyring
import TestAwsKmsHierarchicalKeyring as TestAwsKmsHierarchicalKeyring
import TestAwsKmsEncryptedDataKeyFilter as TestAwsKmsEncryptedDataKeyFilter
import TestLocalCMC as TestLocalCMC
import TestStormTracker as TestStormTracker
import standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import standard_library.internaldafny.generated.JSON_Values as JSON_Values
import standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import standard_library.internaldafny.generated.JSON_ZeroCopy_Serializer as JSON_ZeroCopy_Serializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Core as JSON_ZeroCopy_Deserializer_Core
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Strings as JSON_ZeroCopy_Deserializer_Strings
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Numbers as JSON_ZeroCopy_Deserializer_Numbers
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ObjectParams as JSON_ZeroCopy_Deserializer_ObjectParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Objects as JSON_ZeroCopy_Deserializer_Objects
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ArrayParams as JSON_ZeroCopy_Deserializer_ArrayParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Arrays as JSON_ZeroCopy_Deserializer_Arrays
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Constants as JSON_ZeroCopy_Deserializer_Constants
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Values as JSON_ZeroCopy_Deserializer_Values
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_API as JSON_ZeroCopy_Deserializer_API
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer as JSON_ZeroCopy_Deserializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_API as JSON_ZeroCopy_API
import standard_library.internaldafny.generated.JSON_API as JSON_API

# Module: module_

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Test____Main____(noArgsParameter__):
        d_1012_success_: bool
        d_1012_success_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeyStore.TestCreateKeyStore: ")))
        try:
            if True:
                TestCreateKeyStore.default__.TestCreateKeyStore()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1013_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1013_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDiscoveryGetKeys.TestGetBeaconKeyForTwoKmsArnsSuccess: ")))
        try:
            if True:
                TestDiscoveryGetKeys.default__.TestGetBeaconKeyForTwoKmsArnsSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1014_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1014_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDiscoveryGetKeys.TestGetActiveKeyForTwoKmsArnsSuccess: ")))
        try:
            if True:
                TestDiscoveryGetKeys.default__.TestGetActiveKeyForTwoKmsArnsSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1015_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1015_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDiscoveryGetKeys.TestGetBranchKeyVersionForTwoKmsArnsSuccess: ")))
        try:
            if True:
                TestDiscoveryGetKeys.default__.TestGetBranchKeyVersionForTwoKmsArnsSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1016_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1016_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDiscoveryGetKeys.TestGetKeysForMrk: ")))
        try:
            if True:
                TestDiscoveryGetKeys.default__.TestGetKeysForMrk()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1017_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1017_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestConfig.TestInvalidKmsKeyArnConfig: ")))
        try:
            if True:
                TestConfig.default__.TestInvalidKmsKeyArnConfig()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1018_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1018_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestConfig.TestInvalidKmsKeyArnAliasConfig: ")))
        try:
            if True:
                TestConfig.default__.TestInvalidKmsKeyArnAliasConfig()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1019_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1019_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestConfig.TestValidConfig: ")))
        try:
            if True:
                TestConfig.default__.TestValidConfig()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1020_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1020_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestConfig.TestValidConfigNoClients: ")))
        try:
            if True:
                TestConfig.default__.TestValidConfigNoClients()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1021_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1021_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetBeaconKey: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetBeaconKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1022_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1022_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKey: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1023_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1023_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveMrkKey: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveMrkKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1024_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1024_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetBranchKeyVersion: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetBranchKeyVersion()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1025_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1025_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKeyWithIncorrectKmsKeyArn: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKeyWithIncorrectKmsKeyArn()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1026_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1026_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKeyWrongLogicalKeyStoreName: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKeyWrongLogicalKeyStoreName()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1027_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1027_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKeyDoesNotExistFails: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKeyDoesNotExistFails()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1028_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1028_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKeyWithNoClients: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKeyWithNoClients()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1029_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1029_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.TestCreateBranchAndBeaconKeys: ")))
        try:
            if True:
                TestCreateKeys.default__.TestCreateBranchAndBeaconKeys()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1030_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1030_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.TestCreateOptions: ")))
        try:
            if True:
                TestCreateKeys.default__.TestCreateOptions()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1031_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1031_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.TestCreateDuplicate: ")))
        try:
            if True:
                TestCreateKeys.default__.TestCreateDuplicate()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1032_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1032_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.InsertingADuplicateWillFail: ")))
        try:
            if True:
                TestCreateKeys.default__.InsertingADuplicateWillFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1033_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1033_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.InsertingADuplicateWillWithADifferentVersionFail: ")))
        try:
            if True:
                TestCreateKeys.default__.InsertingADuplicateWillWithADifferentVersionFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1034_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1034_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.TestVersionKey: ")))
        try:
            if True:
                TestVersionKey.default__.TestVersionKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1035_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1035_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.TestVersionKeyWithEC: ")))
        try:
            if True:
                TestVersionKey.default__.TestVersionKeyWithEC()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1036_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1036_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.TestMrkVersionKey: ")))
        try:
            if True:
                TestVersionKey.default__.TestMrkVersionKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1037_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1037_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.InsertingADuplicateVersionWillFail: ")))
        try:
            if True:
                TestVersionKey.default__.InsertingADuplicateVersionWillFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1038_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1038_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.VersioningANonexistentBranchKeyWillFail: ")))
        try:
            if True:
                TestVersionKey.default__.VersioningANonexistentBranchKeyWillFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1039_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1039_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestIntermediateKeyWrapping.IntermediateWrapUnwrapTest: ")))
        try:
            if True:
                TestIntermediateKeyWrapping.default__.IntermediateWrapUnwrapTest()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1040_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1040_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestIntermediateKeyWrapping.IntermediateGenerateAndWrapUnwrapTest: ")))
        try:
            if True:
                TestIntermediateKeyWrapping.default__.IntermediateGenerateAndWrapUnwrapTest()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1041_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1041_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestErrorMessages.TestIncorrectRawDataKeys: ")))
        try:
            if True:
                TestErrorMessages.default__.TestIncorrectRawDataKeys()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1042_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1042_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestErrorMessages.TestIncorrectDataKeys: ")))
        try:
            if True:
                TestErrorMessages.default__.TestIncorrectDataKeys()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1043_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1043_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDefaultClientProvider.GetUsWestTwo: ")))
        try:
            if True:
                TestDefaultClientProvider.default__.GetUsWestTwo()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1044_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1044_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnEncryptOnDecryptGenerateDataKey: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnEncryptOnDecryptGenerateDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1045_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1045_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnEncryptOnDecryptSuppliedDataKey: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnEncryptOnDecryptSuppliedDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1046_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1046_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptKeyNameMismatch: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptKeyNameMismatch()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1047_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1047_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptBadAndGoodEdkSucceeds: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptBadAndGoodEdkSucceeds()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1048_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1048_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptNoEDKs: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptNoEDKs()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1049_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1049_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnEncryptUnserializableEC: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnEncryptUnserializableEC()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1050_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1050_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptUnserializableEC: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptUnserializableEC()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1051_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1051_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestHappyCase: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestHappyCase()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1052_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1052_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestChildKeyringFailureEncrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestChildKeyringFailureEncrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1053_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1053_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorKeyringFails: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorKeyringFails()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1054_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1054_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorKeyringDoesNotReturnPlaintextDataKey: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorKeyringDoesNotReturnPlaintextDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1055_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1055_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorAbleToDecrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorAbleToDecrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1056_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1056_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorUnableToDecrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorUnableToDecrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1057_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1057_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestCollectFailuresDecrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestCollectFailuresDecrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1058_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1058_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnEncryptOnDecryptSuppliedDataKey: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnEncryptOnDecryptSuppliedDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1059_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1059_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnDecryptKeyNameMismatch: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnDecryptKeyNameMismatch()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1060_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1060_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnDecryptFailure: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnDecryptFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1061_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1061_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnDecryptBadAndGoodEdkSucceeds: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnDecryptBadAndGoodEdkSucceeds()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1062_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1062_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsRsaKeyring.TestKmsRsaRoundtrip: ")))
        try:
            if True:
                TestAwsKmsRsaKeyring.default__.TestKmsRsaRoundtrip()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1063_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1063_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsRsaKeyring.TestKmsRsaWithAsymmetricSignatureFails: ")))
        try:
            if True:
                TestAwsKmsRsaKeyring.default__.TestKmsRsaWithAsymmetricSignatureFails()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1064_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1064_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsHierarchicalKeyring.TestHierarchyClientESDKSuite: ")))
        try:
            if True:
                TestAwsKmsHierarchicalKeyring.default__.TestHierarchyClientESDKSuite()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1065_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1065_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsHierarchicalKeyring.TestHierarchyClientDBESuite: ")))
        try:
            if True:
                TestAwsKmsHierarchicalKeyring.default__.TestHierarchyClientDBESuite()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1066_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1066_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsHierarchicalKeyring.TestBranchKeyIdSupplier: ")))
        try:
            if True:
                TestAwsKmsHierarchicalKeyring.default__.TestBranchKeyIdSupplier()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1067_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1067_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsHierarchicalKeyring.TestInvalidDataKeyError: ")))
        try:
            if True:
                TestAwsKmsHierarchicalKeyring.default__.TestInvalidDataKeyError()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1068_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1068_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEncryptedDataKeyFilter.TestFailsNonKeyResource: ")))
        try:
            if True:
                TestAwsKmsEncryptedDataKeyFilter.default__.TestFailsNonKeyResource()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1069_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1069_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEncryptedDataKeyFilter.TestMatchesKeyringsConfiguration: ")))
        try:
            if True:
                TestAwsKmsEncryptedDataKeyFilter.default__.TestMatchesKeyringsConfiguration()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1070_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1070_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestLocalCMC.LocalCMCBasics: ")))
        try:
            if True:
                TestLocalCMC.default__.LocalCMCBasics()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1071_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1071_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerBasics: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerBasics()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1072_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1072_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerFanOut: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerFanOut()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1073_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1073_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerTTL: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerTTL()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1074_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1074_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerGraceInterval: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerGraceInterval()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1075_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1075_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerGracePeriod: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerGracePeriod()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1076_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1076_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_1012_success_ = False
        if not(d_1012_success_):
            raise _dafny.HaltException("<stdin>(1,0): " + _dafny.string_of(_dafny.Seq("Test failures occurred: see above.\n")))

