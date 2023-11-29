import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
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
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
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

# assert "TestConfig" == __name__
TestConfig = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestInvalidKmsKeyArnConfig():
        d_401_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_402_valueOrError0_: Wrappers.Result = None
        out94_: Wrappers.Result
        out94_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_402_valueOrError0_ = out94_
        if not(not((d_402_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(18,18): " + _dafny.string_of(d_402_valueOrError0_))
        d_401_kmsClient_ = (d_402_valueOrError0_).Extract()
        d_403_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_404_valueOrError1_: Wrappers.Result = None
        out95_: Wrappers.Result
        out95_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_404_valueOrError1_ = out95_
        if not(not((d_404_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(19,18): " + _dafny.string_of(d_404_valueOrError1_))
        d_403_ddbClient_ = (d_404_valueOrError1_).Extract()
        d_405_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_405_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((Fixtures.default__).keyId)
        d_406_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_406_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_405_kmsConfig_, (Fixtures.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_403_ddbClient_), Wrappers.Option_Some(d_401_kmsClient_))
        d_407_keyStore_: Wrappers.Result
        out96_: Wrappers.Result
        out96_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_406_keyStoreConfig_)
        d_407_keyStore_ = out96_
        if not((d_407_keyStore_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(33,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_407_keyStore_).error) == (software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid AWS KMS Key Arn")))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestValidConfig():
        d_408_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_409_valueOrError0_: Wrappers.Result = None
        out97_: Wrappers.Result
        out97_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_409_valueOrError0_ = out97_
        if not(not((d_409_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(38,18): " + _dafny.string_of(d_409_valueOrError0_))
        d_408_kmsClient_ = (d_409_valueOrError0_).Extract()
        d_410_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_411_valueOrError1_: Wrappers.Result = None
        out98_: Wrappers.Result
        out98_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_411_valueOrError1_ = out98_
        if not(not((d_411_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(39,18): " + _dafny.string_of(d_411_valueOrError1_))
        d_410_ddbClient_ = (d_411_valueOrError1_).Extract()
        d_412_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_412_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((Fixtures.default__).keyArn)
        d_413_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_413_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_412_kmsConfig_, (Fixtures.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_410_ddbClient_), Wrappers.Option_Some(d_408_kmsClient_))
        d_414_keyStore_: Wrappers.Result
        out99_: Wrappers.Result
        out99_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_413_keyStoreConfig_)
        d_414_keyStore_ = out99_
        if not((d_414_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(53,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_415_conf_: software_amazon_cryptography_keystore_internaldafny_types.GetKeyStoreInfoOutput
        d_416_valueOrError2_: Wrappers.Result = None
        out100_: Wrappers.Result
        out100_ = ((d_414_keyStore_).value).GetKeyStoreInfo()
        d_416_valueOrError2_ = out100_
        if not(not((d_416_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(55,13): " + _dafny.string_of(d_416_valueOrError2_))
        d_415_conf_ = (d_416_valueOrError2_).Extract()
        d_417_idByteUUID_: _dafny.Seq
        d_418_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_418_valueOrError3_ = UUID.default__.ToByteArray((d_415_conf_).keyStoreId)
        if not(not((d_418_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(60,19): " + _dafny.string_of(d_418_valueOrError3_))
        d_417_idByteUUID_ = (d_418_valueOrError3_).Extract()
        d_419_idRoundTrip_: _dafny.Seq
        d_420_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_420_valueOrError4_ = UUID.default__.FromByteArray(d_417_idByteUUID_)
        if not(not((d_420_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(61,20): " + _dafny.string_of(d_420_valueOrError4_))
        d_419_idRoundTrip_ = (d_420_valueOrError4_).Extract()
        if not((d_419_idRoundTrip_) == ((d_415_conf_).keyStoreId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_415_conf_).keyStoreName) == ((Fixtures.default__).branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(64,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_415_conf_).logicalKeyStoreName) == ((Fixtures.default__).logicalKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_415_conf_).kmsConfiguration) == (d_412_kmsConfig_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestValidConfigNoClients():
        d_421_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_422_valueOrError0_: Wrappers.Result = None
        out101_: Wrappers.Result
        out101_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_422_valueOrError0_ = out101_
        if not(not((d_422_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(71,18): " + _dafny.string_of(d_422_valueOrError0_))
        d_421_kmsClient_ = (d_422_valueOrError0_).Extract()
        d_423_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_424_valueOrError1_: Wrappers.Result = None
        out102_: Wrappers.Result
        out102_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_424_valueOrError1_ = out102_
        if not(not((d_424_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(72,18): " + _dafny.string_of(d_424_valueOrError1_))
        d_423_ddbClient_ = (d_424_valueOrError1_).Extract()
        d_425_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_425_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((Fixtures.default__).keyArn)
        d_426_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_426_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_425_kmsConfig_, (Fixtures.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_423_ddbClient_), Wrappers.Option_None())
        d_427_keyStore_: Wrappers.Result
        out103_: Wrappers.Result
        out103_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_426_keyStoreConfig_)
        d_427_keyStore_ = out103_
        if not((d_427_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(86,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_426_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_425_kmsConfig_, (Fixtures.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_421_kmsClient_))
        out104_: Wrappers.Result
        out104_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_426_keyStoreConfig_)
        d_427_keyStore_ = out104_
        if not((d_427_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(99,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_426_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_425_kmsConfig_, (Fixtures.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        out105_: Wrappers.Result
        out105_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_426_keyStoreConfig_)
        d_427_keyStore_ = out105_
        if not((d_427_keyStore_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestConfig.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

