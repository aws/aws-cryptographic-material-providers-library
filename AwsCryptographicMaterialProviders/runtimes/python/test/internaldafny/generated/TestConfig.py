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

# Module: TestConfig

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestInvalidKmsKeyArnConfig():
        d_84_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_85_valueOrError0_: Wrappers.Result = None
        out27_: Wrappers.Result
        out27_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_85_valueOrError0_ = out27_
        if not(not((d_85_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(19,21): " + _dafny.string_of(d_85_valueOrError0_))
        d_84_kmsClient_ = (d_85_valueOrError0_).Extract()
        d_86_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_87_valueOrError1_: Wrappers.Result = None
        out28_: Wrappers.Result
        out28_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_87_valueOrError1_ = out28_
        if not(not((d_87_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(20,21): " + _dafny.string_of(d_87_valueOrError1_))
        d_86_ddbClient_ = (d_87_valueOrError1_).Extract()
        d_88_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_88_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyId)
        d_89_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_89_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_88_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_86_ddbClient_), Wrappers.Option_Some(d_84_kmsClient_))
        d_90_keyStore_: Wrappers.Result
        out29_: Wrappers.Result
        out29_ = KeyStore.default__.KeyStore(d_89_keyStoreConfig_)
        d_90_keyStore_ = out29_
        if not((d_90_keyStore_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source2_ = (d_90_keyStore_).error
        unmatched2 = True
        if unmatched2:
            if source2_.is_KeyStoreException:
                d_91_message_ = source2_.message
                unmatched2 = False
                if not((len(d_91_message_)) > (len(KeyStoreErrorMessages.default__.KMS__CONFIG__KMS__ARN__INVALID))):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(37,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                if not((_dafny.Seq((d_91_message_)[:len(KeyStoreErrorMessages.default__.KMS__CONFIG__KMS__ARN__INVALID):])) == (KeyStoreErrorMessages.default__.KMS__CONFIG__KMS__ARN__INVALID)):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(38,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if unmatched2:
            d_92___v0_ = source2_
            unmatched2 = False
            if not(False):
                raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(39,16): " + _dafny.string_of(_dafny.Seq("Invalid KMS Key ARN should fail Key Store Construction")))

    @staticmethod
    def TestInvalidKmsKeyArnAliasConfig():
        d_93_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_94_valueOrError0_: Wrappers.Result = None
        out30_: Wrappers.Result
        out30_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_94_valueOrError0_ = out30_
        if not(not((d_94_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(47,21): " + _dafny.string_of(d_94_valueOrError0_))
        d_93_kmsClient_ = (d_94_valueOrError0_).Extract()
        d_95_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_96_valueOrError1_: Wrappers.Result = None
        out31_: Wrappers.Result
        out31_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_96_valueOrError1_ = out31_
        if not(not((d_96_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(48,21): " + _dafny.string_of(d_96_valueOrError1_))
        d_95_ddbClient_ = (d_96_valueOrError1_).Extract()
        d_97_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_97_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.kmsKeyAlias)
        d_98_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_98_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_97_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_95_ddbClient_), Wrappers.Option_Some(d_93_kmsClient_))
        d_99_keyStore_: Wrappers.Result
        out32_: Wrappers.Result
        out32_ = KeyStore.default__.KeyStore(d_98_keyStoreConfig_)
        d_99_keyStore_ = out32_
        if not((d_99_keyStore_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source3_ = (d_99_keyStore_).error
        unmatched3 = True
        if unmatched3:
            if source3_.is_KeyStoreException:
                d_100_message_ = source3_.message
                unmatched3 = False
                if not((len(d_100_message_)) >= (len(KeyStoreErrorMessages.default__.ALIAS__NOT__ALLOWED))):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(65,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                if not((_dafny.Seq((d_100_message_)[:len(KeyStoreErrorMessages.default__.ALIAS__NOT__ALLOWED):])) == (KeyStoreErrorMessages.default__.ALIAS__NOT__ALLOWED)):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(66,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if unmatched3:
            d_101___v1_ = source3_
            unmatched3 = False
            if not(False):
                raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(67,16): " + _dafny.string_of(_dafny.Seq("Alias should fail Key Store Construction")))

    @staticmethod
    def TestValidConfig():
        d_102_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_103_valueOrError0_: Wrappers.Result = None
        out33_: Wrappers.Result
        out33_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_103_valueOrError0_ = out33_
        if not(not((d_103_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(73,21): " + _dafny.string_of(d_103_valueOrError0_))
        d_102_kmsClient_ = (d_103_valueOrError0_).Extract()
        d_104_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_105_valueOrError1_: Wrappers.Result = None
        out34_: Wrappers.Result
        out34_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_105_valueOrError1_ = out34_
        if not(not((d_105_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(74,21): " + _dafny.string_of(d_105_valueOrError1_))
        d_104_ddbClient_ = (d_105_valueOrError1_).Extract()
        d_106_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_106_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_107_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_107_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_106_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_104_ddbClient_), Wrappers.Option_Some(d_102_kmsClient_))
        d_108_keyStore_: Wrappers.Result
        out35_: Wrappers.Result
        out35_ = KeyStore.default__.KeyStore(d_107_keyStoreConfig_)
        d_108_keyStore_ = out35_
        if not((d_108_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(88,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_109_conf_: AwsCryptographyKeyStoreTypes.GetKeyStoreInfoOutput
        d_110_valueOrError2_: Wrappers.Result = None
        out36_: Wrappers.Result
        out36_ = ((d_108_keyStore_).value).GetKeyStoreInfo()
        d_110_valueOrError2_ = out36_
        if not(not((d_110_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(90,16): " + _dafny.string_of(d_110_valueOrError2_))
        d_109_conf_ = (d_110_valueOrError2_).Extract()
        d_111_idByteUUID_: _dafny.Seq
        d_112_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_112_valueOrError3_ = UUID.default__.ToByteArray((d_109_conf_).keyStoreId)
        if not(not((d_112_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(95,22): " + _dafny.string_of(d_112_valueOrError3_))
        d_111_idByteUUID_ = (d_112_valueOrError3_).Extract()
        d_113_idRoundTrip_: _dafny.Seq
        d_114_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_114_valueOrError4_ = UUID.default__.FromByteArray(d_111_idByteUUID_)
        if not(not((d_114_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(96,23): " + _dafny.string_of(d_114_valueOrError4_))
        d_113_idRoundTrip_ = (d_114_valueOrError4_).Extract()
        if not((d_113_idRoundTrip_) == ((d_109_conf_).keyStoreId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(97,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_109_conf_).keyStoreName) == (Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(99,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_109_conf_).logicalKeyStoreName) == (Fixtures.default__.logicalKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(100,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_109_conf_).kmsConfiguration) == (d_106_kmsConfig_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestValidConfigNoClients():
        d_115_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_116_valueOrError0_: Wrappers.Result = None
        out37_: Wrappers.Result
        out37_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_116_valueOrError0_ = out37_
        if not(not((d_116_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(106,21): " + _dafny.string_of(d_116_valueOrError0_))
        d_115_kmsClient_ = (d_116_valueOrError0_).Extract()
        d_117_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_118_valueOrError1_: Wrappers.Result = None
        out38_: Wrappers.Result
        out38_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_118_valueOrError1_ = out38_
        if not(not((d_118_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(107,21): " + _dafny.string_of(d_118_valueOrError1_))
        d_117_ddbClient_ = (d_118_valueOrError1_).Extract()
        d_119_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_119_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_120_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_120_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_119_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_117_ddbClient_), Wrappers.Option_None())
        d_121_keyStore_: Wrappers.Result
        out39_: Wrappers.Result
        out39_ = KeyStore.default__.KeyStore(d_120_keyStoreConfig_)
        d_121_keyStore_ = out39_
        if not((d_121_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(134,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_120_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_119_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_115_kmsClient_))
        out40_: Wrappers.Result
        out40_ = KeyStore.default__.KeyStore(d_120_keyStoreConfig_)
        d_121_keyStore_ = out40_
        if not((d_121_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(160,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_120_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_119_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        out41_: Wrappers.Result
        out41_ = KeyStore.default__.KeyStore(d_120_keyStoreConfig_)
        d_121_keyStore_ = out41_
        if not((d_121_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(193,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

