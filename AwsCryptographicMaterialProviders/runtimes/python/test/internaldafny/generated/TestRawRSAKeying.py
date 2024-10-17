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
import TestRawAESKeyring as TestRawAESKeyring
import TestMultiKeyring as TestMultiKeyring

# Module: TestRawRSAKeying

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestOnEncryptOnDecryptSuppliedDataKey():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(20,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_namespace_: _dafny.Seq
        d_3_name_: _dafny.Seq
        out1_: _dafny.Seq
        out2_: _dafny.Seq
        out1_, out2_ = TestUtils.default__.NamespaceAndName(0)
        d_2_namespace_ = out1_
        d_3_name_ = out2_
        d_4_keys_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out3_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out3_ = default__.GenerateKeyPair(2048)
        d_4_keys_ = out3_
        d_5_valueOrError1_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = (d_1_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_2_namespace_, d_3_name_, AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_4_keys_).publicKey).pem), Wrappers.Option_Some(((d_4_keys_).privateKey).pem)))
        d_5_valueOrError1_ = out4_
        if not(not((d_5_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(24,25): " + _dafny.string_of(d_5_valueOrError1_))
        d_6_rawRSAKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_6_rawRSAKeyring_ = (d_5_valueOrError1_).Extract()
        d_7_encryptionContext_: _dafny.Map
        out5_: _dafny.Map
        out5_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_7_encryptionContext_ = out5_
        d_8_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_8_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_9_valueOrError2_: Wrappers.Result = None
        d_9_valueOrError2_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_8_algorithmSuiteId_, d_7_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_9_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(37,33): " + _dafny.string_of(d_9_valueOrError2_))
        d_10_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_10_encryptionMaterialsIn_ = (d_9_valueOrError2_).Extract()
        d_11_valueOrError3_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = (d_6_rawRSAKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_10_encryptionMaterialsIn_))
        d_11_valueOrError3_ = out6_
        if not(not((d_11_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(47,34): " + _dafny.string_of(d_11_valueOrError3_))
        d_12_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_12_encryptionMaterialsOut_ = (d_11_valueOrError3_).Extract()
        d_13_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_13_valueOrError4_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_12_encryptionMaterialsOut_).materials)
        if not(not((d_13_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(50,13): " + _dafny.string_of(d_13_valueOrError4_))
        d_14___v0_: tuple
        d_14___v0_ = (d_13_valueOrError4_).Extract()
        d_15_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_15_edk_ = (((d_12_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_16_valueOrError5_: Wrappers.Result = None
        d_16_valueOrError5_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_8_algorithmSuiteId_, d_7_encryptionContext_, _dafny.Seq([])))
        if not(not((d_16_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(54,33): " + _dafny.string_of(d_16_valueOrError5_))
        d_17_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_17_decryptionMaterialsIn_ = (d_16_valueOrError5_).Extract()
        d_18_valueOrError6_: Wrappers.Result = None
        out7_: Wrappers.Result
        out7_ = (d_6_rawRSAKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_17_decryptionMaterialsIn_, _dafny.Seq([d_15_edk_])))
        d_18_valueOrError6_ = out7_
        if not(not((d_18_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(62,34): " + _dafny.string_of(d_18_valueOrError6_))
        d_19_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_19_decryptionMaterialsOut_ = (d_18_valueOrError6_).Extract()
        if not((((d_19_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_12_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptKeyNameMismatch():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(80,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_namespace_: _dafny.Seq
        d_3_name_: _dafny.Seq
        out1_: _dafny.Seq
        out2_: _dafny.Seq
        out1_, out2_ = TestUtils.default__.NamespaceAndName(0)
        d_2_namespace_ = out1_
        d_3_name_ = out2_
        d_4_keys_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out3_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out3_ = default__.GenerateKeyPair(2048)
        d_4_keys_ = out3_
        d_5_valueOrError1_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = (d_1_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_2_namespace_, d_3_name_, AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_4_keys_).publicKey).pem), Wrappers.Option_Some(((d_4_keys_).privateKey).pem)))
        d_5_valueOrError1_ = out4_
        if not(not((d_5_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(84,25): " + _dafny.string_of(d_5_valueOrError1_))
        d_6_rawRSAKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_6_rawRSAKeyring_ = (d_5_valueOrError1_).Extract()
        d_7_valueOrError2_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = (d_1_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_2_namespace_, _dafny.Seq("mismatched"), AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_4_keys_).publicKey).pem), Wrappers.Option_Some(((d_4_keys_).privateKey).pem)))
        d_7_valueOrError2_ = out5_
        if not(not((d_7_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(92,32): " + _dafny.string_of(d_7_valueOrError2_))
        d_8_mismatchedRSAKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_8_mismatchedRSAKeyring_ = (d_7_valueOrError2_).Extract()
        d_9_encryptionContext_: _dafny.Map
        out6_: _dafny.Map
        out6_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_9_encryptionContext_ = out6_
        d_10_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_10_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_11_valueOrError3_: Wrappers.Result = None
        d_11_valueOrError3_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_10_algorithmSuiteId_, d_9_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_11_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(105,33): " + _dafny.string_of(d_11_valueOrError3_))
        d_12_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_12_encryptionMaterialsIn_ = (d_11_valueOrError3_).Extract()
        d_13_valueOrError4_: Wrappers.Result = None
        out7_: Wrappers.Result
        out7_ = (d_6_rawRSAKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_12_encryptionMaterialsIn_))
        d_13_valueOrError4_ = out7_
        if not(not((d_13_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(114,34): " + _dafny.string_of(d_13_valueOrError4_))
        d_14_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_14_encryptionMaterialsOut_ = (d_13_valueOrError4_).Extract()
        d_15_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_15_valueOrError5_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_14_encryptionMaterialsOut_).materials)
        if not(not((d_15_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(117,13): " + _dafny.string_of(d_15_valueOrError5_))
        d_16___v1_: tuple
        d_16___v1_ = (d_15_valueOrError5_).Extract()
        d_17_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_17_edk_ = (((d_14_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_18_valueOrError6_: Wrappers.Result = None
        d_18_valueOrError6_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_10_algorithmSuiteId_, d_9_encryptionContext_, _dafny.Seq([])))
        if not(not((d_18_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(121,33): " + _dafny.string_of(d_18_valueOrError6_))
        d_19_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_19_decryptionMaterialsIn_ = (d_18_valueOrError6_).Extract()
        d_20_decryptionMaterialsOut_: Wrappers.Result
        out8_: Wrappers.Result
        out8_ = (d_8_mismatchedRSAKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_19_decryptionMaterialsIn_, _dafny.Seq([d_17_edk_])))
        d_20_decryptionMaterialsOut_ = out8_
        if not((d_20_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(135,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_20_decryptionMaterialsOut_).error).is_CollectionOfErrors):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(136,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len(((d_20_decryptionMaterialsOut_).error).list)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(137,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((((d_20_decryptionMaterialsOut_).error).list)[0]).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(138,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((((d_20_decryptionMaterialsOut_).error).list)[0]).message) == (ErrorMessages.default__.IncorrectRawDataKeys(_dafny.Seq("0"), _dafny.Seq("RSAKeyring"), d_2_namespace_))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(139,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptFailure():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(145,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_namespace_: _dafny.Seq
        d_3_name_: _dafny.Seq
        out1_: _dafny.Seq
        out2_: _dafny.Seq
        out1_, out2_ = TestUtils.default__.NamespaceAndName(0)
        d_2_namespace_ = out1_
        d_3_name_ = out2_
        d_4_encryptKeys_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out3_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out3_ = default__.GenerateKeyPair(2048)
        d_4_encryptKeys_ = out3_
        d_5_decryptKeys_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out4_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out4_ = default__.GenerateKeyPair(2048)
        d_5_decryptKeys_ = out4_
        d_6_valueOrError1_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = (d_1_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_2_namespace_, d_3_name_, AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_4_encryptKeys_).publicKey).pem), Wrappers.Option_Some(((d_4_encryptKeys_).privateKey).pem)))
        d_6_valueOrError1_ = out5_
        if not(not((d_6_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(153,26): " + _dafny.string_of(d_6_valueOrError1_))
        d_7_encryptKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_7_encryptKeyring_ = (d_6_valueOrError1_).Extract()
        d_8_valueOrError2_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = (d_1_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_2_namespace_, d_3_name_, AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_5_decryptKeys_).publicKey).pem), Wrappers.Option_Some(((d_5_decryptKeys_).privateKey).pem)))
        d_8_valueOrError2_ = out6_
        if not(not((d_8_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(161,26): " + _dafny.string_of(d_8_valueOrError2_))
        d_9_decryptKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_9_decryptKeyring_ = (d_8_valueOrError2_).Extract()
        d_10_encryptionContext_: _dafny.Map
        out7_: _dafny.Map
        out7_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_10_encryptionContext_ = out7_
        d_11_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_11_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_12_valueOrError3_: Wrappers.Result = None
        d_12_valueOrError3_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_11_algorithmSuiteId_, d_10_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_12_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(172,33): " + _dafny.string_of(d_12_valueOrError3_))
        d_13_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_13_encryptionMaterialsIn_ = (d_12_valueOrError3_).Extract()
        d_14_valueOrError4_: Wrappers.Result = None
        out8_: Wrappers.Result
        out8_ = (d_7_encryptKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_13_encryptionMaterialsIn_))
        d_14_valueOrError4_ = out8_
        if not(not((d_14_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(181,34): " + _dafny.string_of(d_14_valueOrError4_))
        d_15_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_15_encryptionMaterialsOut_ = (d_14_valueOrError4_).Extract()
        d_16_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_16_valueOrError5_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_15_encryptionMaterialsOut_).materials)
        if not(not((d_16_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(184,13): " + _dafny.string_of(d_16_valueOrError5_))
        d_17___v2_: tuple
        d_17___v2_ = (d_16_valueOrError5_).Extract()
        d_18_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_18_edk_ = (((d_15_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_19_valueOrError6_: Wrappers.Result = None
        d_19_valueOrError6_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_11_algorithmSuiteId_, d_10_encryptionContext_, _dafny.Seq([])))
        if not(not((d_19_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(188,33): " + _dafny.string_of(d_19_valueOrError6_))
        d_20_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_20_decryptionMaterialsIn_ = (d_19_valueOrError6_).Extract()
        d_21_decryptionMaterialsOut_: Wrappers.Result
        out9_: Wrappers.Result
        out9_ = (d_9_decryptKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_20_decryptionMaterialsIn_, _dafny.Seq([d_18_edk_])))
        d_21_decryptionMaterialsOut_ = out9_
        if not((d_21_decryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(206,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOnDecryptBadAndGoodEdkSucceeds():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(218,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_namespace_: _dafny.Seq
        d_3_name_: _dafny.Seq
        out1_: _dafny.Seq
        out2_: _dafny.Seq
        out1_, out2_ = TestUtils.default__.NamespaceAndName(0)
        d_2_namespace_ = out1_
        d_3_name_ = out2_
        d_4_keys_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out3_: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput
        out3_ = default__.GenerateKeyPair(2048)
        d_4_keys_ = out3_
        d_5_valueOrError1_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = (d_1_mpl_).CreateRawRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_2_namespace_, d_3_name_, AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(), Wrappers.Option_Some(((d_4_keys_).publicKey).pem), Wrappers.Option_Some(((d_4_keys_).privateKey).pem)))
        d_5_valueOrError1_ = out4_
        if not(not((d_5_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(222,25): " + _dafny.string_of(d_5_valueOrError1_))
        d_6_rawRSAKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_6_rawRSAKeyring_ = (d_5_valueOrError1_).Extract()
        d_7_encryptionContext_: _dafny.Map
        out5_: _dafny.Map
        out5_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_7_encryptionContext_ = out5_
        d_8_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_8_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_9_valueOrError2_: Wrappers.Result = None
        d_9_valueOrError2_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_8_algorithmSuiteId_, d_7_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_9_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(235,33): " + _dafny.string_of(d_9_valueOrError2_))
        d_10_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_10_encryptionMaterialsIn_ = (d_9_valueOrError2_).Extract()
        d_11_valueOrError3_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = (d_6_rawRSAKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_10_encryptionMaterialsIn_))
        d_11_valueOrError3_ = out6_
        if not(not((d_11_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(244,34): " + _dafny.string_of(d_11_valueOrError3_))
        d_12_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_12_encryptionMaterialsOut_ = (d_11_valueOrError3_).Extract()
        d_13_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_13_valueOrError4_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_12_encryptionMaterialsOut_).materials)
        if not(not((d_13_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(247,13): " + _dafny.string_of(d_13_valueOrError4_))
        d_14___v3_: tuple
        d_14___v3_ = (d_13_valueOrError4_).Extract()
        d_15_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_15_edk_ = (((d_12_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_16_valueOrError5_: Wrappers.Result = None
        d_16_valueOrError5_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_8_algorithmSuiteId_, d_7_encryptionContext_, _dafny.Seq([])))
        if not(not((d_16_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(251,33): " + _dafny.string_of(d_16_valueOrError5_))
        d_17_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_17_decryptionMaterialsIn_ = (d_16_valueOrError5_).Extract()
        d_18_fakeEdk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_18_fakeEdk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey((d_15_edk_).keyProviderId, (d_15_edk_).keyProviderInfo, _dafny.Seq([0 for d_19_i_ in range(len((d_15_edk_).ciphertext))]))
        d_20_valueOrError6_: Wrappers.Result = None
        out7_: Wrappers.Result
        out7_ = (d_6_rawRSAKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_17_decryptionMaterialsIn_, _dafny.Seq([d_18_fakeEdk_, d_15_edk_])))
        d_20_valueOrError6_ = out7_
        if not(not((d_20_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(268,34): " + _dafny.string_of(d_20_valueOrError6_))
        d_21_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_21_decryptionMaterialsOut_ = (d_20_valueOrError6_).Extract()
        if not((((d_21_decryptionMaterialsOut_).materials).plaintextDataKey) == (((d_12_encryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(279,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def GenerateKeyPair(keyModulusLength):
        keys: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput = None
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(286,18): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_crypto_: AtomicPrimitives.AtomicPrimitivesClient
        d_1_crypto_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = (d_1_crypto_).GenerateRSAKeyPair(AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairInput_GenerateRSAKeyPairInput(keyModulusLength))
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TestRawRSAKeyring.dfy(288,12): " + _dafny.string_of(d_2_valueOrError1_))
        keys = (d_2_valueOrError1_).Extract()
        return keys

