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
import TestVersionKey as TestVersionKey
import TestUtils as TestUtils
import TestIntermediateKeyWrapping as TestIntermediateKeyWrapping
import TestErrorMessages as TestErrorMessages
import TestDefaultClientProvider as TestDefaultClientProvider
import TestRawECDHKeyring as TestRawECDHKeyring

# Module: TestRawAESKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestOnEncryptOnDecryptGenerateDataKey():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(20,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_namespace_: _dafny.Seq
        d_3_name_: _dafny.Seq
        out1_: _dafny.Seq
        out2_: _dafny.Seq
        out1_, out2_ = TestUtils.default__.NamespaceAndName(0)
        d_2_namespace_ = out1_
        d_3_name_ = out2_
        d_4_valueOrError1_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = (d_1_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_2_namespace_, d_3_name_, _dafny.Seq([0 for d_5_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_4_valueOrError1_ = out3_
        if not(not((d_4_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(23,25): " + _dafny.string_of(d_4_valueOrError1_))
        d_6_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_6_rawAESKeyring_ = (d_4_valueOrError1_).Extract()
        d_7_encryptionContext_: _dafny.Map
        out4_: _dafny.Map
        out4_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_7_encryptionContext_ = out4_
        d_8_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_8_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_9_valueOrError2_: Wrappers.Result = None
        d_9_valueOrError2_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_8_algorithmSuiteId_, d_7_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_9_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(32,33): " + _dafny.string_of(d_9_valueOrError2_))
        d_10_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_10_encryptionMaterialsIn_ = (d_9_valueOrError2_).Extract()
        d_11_valueOrError3_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = (d_6_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_10_encryptionMaterialsIn_))
        d_11_valueOrError3_ = out5_
        if not(not((d_11_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(42,34): " + _dafny.string_of(d_11_valueOrError3_))
        d_12_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_12_encryptionMaterialsOut_ = (d_11_valueOrError3_).Extract()
        d_13_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_13_valueOrError4_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_12_encryptionMaterialsOut_).materials)
        if not(not((d_13_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(57,13): " + _dafny.string_of(d_13_valueOrError4_))
        d_14___v0_: tuple
        d_14___v0_ = (d_13_valueOrError4_).Extract()
        if not((len(((d_12_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(64,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_15_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_15_edk_ = (((d_12_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_16_valueOrError5_: Wrappers.Result = None
        d_16_valueOrError5_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_8_algorithmSuiteId_, d_7_encryptionContext_, _dafny.Seq([])))
        if not(not((d_16_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(68,33): " + _dafny.string_of(d_16_valueOrError5_))
        d_17_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_17_decryptionMaterialsIn_ = (d_16_valueOrError5_).Extract()
        d_18_valueOrError6_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = (d_6_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_17_decryptionMaterialsIn_, _dafny.Seq([d_15_edk_])))
        d_18_valueOrError6_ = out6_
        if not(not((d_18_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(75,34): " + _dafny.string_of(d_18_valueOrError6_))
        d_19_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_19_decryptionMaterialsOut_ = (d_18_valueOrError6_).Extract()
        if not((((d_12_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_12_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(86,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnEncryptOnDecryptSuppliedDataKey():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(93,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_namespace_: _dafny.Seq
        d_3_name_: _dafny.Seq
        out1_: _dafny.Seq
        out2_: _dafny.Seq
        out1_, out2_ = TestUtils.default__.NamespaceAndName(0)
        d_2_namespace_ = out1_
        d_3_name_ = out2_
        d_4_valueOrError1_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = (d_1_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_2_namespace_, d_3_name_, _dafny.Seq([0 for d_5_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_4_valueOrError1_ = out3_
        if not(not((d_4_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(96,25): " + _dafny.string_of(d_4_valueOrError1_))
        d_6_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_6_rawAESKeyring_ = (d_4_valueOrError1_).Extract()
        d_7_encryptionContext_: _dafny.Map
        out4_: _dafny.Map
        out4_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_7_encryptionContext_ = out4_
        d_8_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_8_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_9_valueOrError2_: Wrappers.Result = None
        d_9_valueOrError2_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_8_algorithmSuiteId_, d_7_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_9_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(105,33): " + _dafny.string_of(d_9_valueOrError2_))
        d_10_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_10_encryptionMaterialsIn_ = (d_9_valueOrError2_).Extract()
        d_11_pdk_: _dafny.Seq
        d_11_pdk_ = _dafny.Seq([0 for d_12_i_ in range(32)])
        d_13_valueOrError3_: Wrappers.Result = None
        pat_let_tv0_ = d_11_pdk_
        out5_: Wrappers.Result
        def iife0_(_pat_let2_0):
            def iife1_(d_14_dt__update__tmp_h0_):
                def iife2_(_pat_let3_0):
                    def iife3_(d_15_dt__update_hplaintextDataKey_h0_):
                        return AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((d_14_dt__update__tmp_h0_).algorithmSuite, (d_14_dt__update__tmp_h0_).encryptionContext, (d_14_dt__update__tmp_h0_).encryptedDataKeys, (d_14_dt__update__tmp_h0_).requiredEncryptionContextKeys, d_15_dt__update_hplaintextDataKey_h0_, (d_14_dt__update__tmp_h0_).signingKey, (d_14_dt__update__tmp_h0_).symmetricSigningKeys)
                    return iife3_(_pat_let3_0)
                return iife2_(Wrappers.Option_Some(pat_let_tv0_))
            return iife1_(_pat_let2_0)
        out5_ = (d_6_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(iife0_(d_10_encryptionMaterialsIn_)))
        d_13_valueOrError3_ = out5_
        if not(not((d_13_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(120,34): " + _dafny.string_of(d_13_valueOrError3_))
        d_16_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_16_encryptionMaterialsOut_ = (d_13_valueOrError3_).Extract()
        d_17_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_17_valueOrError4_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_16_encryptionMaterialsOut_).materials)
        if not(not((d_17_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(124,13): " + _dafny.string_of(d_17_valueOrError4_))
        d_18___v1_: tuple
        d_18___v1_ = (d_17_valueOrError4_).Extract()
        d_19_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_19_edk_ = (((d_16_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_20_valueOrError5_: Wrappers.Result = None
        d_20_valueOrError5_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_8_algorithmSuiteId_, d_7_encryptionContext_, _dafny.Seq([])))
        if not(not((d_20_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(128,33): " + _dafny.string_of(d_20_valueOrError5_))
        d_21_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_21_decryptionMaterialsIn_ = (d_20_valueOrError5_).Extract()
        d_22_valueOrError6_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = (d_6_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_21_decryptionMaterialsIn_, _dafny.Seq([d_19_edk_])))
        d_22_valueOrError6_ = out6_
        if not(not((d_22_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(136,34): " + _dafny.string_of(d_22_valueOrError6_))
        d_23_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_23_decryptionMaterialsOut_ = (d_22_valueOrError6_).Extract()
        if not((((d_23_decryptionMaterialsOut_).materials).plaintextDataKey) == (Wrappers.Option_Some(d_11_pdk_))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(148,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptKeyNameMismatch():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(154,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_namespace_: _dafny.Seq
        d_3_name_: _dafny.Seq
        out1_: _dafny.Seq
        out2_: _dafny.Seq
        out1_, out2_ = TestUtils.default__.NamespaceAndName(0)
        d_2_namespace_ = out1_
        d_3_name_ = out2_
        d_4_valueOrError1_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = (d_1_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_2_namespace_, d_3_name_, _dafny.Seq([0 for d_5_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_4_valueOrError1_ = out3_
        if not(not((d_4_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(157,25): " + _dafny.string_of(d_4_valueOrError1_))
        d_6_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_6_rawAESKeyring_ = (d_4_valueOrError1_).Extract()
        d_7_valueOrError2_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = (d_1_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_2_namespace_, _dafny.Seq("mismatched"), _dafny.Seq([1 for d_8_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_7_valueOrError2_ = out4_
        if not(not((d_7_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(164,32): " + _dafny.string_of(d_7_valueOrError2_))
        d_9_mismatchedAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_9_mismatchedAESKeyring_ = (d_7_valueOrError2_).Extract()
        d_10_encryptionContext_: _dafny.Map
        out5_: _dafny.Map
        out5_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_10_encryptionContext_ = out5_
        d_11_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_11_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_12_valueOrError3_: Wrappers.Result = None
        d_12_valueOrError3_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_11_algorithmSuiteId_, d_10_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_12_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(174,33): " + _dafny.string_of(d_12_valueOrError3_))
        d_13_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_13_encryptionMaterialsIn_ = (d_12_valueOrError3_).Extract()
        d_14_valueOrError4_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = (d_6_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_13_encryptionMaterialsIn_))
        d_14_valueOrError4_ = out6_
        if not(not((d_14_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(184,34): " + _dafny.string_of(d_14_valueOrError4_))
        d_15_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_15_encryptionMaterialsOut_ = (d_14_valueOrError4_).Extract()
        d_16_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_16_valueOrError5_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_15_encryptionMaterialsOut_).materials)
        if not(not((d_16_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(188,13): " + _dafny.string_of(d_16_valueOrError5_))
        d_17___v2_: tuple
        d_17___v2_ = (d_16_valueOrError5_).Extract()
        d_18_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_18_edk_ = (((d_15_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_19_valueOrError6_: Wrappers.Result = None
        d_19_valueOrError6_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_11_algorithmSuiteId_, d_10_encryptionContext_, _dafny.Seq([])))
        if not(not((d_19_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(192,33): " + _dafny.string_of(d_19_valueOrError6_))
        d_20_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_20_decryptionMaterialsIn_ = (d_19_valueOrError6_).Extract()
        d_21_decryptionMaterialsOut_: Wrappers.Result
        out7_: Wrappers.Result
        out7_ = (d_9_mismatchedAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_20_decryptionMaterialsIn_, _dafny.Seq([d_18_edk_])))
        d_21_decryptionMaterialsOut_ = out7_
        if not((d_21_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(205,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_21_decryptionMaterialsOut_).error).is_CollectionOfErrors):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_21_decryptionMaterialsOut_).error).list)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(207,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_21_decryptionMaterialsOut_).error).list)[0]).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(208,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((((d_21_decryptionMaterialsOut_).error).list)[0]).message) == (ErrorMessages.default__.IncorrectRawDataKeys(_dafny.Seq("0"), _dafny.Seq("AESKeyring"), d_2_namespace_))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(209,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptBadAndGoodEdkSucceeds():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(215,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_namespace_: _dafny.Seq
        d_3_name_: _dafny.Seq
        out1_: _dafny.Seq
        out2_: _dafny.Seq
        out1_, out2_ = TestUtils.default__.NamespaceAndName(0)
        d_2_namespace_ = out1_
        d_3_name_ = out2_
        d_4_valueOrError1_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = (d_1_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_2_namespace_, d_3_name_, _dafny.Seq([0 for d_5_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_4_valueOrError1_ = out3_
        if not(not((d_4_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(218,25): " + _dafny.string_of(d_4_valueOrError1_))
        d_6_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_6_rawAESKeyring_ = (d_4_valueOrError1_).Extract()
        d_7_encryptionContext_: _dafny.Map
        out4_: _dafny.Map
        out4_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_7_encryptionContext_ = out4_
        d_8_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_8_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_9_valueOrError2_: Wrappers.Result = None
        d_9_valueOrError2_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_8_algorithmSuiteId_, d_7_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_9_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(227,33): " + _dafny.string_of(d_9_valueOrError2_))
        d_10_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_10_encryptionMaterialsIn_ = (d_9_valueOrError2_).Extract()
        d_11_valueOrError3_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = (d_6_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_10_encryptionMaterialsIn_))
        d_11_valueOrError3_ = out5_
        if not(not((d_11_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(237,34): " + _dafny.string_of(d_11_valueOrError3_))
        d_12_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_12_encryptionMaterialsOut_ = (d_11_valueOrError3_).Extract()
        d_13_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_13_valueOrError4_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_12_encryptionMaterialsOut_).materials)
        if not(not((d_13_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(241,13): " + _dafny.string_of(d_13_valueOrError4_))
        d_14___v3_: tuple
        d_14___v3_ = (d_13_valueOrError4_).Extract()
        d_15_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_15_edk_ = (((d_12_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_16_valueOrError5_: Wrappers.Result = None
        d_16_valueOrError5_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_8_algorithmSuiteId_, d_7_encryptionContext_, _dafny.Seq([])))
        if not(not((d_16_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(245,33): " + _dafny.string_of(d_16_valueOrError5_))
        d_17_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_17_decryptionMaterialsIn_ = (d_16_valueOrError5_).Extract()
        d_18_fakeEdk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_18_fakeEdk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey((d_15_edk_).keyProviderId, (d_15_edk_).keyProviderInfo, _dafny.Seq([0 for d_19_i_ in range(len((d_15_edk_).ciphertext))]))
        d_20_valueOrError6_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = (d_6_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_17_decryptionMaterialsIn_, _dafny.Seq([d_18_fakeEdk_, d_15_edk_])))
        d_20_valueOrError6_ = out6_
        if not(not((d_20_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(258,34): " + _dafny.string_of(d_20_valueOrError6_))
        d_21_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_21_decryptionMaterialsOut_ = (d_20_valueOrError6_).Extract()
        if not((((d_21_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_12_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(265,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptNoEDKs():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(271,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_namespace_: _dafny.Seq
        d_3_name_: _dafny.Seq
        out1_: _dafny.Seq
        out2_: _dafny.Seq
        out1_, out2_ = TestUtils.default__.NamespaceAndName(0)
        d_2_namespace_ = out1_
        d_3_name_ = out2_
        d_4_valueOrError1_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = (d_1_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_2_namespace_, d_3_name_, _dafny.Seq([0 for d_5_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_4_valueOrError1_ = out3_
        if not(not((d_4_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(274,25): " + _dafny.string_of(d_4_valueOrError1_))
        d_6_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_6_rawAESKeyring_ = (d_4_valueOrError1_).Extract()
        d_7_encryptionContext_: _dafny.Map
        out4_: _dafny.Map
        out4_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_7_encryptionContext_ = out4_
        d_8_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_8_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_9_valueOrError2_: Wrappers.Result = None
        d_9_valueOrError2_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_8_algorithmSuiteId_, d_7_encryptionContext_, _dafny.Seq([])))
        if not(not((d_9_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(283,33): " + _dafny.string_of(d_9_valueOrError2_))
        d_10_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_10_decryptionMaterialsIn_ = (d_9_valueOrError2_).Extract()
        d_11_decryptionMaterialsOut_: Wrappers.Result
        out5_: Wrappers.Result
        out5_ = (d_6_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_10_decryptionMaterialsIn_, _dafny.Seq([])))
        d_11_decryptionMaterialsOut_ = out5_
        if not((d_11_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(296,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnEncryptUnserializableEC():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(305,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_namespace_: _dafny.Seq
        d_3_name_: _dafny.Seq
        out1_: _dafny.Seq
        out2_: _dafny.Seq
        out1_, out2_ = TestUtils.default__.NamespaceAndName(0)
        d_2_namespace_ = out1_
        d_3_name_ = out2_
        d_4_valueOrError1_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = (d_1_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_2_namespace_, d_3_name_, _dafny.Seq([0 for d_5_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_4_valueOrError1_ = out3_
        if not(not((d_4_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(308,25): " + _dafny.string_of(d_4_valueOrError1_))
        d_6_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_6_rawAESKeyring_ = (d_4_valueOrError1_).Extract()
        d_7_unserializableEncryptionContext_: _dafny.Map
        out4_: _dafny.Map
        out4_ = default__.generateUnserializableEncryptionContext()
        d_7_unserializableEncryptionContext_ = out4_
        d_8_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_8_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_9_valueOrError2_: Wrappers.Result = None
        d_9_valueOrError2_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_8_algorithmSuiteId_, d_7_unserializableEncryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_9_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(317,33): " + _dafny.string_of(d_9_valueOrError2_))
        d_10_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_10_encryptionMaterialsIn_ = (d_9_valueOrError2_).Extract()
        d_11_encryptionMaterialsOut_: Wrappers.Result
        out5_: Wrappers.Result
        out5_ = (d_6_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_10_encryptionMaterialsIn_))
        d_11_encryptionMaterialsOut_ = out5_
        if not((d_11_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(329,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptUnserializableEC():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(339,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_namespace_: _dafny.Seq
        d_3_name_: _dafny.Seq
        out1_: _dafny.Seq
        out2_: _dafny.Seq
        out1_, out2_ = TestUtils.default__.NamespaceAndName(0)
        d_2_namespace_ = out1_
        d_3_name_ = out2_
        d_4_valueOrError1_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = (d_1_mpl_).CreateRawAesKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_2_namespace_, d_3_name_, _dafny.Seq([0 for d_5_i_ in range(32)]), AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()))
        d_4_valueOrError1_ = out3_
        if not(not((d_4_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(342,25): " + _dafny.string_of(d_4_valueOrError1_))
        d_6_rawAESKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_6_rawAESKeyring_ = (d_4_valueOrError1_).Extract()
        d_7_encryptionContext_: _dafny.Map
        out4_: _dafny.Map
        out4_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_7_encryptionContext_ = out4_
        d_8_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_8_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_9_valueOrError2_: Wrappers.Result = None
        d_9_valueOrError2_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_8_algorithmSuiteId_, d_7_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_9_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(351,33): " + _dafny.string_of(d_9_valueOrError2_))
        d_10_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_10_encryptionMaterialsIn_ = (d_9_valueOrError2_).Extract()
        d_11_valueOrError3_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = (d_6_rawAESKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_10_encryptionMaterialsIn_))
        d_11_valueOrError3_ = out5_
        if not(not((d_11_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(361,34): " + _dafny.string_of(d_11_valueOrError3_))
        d_12_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_12_encryptionMaterialsOut_ = (d_11_valueOrError3_).Extract()
        d_13_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_13_valueOrError4_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_12_encryptionMaterialsOut_).materials)
        if not(not((d_13_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(364,13): " + _dafny.string_of(d_13_valueOrError4_))
        d_14___v4_: tuple
        d_14___v4_ = (d_13_valueOrError4_).Extract()
        d_15_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_15_edk_ = (((d_12_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_16_unserializableEncryptionContext_: _dafny.Map
        out6_: _dafny.Map
        out6_ = default__.generateUnserializableEncryptionContext()
        d_16_unserializableEncryptionContext_ = out6_
        d_17_valueOrError5_: Wrappers.Result = None
        d_17_valueOrError5_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_8_algorithmSuiteId_, d_16_unserializableEncryptionContext_, _dafny.Seq([])))
        if not(not((d_17_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(369,33): " + _dafny.string_of(d_17_valueOrError5_))
        d_18_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_18_decryptionMaterialsIn_ = (d_17_valueOrError5_).Extract()
        d_19_decryptionMaterialsOut_: Wrappers.Result
        out7_: Wrappers.Result
        out7_ = (d_6_rawAESKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_18_decryptionMaterialsIn_, _dafny.Seq([d_15_edk_])))
        d_19_decryptionMaterialsOut_ = out7_
        if not((d_19_decryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(382,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def generateUnserializableEncryptionContext():
        encCtx: _dafny.Map = _dafny.Map({})
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_0_valueOrError0_ = UTF8.default__.Encode(_dafny.Seq("keyA"))
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawAESKeyring.dfy(387,16): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_keyA_: _dafny.Seq
        d_1_keyA_ = (d_0_valueOrError0_).Extract()
        d_2_invalidVal_: _dafny.Seq
        d_2_invalidVal_ = _dafny.Seq([0 for d_3___v5_ in range(65536)])
        encCtx = _dafny.Map({d_1_keyA_: d_2_invalidVal_})
        return encCtx
        return encCtx

