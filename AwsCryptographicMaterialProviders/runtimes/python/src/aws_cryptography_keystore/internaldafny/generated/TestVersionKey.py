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
import TestCreateKeys

# assert "TestVersionKey" == __name__
TestVersionKey = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestVersionKey():
        d_560_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_561_valueOrError0_: Wrappers.Result = None
        out155_: Wrappers.Result
        out155_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_561_valueOrError0_ = out155_
        if not(not((d_561_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(25,18): " + _dafny.string_of(d_561_valueOrError0_))
        d_560_kmsClient_ = (d_561_valueOrError0_).Extract()
        d_562_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_563_valueOrError1_: Wrappers.Result = None
        out156_: Wrappers.Result
        out156_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_563_valueOrError1_ = out156_
        if not(not((d_563_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(26,18): " + _dafny.string_of(d_563_valueOrError1_))
        d_562_ddbClient_ = (d_563_valueOrError1_).Extract()
        d_564_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_564_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((Fixtures.default__).keyArn)
        d_565_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_565_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((Fixtures.default__).branchKeyStoreName, d_564_kmsConfig_, (Fixtures.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_562_ddbClient_), Wrappers.Option_Some(d_560_kmsClient_))
        d_566_keyStore_: software_amazon_cryptography_keystore_internaldafny.KeyStoreClient
        d_567_valueOrError2_: Wrappers.Result = None
        out157_: Wrappers.Result
        out157_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_565_keyStoreConfig_)
        d_567_valueOrError2_ = out157_
        if not(not((d_567_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(39,17): " + _dafny.string_of(d_567_valueOrError2_))
        d_566_keyStore_ = (d_567_valueOrError2_).Extract()
        d_568_branchKeyId_: software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput
        d_569_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput.default())()
        out158_: Wrappers.Result
        out158_ = (d_566_keyStore_).CreateKey(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyInput_CreateKeyInput(Wrappers.Option_None(), Wrappers.Option_None()))
        d_569_valueOrError3_ = out158_
        if not(not((d_569_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(44,20): " + _dafny.string_of(d_569_valueOrError3_))
        d_568_branchKeyId_ = (d_569_valueOrError3_).Extract()
        d_570_oldActiveResult_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
        d_571_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out159_: Wrappers.Result
        out159_ = (d_566_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_568_branchKeyId_).branchKeyIdentifier))
        d_571_valueOrError4_ = out159_
        if not(not((d_571_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(49,24): " + _dafny.string_of(d_571_valueOrError4_))
        d_570_oldActiveResult_ = (d_571_valueOrError4_).Extract()
        d_572_oldActiveVersion_: _dafny.Seq
        d_573_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_573_valueOrError5_ = UTF8.default__.Decode(((d_570_oldActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_573_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(54,25): " + _dafny.string_of(d_573_valueOrError5_))
        d_572_oldActiveVersion_ = (d_573_valueOrError5_).Extract()
        d_574_versionKeyResult_: software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput
        d_575_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput.default())()
        out160_: Wrappers.Result
        out160_ = (d_566_keyStore_).VersionKey(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyInput_VersionKeyInput((d_568_branchKeyId_).branchKeyIdentifier))
        d_575_valueOrError6_ = out160_
        if not(not((d_575_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(56,25): " + _dafny.string_of(d_575_valueOrError6_))
        d_574_versionKeyResult_ = (d_575_valueOrError6_).Extract()
        d_576_getBranchKeyVersionResult_: software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput
        d_577_valueOrError7_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        out161_: Wrappers.Result
        out161_ = (d_566_keyStore_).GetBranchKeyVersion(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_568_branchKeyId_).branchKeyIdentifier, d_572_oldActiveVersion_))
        d_577_valueOrError7_ = out161_
        if not(not((d_577_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(61,34): " + _dafny.string_of(d_577_valueOrError7_))
        d_576_getBranchKeyVersionResult_ = (d_577_valueOrError7_).Extract()
        d_578_newActiveResult_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
        d_579_valueOrError8_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out162_: Wrappers.Result
        out162_ = (d_566_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_568_branchKeyId_).branchKeyIdentifier))
        d_579_valueOrError8_ = out162_
        if not(not((d_579_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(69,24): " + _dafny.string_of(d_579_valueOrError8_))
        d_578_newActiveResult_ = (d_579_valueOrError8_).Extract()
        d_580_newActiveVersion_: _dafny.Seq
        d_581_valueOrError9_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_581_valueOrError9_ = UTF8.default__.Decode(((d_578_newActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_581_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(74,25): " + _dafny.string_of(d_581_valueOrError9_))
        d_580_newActiveVersion_ = (d_581_valueOrError9_).Extract()
        CleanupItems.default__.DeleteVersion((d_568_branchKeyId_).branchKeyIdentifier, d_580_newActiveVersion_, d_562_ddbClient_)
        CleanupItems.default__.DeleteVersion((d_568_branchKeyId_).branchKeyIdentifier, d_572_oldActiveVersion_, d_562_ddbClient_)
        CleanupItems.default__.DeleteActive((d_568_branchKeyId_).branchKeyIdentifier, d_562_ddbClient_)
        if not((((d_576_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) == (((d_570_oldActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(84,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_576_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) == (((d_570_oldActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(85,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_576_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) != (((d_578_newActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_576_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) != (((d_578_newActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(88,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def InsertingADuplicateVersionWillFail():
        d_582_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_583_valueOrError0_: Wrappers.Result = None
        out163_: Wrappers.Result
        out163_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_583_valueOrError0_ = out163_
        if not(not((d_583_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(93,18): " + _dafny.string_of(d_583_valueOrError0_))
        d_582_ddbClient_ = (d_583_valueOrError0_).Extract()
        d_584_encryptionContext_: _dafny.Map
        d_584_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext((Fixtures.default__).branchKeyId, (Fixtures.default__).branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), (Fixtures.default__).keyArn, _dafny.Map({}))
        d_585_output_: Wrappers.Result
        out164_: Wrappers.Result
        out164_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(Structure.default__.ToAttributeMap(d_584_encryptionContext_, _dafny.Seq([1])), Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_584_encryptionContext_), _dafny.Seq([2])), (Fixtures.default__).branchKeyStoreName, d_582_ddbClient_)
        d_585_output_ = out164_
        if not((d_585_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(111,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def VersioningANonexistentBranchKeyWillFail():
        d_586_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_587_valueOrError0_: Wrappers.Result = None
        out165_: Wrappers.Result
        out165_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_587_valueOrError0_ = out165_
        if not(not((d_587_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(116,18): " + _dafny.string_of(d_587_valueOrError0_))
        d_586_ddbClient_ = (d_587_valueOrError0_).Extract()
        d_588_encryptionContext_: _dafny.Map
        d_588_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(_dafny.Seq("!= branchKeyId"), (Fixtures.default__).branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), (Fixtures.default__).keyArn, _dafny.Map({}))
        d_589_output_: Wrappers.Result
        out166_: Wrappers.Result
        out166_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(Structure.default__.ToAttributeMap(d_588_encryptionContext_, _dafny.Seq([1])), Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_588_encryptionContext_), _dafny.Seq([2])), (Fixtures.default__).branchKeyStoreName, d_586_ddbClient_)
        d_589_output_ = out166_
        if not((d_589_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(134,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

