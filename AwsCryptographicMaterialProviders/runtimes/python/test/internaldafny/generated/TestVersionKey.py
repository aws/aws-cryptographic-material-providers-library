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
import standard_library.internaldafny.generated.Actions as Actions
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
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
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
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
import TestDiscoveryGetKeys as TestDiscoveryGetKeys
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
        d_284_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_285_valueOrError0_: Wrappers.Result = None
        out110_: Wrappers.Result
        out110_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_285_valueOrError0_ = out110_
        if not(not((d_285_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(26,21): " + _dafny.string_of(d_285_valueOrError0_))
        d_284_kmsClient_ = (d_285_valueOrError0_).Extract()
        d_286_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_287_valueOrError1_: Wrappers.Result = None
        out111_: Wrappers.Result
        out111_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_287_valueOrError1_ = out111_
        if not(not((d_287_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(27,21): " + _dafny.string_of(d_287_valueOrError1_))
        d_286_ddbClient_ = (d_287_valueOrError1_).Extract()
        d_288_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_288_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        if not(ComAmazonawsDynamodbTypes.default__.IsValid__TableName(Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(29,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_289_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_289_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_288_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_286_ddbClient_), Wrappers.Option_Some(d_284_kmsClient_))
        d_290_keyStore_: KeyStore.KeyStoreClient
        d_291_valueOrError2_: Wrappers.Result = None
        out112_: Wrappers.Result
        out112_ = KeyStore.default__.KeyStore(d_289_keyStoreConfig_)
        d_291_valueOrError2_ = out112_
        if not(not((d_291_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(41,20): " + _dafny.string_of(d_291_valueOrError2_))
        d_290_keyStore_ = (d_291_valueOrError2_).Extract()
        d_292_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_293_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out113_: Wrappers.Result
        out113_ = (d_290_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_None(), Wrappers.Option_None()))
        d_293_valueOrError3_ = out113_
        if not(not((d_293_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(46,23): " + _dafny.string_of(d_293_valueOrError3_))
        d_292_branchKeyId_ = (d_293_valueOrError3_).Extract()
        d_294_oldActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_295_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out114_: Wrappers.Result
        out114_ = (d_290_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_292_branchKeyId_).branchKeyIdentifier))
        d_295_valueOrError4_ = out114_
        if not(not((d_295_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(51,27): " + _dafny.string_of(d_295_valueOrError4_))
        d_294_oldActiveResult_ = (d_295_valueOrError4_).Extract()
        d_296_oldActiveVersion_: _dafny.Seq
        d_297_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_297_valueOrError5_ = UTF8.default__.Decode(((d_294_oldActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_297_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(56,28): " + _dafny.string_of(d_297_valueOrError5_))
        d_296_oldActiveVersion_ = (d_297_valueOrError5_).Extract()
        d_298_versionKeyResult_: AwsCryptographyKeyStoreTypes.VersionKeyOutput
        d_299_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        out115_: Wrappers.Result
        out115_ = (d_290_keyStore_).VersionKey(AwsCryptographyKeyStoreTypes.VersionKeyInput_VersionKeyInput((d_292_branchKeyId_).branchKeyIdentifier))
        d_299_valueOrError6_ = out115_
        if not(not((d_299_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(58,28): " + _dafny.string_of(d_299_valueOrError6_))
        d_298_versionKeyResult_ = (d_299_valueOrError6_).Extract()
        d_300_getBranchKeyVersionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_301_valueOrError7_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out116_: Wrappers.Result
        out116_ = (d_290_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_292_branchKeyId_).branchKeyIdentifier, d_296_oldActiveVersion_))
        d_301_valueOrError7_ = out116_
        if not(not((d_301_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(63,37): " + _dafny.string_of(d_301_valueOrError7_))
        d_300_getBranchKeyVersionResult_ = (d_301_valueOrError7_).Extract()
        d_302_newActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_303_valueOrError8_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out117_: Wrappers.Result
        out117_ = (d_290_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_292_branchKeyId_).branchKeyIdentifier))
        d_303_valueOrError8_ = out117_
        if not(not((d_303_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(71,27): " + _dafny.string_of(d_303_valueOrError8_))
        d_302_newActiveResult_ = (d_303_valueOrError8_).Extract()
        d_304_newActiveVersion_: _dafny.Seq
        d_305_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_305_valueOrError9_ = UTF8.default__.Decode(((d_302_newActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_305_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(76,28): " + _dafny.string_of(d_305_valueOrError9_))
        d_304_newActiveVersion_ = (d_305_valueOrError9_).Extract()
        CleanupItems.default__.DeleteVersion((d_292_branchKeyId_).branchKeyIdentifier, d_304_newActiveVersion_, d_286_ddbClient_)
        CleanupItems.default__.DeleteVersion((d_292_branchKeyId_).branchKeyIdentifier, d_296_oldActiveVersion_, d_286_ddbClient_)
        CleanupItems.default__.DeleteActive((d_292_branchKeyId_).branchKeyIdentifier, d_286_ddbClient_)
        if not((((d_300_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) == (((d_294_oldActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(86,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_300_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) == (((d_294_oldActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_300_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) != (((d_302_newActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(89,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_300_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) != (((d_302_newActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(90,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestVersionKeyWithEC():
        d_306_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_307_valueOrError0_: Wrappers.Result = None
        out118_: Wrappers.Result
        out118_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_307_valueOrError0_ = out118_
        if not(not((d_307_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(95,21): " + _dafny.string_of(d_307_valueOrError0_))
        d_306_kmsClient_ = (d_307_valueOrError0_).Extract()
        d_308_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_309_valueOrError1_: Wrappers.Result = None
        out119_: Wrappers.Result
        out119_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_309_valueOrError1_ = out119_
        if not(not((d_309_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(96,21): " + _dafny.string_of(d_309_valueOrError1_))
        d_308_ddbClient_ = (d_309_valueOrError1_).Extract()
        d_310_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_310_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        if not(ComAmazonawsDynamodbTypes.default__.IsValid__TableName(Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(98,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_311_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_311_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_310_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_308_ddbClient_), Wrappers.Option_Some(d_306_kmsClient_))
        d_312_keyStore_: KeyStore.KeyStoreClient
        d_313_valueOrError2_: Wrappers.Result = None
        out120_: Wrappers.Result
        out120_ = KeyStore.default__.KeyStore(d_311_keyStoreConfig_)
        d_313_valueOrError2_ = out120_
        if not(not((d_313_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(110,20): " + _dafny.string_of(d_313_valueOrError2_))
        d_312_keyStore_ = (d_313_valueOrError2_).Extract()
        d_314_id_: _dafny.Seq
        d_315_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out121_: Wrappers.Result
        out121_ = UUID.default__.GenerateUUID()
        d_315_valueOrError3_ = out121_
        if not(not((d_315_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(115,14): " + _dafny.string_of(d_315_valueOrError3_))
        d_314_id_ = (d_315_valueOrError3_).Extract()
        d_316_customEC_: _dafny.Map
        d_316_customEC_ = _dafny.Map({_dafny.Seq("some"): _dafny.Seq("encryption"), _dafny.Seq("context"): _dafny.Seq("values")})
        d_317_encryptionContext_: _dafny.Map
        d_318_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out122_: Wrappers.Result
        out122_ = Fixtures.default__.EncodeEncryptionContext(d_316_customEC_)
        d_318_valueOrError4_ = out122_
        if not(not((d_318_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(121,29): " + _dafny.string_of(d_318_valueOrError4_))
        d_317_encryptionContext_ = (d_318_valueOrError4_).Extract()
        d_319_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_320_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out123_: Wrappers.Result
        out123_ = (d_312_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_Some(d_314_id_), Wrappers.Option_Some(d_317_encryptionContext_)))
        d_320_valueOrError5_ = out123_
        if not(not((d_320_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(123,23): " + _dafny.string_of(d_320_valueOrError5_))
        d_319_branchKeyId_ = (d_320_valueOrError5_).Extract()
        if not(((d_319_branchKeyId_).branchKeyIdentifier) == (d_314_id_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(128,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_321_oldActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_322_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out124_: Wrappers.Result
        out124_ = (d_312_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_319_branchKeyId_).branchKeyIdentifier))
        d_322_valueOrError6_ = out124_
        if not(not((d_322_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(130,27): " + _dafny.string_of(d_322_valueOrError6_))
        d_321_oldActiveResult_ = (d_322_valueOrError6_).Extract()
        d_323_mat_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_323_mat_ = (d_321_oldActiveResult_).branchKeyMaterials
        if not(((d_323_mat_).branchKeyIdentifier) == (d_314_id_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(135,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_324_matEC_: _dafny.Map
        d_325_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out125_: Wrappers.Result
        out125_ = Fixtures.default__.DecodeEncryptionContext((d_323_mat_).encryptionContext)
        d_325_valueOrError7_ = out125_
        if not(not((d_325_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(136,17): " + _dafny.string_of(d_325_valueOrError7_))
        d_324_matEC_ = (d_325_valueOrError7_).Extract()
        if not((d_324_matEC_) == (d_316_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(137,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_326_oldActiveVersion_: _dafny.Seq
        d_327_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_327_valueOrError8_ = UTF8.default__.Decode(((d_321_oldActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_327_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(139,28): " + _dafny.string_of(d_327_valueOrError8_))
        d_326_oldActiveVersion_ = (d_327_valueOrError8_).Extract()
        d_328_versionKeyResult_: AwsCryptographyKeyStoreTypes.VersionKeyOutput
        d_329_valueOrError9_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        out126_: Wrappers.Result
        out126_ = (d_312_keyStore_).VersionKey(AwsCryptographyKeyStoreTypes.VersionKeyInput_VersionKeyInput((d_319_branchKeyId_).branchKeyIdentifier))
        d_329_valueOrError9_ = out126_
        if not(not((d_329_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(141,28): " + _dafny.string_of(d_329_valueOrError9_))
        d_328_versionKeyResult_ = (d_329_valueOrError9_).Extract()
        d_330_getBranchKeyVersionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_331_valueOrError10_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out127_: Wrappers.Result
        out127_ = (d_312_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_319_branchKeyId_).branchKeyIdentifier, d_326_oldActiveVersion_))
        d_331_valueOrError10_ = out127_
        if not(not((d_331_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(146,37): " + _dafny.string_of(d_331_valueOrError10_))
        d_330_getBranchKeyVersionResult_ = (d_331_valueOrError10_).Extract()
        d_332_mat2_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_332_mat2_ = (d_330_getBranchKeyVersionResult_).branchKeyMaterials
        if not(((d_323_mat_).branchKeyIdentifier) == (d_314_id_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(154,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_333_mat2EC_: _dafny.Map
        d_334_valueOrError11_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out128_: Wrappers.Result
        out128_ = Fixtures.default__.DecodeEncryptionContext((d_323_mat_).encryptionContext)
        d_334_valueOrError11_ = out128_
        if not(not((d_334_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(155,18): " + _dafny.string_of(d_334_valueOrError11_))
        d_333_mat2EC_ = (d_334_valueOrError11_).Extract()
        if not((d_333_mat2EC_) == (d_316_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(156,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_332_mat2_).branchKeyVersion) == ((d_323_mat_).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(157,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_335_newActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_336_valueOrError12_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out129_: Wrappers.Result
        out129_ = (d_312_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_319_branchKeyId_).branchKeyIdentifier))
        d_336_valueOrError12_ = out129_
        if not(not((d_336_valueOrError12_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(159,27): " + _dafny.string_of(d_336_valueOrError12_))
        d_335_newActiveResult_ = (d_336_valueOrError12_).Extract()
        d_337_mat3_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_337_mat3_ = (d_335_newActiveResult_).branchKeyMaterials
        if not(((d_323_mat_).branchKeyIdentifier) == (d_314_id_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(164,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_338_mat3EC_: _dafny.Map
        d_339_valueOrError13_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out130_: Wrappers.Result
        out130_ = Fixtures.default__.DecodeEncryptionContext((d_323_mat_).encryptionContext)
        d_339_valueOrError13_ = out130_
        if not(not((d_339_valueOrError13_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(165,18): " + _dafny.string_of(d_339_valueOrError13_))
        d_338_mat3EC_ = (d_339_valueOrError13_).Extract()
        if not((d_338_mat3EC_) == (d_316_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(166,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_337_mat3_).branchKeyVersion) != ((d_323_mat_).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(167,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_340_newActiveVersion_: _dafny.Seq
        d_341_valueOrError14_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_341_valueOrError14_ = UTF8.default__.Decode(((d_335_newActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_341_valueOrError14_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(169,28): " + _dafny.string_of(d_341_valueOrError14_))
        d_340_newActiveVersion_ = (d_341_valueOrError14_).Extract()
        if not((d_340_newActiveVersion_) != (d_326_oldActiveVersion_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(171,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        CleanupItems.default__.DeleteVersion((d_319_branchKeyId_).branchKeyIdentifier, d_340_newActiveVersion_, d_308_ddbClient_)
        CleanupItems.default__.DeleteVersion((d_319_branchKeyId_).branchKeyIdentifier, d_326_oldActiveVersion_, d_308_ddbClient_)
        CleanupItems.default__.DeleteActive((d_319_branchKeyId_).branchKeyIdentifier, d_308_ddbClient_)
        if not((((d_330_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) == (((d_321_oldActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(181,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_330_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) == (((d_321_oldActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(182,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_330_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) != (((d_335_newActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(184,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_330_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) != (((d_335_newActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(185,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_324_matEC_) == (d_316_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(192,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_333_mat2EC_) == (d_316_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(193,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_338_mat3EC_) == (d_316_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(194,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestMrkVersionKey():
        d_342_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_343_valueOrError0_: Wrappers.Result = None
        out131_: Wrappers.Result
        out131_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_343_valueOrError0_ = out131_
        if not(not((d_343_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(199,21): " + _dafny.string_of(d_343_valueOrError0_))
        d_342_ddbClient_ = (d_343_valueOrError0_).Extract()
        d_344_eastKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_344_eastKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsMrkConfigEast, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_342_ddbClient_), Wrappers.Option_None())
        d_345_westKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_345_westKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsMrkConfigWest, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_342_ddbClient_), Wrappers.Option_None())
        d_346_eastKeyStore_: KeyStore.KeyStoreClient
        d_347_valueOrError1_: Wrappers.Result = None
        out132_: Wrappers.Result
        out132_ = KeyStore.default__.KeyStore(d_344_eastKeyStoreConfig_)
        d_347_valueOrError1_ = out132_
        if not(not((d_347_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(219,24): " + _dafny.string_of(d_347_valueOrError1_))
        d_346_eastKeyStore_ = (d_347_valueOrError1_).Extract()
        d_348_westKeyStore_: KeyStore.KeyStoreClient
        d_349_valueOrError2_: Wrappers.Result = None
        out133_: Wrappers.Result
        out133_ = KeyStore.default__.KeyStore(d_345_westKeyStoreConfig_)
        d_349_valueOrError2_ = out133_
        if not(not((d_349_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(220,24): " + _dafny.string_of(d_349_valueOrError2_))
        d_348_westKeyStore_ = (d_349_valueOrError2_).Extract()
        d_350_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_351_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out134_: Wrappers.Result
        out134_ = (d_348_westKeyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_None(), Wrappers.Option_None()))
        d_351_valueOrError3_ = out134_
        if not(not((d_351_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(225,23): " + _dafny.string_of(d_351_valueOrError3_))
        d_350_branchKeyId_ = (d_351_valueOrError3_).Extract()
        d_352_oldActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_353_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out135_: Wrappers.Result
        out135_ = (d_348_westKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_350_branchKeyId_).branchKeyIdentifier))
        d_353_valueOrError4_ = out135_
        if not(not((d_353_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(230,27): " + _dafny.string_of(d_353_valueOrError4_))
        d_352_oldActiveResult_ = (d_353_valueOrError4_).Extract()
        d_354_oldActiveVersion_: _dafny.Seq
        d_355_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_355_valueOrError5_ = UTF8.default__.Decode(((d_352_oldActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_355_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(235,28): " + _dafny.string_of(d_355_valueOrError5_))
        d_354_oldActiveVersion_ = (d_355_valueOrError5_).Extract()
        d_356_versionKeyResult_: AwsCryptographyKeyStoreTypes.VersionKeyOutput
        d_357_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        out136_: Wrappers.Result
        out136_ = (d_346_eastKeyStore_).VersionKey(AwsCryptographyKeyStoreTypes.VersionKeyInput_VersionKeyInput((d_350_branchKeyId_).branchKeyIdentifier))
        d_357_valueOrError6_ = out136_
        if not(not((d_357_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(238,28): " + _dafny.string_of(d_357_valueOrError6_))
        d_356_versionKeyResult_ = (d_357_valueOrError6_).Extract()
        d_358_getBranchKeyVersionResultWest_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_359_valueOrError7_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out137_: Wrappers.Result
        out137_ = (d_348_westKeyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_350_branchKeyId_).branchKeyIdentifier, d_354_oldActiveVersion_))
        d_359_valueOrError7_ = out137_
        if not(not((d_359_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(243,41): " + _dafny.string_of(d_359_valueOrError7_))
        d_358_getBranchKeyVersionResultWest_ = (d_359_valueOrError7_).Extract()
        d_360_getBranchKeyVersionResultEast_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_361_valueOrError8_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out138_: Wrappers.Result
        out138_ = (d_346_eastKeyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_350_branchKeyId_).branchKeyIdentifier, d_354_oldActiveVersion_))
        d_361_valueOrError8_ = out138_
        if not(not((d_361_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(251,41): " + _dafny.string_of(d_361_valueOrError8_))
        d_360_getBranchKeyVersionResultEast_ = (d_361_valueOrError8_).Extract()
        if not((d_358_getBranchKeyVersionResultWest_) == (d_360_getBranchKeyVersionResultEast_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(259,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_362_newActiveResultWest_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_363_valueOrError9_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out139_: Wrappers.Result
        out139_ = (d_348_westKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_350_branchKeyId_).branchKeyIdentifier))
        d_363_valueOrError9_ = out139_
        if not(not((d_363_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(261,31): " + _dafny.string_of(d_363_valueOrError9_))
        d_362_newActiveResultWest_ = (d_363_valueOrError9_).Extract()
        d_364_newActiveResultEast_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_365_valueOrError10_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out140_: Wrappers.Result
        out140_ = (d_346_eastKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_350_branchKeyId_).branchKeyIdentifier))
        d_365_valueOrError10_ = out140_
        if not(not((d_365_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(265,31): " + _dafny.string_of(d_365_valueOrError10_))
        d_364_newActiveResultEast_ = (d_365_valueOrError10_).Extract()
        if not((d_362_newActiveResultWest_) == (d_364_newActiveResultEast_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(270,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_366_newActiveVersionWest_: _dafny.Seq
        d_367_valueOrError11_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_367_valueOrError11_ = UTF8.default__.Decode(((d_362_newActiveResultWest_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_367_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(272,32): " + _dafny.string_of(d_367_valueOrError11_))
        d_366_newActiveVersionWest_ = (d_367_valueOrError11_).Extract()
        d_368_newActiveVersionEast_: _dafny.Seq
        d_369_valueOrError12_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_369_valueOrError12_ = UTF8.default__.Decode(((d_364_newActiveResultEast_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_369_valueOrError12_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(273,32): " + _dafny.string_of(d_369_valueOrError12_))
        d_368_newActiveVersionEast_ = (d_369_valueOrError12_).Extract()
        if not((d_366_newActiveVersionWest_) == (d_368_newActiveVersionEast_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(274,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        CleanupItems.default__.DeleteVersion((d_350_branchKeyId_).branchKeyIdentifier, d_368_newActiveVersionEast_, d_342_ddbClient_)
        CleanupItems.default__.DeleteVersion((d_350_branchKeyId_).branchKeyIdentifier, d_354_oldActiveVersion_, d_342_ddbClient_)
        CleanupItems.default__.DeleteActive((d_350_branchKeyId_).branchKeyIdentifier, d_342_ddbClient_)
        if not((((d_360_getBranchKeyVersionResultEast_).branchKeyMaterials).branchKeyVersion) == (((d_352_oldActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(284,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_360_getBranchKeyVersionResultEast_).branchKeyMaterials).branchKey) == (((d_352_oldActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(285,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_360_getBranchKeyVersionResultEast_).branchKeyMaterials).branchKeyVersion) != (((d_364_newActiveResultEast_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(287,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_360_getBranchKeyVersionResultEast_).branchKeyMaterials).branchKey) != (((d_364_newActiveResultEast_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(288,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def InsertingADuplicateVersionWillFail():
        d_370_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_371_valueOrError0_: Wrappers.Result = None
        out141_: Wrappers.Result
        out141_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_371_valueOrError0_ = out141_
        if not(not((d_371_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(299,21): " + _dafny.string_of(d_371_valueOrError0_))
        d_370_ddbClient_ = (d_371_valueOrError0_).Extract()
        if not((0) < (len(Fixtures.default__.branchKeyId))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(301,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((0) < (len(Fixtures.default__.branchKeyIdActiveVersion))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(302,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_372_customEncryptionContext_: _dafny.Map
        d_372_customEncryptionContext_ = _dafny.Map({})
        def lambda2_(forall_var_2_):
            d_373_k_: _dafny.Seq = forall_var_2_
            return not ((d_373_k_) in (d_372_customEncryptionContext_)) or (ComAmazonawsDynamodbTypes.default__.IsValid__AttributeName((Structure.default__.ENCRYPTION__CONTEXT__PREFIX) + (d_373_k_)))

        if not(_dafny.quantifier((d_372_customEncryptionContext_).keys.Elements, True, lambda2_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(304,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_374_encryptionContext_: _dafny.Map
        d_374_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        if not(ComAmazonawsDynamodbTypes.default__.IsValid__TableName(Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(315,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_375_myBranchKeyStoreName_: _dafny.Seq
        d_375_myBranchKeyStoreName_ = Fixtures.default__.branchKeyStoreName
        d_376_versionBranchKeyItem_: _dafny.Map
        d_376_versionBranchKeyItem_ = Structure.default__.ToAttributeMap(d_374_encryptionContext_, _dafny.Seq([1]))
        d_377_activeBranchKeyItem_: _dafny.Map
        d_377_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_374_encryptionContext_), _dafny.Seq([2]))
        if not(((d_377_activeBranchKeyItem_)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]) == ((d_376_versionBranchKeyItem_)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD])):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(319,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_377_activeBranchKeyItem_)[Structure.default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]) == ((d_376_versionBranchKeyItem_)[Structure.default__.TYPE__FIELD])):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(320,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_378_output_: Wrappers.Result
        out142_: Wrappers.Result
        out142_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(d_376_versionBranchKeyItem_, d_377_activeBranchKeyItem_, d_375_myBranchKeyStoreName_, d_370_ddbClient_)
        d_378_output_ = out142_
        if not((d_378_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(329,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def VersioningANonexistentBranchKeyWillFail():
        d_379_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_380_valueOrError0_: Wrappers.Result = None
        out143_: Wrappers.Result
        out143_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_380_valueOrError0_ = out143_
        if not(not((d_380_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(335,21): " + _dafny.string_of(d_380_valueOrError0_))
        d_379_ddbClient_ = (d_380_valueOrError0_).Extract()
        d_381_encryptionContext_: _dafny.Map
        d_381_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(_dafny.Seq("!= branchKeyId"), Fixtures.default__.branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        d_382_versionBranchKeyItem_: _dafny.Map
        d_382_versionBranchKeyItem_ = Structure.default__.ToAttributeMap(d_381_encryptionContext_, _dafny.Seq([1]))
        d_383_activeBranchKeyItem_: _dafny.Map
        d_383_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_381_encryptionContext_), _dafny.Seq([2]))
        if not(((d_383_activeBranchKeyItem_)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]) == ((d_382_versionBranchKeyItem_)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD])):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(348,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_383_activeBranchKeyItem_)[Structure.default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]) == ((d_382_versionBranchKeyItem_)[Structure.default__.TYPE__FIELD])):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(349,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(ComAmazonawsDynamodbTypes.default__.IsValid__TableName(Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(350,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_384_myBranchKeyStoreName_: _dafny.Seq
        d_384_myBranchKeyStoreName_ = Fixtures.default__.branchKeyStoreName
        d_385_output_: Wrappers.Result
        out144_: Wrappers.Result
        out144_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(d_382_versionBranchKeyItem_, d_383_activeBranchKeyItem_, d_384_myBranchKeyStoreName_, d_379_ddbClient_)
        d_385_output_ = out144_
        if not((d_385_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(360,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

