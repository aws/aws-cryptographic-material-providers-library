import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring
import CMM
import Defaults
import Commitment
import DefaultCMM
import DefaultClientSupplier
import RequiredEncryptionContextCMM
import AwsCryptographyMaterialProvidersOperations
import software_amazon_cryptography_materialproviders_internaldafny
import TestUtils
import TestIntermediateKeyWrapping
import TestDefaultClientProvider
import TestRawAESKeyring
import TestMultiKeyring
import TestRawRSAKeying
import TestAwsKmsRsaKeyring

assert "TestAwsKmsHierarchicalKeyring" == __name__
TestAwsKmsHierarchicalKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetTestMaterials(suiteId):
        out: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials = None
        d_2035_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_2036_valueOrError0_: Wrappers.Result = None
        out546_: Wrappers.Result
        out546_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_2036_valueOrError0_ = out546_
        if not(not((d_2036_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(52,12): " + _dafny.string_of(d_2036_valueOrError0_))
        d_2035_mpl_ = (d_2036_valueOrError0_).Extract()
        d_2037_encryptionContext_: _dafny.Map
        out547_: _dafny.Map
        out547_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_2037_encryptionContext_ = out547_
        d_2038_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_2038_suite_ = AlgorithmSuites.default__.GetSuite(suiteId)
        d_2039_encryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_2040_valueOrError1_: Wrappers.Result = None
        d_2040_valueOrError1_ = (d_2035_mpl_).InitializeEncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(suiteId, d_2037_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_2040_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(57,30): " + _dafny.string_of(d_2040_valueOrError1_))
        d_2039_encryptionMaterialsIn_ = (d_2040_valueOrError1_).Extract()
        out = d_2039_encryptionMaterialsIn_
        return out
        return out

    @staticmethod
    def TestHierarchyClientESDKSuite():
        d_2041_branchKeyId_: _dafny.Seq
        d_2041_branchKeyId_ = (TestAwsKmsHierarchicalKeyring.default__).BRANCH__KEY__ID
        d_2042_ttl_: BoundedInts.int64
        d_2042_ttl_ = ((1) * (60000)) * (10)
        d_2043_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_2044_valueOrError0_: Wrappers.Result = None
        out548_: Wrappers.Result
        out548_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_2044_valueOrError0_ = out548_
        if not(not((d_2044_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(74,12): " + _dafny.string_of(d_2044_valueOrError0_))
        d_2043_mpl_ = (d_2044_valueOrError0_).Extract()
        d_2045_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_2046_valueOrError1_: Wrappers.Result = None
        out549_: Wrappers.Result
        out549_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_2046_valueOrError1_ = out549_
        if not(not((d_2046_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(76,18): " + _dafny.string_of(d_2046_valueOrError1_))
        d_2045_kmsClient_ = (d_2046_valueOrError1_).Extract()
        d_2047_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_2048_valueOrError2_: Wrappers.Result = None
        out550_: Wrappers.Result
        out550_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_2048_valueOrError2_ = out550_
        if not(not((d_2048_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(77,18): " + _dafny.string_of(d_2048_valueOrError2_))
        d_2047_ddbClient_ = (d_2048_valueOrError2_).Extract()
        d_2049_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_2049_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((TestAwsKmsHierarchicalKeyring.default__).keyArn)
        d_2050_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_2050_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((TestAwsKmsHierarchicalKeyring.default__).branchKeyStoreName, d_2049_kmsConfig_, (TestAwsKmsHierarchicalKeyring.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_2047_ddbClient_), Wrappers.Option_Some(d_2045_kmsClient_))
        d_2051_keyStore_: software_amazon_cryptography_keystore_internaldafny.KeyStoreClient
        d_2052_valueOrError3_: Wrappers.Result = None
        out551_: Wrappers.Result
        out551_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_2050_keyStoreConfig_)
        d_2052_valueOrError3_ = out551_
        if not(not((d_2052_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(90,17): " + _dafny.string_of(d_2052_valueOrError3_))
        d_2051_keyStore_ = (d_2052_valueOrError3_).Extract()
        d_2053_hierarchyKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_2054_valueOrError4_: Wrappers.Result = None
        out552_: Wrappers.Result
        out552_ = (d_2043_mpl_).CreateAwsKmsHierarchicalKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(d_2041_branchKeyId_), Wrappers.Option_None(), d_2051_keyStore_, d_2042_ttl_, Wrappers.Option_None()))
        d_2054_valueOrError4_ = out552_
        if not(not((d_2054_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(92,25): " + _dafny.string_of(d_2054_valueOrError4_))
        d_2053_hierarchyKeyring_ = (d_2054_valueOrError4_).Extract()
        d_2055_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out553_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out553_ = TestAwsKmsHierarchicalKeyring.default__.GetTestMaterials((TestAwsKmsHierarchicalKeyring.default__).TEST__ESDK__ALG__SUITE__ID)
        d_2055_materials_ = out553_
        TestAwsKmsHierarchicalKeyring.default__.TestRoundtrip(d_2053_hierarchyKeyring_, d_2055_materials_, (TestAwsKmsHierarchicalKeyring.default__).TEST__ESDK__ALG__SUITE__ID, d_2041_branchKeyId_)
        d_2056_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_2056_suite_ = AlgorithmSuites.default__.GetSuite((TestAwsKmsHierarchicalKeyring.default__).TEST__ESDK__ALG__SUITE__ID)
        d_2057_zeroedKey_: _dafny.Seq
        d_2057_zeroedKey_ = _dafny.Seq([0 for d_2058___v0_ in range(AlgorithmSuites.default__.GetEncryptKeyLength(d_2056_suite_))])
        pat_let_tv40_ = d_2057_zeroedKey_
        def iife73_(_pat_let30_0):
            def iife74_(d_2059_dt__update__tmp_h0_):
                def iife75_(_pat_let31_0):
                    def iife76_(d_2060_dt__update_hplaintextDataKey_h0_):
                        return software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials((d_2059_dt__update__tmp_h0_).algorithmSuite, (d_2059_dt__update__tmp_h0_).encryptionContext, (d_2059_dt__update__tmp_h0_).encryptedDataKeys, (d_2059_dt__update__tmp_h0_).requiredEncryptionContextKeys, d_2060_dt__update_hplaintextDataKey_h0_, (d_2059_dt__update__tmp_h0_).signingKey, (d_2059_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife76_(_pat_let31_0)
                return iife75_(Wrappers.Option_Some(pat_let_tv40_))
            return iife74_(_pat_let30_0)
        d_2055_materials_ = iife73_(d_2055_materials_)
        TestAwsKmsHierarchicalKeyring.default__.TestRoundtrip(d_2053_hierarchyKeyring_, d_2055_materials_, (TestAwsKmsHierarchicalKeyring.default__).TEST__ESDK__ALG__SUITE__ID, d_2041_branchKeyId_)

    @staticmethod
    def TestHierarchyClientDBESuite():
        d_2061_branchKeyId_: _dafny.Seq
        d_2061_branchKeyId_ = (TestAwsKmsHierarchicalKeyring.default__).BRANCH__KEY__ID
        d_2062_ttl_: BoundedInts.int64
        d_2062_ttl_ = ((1) * (60000)) * (10)
        d_2063_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_2064_valueOrError0_: Wrappers.Result = None
        out554_: Wrappers.Result
        out554_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_2064_valueOrError0_ = out554_
        if not(not((d_2064_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(115,12): " + _dafny.string_of(d_2064_valueOrError0_))
        d_2063_mpl_ = (d_2064_valueOrError0_).Extract()
        d_2065_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_2066_valueOrError1_: Wrappers.Result = None
        out555_: Wrappers.Result
        out555_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_2066_valueOrError1_ = out555_
        if not(not((d_2066_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(117,18): " + _dafny.string_of(d_2066_valueOrError1_))
        d_2065_kmsClient_ = (d_2066_valueOrError1_).Extract()
        d_2067_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_2068_valueOrError2_: Wrappers.Result = None
        out556_: Wrappers.Result
        out556_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_2068_valueOrError2_ = out556_
        if not(not((d_2068_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(118,18): " + _dafny.string_of(d_2068_valueOrError2_))
        d_2067_ddbClient_ = (d_2068_valueOrError2_).Extract()
        d_2069_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_2069_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((TestAwsKmsHierarchicalKeyring.default__).keyArn)
        d_2070_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_2070_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((TestAwsKmsHierarchicalKeyring.default__).branchKeyStoreName, d_2069_kmsConfig_, (TestAwsKmsHierarchicalKeyring.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_2067_ddbClient_), Wrappers.Option_Some(d_2065_kmsClient_))
        d_2071_keyStore_: software_amazon_cryptography_keystore_internaldafny.KeyStoreClient
        d_2072_valueOrError3_: Wrappers.Result = None
        out557_: Wrappers.Result
        out557_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_2070_keyStoreConfig_)
        d_2072_valueOrError3_ = out557_
        if not(not((d_2072_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(131,17): " + _dafny.string_of(d_2072_valueOrError3_))
        d_2071_keyStore_ = (d_2072_valueOrError3_).Extract()
        d_2073_hierarchyKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_2074_valueOrError4_: Wrappers.Result = None
        out558_: Wrappers.Result
        out558_ = (d_2063_mpl_).CreateAwsKmsHierarchicalKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(d_2061_branchKeyId_), Wrappers.Option_None(), d_2071_keyStore_, d_2062_ttl_, Wrappers.Option_None()))
        d_2074_valueOrError4_ = out558_
        if not(not((d_2074_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(133,25): " + _dafny.string_of(d_2074_valueOrError4_))
        d_2073_hierarchyKeyring_ = (d_2074_valueOrError4_).Extract()
        d_2075_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out559_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out559_ = TestAwsKmsHierarchicalKeyring.default__.GetTestMaterials((TestAwsKmsHierarchicalKeyring.default__).TEST__DBE__ALG__SUITE__ID)
        d_2075_materials_ = out559_
        TestAwsKmsHierarchicalKeyring.default__.TestRoundtrip(d_2073_hierarchyKeyring_, d_2075_materials_, (TestAwsKmsHierarchicalKeyring.default__).TEST__DBE__ALG__SUITE__ID, d_2061_branchKeyId_)
        d_2076_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_2076_suite_ = AlgorithmSuites.default__.GetSuite((TestAwsKmsHierarchicalKeyring.default__).TEST__DBE__ALG__SUITE__ID)
        d_2077_zeroedKey_: _dafny.Seq
        d_2077_zeroedKey_ = _dafny.Seq([0 for d_2078___v1_ in range(AlgorithmSuites.default__.GetEncryptKeyLength(d_2076_suite_))])
        pat_let_tv41_ = d_2077_zeroedKey_
        def iife77_(_pat_let32_0):
            def iife78_(d_2079_dt__update__tmp_h0_):
                def iife79_(_pat_let33_0):
                    def iife80_(d_2080_dt__update_hplaintextDataKey_h0_):
                        return software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials((d_2079_dt__update__tmp_h0_).algorithmSuite, (d_2079_dt__update__tmp_h0_).encryptionContext, (d_2079_dt__update__tmp_h0_).encryptedDataKeys, (d_2079_dt__update__tmp_h0_).requiredEncryptionContextKeys, d_2080_dt__update_hplaintextDataKey_h0_, (d_2079_dt__update__tmp_h0_).signingKey, (d_2079_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife80_(_pat_let33_0)
                return iife79_(Wrappers.Option_Some(pat_let_tv41_))
            return iife78_(_pat_let32_0)
        d_2075_materials_ = iife77_(d_2075_materials_)
        TestAwsKmsHierarchicalKeyring.default__.TestRoundtrip(d_2073_hierarchyKeyring_, d_2075_materials_, (TestAwsKmsHierarchicalKeyring.default__).TEST__DBE__ALG__SUITE__ID, d_2061_branchKeyId_)

    @staticmethod
    def TestBranchKeyIdSupplier():
        d_2081_branchKeyIdSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IBranchKeyIdSupplier
        nw80_ = TestAwsKmsHierarchicalKeyring.DummyBranchKeyIdSupplier()
        nw80_.ctor__()
        d_2081_branchKeyIdSupplier_ = nw80_
        d_2082_ttl_: BoundedInts.int64
        d_2082_ttl_ = ((1) * (60000)) * (10)
        d_2083_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_2084_valueOrError0_: Wrappers.Result = None
        out560_: Wrappers.Result
        out560_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_2084_valueOrError0_ = out560_
        if not(not((d_2084_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(157,12): " + _dafny.string_of(d_2084_valueOrError0_))
        d_2083_mpl_ = (d_2084_valueOrError0_).Extract()
        d_2085_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_2086_valueOrError1_: Wrappers.Result = None
        out561_: Wrappers.Result
        out561_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_2086_valueOrError1_ = out561_
        if not(not((d_2086_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(159,18): " + _dafny.string_of(d_2086_valueOrError1_))
        d_2085_kmsClient_ = (d_2086_valueOrError1_).Extract()
        d_2087_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_2088_valueOrError2_: Wrappers.Result = None
        out562_: Wrappers.Result
        out562_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_2088_valueOrError2_ = out562_
        if not(not((d_2088_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(160,18): " + _dafny.string_of(d_2088_valueOrError2_))
        d_2087_ddbClient_ = (d_2088_valueOrError2_).Extract()
        d_2089_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_2089_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn((TestAwsKmsHierarchicalKeyring.default__).keyArn)
        d_2090_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_2090_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig((TestAwsKmsHierarchicalKeyring.default__).branchKeyStoreName, d_2089_kmsConfig_, (TestAwsKmsHierarchicalKeyring.default__).logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_2087_ddbClient_), Wrappers.Option_Some(d_2085_kmsClient_))
        d_2091_keyStore_: software_amazon_cryptography_keystore_internaldafny.KeyStoreClient
        d_2092_valueOrError3_: Wrappers.Result = None
        out563_: Wrappers.Result
        out563_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_2090_keyStoreConfig_)
        d_2092_valueOrError3_ = out563_
        if not(not((d_2092_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(173,17): " + _dafny.string_of(d_2092_valueOrError3_))
        d_2091_keyStore_ = (d_2092_valueOrError3_).Extract()
        d_2093_hierarchyKeyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
        d_2094_valueOrError4_: Wrappers.Result = None
        out564_: Wrappers.Result
        out564_ = (d_2083_mpl_).CreateAwsKmsHierarchicalKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_None(), Wrappers.Option_Some(d_2081_branchKeyIdSupplier_), d_2091_keyStore_, d_2082_ttl_, Wrappers.Option_None()))
        d_2094_valueOrError4_ = out564_
        if not(not((d_2094_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(175,25): " + _dafny.string_of(d_2094_valueOrError4_))
        d_2093_hierarchyKeyring_ = (d_2094_valueOrError4_).Extract()
        d_2095_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out565_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        out565_ = TestAwsKmsHierarchicalKeyring.default__.GetTestMaterials((TestAwsKmsHierarchicalKeyring.default__).TEST__DBE__ALG__SUITE__ID)
        d_2095_materials_ = out565_
        d_2096_contextCaseA_: _dafny.Map
        d_2096_contextCaseA_ = ((d_2095_materials_).encryptionContext).set((TestAwsKmsHierarchicalKeyring.default__).BRANCH__KEY, (TestAwsKmsHierarchicalKeyring.default__).CASE__A)
        pat_let_tv42_ = d_2096_contextCaseA_
        def iife81_(_pat_let34_0):
            def iife82_(d_2097_dt__update__tmp_h0_):
                def iife83_(_pat_let35_0):
                    def iife84_(d_2098_dt__update_hencryptionContext_h0_):
                        return software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials((d_2097_dt__update__tmp_h0_).algorithmSuite, d_2098_dt__update_hencryptionContext_h0_, (d_2097_dt__update__tmp_h0_).encryptedDataKeys, (d_2097_dt__update__tmp_h0_).requiredEncryptionContextKeys, (d_2097_dt__update__tmp_h0_).plaintextDataKey, (d_2097_dt__update__tmp_h0_).signingKey, (d_2097_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife84_(_pat_let35_0)
                return iife83_(pat_let_tv42_)
            return iife82_(_pat_let34_0)
        d_2095_materials_ = iife81_(d_2095_materials_)
        TestAwsKmsHierarchicalKeyring.default__.TestRoundtrip(d_2093_hierarchyKeyring_, d_2095_materials_, (TestAwsKmsHierarchicalKeyring.default__).TEST__DBE__ALG__SUITE__ID, (TestAwsKmsHierarchicalKeyring.default__).BRANCH__KEY__ID__A)
        d_2099_contextCaseB_: _dafny.Map
        d_2099_contextCaseB_ = ((d_2095_materials_).encryptionContext).set((TestAwsKmsHierarchicalKeyring.default__).BRANCH__KEY, (TestAwsKmsHierarchicalKeyring.default__).CASE__B)
        pat_let_tv43_ = d_2099_contextCaseB_
        def iife85_(_pat_let36_0):
            def iife86_(d_2100_dt__update__tmp_h1_):
                def iife87_(_pat_let37_0):
                    def iife88_(d_2101_dt__update_hencryptionContext_h1_):
                        return software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials((d_2100_dt__update__tmp_h1_).algorithmSuite, d_2101_dt__update_hencryptionContext_h1_, (d_2100_dt__update__tmp_h1_).encryptedDataKeys, (d_2100_dt__update__tmp_h1_).requiredEncryptionContextKeys, (d_2100_dt__update__tmp_h1_).plaintextDataKey, (d_2100_dt__update__tmp_h1_).signingKey, (d_2100_dt__update__tmp_h1_).symmetricSigningKeys)
                    return iife88_(_pat_let37_0)
                return iife87_(pat_let_tv43_)
            return iife86_(_pat_let36_0)
        d_2095_materials_ = iife85_(d_2095_materials_)
        TestAwsKmsHierarchicalKeyring.default__.TestRoundtrip(d_2093_hierarchyKeyring_, d_2095_materials_, (TestAwsKmsHierarchicalKeyring.default__).TEST__DBE__ALG__SUITE__ID, (TestAwsKmsHierarchicalKeyring.default__).BRANCH__KEY__ID__B)

    @staticmethod
    def TestRoundtrip(hierarchyKeyring, encryptionMaterialsIn, algorithmSuiteId, expectedBranchKeyId):
        d_2102_encryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput
        d_2103_valueOrError0_: Wrappers.Result = None
        out566_: Wrappers.Result
        out566_ = (hierarchyKeyring).OnEncrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput(encryptionMaterialsIn))
        d_2103_valueOrError0_ = out566_
        if not(not((d_2103_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(207,31): " + _dafny.string_of(d_2103_valueOrError0_))
        d_2102_encryptionMaterialsOut_ = (d_2103_valueOrError0_).Extract()
        d_2104_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_2105_valueOrError1_: Wrappers.Result = None
        out567_: Wrappers.Result
        out567_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_2105_valueOrError1_ = out567_
        if not(not((d_2105_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(211,12): " + _dafny.string_of(d_2105_valueOrError1_))
        d_2104_mpl_ = (d_2105_valueOrError1_).Extract()
        d_2106___v2_: tuple
        d_2107_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_2107_valueOrError2_ = (d_2104_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_2102_encryptionMaterialsOut_).materials)
        if not(not((d_2107_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(212,10): " + _dafny.string_of(d_2107_valueOrError2_))
        d_2106___v2_ = (d_2107_valueOrError2_).Extract()
        if not((len(((d_2102_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(214,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2108_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_2108_edk_ = (((d_2102_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_2109_expectedBranchKeyIdUTF8_: _dafny.Seq
        d_2110_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_2110_valueOrError3_ = UTF8.default__.Encode(expectedBranchKeyId)
        if not(not((d_2110_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(219,32): " + _dafny.string_of(d_2110_valueOrError3_))
        d_2109_expectedBranchKeyIdUTF8_ = (d_2110_valueOrError3_).Extract()
        if not(((d_2108_edk_).keyProviderInfo) == (d_2109_expectedBranchKeyIdUTF8_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(220,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2111_decryptionMaterialsIn_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_2112_valueOrError4_: Wrappers.Result = None
        d_2112_valueOrError4_ = (d_2104_mpl_).InitializeDecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(algorithmSuiteId, (encryptionMaterialsIn).encryptionContext, _dafny.Seq([])))
        if not(not((d_2112_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(222,30): " + _dafny.string_of(d_2112_valueOrError4_))
        d_2111_decryptionMaterialsIn_ = (d_2112_valueOrError4_).Extract()
        d_2113_decryptionMaterialsOut_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
        d_2114_valueOrError5_: Wrappers.Result = None
        out568_: Wrappers.Result
        out568_ = (hierarchyKeyring).OnDecrypt(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput(d_2111_decryptionMaterialsIn_, _dafny.Seq([d_2108_edk_])))
        d_2114_valueOrError5_ = out568_
        if not(not((d_2114_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(229,31): " + _dafny.string_of(d_2114_valueOrError5_))
        d_2113_decryptionMaterialsOut_ = (d_2114_valueOrError5_).Extract()
        if not((((d_2102_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_2113_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsHierarchicalKeyring/TestAwsKmsHierarchicalKeyring.dfy(241,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def branchKeyStoreName(instance):
        return (Fixtures.default__).branchKeyStoreName
    @_dafny.classproperty
    def logicalKeyStoreName(instance):
        return (TestAwsKmsHierarchicalKeyring.default__).branchKeyStoreName
    @_dafny.classproperty
    def BRANCH__KEY__ID(instance):
        return (Fixtures.default__).branchKeyId
    @_dafny.classproperty
    def BRANCH__KEY__ID__A(instance):
        return (TestAwsKmsHierarchicalKeyring.default__).BRANCH__KEY__ID
    @_dafny.classproperty
    def keyArn(instance):
        return (Fixtures.default__).keyArn
    @_dafny.classproperty
    def TEST__ESDK__ALG__SUITE__ID(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
    @_dafny.classproperty
    def TEST__DBE__ALG__SUITE__ID(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384())
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
        return (Fixtures.default__).branchKeyIdWithEC

class DummyBranchKeyIdSupplier(software_amazon_cryptography_materialproviders_internaldafny_types.IBranchKeyIdSupplier):
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "TestAwsKmsHierarchicalKeyring.DummyBranchKeyIdSupplier"
    def GetBranchKeyId(self, input):
        out569_: Wrappers.Result
        out569_ = software_amazon_cryptography_materialproviders_internaldafny_types.IBranchKeyIdSupplier.GetBranchKeyId(self, input)
        return out569_

    def ctor__(self):
        pass
        pass

    def GetBranchKeyId_k(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput.default())()
        d_2115_context_: _dafny.Map
        d_2115_context_ = (input).encryptionContext
        if (((TestAwsKmsHierarchicalKeyring.default__).BRANCH__KEY) in ((d_2115_context_).keys)) and (((d_2115_context_)[(TestAwsKmsHierarchicalKeyring.default__).BRANCH__KEY]) == ((TestAwsKmsHierarchicalKeyring.default__).CASE__A)):
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput_GetBranchKeyIdOutput((TestAwsKmsHierarchicalKeyring.default__).BRANCH__KEY__ID__A))
            return output
        elif (((TestAwsKmsHierarchicalKeyring.default__).BRANCH__KEY) in ((d_2115_context_).keys)) and (((d_2115_context_)[(TestAwsKmsHierarchicalKeyring.default__).BRANCH__KEY]) == ((TestAwsKmsHierarchicalKeyring.default__).CASE__B)):
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput_GetBranchKeyIdOutput((TestAwsKmsHierarchicalKeyring.default__).BRANCH__KEY__ID__B))
            return output
        elif True:
            output = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Can't determine branchKeyId from context")))
            return output
        return output

