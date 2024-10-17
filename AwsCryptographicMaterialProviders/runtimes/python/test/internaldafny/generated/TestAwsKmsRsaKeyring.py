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
import TestRawRSAKeying as TestRawRSAKeying

# Module: TestAwsKmsRsaKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestKmsRsaRoundtrip():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(21,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_2_valueOrError1_ = UTF8.default__.Encode(TestUtils.default__.KMS__RSA__PUBLIC__KEY)
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(23,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_publicKey_: _dafny.Seq
        d_3_publicKey_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = (d_1_mpl_).CreateDefaultClientSupplier(AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_4_valueOrError2_ = out1_
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(25,26): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier
        d_5_clientSupplier_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = (d_5_clientSupplier_).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput(_dafny.Seq("us-west-2")))
        d_6_valueOrError3_ = out2_
        if not(not((d_6_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(26,21): " + _dafny.string_of(d_6_valueOrError3_))
        d_7_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_7_kmsClient_ = (d_6_valueOrError3_).Extract()
        d_8_valueOrError4_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = (d_1_mpl_).CreateAwsKmsRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(d_3_publicKey_), TestUtils.default__.KMS__RSA__PRIVATE__KEY__ARN, ComAmazonawsKmsTypes.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1(), Wrappers.Option_Some(d_7_kmsClient_), Wrappers.Option_None()))
        d_8_valueOrError4_ = out3_
        if not(not((d_8_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(28,25): " + _dafny.string_of(d_8_valueOrError4_))
        d_9_kmsRsaKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_9_kmsRsaKeyring_ = (d_8_valueOrError4_).Extract()
        d_10_encryptionContext_: _dafny.Map
        out4_: _dafny.Map
        out4_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_10_encryptionContext_ = out4_
        d_11_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_11_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_12_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_12_suite_ = AlgorithmSuites.default__.GetSuite(d_11_algorithmSuiteId_)
        d_13_valueOrError5_: Wrappers.Result = None
        d_13_valueOrError5_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_11_algorithmSuiteId_, d_10_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_13_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(40,33): " + _dafny.string_of(d_13_valueOrError5_))
        d_14_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_14_encryptionMaterialsIn_ = (d_13_valueOrError5_).Extract()
        d_15_valueOrError6_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = (d_9_kmsRsaKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_14_encryptionMaterialsIn_))
        d_15_valueOrError6_ = out5_
        if not(not((d_15_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(50,34): " + _dafny.string_of(d_15_valueOrError6_))
        d_16_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_16_encryptionMaterialsOut_ = (d_15_valueOrError6_).Extract()
        d_17_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_17_valueOrError7_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_16_encryptionMaterialsOut_).materials)
        if not(not((d_17_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(54,13): " + _dafny.string_of(d_17_valueOrError7_))
        d_18___v0_: tuple
        d_18___v0_ = (d_17_valueOrError7_).Extract()
        if not((len(((d_16_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_19_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_19_edk_ = (((d_16_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_20_valueOrError8_: Wrappers.Result = None
        d_20_valueOrError8_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_11_algorithmSuiteId_, d_10_encryptionContext_, _dafny.Seq([])))
        if not(not((d_20_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(60,33): " + _dafny.string_of(d_20_valueOrError8_))
        d_21_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_21_decryptionMaterialsIn_ = (d_20_valueOrError8_).Extract()
        d_22_valueOrError9_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = (d_9_kmsRsaKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_21_decryptionMaterialsIn_, _dafny.Seq([d_19_edk_])))
        d_22_valueOrError9_ = out6_
        if not(not((d_22_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(67,34): " + _dafny.string_of(d_22_valueOrError9_))
        d_23_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_23_decryptionMaterialsOut_ = (d_22_valueOrError9_).Extract()
        if not((((d_16_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_23_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsRsaWithAsymmetricSignatureFails():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(79,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_2_valueOrError1_ = UTF8.default__.Encode(TestUtils.default__.KMS__RSA__PUBLIC__KEY)
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(81,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_publicKey_: _dafny.Seq
        d_3_publicKey_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = (d_1_mpl_).CreateDefaultClientSupplier(AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_4_valueOrError2_ = out1_
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(83,26): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier
        d_5_clientSupplier_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = (d_5_clientSupplier_).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput(_dafny.Seq("us-west-2")))
        d_6_valueOrError3_ = out2_
        if not(not((d_6_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(84,21): " + _dafny.string_of(d_6_valueOrError3_))
        d_7_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_7_kmsClient_ = (d_6_valueOrError3_).Extract()
        d_8_valueOrError4_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = (d_1_mpl_).CreateAwsKmsRsaKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(d_3_publicKey_), TestUtils.default__.KMS__RSA__PRIVATE__KEY__ARN, ComAmazonawsKmsTypes.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1(), Wrappers.Option_Some(d_7_kmsClient_), Wrappers.Option_None()))
        d_8_valueOrError4_ = out3_
        if not(not((d_8_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(86,25): " + _dafny.string_of(d_8_valueOrError4_))
        d_9_kmsRsaKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_9_kmsRsaKeyring_ = (d_8_valueOrError4_).Extract()
        d_10_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_10_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_DBE(AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384())
        d_11_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_11_suite_ = AlgorithmSuites.default__.GetSuite(d_10_algorithmSuiteId_)
        d_12_valueOrError5_: Wrappers.Result = None
        d_12_valueOrError5_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_10_algorithmSuiteId_, _dafny.Map({}), _dafny.Seq([]), Wrappers.Option_Some(_dafny.Seq([0, 0, 0, 0, 0])), Wrappers.Option_Some(_dafny.Seq([0, 0, 0, 0, 0]))))
        if not(not((d_12_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(96,33): " + _dafny.string_of(d_12_valueOrError5_))
        d_13_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_13_encryptionMaterialsIn_ = (d_12_valueOrError5_).Extract()
        d_14_encryptionMaterialsOutRes_: Wrappers.Result
        out4_: Wrappers.Result
        out4_ = (d_9_kmsRsaKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_13_encryptionMaterialsIn_))
        d_14_encryptionMaterialsOutRes_ = out4_
        if not((d_14_encryptionMaterialsOutRes_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(110,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_14_encryptionMaterialsOutRes_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(111,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_14_encryptionMaterialsOutRes_).error).message) == ((_dafny.Seq("AwsKmsRsaKeyring cannot be used with")) + (_dafny.Seq(" an Algorithm Suite with asymmetric signing. Please specify an algorithm suite without asymmetric signing.")))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_15_valueOrError6_: Wrappers.Result = None
        d_15_valueOrError6_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_10_algorithmSuiteId_, (d_13_encryptionMaterialsIn_).encryptionContext, _dafny.Seq([])))
        if not(not((d_15_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(115,33): " + _dafny.string_of(d_15_valueOrError6_))
        d_16_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_16_decryptionMaterialsIn_ = (d_15_valueOrError6_).Extract()
        d_17_decryptionMaterialsOutRes_: Wrappers.Result
        out5_: Wrappers.Result
        out5_ = (d_9_kmsRsaKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_16_decryptionMaterialsIn_, _dafny.Seq([])))
        d_17_decryptionMaterialsOutRes_ = out5_
        if not((d_17_decryptionMaterialsOutRes_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(129,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_17_decryptionMaterialsOutRes_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(130,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_17_decryptionMaterialsOutRes_).error).message) == ((_dafny.Seq("AwsKmsRsaKeyring cannot be used with")) + (_dafny.Seq(" an Algorithm Suite with asymmetric signing. Please specify an algorithm suite without asymmetric signing.")))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsRsaKeyring.dfy(131,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

