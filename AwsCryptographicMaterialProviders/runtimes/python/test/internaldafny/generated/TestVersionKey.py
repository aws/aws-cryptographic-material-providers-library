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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
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
import aws_cryptographic_materialproviders.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.Utils as Utils
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
import TestLyingBranchKey as TestLyingBranchKey
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
        d_319_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_320_valueOrError0_: Wrappers.Result = None
        out126_: Wrappers.Result
        out126_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_320_valueOrError0_ = out126_
        if not(not((d_320_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(27,21): " + _dafny.string_of(d_320_valueOrError0_))
        d_319_kmsClient_ = (d_320_valueOrError0_).Extract()
        d_321_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_322_valueOrError1_: Wrappers.Result = None
        out127_: Wrappers.Result
        out127_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_322_valueOrError1_ = out127_
        if not(not((d_322_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(28,21): " + _dafny.string_of(d_322_valueOrError1_))
        d_321_ddbClient_ = (d_322_valueOrError1_).Extract()
        d_323_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_323_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        if not(ComAmazonawsDynamodbTypes.default__.IsValid__TableName(Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(30,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_324_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_324_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_323_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_321_ddbClient_), Wrappers.Option_Some(d_319_kmsClient_))
        d_325_keyStore_: KeyStore.KeyStoreClient
        d_326_valueOrError2_: Wrappers.Result = None
        out128_: Wrappers.Result
        out128_ = KeyStore.default__.KeyStore(d_324_keyStoreConfig_)
        d_326_valueOrError2_ = out128_
        if not(not((d_326_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(42,20): " + _dafny.string_of(d_326_valueOrError2_))
        d_325_keyStore_ = (d_326_valueOrError2_).Extract()
        d_327_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_328_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out129_: Wrappers.Result
        out129_ = (d_325_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_None(), Wrappers.Option_None()))
        d_328_valueOrError3_ = out129_
        if not(not((d_328_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(47,23): " + _dafny.string_of(d_328_valueOrError3_))
        d_327_branchKeyId_ = (d_328_valueOrError3_).Extract()
        d_329_oldActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_330_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out130_: Wrappers.Result
        out130_ = (d_325_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_327_branchKeyId_).branchKeyIdentifier))
        d_330_valueOrError4_ = out130_
        if not(not((d_330_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(52,27): " + _dafny.string_of(d_330_valueOrError4_))
        d_329_oldActiveResult_ = (d_330_valueOrError4_).Extract()
        d_331_oldActiveVersion_: _dafny.Seq
        d_332_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_332_valueOrError5_ = UTF8.default__.Decode(((d_329_oldActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_332_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(57,28): " + _dafny.string_of(d_332_valueOrError5_))
        d_331_oldActiveVersion_ = (d_332_valueOrError5_).Extract()
        d_333_versionKeyResult_: AwsCryptographyKeyStoreTypes.VersionKeyOutput
        d_334_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        out131_: Wrappers.Result
        out131_ = (d_325_keyStore_).VersionKey(AwsCryptographyKeyStoreTypes.VersionKeyInput_VersionKeyInput((d_327_branchKeyId_).branchKeyIdentifier))
        d_334_valueOrError6_ = out131_
        if not(not((d_334_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(59,28): " + _dafny.string_of(d_334_valueOrError6_))
        d_333_versionKeyResult_ = (d_334_valueOrError6_).Extract()
        d_335_getBranchKeyVersionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_336_valueOrError7_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out132_: Wrappers.Result
        out132_ = (d_325_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_327_branchKeyId_).branchKeyIdentifier, d_331_oldActiveVersion_))
        d_336_valueOrError7_ = out132_
        if not(not((d_336_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(64,37): " + _dafny.string_of(d_336_valueOrError7_))
        d_335_getBranchKeyVersionResult_ = (d_336_valueOrError7_).Extract()
        d_337_newActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_338_valueOrError8_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out133_: Wrappers.Result
        out133_ = (d_325_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_327_branchKeyId_).branchKeyIdentifier))
        d_338_valueOrError8_ = out133_
        if not(not((d_338_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(72,27): " + _dafny.string_of(d_338_valueOrError8_))
        d_337_newActiveResult_ = (d_338_valueOrError8_).Extract()
        d_339_newActiveVersion_: _dafny.Seq
        d_340_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_340_valueOrError9_ = UTF8.default__.Decode(((d_337_newActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_340_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(77,28): " + _dafny.string_of(d_340_valueOrError9_))
        d_339_newActiveVersion_ = (d_340_valueOrError9_).Extract()
        CleanupItems.default__.DeleteVersion((d_327_branchKeyId_).branchKeyIdentifier, d_339_newActiveVersion_, d_321_ddbClient_)
        CleanupItems.default__.DeleteVersion((d_327_branchKeyId_).branchKeyIdentifier, d_331_oldActiveVersion_, d_321_ddbClient_)
        CleanupItems.default__.DeleteActive((d_327_branchKeyId_).branchKeyIdentifier, d_321_ddbClient_)
        if not((((d_335_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) == (((d_329_oldActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_335_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) == (((d_329_oldActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(88,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_335_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) != (((d_337_newActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(90,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_335_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) != (((d_337_newActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(91,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestVersionKeyWithEC():
        d_341_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_342_valueOrError0_: Wrappers.Result = None
        out134_: Wrappers.Result
        out134_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_342_valueOrError0_ = out134_
        if not(not((d_342_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(96,21): " + _dafny.string_of(d_342_valueOrError0_))
        d_341_kmsClient_ = (d_342_valueOrError0_).Extract()
        d_343_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_344_valueOrError1_: Wrappers.Result = None
        out135_: Wrappers.Result
        out135_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_344_valueOrError1_ = out135_
        if not(not((d_344_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(97,21): " + _dafny.string_of(d_344_valueOrError1_))
        d_343_ddbClient_ = (d_344_valueOrError1_).Extract()
        d_345_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_345_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        if not(ComAmazonawsDynamodbTypes.default__.IsValid__TableName(Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(99,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_346_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_346_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_345_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_343_ddbClient_), Wrappers.Option_Some(d_341_kmsClient_))
        d_347_keyStore_: KeyStore.KeyStoreClient
        d_348_valueOrError2_: Wrappers.Result = None
        out136_: Wrappers.Result
        out136_ = KeyStore.default__.KeyStore(d_346_keyStoreConfig_)
        d_348_valueOrError2_ = out136_
        if not(not((d_348_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(111,20): " + _dafny.string_of(d_348_valueOrError2_))
        d_347_keyStore_ = (d_348_valueOrError2_).Extract()
        d_349_id_: _dafny.Seq
        d_350_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out137_: Wrappers.Result
        out137_ = UUID.default__.GenerateUUID()
        d_350_valueOrError3_ = out137_
        if not(not((d_350_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(116,14): " + _dafny.string_of(d_350_valueOrError3_))
        d_349_id_ = (d_350_valueOrError3_).Extract()
        d_351_customEC_: _dafny.Map
        d_351_customEC_ = _dafny.Map({_dafny.Seq("some"): _dafny.Seq("encryption"), _dafny.Seq("context"): _dafny.Seq("values")})
        d_352_encryptionContext_: _dafny.Map
        d_353_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out138_: Wrappers.Result
        out138_ = Fixtures.default__.EncodeEncryptionContext(d_351_customEC_)
        d_353_valueOrError4_ = out138_
        if not(not((d_353_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(122,29): " + _dafny.string_of(d_353_valueOrError4_))
        d_352_encryptionContext_ = (d_353_valueOrError4_).Extract()
        d_354_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_355_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out139_: Wrappers.Result
        out139_ = (d_347_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_Some(d_349_id_), Wrappers.Option_Some(d_352_encryptionContext_)))
        d_355_valueOrError5_ = out139_
        if not(not((d_355_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(124,23): " + _dafny.string_of(d_355_valueOrError5_))
        d_354_branchKeyId_ = (d_355_valueOrError5_).Extract()
        if not(((d_354_branchKeyId_).branchKeyIdentifier) == (d_349_id_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(129,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_356_oldActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_357_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out140_: Wrappers.Result
        out140_ = (d_347_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_354_branchKeyId_).branchKeyIdentifier))
        d_357_valueOrError6_ = out140_
        if not(not((d_357_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(131,27): " + _dafny.string_of(d_357_valueOrError6_))
        d_356_oldActiveResult_ = (d_357_valueOrError6_).Extract()
        d_358_mat_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_358_mat_ = (d_356_oldActiveResult_).branchKeyMaterials
        if not(((d_358_mat_).branchKeyIdentifier) == (d_349_id_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(136,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_359_matEC_: _dafny.Map
        d_360_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out141_: Wrappers.Result
        out141_ = Fixtures.default__.DecodeEncryptionContext((d_358_mat_).encryptionContext)
        d_360_valueOrError7_ = out141_
        if not(not((d_360_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(137,17): " + _dafny.string_of(d_360_valueOrError7_))
        d_359_matEC_ = (d_360_valueOrError7_).Extract()
        if not((d_359_matEC_) == (d_351_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(138,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_361_oldActiveVersion_: _dafny.Seq
        d_362_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_362_valueOrError8_ = UTF8.default__.Decode(((d_356_oldActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_362_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(140,28): " + _dafny.string_of(d_362_valueOrError8_))
        d_361_oldActiveVersion_ = (d_362_valueOrError8_).Extract()
        d_363_versionKeyResult_: AwsCryptographyKeyStoreTypes.VersionKeyOutput
        d_364_valueOrError9_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        out142_: Wrappers.Result
        out142_ = (d_347_keyStore_).VersionKey(AwsCryptographyKeyStoreTypes.VersionKeyInput_VersionKeyInput((d_354_branchKeyId_).branchKeyIdentifier))
        d_364_valueOrError9_ = out142_
        if not(not((d_364_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(142,28): " + _dafny.string_of(d_364_valueOrError9_))
        d_363_versionKeyResult_ = (d_364_valueOrError9_).Extract()
        d_365_getBranchKeyVersionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_366_valueOrError10_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out143_: Wrappers.Result
        out143_ = (d_347_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_354_branchKeyId_).branchKeyIdentifier, d_361_oldActiveVersion_))
        d_366_valueOrError10_ = out143_
        if not(not((d_366_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(147,37): " + _dafny.string_of(d_366_valueOrError10_))
        d_365_getBranchKeyVersionResult_ = (d_366_valueOrError10_).Extract()
        d_367_mat2_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_367_mat2_ = (d_365_getBranchKeyVersionResult_).branchKeyMaterials
        if not(((d_358_mat_).branchKeyIdentifier) == (d_349_id_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(155,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_368_mat2EC_: _dafny.Map
        d_369_valueOrError11_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out144_: Wrappers.Result
        out144_ = Fixtures.default__.DecodeEncryptionContext((d_358_mat_).encryptionContext)
        d_369_valueOrError11_ = out144_
        if not(not((d_369_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(156,18): " + _dafny.string_of(d_369_valueOrError11_))
        d_368_mat2EC_ = (d_369_valueOrError11_).Extract()
        if not((d_368_mat2EC_) == (d_351_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(157,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_367_mat2_).branchKeyVersion) == ((d_358_mat_).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(158,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_370_newActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_371_valueOrError12_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out145_: Wrappers.Result
        out145_ = (d_347_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_354_branchKeyId_).branchKeyIdentifier))
        d_371_valueOrError12_ = out145_
        if not(not((d_371_valueOrError12_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(160,27): " + _dafny.string_of(d_371_valueOrError12_))
        d_370_newActiveResult_ = (d_371_valueOrError12_).Extract()
        d_372_mat3_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_372_mat3_ = (d_370_newActiveResult_).branchKeyMaterials
        if not(((d_358_mat_).branchKeyIdentifier) == (d_349_id_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(165,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_373_mat3EC_: _dafny.Map
        d_374_valueOrError13_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out146_: Wrappers.Result
        out146_ = Fixtures.default__.DecodeEncryptionContext((d_358_mat_).encryptionContext)
        d_374_valueOrError13_ = out146_
        if not(not((d_374_valueOrError13_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(166,18): " + _dafny.string_of(d_374_valueOrError13_))
        d_373_mat3EC_ = (d_374_valueOrError13_).Extract()
        if not((d_373_mat3EC_) == (d_351_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(167,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_372_mat3_).branchKeyVersion) != ((d_358_mat_).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(168,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_375_newActiveVersion_: _dafny.Seq
        d_376_valueOrError14_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_376_valueOrError14_ = UTF8.default__.Decode(((d_370_newActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_376_valueOrError14_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(170,28): " + _dafny.string_of(d_376_valueOrError14_))
        d_375_newActiveVersion_ = (d_376_valueOrError14_).Extract()
        if not((d_375_newActiveVersion_) != (d_361_oldActiveVersion_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(172,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        CleanupItems.default__.DeleteVersion((d_354_branchKeyId_).branchKeyIdentifier, d_375_newActiveVersion_, d_343_ddbClient_)
        CleanupItems.default__.DeleteVersion((d_354_branchKeyId_).branchKeyIdentifier, d_361_oldActiveVersion_, d_343_ddbClient_)
        CleanupItems.default__.DeleteActive((d_354_branchKeyId_).branchKeyIdentifier, d_343_ddbClient_)
        if not((((d_365_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) == (((d_356_oldActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(182,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_365_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) == (((d_356_oldActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(183,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_365_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) != (((d_370_newActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(185,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_365_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) != (((d_370_newActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(186,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_359_matEC_) == (d_351_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(193,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_368_mat2EC_) == (d_351_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(194,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_373_mat3EC_) == (d_351_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(195,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestMrkVersionKey():
        d_377_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_378_valueOrError0_: Wrappers.Result = None
        out147_: Wrappers.Result
        out147_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_378_valueOrError0_ = out147_
        if not(not((d_378_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(200,21): " + _dafny.string_of(d_378_valueOrError0_))
        d_377_ddbClient_ = (d_378_valueOrError0_).Extract()
        d_379_eastKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_379_eastKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsMrkConfigEast, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_377_ddbClient_), Wrappers.Option_None())
        d_380_westKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        def iife12_(_pat_let4_0):
            def iife13_(d_381_dt__update__tmp_h0_):
                def iife14_(_pat_let5_0):
                    def iife15_(d_382_dt__update_hkmsConfiguration_h0_):
                        return AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig((d_381_dt__update__tmp_h0_).ddbTableName, d_382_dt__update_hkmsConfiguration_h0_, (d_381_dt__update__tmp_h0_).logicalKeyStoreName, (d_381_dt__update__tmp_h0_).id, (d_381_dt__update__tmp_h0_).grantTokens, (d_381_dt__update__tmp_h0_).ddbClient, (d_381_dt__update__tmp_h0_).kmsClient)
                    return iife15_(_pat_let5_0)
                return iife14_(Fixtures.default__.KmsMrkConfigWest)
            return iife13_(_pat_let4_0)
        d_380_westKeyStoreConfig_ = iife12_(d_379_eastKeyStoreConfig_)
        d_383_eastSrkKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        def iife16_(_pat_let6_0):
            def iife17_(d_384_dt__update__tmp_h1_):
                def iife18_(_pat_let7_0):
                    def iife19_(d_385_dt__update_hkmsConfiguration_h1_):
                        return AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig((d_384_dt__update__tmp_h1_).ddbTableName, d_385_dt__update_hkmsConfiguration_h1_, (d_384_dt__update__tmp_h1_).logicalKeyStoreName, (d_384_dt__update__tmp_h1_).id, (d_384_dt__update__tmp_h1_).grantTokens, (d_384_dt__update__tmp_h1_).ddbClient, (d_384_dt__update__tmp_h1_).kmsClient)
                    return iife19_(_pat_let7_0)
                return iife18_(Fixtures.default__.KmsSrkConfigEast)
            return iife17_(_pat_let6_0)
        d_383_eastSrkKeyStoreConfig_ = iife16_(d_379_eastKeyStoreConfig_)
        d_386_westSrkKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        def iife20_(_pat_let8_0):
            def iife21_(d_387_dt__update__tmp_h2_):
                def iife22_(_pat_let9_0):
                    def iife23_(d_388_dt__update_hkmsConfiguration_h2_):
                        return AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig((d_387_dt__update__tmp_h2_).ddbTableName, d_388_dt__update_hkmsConfiguration_h2_, (d_387_dt__update__tmp_h2_).logicalKeyStoreName, (d_387_dt__update__tmp_h2_).id, (d_387_dt__update__tmp_h2_).grantTokens, (d_387_dt__update__tmp_h2_).ddbClient, (d_387_dt__update__tmp_h2_).kmsClient)
                    return iife23_(_pat_let9_0)
                return iife22_(Fixtures.default__.KmsSrkConfigWest)
            return iife21_(_pat_let8_0)
        d_386_westSrkKeyStoreConfig_ = iife20_(d_379_eastKeyStoreConfig_)
        d_389_eastKeyStore_: KeyStore.KeyStoreClient
        d_390_valueOrError1_: Wrappers.Result = None
        out148_: Wrappers.Result
        out148_ = KeyStore.default__.KeyStore(d_379_eastKeyStoreConfig_)
        d_390_valueOrError1_ = out148_
        if not(not((d_390_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(215,24): " + _dafny.string_of(d_390_valueOrError1_))
        d_389_eastKeyStore_ = (d_390_valueOrError1_).Extract()
        d_391_westKeyStore_: KeyStore.KeyStoreClient
        d_392_valueOrError2_: Wrappers.Result = None
        out149_: Wrappers.Result
        out149_ = KeyStore.default__.KeyStore(d_380_westKeyStoreConfig_)
        d_392_valueOrError2_ = out149_
        if not(not((d_392_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(216,24): " + _dafny.string_of(d_392_valueOrError2_))
        d_391_westKeyStore_ = (d_392_valueOrError2_).Extract()
        d_393_eastSrkKeyStore_: KeyStore.KeyStoreClient
        d_394_valueOrError3_: Wrappers.Result = None
        out150_: Wrappers.Result
        out150_ = KeyStore.default__.KeyStore(d_383_eastSrkKeyStoreConfig_)
        d_394_valueOrError3_ = out150_
        if not(not((d_394_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(217,27): " + _dafny.string_of(d_394_valueOrError3_))
        d_393_eastSrkKeyStore_ = (d_394_valueOrError3_).Extract()
        d_395_westSrkKeyStore_: KeyStore.KeyStoreClient
        d_396_valueOrError4_: Wrappers.Result = None
        out151_: Wrappers.Result
        out151_ = KeyStore.default__.KeyStore(d_386_westSrkKeyStoreConfig_)
        d_396_valueOrError4_ = out151_
        if not(not((d_396_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(218,27): " + _dafny.string_of(d_396_valueOrError4_))
        d_395_westSrkKeyStore_ = (d_396_valueOrError4_).Extract()
        d_397_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_398_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out152_: Wrappers.Result
        out152_ = (d_391_westKeyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_None(), Wrappers.Option_None()))
        d_398_valueOrError5_ = out152_
        if not(not((d_398_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(223,23): " + _dafny.string_of(d_398_valueOrError5_))
        d_397_branchKeyId_ = (d_398_valueOrError5_).Extract()
        d_399_oldActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_400_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out153_: Wrappers.Result
        out153_ = (d_391_westKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_397_branchKeyId_).branchKeyIdentifier))
        d_400_valueOrError6_ = out153_
        if not(not((d_400_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(228,27): " + _dafny.string_of(d_400_valueOrError6_))
        d_399_oldActiveResult_ = (d_400_valueOrError6_).Extract()
        d_401_oldActiveVersion_: _dafny.Seq
        d_402_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_402_valueOrError7_ = UTF8.default__.Decode(((d_399_oldActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_402_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(233,28): " + _dafny.string_of(d_402_valueOrError7_))
        d_401_oldActiveVersion_ = (d_402_valueOrError7_).Extract()
        d_403_versionKeyResult_: AwsCryptographyKeyStoreTypes.VersionKeyOutput
        d_404_valueOrError8_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        out154_: Wrappers.Result
        out154_ = (d_389_eastKeyStore_).VersionKey(AwsCryptographyKeyStoreTypes.VersionKeyInput_VersionKeyInput((d_397_branchKeyId_).branchKeyIdentifier))
        d_404_valueOrError8_ = out154_
        if not(not((d_404_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(236,28): " + _dafny.string_of(d_404_valueOrError8_))
        d_403_versionKeyResult_ = (d_404_valueOrError8_).Extract()
        d_405_getBranchKeyVersionResultWest_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_406_valueOrError9_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out155_: Wrappers.Result
        out155_ = (d_391_westKeyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_397_branchKeyId_).branchKeyIdentifier, d_401_oldActiveVersion_))
        d_406_valueOrError9_ = out155_
        if not(not((d_406_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(241,41): " + _dafny.string_of(d_406_valueOrError9_))
        d_405_getBranchKeyVersionResultWest_ = (d_406_valueOrError9_).Extract()
        d_407_getBranchKeyVersionResultEast_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_408_valueOrError10_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out156_: Wrappers.Result
        out156_ = (d_389_eastKeyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_397_branchKeyId_).branchKeyIdentifier, d_401_oldActiveVersion_))
        d_408_valueOrError10_ = out156_
        if not(not((d_408_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(249,41): " + _dafny.string_of(d_408_valueOrError10_))
        d_407_getBranchKeyVersionResultEast_ = (d_408_valueOrError10_).Extract()
        if not((d_405_getBranchKeyVersionResultWest_) == (d_407_getBranchKeyVersionResultEast_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(257,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_409_newActiveResultWest_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_410_valueOrError11_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out157_: Wrappers.Result
        out157_ = (d_391_westKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_397_branchKeyId_).branchKeyIdentifier))
        d_410_valueOrError11_ = out157_
        if not(not((d_410_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(259,31): " + _dafny.string_of(d_410_valueOrError11_))
        d_409_newActiveResultWest_ = (d_410_valueOrError11_).Extract()
        d_411_newActiveResultEast_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_412_valueOrError12_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out158_: Wrappers.Result
        out158_ = (d_389_eastKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_397_branchKeyId_).branchKeyIdentifier))
        d_412_valueOrError12_ = out158_
        if not(not((d_412_valueOrError12_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(263,31): " + _dafny.string_of(d_412_valueOrError12_))
        d_411_newActiveResultEast_ = (d_412_valueOrError12_).Extract()
        if not((d_409_newActiveResultWest_) == (d_411_newActiveResultEast_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(268,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_413_newActiveResultSrkWest_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_414_valueOrError13_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out159_: Wrappers.Result
        out159_ = (d_395_westSrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_397_branchKeyId_).branchKeyIdentifier))
        d_414_valueOrError13_ = out159_
        if not(not((d_414_valueOrError13_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(274,34): " + _dafny.string_of(d_414_valueOrError13_))
        d_413_newActiveResultSrkWest_ = (d_414_valueOrError13_).Extract()
        if not((d_413_newActiveResultSrkWest_) == (d_411_newActiveResultEast_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(279,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_415_newActiveResultSrkEastResult_: Wrappers.Result
        out160_: Wrappers.Result
        out160_ = (d_393_eastSrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_397_branchKeyId_).branchKeyIdentifier))
        d_415_newActiveResultSrkEastResult_ = out160_
        if not((d_415_newActiveResultSrkEastResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(285,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_415_newActiveResultSrkEastResult_).error) == (AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.GET__KEY__ARN__DISAGREEMENT))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(286,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_416_newActiveVersionWest_: _dafny.Seq
        d_417_valueOrError14_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_417_valueOrError14_ = UTF8.default__.Decode(((d_409_newActiveResultWest_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_417_valueOrError14_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(289,32): " + _dafny.string_of(d_417_valueOrError14_))
        d_416_newActiveVersionWest_ = (d_417_valueOrError14_).Extract()
        d_418_newActiveVersionEast_: _dafny.Seq
        d_419_valueOrError15_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_419_valueOrError15_ = UTF8.default__.Decode(((d_411_newActiveResultEast_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_419_valueOrError15_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(290,32): " + _dafny.string_of(d_419_valueOrError15_))
        d_418_newActiveVersionEast_ = (d_419_valueOrError15_).Extract()
        if not((d_416_newActiveVersionWest_) == (d_418_newActiveVersionEast_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(291,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        CleanupItems.default__.DeleteVersion((d_397_branchKeyId_).branchKeyIdentifier, d_418_newActiveVersionEast_, d_377_ddbClient_)
        CleanupItems.default__.DeleteVersion((d_397_branchKeyId_).branchKeyIdentifier, d_401_oldActiveVersion_, d_377_ddbClient_)
        CleanupItems.default__.DeleteActive((d_397_branchKeyId_).branchKeyIdentifier, d_377_ddbClient_)
        if not((((d_407_getBranchKeyVersionResultEast_).branchKeyMaterials).branchKeyVersion) == (((d_399_oldActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(301,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_407_getBranchKeyVersionResultEast_).branchKeyMaterials).branchKey) == (((d_399_oldActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(302,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_407_getBranchKeyVersionResultEast_).branchKeyMaterials).branchKeyVersion) != (((d_411_newActiveResultEast_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(304,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_407_getBranchKeyVersionResultEast_).branchKeyMaterials).branchKey) != (((d_411_newActiveResultEast_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(305,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def InsertingADuplicateVersionWillFail():
        d_420_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_421_valueOrError0_: Wrappers.Result = None
        out161_: Wrappers.Result
        out161_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_421_valueOrError0_ = out161_
        if not(not((d_421_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(316,21): " + _dafny.string_of(d_421_valueOrError0_))
        d_420_ddbClient_ = (d_421_valueOrError0_).Extract()
        if not((0) < (len(Fixtures.default__.branchKeyId))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(318,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((0) < (len(Fixtures.default__.branchKeyIdActiveVersion))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(319,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_422_customEncryptionContext_: _dafny.Map
        d_422_customEncryptionContext_ = _dafny.Map({})
        def lambda2_(forall_var_2_):
            d_423_k_: _dafny.Seq = forall_var_2_
            return not ((d_423_k_) in (d_422_customEncryptionContext_)) or (ComAmazonawsDynamodbTypes.default__.IsValid__AttributeName((Structure.default__.ENCRYPTION__CONTEXT__PREFIX) + (d_423_k_)))

        if not(_dafny.quantifier((d_422_customEncryptionContext_).keys.Elements, True, lambda2_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(321,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_424_encryptionContext_: _dafny.Map
        d_424_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        if not(ComAmazonawsDynamodbTypes.default__.IsValid__TableName(Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(332,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_425_myBranchKeyStoreName_: _dafny.Seq
        d_425_myBranchKeyStoreName_ = Fixtures.default__.branchKeyStoreName
        d_426_versionBranchKeyItem_: _dafny.Map
        d_426_versionBranchKeyItem_ = Structure.default__.ToAttributeMap(d_424_encryptionContext_, _dafny.Seq([1]))
        d_427_activeBranchKeyItem_: _dafny.Map
        d_427_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_424_encryptionContext_), _dafny.Seq([2]))
        if not(((d_427_activeBranchKeyItem_)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]) == ((d_426_versionBranchKeyItem_)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD])):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(336,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_427_activeBranchKeyItem_)[Structure.default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]) == ((d_426_versionBranchKeyItem_)[Structure.default__.TYPE__FIELD])):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(337,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_428_output_: Wrappers.Result
        out162_: Wrappers.Result
        out162_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(d_426_versionBranchKeyItem_, d_427_activeBranchKeyItem_, d_425_myBranchKeyStoreName_, d_420_ddbClient_)
        d_428_output_ = out162_
        if not((d_428_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(346,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def VersioningANonexistentBranchKeyWillFail():
        d_429_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_430_valueOrError0_: Wrappers.Result = None
        out163_: Wrappers.Result
        out163_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_430_valueOrError0_ = out163_
        if not(not((d_430_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(352,21): " + _dafny.string_of(d_430_valueOrError0_))
        d_429_ddbClient_ = (d_430_valueOrError0_).Extract()
        d_431_encryptionContext_: _dafny.Map
        d_431_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(_dafny.Seq("!= branchKeyId"), Fixtures.default__.branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        d_432_versionBranchKeyItem_: _dafny.Map
        d_432_versionBranchKeyItem_ = Structure.default__.ToAttributeMap(d_431_encryptionContext_, _dafny.Seq([1]))
        d_433_activeBranchKeyItem_: _dafny.Map
        d_433_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_431_encryptionContext_), _dafny.Seq([2]))
        if not(((d_433_activeBranchKeyItem_)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]) == ((d_432_versionBranchKeyItem_)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD])):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(365,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_433_activeBranchKeyItem_)[Structure.default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]) == ((d_432_versionBranchKeyItem_)[Structure.default__.TYPE__FIELD])):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(366,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(ComAmazonawsDynamodbTypes.default__.IsValid__TableName(Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(367,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_434_myBranchKeyStoreName_: _dafny.Seq
        d_434_myBranchKeyStoreName_ = Fixtures.default__.branchKeyStoreName
        d_435_output_: Wrappers.Result
        out164_: Wrappers.Result
        out164_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(d_432_versionBranchKeyItem_, d_433_activeBranchKeyItem_, d_434_myBranchKeyStoreName_, d_429_ddbClient_)
        d_435_output_ = out164_
        if not((d_435_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(377,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

