import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_material_providers.internaldafny.generated.GetKeys as GetKeys
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_material_providers.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_material_providers.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_material_providers.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_material_providers.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_material_providers.internaldafny.generated.CMM as CMM
import aws_cryptographic_material_providers.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_material_providers.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_material_providers.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_material_providers.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_material_providers.internaldafny.generated.Utils as Utils
import aws_cryptographic_material_providers.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_material_providers.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import Fixtures as Fixtures
import TestCreateKeyStore as TestCreateKeyStore
import TestLyingBranchKey as TestLyingBranchKey
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
import TestRawECDHKeyring as TestRawECDHKeyring
import TestRawAESKeyring as TestRawAESKeyring
import TestMultiKeyring as TestMultiKeyring
import TestRawRSAKeying as TestRawRSAKeying
import TestAwsKmsRsaKeyring as TestAwsKmsRsaKeyring
import TestAwsKmsHierarchicalKeyring as TestAwsKmsHierarchicalKeyring
import TestAwsKmsEcdhKeyring as TestAwsKmsEcdhKeyring
import TestAwsKmsEncryptedDataKeyFilter as TestAwsKmsEncryptedDataKeyFilter
import TestLocalCMC as TestLocalCMC
import TestStormTracker as TestStormTracker
import TestEcdhCalculation as TestEcdhCalculation
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Values as JSON_Values
import smithy_dafny_standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import smithy_dafny_standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import smithy_dafny_standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import smithy_dafny_standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Serializer as JSON_ZeroCopy_Serializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Core as JSON_ZeroCopy_Deserializer_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Strings as JSON_ZeroCopy_Deserializer_Strings
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Numbers as JSON_ZeroCopy_Deserializer_Numbers
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ObjectParams as JSON_ZeroCopy_Deserializer_ObjectParams
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Objects as JSON_ZeroCopy_Deserializer_Objects
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ArrayParams as JSON_ZeroCopy_Deserializer_ArrayParams
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Arrays as JSON_ZeroCopy_Deserializer_Arrays
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Constants as JSON_ZeroCopy_Deserializer_Constants
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Values as JSON_ZeroCopy_Deserializer_Values
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_API as JSON_ZeroCopy_Deserializer_API
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer as JSON_ZeroCopy_Deserializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_API as JSON_ZeroCopy_API
import smithy_dafny_standard_library.internaldafny.generated.JSON_API as JSON_API

# Module: module_

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Test____Main____(noArgsParameter__):
        d_0_success_: bool
        d_0_success_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeyStore.TestCreateKeyStore: ")))
        try:
            if True:
                TestCreateKeyStore.default__.TestCreateKeyStore()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_1_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_1_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestLyingBranchKey.TestGetActiveKeyForLyingBranchKey: ")))
        try:
            if True:
                TestLyingBranchKey.default__.TestGetActiveKeyForLyingBranchKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_2_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_2_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestLyingBranchKey.TestGetBranchKeyVersionForLyingBranchKey: ")))
        try:
            if True:
                TestLyingBranchKey.default__.TestGetBranchKeyVersionForLyingBranchKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_3_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_3_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestLyingBranchKey.TestGetBeaconKeyForLyingBranchKey: ")))
        try:
            if True:
                TestLyingBranchKey.default__.TestGetBeaconKeyForLyingBranchKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_4_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_4_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestLyingBranchKey.TestVersionKeyForLyingBranchKey: ")))
        try:
            if True:
                TestLyingBranchKey.default__.TestVersionKeyForLyingBranchKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_5_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_5_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDiscoveryGetKeys.TestGetBeaconKeyForTwoKmsArnsSuccess: ")))
        try:
            if True:
                TestDiscoveryGetKeys.default__.TestGetBeaconKeyForTwoKmsArnsSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_6_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_6_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDiscoveryGetKeys.TestGetActiveKeyForTwoKmsArnsSuccess: ")))
        try:
            if True:
                TestDiscoveryGetKeys.default__.TestGetActiveKeyForTwoKmsArnsSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_7_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_7_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDiscoveryGetKeys.TestGetBranchKeyVersionForTwoKmsArnsSuccess: ")))
        try:
            if True:
                TestDiscoveryGetKeys.default__.TestGetBranchKeyVersionForTwoKmsArnsSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_8_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_8_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDiscoveryGetKeys.TestGetKeysForMrk: ")))
        try:
            if True:
                TestDiscoveryGetKeys.default__.TestGetKeysForMrk()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_9_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_9_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestConfig.TestInvalidKmsKeyArnConfig: ")))
        try:
            if True:
                TestConfig.default__.TestInvalidKmsKeyArnConfig()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_10_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_10_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestConfig.TestInvalidKmsKeyArnAliasConfig: ")))
        try:
            if True:
                TestConfig.default__.TestInvalidKmsKeyArnAliasConfig()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_11_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_11_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestConfig.TestValidConfig: ")))
        try:
            if True:
                TestConfig.default__.TestValidConfig()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_12_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_12_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestConfig.TestValidConfigNoClients: ")))
        try:
            if True:
                TestConfig.default__.TestValidConfigNoClients()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_13_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_13_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetBeaconKey: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetBeaconKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_14_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_14_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKey: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_15_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_15_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveMrkKey: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveMrkKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_16_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_16_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetBranchKeyVersion: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetBranchKeyVersion()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_17_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_17_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKeyWithIncorrectKmsKeyArn: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKeyWithIncorrectKmsKeyArn()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_18_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_18_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKeyWrongLogicalKeyStoreName: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKeyWrongLogicalKeyStoreName()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_19_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_19_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKeyDoesNotExistFails: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKeyDoesNotExistFails()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_20_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_20_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestGetKeys.TestGetActiveKeyWithNoClients: ")))
        try:
            if True:
                TestGetKeys.default__.TestGetActiveKeyWithNoClients()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_21_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_21_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.TestCreateBranchAndBeaconKeys: ")))
        try:
            if True:
                TestCreateKeys.default__.TestCreateBranchAndBeaconKeys()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_22_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_22_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.TestCreateOptions: ")))
        try:
            if True:
                TestCreateKeys.default__.TestCreateOptions()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_23_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_23_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.TestCreateDuplicate: ")))
        try:
            if True:
                TestCreateKeys.default__.TestCreateDuplicate()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_24_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_24_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.InsertingADuplicateWillFail: ")))
        try:
            if True:
                TestCreateKeys.default__.InsertingADuplicateWillFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_25_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_25_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCreateKeys.InsertingADuplicateWillWithADifferentVersionFail: ")))
        try:
            if True:
                TestCreateKeys.default__.InsertingADuplicateWillWithADifferentVersionFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_26_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_26_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.TestVersionKey: ")))
        try:
            if True:
                TestVersionKey.default__.TestVersionKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_27_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_27_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.TestVersionKeyWithEC: ")))
        try:
            if True:
                TestVersionKey.default__.TestVersionKeyWithEC()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_28_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_28_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.TestMrkVersionKey: ")))
        try:
            if True:
                TestVersionKey.default__.TestMrkVersionKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_29_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_29_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.InsertingADuplicateVersionWillFail: ")))
        try:
            if True:
                TestVersionKey.default__.InsertingADuplicateVersionWillFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_30_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_30_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestVersionKey.VersioningANonexistentBranchKeyWillFail: ")))
        try:
            if True:
                TestVersionKey.default__.VersioningANonexistentBranchKeyWillFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_31_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_31_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestIntermediateKeyWrapping.IntermediateWrapUnwrapTest: ")))
        try:
            if True:
                TestIntermediateKeyWrapping.default__.IntermediateWrapUnwrapTest()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_32_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_32_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestIntermediateKeyWrapping.IntermediateGenerateAndWrapUnwrapTest: ")))
        try:
            if True:
                TestIntermediateKeyWrapping.default__.IntermediateGenerateAndWrapUnwrapTest()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_33_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_33_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestErrorMessages.TestIncorrectRawDataKeys: ")))
        try:
            if True:
                TestErrorMessages.default__.TestIncorrectRawDataKeys()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_34_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_34_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestErrorMessages.TestIncorrectDataKeys: ")))
        try:
            if True:
                TestErrorMessages.default__.TestIncorrectDataKeys()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_35_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_35_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestDefaultClientProvider.GetUsWestTwo: ")))
        try:
            if True:
                TestDefaultClientProvider.default__.GetUsWestTwo()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_36_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_36_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawECDHKeyring.TestRawEcdhDiscoveryOnEncryptFailure: ")))
        try:
            if True:
                TestRawECDHKeyring.default__.TestRawEcdhDiscoveryOnEncryptFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_37_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_37_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawECDHKeyring.TestRawEcdhEphemeralOnDecryptFailure: ")))
        try:
            if True:
                TestRawECDHKeyring.default__.TestRawEcdhEphemeralOnDecryptFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_38_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_38_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawECDHKeyring.TestRawEcdhKeyringEphemeralDecryptOwnMessageFailure: ")))
        try:
            if True:
                TestRawECDHKeyring.default__.TestRawEcdhKeyringEphemeralDecryptOwnMessageFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_39_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_39_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawECDHKeyring.TestRawEcdhKeyringStaticSuccess: ")))
        try:
            if True:
                TestRawECDHKeyring.default__.TestRawEcdhKeyringStaticSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_40_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_40_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawECDHKeyring.TestTwoRawEcdhKeyringStaticSuccess: ")))
        try:
            if True:
                TestRawECDHKeyring.default__.TestTwoRawEcdhKeyringStaticSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_41_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_41_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawECDHKeyring.TestTwoEcdhKeyringStaticSuccess: ")))
        try:
            if True:
                TestRawECDHKeyring.default__.TestTwoEcdhKeyringStaticSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_42_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_42_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawECDHKeyring.TestRawEcdhKeyringEncryptDecryptSuccessDBESDKSuite: ")))
        try:
            if True:
                TestRawECDHKeyring.default__.TestRawEcdhKeyringEncryptDecryptSuccessDBESDKSuite()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_43_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_43_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawECDHKeyring.TestPrivateKeyandPublicKeySameCurveDiffCurveDefinitionConstructionFailure: ")))
        try:
            if True:
                TestRawECDHKeyring.default__.TestPrivateKeyandPublicKeySameCurveDiffCurveDefinitionConstructionFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_44_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_44_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawECDHKeyring.TestPrivateKeyandPublicKeySameCurveDiffCurveDefinitionConstructionCombinationsFailure: ")))
        try:
            if True:
                TestRawECDHKeyring.default__.TestPrivateKeyandPublicKeySameCurveDiffCurveDefinitionConstructionCombinationsFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_45_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_45_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnEncryptOnDecryptGenerateDataKey: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnEncryptOnDecryptGenerateDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_46_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_46_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnEncryptOnDecryptSuppliedDataKey: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnEncryptOnDecryptSuppliedDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_47_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_47_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptKeyNameMismatch: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptKeyNameMismatch()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_48_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_48_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptBadAndGoodEdkSucceeds: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptBadAndGoodEdkSucceeds()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_49_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_49_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptNoEDKs: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptNoEDKs()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_50_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_50_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnEncryptUnserializableEC: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnEncryptUnserializableEC()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_51_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_51_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawAESKeyring.TestOnDecryptUnserializableEC: ")))
        try:
            if True:
                TestRawAESKeyring.default__.TestOnDecryptUnserializableEC()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_52_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_52_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestHappyCase: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestHappyCase()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_53_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_53_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestChildKeyringFailureEncrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestChildKeyringFailureEncrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_54_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_54_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorKeyringFails: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorKeyringFails()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_55_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_55_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorKeyringDoesNotReturnPlaintextDataKey: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorKeyringDoesNotReturnPlaintextDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_56_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_56_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorAbleToDecrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorAbleToDecrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_57_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_57_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestGeneratorUnableToDecrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestGeneratorUnableToDecrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_58_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_58_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestMultiKeyring.TestCollectFailuresDecrypt: ")))
        try:
            if True:
                TestMultiKeyring.default__.TestCollectFailuresDecrypt()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_59_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_59_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnEncryptOnDecryptSuppliedDataKey: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnEncryptOnDecryptSuppliedDataKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_60_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_60_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnDecryptKeyNameMismatch: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnDecryptKeyNameMismatch()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_61_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_61_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnDecryptFailure: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnDecryptFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_62_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_62_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestRawRSAKeying.TestOnDecryptBadAndGoodEdkSucceeds: ")))
        try:
            if True:
                TestRawRSAKeying.default__.TestOnDecryptBadAndGoodEdkSucceeds()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_63_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_63_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsRsaKeyring.TestKmsRsaRoundtrip: ")))
        try:
            if True:
                TestAwsKmsRsaKeyring.default__.TestKmsRsaRoundtrip()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_64_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_64_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsRsaKeyring.TestKmsRsaWithAsymmetricSignatureFails: ")))
        try:
            if True:
                TestAwsKmsRsaKeyring.default__.TestKmsRsaWithAsymmetricSignatureFails()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_65_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_65_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsHierarchicalKeyring.TestHierarchyClientESDKSuite: ")))
        try:
            if True:
                TestAwsKmsHierarchicalKeyring.default__.TestHierarchyClientESDKSuite()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_66_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_66_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsHierarchicalKeyring.TestHierarchyClientDBESuite: ")))
        try:
            if True:
                TestAwsKmsHierarchicalKeyring.default__.TestHierarchyClientDBESuite()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_67_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_67_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsHierarchicalKeyring.TestBranchKeyIdSupplier: ")))
        try:
            if True:
                TestAwsKmsHierarchicalKeyring.default__.TestBranchKeyIdSupplier()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_68_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_68_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsHierarchicalKeyring.TestInvalidDataKeyError: ")))
        try:
            if True:
                TestAwsKmsHierarchicalKeyring.default__.TestInvalidDataKeyError()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_69_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_69_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEcdhKeyring.TestKmsEcdhConfigurationFailure: ")))
        try:
            if True:
                TestAwsKmsEcdhKeyring.default__.TestKmsEcdhConfigurationFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_70_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_70_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEcdhKeyring.TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccess: ")))
        try:
            if True:
                TestAwsKmsEcdhKeyring.default__.TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_71_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_71_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEcdhKeyring.TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccessDBESDKSuite: ")))
        try:
            if True:
                TestAwsKmsEcdhKeyring.default__.TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccessDBESDKSuite()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_72_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_72_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEcdhKeyring.TestKmsEcdhKeyringDiscoverySuccess: ")))
        try:
            if True:
                TestAwsKmsEcdhKeyring.default__.TestKmsEcdhKeyringDiscoverySuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_73_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_73_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEcdhKeyring.TestKmsEcdhKeyringRecipientRawKeyEncryptDecryptSuccessSetSenderPublicKey: ")))
        try:
            if True:
                TestAwsKmsEcdhKeyring.default__.TestKmsEcdhKeyringRecipientRawKeyEncryptDecryptSuccessSetSenderPublicKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_74_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_74_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEcdhKeyring.TestKmsEcdhKeyringWithDerPublicKeys: ")))
        try:
            if True:
                TestAwsKmsEcdhKeyring.default__.TestKmsEcdhKeyringWithDerPublicKeys()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_75_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_75_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEcdhKeyring.TestKmsEcdhRawEcdhKeyringWithDerPublicKeys: ")))
        try:
            if True:
                TestAwsKmsEcdhKeyring.default__.TestKmsEcdhRawEcdhKeyringWithDerPublicKeys()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_76_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_76_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEcdhKeyring.TestKmsEcdhKeyringWithIncorrectCurveConfigurationFailure: ")))
        try:
            if True:
                TestAwsKmsEcdhKeyring.default__.TestKmsEcdhKeyringWithIncorrectCurveConfigurationFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_77_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_77_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEcdhKeyring.TestKmsEcdhKeyringWithIncorrectCurveConfigurationCombinationsFailure: ")))
        try:
            if True:
                TestAwsKmsEcdhKeyring.default__.TestKmsEcdhKeyringWithIncorrectCurveConfigurationCombinationsFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_78_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_78_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEcdhKeyring.TestLyingKmsKey: ")))
        try:
            if True:
                TestAwsKmsEcdhKeyring.default__.TestLyingKmsKey()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_79_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_79_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEncryptedDataKeyFilter.TestFailsNonKeyResource: ")))
        try:
            if True:
                TestAwsKmsEncryptedDataKeyFilter.default__.TestFailsNonKeyResource()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_80_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_80_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsKmsEncryptedDataKeyFilter.TestMatchesKeyringsConfiguration: ")))
        try:
            if True:
                TestAwsKmsEncryptedDataKeyFilter.default__.TestMatchesKeyringsConfiguration()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_81_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_81_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestLocalCMC.LocalCMCBasics: ")))
        try:
            if True:
                TestLocalCMC.default__.LocalCMCBasics()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_82_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_82_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerBasics: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerBasics()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_83_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_83_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerFanOut: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerFanOut()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_84_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_84_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerTTL: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerTTL()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_85_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_85_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerGraceInterval: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerGraceInterval()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_86_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_86_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestStormTracker.StormTrackerGracePeriod: ")))
        try:
            if True:
                TestStormTracker.default__.StormTrackerGracePeriod()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_87_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_87_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestEcdhCalculation.TestKmsDeriveSharedSecretOfflineCalculation: ")))
        try:
            if True:
                TestEcdhCalculation.default__.TestKmsDeriveSharedSecretOfflineCalculation()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_88_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_88_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestEcdhCalculation.TestKmsDeriveSharedSecretOfflineCalculationCurves: ")))
        try:
            if True:
                TestEcdhCalculation.default__.TestKmsDeriveSharedSecretOfflineCalculationCurves()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_89_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_89_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestEcdhCalculation.TestOfflineDeriveSharedSecretStaticKeys: ")))
        try:
            if True:
                TestEcdhCalculation.default__.TestOfflineDeriveSharedSecretStaticKeys()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_90_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_90_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_0_success_ = False
        if not(d_0_success_):
            raise _dafny.HaltException("<stdin>(1,0): " + _dafny.string_of(_dafny.Seq("Test failures occurred: see above.\n")))

