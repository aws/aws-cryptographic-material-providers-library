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

# Module: TestGetKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestGetBeaconKey():
        d_122_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_123_valueOrError0_: Wrappers.Result = None
        out42_: Wrappers.Result
        out42_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_123_valueOrError0_ = out42_
        if not(not((d_123_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(23,21): " + _dafny.string_of(d_123_valueOrError0_))
        d_122_kmsClient_ = (d_123_valueOrError0_).Extract()
        d_124_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_125_valueOrError1_: Wrappers.Result = None
        out43_: Wrappers.Result
        out43_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_125_valueOrError1_ = out43_
        if not(not((d_125_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(24,21): " + _dafny.string_of(d_125_valueOrError1_))
        d_124_ddbClient_ = (d_125_valueOrError1_).Extract()
        d_126_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_126_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_127_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_127_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_126_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_124_ddbClient_), Wrappers.Option_Some(d_122_kmsClient_))
        d_128_keyStore_: KeyStore.KeyStoreClient
        d_129_valueOrError2_: Wrappers.Result = None
        out44_: Wrappers.Result
        out44_ = KeyStore.default__.KeyStore(d_127_keyStoreConfig_)
        d_129_valueOrError2_ = out44_
        if not(not((d_129_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(37,20): " + _dafny.string_of(d_129_valueOrError2_))
        d_128_keyStore_ = (d_129_valueOrError2_).Extract()
        d_130_beaconKeyResult_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_131_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out45_: Wrappers.Result
        out45_ = (d_128_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.branchKeyId))
        d_131_valueOrError3_ = out45_
        if not(not((d_131_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(39,27): " + _dafny.string_of(d_131_valueOrError3_))
        d_130_beaconKeyResult_ = (d_131_valueOrError3_).Extract()
        if not((((d_130_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(43,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_130_beaconKeyResult_).beaconKeyMaterials).beaconKey).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((((d_130_beaconKeyResult_).beaconKeyMaterials).beaconKey).value)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(45,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKey():
        d_132_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_133_valueOrError0_: Wrappers.Result = None
        out46_: Wrappers.Result
        out46_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_133_valueOrError0_ = out46_
        if not(not((d_133_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(50,21): " + _dafny.string_of(d_133_valueOrError0_))
        d_132_kmsClient_ = (d_133_valueOrError0_).Extract()
        d_134_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_135_valueOrError1_: Wrappers.Result = None
        out47_: Wrappers.Result
        out47_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_135_valueOrError1_ = out47_
        if not(not((d_135_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(51,21): " + _dafny.string_of(d_135_valueOrError1_))
        d_134_ddbClient_ = (d_135_valueOrError1_).Extract()
        d_136_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_136_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_137_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_137_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_136_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_134_ddbClient_), Wrappers.Option_Some(d_132_kmsClient_))
        d_138_keyStore_: KeyStore.KeyStoreClient
        d_139_valueOrError2_: Wrappers.Result = None
        out48_: Wrappers.Result
        out48_ = KeyStore.default__.KeyStore(d_137_keyStoreConfig_)
        d_139_valueOrError2_ = out48_
        if not(not((d_139_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(64,20): " + _dafny.string_of(d_139_valueOrError2_))
        d_138_keyStore_ = (d_139_valueOrError2_).Extract()
        d_140_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_141_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out49_: Wrappers.Result
        out49_ = (d_138_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_141_valueOrError3_ = out49_
        if not(not((d_141_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(66,24): " + _dafny.string_of(d_141_valueOrError3_))
        d_140_activeResult_ = (d_141_valueOrError3_).Extract()
        if not((((d_140_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(71,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_140_activeResult_).branchKeyMaterials).branchKeyVersion) == (Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_140_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(73,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveMrkKey():
        d_142_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_143_valueOrError0_: Wrappers.Result = None
        out50_: Wrappers.Result
        out50_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_143_valueOrError0_ = out50_
        if not(not((d_143_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(78,21): " + _dafny.string_of(d_143_valueOrError0_))
        d_142_ddbClient_ = (d_143_valueOrError0_).Extract()
        d_144_eastKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_144_eastKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsConfigEast, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_142_ddbClient_), Wrappers.Option_None())
        d_145_westKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_145_westKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsConfigWest, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_142_ddbClient_), Wrappers.Option_None())
        d_146_eastMrkKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_146_eastMrkKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsMrkConfigEast, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_142_ddbClient_), Wrappers.Option_None())
        d_147_westMrkKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_147_westMrkKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsMrkConfigWest, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_142_ddbClient_), Wrappers.Option_None())
        d_148_apMrkKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_148_apMrkKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsMrkConfigAP, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_142_ddbClient_), Wrappers.Option_None())
        d_149_westKeyStore_: KeyStore.KeyStoreClient
        d_150_valueOrError1_: Wrappers.Result = None
        out51_: Wrappers.Result
        out51_ = KeyStore.default__.KeyStore(d_145_westKeyStoreConfig_)
        d_150_valueOrError1_ = out51_
        if not(not((d_150_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(127,24): " + _dafny.string_of(d_150_valueOrError1_))
        d_149_westKeyStore_ = (d_150_valueOrError1_).Extract()
        d_151_eastKeyStore_: KeyStore.KeyStoreClient
        d_152_valueOrError2_: Wrappers.Result = None
        out52_: Wrappers.Result
        out52_ = KeyStore.default__.KeyStore(d_144_eastKeyStoreConfig_)
        d_152_valueOrError2_ = out52_
        if not(not((d_152_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(128,24): " + _dafny.string_of(d_152_valueOrError2_))
        d_151_eastKeyStore_ = (d_152_valueOrError2_).Extract()
        d_153_westMrkKeyStore_: KeyStore.KeyStoreClient
        d_154_valueOrError3_: Wrappers.Result = None
        out53_: Wrappers.Result
        out53_ = KeyStore.default__.KeyStore(d_147_westMrkKeyStoreConfig_)
        d_154_valueOrError3_ = out53_
        if not(not((d_154_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(129,27): " + _dafny.string_of(d_154_valueOrError3_))
        d_153_westMrkKeyStore_ = (d_154_valueOrError3_).Extract()
        d_155_eastMrkKeyStore_: KeyStore.KeyStoreClient
        d_156_valueOrError4_: Wrappers.Result = None
        out54_: Wrappers.Result
        out54_ = KeyStore.default__.KeyStore(d_146_eastMrkKeyStoreConfig_)
        d_156_valueOrError4_ = out54_
        if not(not((d_156_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(130,27): " + _dafny.string_of(d_156_valueOrError4_))
        d_155_eastMrkKeyStore_ = (d_156_valueOrError4_).Extract()
        d_157_apMrkKeyStore_: KeyStore.KeyStoreClient
        d_158_valueOrError5_: Wrappers.Result = None
        out55_: Wrappers.Result
        out55_ = KeyStore.default__.KeyStore(d_148_apMrkKeyStoreConfig_)
        d_158_valueOrError5_ = out55_
        if not(not((d_158_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(131,25): " + _dafny.string_of(d_158_valueOrError5_))
        d_157_apMrkKeyStore_ = (d_158_valueOrError5_).Extract()
        d_159_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_160_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out56_: Wrappers.Result
        out56_ = (d_149_westKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.WestBranchKey))
        d_160_valueOrError6_ = out56_
        if not(not((d_160_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(135,24): " + _dafny.string_of(d_160_valueOrError6_))
        d_159_activeResult_ = (d_160_valueOrError6_).Extract()
        if not((((d_159_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.WestBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(137,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_159_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(138,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_161_valueOrError7_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out57_: Wrappers.Result
        out57_ = (d_151_eastKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.EastBranchKey))
        d_161_valueOrError7_ = out57_
        if not(not((d_161_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(140,20): " + _dafny.string_of(d_161_valueOrError7_))
        d_159_activeResult_ = (d_161_valueOrError7_).Extract()
        if not((((d_159_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.EastBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(142,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_159_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(143,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_162_valueOrError8_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out58_: Wrappers.Result
        out58_ = (d_153_westMrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.WestBranchKey))
        d_162_valueOrError8_ = out58_
        if not(not((d_162_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(145,20): " + _dafny.string_of(d_162_valueOrError8_))
        d_159_activeResult_ = (d_162_valueOrError8_).Extract()
        if not((((d_159_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.WestBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(147,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_159_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(148,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_163_valueOrError9_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out59_: Wrappers.Result
        out59_ = (d_155_eastMrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.EastBranchKey))
        d_163_valueOrError9_ = out59_
        if not(not((d_163_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(150,20): " + _dafny.string_of(d_163_valueOrError9_))
        d_159_activeResult_ = (d_163_valueOrError9_).Extract()
        if not((((d_159_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.EastBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(152,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_159_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(153,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_164_valueOrError10_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out60_: Wrappers.Result
        out60_ = (d_153_westMrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.EastBranchKey))
        d_164_valueOrError10_ = out60_
        if not(not((d_164_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(157,20): " + _dafny.string_of(d_164_valueOrError10_))
        d_159_activeResult_ = (d_164_valueOrError10_).Extract()
        if not((((d_159_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.EastBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(159,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_159_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(160,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_165_valueOrError11_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out61_: Wrappers.Result
        out61_ = (d_155_eastMrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.WestBranchKey))
        d_165_valueOrError11_ = out61_
        if not(not((d_165_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(162,20): " + _dafny.string_of(d_165_valueOrError11_))
        d_159_activeResult_ = (d_165_valueOrError11_).Extract()
        if not((((d_159_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.WestBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(164,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_159_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(165,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_166_badResult_: Wrappers.Result
        out62_: Wrappers.Result
        out62_ = (d_149_westKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.EastBranchKey))
        d_166_badResult_ = out62_
        if not((d_166_badResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(171,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_166_badResult_).error) == (AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.GET__KEY__ARN__DISAGREEMENT))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(172,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out63_: Wrappers.Result
        out63_ = (d_151_eastKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.WestBranchKey))
        d_166_badResult_ = out63_
        if not((d_166_badResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(176,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_166_badResult_).error) == (AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.GET__KEY__ARN__DISAGREEMENT))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(177,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out64_: Wrappers.Result
        out64_ = (d_157_apMrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.WestBranchKey))
        d_166_badResult_ = out64_
        if not((d_166_badResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(183,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_166_badResult_).error).is_ComAmazonawsKms):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(184,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_166_badResult_).error).ComAmazonawsKms).is_Opaque):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(185,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetBranchKeyVersion():
        d_167_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_168_valueOrError0_: Wrappers.Result = None
        out65_: Wrappers.Result
        out65_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_168_valueOrError0_ = out65_
        if not(not((d_168_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(191,21): " + _dafny.string_of(d_168_valueOrError0_))
        d_167_kmsClient_ = (d_168_valueOrError0_).Extract()
        d_169_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_170_valueOrError1_: Wrappers.Result = None
        out66_: Wrappers.Result
        out66_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_170_valueOrError1_ = out66_
        if not(not((d_170_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(192,21): " + _dafny.string_of(d_170_valueOrError1_))
        d_169_ddbClient_ = (d_170_valueOrError1_).Extract()
        d_171_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_171_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_172_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_172_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_171_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_169_ddbClient_), Wrappers.Option_Some(d_167_kmsClient_))
        d_173_keyStore_: KeyStore.KeyStoreClient
        d_174_valueOrError2_: Wrappers.Result = None
        out67_: Wrappers.Result
        out67_ = KeyStore.default__.KeyStore(d_172_keyStoreConfig_)
        d_174_valueOrError2_ = out67_
        if not(not((d_174_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(205,20): " + _dafny.string_of(d_174_valueOrError2_))
        d_173_keyStore_ = (d_174_valueOrError2_).Extract()
        d_175_versionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_176_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out68_: Wrappers.Result
        out68_ = (d_173_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion))
        d_176_valueOrError3_ = out68_
        if not(not((d_176_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(207,25): " + _dafny.string_of(d_176_valueOrError3_))
        d_175_versionResult_ = (d_176_valueOrError3_).Extract()
        d_177_testBytes_: _dafny.Seq
        d_178_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_178_valueOrError4_ = UTF8.default__.Encode(Fixtures.default__.branchKeyIdActiveVersion)
        if not(not((d_178_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(213,21): " + _dafny.string_of(d_178_valueOrError4_))
        d_177_testBytes_ = (d_178_valueOrError4_).Extract()
        if not((((d_175_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(215,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_175_versionResult_).branchKeyMaterials).branchKeyVersion) == (Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes)) and ((Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes) == (d_177_testBytes_))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(216,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_175_versionResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(217,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWithIncorrectKmsKeyArn():
        d_179_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_180_valueOrError0_: Wrappers.Result = None
        out69_: Wrappers.Result
        out69_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_180_valueOrError0_ = out69_
        if not(not((d_180_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(222,21): " + _dafny.string_of(d_180_valueOrError0_))
        d_179_kmsClient_ = (d_180_valueOrError0_).Extract()
        d_181_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_182_valueOrError1_: Wrappers.Result = None
        out70_: Wrappers.Result
        out70_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_182_valueOrError1_ = out70_
        if not(not((d_182_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(223,21): " + _dafny.string_of(d_182_valueOrError1_))
        d_181_ddbClient_ = (d_182_valueOrError1_).Extract()
        d_183_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_183_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_184_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_184_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_183_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_181_ddbClient_), Wrappers.Option_Some(d_179_kmsClient_))
        d_185_keyStore_: KeyStore.KeyStoreClient
        d_186_valueOrError2_: Wrappers.Result = None
        out71_: Wrappers.Result
        out71_ = KeyStore.default__.KeyStore(d_184_keyStoreConfig_)
        d_186_valueOrError2_ = out71_
        if not(not((d_186_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(236,20): " + _dafny.string_of(d_186_valueOrError2_))
        d_185_keyStore_ = (d_186_valueOrError2_).Extract()
        d_187_activeResult_: Wrappers.Result
        out72_: Wrappers.Result
        out72_ = (d_185_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.postalHornBranchKeyId))
        d_187_activeResult_ = out72_
        if not((d_187_activeResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(242,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_187_activeResult_).error) == (AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.GET__KEY__ARN__DISAGREEMENT))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(243,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWrongLogicalKeyStoreName():
        d_188_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_189_valueOrError0_: Wrappers.Result = None
        out73_: Wrappers.Result
        out73_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_189_valueOrError0_ = out73_
        if not(not((d_189_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(247,21): " + _dafny.string_of(d_189_valueOrError0_))
        d_188_kmsClient_ = (d_189_valueOrError0_).Extract()
        d_190_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_191_valueOrError1_: Wrappers.Result = None
        out74_: Wrappers.Result
        out74_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_191_valueOrError1_ = out74_
        if not(not((d_191_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(248,21): " + _dafny.string_of(d_191_valueOrError1_))
        d_190_ddbClient_ = (d_191_valueOrError1_).Extract()
        d_192_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_192_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_193_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_193_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_192_kmsConfig_, default__.incorrectLogicalName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_190_ddbClient_), Wrappers.Option_Some(d_188_kmsClient_))
        d_194_keyStore_: KeyStore.KeyStoreClient
        d_195_valueOrError2_: Wrappers.Result = None
        out75_: Wrappers.Result
        out75_ = KeyStore.default__.KeyStore(d_193_keyStoreConfig_)
        d_195_valueOrError2_ = out75_
        if not(not((d_195_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(261,20): " + _dafny.string_of(d_195_valueOrError2_))
        d_194_keyStore_ = (d_195_valueOrError2_).Extract()
        d_196_activeResult_: Wrappers.Result
        out76_: Wrappers.Result
        out76_ = (d_194_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_196_activeResult_ = out76_
        if not((d_196_activeResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(268,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source4_ = (d_196_activeResult_).error
        unmatched4 = True
        if unmatched4:
            if source4_.is_ComAmazonawsKms:
                d_197_nestedError_ = source4_.ComAmazonawsKms
                unmatched4 = False
                if not((d_197_nestedError_).is_InvalidCiphertextException):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(271,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if unmatched4:
            d_198___v0_ = source4_
            unmatched4 = False
            if not(False):
                raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(272,16): " + _dafny.string_of(_dafny.Seq("Wrong Logical Keystore Name SHOULD Fail with KMS InvalidCiphertextException.")))

    @staticmethod
    def TestGetActiveKeyDoesNotExistFails():
        d_199_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_200_valueOrError0_: Wrappers.Result = None
        out77_: Wrappers.Result
        out77_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_200_valueOrError0_ = out77_
        if not(not((d_200_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(278,21): " + _dafny.string_of(d_200_valueOrError0_))
        d_199_kmsClient_ = (d_200_valueOrError0_).Extract()
        d_201_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_202_valueOrError1_: Wrappers.Result = None
        out78_: Wrappers.Result
        out78_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_202_valueOrError1_ = out78_
        if not(not((d_202_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(279,21): " + _dafny.string_of(d_202_valueOrError1_))
        d_201_ddbClient_ = (d_202_valueOrError1_).Extract()
        d_203_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_203_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_204_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_204_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_203_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_201_ddbClient_), Wrappers.Option_Some(d_199_kmsClient_))
        d_205_keyStore_: KeyStore.KeyStoreClient
        d_206_valueOrError2_: Wrappers.Result = None
        out79_: Wrappers.Result
        out79_ = KeyStore.default__.KeyStore(d_204_keyStoreConfig_)
        d_206_valueOrError2_ = out79_
        if not(not((d_206_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(292,20): " + _dafny.string_of(d_206_valueOrError2_))
        d_205_keyStore_ = (d_206_valueOrError2_).Extract()
        d_207_activeResult_: Wrappers.Result
        out80_: Wrappers.Result
        out80_ = (d_205_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(_dafny.Seq("Robbie")))
        d_207_activeResult_ = out80_
        if not((d_207_activeResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(299,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_207_activeResult_).error) == (AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.NO__CORRESPONDING__BRANCH__KEY))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(300,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWithNoClients():
        d_208_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_208_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_209_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_209_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_208_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_210_keyStore_: KeyStore.KeyStoreClient
        d_211_valueOrError0_: Wrappers.Result = None
        out81_: Wrappers.Result
        out81_ = KeyStore.default__.KeyStore(d_209_keyStoreConfig_)
        d_211_valueOrError0_ = out81_
        if not(not((d_211_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(317,20): " + _dafny.string_of(d_211_valueOrError0_))
        d_210_keyStore_ = (d_211_valueOrError0_).Extract()
        d_212_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_213_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out82_: Wrappers.Result
        out82_ = (d_210_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_213_valueOrError1_ = out82_
        if not(not((d_213_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(319,24): " + _dafny.string_of(d_213_valueOrError1_))
        d_212_activeResult_ = (d_213_valueOrError1_).Extract()
        if not((len(((d_212_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(324,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def incorrectLogicalName(instance):
        return _dafny.Seq("MySuperAwesomeTableName")
