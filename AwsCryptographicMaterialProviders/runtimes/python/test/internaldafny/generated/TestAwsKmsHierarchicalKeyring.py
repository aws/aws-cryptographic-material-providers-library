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
import TestVersionKey as TestVersionKey
import TestUtils as TestUtils
import TestIntermediateKeyWrapping as TestIntermediateKeyWrapping
import TestErrorMessages as TestErrorMessages
import TestDefaultClientProvider as TestDefaultClientProvider
import TestRawECDHKeyring as TestRawECDHKeyring
import TestRawAESKeyring as TestRawAESKeyring
import TestMultiKeyring as TestMultiKeyring
import TestRawRSAKeying as TestRawRSAKeying
import TestAwsKmsRsaKeyring as TestAwsKmsRsaKeyring

# Module: TestAwsKmsHierarchicalKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetTestMaterials(suiteId):
        out: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = None
        d_1051_mpl_: MaterialProviders.MaterialProvidersClient
        d_1052_valueOrError0_: Wrappers.Result = None
        out413_: Wrappers.Result
        out413_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1052_valueOrError0_ = out413_
        if not(not((d_1052_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(54,15): " + _dafny.string_of(d_1052_valueOrError0_))
        d_1051_mpl_ = (d_1052_valueOrError0_).Extract()
        d_1053_encryptionContext_: _dafny.Map
        out414_: _dafny.Map
        out414_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_1053_encryptionContext_ = out414_
        d_1054_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1054_suite_ = AlgorithmSuites.default__.GetSuite(suiteId)
        d_1055_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_1056_valueOrError1_: Wrappers.Result = None
        d_1056_valueOrError1_ = (d_1051_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(suiteId, d_1053_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_1056_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(59,33): " + _dafny.string_of(d_1056_valueOrError1_))
        d_1055_encryptionMaterialsIn_ = (d_1056_valueOrError1_).Extract()
        out = d_1055_encryptionMaterialsIn_
        return out
        return out

    @staticmethod
    def TestHierarchyClientESDKSuite():
        d_1057_branchKeyId_: _dafny.Seq
        d_1057_branchKeyId_ = default__.BRANCH__KEY__ID
        d_1058_ttl_: int
        d_1058_ttl_ = ((1) * (60000)) * (10)
        d_1059_mpl_: MaterialProviders.MaterialProvidersClient
        d_1060_valueOrError0_: Wrappers.Result = None
        out415_: Wrappers.Result
        out415_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1060_valueOrError0_ = out415_
        if not(not((d_1060_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(76,15): " + _dafny.string_of(d_1060_valueOrError0_))
        d_1059_mpl_ = (d_1060_valueOrError0_).Extract()
        d_1061_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1062_valueOrError1_: Wrappers.Result = None
        out416_: Wrappers.Result
        out416_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1062_valueOrError1_ = out416_
        if not(not((d_1062_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(78,21): " + _dafny.string_of(d_1062_valueOrError1_))
        d_1061_kmsClient_ = (d_1062_valueOrError1_).Extract()
        d_1063_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_1064_valueOrError2_: Wrappers.Result = None
        out417_: Wrappers.Result
        out417_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_1064_valueOrError2_ = out417_
        if not(not((d_1064_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(79,21): " + _dafny.string_of(d_1064_valueOrError2_))
        d_1063_ddbClient_ = (d_1064_valueOrError2_).Extract()
        d_1065_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_1065_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(default__.keyArn)
        d_1066_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_1066_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(default__.branchKeyStoreName, d_1065_kmsConfig_, default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_1063_ddbClient_), Wrappers.Option_Some(d_1061_kmsClient_))
        d_1067_keyStore_: KeyStore.KeyStoreClient
        d_1068_valueOrError3_: Wrappers.Result = None
        out418_: Wrappers.Result
        out418_ = KeyStore.default__.KeyStore(d_1066_keyStoreConfig_)
        d_1068_valueOrError3_ = out418_
        if not(not((d_1068_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(92,20): " + _dafny.string_of(d_1068_valueOrError3_))
        d_1067_keyStore_ = (d_1068_valueOrError3_).Extract()
        d_1069_hierarchyKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_1070_valueOrError4_: Wrappers.Result = None
        out419_: Wrappers.Result
        out419_ = (d_1059_mpl_).CreateAwsKmsHierarchicalKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(d_1057_branchKeyId_), Wrappers.Option_None(), d_1067_keyStore_, d_1058_ttl_, Wrappers.Option_None()))
        d_1070_valueOrError4_ = out419_
        if not(not((d_1070_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(94,28): " + _dafny.string_of(d_1070_valueOrError4_))
        d_1069_hierarchyKeyring_ = (d_1070_valueOrError4_).Extract()
        d_1071_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out420_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out420_ = default__.GetTestMaterials(default__.TEST__ESDK__ALG__SUITE__ID)
        d_1071_materials_ = out420_
        default__.TestRoundtrip(d_1069_hierarchyKeyring_, d_1071_materials_, default__.TEST__ESDK__ALG__SUITE__ID, d_1057_branchKeyId_)
        d_1072_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1072_suite_ = AlgorithmSuites.default__.GetSuite(default__.TEST__ESDK__ALG__SUITE__ID)
        d_1073_zeroedKey_: _dafny.Seq
        d_1073_zeroedKey_ = _dafny.Seq([0 for d_1074___v0_ in range(AlgorithmSuites.default__.GetEncryptKeyLength(d_1072_suite_))])
        pat_let_tv2_ = d_1073_zeroedKey_
        def iife28_(_pat_let12_0):
            def iife29_(d_1075_dt__update__tmp_h0_):
                def iife30_(_pat_let13_0):
                    def iife31_(d_1076_dt__update_hplaintextDataKey_h0_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_1075_dt__update__tmp_h0_).algorithmSuite, (d_1075_dt__update__tmp_h0_).encryptionContext, (d_1075_dt__update__tmp_h0_).encryptedDataKeys, (d_1075_dt__update__tmp_h0_).requiredEncryptionContextKeys, d_1076_dt__update_hplaintextDataKey_h0_, (d_1075_dt__update__tmp_h0_).signingKey, (d_1075_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife31_(_pat_let13_0)
                return iife30_(Wrappers.Option_Some(pat_let_tv2_))
            return iife29_(_pat_let12_0)
        d_1071_materials_ = iife28_(d_1071_materials_)
        default__.TestRoundtrip(d_1069_hierarchyKeyring_, d_1071_materials_, default__.TEST__ESDK__ALG__SUITE__ID, d_1057_branchKeyId_)

    @staticmethod
    def TestHierarchyClientDBESuite():
        d_1077_branchKeyId_: _dafny.Seq
        d_1077_branchKeyId_ = default__.BRANCH__KEY__ID
        d_1078_ttl_: int
        d_1078_ttl_ = ((1) * (60000)) * (10)
        d_1079_mpl_: MaterialProviders.MaterialProvidersClient
        d_1080_valueOrError0_: Wrappers.Result = None
        out421_: Wrappers.Result
        out421_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1080_valueOrError0_ = out421_
        if not(not((d_1080_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(117,15): " + _dafny.string_of(d_1080_valueOrError0_))
        d_1079_mpl_ = (d_1080_valueOrError0_).Extract()
        d_1081_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1082_valueOrError1_: Wrappers.Result = None
        out422_: Wrappers.Result
        out422_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1082_valueOrError1_ = out422_
        if not(not((d_1082_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(119,21): " + _dafny.string_of(d_1082_valueOrError1_))
        d_1081_kmsClient_ = (d_1082_valueOrError1_).Extract()
        d_1083_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_1084_valueOrError2_: Wrappers.Result = None
        out423_: Wrappers.Result
        out423_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_1084_valueOrError2_ = out423_
        if not(not((d_1084_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(120,21): " + _dafny.string_of(d_1084_valueOrError2_))
        d_1083_ddbClient_ = (d_1084_valueOrError2_).Extract()
        d_1085_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_1085_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(default__.keyArn)
        d_1086_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_1086_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(default__.branchKeyStoreName, d_1085_kmsConfig_, default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_1083_ddbClient_), Wrappers.Option_Some(d_1081_kmsClient_))
        d_1087_keyStore_: KeyStore.KeyStoreClient
        d_1088_valueOrError3_: Wrappers.Result = None
        out424_: Wrappers.Result
        out424_ = KeyStore.default__.KeyStore(d_1086_keyStoreConfig_)
        d_1088_valueOrError3_ = out424_
        if not(not((d_1088_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(133,20): " + _dafny.string_of(d_1088_valueOrError3_))
        d_1087_keyStore_ = (d_1088_valueOrError3_).Extract()
        d_1089_hierarchyKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_1090_valueOrError4_: Wrappers.Result = None
        out425_: Wrappers.Result
        out425_ = (d_1079_mpl_).CreateAwsKmsHierarchicalKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(d_1077_branchKeyId_), Wrappers.Option_None(), d_1087_keyStore_, d_1078_ttl_, Wrappers.Option_None()))
        d_1090_valueOrError4_ = out425_
        if not(not((d_1090_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(135,28): " + _dafny.string_of(d_1090_valueOrError4_))
        d_1089_hierarchyKeyring_ = (d_1090_valueOrError4_).Extract()
        d_1091_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out426_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out426_ = default__.GetTestMaterials(default__.TEST__DBE__ALG__SUITE__ID)
        d_1091_materials_ = out426_
        default__.TestRoundtrip(d_1089_hierarchyKeyring_, d_1091_materials_, default__.TEST__DBE__ALG__SUITE__ID, d_1077_branchKeyId_)
        d_1092_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1092_suite_ = AlgorithmSuites.default__.GetSuite(default__.TEST__DBE__ALG__SUITE__ID)
        d_1093_zeroedKey_: _dafny.Seq
        d_1093_zeroedKey_ = _dafny.Seq([0 for d_1094___v1_ in range(AlgorithmSuites.default__.GetEncryptKeyLength(d_1092_suite_))])
        pat_let_tv3_ = d_1093_zeroedKey_
        def iife32_(_pat_let14_0):
            def iife33_(d_1095_dt__update__tmp_h0_):
                def iife34_(_pat_let15_0):
                    def iife35_(d_1096_dt__update_hplaintextDataKey_h0_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_1095_dt__update__tmp_h0_).algorithmSuite, (d_1095_dt__update__tmp_h0_).encryptionContext, (d_1095_dt__update__tmp_h0_).encryptedDataKeys, (d_1095_dt__update__tmp_h0_).requiredEncryptionContextKeys, d_1096_dt__update_hplaintextDataKey_h0_, (d_1095_dt__update__tmp_h0_).signingKey, (d_1095_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife35_(_pat_let15_0)
                return iife34_(Wrappers.Option_Some(pat_let_tv3_))
            return iife33_(_pat_let14_0)
        d_1091_materials_ = iife32_(d_1091_materials_)
        default__.TestRoundtrip(d_1089_hierarchyKeyring_, d_1091_materials_, default__.TEST__DBE__ALG__SUITE__ID, d_1077_branchKeyId_)

    @staticmethod
    def TestBranchKeyIdSupplier():
        d_1097_branchKeyIdSupplier_: AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplier
        nw6_ = DummyBranchKeyIdSupplier()
        nw6_.ctor__()
        d_1097_branchKeyIdSupplier_ = nw6_
        d_1098_ttl_: int
        d_1098_ttl_ = ((1) * (60000)) * (10)
        d_1099_mpl_: MaterialProviders.MaterialProvidersClient
        d_1100_valueOrError0_: Wrappers.Result = None
        out427_: Wrappers.Result
        out427_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1100_valueOrError0_ = out427_
        if not(not((d_1100_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(159,15): " + _dafny.string_of(d_1100_valueOrError0_))
        d_1099_mpl_ = (d_1100_valueOrError0_).Extract()
        d_1101_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1102_valueOrError1_: Wrappers.Result = None
        out428_: Wrappers.Result
        out428_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1102_valueOrError1_ = out428_
        if not(not((d_1102_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(161,21): " + _dafny.string_of(d_1102_valueOrError1_))
        d_1101_kmsClient_ = (d_1102_valueOrError1_).Extract()
        d_1103_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_1104_valueOrError2_: Wrappers.Result = None
        out429_: Wrappers.Result
        out429_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_1104_valueOrError2_ = out429_
        if not(not((d_1104_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(162,21): " + _dafny.string_of(d_1104_valueOrError2_))
        d_1103_ddbClient_ = (d_1104_valueOrError2_).Extract()
        d_1105_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_1105_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(default__.keyArn)
        d_1106_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_1106_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(default__.branchKeyStoreName, d_1105_kmsConfig_, default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_1103_ddbClient_), Wrappers.Option_Some(d_1101_kmsClient_))
        d_1107_keyStore_: KeyStore.KeyStoreClient
        d_1108_valueOrError3_: Wrappers.Result = None
        out430_: Wrappers.Result
        out430_ = KeyStore.default__.KeyStore(d_1106_keyStoreConfig_)
        d_1108_valueOrError3_ = out430_
        if not(not((d_1108_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(175,20): " + _dafny.string_of(d_1108_valueOrError3_))
        d_1107_keyStore_ = (d_1108_valueOrError3_).Extract()
        d_1109_hierarchyKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_1110_valueOrError4_: Wrappers.Result = None
        out431_: Wrappers.Result
        out431_ = (d_1099_mpl_).CreateAwsKmsHierarchicalKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_None(), Wrappers.Option_Some(d_1097_branchKeyIdSupplier_), d_1107_keyStore_, d_1098_ttl_, Wrappers.Option_None()))
        d_1110_valueOrError4_ = out431_
        if not(not((d_1110_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(177,28): " + _dafny.string_of(d_1110_valueOrError4_))
        d_1109_hierarchyKeyring_ = (d_1110_valueOrError4_).Extract()
        d_1111_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out432_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out432_ = default__.GetTestMaterials(default__.TEST__DBE__ALG__SUITE__ID)
        d_1111_materials_ = out432_
        d_1112_contextCaseA_: _dafny.Map
        d_1112_contextCaseA_ = ((d_1111_materials_).encryptionContext).set(default__.BRANCH__KEY, default__.CASE__A)
        pat_let_tv4_ = d_1112_contextCaseA_
        def iife36_(_pat_let16_0):
            def iife37_(d_1113_dt__update__tmp_h0_):
                def iife38_(_pat_let17_0):
                    def iife39_(d_1114_dt__update_hencryptionContext_h0_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_1113_dt__update__tmp_h0_).algorithmSuite, d_1114_dt__update_hencryptionContext_h0_, (d_1113_dt__update__tmp_h0_).encryptedDataKeys, (d_1113_dt__update__tmp_h0_).requiredEncryptionContextKeys, (d_1113_dt__update__tmp_h0_).plaintextDataKey, (d_1113_dt__update__tmp_h0_).signingKey, (d_1113_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife39_(_pat_let17_0)
                return iife38_(pat_let_tv4_)
            return iife37_(_pat_let16_0)
        d_1111_materials_ = iife36_(d_1111_materials_)
        default__.TestRoundtrip(d_1109_hierarchyKeyring_, d_1111_materials_, default__.TEST__DBE__ALG__SUITE__ID, default__.BRANCH__KEY__ID__A)
        d_1115_contextCaseB_: _dafny.Map
        d_1115_contextCaseB_ = ((d_1111_materials_).encryptionContext).set(default__.BRANCH__KEY, default__.CASE__B)
        pat_let_tv5_ = d_1115_contextCaseB_
        def iife40_(_pat_let18_0):
            def iife41_(d_1116_dt__update__tmp_h1_):
                def iife42_(_pat_let19_0):
                    def iife43_(d_1117_dt__update_hencryptionContext_h1_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_1116_dt__update__tmp_h1_).algorithmSuite, d_1117_dt__update_hencryptionContext_h1_, (d_1116_dt__update__tmp_h1_).encryptedDataKeys, (d_1116_dt__update__tmp_h1_).requiredEncryptionContextKeys, (d_1116_dt__update__tmp_h1_).plaintextDataKey, (d_1116_dt__update__tmp_h1_).signingKey, (d_1116_dt__update__tmp_h1_).symmetricSigningKeys)
                    return iife43_(_pat_let19_0)
                return iife42_(pat_let_tv5_)
            return iife41_(_pat_let18_0)
        d_1111_materials_ = iife40_(d_1111_materials_)
        default__.TestRoundtrip(d_1109_hierarchyKeyring_, d_1111_materials_, default__.TEST__DBE__ALG__SUITE__ID, default__.BRANCH__KEY__ID__B)

    @staticmethod
    def TestInvalidDataKeyError():
        d_1118_branchKeyIdSupplier_: AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplier
        nw7_ = DummyBranchKeyIdSupplier()
        nw7_.ctor__()
        d_1118_branchKeyIdSupplier_ = nw7_
        d_1119_ttl_: int
        d_1119_ttl_ = ((1) * (60000)) * (10)
        d_1120_mpl_: MaterialProviders.MaterialProvidersClient
        d_1121_valueOrError0_: Wrappers.Result = None
        out433_: Wrappers.Result
        out433_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1121_valueOrError0_ = out433_
        if not(not((d_1121_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(203,15): " + _dafny.string_of(d_1121_valueOrError0_))
        d_1120_mpl_ = (d_1121_valueOrError0_).Extract()
        d_1122_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1123_valueOrError1_: Wrappers.Result = None
        out434_: Wrappers.Result
        out434_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_1123_valueOrError1_ = out434_
        if not(not((d_1123_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(204,21): " + _dafny.string_of(d_1123_valueOrError1_))
        d_1122_kmsClient_ = (d_1123_valueOrError1_).Extract()
        d_1124_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_1125_valueOrError2_: Wrappers.Result = None
        out435_: Wrappers.Result
        out435_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_1125_valueOrError2_ = out435_
        if not(not((d_1125_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(205,21): " + _dafny.string_of(d_1125_valueOrError2_))
        d_1124_ddbClient_ = (d_1125_valueOrError2_).Extract()
        d_1126_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_1126_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(default__.keyArn)
        d_1127_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_1127_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(default__.branchKeyStoreName, d_1126_kmsConfig_, default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_1124_ddbClient_), Wrappers.Option_Some(d_1122_kmsClient_))
        d_1128_keyStore_: KeyStore.KeyStoreClient
        d_1129_valueOrError3_: Wrappers.Result = None
        out436_: Wrappers.Result
        out436_ = KeyStore.default__.KeyStore(d_1127_keyStoreConfig_)
        d_1129_valueOrError3_ = out436_
        if not(not((d_1129_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(216,20): " + _dafny.string_of(d_1129_valueOrError3_))
        d_1128_keyStore_ = (d_1129_valueOrError3_).Extract()
        d_1130_hierarchyKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_1131_valueOrError4_: Wrappers.Result = None
        out437_: Wrappers.Result
        out437_ = (d_1120_mpl_).CreateAwsKmsHierarchicalKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_None(), Wrappers.Option_Some(d_1118_branchKeyIdSupplier_), d_1128_keyStore_, d_1119_ttl_, Wrappers.Option_None()))
        d_1131_valueOrError4_ = out437_
        if not(not((d_1131_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(217,28): " + _dafny.string_of(d_1131_valueOrError4_))
        d_1130_hierarchyKeyring_ = (d_1131_valueOrError4_).Extract()
        d_1132_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out438_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out438_ = default__.GetTestMaterials(default__.TEST__DBE__ALG__SUITE__ID)
        d_1132_materials_ = out438_
        d_1133_contextCaseA_: _dafny.Map
        d_1133_contextCaseA_ = ((d_1132_materials_).encryptionContext).set(default__.BRANCH__KEY, default__.CASE__A)
        d_1134_contextCaseB_: _dafny.Map
        d_1134_contextCaseB_ = ((d_1132_materials_).encryptionContext).set(default__.BRANCH__KEY, default__.CASE__B)
        pat_let_tv6_ = d_1133_contextCaseA_
        d_1135_materialsA_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        def iife44_(_pat_let20_0):
            def iife45_(d_1136_dt__update__tmp_h0_):
                def iife46_(_pat_let21_0):
                    def iife47_(d_1137_dt__update_hencryptionContext_h0_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_1136_dt__update__tmp_h0_).algorithmSuite, d_1137_dt__update_hencryptionContext_h0_, (d_1136_dt__update__tmp_h0_).encryptedDataKeys, (d_1136_dt__update__tmp_h0_).requiredEncryptionContextKeys, (d_1136_dt__update__tmp_h0_).plaintextDataKey, (d_1136_dt__update__tmp_h0_).signingKey, (d_1136_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife47_(_pat_let21_0)
                return iife46_(pat_let_tv6_)
            return iife45_(_pat_let20_0)
        d_1135_materialsA_ = iife44_(d_1132_materials_)
        pat_let_tv7_ = d_1134_contextCaseB_
        d_1138_materialsB_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        def iife48_(_pat_let22_0):
            def iife49_(d_1139_dt__update__tmp_h1_):
                def iife50_(_pat_let23_0):
                    def iife51_(d_1140_dt__update_hencryptionContext_h1_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_1139_dt__update__tmp_h1_).algorithmSuite, d_1140_dt__update_hencryptionContext_h1_, (d_1139_dt__update__tmp_h1_).encryptedDataKeys, (d_1139_dt__update__tmp_h1_).requiredEncryptionContextKeys, (d_1139_dt__update__tmp_h1_).plaintextDataKey, (d_1139_dt__update__tmp_h1_).signingKey, (d_1139_dt__update__tmp_h1_).symmetricSigningKeys)
                    return iife51_(_pat_let23_0)
                return iife50_(pat_let_tv7_)
            return iife49_(_pat_let22_0)
        d_1138_materialsB_ = iife48_(d_1132_materials_)
        default__.TestInvalidDataKeyFailureCase(d_1130_hierarchyKeyring_, d_1135_materialsA_, d_1138_materialsB_, default__.TEST__DBE__ALG__SUITE__ID)

    @staticmethod
    def TestInvalidDataKeyFailureCase(hierarchyKeyring, encryptionMaterialsInEncrypt, encryptionMaterialsInDecrypt, algorithmSuiteId):
        d_1141_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_1142_valueOrError0_: Wrappers.Result = None
        out439_: Wrappers.Result
        out439_ = (hierarchyKeyring).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(encryptionMaterialsInEncrypt))
        d_1142_valueOrError0_ = out439_
        if not(not((d_1142_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(245,34): " + _dafny.string_of(d_1142_valueOrError0_))
        d_1141_encryptionMaterialsOut_ = (d_1142_valueOrError0_).Extract()
        d_1143_mpl_: MaterialProviders.MaterialProvidersClient
        d_1144_valueOrError1_: Wrappers.Result = None
        out440_: Wrappers.Result
        out440_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1144_valueOrError1_ = out440_
        if not(not((d_1144_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(249,15): " + _dafny.string_of(d_1144_valueOrError1_))
        d_1143_mpl_ = (d_1144_valueOrError1_).Extract()
        d_1145___v2_: tuple
        d_1146_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1146_valueOrError2_ = (d_1143_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1141_encryptionMaterialsOut_).materials)
        if not(not((d_1146_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(250,13): " + _dafny.string_of(d_1146_valueOrError2_))
        d_1145___v2_ = (d_1146_valueOrError2_).Extract()
        if not((len(((d_1141_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(252,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1147_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_1147_edk_ = (((d_1141_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1148_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1149_valueOrError3_: Wrappers.Result = None
        d_1149_valueOrError3_ = (d_1143_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(algorithmSuiteId, (encryptionMaterialsInDecrypt).encryptionContext, _dafny.Seq([])))
        if not(not((d_1149_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(256,33): " + _dafny.string_of(d_1149_valueOrError3_))
        d_1148_decryptionMaterialsIn_ = (d_1149_valueOrError3_).Extract()
        d_1150_decryptionMaterialsOut_: Wrappers.Result
        out441_: Wrappers.Result
        out441_ = (hierarchyKeyring).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_1148_decryptionMaterialsIn_, _dafny.Seq([d_1147_edk_])))
        d_1150_decryptionMaterialsOut_ = out441_
        if not((d_1150_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(269,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_1150_decryptionMaterialsOut_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(270,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1151_expectedErrorMessage_: _dafny.Seq
        d_1152_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1152_valueOrError4_ = ErrorMessages.default__.IncorrectDataKeys(_dafny.Seq([d_1147_edk_]), (d_1148_decryptionMaterialsIn_).algorithmSuite, _dafny.Seq(""))
        if not(not((d_1152_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(271,32): " + _dafny.string_of(d_1152_valueOrError4_))
        d_1151_expectedErrorMessage_ = (d_1152_valueOrError4_).Extract()
        if not((((d_1150_decryptionMaterialsOut_).error).message) == (d_1151_expectedErrorMessage_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(272,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRoundtrip(hierarchyKeyring, encryptionMaterialsIn, algorithmSuiteId, expectedBranchKeyId):
        d_1153_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_1154_valueOrError0_: Wrappers.Result = None
        out442_: Wrappers.Result
        out442_ = (hierarchyKeyring).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(encryptionMaterialsIn))
        d_1154_valueOrError0_ = out442_
        if not(not((d_1154_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(285,34): " + _dafny.string_of(d_1154_valueOrError0_))
        d_1153_encryptionMaterialsOut_ = (d_1154_valueOrError0_).Extract()
        d_1155_mpl_: MaterialProviders.MaterialProvidersClient
        d_1156_valueOrError1_: Wrappers.Result = None
        out443_: Wrappers.Result
        out443_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_1156_valueOrError1_ = out443_
        if not(not((d_1156_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(289,15): " + _dafny.string_of(d_1156_valueOrError1_))
        d_1155_mpl_ = (d_1156_valueOrError1_).Extract()
        d_1157___v3_: tuple
        d_1158_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_1158_valueOrError2_ = (d_1155_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_1153_encryptionMaterialsOut_).materials)
        if not(not((d_1158_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(290,13): " + _dafny.string_of(d_1158_valueOrError2_))
        d_1157___v3_ = (d_1158_valueOrError2_).Extract()
        if not((len(((d_1153_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(292,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1159_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_1159_edk_ = (((d_1153_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_1160_expectedBranchKeyIdUTF8_: _dafny.Seq
        d_1161_valueOrError3_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_1161_valueOrError3_ = UTF8.default__.Encode(expectedBranchKeyId)
        if not(not((d_1161_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(297,35): " + _dafny.string_of(d_1161_valueOrError3_))
        d_1160_expectedBranchKeyIdUTF8_ = (d_1161_valueOrError3_).Extract()
        if not(((d_1159_edk_).keyProviderInfo) == (d_1160_expectedBranchKeyIdUTF8_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(298,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1162_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1163_valueOrError4_: Wrappers.Result = None
        d_1163_valueOrError4_ = (d_1155_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(algorithmSuiteId, (encryptionMaterialsIn).encryptionContext, _dafny.Seq([])))
        if not(not((d_1163_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(300,33): " + _dafny.string_of(d_1163_valueOrError4_))
        d_1162_decryptionMaterialsIn_ = (d_1163_valueOrError4_).Extract()
        d_1164_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_1165_valueOrError5_: Wrappers.Result = None
        out444_: Wrappers.Result
        out444_ = (hierarchyKeyring).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_1162_decryptionMaterialsIn_, _dafny.Seq([d_1159_edk_])))
        d_1165_valueOrError5_ = out444_
        if not(not((d_1165_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(307,34): " + _dafny.string_of(d_1165_valueOrError5_))
        d_1164_decryptionMaterialsOut_ = (d_1165_valueOrError5_).Extract()
        if not((((d_1153_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_1164_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(319,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def branchKeyStoreName(instance):
        return Fixtures.default__.branchKeyStoreName
    @_dafny.classproperty
    def logicalKeyStoreName(instance):
        return default__.branchKeyStoreName
    @_dafny.classproperty
    def BRANCH__KEY__ID(instance):
        return Fixtures.default__.branchKeyId
    @_dafny.classproperty
    def BRANCH__KEY__ID__A(instance):
        return default__.BRANCH__KEY__ID
    @_dafny.classproperty
    def keyArn(instance):
        return Fixtures.default__.keyArn
    @_dafny.classproperty
    def TEST__ESDK__ALG__SUITE__ID(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
    @_dafny.classproperty
    def TEST__DBE__ALG__SUITE__ID(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_DBE(AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384())
    @_dafny.classproperty
    def BRANCH__KEY(instance):
        return UTF8.default__.EncodeAscii(_dafny.Seq("branchKey"))
    @_dafny.classproperty
    def CASE__A(instance):
        return UTF8.default__.EncodeAscii(_dafny.Seq("caseA"))
    @_dafny.classproperty
    def CASE__B(instance):
        return UTF8.default__.EncodeAscii(_dafny.Seq("caseB"))
    @_dafny.classproperty
    def BRANCH__KEY__ID__B(instance):
        return Fixtures.default__.branchKeyIdWithEC

class DummyBranchKeyIdSupplier(AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplier):
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "TestAwsKmsHierarchicalKeyring.DummyBranchKeyIdSupplier"
    def GetBranchKeyId(self, input):
        out445_: Wrappers.Result
        out445_ = AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplier.GetBranchKeyId(self, input)
        return out445_

    def ctor__(self):
        pass
        pass

    def GetBranchKeyId_k(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput.default())()
        d_1166_context_: _dafny.Map
        d_1166_context_ = (input).encryptionContext
        if ((default__.BRANCH__KEY) in ((d_1166_context_).keys)) and (((d_1166_context_)[default__.BRANCH__KEY]) == (default__.CASE__A)):
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput_GetBranchKeyIdOutput(default__.BRANCH__KEY__ID__A))
            return output
        elif ((default__.BRANCH__KEY) in ((d_1166_context_).keys)) and (((d_1166_context_)[default__.BRANCH__KEY]) == (default__.CASE__B)):
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput_GetBranchKeyIdOutput(default__.BRANCH__KEY__ID__B))
            return output
        elif True:
            output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Can't determine branchKeyId from context")))
            return output
        return output

