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
import TestConfig

# assert "TestGetKeys" == __name__
TestGetKeys = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestGetBeaconKey():
        d_428_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_429_valueOrError0_: Wrappers.Result = None
        out106_: Wrappers.Result
        out106_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_429_valueOrError0_ = out106_
        if not(not((d_429_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(21,18): " + _dafny.string_of(d_429_valueOrError0_))
        d_428_kmsClient_ = (d_429_valueOrError0_).Extract()
        d_430_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_431_valueOrError1_: Wrappers.Result = None
        out107_: Wrappers.Result
        out107_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_431_valueOrError1_ = out107_
        if not(not((d_431_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(22,18): " + _dafny.string_of(d_431_valueOrError1_))
        d_430_ddbClient_ = (d_431_valueOrError1_).Extract()
        d_432_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_432_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((Fixtures.default__).keyArn)
        d_433_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_433_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_432_kmsConfig_, (Fixtures.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_430_ddbClient_), Wrappers.Option_Some(d_428_kmsClient_))
        d_434_keyStore_: software_amazon_cryptography_keystore_internaldafny.KeyStoreClient
        d_435_valueOrError2_: Wrappers.Result = None
        out108_: Wrappers.Result
        out108_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_433_keyStoreConfig_)
        d_435_valueOrError2_ = out108_
        if not(not((d_435_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(35,17): " + _dafny.string_of(d_435_valueOrError2_))
        d_434_keyStore_ = (d_435_valueOrError2_).Extract()
        d_436_beaconKeyResult_: software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput
        d_437_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput.default())()
        out109_: Wrappers.Result
        out109_ = (d_434_keyStore_).GetBeaconKey(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyInput_GetBeaconKeyInput((Fixtures.default__).branchKeyId))
        d_437_valueOrError3_ = out109_
        if not(not((d_437_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(37,24): " + _dafny.string_of(d_437_valueOrError3_))
        d_436_beaconKeyResult_ = (d_437_valueOrError3_).Extract()
        if not((((d_436_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier) == ((Fixtures.default__).branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(41,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_436_beaconKeyResult_).beaconKeyMaterials).beaconKey).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(42,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((((d_436_beaconKeyResult_).beaconKeyMaterials).beaconKey).value)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(43,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKey():
        d_438_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_439_valueOrError0_: Wrappers.Result = None
        out110_: Wrappers.Result
        out110_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_439_valueOrError0_ = out110_
        if not(not((d_439_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(48,18): " + _dafny.string_of(d_439_valueOrError0_))
        d_438_kmsClient_ = (d_439_valueOrError0_).Extract()
        d_440_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_441_valueOrError1_: Wrappers.Result = None
        out111_: Wrappers.Result
        out111_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_441_valueOrError1_ = out111_
        if not(not((d_441_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(49,18): " + _dafny.string_of(d_441_valueOrError1_))
        d_440_ddbClient_ = (d_441_valueOrError1_).Extract()
        d_442_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_442_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((Fixtures.default__).keyArn)
        d_443_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_443_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_442_kmsConfig_, (Fixtures.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_440_ddbClient_), Wrappers.Option_Some(d_438_kmsClient_))
        d_444_keyStore_: software_amazon_cryptography_keystore_internaldafny.KeyStoreClient
        d_445_valueOrError2_: Wrappers.Result = None
        out112_: Wrappers.Result
        out112_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_443_keyStoreConfig_)
        d_445_valueOrError2_ = out112_
        if not(not((d_445_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(62,17): " + _dafny.string_of(d_445_valueOrError2_))
        d_444_keyStore_ = (d_445_valueOrError2_).Extract()
        d_446_activeResult_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
        d_447_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out113_: Wrappers.Result
        out113_ = (d_444_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput((Fixtures.default__).branchKeyId))
        d_447_valueOrError3_ = out113_
        if not(not((d_447_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(64,21): " + _dafny.string_of(d_447_valueOrError3_))
        d_446_activeResult_ = (d_447_valueOrError3_).Extract()
        if not((((d_446_activeResult_).branchKeyMaterials).branchKeyIdentifier) == ((Fixtures.default__).branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_446_activeResult_).branchKeyMaterials).branchKeyVersion) == ((Fixtures.default__).branchKeyIdActiveVersionUtf8Bytes)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(70,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_446_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(71,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetBranchKeyVersion():
        d_448_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_449_valueOrError0_: Wrappers.Result = None
        out114_: Wrappers.Result
        out114_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_449_valueOrError0_ = out114_
        if not(not((d_449_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(76,18): " + _dafny.string_of(d_449_valueOrError0_))
        d_448_kmsClient_ = (d_449_valueOrError0_).Extract()
        d_450_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_451_valueOrError1_: Wrappers.Result = None
        out115_: Wrappers.Result
        out115_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_451_valueOrError1_ = out115_
        if not(not((d_451_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(77,18): " + _dafny.string_of(d_451_valueOrError1_))
        d_450_ddbClient_ = (d_451_valueOrError1_).Extract()
        d_452_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_452_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((Fixtures.default__).keyArn)
        d_453_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_453_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_452_kmsConfig_, (Fixtures.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_450_ddbClient_), Wrappers.Option_Some(d_448_kmsClient_))
        d_454_keyStore_: software_amazon_cryptography_keystore_internaldafny.KeyStoreClient
        d_455_valueOrError2_: Wrappers.Result = None
        out116_: Wrappers.Result
        out116_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_453_keyStoreConfig_)
        d_455_valueOrError2_ = out116_
        if not(not((d_455_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(90,17): " + _dafny.string_of(d_455_valueOrError2_))
        d_454_keyStore_ = (d_455_valueOrError2_).Extract()
        d_456_versionResult_: software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput
        d_457_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        out117_: Wrappers.Result
        out117_ = (d_454_keyStore_).GetBranchKeyVersion(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionInput_GetBranchKeyVersionInput((Fixtures.default__).branchKeyId, (Fixtures.default__).branchKeyIdActiveVersion))
        d_457_valueOrError3_ = out117_
        if not(not((d_457_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(92,22): " + _dafny.string_of(d_457_valueOrError3_))
        d_456_versionResult_ = (d_457_valueOrError3_).Extract()
        d_458_testBytes_: _dafny.Seq
        d_459_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_459_valueOrError4_ = UTF8.default__.Encode((Fixtures.default__).branchKeyIdActiveVersion)
        if not(not((d_459_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(98,18): " + _dafny.string_of(d_459_valueOrError4_))
        d_458_testBytes_ = (d_459_valueOrError4_).Extract()
        if not((((d_456_versionResult_).branchKeyMaterials).branchKeyIdentifier) == ((Fixtures.default__).branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(100,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_456_versionResult_).branchKeyMaterials).branchKeyVersion) == ((Fixtures.default__).branchKeyIdActiveVersionUtf8Bytes)) and (((Fixtures.default__).branchKeyIdActiveVersionUtf8Bytes) == (d_458_testBytes_))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_456_versionResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(102,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWithIncorrectKmsKeyArn():
        d_460_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_461_valueOrError0_: Wrappers.Result = None
        out118_: Wrappers.Result
        out118_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_461_valueOrError0_ = out118_
        if not(not((d_461_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(107,18): " + _dafny.string_of(d_461_valueOrError0_))
        d_460_kmsClient_ = (d_461_valueOrError0_).Extract()
        d_462_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_463_valueOrError1_: Wrappers.Result = None
        out119_: Wrappers.Result
        out119_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_463_valueOrError1_ = out119_
        if not(not((d_463_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(108,18): " + _dafny.string_of(d_463_valueOrError1_))
        d_462_ddbClient_ = (d_463_valueOrError1_).Extract()
        d_464_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_464_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((Fixtures.default__).mkrKeyArn)
        d_465_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_465_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_464_kmsConfig_, (Fixtures.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_462_ddbClient_), Wrappers.Option_Some(d_460_kmsClient_))
        d_466_keyStore_: software_amazon_cryptography_keystore_internaldafny.KeyStoreClient
        d_467_valueOrError2_: Wrappers.Result = None
        out120_: Wrappers.Result
        out120_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_465_keyStoreConfig_)
        d_467_valueOrError2_ = out120_
        if not(not((d_467_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(121,17): " + _dafny.string_of(d_467_valueOrError2_))
        d_466_keyStore_ = (d_467_valueOrError2_).Extract()
        d_468_activeResult_: Wrappers.Result
        out121_: Wrappers.Result
        out121_ = (d_466_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput((Fixtures.default__).branchKeyId))
        d_468_activeResult_ = out121_
        if not((d_468_activeResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWrongLogicalKeyStoreName():
        d_469_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_470_valueOrError0_: Wrappers.Result = None
        out122_: Wrappers.Result
        out122_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_470_valueOrError0_ = out122_
        if not(not((d_470_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(132,18): " + _dafny.string_of(d_470_valueOrError0_))
        d_469_kmsClient_ = (d_470_valueOrError0_).Extract()
        d_471_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_472_valueOrError1_: Wrappers.Result = None
        out123_: Wrappers.Result
        out123_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_472_valueOrError1_ = out123_
        if not(not((d_472_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(133,18): " + _dafny.string_of(d_472_valueOrError1_))
        d_471_ddbClient_ = (d_472_valueOrError1_).Extract()
        d_473_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_473_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((Fixtures.default__).keyArn)
        d_474_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_474_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_473_kmsConfig_, (TestGetKeys.default__).incorrectLogicalName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_471_ddbClient_), Wrappers.Option_Some(d_469_kmsClient_))
        d_475_keyStore_: software_amazon_cryptography_keystore_internaldafny.KeyStoreClient
        d_476_valueOrError2_: Wrappers.Result = None
        out124_: Wrappers.Result
        out124_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_474_keyStoreConfig_)
        d_476_valueOrError2_ = out124_
        if not(not((d_476_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(146,17): " + _dafny.string_of(d_476_valueOrError2_))
        d_475_keyStore_ = (d_476_valueOrError2_).Extract()
        d_477_activeResult_: Wrappers.Result
        out125_: Wrappers.Result
        out125_ = (d_475_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput((Fixtures.default__).branchKeyId))
        d_477_activeResult_ = out125_
        if not((d_477_activeResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(153,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWithNoClients():
        d_478_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_478_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((Fixtures.default__).keyArn)
        d_479_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_479_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_478_kmsConfig_, (Fixtures.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_480_keyStore_: software_amazon_cryptography_keystore_internaldafny.KeyStoreClient
        d_481_valueOrError0_: Wrappers.Result = None
        out126_: Wrappers.Result
        out126_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_479_keyStoreConfig_)
        d_481_valueOrError0_ = out126_
        if not(not((d_481_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(169,17): " + _dafny.string_of(d_481_valueOrError0_))
        d_480_keyStore_ = (d_481_valueOrError0_).Extract()
        d_482_activeResult_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
        d_483_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out127_: Wrappers.Result
        out127_ = (d_480_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput((Fixtures.default__).branchKeyId))
        d_483_valueOrError1_ = out127_
        if not(not((d_483_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(171,21): " + _dafny.string_of(d_483_valueOrError1_))
        d_482_activeResult_ = (d_483_valueOrError1_).Extract()
        if not((len(((d_482_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(176,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def incorrectLogicalName(instance):
        return _dafny.Seq("MySuperAwesomeTableName")
