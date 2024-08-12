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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
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
import aws_cryptographic_materialproviders.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.Utils as Utils
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

# Module: TestLyingBranchKey

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestGetActiveKeyForLyingBranchKey():
        d_22_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_23_valueOrError0_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_23_valueOrError0_ = out4_
        if not(not((d_23_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(26,21): " + _dafny.string_of(d_23_valueOrError0_))
        d_22_kmsClient_ = (d_23_valueOrError0_).Extract()
        d_24_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_25_valueOrError1_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_25_valueOrError1_ = out5_
        if not(not((d_25_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(27,21): " + _dafny.string_of(d_25_valueOrError1_))
        d_24_ddbClient_ = (d_25_valueOrError1_).Extract()
        d_26_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_26_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.postalHornKeyArn)
        d_27_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_27_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_26_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_24_ddbClient_), Wrappers.Option_Some(d_22_kmsClient_))
        d_28_keyStore_: KeyStore.KeyStoreClient
        d_29_valueOrError2_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = KeyStore.default__.KeyStore(d_27_keyStoreConfig_)
        d_29_valueOrError2_ = out6_
        if not(not((d_29_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(38,20): " + _dafny.string_of(d_29_valueOrError2_))
        d_28_keyStore_ = (d_29_valueOrError2_).Extract()
        d_30_result_: Wrappers.Result
        out7_: Wrappers.Result
        out7_ = (d_28_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.lyingBranchKeyId))
        d_30_result_ = out7_
        if not((d_30_result_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source0_ = (d_30_result_).error
        unmatched0 = True
        if unmatched0:
            if source0_.is_ComAmazonawsKms:
                d_31_nestedError_ = source0_.ComAmazonawsKms
                unmatched0 = False
                if not((d_31_nestedError_).is_IncorrectKeyException):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(47,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if unmatched0:
            unmatched0 = False
            if not(False):
                raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(48,16): " + _dafny.string_of(_dafny.Seq("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")))

    @staticmethod
    def TestGetBranchKeyVersionForLyingBranchKey():
        d_32_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_33_valueOrError0_: Wrappers.Result = None
        out8_: Wrappers.Result
        out8_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_33_valueOrError0_ = out8_
        if not(not((d_33_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(53,21): " + _dafny.string_of(d_33_valueOrError0_))
        d_32_kmsClient_ = (d_33_valueOrError0_).Extract()
        d_34_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_35_valueOrError1_: Wrappers.Result = None
        out9_: Wrappers.Result
        out9_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_35_valueOrError1_ = out9_
        if not(not((d_35_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(54,21): " + _dafny.string_of(d_35_valueOrError1_))
        d_34_ddbClient_ = (d_35_valueOrError1_).Extract()
        d_36_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_36_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.postalHornKeyArn)
        d_37_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_37_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_36_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_34_ddbClient_), Wrappers.Option_Some(d_32_kmsClient_))
        d_38_keyStore_: KeyStore.KeyStoreClient
        d_39_valueOrError2_: Wrappers.Result = None
        out10_: Wrappers.Result
        out10_ = KeyStore.default__.KeyStore(d_37_keyStoreConfig_)
        d_39_valueOrError2_ = out10_
        if not(not((d_39_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(65,20): " + _dafny.string_of(d_39_valueOrError2_))
        d_38_keyStore_ = (d_39_valueOrError2_).Extract()
        d_40_result_: Wrappers.Result
        out11_: Wrappers.Result
        out11_ = (d_38_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(Fixtures.default__.lyingBranchKeyId, Fixtures.default__.lyingBranchKeyDecryptOnlyVersion))
        d_40_result_ = out11_
        if not((d_40_result_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source1_ = (d_40_result_).error
        unmatched1 = True
        if unmatched1:
            if source1_.is_ComAmazonawsKms:
                d_41_nestedError_ = source1_.ComAmazonawsKms
                unmatched1 = False
                if not((d_41_nestedError_).is_IncorrectKeyException):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(75,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if unmatched1:
            unmatched1 = False
            if not(False):
                raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(76,16): " + _dafny.string_of(_dafny.Seq("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")))

    @staticmethod
    def TestGetBeaconKeyForLyingBranchKey():
        d_42_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_43_valueOrError0_: Wrappers.Result = None
        out12_: Wrappers.Result
        out12_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_43_valueOrError0_ = out12_
        if not(not((d_43_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(81,21): " + _dafny.string_of(d_43_valueOrError0_))
        d_42_kmsClient_ = (d_43_valueOrError0_).Extract()
        d_44_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_45_valueOrError1_: Wrappers.Result = None
        out13_: Wrappers.Result
        out13_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_45_valueOrError1_ = out13_
        if not(not((d_45_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(82,21): " + _dafny.string_of(d_45_valueOrError1_))
        d_44_ddbClient_ = (d_45_valueOrError1_).Extract()
        d_46_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_46_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.postalHornKeyArn)
        d_47_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_47_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_46_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_44_ddbClient_), Wrappers.Option_Some(d_42_kmsClient_))
        d_48_keyStore_: KeyStore.KeyStoreClient
        d_49_valueOrError2_: Wrappers.Result = None
        out14_: Wrappers.Result
        out14_ = KeyStore.default__.KeyStore(d_47_keyStoreConfig_)
        d_49_valueOrError2_ = out14_
        if not(not((d_49_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(93,20): " + _dafny.string_of(d_49_valueOrError2_))
        d_48_keyStore_ = (d_49_valueOrError2_).Extract()
        d_50_result_: Wrappers.Result
        out15_: Wrappers.Result
        out15_ = (d_48_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.lyingBranchKeyId))
        d_50_result_ = out15_
        if not((d_50_result_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(99,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source2_ = (d_50_result_).error
        unmatched2 = True
        if unmatched2:
            if source2_.is_ComAmazonawsKms:
                d_51_nestedError_ = source2_.ComAmazonawsKms
                unmatched2 = False
                if not((d_51_nestedError_).is_IncorrectKeyException):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(102,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if unmatched2:
            unmatched2 = False
            if not(False):
                raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(103,16): " + _dafny.string_of(_dafny.Seq("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")))

    @staticmethod
    def TestVersionKeyForLyingBranchKey():
        d_52_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_53_valueOrError0_: Wrappers.Result = None
        out16_: Wrappers.Result
        out16_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_53_valueOrError0_ = out16_
        if not(not((d_53_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(108,21): " + _dafny.string_of(d_53_valueOrError0_))
        d_52_kmsClient_ = (d_53_valueOrError0_).Extract()
        d_54_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_55_valueOrError1_: Wrappers.Result = None
        out17_: Wrappers.Result
        out17_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_55_valueOrError1_ = out17_
        if not(not((d_55_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(109,21): " + _dafny.string_of(d_55_valueOrError1_))
        d_54_ddbClient_ = (d_55_valueOrError1_).Extract()
        d_56_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_56_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.postalHornKeyArn)
        d_57_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_57_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_56_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_54_ddbClient_), Wrappers.Option_Some(d_52_kmsClient_))
        d_58_keyStore_: KeyStore.KeyStoreClient
        d_59_valueOrError2_: Wrappers.Result = None
        out18_: Wrappers.Result
        out18_ = KeyStore.default__.KeyStore(d_57_keyStoreConfig_)
        d_59_valueOrError2_ = out18_
        if not(not((d_59_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(120,20): " + _dafny.string_of(d_59_valueOrError2_))
        d_58_keyStore_ = (d_59_valueOrError2_).Extract()
        d_60_result_: Wrappers.Result
        out19_: Wrappers.Result
        out19_ = (d_58_keyStore_).VersionKey(AwsCryptographyKeyStoreTypes.VersionKeyInput_VersionKeyInput(Fixtures.default__.lyingBranchKeyId))
        d_60_result_ = out19_
        if not((d_60_result_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(126,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source3_ = (d_60_result_).error
        unmatched3 = True
        if unmatched3:
            if source3_.is_ComAmazonawsKms:
                d_61_nestedError_ = source3_.ComAmazonawsKms
                unmatched3 = False
                if not((d_61_nestedError_).is_IncorrectKeyException):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(129,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if unmatched3:
            unmatched3 = False
            if not(False):
                raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestLyingBranchKey.dfy(130,16): " + _dafny.string_of(_dafny.Seq("Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.")))

