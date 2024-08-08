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
import TestDiscoveryGetKeys as TestDiscoveryGetKeys
import TestConfig as TestConfig

# Module: TestGetKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestGetBeaconKey():
        d_158_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_159_valueOrError0_: Wrappers.Result = None
        out58_: Wrappers.Result
        out58_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_159_valueOrError0_ = out58_
        if not(not((d_159_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(23,21): " + _dafny.string_of(d_159_valueOrError0_))
        d_158_kmsClient_ = (d_159_valueOrError0_).Extract()
        d_160_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_161_valueOrError1_: Wrappers.Result = None
        out59_: Wrappers.Result
        out59_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_161_valueOrError1_ = out59_
        if not(not((d_161_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(24,21): " + _dafny.string_of(d_161_valueOrError1_))
        d_160_ddbClient_ = (d_161_valueOrError1_).Extract()
        d_162_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_162_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_163_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_163_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_162_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_160_ddbClient_), Wrappers.Option_Some(d_158_kmsClient_))
        d_164_keyStore_: KeyStore.KeyStoreClient
        d_165_valueOrError2_: Wrappers.Result = None
        out60_: Wrappers.Result
        out60_ = KeyStore.default__.KeyStore(d_163_keyStoreConfig_)
        d_165_valueOrError2_ = out60_
        if not(not((d_165_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(37,20): " + _dafny.string_of(d_165_valueOrError2_))
        d_164_keyStore_ = (d_165_valueOrError2_).Extract()
        d_166_beaconKeyResult_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_167_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out61_: Wrappers.Result
        out61_ = (d_164_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.branchKeyId))
        d_167_valueOrError3_ = out61_
        if not(not((d_167_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(39,27): " + _dafny.string_of(d_167_valueOrError3_))
        d_166_beaconKeyResult_ = (d_167_valueOrError3_).Extract()
        if not((((d_166_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(43,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_166_beaconKeyResult_).beaconKeyMaterials).beaconKey).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((((d_166_beaconKeyResult_).beaconKeyMaterials).beaconKey).value)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(45,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKey():
        d_168_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_169_valueOrError0_: Wrappers.Result = None
        out62_: Wrappers.Result
        out62_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_169_valueOrError0_ = out62_
        if not(not((d_169_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(50,21): " + _dafny.string_of(d_169_valueOrError0_))
        d_168_kmsClient_ = (d_169_valueOrError0_).Extract()
        d_170_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_171_valueOrError1_: Wrappers.Result = None
        out63_: Wrappers.Result
        out63_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_171_valueOrError1_ = out63_
        if not(not((d_171_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(51,21): " + _dafny.string_of(d_171_valueOrError1_))
        d_170_ddbClient_ = (d_171_valueOrError1_).Extract()
        d_172_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_172_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_173_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_173_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_172_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_170_ddbClient_), Wrappers.Option_Some(d_168_kmsClient_))
        d_174_keyStore_: KeyStore.KeyStoreClient
        d_175_valueOrError2_: Wrappers.Result = None
        out64_: Wrappers.Result
        out64_ = KeyStore.default__.KeyStore(d_173_keyStoreConfig_)
        d_175_valueOrError2_ = out64_
        if not(not((d_175_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(64,20): " + _dafny.string_of(d_175_valueOrError2_))
        d_174_keyStore_ = (d_175_valueOrError2_).Extract()
        d_176_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_177_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out65_: Wrappers.Result
        out65_ = (d_174_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_177_valueOrError3_ = out65_
        if not(not((d_177_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(66,24): " + _dafny.string_of(d_177_valueOrError3_))
        d_176_activeResult_ = (d_177_valueOrError3_).Extract()
        if not((((d_176_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(71,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_176_activeResult_).branchKeyMaterials).branchKeyVersion) == (Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_176_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(73,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveMrkKey():
        d_178_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_179_valueOrError0_: Wrappers.Result = None
        out66_: Wrappers.Result
        out66_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_179_valueOrError0_ = out66_
        if not(not((d_179_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(78,21): " + _dafny.string_of(d_179_valueOrError0_))
        d_178_ddbClient_ = (d_179_valueOrError0_).Extract()
        d_180_eastKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_180_eastKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsConfigEast, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_178_ddbClient_), Wrappers.Option_None())
        d_181_westKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_181_westKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsConfigWest, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_178_ddbClient_), Wrappers.Option_None())
        d_182_eastMrkKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_182_eastMrkKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsMrkConfigEast, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_178_ddbClient_), Wrappers.Option_None())
        d_183_westMrkKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_183_westMrkKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsMrkConfigWest, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_178_ddbClient_), Wrappers.Option_None())
        d_184_apMrkKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_184_apMrkKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsMrkConfigAP, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_178_ddbClient_), Wrappers.Option_None())
        d_185_westKeyStore_: KeyStore.KeyStoreClient
        d_186_valueOrError1_: Wrappers.Result = None
        out67_: Wrappers.Result
        out67_ = KeyStore.default__.KeyStore(d_181_westKeyStoreConfig_)
        d_186_valueOrError1_ = out67_
        if not(not((d_186_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(127,24): " + _dafny.string_of(d_186_valueOrError1_))
        d_185_westKeyStore_ = (d_186_valueOrError1_).Extract()
        d_187_eastKeyStore_: KeyStore.KeyStoreClient
        d_188_valueOrError2_: Wrappers.Result = None
        out68_: Wrappers.Result
        out68_ = KeyStore.default__.KeyStore(d_180_eastKeyStoreConfig_)
        d_188_valueOrError2_ = out68_
        if not(not((d_188_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(128,24): " + _dafny.string_of(d_188_valueOrError2_))
        d_187_eastKeyStore_ = (d_188_valueOrError2_).Extract()
        d_189_westMrkKeyStore_: KeyStore.KeyStoreClient
        d_190_valueOrError3_: Wrappers.Result = None
        out69_: Wrappers.Result
        out69_ = KeyStore.default__.KeyStore(d_183_westMrkKeyStoreConfig_)
        d_190_valueOrError3_ = out69_
        if not(not((d_190_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(129,27): " + _dafny.string_of(d_190_valueOrError3_))
        d_189_westMrkKeyStore_ = (d_190_valueOrError3_).Extract()
        d_191_eastMrkKeyStore_: KeyStore.KeyStoreClient
        d_192_valueOrError4_: Wrappers.Result = None
        out70_: Wrappers.Result
        out70_ = KeyStore.default__.KeyStore(d_182_eastMrkKeyStoreConfig_)
        d_192_valueOrError4_ = out70_
        if not(not((d_192_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(130,27): " + _dafny.string_of(d_192_valueOrError4_))
        d_191_eastMrkKeyStore_ = (d_192_valueOrError4_).Extract()
        d_193_apMrkKeyStore_: KeyStore.KeyStoreClient
        d_194_valueOrError5_: Wrappers.Result = None
        out71_: Wrappers.Result
        out71_ = KeyStore.default__.KeyStore(d_184_apMrkKeyStoreConfig_)
        d_194_valueOrError5_ = out71_
        if not(not((d_194_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(131,25): " + _dafny.string_of(d_194_valueOrError5_))
        d_193_apMrkKeyStore_ = (d_194_valueOrError5_).Extract()
        d_195_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_196_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out72_: Wrappers.Result
        out72_ = (d_185_westKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.WestBranchKey))
        d_196_valueOrError6_ = out72_
        if not(not((d_196_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(135,24): " + _dafny.string_of(d_196_valueOrError6_))
        d_195_activeResult_ = (d_196_valueOrError6_).Extract()
        if not((((d_195_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.WestBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(137,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_195_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(138,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_197_valueOrError7_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out73_: Wrappers.Result
        out73_ = (d_187_eastKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.EastBranchKey))
        d_197_valueOrError7_ = out73_
        if not(not((d_197_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(140,20): " + _dafny.string_of(d_197_valueOrError7_))
        d_195_activeResult_ = (d_197_valueOrError7_).Extract()
        if not((((d_195_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.EastBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(142,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_195_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(143,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_198_valueOrError8_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out74_: Wrappers.Result
        out74_ = (d_189_westMrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.WestBranchKey))
        d_198_valueOrError8_ = out74_
        if not(not((d_198_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(145,20): " + _dafny.string_of(d_198_valueOrError8_))
        d_195_activeResult_ = (d_198_valueOrError8_).Extract()
        if not((((d_195_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.WestBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(147,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_195_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(148,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_199_valueOrError9_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out75_: Wrappers.Result
        out75_ = (d_191_eastMrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.EastBranchKey))
        d_199_valueOrError9_ = out75_
        if not(not((d_199_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(150,20): " + _dafny.string_of(d_199_valueOrError9_))
        d_195_activeResult_ = (d_199_valueOrError9_).Extract()
        if not((((d_195_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.EastBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(152,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_195_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(153,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_200_valueOrError10_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out76_: Wrappers.Result
        out76_ = (d_189_westMrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.EastBranchKey))
        d_200_valueOrError10_ = out76_
        if not(not((d_200_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(157,20): " + _dafny.string_of(d_200_valueOrError10_))
        d_195_activeResult_ = (d_200_valueOrError10_).Extract()
        if not((((d_195_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.EastBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(159,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_195_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(160,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_201_valueOrError11_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out77_: Wrappers.Result
        out77_ = (d_191_eastMrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.WestBranchKey))
        d_201_valueOrError11_ = out77_
        if not(not((d_201_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(162,20): " + _dafny.string_of(d_201_valueOrError11_))
        d_195_activeResult_ = (d_201_valueOrError11_).Extract()
        if not((((d_195_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.WestBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(164,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_195_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(165,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_202_badResult_: Wrappers.Result
        out78_: Wrappers.Result
        out78_ = (d_185_westKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.EastBranchKey))
        d_202_badResult_ = out78_
        if not((d_202_badResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(171,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_202_badResult_).error) == (AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.GET__KEY__ARN__DISAGREEMENT))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(172,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out79_: Wrappers.Result
        out79_ = (d_187_eastKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.WestBranchKey))
        d_202_badResult_ = out79_
        if not((d_202_badResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(176,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_202_badResult_).error) == (AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.GET__KEY__ARN__DISAGREEMENT))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(177,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out80_: Wrappers.Result
        out80_ = (d_193_apMrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.WestBranchKey))
        d_202_badResult_ = out80_
        if not((d_202_badResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(183,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_202_badResult_).error).is_ComAmazonawsKms):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(184,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_202_badResult_).error).ComAmazonawsKms).is_Opaque):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(185,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetBranchKeyVersion():
        d_203_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_204_valueOrError0_: Wrappers.Result = None
        out81_: Wrappers.Result
        out81_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_204_valueOrError0_ = out81_
        if not(not((d_204_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(191,21): " + _dafny.string_of(d_204_valueOrError0_))
        d_203_kmsClient_ = (d_204_valueOrError0_).Extract()
        d_205_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_206_valueOrError1_: Wrappers.Result = None
        out82_: Wrappers.Result
        out82_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_206_valueOrError1_ = out82_
        if not(not((d_206_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(192,21): " + _dafny.string_of(d_206_valueOrError1_))
        d_205_ddbClient_ = (d_206_valueOrError1_).Extract()
        d_207_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_207_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_208_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_208_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_207_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_205_ddbClient_), Wrappers.Option_Some(d_203_kmsClient_))
        d_209_keyStore_: KeyStore.KeyStoreClient
        d_210_valueOrError2_: Wrappers.Result = None
        out83_: Wrappers.Result
        out83_ = KeyStore.default__.KeyStore(d_208_keyStoreConfig_)
        d_210_valueOrError2_ = out83_
        if not(not((d_210_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(205,20): " + _dafny.string_of(d_210_valueOrError2_))
        d_209_keyStore_ = (d_210_valueOrError2_).Extract()
        d_211_versionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_212_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out84_: Wrappers.Result
        out84_ = (d_209_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion))
        d_212_valueOrError3_ = out84_
        if not(not((d_212_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(207,25): " + _dafny.string_of(d_212_valueOrError3_))
        d_211_versionResult_ = (d_212_valueOrError3_).Extract()
        d_213_testBytes_: _dafny.Seq
        d_214_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_214_valueOrError4_ = UTF8.default__.Encode(Fixtures.default__.branchKeyIdActiveVersion)
        if not(not((d_214_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(213,21): " + _dafny.string_of(d_214_valueOrError4_))
        d_213_testBytes_ = (d_214_valueOrError4_).Extract()
        if not((((d_211_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(215,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_211_versionResult_).branchKeyMaterials).branchKeyVersion) == (Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes)) and ((Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes) == (d_213_testBytes_))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(216,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_211_versionResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(217,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWithIncorrectKmsKeyArn():
        d_215_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_216_valueOrError0_: Wrappers.Result = None
        out85_: Wrappers.Result
        out85_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_216_valueOrError0_ = out85_
        if not(not((d_216_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(222,21): " + _dafny.string_of(d_216_valueOrError0_))
        d_215_kmsClient_ = (d_216_valueOrError0_).Extract()
        d_217_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_218_valueOrError1_: Wrappers.Result = None
        out86_: Wrappers.Result
        out86_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_218_valueOrError1_ = out86_
        if not(not((d_218_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(223,21): " + _dafny.string_of(d_218_valueOrError1_))
        d_217_ddbClient_ = (d_218_valueOrError1_).Extract()
        d_219_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_219_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_220_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_220_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_219_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_217_ddbClient_), Wrappers.Option_Some(d_215_kmsClient_))
        d_221_keyStore_: KeyStore.KeyStoreClient
        d_222_valueOrError2_: Wrappers.Result = None
        out87_: Wrappers.Result
        out87_ = KeyStore.default__.KeyStore(d_220_keyStoreConfig_)
        d_222_valueOrError2_ = out87_
        if not(not((d_222_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(236,20): " + _dafny.string_of(d_222_valueOrError2_))
        d_221_keyStore_ = (d_222_valueOrError2_).Extract()
        d_223_activeResult_: Wrappers.Result
        out88_: Wrappers.Result
        out88_ = (d_221_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.postalHornBranchKeyId))
        d_223_activeResult_ = out88_
        if not((d_223_activeResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(242,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_223_activeResult_).error) == (AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.GET__KEY__ARN__DISAGREEMENT))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(243,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWrongLogicalKeyStoreName():
        d_224_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_225_valueOrError0_: Wrappers.Result = None
        out89_: Wrappers.Result
        out89_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_225_valueOrError0_ = out89_
        if not(not((d_225_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(247,21): " + _dafny.string_of(d_225_valueOrError0_))
        d_224_kmsClient_ = (d_225_valueOrError0_).Extract()
        d_226_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_227_valueOrError1_: Wrappers.Result = None
        out90_: Wrappers.Result
        out90_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_227_valueOrError1_ = out90_
        if not(not((d_227_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(248,21): " + _dafny.string_of(d_227_valueOrError1_))
        d_226_ddbClient_ = (d_227_valueOrError1_).Extract()
        d_228_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_228_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_229_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_229_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_228_kmsConfig_, default__.incorrectLogicalName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_226_ddbClient_), Wrappers.Option_Some(d_224_kmsClient_))
        d_230_keyStore_: KeyStore.KeyStoreClient
        d_231_valueOrError2_: Wrappers.Result = None
        out91_: Wrappers.Result
        out91_ = KeyStore.default__.KeyStore(d_229_keyStoreConfig_)
        d_231_valueOrError2_ = out91_
        if not(not((d_231_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(261,20): " + _dafny.string_of(d_231_valueOrError2_))
        d_230_keyStore_ = (d_231_valueOrError2_).Extract()
        d_232_activeResult_: Wrappers.Result
        out92_: Wrappers.Result
        out92_ = (d_230_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_232_activeResult_ = out92_
        if not((d_232_activeResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(268,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source8_ = (d_232_activeResult_).error
        unmatched8 = True
        if unmatched8:
            if source8_.is_ComAmazonawsKms:
                d_233_nestedError_ = source8_.ComAmazonawsKms
                unmatched8 = False
                if not((d_233_nestedError_).is_InvalidCiphertextException):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(271,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if unmatched8:
            unmatched8 = False
            if not(False):
                raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(272,16): " + _dafny.string_of(_dafny.Seq("Wrong Logical Keystore Name SHOULD Fail with KMS InvalidCiphertextException.")))

    @staticmethod
    def TestGetActiveKeyDoesNotExistFails():
        d_234_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_235_valueOrError0_: Wrappers.Result = None
        out93_: Wrappers.Result
        out93_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_235_valueOrError0_ = out93_
        if not(not((d_235_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(278,21): " + _dafny.string_of(d_235_valueOrError0_))
        d_234_kmsClient_ = (d_235_valueOrError0_).Extract()
        d_236_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_237_valueOrError1_: Wrappers.Result = None
        out94_: Wrappers.Result
        out94_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_237_valueOrError1_ = out94_
        if not(not((d_237_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(279,21): " + _dafny.string_of(d_237_valueOrError1_))
        d_236_ddbClient_ = (d_237_valueOrError1_).Extract()
        d_238_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_238_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_239_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_239_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_238_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_236_ddbClient_), Wrappers.Option_Some(d_234_kmsClient_))
        d_240_keyStore_: KeyStore.KeyStoreClient
        d_241_valueOrError2_: Wrappers.Result = None
        out95_: Wrappers.Result
        out95_ = KeyStore.default__.KeyStore(d_239_keyStoreConfig_)
        d_241_valueOrError2_ = out95_
        if not(not((d_241_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(292,20): " + _dafny.string_of(d_241_valueOrError2_))
        d_240_keyStore_ = (d_241_valueOrError2_).Extract()
        d_242_activeResult_: Wrappers.Result
        out96_: Wrappers.Result
        out96_ = (d_240_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(_dafny.Seq("Robbie")))
        d_242_activeResult_ = out96_
        if not((d_242_activeResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(299,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_242_activeResult_).error) == (AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.NO__CORRESPONDING__BRANCH__KEY))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(300,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWithNoClients():
        d_243_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_243_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_244_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_244_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_243_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_245_keyStore_: KeyStore.KeyStoreClient
        d_246_valueOrError0_: Wrappers.Result = None
        out97_: Wrappers.Result
        out97_ = KeyStore.default__.KeyStore(d_244_keyStoreConfig_)
        d_246_valueOrError0_ = out97_
        if not(not((d_246_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(317,20): " + _dafny.string_of(d_246_valueOrError0_))
        d_245_keyStore_ = (d_246_valueOrError0_).Extract()
        d_247_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_248_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out98_: Wrappers.Result
        out98_ = (d_245_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_248_valueOrError1_ = out98_
        if not(not((d_248_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(319,24): " + _dafny.string_of(d_248_valueOrError1_))
        d_247_activeResult_ = (d_248_valueOrError1_).Extract()
        if not((len(((d_247_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(324,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def incorrectLogicalName(instance):
        return _dafny.Seq("MySuperAwesomeTableName")
