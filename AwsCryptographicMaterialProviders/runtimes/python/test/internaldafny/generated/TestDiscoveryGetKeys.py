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

# Module: TestDiscoveryGetKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestGetBeaconKeyForTwoKmsArnsSuccess():
        d_22_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_23_valueOrError0_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_23_valueOrError0_ = out4_
        if not(not((d_23_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(24,21): " + _dafny.string_of(d_23_valueOrError0_))
        d_22_kmsClient_ = (d_23_valueOrError0_).Extract()
        d_24_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_25_valueOrError1_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_25_valueOrError1_ = out5_
        if not(not((d_25_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(25,21): " + _dafny.string_of(d_25_valueOrError1_))
        d_24_ddbClient_ = (d_25_valueOrError1_).Extract()
        d_26_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_26_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_discovery(AwsCryptographyKeyStoreTypes.Discovery_Discovery())
        d_27_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_27_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_26_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_24_ddbClient_), Wrappers.Option_Some(d_22_kmsClient_))
        d_28_keyStore_: KeyStore.KeyStoreClient
        d_29_valueOrError2_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = KeyStore.default__.KeyStore(d_27_keyStoreConfig_)
        d_29_valueOrError2_ = out6_
        if not(not((d_29_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(38,20): " + _dafny.string_of(d_29_valueOrError2_))
        d_28_keyStore_ = (d_29_valueOrError2_).Extract()
        d_30_beaconKeyResult_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_31_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out7_: Wrappers.Result
        out7_ = (d_28_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.branchKeyId))
        d_31_valueOrError3_ = out7_
        if not(not((d_31_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(40,27): " + _dafny.string_of(d_31_valueOrError3_))
        d_30_beaconKeyResult_ = (d_31_valueOrError3_).Extract()
        if not((((d_30_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_32_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out8_: Wrappers.Result
        out8_ = (d_28_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.postalHornBranchKeyId))
        d_32_valueOrError4_ = out8_
        if not(not((d_32_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(46,23): " + _dafny.string_of(d_32_valueOrError4_))
        d_30_beaconKeyResult_ = (d_32_valueOrError4_).Extract()
        if not((((d_30_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier) == (Fixtures.default__.postalHornBranchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(51,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyForTwoKmsArnsSuccess():
        d_33_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_34_valueOrError0_: Wrappers.Result = None
        out9_: Wrappers.Result
        out9_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_34_valueOrError0_ = out9_
        if not(not((d_34_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(57,21): " + _dafny.string_of(d_34_valueOrError0_))
        d_33_kmsClient_ = (d_34_valueOrError0_).Extract()
        d_35_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_36_valueOrError1_: Wrappers.Result = None
        out10_: Wrappers.Result
        out10_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_36_valueOrError1_ = out10_
        if not(not((d_36_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(58,21): " + _dafny.string_of(d_36_valueOrError1_))
        d_35_ddbClient_ = (d_36_valueOrError1_).Extract()
        d_37_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_37_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_discovery(AwsCryptographyKeyStoreTypes.Discovery_Discovery())
        d_38_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_38_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_37_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_35_ddbClient_), Wrappers.Option_Some(d_33_kmsClient_))
        d_39_keyStore_: KeyStore.KeyStoreClient
        d_40_valueOrError2_: Wrappers.Result = None
        out11_: Wrappers.Result
        out11_ = KeyStore.default__.KeyStore(d_38_keyStoreConfig_)
        d_40_valueOrError2_ = out11_
        if not(not((d_40_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(71,20): " + _dafny.string_of(d_40_valueOrError2_))
        d_39_keyStore_ = (d_40_valueOrError2_).Extract()
        d_41_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_42_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out12_: Wrappers.Result
        out12_ = (d_39_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_42_valueOrError3_ = out12_
        if not(not((d_42_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(73,24): " + _dafny.string_of(d_42_valueOrError3_))
        d_41_activeResult_ = (d_42_valueOrError3_).Extract()
        if not((((d_41_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(78,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_43_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out13_: Wrappers.Result
        out13_ = (d_39_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.postalHornBranchKeyId))
        d_43_valueOrError4_ = out13_
        if not(not((d_43_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(80,20): " + _dafny.string_of(d_43_valueOrError4_))
        d_41_activeResult_ = (d_43_valueOrError4_).Extract()
        if not((((d_41_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.postalHornBranchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(85,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetBranchKeyVersionForTwoKmsArnsSuccess():
        d_44_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_45_valueOrError0_: Wrappers.Result = None
        out14_: Wrappers.Result
        out14_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_45_valueOrError0_ = out14_
        if not(not((d_45_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(90,21): " + _dafny.string_of(d_45_valueOrError0_))
        d_44_kmsClient_ = (d_45_valueOrError0_).Extract()
        d_46_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_47_valueOrError1_: Wrappers.Result = None
        out15_: Wrappers.Result
        out15_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_47_valueOrError1_ = out15_
        if not(not((d_47_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(91,21): " + _dafny.string_of(d_47_valueOrError1_))
        d_46_ddbClient_ = (d_47_valueOrError1_).Extract()
        d_48_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_48_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_discovery(AwsCryptographyKeyStoreTypes.Discovery_Discovery())
        d_49_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_49_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_48_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_46_ddbClient_), Wrappers.Option_Some(d_44_kmsClient_))
        d_50_keyStore_: KeyStore.KeyStoreClient
        d_51_valueOrError2_: Wrappers.Result = None
        out16_: Wrappers.Result
        out16_ = KeyStore.default__.KeyStore(d_49_keyStoreConfig_)
        d_51_valueOrError2_ = out16_
        if not(not((d_51_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(104,20): " + _dafny.string_of(d_51_valueOrError2_))
        d_50_keyStore_ = (d_51_valueOrError2_).Extract()
        d_52_versionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_53_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out17_: Wrappers.Result
        out17_ = (d_50_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion))
        d_53_valueOrError3_ = out17_
        if not(not((d_53_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(106,25): " + _dafny.string_of(d_53_valueOrError3_))
        d_52_versionResult_ = (d_53_valueOrError3_).Extract()
        d_54_testBytes_: _dafny.Seq
        d_55_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_55_valueOrError4_ = UTF8.default__.Encode(Fixtures.default__.branchKeyIdActiveVersion)
        if not(not((d_55_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(111,21): " + _dafny.string_of(d_55_valueOrError4_))
        d_54_testBytes_ = (d_55_valueOrError4_).Extract()
        if not((((d_52_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_52_versionResult_).branchKeyMaterials).branchKeyVersion) == (Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes)) and ((Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes) == (d_54_testBytes_))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_56_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out18_: Wrappers.Result
        out18_ = (d_50_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(Fixtures.default__.postalHornBranchKeyId, Fixtures.default__.postalHornBranchKeyActiveVersion))
        d_56_valueOrError5_ = out18_
        if not(not((d_56_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(115,21): " + _dafny.string_of(d_56_valueOrError5_))
        d_52_versionResult_ = (d_56_valueOrError5_).Extract()
        d_57_valueOrError6_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_57_valueOrError6_ = UTF8.default__.Encode(Fixtures.default__.postalHornBranchKeyActiveVersion)
        if not(not((d_57_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(120,17): " + _dafny.string_of(d_57_valueOrError6_))
        d_54_testBytes_ = (d_57_valueOrError6_).Extract()
        if not((((d_52_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.postalHornBranchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(121,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_52_versionResult_).branchKeyMaterials).branchKeyVersion) == (d_54_testBytes_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(122,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetKeysForMrk():
        d_58_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_59_valueOrError0_: Wrappers.Result = None
        out19_: Wrappers.Result
        out19_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_59_valueOrError0_ = out19_
        if not(not((d_59_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(127,21): " + _dafny.string_of(d_59_valueOrError0_))
        d_58_kmsClient_ = (d_59_valueOrError0_).Extract()
        d_60_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_61_valueOrError1_: Wrappers.Result = None
        out20_: Wrappers.Result
        out20_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_61_valueOrError1_ = out20_
        if not(not((d_61_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(128,21): " + _dafny.string_of(d_61_valueOrError1_))
        d_60_ddbClient_ = (d_61_valueOrError1_).Extract()
        d_62_kmsConfigMr_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_62_kmsConfigMr_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_mrDiscovery(AwsCryptographyKeyStoreTypes.MRDiscovery_MRDiscovery(_dafny.Seq("us-west-2")))
        d_63_kmsConfigSr_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_63_kmsConfigSr_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_discovery(AwsCryptographyKeyStoreTypes.Discovery_Discovery())
        d_64_keyStoreConfigMr_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_64_keyStoreConfigMr_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_62_kmsConfigMr_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_60_ddbClient_), Wrappers.Option_Some(d_58_kmsClient_))
        pat_let_tv0_ = d_63_kmsConfigSr_
        d_65_keyStoreConfigSr_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        def iife8_(_pat_let2_0):
            def iife9_(d_66_dt__update__tmp_h0_):
                def iife10_(_pat_let3_0):
                    def iife11_(d_67_dt__update_hkmsConfiguration_h0_):
                        return AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig((d_66_dt__update__tmp_h0_).ddbTableName, d_67_dt__update_hkmsConfiguration_h0_, (d_66_dt__update__tmp_h0_).logicalKeyStoreName, (d_66_dt__update__tmp_h0_).id, (d_66_dt__update__tmp_h0_).grantTokens, (d_66_dt__update__tmp_h0_).ddbClient, (d_66_dt__update__tmp_h0_).kmsClient)
                    return iife11_(_pat_let3_0)
                return iife10_(pat_let_tv0_)
            return iife9_(_pat_let2_0)
        d_65_keyStoreConfigSr_ = iife8_(d_64_keyStoreConfigMr_)
        d_68_keyStoreMr_: KeyStore.KeyStoreClient
        d_69_valueOrError2_: Wrappers.Result = None
        out21_: Wrappers.Result
        out21_ = KeyStore.default__.KeyStore(d_64_keyStoreConfigMr_)
        d_69_valueOrError2_ = out21_
        if not(not((d_69_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(144,22): " + _dafny.string_of(d_69_valueOrError2_))
        d_68_keyStoreMr_ = (d_69_valueOrError2_).Extract()
        d_70_keyStoreSr_: KeyStore.KeyStoreClient
        d_71_valueOrError3_: Wrappers.Result = None
        out22_: Wrappers.Result
        out22_ = KeyStore.default__.KeyStore(d_65_keyStoreConfigSr_)
        d_71_valueOrError3_ = out22_
        if not(not((d_71_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(145,22): " + _dafny.string_of(d_71_valueOrError3_))
        d_70_keyStoreSr_ = (d_71_valueOrError3_).Extract()
        d_72_beaconInput_: AwsCryptographyKeyStoreTypes.GetBeaconKeyInput
        d_72_beaconInput_ = AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.EastBranchKey)
        d_73_beaconKeyResultMr_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_74_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out23_: Wrappers.Result
        out23_ = (d_68_keyStoreMr_).GetBeaconKey(d_72_beaconInput_)
        d_74_valueOrError4_ = out23_
        if not(not((d_74_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(148,29): " + _dafny.string_of(d_74_valueOrError4_))
        d_73_beaconKeyResultMr_ = (d_74_valueOrError4_).Extract()
        if not((((d_73_beaconKeyResultMr_).beaconKeyMaterials).beaconKeyIdentifier) == (Fixtures.default__.EastBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(149,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_75_beaconKeyResultSr_: Wrappers.Result
        out24_: Wrappers.Result
        out24_ = (d_70_keyStoreSr_).GetBeaconKey(d_72_beaconInput_)
        d_75_beaconKeyResultSr_ = out24_
        if not((d_75_beaconKeyResultSr_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(152,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_75_beaconKeyResultSr_).error).is_ComAmazonawsKms):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(153,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source0_ = (d_75_beaconKeyResultSr_).error
        unmatched0 = True
        if unmatched0:
            if source0_.is_ComAmazonawsKms:
                d_76_nestedError_ = source0_.ComAmazonawsKms
                unmatched0 = False
                if not((d_76_nestedError_).is_IncorrectKeyException):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(156,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if unmatched0:
            d_77___v0_ = source0_
            unmatched0 = False
            if not(False):
                raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(157,16): " + _dafny.string_of(_dafny.Seq("Request for Branch Key's Beacon Key protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")))
        d_78_branchInput_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput
        d_78_branchInput_ = AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.EastBranchKey)
        d_79_branchKeyResultMr_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_80_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out25_: Wrappers.Result
        out25_ = (d_68_keyStoreMr_).GetActiveBranchKey(d_78_branchInput_)
        d_80_valueOrError5_ = out25_
        if not(not((d_80_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(161,29): " + _dafny.string_of(d_80_valueOrError5_))
        d_79_branchKeyResultMr_ = (d_80_valueOrError5_).Extract()
        if not((((d_79_branchKeyResultMr_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.EastBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(162,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_81_branchKeyResultSr_: Wrappers.Result
        out26_: Wrappers.Result
        out26_ = (d_70_keyStoreSr_).GetActiveBranchKey(d_78_branchInput_)
        d_81_branchKeyResultSr_ = out26_
        if not((d_81_branchKeyResultSr_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(165,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_81_branchKeyResultSr_).error).is_ComAmazonawsKms):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(166,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source1_ = (d_81_branchKeyResultSr_).error
        unmatched1 = True
        if unmatched1:
            if source1_.is_ComAmazonawsKms:
                d_82_nestedError_ = source1_.ComAmazonawsKms
                unmatched1 = False
                if not((d_82_nestedError_).is_IncorrectKeyException):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(170,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if unmatched1:
            d_83___v1_ = source1_
            unmatched1 = False
            if not(False):
                raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(171,16): " + _dafny.string_of(_dafny.Seq("Request for Branch Key Active Version protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")))

