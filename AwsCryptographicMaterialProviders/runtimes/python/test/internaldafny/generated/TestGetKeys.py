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

# Module: TestGetKeys

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestGetBeaconKey():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(23,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(24,21): " + _dafny.string_of(d_2_valueOrError1_))
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
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(37,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput.default())()
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).GetBeaconKey(AwsCryptographyKeyStoreTypes.GetBeaconKeyInput_GetBeaconKeyInput(Fixtures.default__.branchKeyId))
        d_8_valueOrError3_ = out3_
        if not(not((d_8_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(39,27): " + _dafny.string_of(d_8_valueOrError3_))
        d_9_beaconKeyResult_: AwsCryptographyKeyStoreTypes.GetBeaconKeyOutput
        d_9_beaconKeyResult_ = (d_8_valueOrError3_).Extract()
        if not((((d_9_beaconKeyResult_).beaconKeyMaterials).beaconKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(43,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_9_beaconKeyResult_).beaconKeyMaterials).beaconKey).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((((d_9_beaconKeyResult_).beaconKeyMaterials).beaconKey).value)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(45,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKey():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(50,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(51,21): " + _dafny.string_of(d_2_valueOrError1_))
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
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(64,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_8_valueOrError3_ = out3_
        if not(not((d_8_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(66,24): " + _dafny.string_of(d_8_valueOrError3_))
        d_9_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_9_activeResult_ = (d_8_valueOrError3_).Extract()
        if not((((d_9_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(71,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_9_activeResult_).branchKeyMaterials).branchKeyVersion) == (Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_9_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(73,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveMrkKey():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(78,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_1_ddbClient_ = (d_0_valueOrError0_).Extract()
        d_2_eastKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_2_eastKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsConfigEast, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_1_ddbClient_), Wrappers.Option_None())
        d_3_westKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_3_westKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsConfigWest, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_1_ddbClient_), Wrappers.Option_None())
        d_4_eastMrkKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_4_eastMrkKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsMrkConfigEast, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_1_ddbClient_), Wrappers.Option_None())
        d_5_westMrkKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_5_westMrkKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsMrkConfigWest, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_1_ddbClient_), Wrappers.Option_None())
        d_6_apMrkKeyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_6_apMrkKeyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, Fixtures.default__.KmsMrkConfigAP, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_1_ddbClient_), Wrappers.Option_None())
        d_7_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = KeyStore.default__.KeyStore(d_3_westKeyStoreConfig_)
        d_7_valueOrError1_ = out1_
        if not(not((d_7_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(127,24): " + _dafny.string_of(d_7_valueOrError1_))
        d_8_westKeyStore_: KeyStore.KeyStoreClient
        d_8_westKeyStore_ = (d_7_valueOrError1_).Extract()
        d_9_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_2_eastKeyStoreConfig_)
        d_9_valueOrError2_ = out2_
        if not(not((d_9_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(128,24): " + _dafny.string_of(d_9_valueOrError2_))
        d_10_eastKeyStore_: KeyStore.KeyStoreClient
        d_10_eastKeyStore_ = (d_9_valueOrError2_).Extract()
        d_11_valueOrError3_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = KeyStore.default__.KeyStore(d_5_westMrkKeyStoreConfig_)
        d_11_valueOrError3_ = out3_
        if not(not((d_11_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(129,27): " + _dafny.string_of(d_11_valueOrError3_))
        d_12_westMrkKeyStore_: KeyStore.KeyStoreClient
        d_12_westMrkKeyStore_ = (d_11_valueOrError3_).Extract()
        d_13_valueOrError4_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = KeyStore.default__.KeyStore(d_4_eastMrkKeyStoreConfig_)
        d_13_valueOrError4_ = out4_
        if not(not((d_13_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(130,27): " + _dafny.string_of(d_13_valueOrError4_))
        d_14_eastMrkKeyStore_: KeyStore.KeyStoreClient
        d_14_eastMrkKeyStore_ = (d_13_valueOrError4_).Extract()
        d_15_valueOrError5_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = KeyStore.default__.KeyStore(d_6_apMrkKeyStoreConfig_)
        d_15_valueOrError5_ = out5_
        if not(not((d_15_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(131,25): " + _dafny.string_of(d_15_valueOrError5_))
        d_16_apMrkKeyStore_: KeyStore.KeyStoreClient
        d_16_apMrkKeyStore_ = (d_15_valueOrError5_).Extract()
        d_17_valueOrError6_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out6_: Wrappers.Result
        out6_ = (d_8_westKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.WestBranchKey))
        d_17_valueOrError6_ = out6_
        if not(not((d_17_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(135,24): " + _dafny.string_of(d_17_valueOrError6_))
        d_18_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_18_activeResult_ = (d_17_valueOrError6_).Extract()
        if not((((d_18_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.WestBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(137,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_18_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(138,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_19_valueOrError7_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out7_: Wrappers.Result
        out7_ = (d_10_eastKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.EastBranchKey))
        d_19_valueOrError7_ = out7_
        if not(not((d_19_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(140,20): " + _dafny.string_of(d_19_valueOrError7_))
        d_18_activeResult_ = (d_19_valueOrError7_).Extract()
        if not((((d_18_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.EastBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(142,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_18_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(143,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_20_valueOrError8_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out8_: Wrappers.Result
        out8_ = (d_12_westMrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.WestBranchKey))
        d_20_valueOrError8_ = out8_
        if not(not((d_20_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(145,20): " + _dafny.string_of(d_20_valueOrError8_))
        d_18_activeResult_ = (d_20_valueOrError8_).Extract()
        if not((((d_18_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.WestBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(147,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_18_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(148,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_21_valueOrError9_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out9_: Wrappers.Result
        out9_ = (d_14_eastMrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.EastBranchKey))
        d_21_valueOrError9_ = out9_
        if not(not((d_21_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(150,20): " + _dafny.string_of(d_21_valueOrError9_))
        d_18_activeResult_ = (d_21_valueOrError9_).Extract()
        if not((((d_18_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.EastBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(152,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_18_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(153,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_22_valueOrError10_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out10_: Wrappers.Result
        out10_ = (d_12_westMrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.EastBranchKey))
        d_22_valueOrError10_ = out10_
        if not(not((d_22_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(157,20): " + _dafny.string_of(d_22_valueOrError10_))
        d_18_activeResult_ = (d_22_valueOrError10_).Extract()
        if not((((d_18_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.EastBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(159,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_18_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(160,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_23_valueOrError11_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out11_: Wrappers.Result
        out11_ = (d_14_eastMrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.WestBranchKey))
        d_23_valueOrError11_ = out11_
        if not(not((d_23_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(162,20): " + _dafny.string_of(d_23_valueOrError11_))
        d_18_activeResult_ = (d_23_valueOrError11_).Extract()
        if not((((d_18_activeResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.WestBranchKey)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(164,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_18_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(165,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_24_badResult_: Wrappers.Result
        out12_: Wrappers.Result
        out12_ = (d_8_westKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.EastBranchKey))
        d_24_badResult_ = out12_
        if not((d_24_badResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(171,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_24_badResult_).error) == (AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.GET__KEY__ARN__DISAGREEMENT))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(172,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out13_: Wrappers.Result
        out13_ = (d_10_eastKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.WestBranchKey))
        d_24_badResult_ = out13_
        if not((d_24_badResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(176,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_24_badResult_).error) == (AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.GET__KEY__ARN__DISAGREEMENT))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(177,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out14_: Wrappers.Result
        out14_ = (d_16_apMrkKeyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.WestBranchKey))
        d_24_badResult_ = out14_
        if not((d_24_badResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(183,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_24_badResult_).error).is_ComAmazonawsKms):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(184,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_24_badResult_).error).ComAmazonawsKms).is_Opaque):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(185,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetBranchKeyVersion():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(191,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(192,21): " + _dafny.string_of(d_2_valueOrError1_))
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
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(205,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(Fixtures.default__.branchKeyId, Fixtures.default__.branchKeyIdActiveVersion))
        d_8_valueOrError3_ = out3_
        if not(not((d_8_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(207,25): " + _dafny.string_of(d_8_valueOrError3_))
        d_9_versionResult_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
        d_9_versionResult_ = (d_8_valueOrError3_).Extract()
        d_10_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_10_valueOrError4_ = UTF8.default__.Encode(Fixtures.default__.branchKeyIdActiveVersion)
        if not(not((d_10_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(213,21): " + _dafny.string_of(d_10_valueOrError4_))
        d_11_testBytes_: _dafny.Seq
        d_11_testBytes_ = (d_10_valueOrError4_).Extract()
        if not((((d_9_versionResult_).branchKeyMaterials).branchKeyIdentifier) == (Fixtures.default__.branchKeyId)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(215,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_9_versionResult_).branchKeyMaterials).branchKeyVersion) == (Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes)) and ((Fixtures.default__.branchKeyIdActiveVersionUtf8Bytes) == (d_11_testBytes_))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(216,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_9_versionResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(217,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWithIncorrectKmsKeyArn():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(222,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(223,21): " + _dafny.string_of(d_2_valueOrError1_))
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
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(236,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_activeResult_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.postalHornBranchKeyId))
        d_8_activeResult_ = out3_
        if not((d_8_activeResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(242,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_8_activeResult_).error) == (AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.GET__KEY__ARN__DISAGREEMENT))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(243,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWrongLogicalKeyStoreName():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(247,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(248,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_3_ddbClient_ = (d_2_valueOrError1_).Extract()
        d_4_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_4_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_5_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_5_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_4_kmsConfig_, default__.incorrectLogicalName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_3_ddbClient_), Wrappers.Option_Some(d_1_kmsClient_))
        d_6_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = KeyStore.default__.KeyStore(d_5_keyStoreConfig_)
        d_6_valueOrError2_ = out2_
        if not(not((d_6_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(261,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_activeResult_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_8_activeResult_ = out3_
        if not((d_8_activeResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(268,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        source0_ = (d_8_activeResult_).error
        with _dafny.label("match0"):
            if True:
                if source0_.is_ComAmazonawsKms:
                    d_9_nestedError_ = source0_.ComAmazonawsKms
                    if not((d_9_nestedError_).is_InvalidCiphertextException):
                        raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(271,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
                    raise _dafny.Break("match0")
            if True:
                if not(False):
                    raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(272,16): " + _dafny.string_of(_dafny.Seq("Wrong Logical Keystore Name SHOULD Fail with KMS InvalidCiphertextException.")))
            pass

    @staticmethod
    def TestGetActiveKeyDoesNotExistFails():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(278,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(279,21): " + _dafny.string_of(d_2_valueOrError1_))
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
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(292,20): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_keyStore_: KeyStore.KeyStoreClient
        d_7_keyStore_ = (d_6_valueOrError2_).Extract()
        d_8_activeResult_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_7_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(_dafny.Seq("Robbie")))
        d_8_activeResult_ = out3_
        if not((d_8_activeResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(299,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_8_activeResult_).error) == (AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.NO__CORRESPONDING__BRANCH__KEY))):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(300,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestGetActiveKeyWithNoClients():
        d_0_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_0_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_1_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_1_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_0_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_2_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = KeyStore.default__.KeyStore(d_1_keyStoreConfig_)
        d_2_valueOrError0_ = out0_
        if not(not((d_2_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(317,20): " + _dafny.string_of(d_2_valueOrError0_))
        d_3_keyStore_: KeyStore.KeyStoreClient
        d_3_keyStore_ = (d_2_valueOrError0_).Extract()
        d_4_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
        out1_: Wrappers.Result
        out1_ = (d_3_keyStore_).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(Fixtures.default__.branchKeyId))
        d_4_valueOrError1_ = out1_
        if not(not((d_4_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(319,24): " + _dafny.string_of(d_4_valueOrError1_))
        d_5_activeResult_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
        d_5_activeResult_ = (d_4_valueOrError1_).Extract()
        if not((len(((d_5_activeResult_).branchKeyMaterials).branchKey)) == (32)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestGetKeys.dfy(324,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def incorrectLogicalName(instance):
        return _dafny.Seq("MySuperAwesomeTableName")
