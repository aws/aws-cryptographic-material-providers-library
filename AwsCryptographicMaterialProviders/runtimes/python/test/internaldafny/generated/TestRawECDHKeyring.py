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

# Module: TestRawECDHKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestRawEcdhDiscoveryOnEncryptFailure():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(30,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(31,22): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_primitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_3_primitives_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out2_: Wrappers.Result
        out2_ = (d_3_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_4_valueOrError2_ = out2_
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(33,19): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_keypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_5_keypair_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_PublicKeyDiscovery(AwsCryptographyMaterialProvidersTypes.PublicKeyDiscoveryInput_PublicKeyDiscoveryInput(((d_5_keypair_).privateKey).pem)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_6_valueOrError3_ = out3_
        if not(not((d_6_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(39,19): " + _dafny.string_of(d_6_valueOrError3_))
        d_7_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_7_keyring_ = (d_6_valueOrError3_).Extract()
        d_8_encryptionContext_: _dafny.Map
        out4_: _dafny.Map
        out4_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_8_encryptionContext_ = out4_
        d_9_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_9_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_10_valueOrError4_: Wrappers.Result = None
        d_10_valueOrError4_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_9_algorithmSuiteId_, d_8_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_10_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(51,33): " + _dafny.string_of(d_10_valueOrError4_))
        d_11_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_11_encryptionMaterialsIn_ = (d_10_valueOrError4_).Extract()
        d_12_encryptionMaterialsOut_: Wrappers.Result
        out5_: Wrappers.Result
        out5_ = (d_7_keyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_11_encryptionMaterialsIn_))
        d_12_encryptionMaterialsOut_ = out5_
        if not((d_12_encryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_12_encryptionMaterialsOut_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_13_expectedErrorMessage_: _dafny.Seq
        d_13_expectedErrorMessage_ = ErrorMessages.default__.RAW__ECDH__DISCOVERY__ENCRYPT__ERROR
        if not((((d_12_encryptionMaterialsOut_).error).message) == (d_13_expectedErrorMessage_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRawEcdhEphemeralOnDecryptFailure():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(73,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(74,22): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_primitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_3_primitives_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out2_: Wrappers.Result
        out2_ = (d_3_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_4_valueOrError2_ = out2_
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(76,19): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_keypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_5_keypair_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.EphemeralPrivateKeyToStaticPublicKeyInput_EphemeralPrivateKeyToStaticPublicKeyInput(((d_5_keypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_6_valueOrError3_ = out3_
        if not(not((d_6_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(82,19): " + _dafny.string_of(d_6_valueOrError3_))
        d_7_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_7_keyring_ = (d_6_valueOrError3_).Extract()
        d_8_encryptionContext_: _dafny.Map
        out4_: _dafny.Map
        out4_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_8_encryptionContext_ = out4_
        d_9_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_9_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_10_valueOrError4_: Wrappers.Result = None
        d_10_valueOrError4_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_9_algorithmSuiteId_, _dafny.Map({}), _dafny.Seq([])))
        if not(not((d_10_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(96,33): " + _dafny.string_of(d_10_valueOrError4_))
        d_11_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_11_decryptionMaterialsIn_ = (d_10_valueOrError4_).Extract()
        d_12_decryptionMaterialsOutRes_: Wrappers.Result
        out5_: Wrappers.Result
        out5_ = (d_7_keyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_11_decryptionMaterialsIn_, _dafny.Seq([])))
        d_12_decryptionMaterialsOutRes_ = out5_
        if not((d_12_decryptionMaterialsOutRes_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(110,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_12_decryptionMaterialsOutRes_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(111,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_12_decryptionMaterialsOutRes_).error).message) == (ErrorMessages.default__.RAW__ECDH__EPHEMERAL__DECRYPT__ERROR)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRawEcdhKeyringEphemeralDecryptOwnMessageFailure():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(117,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(118,22): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_primitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_3_primitives_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out2_: Wrappers.Result
        out2_ = (d_3_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_4_valueOrError2_ = out2_
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(120,19): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_keypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_5_keypair_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.EphemeralPrivateKeyToStaticPublicKeyInput_EphemeralPrivateKeyToStaticPublicKeyInput(((d_5_keypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_6_valueOrError3_ = out3_
        if not(not((d_6_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(126,19): " + _dafny.string_of(d_6_valueOrError3_))
        d_7_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_7_keyring_ = (d_6_valueOrError3_).Extract()
        d_8_encryptionContext_: _dafny.Map
        out4_: _dafny.Map
        out4_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_8_encryptionContext_ = out4_
        d_9_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_9_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_10_valueOrError4_: Wrappers.Result = None
        d_10_valueOrError4_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_9_algorithmSuiteId_, d_8_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_10_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(140,33): " + _dafny.string_of(d_10_valueOrError4_))
        d_11_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_11_encryptionMaterialsIn_ = (d_10_valueOrError4_).Extract()
        d_12_valueOrError5_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = (d_7_keyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_11_encryptionMaterialsIn_))
        d_12_valueOrError5_ = out5_
        if not(not((d_12_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(150,34): " + _dafny.string_of(d_12_valueOrError5_))
        d_13_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_13_encryptionMaterialsOut_ = (d_12_valueOrError5_).Extract()
        d_14_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_14_valueOrError6_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_13_encryptionMaterialsOut_).materials)
        if not(not((d_14_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(154,13): " + _dafny.string_of(d_14_valueOrError6_))
        d_15___v0_: tuple
        d_15___v0_ = (d_14_valueOrError6_).Extract()
        if not((len(((d_13_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(156,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_16_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_16_edk_ = (((d_13_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_17_valueOrError7_: Wrappers.Result = None
        d_17_valueOrError7_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_9_algorithmSuiteId_, d_8_encryptionContext_, _dafny.Seq([])))
        if not(not((d_17_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(159,33): " + _dafny.string_of(d_17_valueOrError7_))
        d_18_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_18_decryptionMaterialsIn_ = (d_17_valueOrError7_).Extract()
        d_19_decryptionMaterialsOut_: Wrappers.Result
        out6_: Wrappers.Result
        out6_ = (d_7_keyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_18_decryptionMaterialsIn_, _dafny.Seq([d_16_edk_])))
        d_19_decryptionMaterialsOut_ = out6_
        if not((d_19_decryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(173,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_19_decryptionMaterialsOut_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(174,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_20_expectedErrorMessage_: _dafny.Seq
        d_20_expectedErrorMessage_ = ErrorMessages.default__.RAW__ECDH__EPHEMERAL__DECRYPT__ERROR
        if not((((d_19_decryptionMaterialsOut_).error).message) == (d_20_expectedErrorMessage_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(177,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRawEcdhKeyringStaticSuccess():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(181,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(182,22): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_primitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_3_primitives_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out2_: Wrappers.Result
        out2_ = (d_3_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_4_valueOrError2_ = out2_
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(184,25): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_senderKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_5_senderKeypair_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out3_: Wrappers.Result
        out3_ = (d_3_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_6_valueOrError3_ = out3_
        if not(not((d_6_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(190,28): " + _dafny.string_of(d_6_valueOrError3_))
        d_7_recipientKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_7_recipientKeypair_ = (d_6_valueOrError3_).Extract()
        d_8_valueOrError4_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(((d_5_senderKeypair_).privateKey).pem, ((d_7_recipientKeypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_8_valueOrError4_ = out4_
        if not(not((d_8_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(196,19): " + _dafny.string_of(d_8_valueOrError4_))
        d_9_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_9_keyring_ = (d_8_valueOrError4_).Extract()
        d_10_encryptionContext_: _dafny.Map
        out5_: _dafny.Map
        out5_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_10_encryptionContext_ = out5_
        d_11_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_11_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_12_valueOrError5_: Wrappers.Result = None
        d_12_valueOrError5_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_11_algorithmSuiteId_, d_10_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_12_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(211,33): " + _dafny.string_of(d_12_valueOrError5_))
        d_13_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_13_encryptionMaterialsIn_ = (d_12_valueOrError5_).Extract()
        d_14_valueOrError6_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = (d_9_keyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_13_encryptionMaterialsIn_))
        d_14_valueOrError6_ = out6_
        if not(not((d_14_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(221,34): " + _dafny.string_of(d_14_valueOrError6_))
        d_15_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_15_encryptionMaterialsOut_ = (d_14_valueOrError6_).Extract()
        d_16_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_16_valueOrError7_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_15_encryptionMaterialsOut_).materials)
        if not(not((d_16_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(225,13): " + _dafny.string_of(d_16_valueOrError7_))
        d_17___v1_: tuple
        d_17___v1_ = (d_16_valueOrError7_).Extract()
        if not((len(((d_15_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(227,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_18_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_18_edk_ = (((d_15_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_19_valueOrError8_: Wrappers.Result = None
        d_19_valueOrError8_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_11_algorithmSuiteId_, d_10_encryptionContext_, _dafny.Seq([])))
        if not(not((d_19_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(230,33): " + _dafny.string_of(d_19_valueOrError8_))
        d_20_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_20_decryptionMaterialsIn_ = (d_19_valueOrError8_).Extract()
        d_21_valueOrError9_: Wrappers.Result = None
        out7_: Wrappers.Result
        out7_ = (d_9_keyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_20_decryptionMaterialsIn_, _dafny.Seq([d_18_edk_])))
        d_21_valueOrError9_ = out7_
        if not(not((d_21_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(237,34): " + _dafny.string_of(d_21_valueOrError9_))
        d_22_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_22_decryptionMaterialsOut_ = (d_21_valueOrError9_).Extract()
        if not((((d_15_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_22_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(244,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestTwoRawEcdhKeyringStaticSuccess():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(250,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(251,22): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_primitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_3_primitives_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out2_: Wrappers.Result
        out2_ = (d_3_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_4_valueOrError2_ = out2_
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(253,25): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_senderKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_5_senderKeypair_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out3_: Wrappers.Result
        out3_ = (d_3_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_6_valueOrError3_ = out3_
        if not(not((d_6_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(259,28): " + _dafny.string_of(d_6_valueOrError3_))
        d_7_recipientKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_7_recipientKeypair_ = (d_6_valueOrError3_).Extract()
        d_8_valueOrError4_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(((d_5_senderKeypair_).privateKey).pem, ((d_7_recipientKeypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_8_valueOrError4_ = out4_
        if not(not((d_8_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(265,25): " + _dafny.string_of(d_8_valueOrError4_))
        d_9_senderKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_9_senderKeyring_ = (d_8_valueOrError4_).Extract()
        d_10_valueOrError5_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(((d_7_recipientKeypair_).privateKey).pem, ((d_5_senderKeypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_10_valueOrError5_ = out5_
        if not(not((d_10_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(277,28): " + _dafny.string_of(d_10_valueOrError5_))
        d_11_recipientKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_11_recipientKeyring_ = (d_10_valueOrError5_).Extract()
        d_12_encryptionContext_: _dafny.Map
        out6_: _dafny.Map
        out6_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_12_encryptionContext_ = out6_
        d_13_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_13_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_14_valueOrError6_: Wrappers.Result = None
        d_14_valueOrError6_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_13_algorithmSuiteId_, d_12_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_14_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(292,33): " + _dafny.string_of(d_14_valueOrError6_))
        d_15_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_15_encryptionMaterialsIn_ = (d_14_valueOrError6_).Extract()
        d_16_valueOrError7_: Wrappers.Result = None
        out7_: Wrappers.Result
        out7_ = (d_9_senderKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_15_encryptionMaterialsIn_))
        d_16_valueOrError7_ = out7_
        if not(not((d_16_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(302,34): " + _dafny.string_of(d_16_valueOrError7_))
        d_17_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_17_encryptionMaterialsOut_ = (d_16_valueOrError7_).Extract()
        d_18_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_18_valueOrError8_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_17_encryptionMaterialsOut_).materials)
        if not(not((d_18_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(306,13): " + _dafny.string_of(d_18_valueOrError8_))
        d_19___v2_: tuple
        d_19___v2_ = (d_18_valueOrError8_).Extract()
        if not((len(((d_17_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(308,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_20_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_20_edk_ = (((d_17_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_21_valueOrError9_: Wrappers.Result = None
        d_21_valueOrError9_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_13_algorithmSuiteId_, d_12_encryptionContext_, _dafny.Seq([])))
        if not(not((d_21_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(311,33): " + _dafny.string_of(d_21_valueOrError9_))
        d_22_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_22_decryptionMaterialsIn_ = (d_21_valueOrError9_).Extract()
        d_23_valueOrError10_: Wrappers.Result = None
        out8_: Wrappers.Result
        out8_ = (d_11_recipientKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_22_decryptionMaterialsIn_, _dafny.Seq([d_20_edk_])))
        d_23_valueOrError10_ = out8_
        if not(not((d_23_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(318,34): " + _dafny.string_of(d_23_valueOrError10_))
        d_24_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_24_decryptionMaterialsOut_ = (d_23_valueOrError10_).Extract()
        if not((((d_17_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_24_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(325,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestTwoEcdhKeyringStaticSuccess():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(331,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(332,22): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_primitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_3_primitives_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out2_: Wrappers.Result
        out2_ = (d_3_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_4_valueOrError2_ = out2_
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(334,25): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_senderKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_5_senderKeypair_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_6_valueOrError3_ = out3_
        if not(not((d_6_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(340,21): " + _dafny.string_of(d_6_valueOrError3_))
        d_7_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_7_kmsClient_ = (d_6_valueOrError3_).Extract()
        d_8_publicKeyResponse_: Wrappers.Result
        out4_: Wrappers.Result
        out4_ = (d_7_kmsClient_).GetPublicKey(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest(TestUtils.default__.KMS__ECC__256__KEY__ARN__R, Wrappers.Option_None()))
        d_8_publicKeyResponse_ = out4_
        if not((d_8_publicKeyResponse_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(347,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs0_ = (d_8_publicKeyResponse_).value
        d_9___v3_ = let_tmp_rhs0_.KeyId
        d_10_PublicKey_ = let_tmp_rhs0_.PublicKey
        d_11___v4_ = let_tmp_rhs0_.CustomerMasterKeySpec
        d_12___v5_ = let_tmp_rhs0_.KeySpec
        d_13___v6_ = let_tmp_rhs0_.KeyUsage
        d_14___v7_ = let_tmp_rhs0_.EncryptionAlgorithms
        d_15___v8_ = let_tmp_rhs0_.SigningAlgorithms
        d_16___v9_ = let_tmp_rhs0_.KeyAgreementAlgorithms
        if not((d_10_PublicKey_).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(350,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_17_valueOrError4_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(((d_5_senderKeypair_).privateKey).pem, (d_10_PublicKey_).value)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_17_valueOrError4_ = out5_
        if not(not((d_17_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(352,25): " + _dafny.string_of(d_17_valueOrError4_))
        d_18_senderKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_18_senderKeyring_ = (d_17_valueOrError4_).Extract()
        d_19_valueOrError5_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(TestUtils.default__.KMS__ECC__256__KEY__ARN__R, Wrappers.Option_None(), ((d_5_senderKeypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), d_7_kmsClient_, Wrappers.Option_None()))
        d_19_valueOrError5_ = out6_
        if not(not((d_19_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(364,35): " + _dafny.string_of(d_19_valueOrError5_))
        d_20_recipientKmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_20_recipientKmsEcdhKeyring_ = (d_19_valueOrError5_).Extract()
        d_21_encryptionContext_: _dafny.Map
        out7_: _dafny.Map
        out7_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_21_encryptionContext_ = out7_
        d_22_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_22_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_23_valueOrError6_: Wrappers.Result = None
        d_23_valueOrError6_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_22_algorithmSuiteId_, d_21_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_23_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(381,33): " + _dafny.string_of(d_23_valueOrError6_))
        d_24_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_24_encryptionMaterialsIn_ = (d_23_valueOrError6_).Extract()
        d_25_valueOrError7_: Wrappers.Result = None
        out8_: Wrappers.Result
        out8_ = (d_18_senderKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_24_encryptionMaterialsIn_))
        d_25_valueOrError7_ = out8_
        if not(not((d_25_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(391,34): " + _dafny.string_of(d_25_valueOrError7_))
        d_26_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_26_encryptionMaterialsOut_ = (d_25_valueOrError7_).Extract()
        d_27_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_27_valueOrError8_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_26_encryptionMaterialsOut_).materials)
        if not(not((d_27_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(395,13): " + _dafny.string_of(d_27_valueOrError8_))
        d_28___v10_: tuple
        d_28___v10_ = (d_27_valueOrError8_).Extract()
        if not((len(((d_26_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(397,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_29_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_29_edk_ = (((d_26_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_30_valueOrError9_: Wrappers.Result = None
        d_30_valueOrError9_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_22_algorithmSuiteId_, d_21_encryptionContext_, _dafny.Seq([])))
        if not(not((d_30_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(400,33): " + _dafny.string_of(d_30_valueOrError9_))
        d_31_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_31_decryptionMaterialsIn_ = (d_30_valueOrError9_).Extract()
        d_32_valueOrError10_: Wrappers.Result = None
        out9_: Wrappers.Result
        out9_ = (d_20_recipientKmsEcdhKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_31_decryptionMaterialsIn_, _dafny.Seq([d_29_edk_])))
        d_32_valueOrError10_ = out9_
        if not(not((d_32_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(407,34): " + _dafny.string_of(d_32_valueOrError10_))
        d_33_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_33_decryptionMaterialsOut_ = (d_32_valueOrError10_).Extract()
        if not((((d_26_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_33_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(414,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestRawEcdhKeyringEncryptDecryptSuccessDBESDKSuite():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(420,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(421,22): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_primitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_3_primitives_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out2_: Wrappers.Result
        out2_ = (d_3_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_4_valueOrError2_ = out2_
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(423,25): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_senderKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_5_senderKeypair_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out3_: Wrappers.Result
        out3_ = (d_3_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_6_valueOrError3_ = out3_
        if not(not((d_6_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(429,28): " + _dafny.string_of(d_6_valueOrError3_))
        d_7_recipientKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_7_recipientKeypair_ = (d_6_valueOrError3_).Extract()
        d_8_valueOrError4_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(((d_5_senderKeypair_).privateKey).pem, ((d_7_recipientKeypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_8_valueOrError4_ = out4_
        if not(not((d_8_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(435,25): " + _dafny.string_of(d_8_valueOrError4_))
        d_9_senderKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_9_senderKeyring_ = (d_8_valueOrError4_).Extract()
        d_10_valueOrError5_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(((d_7_recipientKeypair_).privateKey).pem, ((d_5_senderKeypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_10_valueOrError5_ = out5_
        if not(not((d_10_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(447,28): " + _dafny.string_of(d_10_valueOrError5_))
        d_11_recipientKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_11_recipientKeyring_ = (d_10_valueOrError5_).Extract()
        d_12_encryptionContext_: _dafny.Map
        out6_: _dafny.Map
        out6_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_12_encryptionContext_ = out6_
        d_13_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out7_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        out7_ = default__.GetTestMaterials(default__.TEST__DBE__ALG__SUITE__ID)
        d_13_materials_ = out7_
        d_14_valueOrError6_: Wrappers.Result = None
        out8_: Wrappers.Result
        out8_ = (d_9_senderKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_13_materials_))
        d_14_valueOrError6_ = out8_
        if not(not((d_14_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(463,34): " + _dafny.string_of(d_14_valueOrError6_))
        d_15_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_15_encryptionMaterialsOut_ = (d_14_valueOrError6_).Extract()
        d_16_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_16_valueOrError7_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_15_encryptionMaterialsOut_).materials)
        if not(not((d_16_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(467,13): " + _dafny.string_of(d_16_valueOrError7_))
        d_17___v11_: tuple
        d_17___v11_ = (d_16_valueOrError7_).Extract()
        if not((len(((d_15_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(469,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_18_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_18_edk_ = (((d_15_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_19_valueOrError8_: Wrappers.Result = None
        d_19_valueOrError8_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(default__.TEST__DBE__ALG__SUITE__ID, d_12_encryptionContext_, _dafny.Seq([])))
        if not(not((d_19_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(472,33): " + _dafny.string_of(d_19_valueOrError8_))
        d_20_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_20_decryptionMaterialsIn_ = (d_19_valueOrError8_).Extract()
        d_21_valueOrError9_: Wrappers.Result = None
        out9_: Wrappers.Result
        out9_ = (d_11_recipientKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_20_decryptionMaterialsIn_, _dafny.Seq([d_18_edk_])))
        d_21_valueOrError9_ = out9_
        if not(not((d_21_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(479,34): " + _dafny.string_of(d_21_valueOrError9_))
        d_22_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_22_decryptionMaterialsOut_ = (d_21_valueOrError9_).Extract()
        if not((((d_15_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_22_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(486,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestPrivateKeyandPublicKeySameCurveDiffCurveDefinitionConstructionFailure():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(492,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_2_valueOrError1_ = UTF8.default__.Encode(TestUtils.default__.ECC__P256__PRIVATE)
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(494,28): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_senderPrivateKey_: _dafny.Seq
        d_3_senderPrivateKey_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_4_valueOrError2_ = UTF8.default__.Encode(TestUtils.default__.ECC__P256__PRIVATE__R)
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(495,31): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_recipientPrivateKey_: _dafny.Seq
        d_5_recipientPrivateKey_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_6_valueOrError3_ = Base64.default__.Decode(TestUtils.default__.ECC__P256__PUBLIC__R)
        if not(not((d_6_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(496,30): " + _dafny.string_of(d_6_valueOrError3_))
        d_7_recipientPublicKey_: _dafny.Seq
        d_7_recipientPublicKey_ = (d_6_valueOrError3_).Extract()
        d_8_rawEcdhKeyring_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_3_senderPrivateKey_, d_7_recipientPublicKey_)), default__.P384))
        d_8_rawEcdhKeyring_ = out1_
        if not((d_8_rawEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(509,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestPrivateKeyandPublicKeySameCurveDiffCurveDefinitionConstructionCombinationsFailure():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(514,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_2_valueOrError1_ = UTF8.default__.Encode(TestUtils.default__.ECC__P256__PRIVATE)
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(516,31): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_senderPrivateKey256_: _dafny.Seq
        d_3_senderPrivateKey256_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_4_valueOrError2_ = UTF8.default__.Encode(TestUtils.default__.ECC__P256__PRIVATE__R)
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(517,34): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_recipientPrivateKey256_: _dafny.Seq
        d_5_recipientPrivateKey256_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_6_valueOrError3_ = Base64.default__.Decode(TestUtils.default__.ECC__P256__PUBLIC__R)
        if not(not((d_6_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(518,33): " + _dafny.string_of(d_6_valueOrError3_))
        d_7_recipientPublicKey256_: _dafny.Seq
        d_7_recipientPublicKey256_ = (d_6_valueOrError3_).Extract()
        d_8_valueOrError4_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_8_valueOrError4_ = UTF8.default__.Encode(TestUtils.default__.ECC__P384__PRIVATE)
        if not(not((d_8_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(520,31): " + _dafny.string_of(d_8_valueOrError4_))
        d_9_senderPrivateKey384_: _dafny.Seq
        d_9_senderPrivateKey384_ = (d_8_valueOrError4_).Extract()
        d_10_valueOrError5_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_10_valueOrError5_ = UTF8.default__.Encode(TestUtils.default__.ECC__P384__PRIVATE__R)
        if not(not((d_10_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(521,34): " + _dafny.string_of(d_10_valueOrError5_))
        d_11_recipientPrivateKey384_: _dafny.Seq
        d_11_recipientPrivateKey384_ = (d_10_valueOrError5_).Extract()
        d_12_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_12_valueOrError6_ = Base64.default__.Decode(TestUtils.default__.ECC__P384__PUBLIC__R)
        if not(not((d_12_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(522,33): " + _dafny.string_of(d_12_valueOrError6_))
        d_13_recipientPublicKey384_: _dafny.Seq
        d_13_recipientPublicKey384_ = (d_12_valueOrError6_).Extract()
        d_14_valueOrError7_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_14_valueOrError7_ = UTF8.default__.Encode(TestUtils.default__.ECC__P521__PRIVATE)
        if not(not((d_14_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(524,31): " + _dafny.string_of(d_14_valueOrError7_))
        d_15_senderPrivateKey521_: _dafny.Seq
        d_15_senderPrivateKey521_ = (d_14_valueOrError7_).Extract()
        d_16_valueOrError8_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_16_valueOrError8_ = UTF8.default__.Encode(TestUtils.default__.ECC__P521__PRIVATE__R)
        if not(not((d_16_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(525,34): " + _dafny.string_of(d_16_valueOrError8_))
        d_17_recipientPrivateKey521_: _dafny.Seq
        d_17_recipientPrivateKey521_ = (d_16_valueOrError8_).Extract()
        d_18_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_18_valueOrError9_ = Base64.default__.Decode(TestUtils.default__.ECC__P521__PUBLIC__R)
        if not(not((d_18_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(526,33): " + _dafny.string_of(d_18_valueOrError9_))
        d_19_recipientPublicKey521_: _dafny.Seq
        d_19_recipientPublicKey521_ = (d_18_valueOrError9_).Extract()
        d_20_rawEcdhKeyring_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_3_senderPrivateKey256_, d_7_recipientPublicKey256_)), default__.P384))
        d_20_rawEcdhKeyring_ = out1_
        if not((d_20_rawEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(542,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out2_: Wrappers.Result
        out2_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_3_senderPrivateKey256_, d_7_recipientPublicKey256_)), default__.P521))
        d_20_rawEcdhKeyring_ = out2_
        if not((d_20_rawEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(555,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out3_: Wrappers.Result
        out3_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_9_senderPrivateKey384_, d_13_recipientPublicKey384_)), default__.P256))
        d_20_rawEcdhKeyring_ = out3_
        if not((d_20_rawEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(569,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out4_: Wrappers.Result
        out4_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_9_senderPrivateKey384_, d_13_recipientPublicKey384_)), default__.P521))
        d_20_rawEcdhKeyring_ = out4_
        if not((d_20_rawEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(582,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out5_: Wrappers.Result
        out5_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_15_senderPrivateKey521_, d_19_recipientPublicKey521_)), default__.P256))
        d_20_rawEcdhKeyring_ = out5_
        if not((d_20_rawEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(596,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out6_: Wrappers.Result
        out6_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_15_senderPrivateKey521_, d_19_recipientPublicKey521_)), default__.P384))
        d_20_rawEcdhKeyring_ = out6_
        if not((d_20_rawEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(609,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_21_rawEcdhKeyringT2_: Wrappers.Result
        out7_: Wrappers.Result
        out7_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_3_senderPrivateKey256_, d_13_recipientPublicKey384_)), default__.P256))
        d_21_rawEcdhKeyringT2_ = out7_
        if not((d_21_rawEcdhKeyringT2_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(623,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out8_: Wrappers.Result
        out8_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_3_senderPrivateKey256_, d_19_recipientPublicKey521_)), default__.P256))
        d_21_rawEcdhKeyringT2_ = out8_
        if not((d_21_rawEcdhKeyringT2_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(636,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out9_: Wrappers.Result
        out9_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_9_senderPrivateKey384_, d_7_recipientPublicKey256_)), default__.P384))
        d_21_rawEcdhKeyringT2_ = out9_
        if not((d_21_rawEcdhKeyringT2_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(649,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out10_: Wrappers.Result
        out10_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_9_senderPrivateKey384_, d_19_recipientPublicKey521_)), default__.P384))
        d_21_rawEcdhKeyringT2_ = out10_
        if not((d_21_rawEcdhKeyringT2_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(662,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out11_: Wrappers.Result
        out11_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_15_senderPrivateKey521_, d_7_recipientPublicKey256_)), default__.P521))
        d_21_rawEcdhKeyringT2_ = out11_
        if not((d_21_rawEcdhKeyringT2_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(675,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out12_: Wrappers.Result
        out12_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_15_senderPrivateKey521_, d_13_recipientPublicKey384_)), default__.P521))
        d_21_rawEcdhKeyringT2_ = out12_
        if not((d_21_rawEcdhKeyringT2_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(688,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_22_rawEcdhKeyringT3_: Wrappers.Result
        out13_: Wrappers.Result
        out13_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_9_senderPrivateKey384_, d_7_recipientPublicKey256_)), default__.P256))
        d_22_rawEcdhKeyringT3_ = out13_
        if not((d_22_rawEcdhKeyringT3_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(703,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out14_: Wrappers.Result
        out14_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_15_senderPrivateKey521_, d_7_recipientPublicKey256_)), default__.P256))
        d_22_rawEcdhKeyringT3_ = out14_
        if not((d_22_rawEcdhKeyringT3_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(716,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out15_: Wrappers.Result
        out15_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_3_senderPrivateKey256_, d_13_recipientPublicKey384_)), default__.P384))
        d_22_rawEcdhKeyringT3_ = out15_
        if not((d_22_rawEcdhKeyringT3_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(729,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out16_: Wrappers.Result
        out16_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_15_senderPrivateKey521_, d_13_recipientPublicKey384_)), default__.P384))
        d_22_rawEcdhKeyringT3_ = out16_
        if not((d_22_rawEcdhKeyringT3_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(742,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out17_: Wrappers.Result
        out17_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_3_senderPrivateKey256_, d_19_recipientPublicKey521_)), default__.P521))
        d_22_rawEcdhKeyringT3_ = out17_
        if not((d_22_rawEcdhKeyringT3_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(755,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out18_: Wrappers.Result
        out18_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_9_senderPrivateKey384_, d_19_recipientPublicKey521_)), default__.P521))
        d_22_rawEcdhKeyringT3_ = out18_
        if not((d_22_rawEcdhKeyringT3_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(768,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def GetTestMaterials(suiteId):
        out: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = None
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(773,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_encryptionContext_: _dafny.Map
        out1_: _dafny.Map
        out1_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_2_encryptionContext_ = out1_
        d_3_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_3_suite_ = AlgorithmSuites.default__.GetSuite(suiteId)
        d_4_valueOrError1_: Wrappers.Result = None
        d_4_valueOrError1_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(suiteId, d_2_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_4_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/TesRawECDHKeyring.dfy(778,33): " + _dafny.string_of(d_4_valueOrError1_))
        d_5_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_5_encryptionMaterialsIn_ = (d_4_valueOrError1_).Extract()
        out = d_5_encryptionMaterialsIn_
        return out
        return out

    @_dafny.classproperty
    def P256(instance):
        return AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()
    @_dafny.classproperty
    def TEST__DBE__ALG__SUITE__ID(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_DBE(AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384())
    @_dafny.classproperty
    def P384(instance):
        return AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384()
    @_dafny.classproperty
    def P521(instance):
        return AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()
