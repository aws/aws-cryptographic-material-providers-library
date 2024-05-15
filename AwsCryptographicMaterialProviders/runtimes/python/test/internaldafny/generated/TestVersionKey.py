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
import TestConfig as TestConfig
import TestGetKeys as TestGetKeys
import CleanupItems as CleanupItems
import TestCreateKeys as TestCreateKeys

# Module: TestVersionKey

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestVersionKey():
        d_169_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_170_valueOrError0_: Wrappers.Result = None
        out65_: Wrappers.Result
        out65_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_170_valueOrError0_ = out65_
        if not(not((d_170_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(25,21): " + _dafny.string_of(d_170_valueOrError0_))
        d_169_kmsClient_ = (d_170_valueOrError0_).Extract()
        d_171_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_172_valueOrError1_: Wrappers.Result = None
        out66_: Wrappers.Result
        out66_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_172_valueOrError1_ = out66_
        if not(not((d_172_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(26,21): " + _dafny.string_of(d_172_valueOrError1_))
        d_171_ddbClient_ = (d_172_valueOrError1_).Extract()
        d_173_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_173_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_174_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_174_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_173_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_171_ddbClient_), Wrappers.Option_Some(d_169_kmsClient_))
        d_175_keyStore_: KeyStore.KeyStoreClient
        d_176_valueOrError2_: Wrappers.Result = None
        out67_: Wrappers.Result
        out67_ = KeyStore.default__.KeyStore(d_174_keyStoreConfig_)
        d_176_valueOrError2_ = out67_
        if not(not((d_176_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(39,20): " + _dafny.string_of(d_176_valueOrError2_))
        d_175_keyStore_ = (d_176_valueOrError2_).Extract()
        d_177_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_178_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out68_: Wrappers.Result
        out68_ = (d_175_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_None(), Wrappers.Option_None()))
        d_178_valueOrError3_ = out68_
        if not(not((d_178_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(44,23): " + _dafny.string_of(d_178_valueOrError3_))
        d_177_branchKeyId_ = (d_178_valueOrError3_).Extract()
        d_179_oldActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_180_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out69_: Wrappers.Result
        out69_ = (d_175_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_177_branchKeyId_).branchKeyIdentifier))
        d_180_valueOrError4_ = out69_
        if not(not((d_180_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(49,27): " + _dafny.string_of(d_180_valueOrError4_))
        d_179_oldActiveResult_ = (d_180_valueOrError4_).Extract()
        d_181_oldActiveVersion_: _dafny.Seq
        d_182_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_182_valueOrError5_ = UTF8.default__.Decode(((d_179_oldActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_182_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(54,28): " + _dafny.string_of(d_182_valueOrError5_))
        d_181_oldActiveVersion_ = (d_182_valueOrError5_).Extract()
        d_183_versionKeyResult_: AwsCryptographyKeyStoreTypes.VersionKeyOutput
        d_184_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        out70_: Wrappers.Result
        out70_ = (d_175_keyStore_).VersionKey(AwsCryptographyKeyStoreTypes.VersionKeyInput_VersionKeyInput((d_177_branchKeyId_).branchKeyIdentifier))
        d_184_valueOrError6_ = out70_
        if not(not((d_184_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(56,28): " + _dafny.string_of(d_184_valueOrError6_))
        d_183_versionKeyResult_ = (d_184_valueOrError6_).Extract()
        d_185_getBranchKeyVersionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_186_valueOrError7_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out71_: Wrappers.Result
        out71_ = (d_175_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_177_branchKeyId_).branchKeyIdentifier, d_181_oldActiveVersion_))
        d_186_valueOrError7_ = out71_
        if not(not((d_186_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(61,37): " + _dafny.string_of(d_186_valueOrError7_))
        d_185_getBranchKeyVersionResult_ = (d_186_valueOrError7_).Extract()
        d_187_newActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_188_valueOrError8_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out72_: Wrappers.Result
        out72_ = (d_175_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_177_branchKeyId_).branchKeyIdentifier))
        d_188_valueOrError8_ = out72_
        if not(not((d_188_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(69,27): " + _dafny.string_of(d_188_valueOrError8_))
        d_187_newActiveResult_ = (d_188_valueOrError8_).Extract()
        d_189_newActiveVersion_: _dafny.Seq
        d_190_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_190_valueOrError9_ = UTF8.default__.Decode(((d_187_newActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_190_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(74,28): " + _dafny.string_of(d_190_valueOrError9_))
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
        d_191_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_192_valueOrError0_: Wrappers.Result = None
        out73_: Wrappers.Result
        out73_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_192_valueOrError0_ = out73_
        if not(not((d_192_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(93,21): " + _dafny.string_of(d_192_valueOrError0_))
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
        d_195_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_196_valueOrError0_: Wrappers.Result = None
        out75_: Wrappers.Result
        out75_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_196_valueOrError0_ = out75_
        if not(not((d_196_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(116,21): " + _dafny.string_of(d_196_valueOrError0_))
        d_195_ddbClient_ = (d_196_valueOrError0_).Extract()
        d_197_encryptionContext_: _dafny.Map
        d_197_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(_dafny.Seq("!= branchKeyId"), Fixtures.default__.branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        d_198_output_: Wrappers.Result
        out76_: Wrappers.Result
        out76_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(Structure.default__.ToAttributeMap(d_197_encryptionContext_, _dafny.Seq([1])), Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_197_encryptionContext_), _dafny.Seq([2])), Fixtures.default__.branchKeyStoreName, d_195_ddbClient_)
        d_198_output_ = out76_
        if not((d_198_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(134,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

