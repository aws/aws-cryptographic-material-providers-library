import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import Relations
import Seq_MergeSort
import Math
import Seq
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import Actions
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import UUID
import Time
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import Base64
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import DafnyLibraries
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring
import CMM
import Defaults
import Commitment
import DefaultCMM
import DefaultClientSupplier
import RequiredEncryptionContextCMM
import AwsCryptographyMaterialProvidersOperations
import software_amazon_cryptography_materialproviders_internaldafny
import AesKdfCtr
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibraryInterop
import Streams
import Sorting
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64Lemmas
import Fixtures
import TestCreateKeyStore

# Module: TestConfig

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestInvalidKmsKeyArnConfig():
        d_10_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_11_valueOrError0_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_11_valueOrError0_ = out4_
        if not(not((d_11_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(18,21): " + _dafny.string_of(d_11_valueOrError0_))
        d_10_kmsClient_ = (d_11_valueOrError0_).Extract()
        d_12_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_13_valueOrError1_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_13_valueOrError1_ = out5_
        if not(not((d_13_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(19,21): " + _dafny.string_of(d_13_valueOrError1_))
        d_12_ddbClient_ = (d_13_valueOrError1_).Extract()
        d_14_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_14_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyId)
        d_15_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_15_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_14_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_12_ddbClient_), Wrappers.Option_Some(d_10_kmsClient_))
        d_16_keyStore_: Wrappers.Result
        out6_: Wrappers.Result
        out6_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_15_keyStoreConfig_)
        d_16_keyStore_ = out6_
        if not((d_16_keyStore_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(33,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_16_keyStore_).error) == (software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid AWS KMS Key Arn")))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestValidConfig():
        d_17_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_18_valueOrError0_: Wrappers.Result = None
        out7_: Wrappers.Result
        out7_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_18_valueOrError0_ = out7_
        if not(not((d_18_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(38,21): " + _dafny.string_of(d_18_valueOrError0_))
        d_17_kmsClient_ = (d_18_valueOrError0_).Extract()
        d_19_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_20_valueOrError1_: Wrappers.Result = None
        out8_: Wrappers.Result
        out8_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_20_valueOrError1_ = out8_
        if not(not((d_20_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(39,21): " + _dafny.string_of(d_20_valueOrError1_))
        d_19_ddbClient_ = (d_20_valueOrError1_).Extract()
        d_21_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_21_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_22_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_22_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_21_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_19_ddbClient_), Wrappers.Option_Some(d_17_kmsClient_))
        d_23_keyStore_: Wrappers.Result
        out9_: Wrappers.Result
        out9_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_22_keyStoreConfig_)
        d_23_keyStore_ = out9_
        if not((d_23_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(53,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_24_conf_: software_amazon_cryptography_keystore_internaldafny_types.GetKeyStoreInfoOutput
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
        d_30_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_31_valueOrError0_: Wrappers.Result = None
        out11_: Wrappers.Result
        out11_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_31_valueOrError0_ = out11_
        if not(not((d_31_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(71,21): " + _dafny.string_of(d_31_valueOrError0_))
        d_30_kmsClient_ = (d_31_valueOrError0_).Extract()
        d_32_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_33_valueOrError1_: Wrappers.Result = None
        out12_: Wrappers.Result
        out12_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_33_valueOrError1_ = out12_
        if not(not((d_33_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(72,21): " + _dafny.string_of(d_33_valueOrError1_))
        d_32_ddbClient_ = (d_33_valueOrError1_).Extract()
        d_34_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_34_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_35_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_35_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_34_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_32_ddbClient_), Wrappers.Option_None())
        d_36_keyStore_: Wrappers.Result
        out13_: Wrappers.Result
        out13_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_35_keyStoreConfig_)
        d_36_keyStore_ = out13_
        if not((d_36_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(86,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_35_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_34_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_30_kmsClient_))
        out14_: Wrappers.Result
        out14_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_35_keyStoreConfig_)
        d_36_keyStore_ = out14_
        if not((d_36_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(99,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_35_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_34_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        out15_: Wrappers.Result
        out15_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_35_keyStoreConfig_)
        d_36_keyStore_ = out15_
        if not((d_36_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

