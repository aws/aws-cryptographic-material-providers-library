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

# Module: TestDiscoveryGetKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestGetBeaconKeyForTwoKmsArnsSuccess():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(24,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(25,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_3_ddbClient_ = (d_2_valueOrError1_).Extract()
        d_4_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_4_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_discovery(AwsCryptographyKeyStoreTypes.Discovery_Discovery())
        d_5_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_5_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_4_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_3_ddbClient_), Wrappers.Option_Some(d_1_kmsClient_))
        d_6_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_5_keyStoreConfig_)
        d_6_valueOrError2_ = out2_
        if not(not((d_6_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(38,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.branchKeyId))
        d_8_valueOrError3_ = out3_
        if not(not((d_8_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(40,27): " + _dafny.string_of(d_8_valueOrError3_))
        d_9_beaconKeyResult_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_9_beaconKeyResult_ = (d_8_valueOrError3_).Extract()
        if not((((d_9_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_10_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out4_: Wrappers.Result
        out4_ = (d_7_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.postalHornBranchKeyId))
        d_10_valueOrError4_ = out4_
        if not(not((d_10_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(46,23): " + _dafny.string_of(d_10_valueOrError4_))
        d_9_beaconKeyResult_ = (d_10_valueOrError4_).Extract()
        if not((((d_9_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier) == (Fixtures.default__.postalHornBranchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(51,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyForTwoKmsArnsSuccess():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(57,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(58,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_3_ddbClient_ = (d_2_valueOrError1_).Extract()
        d_4_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_4_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_discovery(AwsCryptographyKeyStoreTypes.Discovery_Discovery())
        d_5_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_5_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_4_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_3_ddbClient_), Wrappers.Option_Some(d_1_kmsClient_))
        d_6_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_5_keyStoreConfig_)
        d_6_valueOrError2_ = out2_
        if not(not((d_6_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(71,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_8_valueOrError3_ = out3_
        if not(not((d_8_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(73,24): " + _dafny.string_of(d_8_valueOrError3_))
        d_9_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_9_activeResult_ = (d_8_valueOrError3_).Extract()
        if not((((d_9_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(78,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_10_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out4_: Wrappers.Result
        out4_ = (d_7_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.postalHornBranchKeyId))
        d_10_valueOrError4_ = out4_
        if not(not((d_10_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(80,20): " + _dafny.string_of(d_10_valueOrError4_))
        d_9_activeResult_ = (d_10_valueOrError4_).Extract()
        if not((((d_9_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.postalHornBranchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(85,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetBranchKeyVersionForTwoKmsArnsSuccess():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(90,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(91,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_3_ddbClient_ = (d_2_valueOrError1_).Extract()
        d_4_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_4_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_discovery(AwsCryptographyKeyStoreTypes.Discovery_Discovery())
        d_5_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_5_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_4_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_3_ddbClient_), Wrappers.Option_Some(d_1_kmsClient_))
        d_6_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_5_keyStoreConfig_)
        d_6_valueOrError2_ = out2_
        if not(not((d_6_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(104,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion))
        d_8_valueOrError3_ = out3_
        if not(not((d_8_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(106,25): " + _dafny.string_of(d_8_valueOrError3_))
        d_9_versionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_9_versionResult_ = (d_8_valueOrError3_).Extract()
        d_10_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_10_valueOrError4_ = UTF8.default__.Encode(Fixtures.default__.branchKeyIdActiveVersion)
        if not(not((d_10_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(111,21): " + _dafny.string_of(d_10_valueOrError4_))
        d_11_testBytes_: _dafny.Seq
        d_11_testBytes_ = (d_10_valueOrError4_).Extract()
        if not((((d_9_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_9_versionResult_).branchKeyMaterials).branchKeyVersion) == (Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes)) and ((Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes) == (d_11_testBytes_))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_12_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out4_: Wrappers.Result
        out4_ = (d_7_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(Fixtures.default__.postalHornBranchKeyId, Fixtures.default__.postalHornBranchKeyActiveVersion))
        d_12_valueOrError5_ = out4_
        if not(not((d_12_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(115,21): " + _dafny.string_of(d_12_valueOrError5_))
        d_9_versionResult_ = (d_12_valueOrError5_).Extract()
        d_13_valueOrError6_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_13_valueOrError6_ = UTF8.default__.Encode(Fixtures.default__.postalHornBranchKeyActiveVersion)
        if not(not((d_13_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(120,17): " + _dafny.string_of(d_13_valueOrError6_))
        d_11_testBytes_ = (d_13_valueOrError6_).Extract()
        if not((((d_9_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.postalHornBranchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(121,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_9_versionResult_).branchKeyMaterials).branchKeyVersion) == (d_11_testBytes_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(122,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetKeysForMrk():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(127,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(128,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_3_ddbClient_ = (d_2_valueOrError1_).Extract()
        d_4_kmsConfigMr_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_4_kmsConfigMr_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_mrDiscovery(AwsCryptographyKeyStoreTypes.MRDiscovery_MRDiscovery(_dafny.Seq("us-west-2")))
        d_5_kmsConfigSr_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_5_kmsConfigSr_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_discovery(AwsCryptographyKeyStoreTypes.Discovery_Discovery())
        d_6_keyStoreConfigMr_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_6_keyStoreConfigMr_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_4_kmsConfigMr_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_3_ddbClient_), Wrappers.Option_Some(d_1_kmsClient_))
        d_7_keyStoreConfigSr_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_8_dt__update__tmp_h0_ = d_6_keyStoreConfigMr_
        d_9_dt__update_hkmsConfiguration_h0_ = d_5_kmsConfigSr_
        d_7_keyStoreConfigSr_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig((d_8_dt__update__tmp_h0_).ddbTableName, d_9_dt__update_hkmsConfiguration_h0_, (d_8_dt__update__tmp_h0_).logicalKeyStoreName, (d_8_dt__update__tmp_h0_).id, (d_8_dt__update__tmp_h0_).grantTokens, (d_8_dt__update__tmp_h0_).ddbClient, (d_8_dt__update__tmp_h0_).kmsClient)
        d_10_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_6_keyStoreConfigMr_)
        d_10_valueOrError2_ = out2_
        if not(not((d_10_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(144,22): " + _dafny.string_of(d_10_valueOrError2_))
        d_11_keyStoreMr_: KeyStore.KeyStoreClient
        d_11_keyStoreMr_ = (d_10_valueOrError2_).Extract()
        d_12_valueOrError3_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = KeyStore.default__.KeyStore(d_7_keyStoreConfigSr_)
        d_12_valueOrError3_ = out3_
        if not(not((d_12_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(145,22): " + _dafny.string_of(d_12_valueOrError3_))
        d_13_keyStoreSr_: KeyStore.KeyStoreClient
        d_13_keyStoreSr_ = (d_12_valueOrError3_).Extract()
        d_14_beaconInput_: AwsCryptographyKeyStoreTypes.GetBeaconKeyInput
        d_14_beaconInput_ = AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.EastBranchKey)
        d_15_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out4_: Wrappers.Result
        out4_ = (d_11_keyStoreMr_).GetBeaconKey(d_14_beaconInput_)
        d_15_valueOrError4_ = out4_
        if not(not((d_15_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(148,29): " + _dafny.string_of(d_15_valueOrError4_))
        d_16_beaconKeyResultMr_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_16_beaconKeyResultMr_ = (d_15_valueOrError4_).Extract()
        if not((((d_16_beaconKeyResultMr_).beaconKeyMaterials).beaconKeyIdentifier) == (Fixtures.default__.EastBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(149,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_17_beaconKeyResultSr_: Wrappers.Result
        out5_: Wrappers.Result
        out5_ = (d_13_keyStoreSr_).GetBeaconKey(d_14_beaconInput_)
        d_17_beaconKeyResultSr_ = out5_
        if not((d_17_beaconKeyResultSr_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(152,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_17_beaconKeyResultSr_).error).is_ComAmazonawsKms):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(153,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source0_ = (d_17_beaconKeyResultSr_).error
        with _dafny.label("match0"):
            if True:
                if source0_.is_ComAmazonawsKms:
                    d_18_nestedError_ = source0_.ComAmazonawsKms
                    if not((d_18_nestedError_).is_IncorrectKeyException):
                        raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(156,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                    raise _dafny.Break("match0")
            if True:
                if not(False):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(157,16): " + _dafny.string_of(_dafny.Seq("Request for Branch Key's Beacon Key protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")))
            pass
        d_19_branchInput_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput
        d_19_branchInput_ = AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.EastBranchKey)
        d_20_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out6_: Wrappers.Result
        out6_ = (d_11_keyStoreMr_).GetActiveBranchKey(d_19_branchInput_)
        d_20_valueOrError5_ = out6_
        if not(not((d_20_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(161,29): " + _dafny.string_of(d_20_valueOrError5_))
        d_21_branchKeyResultMr_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_21_branchKeyResultMr_ = (d_20_valueOrError5_).Extract()
        if not((((d_21_branchKeyResultMr_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.EastBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(162,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_22_branchKeyResultSr_: Wrappers.Result
        out7_: Wrappers.Result
        out7_ = (d_13_keyStoreSr_).GetActiveBranchKey(d_19_branchInput_)
        d_22_branchKeyResultSr_ = out7_
        if not((d_22_branchKeyResultSr_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(165,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_22_branchKeyResultSr_).error).is_ComAmazonawsKms):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(166,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source1_ = (d_22_branchKeyResultSr_).error
        with _dafny.label("match1"):
            if True:
                if source1_.is_ComAmazonawsKms:
                    d_23_nestedError_ = source1_.ComAmazonawsKms
                    if not((d_23_nestedError_).is_IncorrectKeyException):
                        raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(170,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                    raise _dafny.Break("match1")
            if True:
                if not(False):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestDiscoveryGetKeys.dfy(171,16): " + _dafny.string_of(_dafny.Seq("Request for Branch Key Active Version protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.")))
            pass

