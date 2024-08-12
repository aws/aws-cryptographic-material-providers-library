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
import TestLyingBranchKey as TestLyingBranchKey

# Module: TestDiscoveryGetKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestGetBeaconKeyForTwoKmsArnsSuccess():
        d_62_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_63_valueOrError0_: Wrappers.Result = None
        out20_: Wrappers.Result
        out20_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_63_valueOrError0_ = out20_
        if not(not((d_63_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(24,21): " + _dafny.string_of(d_63_valueOrError0_))
        d_62_kmsClient_ = (d_63_valueOrError0_).Extract()
        d_64_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_65_valueOrError1_: Wrappers.Result = None
        out21_: Wrappers.Result
        out21_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_65_valueOrError1_ = out21_
        if not(not((d_65_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(25,21): " + _dafny.string_of(d_65_valueOrError1_))
        d_64_ddbClient_ = (d_65_valueOrError1_).Extract()
        d_66_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_66_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_discovery(AwsCryptographyKeyStoreTypes.Discovery_Discovery())
        d_67_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_67_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_66_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_64_ddbClient_), Wrappers.Option_Some(d_62_kmsClient_))
        d_68_keyStore_: KeyStore.KeyStoreClient
        d_69_valueOrError2_: Wrappers.Result = None
        out22_: Wrappers.Result
        out22_ = KeyStore.default__.KeyStore(d_67_keyStoreConfig_)
        d_69_valueOrError2_ = out22_
        if not(not((d_69_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(38,20): " + _dafny.string_of(d_69_valueOrError2_))
        d_68_keyStore_ = (d_69_valueOrError2_).Extract()
        d_70_beaconKeyResult_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_71_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out23_: Wrappers.Result
        out23_ = (d_68_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.branchKeyId))
        d_71_valueOrError3_ = out23_
        if not(not((d_71_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(40,27): " + _dafny.string_of(d_71_valueOrError3_))
        d_70_beaconKeyResult_ = (d_71_valueOrError3_).Extract()
        if not((((d_70_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_72_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out24_: Wrappers.Result
        out24_ = (d_68_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.postalHornBranchKeyId))
        d_72_valueOrError4_ = out24_
        if not(not((d_72_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(46,23): " + _dafny.string_of(d_72_valueOrError4_))
        d_70_beaconKeyResult_ = (d_72_valueOrError4_).Extract()
        if not((((d_70_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier) == (Fixtures.default__.postalHornBranchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(51,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyForTwoKmsArnsSuccess():
        d_73_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_74_valueOrError0_: Wrappers.Result = None
        out25_: Wrappers.Result
        out25_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_74_valueOrError0_ = out25_
        if not(not((d_74_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(57,21): " + _dafny.string_of(d_74_valueOrError0_))
        d_73_kmsClient_ = (d_74_valueOrError0_).Extract()
        d_75_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_76_valueOrError1_: Wrappers.Result = None
        out26_: Wrappers.Result
        out26_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_76_valueOrError1_ = out26_
        if not(not((d_76_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(58,21): " + _dafny.string_of(d_76_valueOrError1_))
        d_75_ddbClient_ = (d_76_valueOrError1_).Extract()
        d_77_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_77_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_discovery(AwsCryptographyKeyStoreTypes.Discovery_Discovery())
        d_78_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_78_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_77_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_75_ddbClient_), Wrappers.Option_Some(d_73_kmsClient_))
        d_79_keyStore_: KeyStore.KeyStoreClient
        d_80_valueOrError2_: Wrappers.Result = None
        out27_: Wrappers.Result
        out27_ = KeyStore.default__.KeyStore(d_78_keyStoreConfig_)
        d_80_valueOrError2_ = out27_
        if not(not((d_80_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(71,20): " + _dafny.string_of(d_80_valueOrError2_))
        d_79_keyStore_ = (d_80_valueOrError2_).Extract()
        d_81_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_82_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out28_: Wrappers.Result
        out28_ = (d_79_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_82_valueOrError3_ = out28_
        if not(not((d_82_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(73,24): " + _dafny.string_of(d_82_valueOrError3_))
        d_81_activeResult_ = (d_82_valueOrError3_).Extract()
        if not((((d_81_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(78,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_83_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out29_: Wrappers.Result
        out29_ = (d_79_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.postalHornBranchKeyId))
        d_83_valueOrError4_ = out29_
        if not(not((d_83_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(80,20): " + _dafny.string_of(d_83_valueOrError4_))
        d_81_activeResult_ = (d_83_valueOrError4_).Extract()
        if not((((d_81_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.postalHornBranchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(85,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetBranchKeyVersionForTwoKmsArnsSuccess():
        d_84_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_85_valueOrError0_: Wrappers.Result = None
        out30_: Wrappers.Result
        out30_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_85_valueOrError0_ = out30_
        if not(not((d_85_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(90,21): " + _dafny.string_of(d_85_valueOrError0_))
        d_84_kmsClient_ = (d_85_valueOrError0_).Extract()
        d_86_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_87_valueOrError1_: Wrappers.Result = None
        out31_: Wrappers.Result
        out31_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_87_valueOrError1_ = out31_
        if not(not((d_87_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(91,21): " + _dafny.string_of(d_87_valueOrError1_))
        d_86_ddbClient_ = (d_87_valueOrError1_).Extract()
        d_88_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_88_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_discovery(AwsCryptographyKeyStoreTypes.Discovery_Discovery())
        d_89_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_89_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_88_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_86_ddbClient_), Wrappers.Option_Some(d_84_kmsClient_))
        d_90_keyStore_: KeyStore.KeyStoreClient
        d_91_valueOrError2_: Wrappers.Result = None
        out32_: Wrappers.Result
        out32_ = KeyStore.default__.KeyStore(d_89_keyStoreConfig_)
        d_91_valueOrError2_ = out32_
        if not(not((d_91_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(104,20): " + _dafny.string_of(d_91_valueOrError2_))
        d_90_keyStore_ = (d_91_valueOrError2_).Extract()
        d_92_versionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_93_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out33_: Wrappers.Result
        out33_ = (d_90_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion))
        d_93_valueOrError3_ = out33_
        if not(not((d_93_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(106,25): " + _dafny.string_of(d_93_valueOrError3_))
        d_92_versionResult_ = (d_93_valueOrError3_).Extract()
        d_94_testBytes_: _dafny.Seq
        d_95_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_95_valueOrError4_ = UTF8.default__.Encode(Fixtures.default__.branchKeyIdActiveVersion)
        if not(not((d_95_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(111,21): " + _dafny.string_of(d_95_valueOrError4_))
        d_94_testBytes_ = (d_95_valueOrError4_).Extract()
        if not((((d_92_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_92_versionResult_).branchKeyMaterials).branchKeyVersion) == (Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes)) and ((Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes) == (d_94_testBytes_))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_96_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out34_: Wrappers.Result
        out34_ = (d_90_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(Fixtures.default__.postalHornBranchKeyId, Fixtures.default__.postalHornBranchKeyActiveVersion))
        d_96_valueOrError5_ = out34_
        if not(not((d_96_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(115,21): " + _dafny.string_of(d_96_valueOrError5_))
        d_92_versionResult_ = (d_96_valueOrError5_).Extract()
        d_97_valueOrError6_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_97_valueOrError6_ = UTF8.default__.Encode(Fixtures.default__.postalHornBranchKeyActiveVersion)
        if not(not((d_97_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(120,17): " + _dafny.string_of(d_97_valueOrError6_))
        d_94_testBytes_ = (d_97_valueOrError6_).Extract()
        if not((((d_92_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.postalHornBranchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(121,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_92_versionResult_).branchKeyMaterials).branchKeyVersion) == (d_94_testBytes_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(122,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetKeysForMrk():
        d_98_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_99_valueOrError0_: Wrappers.Result = None
        out35_: Wrappers.Result
        out35_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_99_valueOrError0_ = out35_
        if not(not((d_99_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(127,21): " + _dafny.string_of(d_99_valueOrError0_))
        d_98_kmsClient_ = (d_99_valueOrError0_).Extract()
        d_100_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_101_valueOrError1_: Wrappers.Result = None
        out36_: Wrappers.Result
        out36_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_101_valueOrError1_ = out36_
        if not(not((d_101_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(128,21): " + _dafny.string_of(d_101_valueOrError1_))
        d_100_ddbClient_ = (d_101_valueOrError1_).Extract()
        d_102_kmsConfigMr_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_102_kmsConfigMr_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_mrDiscovery(AwsCryptographyKeyStoreTypes.MRDiscovery_MRDiscovery(_dafny.Seq("us-west-2")))
        d_103_kmsConfigSr_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_103_kmsConfigSr_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_discovery(AwsCryptographyKeyStoreTypes.Discovery_Discovery())
        d_104_keyStoreConfigMr_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_104_keyStoreConfigMr_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_102_kmsConfigMr_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_100_ddbClient_), Wrappers.Option_Some(d_98_kmsClient_))
        pat_let_tv0_ = d_103_kmsConfigSr_
        d_105_keyStoreConfigSr_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        def iife8_(_pat_let2_0):
            def iife9_(d_106_dt__update__tmp_h0_):
                def iife10_(_pat_let3_0):
                    def iife11_(d_107_dt__update_hkmsConfiguration_h0_):
                        return AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig((d_106_dt__update__tmp_h0_).ddbTableName, d_107_dt__update_hkmsConfiguration_h0_, (d_106_dt__update__tmp_h0_).logicalKeyStoreName, (d_106_dt__update__tmp_h0_).id, (d_106_dt__update__tmp_h0_).grantTokens, (d_106_dt__update__tmp_h0_).ddbClient, (d_106_dt__update__tmp_h0_).kmsClient)
                    return iife11_(_pat_let3_0)
                return iife10_(pat_let_tv0_)
            return iife9_(_pat_let2_0)
        d_105_keyStoreConfigSr_ = iife8_(d_104_keyStoreConfigMr_)
        d_108_keyStoreMr_: KeyStore.KeyStoreClient
        d_109_valueOrError2_: Wrappers.Result = None
        out37_: Wrappers.Result
        out37_ = KeyStore.default__.KeyStore(d_104_keyStoreConfigMr_)
        d_109_valueOrError2_ = out37_
        if not(not((d_109_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(144,22): " + _dafny.string_of(d_109_valueOrError2_))
        d_108_keyStoreMr_ = (d_109_valueOrError2_).Extract()
        d_110_keyStoreSr_: KeyStore.KeyStoreClient
        d_111_valueOrError3_: Wrappers.Result = None
        out38_: Wrappers.Result
        out38_ = KeyStore.default__.KeyStore(d_105_keyStoreConfigSr_)
        d_111_valueOrError3_ = out38_
        if not(not((d_111_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(145,22): " + _dafny.string_of(d_111_valueOrError3_))
        d_110_keyStoreSr_ = (d_111_valueOrError3_).Extract()
        d_112_beaconInput_: AwsCryptographyKeyStoreTypes.GetBeaconKeyInput
        d_112_beaconInput_ = AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.EastBranchKey)
        d_113_beaconKeyResultMr_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_114_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out39_: Wrappers.Result
        out39_ = (d_108_keyStoreMr_).GetBeaconKey(d_112_beaconInput_)
        d_114_valueOrError4_ = out39_
        if not(not((d_114_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(148,29): " + _dafny.string_of(d_114_valueOrError4_))
        d_113_beaconKeyResultMr_ = (d_114_valueOrError4_).Extract()
        if not((((d_113_beaconKeyResultMr_).beaconKeyMaterials).beaconKeyIdentifier) == (Fixtures.default__.EastBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(149,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_115_beaconKeyResultSr_: Wrappers.Result
        out40_: Wrappers.Result
        out40_ = (d_110_keyStoreSr_).GetBeaconKey(d_112_beaconInput_)
        d_115_beaconKeyResultSr_ = out40_
        if not((d_115_beaconKeyResultSr_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(152,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_115_beaconKeyResultSr_).error).is_ComAmazonawsKms):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(153,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source4_ = (d_115_beaconKeyResultSr_).error
        unmatched4 = True
        if unmatched4:
            if source4_.is_ComAmazonawsKms:
                d_116_nestedError_ = source4_.ComAmazonawsKms
                unmatched4 = False
                if not((d_116_nestedError_).is_IncorrectKeyException):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(156,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if unmatched4:
            unmatched4 = False
            if not(False):
                raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(157,16): " + _dafny.string_of(_dafny.Seq("Request for Branch Key's Beacon Key protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")))
        d_117_branchInput_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput
        d_117_branchInput_ = AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.EastBranchKey)
        d_118_branchKeyResultMr_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_119_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out41_: Wrappers.Result
        out41_ = (d_108_keyStoreMr_).GetActiveBranchKey(d_117_branchInput_)
        d_119_valueOrError5_ = out41_
        if not(not((d_119_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(161,29): " + _dafny.string_of(d_119_valueOrError5_))
        d_118_branchKeyResultMr_ = (d_119_valueOrError5_).Extract()
        if not((((d_118_branchKeyResultMr_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.EastBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(162,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_120_branchKeyResultSr_: Wrappers.Result
        out42_: Wrappers.Result
        out42_ = (d_110_keyStoreSr_).GetActiveBranchKey(d_117_branchInput_)
        d_120_branchKeyResultSr_ = out42_
        if not((d_120_branchKeyResultSr_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(165,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_120_branchKeyResultSr_).error).is_ComAmazonawsKms):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(166,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source5_ = (d_120_branchKeyResultSr_).error
        unmatched5 = True
        if unmatched5:
            if source5_.is_ComAmazonawsKms:
                d_121_nestedError_ = source5_.ComAmazonawsKms
                unmatched5 = False
                if not((d_121_nestedError_).is_IncorrectKeyException):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(170,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if unmatched5:
            unmatched5 = False
            if not(False):
                raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(171,16): " + _dafny.string_of(_dafny.Seq("Request for Branch Key Active Version protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")))

