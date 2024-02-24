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
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import Base64
import AlgorithmSuites
import Materials
import Keyring
import Relations
import Seq_MergeSort
import Math
import Seq
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import Actions
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import DafnyLibraries
import Time
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import UUID
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
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
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
import Streams
import Sorting
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64Lemmas
import Fixtures
import TestCreateKeyStore
import TestConfig

# Module: TestGetKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestGetBeaconKey():
        d_37_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_38_valueOrError0_: Wrappers.Result = None
        out16_: Wrappers.Result
        out16_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_38_valueOrError0_ = out16_
        if not(not((d_38_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(21,18): " + _dafny.string_of(d_38_valueOrError0_))
        d_37_kmsClient_ = (d_38_valueOrError0_).Extract()
        d_39_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_40_valueOrError1_: Wrappers.Result = None
        out17_: Wrappers.Result
        out17_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_40_valueOrError1_ = out17_
        if not(not((d_40_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(22,18): " + _dafny.string_of(d_40_valueOrError1_))
        d_39_ddbClient_ = (d_40_valueOrError1_).Extract()
        d_41_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_41_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_42_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_42_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_41_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_39_ddbClient_), Wrappers.Option_Some(d_37_kmsClient_))
        d_43_keyStore_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
        d_44_valueOrError2_: Wrappers.Result = None
        out18_: Wrappers.Result
        out18_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_42_keyStoreConfig_)
        d_44_valueOrError2_ = out18_
        if not(not((d_44_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(35,17): " + _dafny.string_of(d_44_valueOrError2_))
        d_43_keyStore_ = (d_44_valueOrError2_).Extract()
        d_45_beaconKeyResult_: software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput
        d_46_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput.default())()
        out19_: Wrappers.Result
        out19_ = (d_43_keyStore_).GetBeaconKey(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.branchKeyId))
        d_46_valueOrError3_ = out19_
        if not(not((d_46_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(37,24): " + _dafny.string_of(d_46_valueOrError3_))
        d_45_beaconKeyResult_ = (d_46_valueOrError3_).Extract()
        if not((((d_45_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(41,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_45_beaconKeyResult_).beaconKeyMaterials).beaconKey).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(42,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((((d_45_beaconKeyResult_).beaconKeyMaterials).beaconKey).value)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(43,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKey():
        d_47_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_48_valueOrError0_: Wrappers.Result = None
        out20_: Wrappers.Result
        out20_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_48_valueOrError0_ = out20_
        if not(not((d_48_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(48,18): " + _dafny.string_of(d_48_valueOrError0_))
        d_47_kmsClient_ = (d_48_valueOrError0_).Extract()
        d_49_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_50_valueOrError1_: Wrappers.Result = None
        out21_: Wrappers.Result
        out21_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_50_valueOrError1_ = out21_
        if not(not((d_50_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(49,18): " + _dafny.string_of(d_50_valueOrError1_))
        d_49_ddbClient_ = (d_50_valueOrError1_).Extract()
        d_51_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_51_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_52_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_52_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_51_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_49_ddbClient_), Wrappers.Option_Some(d_47_kmsClient_))
        d_53_keyStore_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
        d_54_valueOrError2_: Wrappers.Result = None
        out22_: Wrappers.Result
        out22_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_52_keyStoreConfig_)
        d_54_valueOrError2_ = out22_
        if not(not((d_54_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(62,17): " + _dafny.string_of(d_54_valueOrError2_))
        d_53_keyStore_ = (d_54_valueOrError2_).Extract()
        d_55_activeResult_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
        d_56_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out23_: Wrappers.Result
        out23_ = (d_53_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_56_valueOrError3_ = out23_
        if not(not((d_56_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(64,21): " + _dafny.string_of(d_56_valueOrError3_))
        d_55_activeResult_ = (d_56_valueOrError3_).Extract()
        if not((((d_55_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_55_activeResult_).branchKeyMaterials).branchKeyVersion) == (Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(70,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_55_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(71,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetBranchKeyVersion():
        d_57_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_58_valueOrError0_: Wrappers.Result = None
        out24_: Wrappers.Result
        out24_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_58_valueOrError0_ = out24_
        if not(not((d_58_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(76,18): " + _dafny.string_of(d_58_valueOrError0_))
        d_57_kmsClient_ = (d_58_valueOrError0_).Extract()
        d_59_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_60_valueOrError1_: Wrappers.Result = None
        out25_: Wrappers.Result
        out25_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_60_valueOrError1_ = out25_
        if not(not((d_60_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(77,18): " + _dafny.string_of(d_60_valueOrError1_))
        d_59_ddbClient_ = (d_60_valueOrError1_).Extract()
        d_61_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_61_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_62_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_62_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_61_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_59_ddbClient_), Wrappers.Option_Some(d_57_kmsClient_))
        d_63_keyStore_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
        d_64_valueOrError2_: Wrappers.Result = None
        out26_: Wrappers.Result
        out26_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_62_keyStoreConfig_)
        d_64_valueOrError2_ = out26_
        if not(not((d_64_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(90,17): " + _dafny.string_of(d_64_valueOrError2_))
        d_63_keyStore_ = (d_64_valueOrError2_).Extract()
        d_65_versionResult_: software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput
        d_66_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        out27_: Wrappers.Result
        out27_ = (d_63_keyStore_).GetBranchKeyVersion(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionInput_GetBranchKeyVersionInput(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion))
        d_66_valueOrError3_ = out27_
        if not(not((d_66_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(92,22): " + _dafny.string_of(d_66_valueOrError3_))
        d_65_versionResult_ = (d_66_valueOrError3_).Extract()
        d_67_testBytes_: _dafny.Seq
        d_68_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_68_valueOrError4_ = UTF8.default__.Encode(Fixtures.default__.branchKeyIdActiveVersion)
        if not(not((d_68_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(98,18): " + _dafny.string_of(d_68_valueOrError4_))
        d_67_testBytes_ = (d_68_valueOrError4_).Extract()
        if not((((d_65_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(100,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_65_versionResult_).branchKeyMaterials).branchKeyVersion) == (Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes)) and ((Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes) == (d_67_testBytes_))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_65_versionResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(102,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWithIncorrectKmsKeyArn():
        d_69_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_70_valueOrError0_: Wrappers.Result = None
        out28_: Wrappers.Result
        out28_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_70_valueOrError0_ = out28_
        if not(not((d_70_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(107,18): " + _dafny.string_of(d_70_valueOrError0_))
        d_69_kmsClient_ = (d_70_valueOrError0_).Extract()
        d_71_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_72_valueOrError1_: Wrappers.Result = None
        out29_: Wrappers.Result
        out29_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_72_valueOrError1_ = out29_
        if not(not((d_72_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(108,18): " + _dafny.string_of(d_72_valueOrError1_))
        d_71_ddbClient_ = (d_72_valueOrError1_).Extract()
        d_73_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_73_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn(Fixtures.default__.mkrKeyArn)
        d_74_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_74_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_73_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_71_ddbClient_), Wrappers.Option_Some(d_69_kmsClient_))
        d_75_keyStore_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
        d_76_valueOrError2_: Wrappers.Result = None
        out30_: Wrappers.Result
        out30_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_74_keyStoreConfig_)
        d_76_valueOrError2_ = out30_
        if not(not((d_76_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(121,17): " + _dafny.string_of(d_76_valueOrError2_))
        d_75_keyStore_ = (d_76_valueOrError2_).Extract()
        d_77_activeResult_: Wrappers.Result
        out31_: Wrappers.Result
        out31_ = (d_75_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_77_activeResult_ = out31_
        if not((d_77_activeResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWrongLogicalKeyStoreName():
        d_78_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_79_valueOrError0_: Wrappers.Result = None
        out32_: Wrappers.Result
        out32_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_79_valueOrError0_ = out32_
        if not(not((d_79_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(132,18): " + _dafny.string_of(d_79_valueOrError0_))
        d_78_kmsClient_ = (d_79_valueOrError0_).Extract()
        d_80_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_81_valueOrError1_: Wrappers.Result = None
        out33_: Wrappers.Result
        out33_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_81_valueOrError1_ = out33_
        if not(not((d_81_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(133,18): " + _dafny.string_of(d_81_valueOrError1_))
        d_80_ddbClient_ = (d_81_valueOrError1_).Extract()
        d_82_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_82_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_83_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_83_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_82_kmsConfig_, default__.incorrectLogicalName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_80_ddbClient_), Wrappers.Option_Some(d_78_kmsClient_))
        d_84_keyStore_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
        d_85_valueOrError2_: Wrappers.Result = None
        out34_: Wrappers.Result
        out34_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_83_keyStoreConfig_)
        d_85_valueOrError2_ = out34_
        if not(not((d_85_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(146,17): " + _dafny.string_of(d_85_valueOrError2_))
        d_84_keyStore_ = (d_85_valueOrError2_).Extract()
        d_86_activeResult_: Wrappers.Result
        out35_: Wrappers.Result
        out35_ = (d_84_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_86_activeResult_ = out35_
        if not((d_86_activeResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(153,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWithNoClients():
        d_87_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_87_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_88_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_88_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_87_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_89_keyStore_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
        d_90_valueOrError0_: Wrappers.Result = None
        out36_: Wrappers.Result
        out36_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_88_keyStoreConfig_)
        d_90_valueOrError0_ = out36_
        if not(not((d_90_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(169,17): " + _dafny.string_of(d_90_valueOrError0_))
        d_89_keyStore_ = (d_90_valueOrError0_).Extract()
        d_91_activeResult_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
        d_92_valueOrError1_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out37_: Wrappers.Result
        out37_ = (d_89_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_92_valueOrError1_ = out37_
        if not(not((d_92_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(171,21): " + _dafny.string_of(d_92_valueOrError1_))
        d_91_activeResult_ = (d_92_valueOrError1_).Extract()
        if not((len(((d_91_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(176,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def incorrectLogicalName(instance):
        return _dafny.Seq("MySuperAwesomeTableName")
