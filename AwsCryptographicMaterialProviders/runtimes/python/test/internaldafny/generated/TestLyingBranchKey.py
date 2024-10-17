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

# Module: TestLyingBranchKey

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestGetActiveKeyForLyingBranchKey():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(26,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(27,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_3_ddbClient_ = (d_2_valueOrError1_).Extract()
        d_4_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_4_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.postalHornKeyArn)
        d_5_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_5_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_4_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_3_ddbClient_), Wrappers.Option_Some(d_1_kmsClient_))
        d_6_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_5_keyStoreConfig_)
        d_6_valueOrError2_ = out2_
        if not(not((d_6_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(38,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_result_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.lyingBranchKeyId))
        d_8_result_ = out3_
        if not((d_8_result_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source0_ = (d_8_result_).error
        with _dafny.label("match0"):
            if True:
                if source0_.is_ComAmazonawsKms:
                    d_9_nestedError_ = source0_.ComAmazonawsKms
                    if not((d_9_nestedError_).is_IncorrectKeyException):
                        raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(47,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                    raise _dafny.Break("match0")
            if True:
                if not(False):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(48,16): " + _dafny.string_of(_dafny.Seq("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")))
            pass

    @staticmethod
    def TestGetBranchKeyVersionForLyingBranchKey():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(53,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(54,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_3_ddbClient_ = (d_2_valueOrError1_).Extract()
        d_4_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_4_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.postalHornKeyArn)
        d_5_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_5_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_4_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_3_ddbClient_), Wrappers.Option_Some(d_1_kmsClient_))
        d_6_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_5_keyStoreConfig_)
        d_6_valueOrError2_ = out2_
        if not(not((d_6_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(65,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_result_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(Fixtures.default__.lyingBranchKeyId, Fixtures.default__.lyingBranchKeyDecryptOnlyVersion))
        d_8_result_ = out3_
        if not((d_8_result_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source0_ = (d_8_result_).error
        with _dafny.label("match0"):
            if True:
                if source0_.is_ComAmazonawsKms:
                    d_9_nestedError_ = source0_.ComAmazonawsKms
                    if not((d_9_nestedError_).is_IncorrectKeyException):
                        raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(75,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                    raise _dafny.Break("match0")
            if True:
                if not(False):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(76,16): " + _dafny.string_of(_dafny.Seq("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")))
            pass

    @staticmethod
    def TestGetBeaconKeyForLyingBranchKey():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(81,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(82,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_3_ddbClient_ = (d_2_valueOrError1_).Extract()
        d_4_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_4_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.postalHornKeyArn)
        d_5_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_5_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_4_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_3_ddbClient_), Wrappers.Option_Some(d_1_kmsClient_))
        d_6_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_5_keyStoreConfig_)
        d_6_valueOrError2_ = out2_
        if not(not((d_6_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(93,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_result_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.lyingBranchKeyId))
        d_8_result_ = out3_
        if not((d_8_result_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(99,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source0_ = (d_8_result_).error
        with _dafny.label("match0"):
            if True:
                if source0_.is_ComAmazonawsKms:
                    d_9_nestedError_ = source0_.ComAmazonawsKms
                    if not((d_9_nestedError_).is_IncorrectKeyException):
                        raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(102,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                    raise _dafny.Break("match0")
            if True:
                if not(False):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(103,16): " + _dafny.string_of(_dafny.Seq("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")))
            pass

    @staticmethod
    def TestVersionKeyForLyingBranchKey():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(108,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(109,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_3_ddbClient_ = (d_2_valueOrError1_).Extract()
        d_4_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_4_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.postalHornKeyArn)
        d_5_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_5_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_4_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_3_ddbClient_), Wrappers.Option_Some(d_1_kmsClient_))
        d_6_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_5_keyStoreConfig_)
        d_6_valueOrError2_ = out2_
        if not(not((d_6_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(120,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_result_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).VersionKey(AwsCryptographyKeyStoreTypes.VersionKeyInput_VersionKeyInput(Fixtures.default__.lyingBranchKeyId))
        d_8_result_ = out3_
        if not((d_8_result_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(126,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source0_ = (d_8_result_).error
        with _dafny.label("match0"):
            if True:
                if source0_.is_ComAmazonawsKms:
                    d_9_nestedError_ = source0_.ComAmazonawsKms
                    if not((d_9_nestedError_).is_IncorrectKeyException):
                        raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(129,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                    raise _dafny.Break("match0")
            if True:
                if not(False):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(130,16): " + _dafny.string_of(_dafny.Seq("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")))
            pass

