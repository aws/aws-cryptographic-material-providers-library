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
import TestGetKeys
import CleanupItems

assert "TestCreateKeys" == __name__
TestCreateKeys = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestCreateBranchAndBeaconKeys():
        d_487_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_488_valueOrError0_: Wrappers.Result = None
        out131_: Wrappers.Result
        out131_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_488_valueOrError0_ = out131_
        if not(not((d_488_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(25,18): " + _dafny.string_of(d_488_valueOrError0_))
        d_487_kmsClient_ = (d_488_valueOrError0_).Extract()
        d_489_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_490_valueOrError1_: Wrappers.Result = None
        out132_: Wrappers.Result
        out132_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_490_valueOrError1_ = out132_
        if not(not((d_490_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(26,18): " + _dafny.string_of(d_490_valueOrError1_))
        d_489_ddbClient_ = (d_490_valueOrError1_).Extract()
        d_491_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_491_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((Fixtures.default__).keyArn)
        d_492_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_492_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_491_kmsConfig_, (Fixtures.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_489_ddbClient_), Wrappers.Option_Some(d_487_kmsClient_))
        d_493_keyStore_: software_amazon_cryptography_keystore_internaldafny.KeyStoreClient
        d_494_valueOrError2_: Wrappers.Result = None
        out133_: Wrappers.Result
        out133_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_492_keyStoreConfig_)
        d_494_valueOrError2_ = out133_
        if not(not((d_494_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(39,17): " + _dafny.string_of(d_494_valueOrError2_))
        d_493_keyStore_ = (d_494_valueOrError2_).Extract()
        d_495_branchKeyId_: software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput
        d_496_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput.default())()
        out134_: Wrappers.Result
        out134_ = (d_493_keyStore_).CreateKey(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyInput_CreateKeyInput(Wrappers.Option_None(), Wrappers.Option_None()))
        d_496_valueOrError3_ = out134_
        if not(not((d_496_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(41,20): " + _dafny.string_of(d_496_valueOrError3_))
        d_495_branchKeyId_ = (d_496_valueOrError3_).Extract()
        d_497_beaconKeyResult_: software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput
        d_498_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput.default())()
        out135_: Wrappers.Result
        out135_ = (d_493_keyStore_).GetBeaconKey(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyInput_GetBeaconKeyInput((d_495_branchKeyId_).branchKeyIdentifier))
        d_498_valueOrError4_ = out135_
        if not(not((d_498_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(46,24): " + _dafny.string_of(d_498_valueOrError4_))
        d_497_beaconKeyResult_ = (d_498_valueOrError4_).Extract()
        d_499_activeResult_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
        d_500_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out136_: Wrappers.Result
        out136_ = (d_493_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_495_branchKeyId_).branchKeyIdentifier))
        d_500_valueOrError5_ = out136_
        if not(not((d_500_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(51,21): " + _dafny.string_of(d_500_valueOrError5_))
        d_499_activeResult_ = (d_500_valueOrError5_).Extract()
        d_501_branchKeyVersion_: _dafny.Seq
        d_502_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_502_valueOrError6_ = UTF8.default__.Decode(((d_499_activeResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_502_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(56,25): " + _dafny.string_of(d_502_valueOrError6_))
        d_501_branchKeyVersion_ = (d_502_valueOrError6_).Extract()
        d_503_versionResult_: software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput
        d_504_valueOrError7_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        out137_: Wrappers.Result
        out137_ = (d_493_keyStore_).GetBranchKeyVersion(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_495_branchKeyId_).branchKeyIdentifier, d_501_branchKeyVersion_))
        d_504_valueOrError7_ = out137_
        if not(not((d_504_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(57,22): " + _dafny.string_of(d_504_valueOrError7_))
        d_503_versionResult_ = (d_504_valueOrError7_).Extract()
        CleanupItems.default__.DeleteVersion((d_495_branchKeyId_).branchKeyIdentifier, d_501_branchKeyVersion_, d_489_ddbClient_)
        CleanupItems.default__.DeleteActive((d_495_branchKeyId_).branchKeyIdentifier, d_489_ddbClient_)
        if not((((d_497_beaconKeyResult_).beaconKeyMaterials).beaconKey).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((((d_497_beaconKeyResult_).beaconKeyMaterials).beaconKey).value)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(70,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_499_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(71,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_503_versionResult_).branchKeyMaterials).branchKey) == (((d_499_activeResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_503_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_499_activeResult_).branchKeyMaterials).branchKeyIdentifier)) and ((((d_499_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_497_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(73,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_503_versionResult_).branchKeyMaterials).branchKeyVersion) == (((d_499_activeResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(76,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_505_idByteUUID_: _dafny.Seq
        d_506_valueOrError8_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_506_valueOrError8_ = UUID.default__.ToByteArray(((d_499_activeResult_).branchKeyMaterials).branchKeyIdentifier)
        if not(not((d_506_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(83,19): " + _dafny.string_of(d_506_valueOrError8_))
        d_505_idByteUUID_ = (d_506_valueOrError8_).Extract()
        d_507_idRoundTrip_: _dafny.Seq
        d_508_valueOrError9_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_508_valueOrError9_ = UUID.default__.FromByteArray(d_505_idByteUUID_)
        if not(not((d_508_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(84,20): " + _dafny.string_of(d_508_valueOrError9_))
        d_507_idRoundTrip_ = (d_508_valueOrError9_).Extract()
        if not((d_507_idRoundTrip_) == (((d_499_activeResult_).branchKeyMaterials).branchKeyIdentifier)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(85,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_509_versionString_: _dafny.Seq
        d_510_valueOrError10_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_510_valueOrError10_ = UTF8.default__.Decode(((d_499_activeResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_510_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(91,22): " + _dafny.string_of(d_510_valueOrError10_))
        d_509_versionString_ = (d_510_valueOrError10_).Extract()
        d_511_versionByteUUID_: _dafny.Seq
        d_512_valueOrError11_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_512_valueOrError11_ = UUID.default__.ToByteArray(d_509_versionString_)
        if not(not((d_512_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(92,24): " + _dafny.string_of(d_512_valueOrError11_))
        d_511_versionByteUUID_ = (d_512_valueOrError11_).Extract()
        d_513_versionRoundTrip_: _dafny.Seq
        d_514_valueOrError12_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_514_valueOrError12_ = UUID.default__.FromByteArray(d_511_versionByteUUID_)
        if not(not((d_514_valueOrError12_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(93,25): " + _dafny.string_of(d_514_valueOrError12_))
        d_513_versionRoundTrip_ = (d_514_valueOrError12_).Extract()
        if not((d_513_versionRoundTrip_) == (d_509_versionString_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(94,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCreateOptions():
        d_515_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_516_valueOrError0_: Wrappers.Result = None
        out138_: Wrappers.Result
        out138_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_516_valueOrError0_ = out138_
        if not(not((d_516_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(100,18): " + _dafny.string_of(d_516_valueOrError0_))
        d_515_kmsClient_ = (d_516_valueOrError0_).Extract()
        d_517_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_518_valueOrError1_: Wrappers.Result = None
        out139_: Wrappers.Result
        out139_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_518_valueOrError1_ = out139_
        if not(not((d_518_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(101,18): " + _dafny.string_of(d_518_valueOrError1_))
        d_517_ddbClient_ = (d_518_valueOrError1_).Extract()
        d_519_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_519_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((Fixtures.default__).keyArn)
        d_520_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_520_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_519_kmsConfig_, (Fixtures.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_517_ddbClient_), Wrappers.Option_Some(d_515_kmsClient_))
        d_521_keyStore_: software_amazon_cryptography_keystore_internaldafny.KeyStoreClient
        d_522_valueOrError2_: Wrappers.Result = None
        out140_: Wrappers.Result
        out140_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_520_keyStoreConfig_)
        d_522_valueOrError2_ = out140_
        if not(not((d_522_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(114,17): " + _dafny.string_of(d_522_valueOrError2_))
        d_521_keyStore_ = (d_522_valueOrError2_).Extract()
        d_523_id_: _dafny.Seq
        d_524_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out141_: Wrappers.Result
        out141_ = UUID.default__.GenerateUUID()
        d_524_valueOrError3_ = out141_
        if not(not((d_524_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(117,11): " + _dafny.string_of(d_524_valueOrError3_))
        d_523_id_ = (d_524_valueOrError3_).Extract()
        d_525_encryptionContext_: _dafny.Map
        d_526_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Map)()
        out142_: Wrappers.Result
        out142_ = TestCreateKeys.default__.EncodeEncryptionContext(_dafny.Map({_dafny.Seq("some"): _dafny.Seq("encryption"), _dafny.Seq("context"): _dafny.Seq("values")}))
        d_526_valueOrError4_ = out142_
        if not(not((d_526_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(119,26): " + _dafny.string_of(d_526_valueOrError4_))
        d_525_encryptionContext_ = (d_526_valueOrError4_).Extract()
        d_527_branchKeyId_: software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput
        d_528_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput.default())()
        out143_: Wrappers.Result
        out143_ = (d_521_keyStore_).CreateKey(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyInput_CreateKeyInput(Wrappers.Option_Some(d_523_id_), Wrappers.Option_Some(d_525_encryptionContext_)))
        d_528_valueOrError5_ = out143_
        if not(not((d_528_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(124,20): " + _dafny.string_of(d_528_valueOrError5_))
        d_527_branchKeyId_ = (d_528_valueOrError5_).Extract()
        d_529_beaconKeyResult_: software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput
        d_530_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput.default())()
        out144_: Wrappers.Result
        out144_ = (d_521_keyStore_).GetBeaconKey(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyInput_GetBeaconKeyInput((d_527_branchKeyId_).branchKeyIdentifier))
        d_530_valueOrError6_ = out144_
        if not(not((d_530_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(129,24): " + _dafny.string_of(d_530_valueOrError6_))
        d_529_beaconKeyResult_ = (d_530_valueOrError6_).Extract()
        d_531_activeResult_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
        d_532_valueOrError7_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out145_: Wrappers.Result
        out145_ = (d_521_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_527_branchKeyId_).branchKeyIdentifier))
        d_532_valueOrError7_ = out145_
        if not(not((d_532_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(134,21): " + _dafny.string_of(d_532_valueOrError7_))
        d_531_activeResult_ = (d_532_valueOrError7_).Extract()
        d_533_branchKeyVersion_: _dafny.Seq
        d_534_valueOrError8_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_534_valueOrError8_ = UTF8.default__.Decode(((d_531_activeResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_534_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(139,25): " + _dafny.string_of(d_534_valueOrError8_))
        d_533_branchKeyVersion_ = (d_534_valueOrError8_).Extract()
        d_535_versionResult_: software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput
        d_536_valueOrError9_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        out146_: Wrappers.Result
        out146_ = (d_521_keyStore_).GetBranchKeyVersion(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_527_branchKeyId_).branchKeyIdentifier, d_533_branchKeyVersion_))
        d_536_valueOrError9_ = out146_
        if not(not((d_536_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(140,22): " + _dafny.string_of(d_536_valueOrError9_))
        d_535_versionResult_ = (d_536_valueOrError9_).Extract()
        CleanupItems.default__.DeleteVersion((d_527_branchKeyId_).branchKeyIdentifier, d_533_branchKeyVersion_, d_517_ddbClient_)
        CleanupItems.default__.DeleteActive((d_527_branchKeyId_).branchKeyIdentifier, d_517_ddbClient_)
        if not((((d_523_id_) == (((d_535_versionResult_).branchKeyMaterials).branchKeyIdentifier)) and ((((d_535_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_531_activeResult_).branchKeyMaterials).branchKeyIdentifier))) and ((((d_531_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_529_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(153,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_525_encryptionContext_) == (((d_535_versionResult_).branchKeyMaterials).encryptionContext)) and ((((d_535_versionResult_).branchKeyMaterials).encryptionContext) == (((d_531_activeResult_).branchKeyMaterials).encryptionContext))) and ((((d_531_activeResult_).branchKeyMaterials).encryptionContext) == (((d_529_beaconKeyResult_).beaconKeyMaterials).encryptionContext))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(158,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCreateDuplicate():
        d_537_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_538_valueOrError0_: Wrappers.Result = None
        out147_: Wrappers.Result
        out147_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_538_valueOrError0_ = out147_
        if not(not((d_538_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(167,18): " + _dafny.string_of(d_538_valueOrError0_))
        d_537_kmsClient_ = (d_538_valueOrError0_).Extract()
        d_539_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_540_valueOrError1_: Wrappers.Result = None
        out148_: Wrappers.Result
        out148_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_540_valueOrError1_ = out148_
        if not(not((d_540_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(168,18): " + _dafny.string_of(d_540_valueOrError1_))
        d_539_ddbClient_ = (d_540_valueOrError1_).Extract()
        d_541_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_541_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((Fixtures.default__).keyArn)
        d_542_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_542_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_541_kmsConfig_, (Fixtures.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_539_ddbClient_), Wrappers.Option_Some(d_537_kmsClient_))
        d_543_keyStore_: software_amazon_cryptography_keystore_internaldafny.KeyStoreClient
        d_544_valueOrError2_: Wrappers.Result = None
        out149_: Wrappers.Result
        out149_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_542_keyStoreConfig_)
        d_544_valueOrError2_ = out149_
        if not(not((d_544_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(181,17): " + _dafny.string_of(d_544_valueOrError2_))
        d_543_keyStore_ = (d_544_valueOrError2_).Extract()
        d_545_attempt_: Wrappers.Result
        out150_: Wrappers.Result
        out150_ = (d_543_keyStore_).CreateKey(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyInput_CreateKeyInput(Wrappers.Option_Some((Fixtures.default__).branchKeyId), Wrappers.Option_None()))
        d_545_attempt_ = out150_
        if not((d_545_attempt_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(188,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def InsertingADuplicateWillFail():
        d_546_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_547_valueOrError0_: Wrappers.Result = None
        out151_: Wrappers.Result
        out151_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_547_valueOrError0_ = out151_
        if not(not((d_547_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(193,18): " + _dafny.string_of(d_547_valueOrError0_))
        d_546_ddbClient_ = (d_547_valueOrError0_).Extract()
        d_548_encryptionContext_: _dafny.Map
        d_548_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext((Fixtures.default__).branchKeyId, (Fixtures.default__).branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), (Fixtures.default__).keyArn, _dafny.Map({}))
        d_549_output_: Wrappers.Result
        out152_: Wrappers.Result
        out152_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(Structure.default__.ToAttributeMap(d_548_encryptionContext_, _dafny.Seq([1])), Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_548_encryptionContext_), _dafny.Seq([2])), Structure.default__.ToAttributeMap(Structure.default__.BeaconKeyEncryptionContext(d_548_encryptionContext_), _dafny.Seq([3])), (Fixtures.default__).branchKeyStoreName, d_546_ddbClient_)
        d_549_output_ = out152_
        if not((d_549_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(212,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def InsertingADuplicateWillWithADifferentVersionFail():
        d_550_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_551_valueOrError0_: Wrappers.Result = None
        out153_: Wrappers.Result
        out153_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_551_valueOrError0_ = out153_
        if not(not((d_551_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(217,18): " + _dafny.string_of(d_551_valueOrError0_))
        d_550_ddbClient_ = (d_551_valueOrError0_).Extract()
        d_552_encryptionContext_: _dafny.Map
        d_552_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext((Fixtures.default__).branchKeyId, _dafny.Seq("!= branchKeyIdActiveVersion"), _dafny.Seq(""), _dafny.Seq(""), (Fixtures.default__).keyArn, _dafny.Map({}))
        d_553_output_: Wrappers.Result
        out154_: Wrappers.Result
        out154_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(Structure.default__.ToAttributeMap(d_552_encryptionContext_, _dafny.Seq([1])), Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_552_encryptionContext_), _dafny.Seq([2])), Structure.default__.ToAttributeMap(Structure.default__.BeaconKeyEncryptionContext(d_552_encryptionContext_), _dafny.Seq([3])), (Fixtures.default__).branchKeyStoreName, d_550_ddbClient_)
        d_553_output_ = out154_
        if not((d_553_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(236,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def EncodeEncryptionContext(input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Map)()
        d_554_encodedEncryptionContext_: _dafny.Set
        def iife11_():
            coll9_ = _dafny.Set()
            compr_9_: _dafny.Seq
            for compr_9_ in (input).keys.Elements:
                d_555_k_: _dafny.Seq = compr_9_
                if (d_555_k_) in (input):
                    coll9_ = coll9_.union(_dafny.Set([(UTF8.default__.Encode(d_555_k_), UTF8.default__.Encode((input)[d_555_k_]), d_555_k_)]))
            return _dafny.Set(coll9_)
        d_554_encodedEncryptionContext_ = iife11_()
        
        d_556_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def lambda29_(forall_var_8_):
            def iife12_(_pat_let1_0):
                def iife13_(d_558_encoded_):
                    return ((d_558_encoded_).is_Success) and (((d_557_i_)[2]) == ((d_558_encoded_).value))
                return iife13_(_pat_let1_0)
            d_557_i_: tuple = forall_var_8_
            return not ((d_557_i_) in (d_554_encodedEncryptionContext_)) or (((((d_557_i_)[0]).is_Success) and (((d_557_i_)[1]).is_Success)) and (iife12_(UTF8.default__.Decode(((d_557_i_)[0]).value))))

        d_556_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier((d_554_encodedEncryptionContext_).Elements, True, lambda29_), _dafny.Seq("Unable to encode string"))
        if (d_556_valueOrError0_).IsFailure():
            output = (d_556_valueOrError0_).PropagateFailure()
            return output
        def iife14_():
            coll10_ = _dafny.Map()
            compr_10_: tuple
            for compr_10_ in (d_554_encodedEncryptionContext_).Elements:
                d_559_i_: tuple = compr_10_
                if (d_559_i_) in (d_554_encodedEncryptionContext_):
                    coll10_[((d_559_i_)[0]).value] = ((d_559_i_)[1]).value
            return _dafny.Map(coll10_)
        output = Wrappers.Result_Success(iife14_()
)
        return output

