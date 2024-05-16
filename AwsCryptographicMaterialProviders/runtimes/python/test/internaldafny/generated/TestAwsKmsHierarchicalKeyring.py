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
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
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
import TestVersionKey as TestVersionKey
import TestUtils as TestUtils
import TestIntermediateKeyWrapping as TestIntermediateKeyWrapping
import TestDefaultClientProvider as TestDefaultClientProvider
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
        d_614_mpl_: MaterialProviders.MaterialProvidersClient
        d_615_valueOrError0_: Wrappers.Result = None
        out246_: Wrappers.Result
        out246_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_615_valueOrError0_ = out246_
        if not(not((d_615_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(52,15): " + _dafny.string_of(d_615_valueOrError0_))
        d_614_mpl_ = (d_615_valueOrError0_).Extract()
        d_616_encryptionContext_: _dafny.Map
        out247_: _dafny.Map
        out247_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_616_encryptionContext_ = out247_
        d_617_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_617_suite_ = AlgorithmSuites.default__.GetSuite(suiteId)
        d_618_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_619_valueOrError1_: Wrappers.Result = None
        d_619_valueOrError1_ = (d_614_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(suiteId, d_616_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_619_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(57,33): " + _dafny.string_of(d_619_valueOrError1_))
        d_618_encryptionMaterialsIn_ = (d_619_valueOrError1_).Extract()
        out = d_618_encryptionMaterialsIn_
        return out
        return out

    @staticmethod
    def TestHierarchyClientESDKSuite():
        d_620_branchKeyId_: _dafny.Seq
        d_620_branchKeyId_ = default__.BRANCH__KEY__ID
        d_621_ttl_: int
        d_621_ttl_ = ((1) * (60000)) * (10)
        d_622_mpl_: MaterialProviders.MaterialProvidersClient
        d_623_valueOrError0_: Wrappers.Result = None
        out248_: Wrappers.Result
        out248_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_623_valueOrError0_ = out248_
        if not(not((d_623_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(74,15): " + _dafny.string_of(d_623_valueOrError0_))
        d_622_mpl_ = (d_623_valueOrError0_).Extract()
        d_624_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_625_valueOrError1_: Wrappers.Result = None
        out249_: Wrappers.Result
        out249_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_625_valueOrError1_ = out249_
        if not(not((d_625_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(76,21): " + _dafny.string_of(d_625_valueOrError1_))
        d_624_kmsClient_ = (d_625_valueOrError1_).Extract()
        d_626_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_627_valueOrError2_: Wrappers.Result = None
        out250_: Wrappers.Result
        out250_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_627_valueOrError2_ = out250_
        if not(not((d_627_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(77,21): " + _dafny.string_of(d_627_valueOrError2_))
        d_626_ddbClient_ = (d_627_valueOrError2_).Extract()
        d_628_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_628_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(default__.keyArn)
        d_629_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_629_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(default__.branchKeyStoreName, d_628_kmsConfig_, default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_626_ddbClient_), Wrappers.Option_Some(d_624_kmsClient_))
        d_630_keyStore_: KeyStore.KeyStoreClient
        d_631_valueOrError3_: Wrappers.Result = None
        out251_: Wrappers.Result
        out251_ = KeyStore.default__.KeyStore(d_629_keyStoreConfig_)
        d_631_valueOrError3_ = out251_
        if not(not((d_631_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(90,20): " + _dafny.string_of(d_631_valueOrError3_))
        d_630_keyStore_ = (d_631_valueOrError3_).Extract()
        d_632_hierarchyKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_633_valueOrError4_: Wrappers.Result = None
        out252_: Wrappers.Result
        out252_ = (d_622_mpl_).CreateAwsKmsHierarchicalKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(d_620_branchKeyId_), Wrappers.Option_None(), d_630_keyStore_, d_621_ttl_, Wrappers.Option_None()))
        d_633_valueOrError4_ = out252_
        if not(not((d_633_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(92,28): " + _dafny.string_of(d_633_valueOrError4_))
        d_632_hierarchyKeyring_ = (d_633_valueOrError4_).Extract()
        d_634_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out253_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out253_ = default__.GetTestMaterials(default__.TEST__ESDK__ALG__SUITE__ID)
        d_634_materials_ = out253_
        default__.TestRoundtrip(d_632_hierarchyKeyring_, d_634_materials_, default__.TEST__ESDK__ALG__SUITE__ID, d_620_branchKeyId_)
        d_635_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_635_suite_ = AlgorithmSuites.default__.GetSuite(default__.TEST__ESDK__ALG__SUITE__ID)
        d_636_zeroedKey_: _dafny.Seq
        d_636_zeroedKey_ = _dafny.Seq([0 for d_637___v0_ in range(AlgorithmSuites.default__.GetEncryptKeyLength(d_635_suite_))])
        pat_let_tv1_ = d_636_zeroedKey_
        def iife8_(_pat_let3_0):
            def iife9_(d_638_dt__update__tmp_h0_):
                def iife10_(_pat_let4_0):
                    def iife11_(d_639_dt__update_hplaintextDataKey_h0_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_638_dt__update__tmp_h0_).algorithmSuite, (d_638_dt__update__tmp_h0_).encryptionContext, (d_638_dt__update__tmp_h0_).encryptedDataKeys, (d_638_dt__update__tmp_h0_).requiredEncryptionContextKeys, d_639_dt__update_hplaintextDataKey_h0_, (d_638_dt__update__tmp_h0_).signingKey, (d_638_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife11_(_pat_let4_0)
                return iife10_(Wrappers.Option_Some(pat_let_tv1_))
            return iife9_(_pat_let3_0)
        d_634_materials_ = iife8_(d_634_materials_)
        default__.TestRoundtrip(d_632_hierarchyKeyring_, d_634_materials_, default__.TEST__ESDK__ALG__SUITE__ID, d_620_branchKeyId_)

    @staticmethod
    def TestHierarchyClientDBESuite():
        d_640_branchKeyId_: _dafny.Seq
        d_640_branchKeyId_ = default__.BRANCH__KEY__ID
        d_641_ttl_: int
        d_641_ttl_ = ((1) * (60000)) * (10)
        d_642_mpl_: MaterialProviders.MaterialProvidersClient
        d_643_valueOrError0_: Wrappers.Result = None
        out254_: Wrappers.Result
        out254_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_643_valueOrError0_ = out254_
        if not(not((d_643_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(115,15): " + _dafny.string_of(d_643_valueOrError0_))
        d_642_mpl_ = (d_643_valueOrError0_).Extract()
        d_644_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_645_valueOrError1_: Wrappers.Result = None
        out255_: Wrappers.Result
        out255_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_645_valueOrError1_ = out255_
        if not(not((d_645_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(117,21): " + _dafny.string_of(d_645_valueOrError1_))
        d_644_kmsClient_ = (d_645_valueOrError1_).Extract()
        d_646_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_647_valueOrError2_: Wrappers.Result = None
        out256_: Wrappers.Result
        out256_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_647_valueOrError2_ = out256_
        if not(not((d_647_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(118,21): " + _dafny.string_of(d_647_valueOrError2_))
        d_646_ddbClient_ = (d_647_valueOrError2_).Extract()
        d_648_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_648_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(default__.keyArn)
        d_649_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_649_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(default__.branchKeyStoreName, d_648_kmsConfig_, default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_646_ddbClient_), Wrappers.Option_Some(d_644_kmsClient_))
        d_650_keyStore_: KeyStore.KeyStoreClient
        d_651_valueOrError3_: Wrappers.Result = None
        out257_: Wrappers.Result
        out257_ = KeyStore.default__.KeyStore(d_649_keyStoreConfig_)
        d_651_valueOrError3_ = out257_
        if not(not((d_651_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(131,20): " + _dafny.string_of(d_651_valueOrError3_))
        d_650_keyStore_ = (d_651_valueOrError3_).Extract()
        d_652_hierarchyKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_653_valueOrError4_: Wrappers.Result = None
        out258_: Wrappers.Result
        out258_ = (d_642_mpl_).CreateAwsKmsHierarchicalKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(d_640_branchKeyId_), Wrappers.Option_None(), d_650_keyStore_, d_641_ttl_, Wrappers.Option_None()))
        d_653_valueOrError4_ = out258_
        if not(not((d_653_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(133,28): " + _dafny.string_of(d_653_valueOrError4_))
        d_652_hierarchyKeyring_ = (d_653_valueOrError4_).Extract()
        d_654_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out259_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out259_ = default__.GetTestMaterials(default__.TEST__DBE__ALG__SUITE__ID)
        d_654_materials_ = out259_
        default__.TestRoundtrip(d_652_hierarchyKeyring_, d_654_materials_, default__.TEST__DBE__ALG__SUITE__ID, d_640_branchKeyId_)
        d_655_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_655_suite_ = AlgorithmSuites.default__.GetSuite(default__.TEST__DBE__ALG__SUITE__ID)
        d_656_zeroedKey_: _dafny.Seq
        d_656_zeroedKey_ = _dafny.Seq([0 for d_657___v1_ in range(AlgorithmSuites.default__.GetEncryptKeyLength(d_655_suite_))])
        pat_let_tv2_ = d_656_zeroedKey_
        def iife12_(_pat_let5_0):
            def iife13_(d_658_dt__update__tmp_h0_):
                def iife14_(_pat_let6_0):
                    def iife15_(d_659_dt__update_hplaintextDataKey_h0_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_658_dt__update__tmp_h0_).algorithmSuite, (d_658_dt__update__tmp_h0_).encryptionContext, (d_658_dt__update__tmp_h0_).encryptedDataKeys, (d_658_dt__update__tmp_h0_).requiredEncryptionContextKeys, d_659_dt__update_hplaintextDataKey_h0_, (d_658_dt__update__tmp_h0_).signingKey, (d_658_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife15_(_pat_let6_0)
                return iife14_(Wrappers.Option_Some(pat_let_tv2_))
            return iife13_(_pat_let5_0)
        d_654_materials_ = iife12_(d_654_materials_)
        default__.TestRoundtrip(d_652_hierarchyKeyring_, d_654_materials_, default__.TEST__DBE__ALG__SUITE__ID, d_640_branchKeyId_)

    @staticmethod
    def TestBranchKeyIdSupplier():
        d_660_branchKeyIdSupplier_: AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplier
        nw6_ = DummyBranchKeyIdSupplier()
        nw6_.ctor__()
        d_660_branchKeyIdSupplier_ = nw6_
        d_661_ttl_: int
        d_661_ttl_ = ((1) * (60000)) * (10)
        d_662_mpl_: MaterialProviders.MaterialProvidersClient
        d_663_valueOrError0_: Wrappers.Result = None
        out260_: Wrappers.Result
        out260_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_663_valueOrError0_ = out260_
        if not(not((d_663_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(157,15): " + _dafny.string_of(d_663_valueOrError0_))
        d_662_mpl_ = (d_663_valueOrError0_).Extract()
        d_664_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_665_valueOrError1_: Wrappers.Result = None
        out261_: Wrappers.Result
        out261_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_665_valueOrError1_ = out261_
        if not(not((d_665_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(159,21): " + _dafny.string_of(d_665_valueOrError1_))
        d_664_kmsClient_ = (d_665_valueOrError1_).Extract()
        d_666_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_667_valueOrError2_: Wrappers.Result = None
        out262_: Wrappers.Result
        out262_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_667_valueOrError2_ = out262_
        if not(not((d_667_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(160,21): " + _dafny.string_of(d_667_valueOrError2_))
        d_666_ddbClient_ = (d_667_valueOrError2_).Extract()
        d_668_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_668_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(default__.keyArn)
        d_669_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_669_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(default__.branchKeyStoreName, d_668_kmsConfig_, default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_666_ddbClient_), Wrappers.Option_Some(d_664_kmsClient_))
        d_670_keyStore_: KeyStore.KeyStoreClient
        d_671_valueOrError3_: Wrappers.Result = None
        out263_: Wrappers.Result
        out263_ = KeyStore.default__.KeyStore(d_669_keyStoreConfig_)
        d_671_valueOrError3_ = out263_
        if not(not((d_671_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(173,20): " + _dafny.string_of(d_671_valueOrError3_))
        d_670_keyStore_ = (d_671_valueOrError3_).Extract()
        d_672_hierarchyKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_673_valueOrError4_: Wrappers.Result = None
        out264_: Wrappers.Result
        out264_ = (d_662_mpl_).CreateAwsKmsHierarchicalKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_None(), Wrappers.Option_Some(d_660_branchKeyIdSupplier_), d_670_keyStore_, d_661_ttl_, Wrappers.Option_None()))
        d_673_valueOrError4_ = out264_
        if not(not((d_673_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(175,28): " + _dafny.string_of(d_673_valueOrError4_))
        d_672_hierarchyKeyring_ = (d_673_valueOrError4_).Extract()
        d_674_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out265_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out265_ = default__.GetTestMaterials(default__.TEST__DBE__ALG__SUITE__ID)
        d_674_materials_ = out265_
        d_675_contextCaseA_: _dafny.Map
        d_675_contextCaseA_ = ((d_674_materials_).encryptionContext).set(default__.BRANCH__KEY, default__.CASE__A)
        pat_let_tv3_ = d_675_contextCaseA_
        def iife16_(_pat_let7_0):
            def iife17_(d_676_dt__update__tmp_h0_):
                def iife18_(_pat_let8_0):
                    def iife19_(d_677_dt__update_hencryptionContext_h0_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_676_dt__update__tmp_h0_).algorithmSuite, d_677_dt__update_hencryptionContext_h0_, (d_676_dt__update__tmp_h0_).encryptedDataKeys, (d_676_dt__update__tmp_h0_).requiredEncryptionContextKeys, (d_676_dt__update__tmp_h0_).plaintextDataKey, (d_676_dt__update__tmp_h0_).signingKey, (d_676_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife19_(_pat_let8_0)
                return iife18_(pat_let_tv3_)
            return iife17_(_pat_let7_0)
        d_674_materials_ = iife16_(d_674_materials_)
        default__.TestRoundtrip(d_672_hierarchyKeyring_, d_674_materials_, default__.TEST__DBE__ALG__SUITE__ID, default__.BRANCH__KEY__ID__A)
        d_678_contextCaseB_: _dafny.Map
        d_678_contextCaseB_ = ((d_674_materials_).encryptionContext).set(default__.BRANCH__KEY, default__.CASE__B)
        pat_let_tv4_ = d_678_contextCaseB_
        def iife20_(_pat_let9_0):
            def iife21_(d_679_dt__update__tmp_h1_):
                def iife22_(_pat_let10_0):
                    def iife23_(d_680_dt__update_hencryptionContext_h1_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_679_dt__update__tmp_h1_).algorithmSuite, d_680_dt__update_hencryptionContext_h1_, (d_679_dt__update__tmp_h1_).encryptedDataKeys, (d_679_dt__update__tmp_h1_).requiredEncryptionContextKeys, (d_679_dt__update__tmp_h1_).plaintextDataKey, (d_679_dt__update__tmp_h1_).signingKey, (d_679_dt__update__tmp_h1_).symmetricSigningKeys)
                    return iife23_(_pat_let10_0)
                return iife22_(pat_let_tv4_)
            return iife21_(_pat_let9_0)
        d_674_materials_ = iife20_(d_674_materials_)
        default__.TestRoundtrip(d_672_hierarchyKeyring_, d_674_materials_, default__.TEST__DBE__ALG__SUITE__ID, default__.BRANCH__KEY__ID__B)

    @staticmethod
    def TestRoundtrip(hierarchyKeyring, encryptionMaterialsIn, algorithmSuiteId, expectedBranchKeyId):
        d_681_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_682_valueOrError0_: Wrappers.Result = None
        out266_: Wrappers.Result
        out266_ = (hierarchyKeyring).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(encryptionMaterialsIn))
        d_682_valueOrError0_ = out266_
        if not(not((d_682_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(207,34): " + _dafny.string_of(d_682_valueOrError0_))
        d_681_encryptionMaterialsOut_ = (d_682_valueOrError0_).Extract()
        d_683_mpl_: MaterialProviders.MaterialProvidersClient
        d_684_valueOrError1_: Wrappers.Result = None
        out267_: Wrappers.Result
        out267_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_684_valueOrError1_ = out267_
        if not(not((d_684_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(211,15): " + _dafny.string_of(d_684_valueOrError1_))
        d_683_mpl_ = (d_684_valueOrError1_).Extract()
        d_685___v2_: tuple
        d_686_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_686_valueOrError2_ = (d_683_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_681_encryptionMaterialsOut_).materials)
        if not(not((d_686_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(212,13): " + _dafny.string_of(d_686_valueOrError2_))
        d_685___v2_ = (d_686_valueOrError2_).Extract()
        if not((len(((d_681_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(214,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_687_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_687_edk_ = (((d_681_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_688_expectedBranchKeyIdUTF8_: _dafny.Seq
        d_689_valueOrError3_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_689_valueOrError3_ = UTF8.default__.Encode(expectedBranchKeyId)
        if not(not((d_689_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(219,35): " + _dafny.string_of(d_689_valueOrError3_))
        d_688_expectedBranchKeyIdUTF8_ = (d_689_valueOrError3_).Extract()
        if not(((d_687_edk_).keyProviderInfo) == (d_688_expectedBranchKeyIdUTF8_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(220,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_690_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_691_valueOrError4_: Wrappers.Result = None
        d_691_valueOrError4_ = (d_683_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(algorithmSuiteId, (encryptionMaterialsIn).encryptionContext, _dafny.Seq([])))
        if not(not((d_691_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(222,33): " + _dafny.string_of(d_691_valueOrError4_))
        d_690_decryptionMaterialsIn_ = (d_691_valueOrError4_).Extract()
        d_692_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_693_valueOrError5_: Wrappers.Result = None
        out268_: Wrappers.Result
        out268_ = (hierarchyKeyring).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_690_decryptionMaterialsIn_, _dafny.Seq([d_687_edk_])))
        d_693_valueOrError5_ = out268_
        if not(not((d_693_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(229,34): " + _dafny.string_of(d_693_valueOrError5_))
        d_692_decryptionMaterialsOut_ = (d_693_valueOrError5_).Extract()
        if not((((d_681_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_692_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(241,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

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
        out269_: Wrappers.Result
        out269_ = AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplier.GetBranchKeyId(self, input)
        return out269_

    def ctor__(self):
        pass
        pass

    def GetBranchKeyId_k(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput.default())()
        d_694_context_: _dafny.Map
        d_694_context_ = (input).encryptionContext
        if ((default__.BRANCH__KEY) in ((d_694_context_).keys)) and (((d_694_context_)[default__.BRANCH__KEY]) == (default__.CASE__A)):
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput_GetBranchKeyIdOutput(default__.BRANCH__KEY__ID__A))
            return output
        elif ((default__.BRANCH__KEY) in ((d_694_context_).keys)) and (((d_694_context_)[default__.BRANCH__KEY]) == (default__.CASE__B)):
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput_GetBranchKeyIdOutput(default__.BRANCH__KEY__ID__B))
            return output
        elif True:
            output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Can't determine branchKeyId from context")))
            return output
        return output

