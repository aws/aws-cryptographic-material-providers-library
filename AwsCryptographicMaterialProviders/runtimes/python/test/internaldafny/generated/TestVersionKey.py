import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_material_providers.internaldafny.generated.GetKeys as GetKeys
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
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
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_material_providers.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_material_providers.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_material_providers.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_material_providers.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_material_providers.internaldafny.generated.CMM as CMM
import aws_cryptographic_material_providers.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_material_providers.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_material_providers.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_material_providers.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_material_providers.internaldafny.generated.Utils as Utils
import aws_cryptographic_material_providers.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_material_providers.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
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
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(27,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(28,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_3_ddbClient_ = (d_2_valueOrError1_).Extract()
        d_4_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_4_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        if not(ComAmazonawsDynamodbTypes.default__.IsValid__TableName(Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(30,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_5_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_5_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_4_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_3_ddbClient_), Wrappers.Option_Some(d_1_kmsClient_))
        d_6_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_5_keyStoreConfig_)
        d_6_valueOrError2_ = out2_
        if not(not((d_6_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(42,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_None(), Wrappers.Option_None()))
        d_8_valueOrError3_ = out3_
        if not(not((d_8_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(47,23): " + _dafny.string_of(d_8_valueOrError3_))
        d_9_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_9_branchKeyId_ = (d_8_valueOrError3_).Extract()
        d_10_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out4_: Wrappers.Result
        out4_ = (d_7_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_9_branchKeyId_).branchKeyIdentifier))
        d_10_valueOrError4_ = out4_
        if not(not((d_10_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(52,27): " + _dafny.string_of(d_10_valueOrError4_))
        d_11_oldActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_11_oldActiveResult_ = (d_10_valueOrError4_).Extract()
        d_12_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_12_valueOrError5_ = UTF8.default__.Decode(((d_11_oldActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_12_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(57,28): " + _dafny.string_of(d_12_valueOrError5_))
        d_13_oldActiveVersion_: _dafny.Seq
        d_13_oldActiveVersion_ = (d_12_valueOrError5_).Extract()
        d_14_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        out5_: Wrappers.Result
        out5_ = (d_7_keyStore_).VersionKey(AwsCryptographyKeyStoreTypes.VersionKeyInput_VersionKeyInput((d_9_branchKeyId_).branchKeyIdentifier))
        d_14_valueOrError6_ = out5_
        if not(not((d_14_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(59,28): " + _dafny.string_of(d_14_valueOrError6_))
        d_15_versionKeyResult_: AwsCryptographyKeyStoreTypes.VersionKeyOutput
        d_15_versionKeyResult_ = (d_14_valueOrError6_).Extract()
        d_16_valueOrError7_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out6_: Wrappers.Result
        out6_ = (d_7_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_9_branchKeyId_).branchKeyIdentifier, d_13_oldActiveVersion_))
        d_16_valueOrError7_ = out6_
        if not(not((d_16_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(64,37): " + _dafny.string_of(d_16_valueOrError7_))
        d_17_getBranchKeyVersionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_17_getBranchKeyVersionResult_ = (d_16_valueOrError7_).Extract()
        d_18_valueOrError8_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out7_: Wrappers.Result
        out7_ = (d_7_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_9_branchKeyId_).branchKeyIdentifier))
        d_18_valueOrError8_ = out7_
        if not(not((d_18_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(72,27): " + _dafny.string_of(d_18_valueOrError8_))
        d_19_newActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_19_newActiveResult_ = (d_18_valueOrError8_).Extract()
        d_20_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_20_valueOrError9_ = UTF8.default__.Decode(((d_19_newActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_20_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(77,28): " + _dafny.string_of(d_20_valueOrError9_))
        d_21_newActiveVersion_: _dafny.Seq
        d_21_newActiveVersion_ = (d_20_valueOrError9_).Extract()
        CleanupItems.default__.DeleteVersion((d_9_branchKeyId_).branchKeyIdentifier, d_21_newActiveVersion_, d_3_ddbClient_)
        CleanupItems.default__.DeleteVersion((d_9_branchKeyId_).branchKeyIdentifier, d_13_oldActiveVersion_, d_3_ddbClient_)
        CleanupItems.default__.DeleteActive((d_9_branchKeyId_).branchKeyIdentifier, d_3_ddbClient_)
        if not((((d_17_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) == (((d_11_oldActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_17_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) == (((d_11_oldActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(88,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_17_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) != (((d_19_newActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(90,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_17_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) != (((d_19_newActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(91,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestVersionKeyWithEC():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(96,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(97,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_3_ddbClient_ = (d_2_valueOrError1_).Extract()
        d_4_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_4_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        if not(ComAmazonawsDynamodbTypes.default__.IsValid__TableName(Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(99,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_5_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_5_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_4_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_3_ddbClient_), Wrappers.Option_Some(d_1_kmsClient_))
        d_6_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_5_keyStoreConfig_)
        d_6_valueOrError2_ = out2_
        if not(not((d_6_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(111,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out3_: Wrappers.Result
        out3_ = UUID.default__.GenerateUUID()
        d_8_valueOrError3_ = out3_
        if not(not((d_8_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(116,14): " + _dafny.string_of(d_8_valueOrError3_))
        d_9_id_: _dafny.Seq
        d_9_id_ = (d_8_valueOrError3_).Extract()
        d_10_customEC_: _dafny.Map
        d_10_customEC_ = _dafny.Map({_dafny.Seq("some"): _dafny.Seq("encryption"), _dafny.Seq("context"): _dafny.Seq("values")})
        d_11_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out4_: Wrappers.Result
        out4_ = Fixtures.default__.EncodeEncryptionContext(d_10_customEC_)
        d_11_valueOrError4_ = out4_
        if not(not((d_11_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(122,29): " + _dafny.string_of(d_11_valueOrError4_))
        d_12_encryptionContext_: _dafny.Map
        d_12_encryptionContext_ = (d_11_valueOrError4_).Extract()
        d_13_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out5_: Wrappers.Result
        out5_ = (d_7_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_Some(d_9_id_), Wrappers.Option_Some(d_12_encryptionContext_)))
        d_13_valueOrError5_ = out5_
        if not(not((d_13_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(124,23): " + _dafny.string_of(d_13_valueOrError5_))
        d_14_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_14_branchKeyId_ = (d_13_valueOrError5_).Extract()
        if not(((d_14_branchKeyId_).branchKeyIdentifier) == (d_9_id_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(129,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_15_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out6_: Wrappers.Result
        out6_ = (d_7_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_14_branchKeyId_).branchKeyIdentifier))
        d_15_valueOrError6_ = out6_
        if not(not((d_15_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(131,27): " + _dafny.string_of(d_15_valueOrError6_))
        d_16_oldActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_16_oldActiveResult_ = (d_15_valueOrError6_).Extract()
        d_17_mat_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_17_mat_ = (d_16_oldActiveResult_).branchKeyMaterials
        if not(((d_17_mat_).branchKeyIdentifier) == (d_9_id_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(136,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_18_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out7_: Wrappers.Result
        out7_ = Fixtures.default__.DecodeEncryptionContext((d_17_mat_).encryptionContext)
        d_18_valueOrError7_ = out7_
        if not(not((d_18_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(137,17): " + _dafny.string_of(d_18_valueOrError7_))
        d_19_matEC_: _dafny.Map
        d_19_matEC_ = (d_18_valueOrError7_).Extract()
        if not((d_19_matEC_) == (d_10_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(138,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_20_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_20_valueOrError8_ = UTF8.default__.Decode(((d_16_oldActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_20_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(140,28): " + _dafny.string_of(d_20_valueOrError8_))
        d_21_oldActiveVersion_: _dafny.Seq
        d_21_oldActiveVersion_ = (d_20_valueOrError8_).Extract()
        d_22_valueOrError9_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        out8_: Wrappers.Result
        out8_ = (d_7_keyStore_).VersionKey(AwsCryptographyKeyStoreTypes.VersionKeyInput_VersionKeyInput((d_14_branchKeyId_).branchKeyIdentifier))
        d_22_valueOrError9_ = out8_
        if not(not((d_22_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(142,28): " + _dafny.string_of(d_22_valueOrError9_))
        d_23_versionKeyResult_: AwsCryptographyKeyStoreTypes.VersionKeyOutput
        d_23_versionKeyResult_ = (d_22_valueOrError9_).Extract()
        d_24_valueOrError10_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out9_: Wrappers.Result
        out9_ = (d_7_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_14_branchKeyId_).branchKeyIdentifier, d_21_oldActiveVersion_))
        d_24_valueOrError10_ = out9_
        if not(not((d_24_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(147,37): " + _dafny.string_of(d_24_valueOrError10_))
        d_25_getBranchKeyVersionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_25_getBranchKeyVersionResult_ = (d_24_valueOrError10_).Extract()
        d_26_mat2_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_26_mat2_ = (d_25_getBranchKeyVersionResult_).branchKeyMaterials
        if not(((d_17_mat_).branchKeyIdentifier) == (d_9_id_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(155,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_27_valueOrError11_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out10_: Wrappers.Result
        out10_ = Fixtures.default__.DecodeEncryptionContext((d_17_mat_).encryptionContext)
        d_27_valueOrError11_ = out10_
        if not(not((d_27_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(156,18): " + _dafny.string_of(d_27_valueOrError11_))
        d_28_mat2EC_: _dafny.Map
        d_28_mat2EC_ = (d_27_valueOrError11_).Extract()
        if not((d_28_mat2EC_) == (d_10_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(157,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_26_mat2_).branchKeyVersion) == ((d_17_mat_).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(158,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_29_valueOrError12_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out11_: Wrappers.Result
        out11_ = (d_7_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_14_branchKeyId_).branchKeyIdentifier))
        d_29_valueOrError12_ = out11_
        if not(not((d_29_valueOrError12_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(160,27): " + _dafny.string_of(d_29_valueOrError12_))
        d_30_newActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_30_newActiveResult_ = (d_29_valueOrError12_).Extract()
        d_31_mat3_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_31_mat3_ = (d_30_newActiveResult_).branchKeyMaterials
        if not(((d_17_mat_).branchKeyIdentifier) == (d_9_id_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(165,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_32_valueOrError13_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out12_: Wrappers.Result
        out12_ = Fixtures.default__.DecodeEncryptionContext((d_17_mat_).encryptionContext)
        d_32_valueOrError13_ = out12_
        if not(not((d_32_valueOrError13_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(166,18): " + _dafny.string_of(d_32_valueOrError13_))
        d_33_mat3EC_: _dafny.Map
        d_33_mat3EC_ = (d_32_valueOrError13_).Extract()
        if not((d_33_mat3EC_) == (d_10_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(167,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_31_mat3_).branchKeyVersion) != ((d_17_mat_).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(168,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_34_valueOrError14_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_34_valueOrError14_ = UTF8.default__.Decode(((d_30_newActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_34_valueOrError14_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(170,28): " + _dafny.string_of(d_34_valueOrError14_))
        d_35_newActiveVersion_: _dafny.Seq
        d_35_newActiveVersion_ = (d_34_valueOrError14_).Extract()
        if not((d_35_newActiveVersion_) != (d_21_oldActiveVersion_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(172,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        CleanupItems.default__.DeleteVersion((d_14_branchKeyId_).branchKeyIdentifier, d_35_newActiveVersion_, d_3_ddbClient_)
        CleanupItems.default__.DeleteVersion((d_14_branchKeyId_).branchKeyIdentifier, d_21_oldActiveVersion_, d_3_ddbClient_)
        CleanupItems.default__.DeleteActive((d_14_branchKeyId_).branchKeyIdentifier, d_3_ddbClient_)
        if not((((d_25_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) == (((d_16_oldActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(182,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_25_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) == (((d_16_oldActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(183,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_25_getBranchKeyVersionResult_).branchKeyMaterials).branchKeyVersion) != (((d_30_newActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(185,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_25_getBranchKeyVersionResult_).branchKeyMaterials).branchKey) != (((d_30_newActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(186,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_19_matEC_) == (d_10_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(193,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_28_mat2EC_) == (d_10_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(194,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_33_mat3EC_) == (d_10_customEC_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(195,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestMrkVersionKey():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(200,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_1_ddbClient_ = (d_0_valueOrError0_).Extract()
        d_2_eastKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_2_eastKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsMrkConfigEast, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_1_ddbClient_), Wrappers.Option_None())
        d_3_westKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_4_dt__update__tmp_h0_ = d_2_eastKeyStoreConfig_
        d_5_dt__update_hkmsConfiguration_h0_ = Fixtures.default__.KmsMrkConfigWest
        d_3_westKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig((d_4_dt__update__tmp_h0_).ddbTableName, d_5_dt__update_hkmsConfiguration_h0_, (d_4_dt__update__tmp_h0_).logicalKeyStoreName, (d_4_dt__update__tmp_h0_).id, (d_4_dt__update__tmp_h0_).grantTokens, (d_4_dt__update__tmp_h0_).ddbClient, (d_4_dt__update__tmp_h0_).kmsClient)
        d_6_eastSrkKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_7_dt__update__tmp_h1_ = d_2_eastKeyStoreConfig_
        d_8_dt__update_hkmsConfiguration_h1_ = Fixtures.default__.KmsSrkConfigEast
        d_6_eastSrkKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig((d_7_dt__update__tmp_h1_).ddbTableName, d_8_dt__update_hkmsConfiguration_h1_, (d_7_dt__update__tmp_h1_).logicalKeyStoreName, (d_7_dt__update__tmp_h1_).id, (d_7_dt__update__tmp_h1_).grantTokens, (d_7_dt__update__tmp_h1_).ddbClient, (d_7_dt__update__tmp_h1_).kmsClient)
        d_9_westSrkKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_10_dt__update__tmp_h2_ = d_2_eastKeyStoreConfig_
        d_11_dt__update_hkmsConfiguration_h2_ = Fixtures.default__.KmsSrkConfigWest
        d_9_westSrkKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig((d_10_dt__update__tmp_h2_).ddbTableName, d_11_dt__update_hkmsConfiguration_h2_, (d_10_dt__update__tmp_h2_).logicalKeyStoreName, (d_10_dt__update__tmp_h2_).id, (d_10_dt__update__tmp_h2_).grantTokens, (d_10_dt__update__tmp_h2_).ddbClient, (d_10_dt__update__tmp_h2_).kmsClient)
        d_12_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = KeyStore.default__.KeyStore(d_2_eastKeyStoreConfig_)
        d_12_valueOrError1_ = out1_
        if not(not((d_12_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(215,24): " + _dafny.string_of(d_12_valueOrError1_))
        d_13_eastKeyStore_: KeyStore.KeyStoreClient
        d_13_eastKeyStore_ = (d_12_valueOrError1_).Extract()
        d_14_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_3_westKeyStoreConfig_)
        d_14_valueOrError2_ = out2_
        if not(not((d_14_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(216,24): " + _dafny.string_of(d_14_valueOrError2_))
        d_15_westKeyStore_: KeyStore.KeyStoreClient
        d_15_westKeyStore_ = (d_14_valueOrError2_).Extract()
        d_16_valueOrError3_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = KeyStore.default__.KeyStore(d_6_eastSrkKeyStoreConfig_)
        d_16_valueOrError3_ = out3_
        if not(not((d_16_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(217,27): " + _dafny.string_of(d_16_valueOrError3_))
        d_17_eastSrkKeyStore_: KeyStore.KeyStoreClient
        d_17_eastSrkKeyStore_ = (d_16_valueOrError3_).Extract()
        d_18_valueOrError4_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = KeyStore.default__.KeyStore(d_9_westSrkKeyStoreConfig_)
        d_18_valueOrError4_ = out4_
        if not(not((d_18_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(218,27): " + _dafny.string_of(d_18_valueOrError4_))
        d_19_westSrkKeyStore_: KeyStore.KeyStoreClient
        d_19_westSrkKeyStore_ = (d_18_valueOrError4_).Extract()
        d_20_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out5_: Wrappers.Result
        out5_ = (d_15_westKeyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_None(), Wrappers.Option_None()))
        d_20_valueOrError5_ = out5_
        if not(not((d_20_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(223,23): " + _dafny.string_of(d_20_valueOrError5_))
        d_21_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_21_branchKeyId_ = (d_20_valueOrError5_).Extract()
        d_22_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out6_: Wrappers.Result
        out6_ = (d_15_westKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_21_branchKeyId_).branchKeyIdentifier))
        d_22_valueOrError6_ = out6_
        if not(not((d_22_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(228,27): " + _dafny.string_of(d_22_valueOrError6_))
        d_23_oldActiveResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_23_oldActiveResult_ = (d_22_valueOrError6_).Extract()
        d_24_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_24_valueOrError7_ = UTF8.default__.Decode(((d_23_oldActiveResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_24_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(233,28): " + _dafny.string_of(d_24_valueOrError7_))
        d_25_oldActiveVersion_: _dafny.Seq
        d_25_oldActiveVersion_ = (d_24_valueOrError7_).Extract()
        d_26_valueOrError8_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.VersionKeyOutput.default())()
        out7_: Wrappers.Result
        out7_ = (d_13_eastKeyStore_).VersionKey(AwsCryptographyKeyStoreTypes.VersionKeyInput_VersionKeyInput((d_21_branchKeyId_).branchKeyIdentifier))
        d_26_valueOrError8_ = out7_
        if not(not((d_26_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(236,28): " + _dafny.string_of(d_26_valueOrError8_))
        d_27_versionKeyResult_: AwsCryptographyKeyStoreTypes.VersionKeyOutput
        d_27_versionKeyResult_ = (d_26_valueOrError8_).Extract()
        d_28_valueOrError9_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out8_: Wrappers.Result
        out8_ = (d_15_westKeyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_21_branchKeyId_).branchKeyIdentifier, d_25_oldActiveVersion_))
        d_28_valueOrError9_ = out8_
        if not(not((d_28_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(241,41): " + _dafny.string_of(d_28_valueOrError9_))
        d_29_getBranchKeyVersionResultWest_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_29_getBranchKeyVersionResultWest_ = (d_28_valueOrError9_).Extract()
        d_30_valueOrError10_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out9_: Wrappers.Result
        out9_ = (d_13_eastKeyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_21_branchKeyId_).branchKeyIdentifier, d_25_oldActiveVersion_))
        d_30_valueOrError10_ = out9_
        if not(not((d_30_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(249,41): " + _dafny.string_of(d_30_valueOrError10_))
        d_31_getBranchKeyVersionResultEast_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_31_getBranchKeyVersionResultEast_ = (d_30_valueOrError10_).Extract()
        if not((d_29_getBranchKeyVersionResultWest_) == (d_31_getBranchKeyVersionResultEast_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(257,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_32_valueOrError11_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out10_: Wrappers.Result
        out10_ = (d_15_westKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_21_branchKeyId_).branchKeyIdentifier))
        d_32_valueOrError11_ = out10_
        if not(not((d_32_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(259,31): " + _dafny.string_of(d_32_valueOrError11_))
        d_33_newActiveResultWest_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_33_newActiveResultWest_ = (d_32_valueOrError11_).Extract()
        d_34_valueOrError12_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out11_: Wrappers.Result
        out11_ = (d_13_eastKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_21_branchKeyId_).branchKeyIdentifier))
        d_34_valueOrError12_ = out11_
        if not(not((d_34_valueOrError12_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(263,31): " + _dafny.string_of(d_34_valueOrError12_))
        d_35_newActiveResultEast_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_35_newActiveResultEast_ = (d_34_valueOrError12_).Extract()
        if not((d_33_newActiveResultWest_) == (d_35_newActiveResultEast_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(268,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_36_valueOrError13_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out12_: Wrappers.Result
        out12_ = (d_19_westSrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_21_branchKeyId_).branchKeyIdentifier))
        d_36_valueOrError13_ = out12_
        if not(not((d_36_valueOrError13_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(274,34): " + _dafny.string_of(d_36_valueOrError13_))
        d_37_newActiveResultSrkWest_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_37_newActiveResultSrkWest_ = (d_36_valueOrError13_).Extract()
        if not((d_37_newActiveResultSrkWest_) == (d_35_newActiveResultEast_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(279,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_38_newActiveResultSrkEastResult_: Wrappers.Result
        out13_: Wrappers.Result
        out13_ = (d_17_eastSrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_21_branchKeyId_).branchKeyIdentifier))
        d_38_newActiveResultSrkEastResult_ = out13_
        if not((d_38_newActiveResultSrkEastResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(285,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_38_newActiveResultSrkEastResult_).error) == (AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.GET__KEY__ARN__DISAGREEMENT))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(286,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_39_valueOrError14_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_39_valueOrError14_ = UTF8.default__.Decode(((d_33_newActiveResultWest_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_39_valueOrError14_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(289,32): " + _dafny.string_of(d_39_valueOrError14_))
        d_40_newActiveVersionWest_: _dafny.Seq
        d_40_newActiveVersionWest_ = (d_39_valueOrError14_).Extract()
        d_41_valueOrError15_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_41_valueOrError15_ = UTF8.default__.Decode(((d_35_newActiveResultEast_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_41_valueOrError15_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(290,32): " + _dafny.string_of(d_41_valueOrError15_))
        d_42_newActiveVersionEast_: _dafny.Seq
        d_42_newActiveVersionEast_ = (d_41_valueOrError15_).Extract()
        if not((d_40_newActiveVersionWest_) == (d_42_newActiveVersionEast_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(291,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        CleanupItems.default__.DeleteVersion((d_21_branchKeyId_).branchKeyIdentifier, d_42_newActiveVersionEast_, d_1_ddbClient_)
        CleanupItems.default__.DeleteVersion((d_21_branchKeyId_).branchKeyIdentifier, d_25_oldActiveVersion_, d_1_ddbClient_)
        CleanupItems.default__.DeleteActive((d_21_branchKeyId_).branchKeyIdentifier, d_1_ddbClient_)
        if not((((d_31_getBranchKeyVersionResultEast_).branchKeyMaterials).branchKeyVersion) == (((d_23_oldActiveResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(301,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_31_getBranchKeyVersionResultEast_).branchKeyMaterials).branchKey) == (((d_23_oldActiveResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(302,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_31_getBranchKeyVersionResultEast_).branchKeyMaterials).branchKeyVersion) != (((d_35_newActiveResultEast_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(304,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_31_getBranchKeyVersionResultEast_).branchKeyMaterials).branchKey) != (((d_35_newActiveResultEast_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(305,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def InsertingADuplicateVersionWillFail():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(316,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_1_ddbClient_ = (d_0_valueOrError0_).Extract()
        if not((0) < (len(Fixtures.default__.branchKeyId))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(318,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((0) < (len(Fixtures.default__.branchKeyIdActiveVersion))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(319,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2_customEncryptionContext_: _dafny.Map
        d_2_customEncryptionContext_ = _dafny.Map({})
        def lambda0_(forall_var_0_):
            d_3_k_: _dafny.Seq = forall_var_0_
            return not ((d_3_k_) in (d_2_customEncryptionContext_)) or (ComAmazonawsDynamodbTypes.default__.IsValid__AttributeName((Structure.default__.ENCRYPTION__CONTEXT__PREFIX) + (d_3_k_)))

        if not(_dafny.quantifier((d_2_customEncryptionContext_).keys.Elements, True, lambda0_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(321,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_4_encryptionContext_: _dafny.Map
        d_4_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        if not(ComAmazonawsDynamodbTypes.default__.IsValid__TableName(Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(332,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_5_myBranchKeyStoreName_: _dafny.Seq
        d_5_myBranchKeyStoreName_ = Fixtures.default__.branchKeyStoreName
        d_6_versionBranchKeyItem_: _dafny.Map
        d_6_versionBranchKeyItem_ = Structure.default__.ToAttributeMap(d_4_encryptionContext_, _dafny.Seq([1]))
        d_7_activeBranchKeyItem_: _dafny.Map
        d_7_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_4_encryptionContext_), _dafny.Seq([2]))
        if not(((d_7_activeBranchKeyItem_)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]) == ((d_6_versionBranchKeyItem_)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD])):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(336,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_7_activeBranchKeyItem_)[Structure.default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]) == ((d_6_versionBranchKeyItem_)[Structure.default__.TYPE__FIELD])):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(337,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_8_output_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(d_6_versionBranchKeyItem_, d_7_activeBranchKeyItem_, d_5_myBranchKeyStoreName_, d_1_ddbClient_)
        d_8_output_ = out1_
        if not((d_8_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(346,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def VersioningANonexistentBranchKeyWillFail():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(352,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_1_ddbClient_ = (d_0_valueOrError0_).Extract()
        d_2_encryptionContext_: _dafny.Map
        d_2_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(_dafny.Seq("!= branchKeyId"), Fixtures.default__.branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        d_3_versionBranchKeyItem_: _dafny.Map
        d_3_versionBranchKeyItem_ = Structure.default__.ToAttributeMap(d_2_encryptionContext_, _dafny.Seq([1]))
        d_4_activeBranchKeyItem_: _dafny.Map
        d_4_activeBranchKeyItem_ = Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_2_encryptionContext_), _dafny.Seq([2]))
        if not(((d_4_activeBranchKeyItem_)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]) == ((d_3_versionBranchKeyItem_)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD])):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(365,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_4_activeBranchKeyItem_)[Structure.default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]) == ((d_3_versionBranchKeyItem_)[Structure.default__.TYPE__FIELD])):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(366,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(ComAmazonawsDynamodbTypes.default__.IsValid__TableName(Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(367,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_5_myBranchKeyStoreName_: _dafny.Seq
        d_5_myBranchKeyStoreName_ = Fixtures.default__.branchKeyStoreName
        d_6_output_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = DDBKeystoreOperations.default__.WriteNewBranchKeyVersionToKeystore(d_3_versionBranchKeyItem_, d_4_activeBranchKeyItem_, d_5_myBranchKeyStoreName_, d_1_ddbClient_)
        d_6_output_ = out1_
        if not((d_6_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestVersionKey.dfy(377,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

