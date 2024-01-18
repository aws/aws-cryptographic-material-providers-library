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
import TestGetKeys
import CleanupItems

# Module: TestCreateKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestCreateBranchAndBeaconKeys():
        d_96_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_97_valueOrError0_: Wrappers.Result = None
        out41_: Wrappers.Result
        out41_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_97_valueOrError0_ = out41_
        if not(not((d_97_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(25,18): " + _dafny.string_of(d_97_valueOrError0_))
        d_96_kmsClient_ = (d_97_valueOrError0_).Extract()
        d_98_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_99_valueOrError1_: Wrappers.Result = None
        out42_: Wrappers.Result
        out42_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_99_valueOrError1_ = out42_
        if not(not((d_99_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(26,18): " + _dafny.string_of(d_99_valueOrError1_))
        d_98_ddbClient_ = (d_99_valueOrError1_).Extract()
        d_100_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_100_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_101_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_101_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_100_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_98_ddbClient_), Wrappers.Option_Some(d_96_kmsClient_))
        d_102_keyStore_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
        d_103_valueOrError2_: Wrappers.Result = None
        out43_: Wrappers.Result
        out43_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_101_keyStoreConfig_)
        d_103_valueOrError2_ = out43_
        if not(not((d_103_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(39,17): " + _dafny.string_of(d_103_valueOrError2_))
        d_102_keyStore_ = (d_103_valueOrError2_).Extract()
        d_104_branchKeyId_: software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput
        d_105_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput.default())()
        out44_: Wrappers.Result
        out44_ = (d_102_keyStore_).CreateKey(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyInput_CreateKeyInput(Wrappers.Option_None(), Wrappers.Option_None()))
        d_105_valueOrError3_ = out44_
        if not(not((d_105_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(41,20): " + _dafny.string_of(d_105_valueOrError3_))
        d_104_branchKeyId_ = (d_105_valueOrError3_).Extract()
        d_106_beaconKeyResult_: software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput
        d_107_valueOrError4_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput.default())()
        out45_: Wrappers.Result
        out45_ = (d_102_keyStore_).GetBeaconKey(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyInput_GetBeaconKeyInput((d_104_branchKeyId_).branchKeyIdentifier))
        d_107_valueOrError4_ = out45_
        if not(not((d_107_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(46,24): " + _dafny.string_of(d_107_valueOrError4_))
        d_106_beaconKeyResult_ = (d_107_valueOrError4_).Extract()
        d_108_activeResult_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
        d_109_valueOrError5_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out46_: Wrappers.Result
        out46_ = (d_102_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_104_branchKeyId_).branchKeyIdentifier))
        d_109_valueOrError5_ = out46_
        if not(not((d_109_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(51,21): " + _dafny.string_of(d_109_valueOrError5_))
        d_108_activeResult_ = (d_109_valueOrError5_).Extract()
        d_110_branchKeyVersion_: _dafny.Seq
        d_111_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_111_valueOrError6_ = UTF8.default__.Decode(((d_108_activeResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_111_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(56,25): " + _dafny.string_of(d_111_valueOrError6_))
        d_110_branchKeyVersion_ = (d_111_valueOrError6_).Extract()
        d_112_versionResult_: software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput
        d_113_valueOrError7_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        out47_: Wrappers.Result
        out47_ = (d_102_keyStore_).GetBranchKeyVersion(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_104_branchKeyId_).branchKeyIdentifier, d_110_branchKeyVersion_))
        d_113_valueOrError7_ = out47_
        if not(not((d_113_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(57,22): " + _dafny.string_of(d_113_valueOrError7_))
        d_112_versionResult_ = (d_113_valueOrError7_).Extract()
        CleanupItems.default__.DeleteVersion((d_104_branchKeyId_).branchKeyIdentifier, d_110_branchKeyVersion_, d_98_ddbClient_)
        CleanupItems.default__.DeleteActive((d_104_branchKeyId_).branchKeyIdentifier, d_98_ddbClient_)
        if not((((d_106_beaconKeyResult_).beaconKeyMaterials).beaconKey).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((((d_106_beaconKeyResult_).beaconKeyMaterials).beaconKey).value)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(70,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_108_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(71,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_112_versionResult_).branchKeyMaterials).branchKey) == (((d_108_activeResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_112_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_108_activeResult_).branchKeyMaterials).branchKeyIdentifier)) and ((((d_108_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_106_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(73,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_112_versionResult_).branchKeyMaterials).branchKeyVersion) == (((d_108_activeResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(76,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_114_idByteUUID_: _dafny.Seq
        d_115_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_115_valueOrError8_ = UUID.default__.ToByteArray(((d_108_activeResult_).branchKeyMaterials).branchKeyIdentifier)
        if not(not((d_115_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(83,19): " + _dafny.string_of(d_115_valueOrError8_))
        d_114_idByteUUID_ = (d_115_valueOrError8_).Extract()
        d_116_idRoundTrip_: _dafny.Seq
        d_117_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_117_valueOrError9_ = UUID.default__.FromByteArray(d_114_idByteUUID_)
        if not(not((d_117_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(84,20): " + _dafny.string_of(d_117_valueOrError9_))
        d_116_idRoundTrip_ = (d_117_valueOrError9_).Extract()
        if not((d_116_idRoundTrip_) == (((d_108_activeResult_).branchKeyMaterials).branchKeyIdentifier)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(85,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_118_versionString_: _dafny.Seq
        d_119_valueOrError10_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_119_valueOrError10_ = UTF8.default__.Decode(((d_108_activeResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_119_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(91,22): " + _dafny.string_of(d_119_valueOrError10_))
        d_118_versionString_ = (d_119_valueOrError10_).Extract()
        d_120_versionByteUUID_: _dafny.Seq
        d_121_valueOrError11_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_121_valueOrError11_ = UUID.default__.ToByteArray(d_118_versionString_)
        if not(not((d_121_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(92,24): " + _dafny.string_of(d_121_valueOrError11_))
        d_120_versionByteUUID_ = (d_121_valueOrError11_).Extract()
        d_122_versionRoundTrip_: _dafny.Seq
        d_123_valueOrError12_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_123_valueOrError12_ = UUID.default__.FromByteArray(d_120_versionByteUUID_)
        if not(not((d_123_valueOrError12_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(93,25): " + _dafny.string_of(d_123_valueOrError12_))
        d_122_versionRoundTrip_ = (d_123_valueOrError12_).Extract()
        if not((d_122_versionRoundTrip_) == (d_118_versionString_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(94,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCreateOptions():
        d_124_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_125_valueOrError0_: Wrappers.Result = None
        out48_: Wrappers.Result
        out48_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_125_valueOrError0_ = out48_
        if not(not((d_125_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(100,18): " + _dafny.string_of(d_125_valueOrError0_))
        d_124_kmsClient_ = (d_125_valueOrError0_).Extract()
        d_126_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_127_valueOrError1_: Wrappers.Result = None
        out49_: Wrappers.Result
        out49_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_127_valueOrError1_ = out49_
        if not(not((d_127_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(101,18): " + _dafny.string_of(d_127_valueOrError1_))
        d_126_ddbClient_ = (d_127_valueOrError1_).Extract()
        d_128_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_128_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_129_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_129_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_128_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_126_ddbClient_), Wrappers.Option_Some(d_124_kmsClient_))
        d_130_keyStore_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
        d_131_valueOrError2_: Wrappers.Result = None
        out50_: Wrappers.Result
        out50_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_129_keyStoreConfig_)
        d_131_valueOrError2_ = out50_
        if not(not((d_131_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(114,17): " + _dafny.string_of(d_131_valueOrError2_))
        d_130_keyStore_ = (d_131_valueOrError2_).Extract()
        d_132_id_: _dafny.Seq
        d_133_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out51_: Wrappers.Result
        out51_ = UUID.default__.GenerateUUID()
        d_133_valueOrError3_ = out51_
        if not(not((d_133_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(117,11): " + _dafny.string_of(d_133_valueOrError3_))
        d_132_id_ = (d_133_valueOrError3_).Extract()
        d_134_encryptionContext_: _dafny.Map
        d_135_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out52_: Wrappers.Result
        out52_ = default__.EncodeEncryptionContext(_dafny.Map({_dafny.Seq("some"): _dafny.Seq("encryption"), _dafny.Seq("context"): _dafny.Seq("values")}))
        d_135_valueOrError4_ = out52_
        if not(not((d_135_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(119,26): " + _dafny.string_of(d_135_valueOrError4_))
        d_134_encryptionContext_ = (d_135_valueOrError4_).Extract()
        d_136_branchKeyId_: software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput
        d_137_valueOrError5_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput.default())()
        out53_: Wrappers.Result
        out53_ = (d_130_keyStore_).CreateKey(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyInput_CreateKeyInput(Wrappers.Option_Some(d_132_id_), Wrappers.Option_Some(d_134_encryptionContext_)))
        d_137_valueOrError5_ = out53_
        if not(not((d_137_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(124,20): " + _dafny.string_of(d_137_valueOrError5_))
        d_136_branchKeyId_ = (d_137_valueOrError5_).Extract()
        d_138_beaconKeyResult_: software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput
        d_139_valueOrError6_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyOutput.default())()
        out54_: Wrappers.Result
        out54_ = (d_130_keyStore_).GetBeaconKey(software_amazon_cryptography_keystore_internaldafny_types.GetBeaconKeyInput_GetBeaconKeyInput((d_136_branchKeyId_).branchKeyIdentifier))
        d_139_valueOrError6_ = out54_
        if not(not((d_139_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(129,24): " + _dafny.string_of(d_139_valueOrError6_))
        d_138_beaconKeyResult_ = (d_139_valueOrError6_).Extract()
        d_140_activeResult_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
        d_141_valueOrError7_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out55_: Wrappers.Result
        out55_ = (d_130_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_136_branchKeyId_).branchKeyIdentifier))
        d_141_valueOrError7_ = out55_
        if not(not((d_141_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(134,21): " + _dafny.string_of(d_141_valueOrError7_))
        d_140_activeResult_ = (d_141_valueOrError7_).Extract()
        d_142_branchKeyVersion_: _dafny.Seq
        d_143_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_143_valueOrError8_ = UTF8.default__.Decode(((d_140_activeResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_143_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(139,25): " + _dafny.string_of(d_143_valueOrError8_))
        d_142_branchKeyVersion_ = (d_143_valueOrError8_).Extract()
        d_144_versionResult_: software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput
        d_145_valueOrError9_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        out56_: Wrappers.Result
        out56_ = (d_130_keyStore_).GetBranchKeyVersion(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_136_branchKeyId_).branchKeyIdentifier, d_142_branchKeyVersion_))
        d_145_valueOrError9_ = out56_
        if not(not((d_145_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(140,22): " + _dafny.string_of(d_145_valueOrError9_))
        d_144_versionResult_ = (d_145_valueOrError9_).Extract()
        CleanupItems.default__.DeleteVersion((d_136_branchKeyId_).branchKeyIdentifier, d_142_branchKeyVersion_, d_126_ddbClient_)
        CleanupItems.default__.DeleteActive((d_136_branchKeyId_).branchKeyIdentifier, d_126_ddbClient_)
        if not((((d_132_id_) == (((d_144_versionResult_).branchKeyMaterials).branchKeyIdentifier)) and ((((d_144_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_140_activeResult_).branchKeyMaterials).branchKeyIdentifier))) and ((((d_140_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_138_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(153,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_134_encryptionContext_) == (((d_144_versionResult_).branchKeyMaterials).encryptionContext)) and ((((d_144_versionResult_).branchKeyMaterials).encryptionContext) == (((d_140_activeResult_).branchKeyMaterials).encryptionContext))) and ((((d_140_activeResult_).branchKeyMaterials).encryptionContext) == (((d_138_beaconKeyResult_).beaconKeyMaterials).encryptionContext))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(158,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCreateDuplicate():
        d_146_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_147_valueOrError0_: Wrappers.Result = None
        out57_: Wrappers.Result
        out57_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_147_valueOrError0_ = out57_
        if not(not((d_147_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(167,18): " + _dafny.string_of(d_147_valueOrError0_))
        d_146_kmsClient_ = (d_147_valueOrError0_).Extract()
        d_148_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_149_valueOrError1_: Wrappers.Result = None
        out58_: Wrappers.Result
        out58_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_149_valueOrError1_ = out58_
        if not(not((d_149_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(168,18): " + _dafny.string_of(d_149_valueOrError1_))
        d_148_ddbClient_ = (d_149_valueOrError1_).Extract()
        d_150_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_150_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_151_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_151_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_150_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_148_ddbClient_), Wrappers.Option_Some(d_146_kmsClient_))
        d_152_keyStore_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
        d_153_valueOrError2_: Wrappers.Result = None
        out59_: Wrappers.Result
        out59_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_151_keyStoreConfig_)
        d_153_valueOrError2_ = out59_
        if not(not((d_153_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(181,17): " + _dafny.string_of(d_153_valueOrError2_))
        d_152_keyStore_ = (d_153_valueOrError2_).Extract()
        d_154_attempt_: Wrappers.Result
        out60_: Wrappers.Result
        out60_ = (d_152_keyStore_).CreateKey(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyInput_CreateKeyInput(Wrappers.Option_Some(Fixtures.default__.branchKeyId), Wrappers.Option_None()))
        d_154_attempt_ = out60_
        if not((d_154_attempt_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(188,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def InsertingADuplicateWillFail():
        d_155_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_156_valueOrError0_: Wrappers.Result = None
        out61_: Wrappers.Result
        out61_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_156_valueOrError0_ = out61_
        if not(not((d_156_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(193,18): " + _dafny.string_of(d_156_valueOrError0_))
        d_155_ddbClient_ = (d_156_valueOrError0_).Extract()
        d_157_encryptionContext_: _dafny.Map
        d_157_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        d_158_output_: Wrappers.Result
        out62_: Wrappers.Result
        out62_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(Structure.default__.ToAttributeMap(d_157_encryptionContext_, _dafny.Seq([1])), Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_157_encryptionContext_), _dafny.Seq([2])), Structure.default__.ToAttributeMap(Structure.default__.BeaconKeyEncryptionContext(d_157_encryptionContext_), _dafny.Seq([3])), Fixtures.default__.branchKeyStoreName, d_155_ddbClient_)
        d_158_output_ = out62_
        if not((d_158_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(212,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def InsertingADuplicateWillWithADifferentVersionFail():
        d_159_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_160_valueOrError0_: Wrappers.Result = None
        out63_: Wrappers.Result
        out63_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_160_valueOrError0_ = out63_
        if not(not((d_160_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(217,18): " + _dafny.string_of(d_160_valueOrError0_))
        d_159_ddbClient_ = (d_160_valueOrError0_).Extract()
        d_161_encryptionContext_: _dafny.Map
        d_161_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(Fixtures.default__.branchKeyId, _dafny.Seq("!= branchKeyIdActiveVersion"), _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        d_162_output_: Wrappers.Result
        out64_: Wrappers.Result
        out64_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(Structure.default__.ToAttributeMap(d_161_encryptionContext_, _dafny.Seq([1])), Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_161_encryptionContext_), _dafny.Seq([2])), Structure.default__.ToAttributeMap(Structure.default__.BeaconKeyEncryptionContext(d_161_encryptionContext_), _dafny.Seq([3])), Fixtures.default__.branchKeyStoreName, d_159_ddbClient_)
        d_162_output_ = out64_
        if not((d_162_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(236,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def EncodeEncryptionContext(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_163_encodedEncryptionContext_: _dafny.Set
        def iife0_():
            coll0_ = _dafny.Set()
            compr_0_: _dafny.Seq
            for compr_0_ in (input).keys.Elements:
                d_164_k_: _dafny.Seq = compr_0_
                if (d_164_k_) in (input):
                    coll0_ = coll0_.union(_dafny.Set([(UTF8.default__.Encode(d_164_k_), UTF8.default__.Encode((input)[d_164_k_]), d_164_k_)]))
            return _dafny.Set(coll0_)
        d_163_encodedEncryptionContext_ = iife0_()
        
        d_165_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def lambda0_(forall_var_0_):
            def iife1_(_pat_let0_0):
                def iife2_(d_167_encoded_):
                    return ((d_167_encoded_).is_Success) and (((d_166_i_)[2]) == ((d_167_encoded_).value))
                return iife2_(_pat_let0_0)
            d_166_i_: tuple = forall_var_0_
            return not ((d_166_i_) in (d_163_encodedEncryptionContext_)) or (((((d_166_i_)[0]).is_Success) and (((d_166_i_)[1]).is_Success)) and (iife1_(UTF8.default__.Decode(((d_166_i_)[0]).value))))

        d_165_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier((d_163_encodedEncryptionContext_).Elements, True, lambda0_), _dafny.Seq("Unable to encode string"))
        if (d_165_valueOrError0_).IsFailure():
            output = (d_165_valueOrError0_).PropagateFailure()
            return output
        def iife3_():
            coll1_ = _dafny.Map()
            compr_1_: tuple
            for compr_1_ in (d_163_encodedEncryptionContext_).Elements:
                d_168_i_: tuple = compr_1_
                if (d_168_i_) in (d_163_encodedEncryptionContext_):
                    coll1_[((d_168_i_)[0]).value] = ((d_168_i_)[1]).value
            return _dafny.Map(coll1_)
        output = Wrappers.Result_Success(iife3_()
)
        return output

