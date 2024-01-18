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
import TestCreateKeys

# Module: TestVersionKey

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestVersionKey():
        d_169_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_170_valueOrError0_: Wrappers.Result = None
        out65_: Wrappers.Result
        out65_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_170_valueOrError0_ = out65_
        if not(not((d_170_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(25,18): " + _dafny.string_of(d_170_valueOrError0_))
        d_169_kmsClient_ = (d_170_valueOrError0_).Extract()
        d_171_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_172_valueOrError1_: Wrappers.Result = None
        out66_: Wrappers.Result
        out66_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_172_valueOrError1_ = out66_
        if not(not((d_172_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(26,18): " + _dafny.string_of(d_172_valueOrError1_))
        d_171_ddbClient_ = (d_172_valueOrError1_).Extract()
        d_173_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_173_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_174_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_174_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_173_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_171_ddbClient_), Wrappers.Option_Some(d_169_kmsClient_))
        d_175_keyStore_: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient
        d_176_valueOrError2_: Wrappers.Result = None
        out67_: Wrappers.Result
        out67_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_174_keyStoreConfig_)
        d_176_valueOrError2_ = out67_
        if not(not((d_176_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(39,17): " + _dafny.string_of(d_176_valueOrError2_))
        d_175_keyStore_ = (d_176_valueOrError2_).Extract()
        d_177_branchKeyId_: software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput
        d_178_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyOutput.default())()
        out68_: Wrappers.Result
        out68_ = (d_175_keyStore_).CreateKey(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyInput_CreateKeyInput(Wrappers.Option_None(), Wrappers.Option_None()))
        d_178_valueOrError3_ = out68_
        if not(not((d_178_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(44,20): " + _dafny.string_of(d_178_valueOrError3_))
        d_177_branchKeyId_ = (d_178_valueOrError3_).Extract()
        d_179_oldActiveResult_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
        d_180_valueOrError4_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out69_: Wrappers.Result
        out69_ = (d_175_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_177_branchKeyId_).branchKeyIdentifier))
        d_180_valueOrError4_ = out69_
        if not(not((d_180_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(49,24): " + _dafny.string_of(d_180_valueOrError4_))
        d_179_oldActiveResult_ = (d_180_valueOrError4_).Extract()
        d_181_oldActiveVersion_: _dafny.Seq
        d_182_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_182_valueOrError5_ = UTF8.default__.Decode(((d_179_oldActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_182_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(54,25): " + _dafny.string_of(d_182_valueOrError5_))
        d_181_oldActiveVersion_ = (d_182_valueOrError5_).Extract()
        d_183_versionKeyResult_: software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput
        d_184_valueOrError6_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyOutput.default())()
        out70_: Wrappers.Result
        out70_ = (d_175_keyStore_).VersionKey(software_amazon_cryptography_keystore_internaldafny_types.VersionKeyInput_VersionKeyInput((d_177_branchKeyId_).branchKeyIdentifier))
        d_184_valueOrError6_ = out70_
        if not(not((d_184_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(56,25): " + _dafny.string_of(d_184_valueOrError6_))
        d_183_versionKeyResult_ = (d_184_valueOrError6_).Extract()
        d_185_getBranchKeyVersionResult_: software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput
        d_186_valueOrError7_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
        out71_: Wrappers.Result
        out71_ = (d_175_keyStore_).GetBranchKeyVersion(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_177_branchKeyId_).branchKeyIdentifier, d_181_oldActiveVersion_))
        d_186_valueOrError7_ = out71_
        if not(not((d_186_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(61,34): " + _dafny.string_of(d_186_valueOrError7_))
        d_185_getBranchKeyVersionResult_ = (d_186_valueOrError7_).Extract()
        d_187_newActiveResult_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
        d_188_valueOrError8_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
        out72_: Wrappers.Result
        out72_ = (d_175_keyStore_).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_177_branchKeyId_).branchKeyIdentifier))
        d_188_valueOrError8_ = out72_
        if not(not((d_188_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(69,24): " + _dafny.string_of(d_188_valueOrError8_))
        d_187_newActiveResult_ = (d_188_valueOrError8_).Extract()
        d_189_newActiveVersion_: _dafny.Seq
        d_190_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_190_valueOrError9_ = UTF8.default__.Decode(((d_187_newActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_190_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(74,25): " + _dafny.string_of(d_190_valueOrError9_))
        d_189_newActiveVersion_ = (d_190_valueOrError9_).Extract()
        CleanupItems.default__.DeleteVersion((d_177_branchKeyId_).branchKeyIdentifier, d_189_newActiveVersion_, d_171_ddbClient_)
        CleanupItems.default__.DeleteVersion((d_177_branchKeyId_).branchKeyIdentifier, d_181_oldActiveVersion_, d_171_ddbClient_)
        CleanupItems.default__.DeleteActive((d_177_branchKeyId_).branchKeyIdentifier, d_171_ddbClient_)
        if not((((d_185_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) == (((d_179_oldActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(84,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_185_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) == (((d_179_oldActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(85,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_185_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) != (((d_187_newActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_185_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) != (((d_187_newActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(88,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def InsertingADuplicateVersionWillFail():
        d_191_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_192_valueOrError0_: Wrappers.Result = None
        out73_: Wrappers.Result
        out73_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_192_valueOrError0_ = out73_
        if not(not((d_192_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(93,18): " + _dafny.string_of(d_192_valueOrError0_))
        d_191_ddbClient_ = (d_192_valueOrError0_).Extract()
        d_193_encryptionContext_: _dafny.Map
        d_193_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        d_194_output_: Wrappers.Result
        out74_: Wrappers.Result
        out74_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(Structure.default__.ToAttributeMap(d_193_encryptionContext_, _dafny.Seq([1])), Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_193_encryptionContext_), _dafny.Seq([2])), Fixtures.default__.branchKeyStoreName, d_191_ddbClient_)
        d_194_output_ = out74_
        if not((d_194_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(111,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def VersioningANonexistentBranchKeyWillFail():
        d_195_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_196_valueOrError0_: Wrappers.Result = None
        out75_: Wrappers.Result
        out75_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_196_valueOrError0_ = out75_
        if not(not((d_196_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(116,18): " + _dafny.string_of(d_196_valueOrError0_))
        d_195_ddbClient_ = (d_196_valueOrError0_).Extract()
        d_197_encryptionContext_: _dafny.Map
        d_197_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(_dafny.Seq("!= branchKeyId"), Fixtures.default__.branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        d_198_output_: Wrappers.Result
        out76_: Wrappers.Result
        out76_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(Structure.default__.ToAttributeMap(d_197_encryptionContext_, _dafny.Seq([1])), Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_197_encryptionContext_), _dafny.Seq([2])), Fixtures.default__.branchKeyStoreName, d_195_ddbClient_)
        d_198_output_ = out76_
        if not((d_198_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(134,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

