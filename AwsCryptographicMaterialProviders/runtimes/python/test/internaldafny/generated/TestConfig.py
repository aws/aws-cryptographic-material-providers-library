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

# Module: TestConfig

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestInvalidKmsKeyArnConfig():
        d_122_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_123_valueOrError0_: Wrappers.Result = None
        out43_: Wrappers.Result
        out43_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_123_valueOrError0_ = out43_
        if not(not((d_123_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(19,21): " + _dafny.string_of(d_123_valueOrError0_))
        d_122_kmsClient_ = (d_123_valueOrError0_).Extract()
        d_124_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_125_valueOrError1_: Wrappers.Result = None
        out44_: Wrappers.Result
        out44_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_125_valueOrError1_ = out44_
        if not(not((d_125_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(20,21): " + _dafny.string_of(d_125_valueOrError1_))
        d_124_ddbClient_ = (d_125_valueOrError1_).Extract()
        d_126_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_126_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyId)
        d_127_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_127_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_126_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_124_ddbClient_), Wrappers.Option_Some(d_122_kmsClient_))
        d_128_keyStore_: Wrappers.Result
        out45_: Wrappers.Result
        out45_ = KeyStore.default__.KeyStore(d_127_keyStoreConfig_)
        d_128_keyStore_ = out45_
        if not((d_128_keyStore_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source6_ = (d_128_keyStore_).error
        unmatched6 = True
        if unmatched6:
            if source6_.is_KeyStoreException:
                d_129_message_ = source6_.message
                unmatched6 = False
                if not((len(d_129_message_)) > (len(KeyStoreErrorMessages.default__.KMS__CONFIG__KMS__ARN__INVALID))):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(37,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                if not((_dafny.Seq((d_129_message_)[:len(KeyStoreErrorMessages.default__.KMS__CONFIG__KMS__ARN__INVALID):])) == (KeyStoreErrorMessages.default__.KMS__CONFIG__KMS__ARN__INVALID)):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(38,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if unmatched6:
            unmatched6 = False
            if not(False):
                raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(39,16): " + _dafny.string_of(_dafny.Seq("Invalid KMS Key ARN should fail Key Store Construction")))

    @staticmethod
    def TestInvalidKmsKeyArnAliasConfig():
        d_130_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_131_valueOrError0_: Wrappers.Result = None
        out46_: Wrappers.Result
        out46_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_131_valueOrError0_ = out46_
        if not(not((d_131_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(47,21): " + _dafny.string_of(d_131_valueOrError0_))
        d_130_kmsClient_ = (d_131_valueOrError0_).Extract()
        d_132_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_133_valueOrError1_: Wrappers.Result = None
        out47_: Wrappers.Result
        out47_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_133_valueOrError1_ = out47_
        if not(not((d_133_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(48,21): " + _dafny.string_of(d_133_valueOrError1_))
        d_132_ddbClient_ = (d_133_valueOrError1_).Extract()
        d_134_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_134_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.kmsKeyAlias)
        d_135_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_135_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_134_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_132_ddbClient_), Wrappers.Option_Some(d_130_kmsClient_))
        d_136_keyStore_: Wrappers.Result
        out48_: Wrappers.Result
        out48_ = KeyStore.default__.KeyStore(d_135_keyStoreConfig_)
        d_136_keyStore_ = out48_
        if not((d_136_keyStore_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source7_ = (d_136_keyStore_).error
        unmatched7 = True
        if unmatched7:
            if source7_.is_KeyStoreException:
                d_137_message_ = source7_.message
                unmatched7 = False
                if not((len(d_137_message_)) >= (len(KeyStoreErrorMessages.default__.ALIAS__NOT__ALLOWED))):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(65,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                if not((_dafny.Seq((d_137_message_)[:len(KeyStoreErrorMessages.default__.ALIAS__NOT__ALLOWED):])) == (KeyStoreErrorMessages.default__.ALIAS__NOT__ALLOWED)):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(66,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if unmatched7:
            unmatched7 = False
            if not(False):
                raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(67,16): " + _dafny.string_of(_dafny.Seq("Alias should fail Key Store Construction")))

    @staticmethod
    def TestValidConfig():
        d_138_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_139_valueOrError0_: Wrappers.Result = None
        out49_: Wrappers.Result
        out49_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_139_valueOrError0_ = out49_
        if not(not((d_139_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(73,21): " + _dafny.string_of(d_139_valueOrError0_))
        d_138_kmsClient_ = (d_139_valueOrError0_).Extract()
        d_140_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_141_valueOrError1_: Wrappers.Result = None
        out50_: Wrappers.Result
        out50_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_141_valueOrError1_ = out50_
        if not(not((d_141_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(74,21): " + _dafny.string_of(d_141_valueOrError1_))
        d_140_ddbClient_ = (d_141_valueOrError1_).Extract()
        d_142_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_142_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_143_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_143_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_142_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_140_ddbClient_), Wrappers.Option_Some(d_138_kmsClient_))
        d_144_keyStore_: Wrappers.Result
        out51_: Wrappers.Result
        out51_ = KeyStore.default__.KeyStore(d_143_keyStoreConfig_)
        d_144_keyStore_ = out51_
        if not((d_144_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(88,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_145_conf_: AwsCryptographyKeyStoreTypes.GetKeyStoreInfoOutput
        d_146_valueOrError2_: Wrappers.Result = None
        out52_: Wrappers.Result
        out52_ = ((d_144_keyStore_).value).GetKeyStoreInfo()
        d_146_valueOrError2_ = out52_
        if not(not((d_146_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(90,16): " + _dafny.string_of(d_146_valueOrError2_))
        d_145_conf_ = (d_146_valueOrError2_).Extract()
        d_147_idByteUUID_: _dafny.Seq
        d_148_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_148_valueOrError3_ = UUID.default__.ToByteArray((d_145_conf_).keyStoreId)
        if not(not((d_148_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(95,22): " + _dafny.string_of(d_148_valueOrError3_))
        d_147_idByteUUID_ = (d_148_valueOrError3_).Extract()
        d_149_idRoundTrip_: _dafny.Seq
        d_150_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_150_valueOrError4_ = UUID.default__.FromByteArray(d_147_idByteUUID_)
        if not(not((d_150_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(96,23): " + _dafny.string_of(d_150_valueOrError4_))
        d_149_idRoundTrip_ = (d_150_valueOrError4_).Extract()
        if not((d_149_idRoundTrip_) == ((d_145_conf_).keyStoreId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(97,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_145_conf_).keyStoreName) == (Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(99,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_145_conf_).logicalKeyStoreName) == (Fixtures.default__.logicalKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(100,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_145_conf_).kmsConfiguration) == (d_142_kmsConfig_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestValidConfigNoClients():
        d_151_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_152_valueOrError0_: Wrappers.Result = None
        out53_: Wrappers.Result
        out53_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_152_valueOrError0_ = out53_
        if not(not((d_152_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(106,21): " + _dafny.string_of(d_152_valueOrError0_))
        d_151_kmsClient_ = (d_152_valueOrError0_).Extract()
        d_153_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_154_valueOrError1_: Wrappers.Result = None
        out54_: Wrappers.Result
        out54_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_154_valueOrError1_ = out54_
        if not(not((d_154_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(107,21): " + _dafny.string_of(d_154_valueOrError1_))
        d_153_ddbClient_ = (d_154_valueOrError1_).Extract()
        d_155_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_155_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_156_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_156_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_155_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_153_ddbClient_), Wrappers.Option_None())
        d_157_keyStore_: Wrappers.Result
        out55_: Wrappers.Result
        out55_ = KeyStore.default__.KeyStore(d_156_keyStoreConfig_)
        d_157_keyStore_ = out55_
        if not((d_157_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(134,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_156_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_155_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_151_kmsClient_))
        out56_: Wrappers.Result
        out56_ = KeyStore.default__.KeyStore(d_156_keyStoreConfig_)
        d_157_keyStore_ = out56_
        if not((d_157_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(160,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_156_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_155_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        out57_: Wrappers.Result
        out57_ = KeyStore.default__.KeyStore(d_156_keyStoreConfig_)
        d_157_keyStore_ = out57_
        if not((d_157_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(193,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

