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
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import standard_library.internaldafny.generated.Actions as Actions
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
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
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws as Com_Amazonaws
import com_amazonaws_dynamodb.internaldafny.generated.Com as Com
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
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography as Aws_Cryptography
import aws_cryptography_primitives.internaldafny.generated.Aws as Aws
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
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

# Module: TestConfig

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestInvalidKmsKeyArnConfig():
        d_10_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_11_valueOrError0_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_11_valueOrError0_ = out4_
        if not(not((d_11_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(18,21): " + _dafny.string_of(d_11_valueOrError0_))
        d_10_kmsClient_ = (d_11_valueOrError0_).Extract()
        d_12_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_13_valueOrError1_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_13_valueOrError1_ = out5_
        if not(not((d_13_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(19,21): " + _dafny.string_of(d_13_valueOrError1_))
        d_12_ddbClient_ = (d_13_valueOrError1_).Extract()
        d_14_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_14_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyId)
        d_15_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_15_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_14_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_12_ddbClient_), Wrappers.Option_Some(d_10_kmsClient_))
        d_16_keyStore_: Wrappers.Result
        out6_: Wrappers.Result
        out6_ = KeyStore.default__.KeyStore(d_15_keyStoreConfig_)
        d_16_keyStore_ = out6_
        if not((d_16_keyStore_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(33,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_16_keyStore_).error) == (AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Invalid AWS KMS Key Arn")))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestValidConfig():
        d_17_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_18_valueOrError0_: Wrappers.Result = None
        out7_: Wrappers.Result
        out7_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_18_valueOrError0_ = out7_
        if not(not((d_18_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(38,21): " + _dafny.string_of(d_18_valueOrError0_))
        d_17_kmsClient_ = (d_18_valueOrError0_).Extract()
        d_19_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_20_valueOrError1_: Wrappers.Result = None
        out8_: Wrappers.Result
        out8_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_20_valueOrError1_ = out8_
        if not(not((d_20_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(39,21): " + _dafny.string_of(d_20_valueOrError1_))
        d_19_ddbClient_ = (d_20_valueOrError1_).Extract()
        d_21_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_21_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_22_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_22_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_21_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_19_ddbClient_), Wrappers.Option_Some(d_17_kmsClient_))
        d_23_keyStore_: Wrappers.Result
        out9_: Wrappers.Result
        out9_ = KeyStore.default__.KeyStore(d_22_keyStoreConfig_)
        d_23_keyStore_ = out9_
        if not((d_23_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(53,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_24_conf_: AwsCryptographyKeyStoreTypes.GetKeyStoreInfoOutput
        d_25_valueOrError2_: Wrappers.Result = None
        out10_: Wrappers.Result
        out10_ = ((d_23_keyStore_).value).GetKeyStoreInfo()
        d_25_valueOrError2_ = out10_
        if not(not((d_25_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(55,16): " + _dafny.string_of(d_25_valueOrError2_))
        d_24_conf_ = (d_25_valueOrError2_).Extract()
        d_26_idByteUUID_: _dafny.Seq
        d_27_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_27_valueOrError3_ = UUID.default__.ToByteArray((d_24_conf_).keyStoreId)
        if not(not((d_27_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(60,22): " + _dafny.string_of(d_27_valueOrError3_))
        d_26_idByteUUID_ = (d_27_valueOrError3_).Extract()
        d_28_idRoundTrip_: _dafny.Seq
        d_29_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_29_valueOrError4_ = UUID.default__.FromByteArray(d_26_idByteUUID_)
        if not(not((d_29_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(61,23): " + _dafny.string_of(d_29_valueOrError4_))
        d_28_idRoundTrip_ = (d_29_valueOrError4_).Extract()
        if not((d_28_idRoundTrip_) == ((d_24_conf_).keyStoreId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_24_conf_).keyStoreName) == (Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(64,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_24_conf_).logicalKeyStoreName) == (Fixtures.default__.logicalKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_24_conf_).kmsConfiguration) == (d_21_kmsConfig_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestValidConfigNoClients():
        d_30_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_31_valueOrError0_: Wrappers.Result = None
        out11_: Wrappers.Result
        out11_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_31_valueOrError0_ = out11_
        if not(not((d_31_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(71,21): " + _dafny.string_of(d_31_valueOrError0_))
        d_30_kmsClient_ = (d_31_valueOrError0_).Extract()
        d_32_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_33_valueOrError1_: Wrappers.Result = None
        out12_: Wrappers.Result
        out12_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_33_valueOrError1_ = out12_
        if not(not((d_33_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(72,21): " + _dafny.string_of(d_33_valueOrError1_))
        d_32_ddbClient_ = (d_33_valueOrError1_).Extract()
        d_34_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_34_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_35_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_35_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_34_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_32_ddbClient_), Wrappers.Option_None())
        d_36_keyStore_: Wrappers.Result
        out13_: Wrappers.Result
        out13_ = KeyStore.default__.KeyStore(d_35_keyStoreConfig_)
        d_36_keyStore_ = out13_
        if not((d_36_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(86,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_35_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_34_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_30_kmsClient_))
        out14_: Wrappers.Result
        out14_ = KeyStore.default__.KeyStore(d_35_keyStoreConfig_)
        d_36_keyStore_ = out14_
        if not((d_36_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(99,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_35_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_34_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        out15_: Wrappers.Result
        out15_ = KeyStore.default__.KeyStore(d_35_keyStoreConfig_)
        d_36_keyStore_ = out15_
        if not((d_36_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

