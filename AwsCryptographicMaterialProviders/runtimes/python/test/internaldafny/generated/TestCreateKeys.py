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

# Module: TestCreateKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestCreateBranchAndBeaconKeys():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(68,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(69,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_3_ddbClient_ = (d_2_valueOrError1_).Extract()
        d_4_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_4_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_5_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_5_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_4_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_3_ddbClient_), Wrappers.Option_Some(d_1_kmsClient_))
        d_6_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_5_keyStoreConfig_)
        d_6_valueOrError2_ = out2_
        if not(not((d_6_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(82,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_None(), Wrappers.Option_None()))
        d_8_valueOrError3_ = out3_
        if not(not((d_8_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(84,23): " + _dafny.string_of(d_8_valueOrError3_))
        d_9_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_9_branchKeyId_ = (d_8_valueOrError3_).Extract()
        d_10_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out4_: Wrappers.Result
        out4_ = (d_7_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput((d_9_branchKeyId_).branchKeyIdentifier))
        d_10_valueOrError4_ = out4_
        if not(not((d_10_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(88,27): " + _dafny.string_of(d_10_valueOrError4_))
        d_11_beaconKeyResult_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_11_beaconKeyResult_ = (d_10_valueOrError4_).Extract()
        d_12_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out5_: Wrappers.Result
        out5_ = (d_7_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_9_branchKeyId_).branchKeyIdentifier))
        d_12_valueOrError5_ = out5_
        if not(not((d_12_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(93,24): " + _dafny.string_of(d_12_valueOrError5_))
        d_13_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_13_activeResult_ = (d_12_valueOrError5_).Extract()
        d_14_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_14_valueOrError6_ = UTF8.default__.Decode(((d_13_activeResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_14_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(98,28): " + _dafny.string_of(d_14_valueOrError6_))
        d_15_branchKeyVersion_: _dafny.Seq
        d_15_branchKeyVersion_ = (d_14_valueOrError6_).Extract()
        d_16_valueOrError7_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out6_: Wrappers.Result
        out6_ = (d_7_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_9_branchKeyId_).branchKeyIdentifier, d_15_branchKeyVersion_))
        d_16_valueOrError7_ = out6_
        if not(not((d_16_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(99,25): " + _dafny.string_of(d_16_valueOrError7_))
        d_17_versionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_17_versionResult_ = (d_16_valueOrError7_).Extract()
        CleanupItems.default__.DeleteVersion((d_9_branchKeyId_).branchKeyIdentifier, d_15_branchKeyVersion_, d_3_ddbClient_)
        CleanupItems.default__.DeleteActive((d_9_branchKeyId_).branchKeyIdentifier, d_3_ddbClient_)
        if not((((d_11_beaconKeyResult_).beaconKeyMaterials).beaconKey).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(111,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((((d_11_beaconKeyResult_).beaconKeyMaterials).beaconKey).value)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_13_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_17_versionResult_).branchKeyMaterials).branchKey) == (((d_13_activeResult_).branchKeyMaterials).branchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(114,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_17_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_13_activeResult_).branchKeyMaterials).branchKeyIdentifier)) and ((((d_13_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_11_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(115,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_17_versionResult_).branchKeyMaterials).branchKeyVersion) == (((d_13_activeResult_).branchKeyMaterials).branchKeyVersion)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(118,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_18_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_18_valueOrError8_ = UUID.default__.ToByteArray(((d_13_activeResult_).branchKeyMaterials).branchKeyIdentifier)
        if not(not((d_18_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(125,22): " + _dafny.string_of(d_18_valueOrError8_))
        d_19_idByteUUID_: _dafny.Seq
        d_19_idByteUUID_ = (d_18_valueOrError8_).Extract()
        d_20_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_20_valueOrError9_ = UUID.default__.FromByteArray(d_19_idByteUUID_)
        if not(not((d_20_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(126,23): " + _dafny.string_of(d_20_valueOrError9_))
        d_21_idRoundTrip_: _dafny.Seq
        d_21_idRoundTrip_ = (d_20_valueOrError9_).Extract()
        if not((d_21_idRoundTrip_) == (((d_13_activeResult_).branchKeyMaterials).branchKeyIdentifier)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(127,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_22_valueOrError10_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_22_valueOrError10_ = UTF8.default__.Decode(((d_13_activeResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_22_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(133,25): " + _dafny.string_of(d_22_valueOrError10_))
        d_23_versionString_: _dafny.Seq
        d_23_versionString_ = (d_22_valueOrError10_).Extract()
        d_24_valueOrError11_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_24_valueOrError11_ = UUID.default__.ToByteArray(d_23_versionString_)
        if not(not((d_24_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(134,27): " + _dafny.string_of(d_24_valueOrError11_))
        d_25_versionByteUUID_: _dafny.Seq
        d_25_versionByteUUID_ = (d_24_valueOrError11_).Extract()
        d_26_valueOrError12_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_26_valueOrError12_ = UUID.default__.FromByteArray(d_25_versionByteUUID_)
        if not(not((d_26_valueOrError12_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(135,28): " + _dafny.string_of(d_26_valueOrError12_))
        d_27_versionRoundTrip_: _dafny.Seq
        d_27_versionRoundTrip_ = (d_26_valueOrError12_).Extract()
        if not((d_27_versionRoundTrip_) == (d_23_versionString_)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(136,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCreateOptions():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(142,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(143,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_3_ddbClient_ = (d_2_valueOrError1_).Extract()
        d_4_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_4_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_5_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_5_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_4_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_3_ddbClient_), Wrappers.Option_Some(d_1_kmsClient_))
        d_6_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_5_keyStoreConfig_)
        d_6_valueOrError2_ = out2_
        if not(not((d_6_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(156,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out3_: Wrappers.Result
        out3_ = UUID.default__.GenerateUUID()
        d_8_valueOrError3_ = out3_
        if not(not((d_8_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(159,14): " + _dafny.string_of(d_8_valueOrError3_))
        d_9_id_: _dafny.Seq
        d_9_id_ = (d_8_valueOrError3_).Extract()
        d_10_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        out4_: Wrappers.Result
        out4_ = Fixtures.default__.EncodeEncryptionContext(_dafny.Map({_dafny.Seq("some"): _dafny.Seq("encryption"), _dafny.Seq("context"): _dafny.Seq("values")}))
        d_10_valueOrError4_ = out4_
        if not(not((d_10_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(161,29): " + _dafny.string_of(d_10_valueOrError4_))
        d_11_encryptionContext_: _dafny.Map
        d_11_encryptionContext_ = (d_10_valueOrError4_).Extract()
        d_12_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.CreateKeyOutput.default())()
        out5_: Wrappers.Result
        out5_ = (d_7_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_Some(d_9_id_), Wrappers.Option_Some(d_11_encryptionContext_)))
        d_12_valueOrError5_ = out5_
        if not(not((d_12_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(166,23): " + _dafny.string_of(d_12_valueOrError5_))
        d_13_branchKeyId_: AwsCryptographyKeyStoreTypes.CreateKeyOutput
        d_13_branchKeyId_ = (d_12_valueOrError5_).Extract()
        d_14_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out6_: Wrappers.Result
        out6_ = (d_7_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput((d_13_branchKeyId_).branchKeyIdentifier))
        d_14_valueOrError6_ = out6_
        if not(not((d_14_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(171,27): " + _dafny.string_of(d_14_valueOrError6_))
        d_15_beaconKeyResult_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_15_beaconKeyResult_ = (d_14_valueOrError6_).Extract()
        d_16_valueOrError7_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out7_: Wrappers.Result
        out7_ = (d_7_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput((d_13_branchKeyId_).branchKeyIdentifier))
        d_16_valueOrError7_ = out7_
        if not(not((d_16_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(176,24): " + _dafny.string_of(d_16_valueOrError7_))
        d_17_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_17_activeResult_ = (d_16_valueOrError7_).Extract()
        d_18_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_18_valueOrError8_ = UTF8.default__.Decode(((d_17_activeResult_).branchKeyMaterials).branchKeyVersion)
        if not(not((d_18_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(181,28): " + _dafny.string_of(d_18_valueOrError8_))
        d_19_branchKeyVersion_: _dafny.Seq
        d_19_branchKeyVersion_ = (d_18_valueOrError8_).Extract()
        d_20_valueOrError9_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out8_: Wrappers.Result
        out8_ = (d_7_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput((d_13_branchKeyId_).branchKeyIdentifier, d_19_branchKeyVersion_))
        d_20_valueOrError9_ = out8_
        if not(not((d_20_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(182,25): " + _dafny.string_of(d_20_valueOrError9_))
        d_21_versionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_21_versionResult_ = (d_20_valueOrError9_).Extract()
        CleanupItems.default__.DeleteVersion((d_13_branchKeyId_).branchKeyIdentifier, d_19_branchKeyVersion_, d_3_ddbClient_)
        CleanupItems.default__.DeleteActive((d_13_branchKeyId_).branchKeyIdentifier, d_3_ddbClient_)
        if not((((d_9_id_) == (((d_21_versionResult_).branchKeyMaterials).branchKeyIdentifier)) and ((((d_21_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_17_activeResult_).branchKeyMaterials).branchKeyIdentifier))) and ((((d_17_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (((d_15_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(195,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_11_encryptionContext_) == (((d_21_versionResult_).branchKeyMaterials).encryptionContext)) and ((((d_21_versionResult_).branchKeyMaterials).encryptionContext) == (((d_17_activeResult_).branchKeyMaterials).encryptionContext))) and ((((d_17_activeResult_).branchKeyMaterials).encryptionContext) == (((d_15_beaconKeyResult_).beaconKeyMaterials).encryptionContext))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(200,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestCreateDuplicate():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(209,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(210,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_3_ddbClient_ = (d_2_valueOrError1_).Extract()
        d_4_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_4_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_5_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_5_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_4_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_3_ddbClient_), Wrappers.Option_Some(d_1_kmsClient_))
        d_6_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_5_keyStoreConfig_)
        d_6_valueOrError2_ = out2_
        if not(not((d_6_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(223,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_attempt_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).CreateKey(AwsCryptographyKeyStoreTypes.CreateKeyInput_CreateKeyInput(Wrappers.Option_Some(Fixtures.default__.branchKeyId), Wrappers.Option_None()))
        d_8_attempt_ = out3_
        if not((d_8_attempt_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(230,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def InsertingADuplicateWillFail():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(236,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_1_ddbClient_ = (d_0_valueOrError0_).Extract()
        d_2_encryptionContext_: _dafny.Map
        d_2_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion, _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        d_3_output_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(Structure.default__.ToAttributeMap(d_2_encryptionContext_, _dafny.Seq([1])), Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_2_encryptionContext_), _dafny.Seq([2])), Structure.default__.ToAttributeMap(Structure.default__.BeaconKeyEncryptionContext(d_2_encryptionContext_), _dafny.Seq([3])), Fixtures.default__.branchKeyStoreName, d_1_ddbClient_)
        d_3_output_ = out1_
        if not((d_3_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(255,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def InsertingADuplicateWillWithADifferentVersionFail():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(261,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_1_ddbClient_ = (d_0_valueOrError0_).Extract()
        d_2_encryptionContext_: _dafny.Map
        d_2_encryptionContext_ = Structure.default__.DecryptOnlyBranchKeyEncryptionContext(Fixtures.default__.branchKeyId, _dafny.Seq("!= branchKeyIdActiveVersion"), _dafny.Seq(""), _dafny.Seq(""), Fixtures.default__.keyArn, _dafny.Map({}))
        d_3_output_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = DDBKeystoreOperations.default__.WriteNewKeyToStore(Structure.default__.ToAttributeMap(d_2_encryptionContext_, _dafny.Seq([1])), Structure.default__.ToAttributeMap(Structure.default__.ActiveBranchKeyEncryptionContext(d_2_encryptionContext_), _dafny.Seq([2])), Structure.default__.ToAttributeMap(Structure.default__.BeaconKeyEncryptionContext(d_2_encryptionContext_), _dafny.Seq([3])), Fixtures.default__.branchKeyStoreName, d_1_ddbClient_)
        d_3_output_ = out1_
        if not((d_3_output_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeys.dfy(280,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

