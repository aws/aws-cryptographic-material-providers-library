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
import TestVersionKey as TestVersionKey
import TestUtils as TestUtils
import TestIntermediateKeyWrapping as TestIntermediateKeyWrapping
import TestErrorMessages as TestErrorMessages
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
        d_810_mpl_: MaterialProviders.MaterialProvidersClient
        d_811_valueOrError0_: Wrappers.Result = None
        out314_: Wrappers.Result
        out314_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_811_valueOrError0_ = out314_
        if not(not((d_811_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(54,15): " + _dafny.string_of(d_811_valueOrError0_))
        d_810_mpl_ = (d_811_valueOrError0_).Extract()
        d_812_encryptionContext_: _dafny.Map
        out315_: _dafny.Map
        out315_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_812_encryptionContext_ = out315_
        d_813_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_813_suite_ = AlgorithmSuites.default__.GetSuite(suiteId)
        d_814_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_815_valueOrError1_: Wrappers.Result = None
        d_815_valueOrError1_ = (d_810_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(suiteId, d_812_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_815_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(59,33): " + _dafny.string_of(d_815_valueOrError1_))
        d_814_encryptionMaterialsIn_ = (d_815_valueOrError1_).Extract()
        out = d_814_encryptionMaterialsIn_
        return out
        return out

    @staticmethod
    def TestHierarchyClientESDKSuite():
        d_816_branchKeyId_: _dafny.Seq
        d_816_branchKeyId_ = default__.BRANCH__KEY__ID
        d_817_ttl_: int
        d_817_ttl_ = ((1) * (60000)) * (10)
        d_818_mpl_: MaterialProviders.MaterialProvidersClient
        d_819_valueOrError0_: Wrappers.Result = None
        out316_: Wrappers.Result
        out316_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_819_valueOrError0_ = out316_
        if not(not((d_819_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(76,15): " + _dafny.string_of(d_819_valueOrError0_))
        d_818_mpl_ = (d_819_valueOrError0_).Extract()
        d_820_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_821_valueOrError1_: Wrappers.Result = None
        out317_: Wrappers.Result
        out317_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_821_valueOrError1_ = out317_
        if not(not((d_821_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(78,21): " + _dafny.string_of(d_821_valueOrError1_))
        d_820_kmsClient_ = (d_821_valueOrError1_).Extract()
        d_822_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_823_valueOrError2_: Wrappers.Result = None
        out318_: Wrappers.Result
        out318_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_823_valueOrError2_ = out318_
        if not(not((d_823_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(79,21): " + _dafny.string_of(d_823_valueOrError2_))
        d_822_ddbClient_ = (d_823_valueOrError2_).Extract()
        d_824_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_824_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(default__.keyArn)
        d_825_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_825_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(default__.branchKeyStoreName, d_824_kmsConfig_, default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_822_ddbClient_), Wrappers.Option_Some(d_820_kmsClient_))
        d_826_keyStore_: KeyStore.KeyStoreClient
        d_827_valueOrError3_: Wrappers.Result = None
        out319_: Wrappers.Result
        out319_ = KeyStore.default__.KeyStore(d_825_keyStoreConfig_)
        d_827_valueOrError3_ = out319_
        if not(not((d_827_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(92,20): " + _dafny.string_of(d_827_valueOrError3_))
        d_826_keyStore_ = (d_827_valueOrError3_).Extract()
        d_828_hierarchyKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_829_valueOrError4_: Wrappers.Result = None
        out320_: Wrappers.Result
        out320_ = (d_818_mpl_).CreateAwsKmsHierarchicalKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(d_816_branchKeyId_), Wrappers.Option_None(), d_826_keyStore_, d_817_ttl_, Wrappers.Option_None()))
        d_829_valueOrError4_ = out320_
        if not(not((d_829_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(94,28): " + _dafny.string_of(d_829_valueOrError4_))
        d_828_hierarchyKeyring_ = (d_829_valueOrError4_).Extract()
        d_830_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out321_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out321_ = default__.GetTestMaterials(default__.TEST__ESDK__ALG__SUITE__ID)
        d_830_materials_ = out321_
        default__.TestRoundtrip(d_828_hierarchyKeyring_, d_830_materials_, default__.TEST__ESDK__ALG__SUITE__ID, d_816_branchKeyId_)
        d_831_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_831_suite_ = AlgorithmSuites.default__.GetSuite(default__.TEST__ESDK__ALG__SUITE__ID)
        d_832_zeroedKey_: _dafny.Seq
        d_832_zeroedKey_ = _dafny.Seq([0 for d_833___v0_ in range(AlgorithmSuites.default__.GetEncryptKeyLength(d_831_suite_))])
        pat_let_tv2_ = d_832_zeroedKey_
        def iife16_(_pat_let6_0):
            def iife17_(d_834_dt__update__tmp_h0_):
                def iife18_(_pat_let7_0):
                    def iife19_(d_835_dt__update_hplaintextDataKey_h0_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_834_dt__update__tmp_h0_).algorithmSuite, (d_834_dt__update__tmp_h0_).encryptionContext, (d_834_dt__update__tmp_h0_).encryptedDataKeys, (d_834_dt__update__tmp_h0_).requiredEncryptionContextKeys, d_835_dt__update_hplaintextDataKey_h0_, (d_834_dt__update__tmp_h0_).signingKey, (d_834_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife19_(_pat_let7_0)
                return iife18_(Wrappers.Option_Some(pat_let_tv2_))
            return iife17_(_pat_let6_0)
        d_830_materials_ = iife16_(d_830_materials_)
        default__.TestRoundtrip(d_828_hierarchyKeyring_, d_830_materials_, default__.TEST__ESDK__ALG__SUITE__ID, d_816_branchKeyId_)

    @staticmethod
    def TestHierarchyClientDBESuite():
        d_836_branchKeyId_: _dafny.Seq
        d_836_branchKeyId_ = default__.BRANCH__KEY__ID
        d_837_ttl_: int
        d_837_ttl_ = ((1) * (60000)) * (10)
        d_838_mpl_: MaterialProviders.MaterialProvidersClient
        d_839_valueOrError0_: Wrappers.Result = None
        out322_: Wrappers.Result
        out322_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_839_valueOrError0_ = out322_
        if not(not((d_839_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(117,15): " + _dafny.string_of(d_839_valueOrError0_))
        d_838_mpl_ = (d_839_valueOrError0_).Extract()
        d_840_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_841_valueOrError1_: Wrappers.Result = None
        out323_: Wrappers.Result
        out323_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_841_valueOrError1_ = out323_
        if not(not((d_841_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(119,21): " + _dafny.string_of(d_841_valueOrError1_))
        d_840_kmsClient_ = (d_841_valueOrError1_).Extract()
        d_842_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_843_valueOrError2_: Wrappers.Result = None
        out324_: Wrappers.Result
        out324_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_843_valueOrError2_ = out324_
        if not(not((d_843_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(120,21): " + _dafny.string_of(d_843_valueOrError2_))
        d_842_ddbClient_ = (d_843_valueOrError2_).Extract()
        d_844_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_844_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(default__.keyArn)
        d_845_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_845_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(default__.branchKeyStoreName, d_844_kmsConfig_, default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_842_ddbClient_), Wrappers.Option_Some(d_840_kmsClient_))
        d_846_keyStore_: KeyStore.KeyStoreClient
        d_847_valueOrError3_: Wrappers.Result = None
        out325_: Wrappers.Result
        out325_ = KeyStore.default__.KeyStore(d_845_keyStoreConfig_)
        d_847_valueOrError3_ = out325_
        if not(not((d_847_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(133,20): " + _dafny.string_of(d_847_valueOrError3_))
        d_846_keyStore_ = (d_847_valueOrError3_).Extract()
        d_848_hierarchyKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_849_valueOrError4_: Wrappers.Result = None
        out326_: Wrappers.Result
        out326_ = (d_838_mpl_).CreateAwsKmsHierarchicalKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(d_836_branchKeyId_), Wrappers.Option_None(), d_846_keyStore_, d_837_ttl_, Wrappers.Option_None()))
        d_849_valueOrError4_ = out326_
        if not(not((d_849_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(135,28): " + _dafny.string_of(d_849_valueOrError4_))
        d_848_hierarchyKeyring_ = (d_849_valueOrError4_).Extract()
        d_850_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out327_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out327_ = default__.GetTestMaterials(default__.TEST__DBE__ALG__SUITE__ID)
        d_850_materials_ = out327_
        default__.TestRoundtrip(d_848_hierarchyKeyring_, d_850_materials_, default__.TEST__DBE__ALG__SUITE__ID, d_836_branchKeyId_)
        d_851_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_851_suite_ = AlgorithmSuites.default__.GetSuite(default__.TEST__DBE__ALG__SUITE__ID)
        d_852_zeroedKey_: _dafny.Seq
        d_852_zeroedKey_ = _dafny.Seq([0 for d_853___v1_ in range(AlgorithmSuites.default__.GetEncryptKeyLength(d_851_suite_))])
        pat_let_tv3_ = d_852_zeroedKey_
        def iife20_(_pat_let8_0):
            def iife21_(d_854_dt__update__tmp_h0_):
                def iife22_(_pat_let9_0):
                    def iife23_(d_855_dt__update_hplaintextDataKey_h0_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_854_dt__update__tmp_h0_).algorithmSuite, (d_854_dt__update__tmp_h0_).encryptionContext, (d_854_dt__update__tmp_h0_).encryptedDataKeys, (d_854_dt__update__tmp_h0_).requiredEncryptionContextKeys, d_855_dt__update_hplaintextDataKey_h0_, (d_854_dt__update__tmp_h0_).signingKey, (d_854_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife23_(_pat_let9_0)
                return iife22_(Wrappers.Option_Some(pat_let_tv3_))
            return iife21_(_pat_let8_0)
        d_850_materials_ = iife20_(d_850_materials_)
        default__.TestRoundtrip(d_848_hierarchyKeyring_, d_850_materials_, default__.TEST__DBE__ALG__SUITE__ID, d_836_branchKeyId_)

    @staticmethod
    def TestBranchKeyIdSupplier():
        d_856_branchKeyIdSupplier_: AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplier
        nw6_ = DummyBranchKeyIdSupplier()
        nw6_.ctor__()
        d_856_branchKeyIdSupplier_ = nw6_
        d_857_ttl_: int
        d_857_ttl_ = ((1) * (60000)) * (10)
        d_858_mpl_: MaterialProviders.MaterialProvidersClient
        d_859_valueOrError0_: Wrappers.Result = None
        out328_: Wrappers.Result
        out328_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_859_valueOrError0_ = out328_
        if not(not((d_859_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(159,15): " + _dafny.string_of(d_859_valueOrError0_))
        d_858_mpl_ = (d_859_valueOrError0_).Extract()
        d_860_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_861_valueOrError1_: Wrappers.Result = None
        out329_: Wrappers.Result
        out329_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_861_valueOrError1_ = out329_
        if not(not((d_861_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(161,21): " + _dafny.string_of(d_861_valueOrError1_))
        d_860_kmsClient_ = (d_861_valueOrError1_).Extract()
        d_862_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_863_valueOrError2_: Wrappers.Result = None
        out330_: Wrappers.Result
        out330_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_863_valueOrError2_ = out330_
        if not(not((d_863_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(162,21): " + _dafny.string_of(d_863_valueOrError2_))
        d_862_ddbClient_ = (d_863_valueOrError2_).Extract()
        d_864_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_864_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(default__.keyArn)
        d_865_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_865_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(default__.branchKeyStoreName, d_864_kmsConfig_, default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_862_ddbClient_), Wrappers.Option_Some(d_860_kmsClient_))
        d_866_keyStore_: KeyStore.KeyStoreClient
        d_867_valueOrError3_: Wrappers.Result = None
        out331_: Wrappers.Result
        out331_ = KeyStore.default__.KeyStore(d_865_keyStoreConfig_)
        d_867_valueOrError3_ = out331_
        if not(not((d_867_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(175,20): " + _dafny.string_of(d_867_valueOrError3_))
        d_866_keyStore_ = (d_867_valueOrError3_).Extract()
        d_868_hierarchyKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_869_valueOrError4_: Wrappers.Result = None
        out332_: Wrappers.Result
        out332_ = (d_858_mpl_).CreateAwsKmsHierarchicalKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_None(), Wrappers.Option_Some(d_856_branchKeyIdSupplier_), d_866_keyStore_, d_857_ttl_, Wrappers.Option_None()))
        d_869_valueOrError4_ = out332_
        if not(not((d_869_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(177,28): " + _dafny.string_of(d_869_valueOrError4_))
        d_868_hierarchyKeyring_ = (d_869_valueOrError4_).Extract()
        d_870_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out333_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out333_ = default__.GetTestMaterials(default__.TEST__DBE__ALG__SUITE__ID)
        d_870_materials_ = out333_
        d_871_contextCaseA_: _dafny.Map
        d_871_contextCaseA_ = ((d_870_materials_).encryptionContext).set(default__.BRANCH__KEY, default__.CASE__A)
        pat_let_tv4_ = d_871_contextCaseA_
        def iife24_(_pat_let10_0):
            def iife25_(d_872_dt__update__tmp_h0_):
                def iife26_(_pat_let11_0):
                    def iife27_(d_873_dt__update_hencryptionContext_h0_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_872_dt__update__tmp_h0_).algorithmSuite, d_873_dt__update_hencryptionContext_h0_, (d_872_dt__update__tmp_h0_).encryptedDataKeys, (d_872_dt__update__tmp_h0_).requiredEncryptionContextKeys, (d_872_dt__update__tmp_h0_).plaintextDataKey, (d_872_dt__update__tmp_h0_).signingKey, (d_872_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife27_(_pat_let11_0)
                return iife26_(pat_let_tv4_)
            return iife25_(_pat_let10_0)
        d_870_materials_ = iife24_(d_870_materials_)
        default__.TestRoundtrip(d_868_hierarchyKeyring_, d_870_materials_, default__.TEST__DBE__ALG__SUITE__ID, default__.BRANCH__KEY__ID__A)
        d_874_contextCaseB_: _dafny.Map
        d_874_contextCaseB_ = ((d_870_materials_).encryptionContext).set(default__.BRANCH__KEY, default__.CASE__B)
        pat_let_tv5_ = d_874_contextCaseB_
        def iife28_(_pat_let12_0):
            def iife29_(d_875_dt__update__tmp_h1_):
                def iife30_(_pat_let13_0):
                    def iife31_(d_876_dt__update_hencryptionContext_h1_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_875_dt__update__tmp_h1_).algorithmSuite, d_876_dt__update_hencryptionContext_h1_, (d_875_dt__update__tmp_h1_).encryptedDataKeys, (d_875_dt__update__tmp_h1_).requiredEncryptionContextKeys, (d_875_dt__update__tmp_h1_).plaintextDataKey, (d_875_dt__update__tmp_h1_).signingKey, (d_875_dt__update__tmp_h1_).symmetricSigningKeys)
                    return iife31_(_pat_let13_0)
                return iife30_(pat_let_tv5_)
            return iife29_(_pat_let12_0)
        d_870_materials_ = iife28_(d_870_materials_)
        default__.TestRoundtrip(d_868_hierarchyKeyring_, d_870_materials_, default__.TEST__DBE__ALG__SUITE__ID, default__.BRANCH__KEY__ID__B)

    @staticmethod
    def TestInvalidDataKeyError():
        d_877_branchKeyIdSupplier_: AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplier
        nw7_ = DummyBranchKeyIdSupplier()
        nw7_.ctor__()
        d_877_branchKeyIdSupplier_ = nw7_
        d_878_ttl_: int
        d_878_ttl_ = ((1) * (60000)) * (10)
        d_879_mpl_: MaterialProviders.MaterialProvidersClient
        d_880_valueOrError0_: Wrappers.Result = None
        out334_: Wrappers.Result
        out334_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_880_valueOrError0_ = out334_
        if not(not((d_880_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(203,15): " + _dafny.string_of(d_880_valueOrError0_))
        d_879_mpl_ = (d_880_valueOrError0_).Extract()
        d_881_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_882_valueOrError1_: Wrappers.Result = None
        out335_: Wrappers.Result
        out335_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_882_valueOrError1_ = out335_
        if not(not((d_882_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(204,21): " + _dafny.string_of(d_882_valueOrError1_))
        d_881_kmsClient_ = (d_882_valueOrError1_).Extract()
        d_883_ddbClient_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_884_valueOrError2_: Wrappers.Result = None
        out336_: Wrappers.Result
        out336_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_884_valueOrError2_ = out336_
        if not(not((d_884_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(205,21): " + _dafny.string_of(d_884_valueOrError2_))
        d_883_ddbClient_ = (d_884_valueOrError2_).Extract()
        d_885_kmsConfig_: AwsCryptographyKeyStoreTypes.KMSConfiguration
        d_885_kmsConfig_ = AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(default__.keyArn)
        d_886_keyStoreConfig_: AwsCryptographyKeyStoreTypes.KeyStoreConfig
        d_886_keyStoreConfig_ = AwsCryptographyKeyStoreTypes.KeyStoreConfig_KeyStoreConfig(default__.branchKeyStoreName, d_885_kmsConfig_, default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_883_ddbClient_), Wrappers.Option_Some(d_881_kmsClient_))
        d_887_keyStore_: KeyStore.KeyStoreClient
        d_888_valueOrError3_: Wrappers.Result = None
        out337_: Wrappers.Result
        out337_ = KeyStore.default__.KeyStore(d_886_keyStoreConfig_)
        d_888_valueOrError3_ = out337_
        if not(not((d_888_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(216,20): " + _dafny.string_of(d_888_valueOrError3_))
        d_887_keyStore_ = (d_888_valueOrError3_).Extract()
        d_889_hierarchyKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_890_valueOrError4_: Wrappers.Result = None
        out338_: Wrappers.Result
        out338_ = (d_879_mpl_).CreateAwsKmsHierarchicalKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_None(), Wrappers.Option_Some(d_877_branchKeyIdSupplier_), d_887_keyStore_, d_878_ttl_, Wrappers.Option_None()))
        d_890_valueOrError4_ = out338_
        if not(not((d_890_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(217,28): " + _dafny.string_of(d_890_valueOrError4_))
        d_889_hierarchyKeyring_ = (d_890_valueOrError4_).Extract()
        d_891_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out339_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out339_ = default__.GetTestMaterials(default__.TEST__DBE__ALG__SUITE__ID)
        d_891_materials_ = out339_
        d_892_contextCaseA_: _dafny.Map
        d_892_contextCaseA_ = ((d_891_materials_).encryptionContext).set(default__.BRANCH__KEY, default__.CASE__A)
        d_893_contextCaseB_: _dafny.Map
        d_893_contextCaseB_ = ((d_891_materials_).encryptionContext).set(default__.BRANCH__KEY, default__.CASE__B)
        pat_let_tv6_ = d_892_contextCaseA_
        d_894_materialsA_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        def iife32_(_pat_let14_0):
            def iife33_(d_895_dt__update__tmp_h0_):
                def iife34_(_pat_let15_0):
                    def iife35_(d_896_dt__update_hencryptionContext_h0_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_895_dt__update__tmp_h0_).algorithmSuite, d_896_dt__update_hencryptionContext_h0_, (d_895_dt__update__tmp_h0_).encryptedDataKeys, (d_895_dt__update__tmp_h0_).requiredEncryptionContextKeys, (d_895_dt__update__tmp_h0_).plaintextDataKey, (d_895_dt__update__tmp_h0_).signingKey, (d_895_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife35_(_pat_let15_0)
                return iife34_(pat_let_tv6_)
            return iife33_(_pat_let14_0)
        d_894_materialsA_ = iife32_(d_891_materials_)
        pat_let_tv7_ = d_893_contextCaseB_
        d_897_materialsB_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        def iife36_(_pat_let16_0):
            def iife37_(d_898_dt__update__tmp_h1_):
                def iife38_(_pat_let17_0):
                    def iife39_(d_899_dt__update_hencryptionContext_h1_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_898_dt__update__tmp_h1_).algorithmSuite, d_899_dt__update_hencryptionContext_h1_, (d_898_dt__update__tmp_h1_).encryptedDataKeys, (d_898_dt__update__tmp_h1_).requiredEncryptionContextKeys, (d_898_dt__update__tmp_h1_).plaintextDataKey, (d_898_dt__update__tmp_h1_).signingKey, (d_898_dt__update__tmp_h1_).symmetricSigningKeys)
                    return iife39_(_pat_let17_0)
                return iife38_(pat_let_tv7_)
            return iife37_(_pat_let16_0)
        d_897_materialsB_ = iife36_(d_891_materials_)
        default__.TestInvalidDataKeyFailureCase(d_889_hierarchyKeyring_, d_894_materialsA_, d_897_materialsB_, default__.TEST__DBE__ALG__SUITE__ID)

    @staticmethod
    def TestInvalidDataKeyFailureCase(hierarchyKeyring, encryptionMaterialsInEncrypt, encryptionMaterialsInDecrypt, algorithmSuiteId):
        d_900_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_901_valueOrError0_: Wrappers.Result = None
        out340_: Wrappers.Result
        out340_ = (hierarchyKeyring).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(encryptionMaterialsInEncrypt))
        d_901_valueOrError0_ = out340_
        if not(not((d_901_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(245,34): " + _dafny.string_of(d_901_valueOrError0_))
        d_900_encryptionMaterialsOut_ = (d_901_valueOrError0_).Extract()
        d_902_mpl_: MaterialProviders.MaterialProvidersClient
        d_903_valueOrError1_: Wrappers.Result = None
        out341_: Wrappers.Result
        out341_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_903_valueOrError1_ = out341_
        if not(not((d_903_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(249,15): " + _dafny.string_of(d_903_valueOrError1_))
        d_902_mpl_ = (d_903_valueOrError1_).Extract()
        d_904___v2_: tuple
        d_905_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_905_valueOrError2_ = (d_902_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_900_encryptionMaterialsOut_).materials)
        if not(not((d_905_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(250,13): " + _dafny.string_of(d_905_valueOrError2_))
        d_904___v2_ = (d_905_valueOrError2_).Extract()
        if not((len(((d_900_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(252,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_906_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_906_edk_ = (((d_900_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_907_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_908_valueOrError3_: Wrappers.Result = None
        d_908_valueOrError3_ = (d_902_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(algorithmSuiteId, (encryptionMaterialsInDecrypt).encryptionContext, _dafny.Seq([])))
        if not(not((d_908_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(256,33): " + _dafny.string_of(d_908_valueOrError3_))
        d_907_decryptionMaterialsIn_ = (d_908_valueOrError3_).Extract()
        d_909_decryptionMaterialsOut_: Wrappers.Result
        out342_: Wrappers.Result
        out342_ = (hierarchyKeyring).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_907_decryptionMaterialsIn_, _dafny.Seq([d_906_edk_])))
        d_909_decryptionMaterialsOut_ = out342_
        if not((d_909_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(269,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_909_decryptionMaterialsOut_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(270,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_910_expectedErrorMessage_: _dafny.Seq
        d_911_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_911_valueOrError4_ = ErrorMessages.default__.IncorrectDataKeys(_dafny.Seq([d_906_edk_]), (d_907_decryptionMaterialsIn_).algorithmSuite, _dafny.Seq(""))
        if not(not((d_911_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(271,32): " + _dafny.string_of(d_911_valueOrError4_))
        d_910_expectedErrorMessage_ = (d_911_valueOrError4_).Extract()
        if not((((d_909_decryptionMaterialsOut_).error).message) == (d_910_expectedErrorMessage_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(272,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRoundtrip(hierarchyKeyring, encryptionMaterialsIn, algorithmSuiteId, expectedBranchKeyId):
        d_912_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_913_valueOrError0_: Wrappers.Result = None
        out343_: Wrappers.Result
        out343_ = (hierarchyKeyring).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(encryptionMaterialsIn))
        d_913_valueOrError0_ = out343_
        if not(not((d_913_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(285,34): " + _dafny.string_of(d_913_valueOrError0_))
        d_912_encryptionMaterialsOut_ = (d_913_valueOrError0_).Extract()
        d_914_mpl_: MaterialProviders.MaterialProvidersClient
        d_915_valueOrError1_: Wrappers.Result = None
        out344_: Wrappers.Result
        out344_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_915_valueOrError1_ = out344_
        if not(not((d_915_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(289,15): " + _dafny.string_of(d_915_valueOrError1_))
        d_914_mpl_ = (d_915_valueOrError1_).Extract()
        d_916___v3_: tuple
        d_917_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_917_valueOrError2_ = (d_914_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_912_encryptionMaterialsOut_).materials)
        if not(not((d_917_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(290,13): " + _dafny.string_of(d_917_valueOrError2_))
        d_916___v3_ = (d_917_valueOrError2_).Extract()
        if not((len(((d_912_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(292,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_918_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_918_edk_ = (((d_912_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_919_expectedBranchKeyIdUTF8_: _dafny.Seq
        d_920_valueOrError3_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_920_valueOrError3_ = UTF8.default__.Encode(expectedBranchKeyId)
        if not(not((d_920_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(297,35): " + _dafny.string_of(d_920_valueOrError3_))
        d_919_expectedBranchKeyIdUTF8_ = (d_920_valueOrError3_).Extract()
        if not(((d_918_edk_).keyProviderInfo) == (d_919_expectedBranchKeyIdUTF8_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(298,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_921_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_922_valueOrError4_: Wrappers.Result = None
        d_922_valueOrError4_ = (d_914_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(algorithmSuiteId, (encryptionMaterialsIn).encryptionContext, _dafny.Seq([])))
        if not(not((d_922_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(300,33): " + _dafny.string_of(d_922_valueOrError4_))
        d_921_decryptionMaterialsIn_ = (d_922_valueOrError4_).Extract()
        d_923_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_924_valueOrError5_: Wrappers.Result = None
        out345_: Wrappers.Result
        out345_ = (hierarchyKeyring).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_921_decryptionMaterialsIn_, _dafny.Seq([d_918_edk_])))
        d_924_valueOrError5_ = out345_
        if not(not((d_924_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(307,34): " + _dafny.string_of(d_924_valueOrError5_))
        d_923_decryptionMaterialsOut_ = (d_924_valueOrError5_).Extract()
        if not((((d_912_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_923_decryptionMaterialsOut_).materials).plaintextDataKey)):
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
        out346_: Wrappers.Result
        out346_ = AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplier.GetBranchKeyId(self, input)
        return out346_

    def ctor__(self):
        pass
        pass

    def GetBranchKeyId_k(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput.default())()
        d_925_context_: _dafny.Map
        d_925_context_ = (input).encryptionContext
        if ((default__.BRANCH__KEY) in ((d_925_context_).keys)) and (((d_925_context_)[default__.BRANCH__KEY]) == (default__.CASE__A)):
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput_GetBranchKeyIdOutput(default__.BRANCH__KEY__ID__A))
            return output
        elif ((default__.BRANCH__KEY) in ((d_925_context_).keys)) and (((d_925_context_)[default__.BRANCH__KEY]) == (default__.CASE__B)):
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput_GetBranchKeyIdOutput(default__.BRANCH__KEY__ID__B))
            return output
        elif True:
            output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Can't determine branchKeyId from context")))
            return output
        return output

