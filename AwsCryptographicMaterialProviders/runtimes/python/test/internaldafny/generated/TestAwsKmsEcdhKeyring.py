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
import TestAwsKmsRsaKeyring as TestAwsKmsRsaKeyring
import TestAwsKmsHierarchicalKeyring as TestAwsKmsHierarchicalKeyring

# Module: TestAwsKmsEcdhKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetTestMaterials(suiteId):
        out: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = None
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(44,15): " + _dafny.string_of(d_0_valueOrError0_))
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
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(49,33): " + _dafny.string_of(d_4_valueOrError1_))
        d_5_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_5_encryptionMaterialsIn_ = (d_4_valueOrError1_).Extract()
        out = d_5_encryptionMaterialsIn_
        return out
        return out

    @staticmethod
    def TestKmsEcdhConfigurationFailure():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(63,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(65,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_3_kmsClient_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery(AwsCryptographyMaterialProvidersTypes.KmsPublicKeyDiscoveryInput_KmsPublicKeyDiscoveryInput(TestUtils.default__.KMS__ECC__256__KEY__ARN__R)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), d_3_kmsClient_, Wrappers.Option_None()))
        d_4_valueOrError2_ = out2_
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(67,48): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_kmsEcdhKeyringDiscoveryConfiguration_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_5_kmsEcdhKeyringDiscoveryConfiguration_ = (d_4_valueOrError2_).Extract()
        d_6_encryptionContext_: _dafny.Map
        out3_: _dafny.Map
        out3_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_6_encryptionContext_ = out3_
        d_7_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_7_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_8_valueOrError3_: Wrappers.Result = None
        d_8_valueOrError3_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_7_algorithmSuiteId_, d_6_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_8_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(83,33): " + _dafny.string_of(d_8_valueOrError3_))
        d_9_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_9_encryptionMaterialsIn_ = (d_8_valueOrError3_).Extract()
        d_10_encryptionMaterialsOut_: Wrappers.Result
        out4_: Wrappers.Result
        out4_ = (d_5_kmsEcdhKeyringDiscoveryConfiguration_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_9_encryptionMaterialsIn_))
        d_10_encryptionMaterialsOut_ = out4_
        if not((d_10_encryptionMaterialsOut_).IsFailure()):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(97,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_10_encryptionMaterialsOut_).error).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(98,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_11_expectedErrorMessage_: _dafny.Seq
        d_11_expectedErrorMessage_ = ErrorMessages.default__.KMS__ECDH__DISCOVERY__ENCRYPT__ERROR
        if not((((d_10_encryptionMaterialsOut_).error).message) == (d_11_expectedErrorMessage_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccess():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(105,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(107,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_3_kmsClient_ = (d_2_valueOrError1_).Extract()
        d_4_senderArns_: _dafny.Seq
        d_4_senderArns_ = _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__S, TestUtils.default__.KMS__ECC__384__KEY__ARN__S, TestUtils.default__.KMS__ECC__521__KEY__ARN__S])
        d_5_recipientArns_: _dafny.Seq
        d_5_recipientArns_ = _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__R, TestUtils.default__.KMS__ECC__384__KEY__ARN__R, TestUtils.default__.KMS__ECC__521__KEY__ARN__R])
        d_6_curveSpecs_: _dafny.Seq
        d_6_curveSpecs_ = _dafny.Seq([AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()])
        hi0_ = len(d_4_senderArns_)
        for d_7_i_ in range(0, hi0_):
            d_8_publicKeyResponse_: Wrappers.Result
            out2_: Wrappers.Result
            out2_ = (d_3_kmsClient_).GetPublicKey(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest((d_5_recipientArns_)[d_7_i_], Wrappers.Option_None()))
            d_8_publicKeyResponse_ = out2_
            if not((d_8_publicKeyResponse_).is_Success):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(121,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            let_tmp_rhs0_ = (d_8_publicKeyResponse_).value
            d_9___v0_ = let_tmp_rhs0_.KeyId
            d_10_PublicKey_ = let_tmp_rhs0_.PublicKey
            d_11___v1_ = let_tmp_rhs0_.CustomerMasterKeySpec
            d_12___v2_ = let_tmp_rhs0_.KeySpec
            d_13___v3_ = let_tmp_rhs0_.KeyUsage
            d_14___v4_ = let_tmp_rhs0_.EncryptionAlgorithms
            d_15___v5_ = let_tmp_rhs0_.SigningAlgorithms
            d_16___v6_ = let_tmp_rhs0_.KeyAgreementAlgorithms
            if not((d_10_PublicKey_).is_Some):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(123,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            _dafny.print(_dafny.string_of(((((_dafny.Seq("\nTest with sender: ")) + ((d_4_senderArns_)[d_7_i_])) + (_dafny.Seq(" and recipient: "))) + ((d_5_recipientArns_)[d_7_i_])) + (_dafny.Seq("\n"))))
            d_17_valueOrError2_: Wrappers.Result = None
            out3_: Wrappers.Result
            out3_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput((d_4_senderArns_)[d_7_i_], Wrappers.Option_None(), (d_10_PublicKey_).value)), (d_6_curveSpecs_)[d_7_i_], d_3_kmsClient_, Wrappers.Option_None()))
            d_17_valueOrError2_ = out3_
            if not(not((d_17_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(126,28): " + _dafny.string_of(d_17_valueOrError2_))
            d_18_kmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_18_kmsEcdhKeyring_ = (d_17_valueOrError2_).Extract()
            d_19_encryptionContext_: _dafny.Map
            out4_: _dafny.Map
            out4_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
            d_19_encryptionContext_ = out4_
            d_20_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
            d_20_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
            d_21_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
            d_21_suite_ = AlgorithmSuites.default__.GetSuite(d_20_algorithmSuiteId_)
            d_22_valueOrError3_: Wrappers.Result = None
            d_22_valueOrError3_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_20_algorithmSuiteId_, d_19_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
            if not(not((d_22_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(144,35): " + _dafny.string_of(d_22_valueOrError3_))
            d_23_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_23_encryptionMaterialsIn_ = (d_22_valueOrError3_).Extract()
            d_24_valueOrError4_: Wrappers.Result = None
            out5_: Wrappers.Result
            out5_ = (d_18_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_23_encryptionMaterialsIn_))
            d_24_valueOrError4_ = out5_
            if not(not((d_24_valueOrError4_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(154,36): " + _dafny.string_of(d_24_valueOrError4_))
            d_25_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
            d_25_encryptionMaterialsOut_ = (d_24_valueOrError4_).Extract()
            d_26_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_26_valueOrError5_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_25_encryptionMaterialsOut_).materials)
            if not(not((d_26_valueOrError5_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(158,15): " + _dafny.string_of(d_26_valueOrError5_))
            d_27___v7_: tuple
            d_27___v7_ = (d_26_valueOrError5_).Extract()
            if not((len(((d_25_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(160,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_28_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
            d_28_edk_ = (((d_25_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
            d_29_valueOrError6_: Wrappers.Result = None
            d_29_valueOrError6_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_20_algorithmSuiteId_, d_19_encryptionContext_, _dafny.Seq([])))
            if not(not((d_29_valueOrError6_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(163,35): " + _dafny.string_of(d_29_valueOrError6_))
            d_30_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
            d_30_decryptionMaterialsIn_ = (d_29_valueOrError6_).Extract()
            d_31_valueOrError7_: Wrappers.Result = None
            out6_: Wrappers.Result
            out6_ = (d_18_kmsEcdhKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_30_decryptionMaterialsIn_, _dafny.Seq([d_28_edk_])))
            d_31_valueOrError7_ = out6_
            if not(not((d_31_valueOrError7_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(170,36): " + _dafny.string_of(d_31_valueOrError7_))
            d_32_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
            d_32_decryptionMaterialsOut_ = (d_31_valueOrError7_).Extract()
            if not((((d_25_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_32_decryptionMaterialsOut_).materials).plaintextDataKey)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(177,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccessDBESDKSuite():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(183,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(185,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_3_kmsClient_ = (d_2_valueOrError1_).Extract()
        d_4_senderArns_: _dafny.Seq
        d_4_senderArns_ = _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__S, TestUtils.default__.KMS__ECC__384__KEY__ARN__S, TestUtils.default__.KMS__ECC__521__KEY__ARN__S])
        d_5_recipientArns_: _dafny.Seq
        d_5_recipientArns_ = _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__R, TestUtils.default__.KMS__ECC__384__KEY__ARN__R, TestUtils.default__.KMS__ECC__521__KEY__ARN__R])
        d_6_curveSpecs_: _dafny.Seq
        d_6_curveSpecs_ = _dafny.Seq([AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()])
        hi0_ = len(d_4_senderArns_)
        for d_7_i_ in range(0, hi0_):
            d_8_publicKeyResponse_: Wrappers.Result
            out2_: Wrappers.Result
            out2_ = (d_3_kmsClient_).GetPublicKey(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest((d_5_recipientArns_)[d_7_i_], Wrappers.Option_None()))
            d_8_publicKeyResponse_ = out2_
            if not((d_8_publicKeyResponse_).is_Success):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(199,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            let_tmp_rhs0_ = (d_8_publicKeyResponse_).value
            d_9___v8_ = let_tmp_rhs0_.KeyId
            d_10_PublicKey_ = let_tmp_rhs0_.PublicKey
            d_11___v9_ = let_tmp_rhs0_.CustomerMasterKeySpec
            d_12___v10_ = let_tmp_rhs0_.KeySpec
            d_13___v11_ = let_tmp_rhs0_.KeyUsage
            d_14___v12_ = let_tmp_rhs0_.EncryptionAlgorithms
            d_15___v13_ = let_tmp_rhs0_.SigningAlgorithms
            d_16___v14_ = let_tmp_rhs0_.KeyAgreementAlgorithms
            if not((d_10_PublicKey_).is_Some):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(201,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            _dafny.print(_dafny.string_of(((((_dafny.Seq("\nTest with sender: ")) + ((d_4_senderArns_)[d_7_i_])) + (_dafny.Seq(" and recipient: "))) + ((d_5_recipientArns_)[d_7_i_])) + (_dafny.Seq("\n"))))
            d_17_valueOrError2_: Wrappers.Result = None
            out3_: Wrappers.Result
            out3_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput((d_4_senderArns_)[d_7_i_], Wrappers.Option_None(), (d_10_PublicKey_).value)), (d_6_curveSpecs_)[d_7_i_], d_3_kmsClient_, Wrappers.Option_None()))
            d_17_valueOrError2_ = out3_
            if not(not((d_17_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(204,28): " + _dafny.string_of(d_17_valueOrError2_))
            d_18_kmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_18_kmsEcdhKeyring_ = (d_17_valueOrError2_).Extract()
            d_19_encryptionContext_: _dafny.Map
            out4_: _dafny.Map
            out4_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
            d_19_encryptionContext_ = out4_
            d_20_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            out5_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            out5_ = default__.GetTestMaterials(default__.TEST__DBE__ALG__SUITE__ID)
            d_20_materials_ = out5_
            d_21_valueOrError3_: Wrappers.Result = None
            out6_: Wrappers.Result
            out6_ = (d_18_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_20_materials_))
            d_21_valueOrError3_ = out6_
            if not(not((d_21_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(221,36): " + _dafny.string_of(d_21_valueOrError3_))
            d_22_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
            d_22_encryptionMaterialsOut_ = (d_21_valueOrError3_).Extract()
            d_23_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_23_valueOrError4_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_22_encryptionMaterialsOut_).materials)
            if not(not((d_23_valueOrError4_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(225,15): " + _dafny.string_of(d_23_valueOrError4_))
            d_24___v15_: tuple
            d_24___v15_ = (d_23_valueOrError4_).Extract()
            if not((len(((d_22_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(227,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_25_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
            d_25_edk_ = (((d_22_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
            d_26_valueOrError5_: Wrappers.Result = None
            d_26_valueOrError5_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(default__.TEST__DBE__ALG__SUITE__ID, d_19_encryptionContext_, _dafny.Seq([])))
            if not(not((d_26_valueOrError5_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(230,35): " + _dafny.string_of(d_26_valueOrError5_))
            d_27_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
            d_27_decryptionMaterialsIn_ = (d_26_valueOrError5_).Extract()
            d_28_valueOrError6_: Wrappers.Result = None
            out7_: Wrappers.Result
            out7_ = (d_18_kmsEcdhKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_27_decryptionMaterialsIn_, _dafny.Seq([d_25_edk_])))
            d_28_valueOrError6_ = out7_
            if not(not((d_28_valueOrError6_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(237,36): " + _dafny.string_of(d_28_valueOrError6_))
            d_29_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
            d_29_decryptionMaterialsOut_ = (d_28_valueOrError6_).Extract()
            if not((((d_22_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_29_decryptionMaterialsOut_).materials).plaintextDataKey)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(244,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhKeyringDiscoverySuccess():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(251,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(253,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_3_kmsClient_ = (d_2_valueOrError1_).Extract()
        d_4_senderArns_: _dafny.Seq
        d_4_senderArns_ = _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__S, TestUtils.default__.KMS__ECC__384__KEY__ARN__S, TestUtils.default__.KMS__ECC__521__KEY__ARN__S])
        d_5_recipientArns_: _dafny.Seq
        d_5_recipientArns_ = _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__R, TestUtils.default__.KMS__ECC__384__KEY__ARN__R, TestUtils.default__.KMS__ECC__521__KEY__ARN__R])
        d_6_curveSpecs_: _dafny.Seq
        d_6_curveSpecs_ = _dafny.Seq([AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()])
        hi0_ = len(d_4_senderArns_)
        for d_7_i_ in range(0, hi0_):
            d_8_publicKeyResponse_: Wrappers.Result
            out2_: Wrappers.Result
            out2_ = (d_3_kmsClient_).GetPublicKey(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest((d_5_recipientArns_)[d_7_i_], Wrappers.Option_None()))
            d_8_publicKeyResponse_ = out2_
            if not((d_8_publicKeyResponse_).is_Success):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(267,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            let_tmp_rhs0_ = (d_8_publicKeyResponse_).value
            d_9___v16_ = let_tmp_rhs0_.KeyId
            d_10_PublicKey_ = let_tmp_rhs0_.PublicKey
            d_11___v17_ = let_tmp_rhs0_.CustomerMasterKeySpec
            d_12___v18_ = let_tmp_rhs0_.KeySpec
            d_13___v19_ = let_tmp_rhs0_.KeyUsage
            d_14___v20_ = let_tmp_rhs0_.EncryptionAlgorithms
            d_15___v21_ = let_tmp_rhs0_.SigningAlgorithms
            d_16___v22_ = let_tmp_rhs0_.KeyAgreementAlgorithms
            if not((d_10_PublicKey_).is_Some):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(269,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_17_valueOrError2_: Wrappers.Result = None
            out3_: Wrappers.Result
            out3_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput((d_4_senderArns_)[d_7_i_], Wrappers.Option_None(), (d_10_PublicKey_).value)), (d_6_curveSpecs_)[d_7_i_], d_3_kmsClient_, Wrappers.Option_None()))
            d_17_valueOrError2_ = out3_
            if not(not((d_17_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(271,28): " + _dafny.string_of(d_17_valueOrError2_))
            d_18_kmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_18_kmsEcdhKeyring_ = (d_17_valueOrError2_).Extract()
            d_19_valueOrError3_: Wrappers.Result = None
            out4_: Wrappers.Result
            out4_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery(AwsCryptographyMaterialProvidersTypes.KmsPublicKeyDiscoveryInput_KmsPublicKeyDiscoveryInput((d_5_recipientArns_)[d_7_i_])), (d_6_curveSpecs_)[d_7_i_], d_3_kmsClient_, Wrappers.Option_None()))
            d_19_valueOrError3_ = out4_
            if not(not((d_19_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(285,37): " + _dafny.string_of(d_19_valueOrError3_))
            d_20_kmsEcdhKeyringDiscovery_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_20_kmsEcdhKeyringDiscovery_ = (d_19_valueOrError3_).Extract()
            d_21_encryptionContext_: _dafny.Map
            out5_: _dafny.Map
            out5_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
            d_21_encryptionContext_ = out5_
            d_22_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
            d_22_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
            d_23_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
            d_23_suite_ = AlgorithmSuites.default__.GetSuite(d_22_algorithmSuiteId_)
            d_24_valueOrError4_: Wrappers.Result = None
            d_24_valueOrError4_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_22_algorithmSuiteId_, d_21_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
            if not(not((d_24_valueOrError4_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(302,35): " + _dafny.string_of(d_24_valueOrError4_))
            d_25_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_25_encryptionMaterialsIn_ = (d_24_valueOrError4_).Extract()
            d_26_valueOrError5_: Wrappers.Result = None
            out6_: Wrappers.Result
            out6_ = (d_18_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_25_encryptionMaterialsIn_))
            d_26_valueOrError5_ = out6_
            if not(not((d_26_valueOrError5_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(312,36): " + _dafny.string_of(d_26_valueOrError5_))
            d_27_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
            d_27_encryptionMaterialsOut_ = (d_26_valueOrError5_).Extract()
            d_28_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_28_valueOrError6_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_27_encryptionMaterialsOut_).materials)
            if not(not((d_28_valueOrError6_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(316,15): " + _dafny.string_of(d_28_valueOrError6_))
            d_29___v23_: tuple
            d_29___v23_ = (d_28_valueOrError6_).Extract()
            if not((len(((d_27_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(318,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_30_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
            d_30_edk_ = (((d_27_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
            d_31_valueOrError7_: Wrappers.Result = None
            d_31_valueOrError7_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_22_algorithmSuiteId_, d_21_encryptionContext_, _dafny.Seq([])))
            if not(not((d_31_valueOrError7_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(321,35): " + _dafny.string_of(d_31_valueOrError7_))
            d_32_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
            d_32_decryptionMaterialsIn_ = (d_31_valueOrError7_).Extract()
            _dafny.print(_dafny.string_of(((_dafny.Seq("\nDiscovery Test for: ")) + ((d_5_recipientArns_)[d_7_i_])) + (_dafny.Seq("\n"))))
            d_33_valueOrError8_: Wrappers.Result = None
            out7_: Wrappers.Result
            out7_ = (d_20_kmsEcdhKeyringDiscovery_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_32_decryptionMaterialsIn_, _dafny.Seq([d_30_edk_])))
            d_33_valueOrError8_ = out7_
            if not(not((d_33_valueOrError8_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(329,36): " + _dafny.string_of(d_33_valueOrError8_))
            d_34_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
            d_34_decryptionMaterialsOut_ = (d_33_valueOrError8_).Extract()
            if not((((d_27_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_34_decryptionMaterialsOut_).materials).plaintextDataKey)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(336,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhKeyringRecipientRawKeyEncryptDecryptSuccessSetSenderPublicKey():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(343,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(344,22): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_primitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_3_primitives_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out2_: Wrappers.Result
        out2_ = (d_3_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(default__.P256))
        d_4_valueOrError2_ = out2_
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(346,28): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_recipientKeypair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_5_recipientKeypair_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_6_valueOrError3_ = out3_
        if not(not((d_6_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(352,21): " + _dafny.string_of(d_6_valueOrError3_))
        d_7_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_7_kmsClient_ = (d_6_valueOrError3_).Extract()
        d_8_publicKeyResponse_: Wrappers.Result
        out4_: Wrappers.Result
        out4_ = (d_7_kmsClient_).GetPublicKey(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest(TestUtils.default__.KMS__ECC__256__KEY__ARN__S, Wrappers.Option_None()))
        d_8_publicKeyResponse_ = out4_
        if not((d_8_publicKeyResponse_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(359,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs0_ = (d_8_publicKeyResponse_).value
        d_9___v24_ = let_tmp_rhs0_.KeyId
        d_10_PublicKey_ = let_tmp_rhs0_.PublicKey
        d_11___v25_ = let_tmp_rhs0_.CustomerMasterKeySpec
        d_12___v26_ = let_tmp_rhs0_.KeySpec
        d_13___v27_ = let_tmp_rhs0_.KeyUsage
        d_14___v28_ = let_tmp_rhs0_.EncryptionAlgorithms
        d_15___v29_ = let_tmp_rhs0_.SigningAlgorithms
        d_16___v30_ = let_tmp_rhs0_.KeyAgreementAlgorithms
        if not((d_10_PublicKey_).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(362,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_17_valueOrError4_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(TestUtils.default__.KMS__ECC__256__KEY__ARN__S, Wrappers.Option_Some((d_10_PublicKey_).value), ((d_5_recipientKeypair_).publicKey).der)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), d_7_kmsClient_, Wrappers.Option_None()))
        d_17_valueOrError4_ = out5_
        if not(not((d_17_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(364,26): " + _dafny.string_of(d_17_valueOrError4_))
        d_18_kmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_18_kmsEcdhKeyring_ = (d_17_valueOrError4_).Extract()
        d_19_valueOrError5_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(((d_5_recipientKeypair_).privateKey).pem, (d_10_PublicKey_).value)), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_19_valueOrError5_ = out6_
        if not(not((d_19_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(379,28): " + _dafny.string_of(d_19_valueOrError5_))
        d_20_recipientKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_20_recipientKeyring_ = (d_19_valueOrError5_).Extract()
        d_21_encryptionContext_: _dafny.Map
        out7_: _dafny.Map
        out7_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_21_encryptionContext_ = out7_
        d_22_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_22_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_23_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_23_suite_ = AlgorithmSuites.default__.GetSuite(d_22_algorithmSuiteId_)
        d_24_valueOrError6_: Wrappers.Result = None
        d_24_valueOrError6_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_22_algorithmSuiteId_, d_21_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_24_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(395,33): " + _dafny.string_of(d_24_valueOrError6_))
        d_25_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_25_encryptionMaterialsIn_ = (d_24_valueOrError6_).Extract()
        d_26_valueOrError7_: Wrappers.Result = None
        out8_: Wrappers.Result
        out8_ = (d_18_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_25_encryptionMaterialsIn_))
        d_26_valueOrError7_ = out8_
        if not(not((d_26_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(405,34): " + _dafny.string_of(d_26_valueOrError7_))
        d_27_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
        d_27_encryptionMaterialsOut_ = (d_26_valueOrError7_).Extract()
        d_28_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_28_valueOrError8_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_27_encryptionMaterialsOut_).materials)
        if not(not((d_28_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(409,13): " + _dafny.string_of(d_28_valueOrError8_))
        d_29___v31_: tuple
        d_29___v31_ = (d_28_valueOrError8_).Extract()
        if not((len(((d_27_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(411,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_30_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_30_edk_ = (((d_27_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
        d_31_valueOrError9_: Wrappers.Result = None
        d_31_valueOrError9_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_22_algorithmSuiteId_, d_21_encryptionContext_, _dafny.Seq([])))
        if not(not((d_31_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(414,33): " + _dafny.string_of(d_31_valueOrError9_))
        d_32_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_32_decryptionMaterialsIn_ = (d_31_valueOrError9_).Extract()
        d_33_valueOrError10_: Wrappers.Result = None
        out9_: Wrappers.Result
        out9_ = (d_20_recipientKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_32_decryptionMaterialsIn_, _dafny.Seq([d_30_edk_])))
        d_33_valueOrError10_ = out9_
        if not(not((d_33_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(421,34): " + _dafny.string_of(d_33_valueOrError10_))
        d_34_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
        d_34_decryptionMaterialsOut_ = (d_33_valueOrError10_).Extract()
        if not((((d_27_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_34_decryptionMaterialsOut_).materials).plaintextDataKey)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(428,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhKeyringWithDerPublicKeys():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(434,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(436,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_3_kmsClient_ = (d_2_valueOrError1_).Extract()
        hi0_ = len(default__.CURVES)
        for d_4_i_ in range(0, hi0_):
            d_5_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_5_valueOrError2_ = Base64.default__.Decode((default__.derKmsSenderPublicKeyStrings)[d_4_i_])
            if not(not((d_5_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(440,29): " + _dafny.string_of(d_5_valueOrError2_))
            d_6_senderPublicKey_: _dafny.Seq
            d_6_senderPublicKey_ = (d_5_valueOrError2_).Extract()
            d_7_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_7_valueOrError3_ = Base64.default__.Decode((default__.derKmsRecipientPublicKeyStrings)[d_4_i_])
            if not(not((d_7_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(441,32): " + _dafny.string_of(d_7_valueOrError3_))
            d_8_recipientPublicKey_: _dafny.Seq
            d_8_recipientPublicKey_ = (d_7_valueOrError3_).Extract()
            d_9_valueOrError4_: Wrappers.Result = None
            out2_: Wrappers.Result
            out2_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput((default__.senderKmsKeys)[d_4_i_], Wrappers.Option_Some(d_6_senderPublicKey_), d_8_recipientPublicKey_)), (default__.CURVES)[d_4_i_], d_3_kmsClient_, Wrappers.Option_None()))
            d_9_valueOrError4_ = out2_
            if not(not((d_9_valueOrError4_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(443,34): " + _dafny.string_of(d_9_valueOrError4_))
            d_10_senderKmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_10_senderKmsEcdhKeyring_ = (d_9_valueOrError4_).Extract()
            d_11_valueOrError5_: Wrappers.Result = None
            out3_: Wrappers.Result
            out3_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput((default__.recipientKmsKeys)[d_4_i_], Wrappers.Option_Some(d_8_recipientPublicKey_), d_6_senderPublicKey_)), (default__.CURVES)[d_4_i_], d_3_kmsClient_, Wrappers.Option_None()))
            d_11_valueOrError5_ = out3_
            if not(not((d_11_valueOrError5_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(458,37): " + _dafny.string_of(d_11_valueOrError5_))
            d_12_recipientKmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_12_recipientKmsEcdhKeyring_ = (d_11_valueOrError5_).Extract()
            d_13_encryptionContext_: _dafny.Map
            out4_: _dafny.Map
            out4_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
            d_13_encryptionContext_ = out4_
            d_14_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
            d_14_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
            d_15_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
            d_15_suite_ = AlgorithmSuites.default__.GetSuite(d_14_algorithmSuiteId_)
            d_16_valueOrError6_: Wrappers.Result = None
            d_16_valueOrError6_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_14_algorithmSuiteId_, d_13_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
            if not(not((d_16_valueOrError6_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(477,35): " + _dafny.string_of(d_16_valueOrError6_))
            d_17_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_17_encryptionMaterialsIn_ = (d_16_valueOrError6_).Extract()
            d_18_valueOrError7_: Wrappers.Result = None
            out5_: Wrappers.Result
            out5_ = (d_10_senderKmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_17_encryptionMaterialsIn_))
            d_18_valueOrError7_ = out5_
            if not(not((d_18_valueOrError7_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(487,36): " + _dafny.string_of(d_18_valueOrError7_))
            d_19_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
            d_19_encryptionMaterialsOut_ = (d_18_valueOrError7_).Extract()
            d_20_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_20_valueOrError8_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_19_encryptionMaterialsOut_).materials)
            if not(not((d_20_valueOrError8_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(491,15): " + _dafny.string_of(d_20_valueOrError8_))
            d_21___v32_: tuple
            d_21___v32_ = (d_20_valueOrError8_).Extract()
            if not((len(((d_19_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(493,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_22_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
            d_22_edk_ = (((d_19_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
            d_23_valueOrError9_: Wrappers.Result = None
            d_23_valueOrError9_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_14_algorithmSuiteId_, d_13_encryptionContext_, _dafny.Seq([])))
            if not(not((d_23_valueOrError9_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(496,35): " + _dafny.string_of(d_23_valueOrError9_))
            d_24_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
            d_24_decryptionMaterialsIn_ = (d_23_valueOrError9_).Extract()
            d_25_valueOrError10_: Wrappers.Result = None
            out6_: Wrappers.Result
            out6_ = (d_12_recipientKmsEcdhKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_24_decryptionMaterialsIn_, _dafny.Seq([d_22_edk_])))
            d_25_valueOrError10_ = out6_
            if not(not((d_25_valueOrError10_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(503,36): " + _dafny.string_of(d_25_valueOrError10_))
            d_26_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
            d_26_decryptionMaterialsOut_ = (d_25_valueOrError10_).Extract()
            if not((((d_19_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_26_decryptionMaterialsOut_).materials).plaintextDataKey)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(510,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhRawEcdhKeyringWithDerPublicKeys():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(518,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(520,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_3_kmsClient_ = (d_2_valueOrError1_).Extract()
        hi0_ = len(default__.CURVES)
        for d_4_i_ in range(0, hi0_):
            d_5_senderKmsKey_: _dafny.Seq
            d_5_senderKmsKey_ = (default__.senderKmsKeys)[d_4_i_]
            d_6_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_6_valueOrError2_ = Base64.default__.Decode((default__.derKmsSenderPublicKeyStrings)[d_4_i_])
            if not(not((d_6_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(525,29): " + _dafny.string_of(d_6_valueOrError2_))
            d_7_senderPublicKey_: _dafny.Seq
            d_7_senderPublicKey_ = (d_6_valueOrError2_).Extract()
            d_8_valueOrError3_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
            d_8_valueOrError3_ = UTF8.default__.Encode((default__.rawEccPrivateKeys)[d_4_i_])
            if not(not((d_8_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(526,33): " + _dafny.string_of(d_8_valueOrError3_))
            d_9_recipientPrivateKey_: _dafny.Seq
            d_9_recipientPrivateKey_ = (d_8_valueOrError3_).Extract()
            d_10_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_10_valueOrError4_ = Base64.default__.Decode((default__.rawEccPublicKeysB64der)[d_4_i_])
            if not(not((d_10_valueOrError4_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(527,32): " + _dafny.string_of(d_10_valueOrError4_))
            d_11_recipientPublicKey_: _dafny.Seq
            d_11_recipientPublicKey_ = (d_10_valueOrError4_).Extract()
            d_12_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_12_curve_ = (default__.CURVES)[d_4_i_]
            d_13_valueOrError5_: Wrappers.Result = None
            out2_: Wrappers.Result
            out2_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_5_senderKmsKey_, Wrappers.Option_Some(d_7_senderPublicKey_), d_11_recipientPublicKey_)), d_12_curve_, d_3_kmsClient_, Wrappers.Option_None()))
            d_13_valueOrError5_ = out2_
            if not(not((d_13_valueOrError5_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(530,34): " + _dafny.string_of(d_13_valueOrError5_))
            d_14_senderKmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_14_senderKmsEcdhKeyring_ = (d_13_valueOrError5_).Extract()
            d_15_valueOrError6_: Wrappers.Result = None
            out3_: Wrappers.Result
            out3_ = (d_1_mpl_).CreateRawEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_9_recipientPrivateKey_, d_7_senderPublicKey_)), d_12_curve_))
            d_15_valueOrError6_ = out3_
            if not(not((d_15_valueOrError6_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(545,33): " + _dafny.string_of(d_15_valueOrError6_))
            d_16_recipientRawKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
            d_16_recipientRawKeyring_ = (d_15_valueOrError6_).Extract()
            d_17_encryptionContext_: _dafny.Map
            out4_: _dafny.Map
            out4_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
            d_17_encryptionContext_ = out4_
            d_18_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
            d_18_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
            d_19_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
            d_19_suite_ = AlgorithmSuites.default__.GetSuite(d_18_algorithmSuiteId_)
            d_20_valueOrError7_: Wrappers.Result = None
            d_20_valueOrError7_ = (d_1_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_18_algorithmSuiteId_, d_17_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
            if not(not((d_20_valueOrError7_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(561,35): " + _dafny.string_of(d_20_valueOrError7_))
            d_21_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_21_encryptionMaterialsIn_ = (d_20_valueOrError7_).Extract()
            d_22_valueOrError8_: Wrappers.Result = None
            out5_: Wrappers.Result
            out5_ = (d_14_senderKmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_21_encryptionMaterialsIn_))
            d_22_valueOrError8_ = out5_
            if not(not((d_22_valueOrError8_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(571,36): " + _dafny.string_of(d_22_valueOrError8_))
            d_23_encryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnEncryptOutput
            d_23_encryptionMaterialsOut_ = (d_22_valueOrError8_).Extract()
            d_24_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_24_valueOrError9_ = (d_1_mpl_).EncryptionMaterialsHasPlaintextDataKey((d_23_encryptionMaterialsOut_).materials)
            if not(not((d_24_valueOrError9_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(575,15): " + _dafny.string_of(d_24_valueOrError9_))
            d_25___v33_: tuple
            d_25___v33_ = (d_24_valueOrError9_).Extract()
            if not((len(((d_23_encryptionMaterialsOut_).materials).encryptedDataKeys)) == (1)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(577,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_26_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
            d_26_edk_ = (((d_23_encryptionMaterialsOut_).materials).encryptedDataKeys)[0]
            d_27_valueOrError10_: Wrappers.Result = None
            d_27_valueOrError10_ = (d_1_mpl_).InitializeDecryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(d_18_algorithmSuiteId_, d_17_encryptionContext_, _dafny.Seq([])))
            if not(not((d_27_valueOrError10_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(580,35): " + _dafny.string_of(d_27_valueOrError10_))
            d_28_decryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
            d_28_decryptionMaterialsIn_ = (d_27_valueOrError10_).Extract()
            d_29_valueOrError11_: Wrappers.Result = None
            out6_: Wrappers.Result
            out6_ = (d_16_recipientRawKeyring_).OnDecrypt(AwsCryptographyMaterialProvidersTypes.OnDecryptInput_OnDecryptInput(d_28_decryptionMaterialsIn_, _dafny.Seq([d_26_edk_])))
            d_29_valueOrError11_ = out6_
            if not(not((d_29_valueOrError11_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(587,36): " + _dafny.string_of(d_29_valueOrError11_))
            d_30_decryptionMaterialsOut_: AwsCryptographyMaterialProvidersTypes.OnDecryptOutput
            d_30_decryptionMaterialsOut_ = (d_29_valueOrError11_).Extract()
            if not((((d_23_encryptionMaterialsOut_).materials).plaintextDataKey) == (((d_30_decryptionMaterialsOut_).materials).plaintextDataKey)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(594,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhKeyringWithIncorrectCurveConfigurationFailure():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(603,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(605,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_3_kmsClient_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_4_valueOrError2_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__256__PUBLIC__KEY__S)
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(607,27): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_senderPublicKey_: _dafny.Seq
        d_5_senderPublicKey_ = (d_4_valueOrError2_).Extract()
        d_6_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_6_valueOrError3_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__256__PUBLIC__KEY__R)
        if not(not((d_6_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(608,30): " + _dafny.string_of(d_6_valueOrError3_))
        d_7_recipientPublicKey_: _dafny.Seq
        d_7_recipientPublicKey_ = (d_6_valueOrError3_).Extract()
        d_8_senderKmsEcdhKeyring_: Wrappers.Result
        out2_: Wrappers.Result
        out2_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(TestUtils.default__.KMS__ECC__256__KEY__ARN__S, Wrappers.Option_Some(d_5_senderPublicKey_), d_7_recipientPublicKey_)), default__.P384, d_3_kmsClient_, Wrappers.Option_None()))
        d_8_senderKmsEcdhKeyring_ = out2_
        if not((d_8_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(625,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsEcdhKeyringWithIncorrectCurveConfigurationCombinationsFailure():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(630,15): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_mpl_: MaterialProviders.MaterialProvidersClient
        d_1_mpl_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(632,21): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_3_kmsClient_ = (d_2_valueOrError1_).Extract()
        d_4_senderKmsKey256_: _dafny.Seq
        d_4_senderKmsKey256_ = TestUtils.default__.KMS__ECC__256__KEY__ARN__S
        d_5_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_5_valueOrError2_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__256__PUBLIC__KEY__S)
        if not(not((d_5_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(635,33): " + _dafny.string_of(d_5_valueOrError2_))
        d_6_senderPublicKey256_: _dafny.Seq
        d_6_senderPublicKey256_ = (d_5_valueOrError2_).Extract()
        d_7_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_7_valueOrError3_ = Base64.default__.Decode(TestUtils.default__.ECC__P256__PUBLIC__R)
        if not(not((d_7_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(636,33): " + _dafny.string_of(d_7_valueOrError3_))
        d_8_recipientPublicKey256_: _dafny.Seq
        d_8_recipientPublicKey256_ = (d_7_valueOrError3_).Extract()
        d_9_senderKmsKey384_: _dafny.Seq
        d_9_senderKmsKey384_ = TestUtils.default__.KMS__ECC__384__KEY__ARN__S
        d_10_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_10_valueOrError4_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__384__PUBLIC__KEY__S)
        if not(not((d_10_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(639,33): " + _dafny.string_of(d_10_valueOrError4_))
        d_11_senderPublicKey384_: _dafny.Seq
        d_11_senderPublicKey384_ = (d_10_valueOrError4_).Extract()
        d_12_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_12_valueOrError5_ = Base64.default__.Decode(TestUtils.default__.ECC__P384__PUBLIC__R)
        if not(not((d_12_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(640,33): " + _dafny.string_of(d_12_valueOrError5_))
        d_13_recipientPublicKey384_: _dafny.Seq
        d_13_recipientPublicKey384_ = (d_12_valueOrError5_).Extract()
        d_14_senderKmsKey521_: _dafny.Seq
        d_14_senderKmsKey521_ = TestUtils.default__.KMS__ECC__521__KEY__ARN__S
        d_15_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_15_valueOrError6_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__521__PUBLIC__KEY__S)
        if not(not((d_15_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(643,33): " + _dafny.string_of(d_15_valueOrError6_))
        d_16_senderPublicKey521_: _dafny.Seq
        d_16_senderPublicKey521_ = (d_15_valueOrError6_).Extract()
        d_17_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_17_valueOrError7_ = Base64.default__.Decode(TestUtils.default__.ECC__P521__PUBLIC__R)
        if not(not((d_17_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(644,33): " + _dafny.string_of(d_17_valueOrError7_))
        d_18_recipientPublicKey521_: _dafny.Seq
        d_18_recipientPublicKey521_ = (d_17_valueOrError7_).Extract()
        d_19_senderKmsEcdhKeyring_: Wrappers.Result
        out2_: Wrappers.Result
        out2_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_4_senderKmsKey256_, Wrappers.Option_Some(d_6_senderPublicKey256_), d_8_recipientPublicKey256_)), default__.P384, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out2_
        if not((d_19_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(662,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out3_: Wrappers.Result
        out3_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_4_senderKmsKey256_, Wrappers.Option_Some(d_6_senderPublicKey256_), d_8_recipientPublicKey256_)), default__.P521, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out3_
        out4_: Wrappers.Result
        out4_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_9_senderKmsKey384_, Wrappers.Option_Some(d_11_senderPublicKey384_), d_13_recipientPublicKey384_)), default__.P256, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out4_
        if not((d_19_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(694,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out5_: Wrappers.Result
        out5_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_9_senderKmsKey384_, Wrappers.Option_Some(d_11_senderPublicKey384_), d_13_recipientPublicKey384_)), default__.P521, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out5_
        out6_: Wrappers.Result
        out6_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_14_senderKmsKey521_, Wrappers.Option_Some(d_16_senderPublicKey521_), d_18_recipientPublicKey521_)), default__.P256, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out6_
        if not((d_19_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(726,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out7_: Wrappers.Result
        out7_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_14_senderKmsKey521_, Wrappers.Option_Some(d_16_senderPublicKey521_), d_18_recipientPublicKey521_)), default__.P384, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out7_
        out8_: Wrappers.Result
        out8_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_4_senderKmsKey256_, Wrappers.Option_Some(d_6_senderPublicKey256_), d_13_recipientPublicKey384_)), default__.P256, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out8_
        if not((d_19_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(759,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out9_: Wrappers.Result
        out9_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_4_senderKmsKey256_, Wrappers.Option_Some(d_6_senderPublicKey256_), d_18_recipientPublicKey521_)), default__.P256, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out9_
        if not((d_19_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(775,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out10_: Wrappers.Result
        out10_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_9_senderKmsKey384_, Wrappers.Option_Some(d_11_senderPublicKey384_), d_8_recipientPublicKey256_)), default__.P384, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out10_
        if not((d_19_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(792,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out11_: Wrappers.Result
        out11_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_9_senderKmsKey384_, Wrappers.Option_Some(d_11_senderPublicKey384_), d_18_recipientPublicKey521_)), default__.P384, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out11_
        if not((d_19_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(808,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out12_: Wrappers.Result
        out12_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_14_senderKmsKey521_, Wrappers.Option_Some(d_16_senderPublicKey521_), d_8_recipientPublicKey256_)), default__.P521, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out12_
        if not((d_19_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(825,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out13_: Wrappers.Result
        out13_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_14_senderKmsKey521_, Wrappers.Option_Some(d_16_senderPublicKey521_), d_13_recipientPublicKey384_)), default__.P521, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out13_
        if not((d_19_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(841,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out14_: Wrappers.Result
        out14_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_9_senderKmsKey384_, Wrappers.Option_Some(d_11_senderPublicKey384_), d_8_recipientPublicKey256_)), default__.P256, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out14_
        if not((d_19_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(860,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out15_: Wrappers.Result
        out15_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_14_senderKmsKey521_, Wrappers.Option_Some(d_16_senderPublicKey521_), d_8_recipientPublicKey256_)), default__.P256, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out15_
        if not((d_19_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(876,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out16_: Wrappers.Result
        out16_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_4_senderKmsKey256_, Wrappers.Option_Some(d_6_senderPublicKey256_), d_13_recipientPublicKey384_)), default__.P384, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out16_
        if not((d_19_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(893,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out17_: Wrappers.Result
        out17_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_14_senderKmsKey521_, Wrappers.Option_Some(d_16_senderPublicKey521_), d_13_recipientPublicKey384_)), default__.P384, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out17_
        if not((d_19_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(909,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out18_: Wrappers.Result
        out18_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_4_senderKmsKey256_, Wrappers.Option_Some(d_6_senderPublicKey256_), d_18_recipientPublicKey521_)), default__.P521, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out18_
        if not((d_19_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(926,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        out19_: Wrappers.Result
        out19_ = (d_1_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_9_senderKmsKey384_, Wrappers.Option_Some(d_11_senderPublicKey384_), d_18_recipientPublicKey521_)), default__.P521, d_3_kmsClient_, Wrappers.Option_None()))
        d_19_senderKmsEcdhKeyring_ = out19_
        if not((d_19_senderKmsEcdhKeyring_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(942,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestLyingKmsKey():
        d_0_senderKmsKey256_: _dafny.Seq
        d_0_senderKmsKey256_ = TestUtils.default__.KMS__ECC__256__KEY__ARN__S
        d_1_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1_valueOrError0_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__256__PUBLIC__KEY__S)
        if not(not((d_1_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(948,33): " + _dafny.string_of(d_1_valueOrError0_))
        d_2_senderPublicKey256_: _dafny.Seq
        d_2_senderPublicKey256_ = (d_1_valueOrError0_).Extract()
        d_3_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_3_valueOrError1_ = Base64.default__.Decode(TestUtils.default__.ECC__P256__PUBLIC__R)
        if not(not((d_3_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(949,33): " + _dafny.string_of(d_3_valueOrError1_))
        d_4_recipientPublicKey256_: _dafny.Seq
        d_4_recipientPublicKey256_ = (d_3_valueOrError1_).Extract()
        d_5_senderKmsKey384_: _dafny.Seq
        d_5_senderKmsKey384_ = TestUtils.default__.KMS__ECC__384__KEY__ARN__S
        d_6_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_6_valueOrError2_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__384__PUBLIC__KEY__S)
        if not(not((d_6_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(952,33): " + _dafny.string_of(d_6_valueOrError2_))
        d_7_senderPublicKey384_: _dafny.Seq
        d_7_senderPublicKey384_ = (d_6_valueOrError2_).Extract()
        d_8_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_8_valueOrError3_ = Base64.default__.Decode(TestUtils.default__.ECC__P384__PUBLIC__R)
        if not(not((d_8_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(953,33): " + _dafny.string_of(d_8_valueOrError3_))
        d_9_recipientPublicKey384_: _dafny.Seq
        d_9_recipientPublicKey384_ = (d_8_valueOrError3_).Extract()
        d_10_senderKmsKey521_: _dafny.Seq
        d_10_senderKmsKey521_ = TestUtils.default__.KMS__ECC__521__KEY__ARN__S
        d_11_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_11_valueOrError4_ = Base64.default__.Decode(TestUtils.default__.KMS__ECC__521__PUBLIC__KEY__S)
        if not(not((d_11_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(956,33): " + _dafny.string_of(d_11_valueOrError4_))
        d_12_senderPublicKey521_: _dafny.Seq
        d_12_senderPublicKey521_ = (d_11_valueOrError4_).Extract()
        d_13_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_13_valueOrError5_ = Base64.default__.Decode(TestUtils.default__.ECC__P521__PUBLIC__R)
        if not(not((d_13_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(957,33): " + _dafny.string_of(d_13_valueOrError5_))
        d_14_recipientPublicKey521_: _dafny.Seq
        d_14_recipientPublicKey521_ = (d_13_valueOrError5_).Extract()
        d_15_valueOrError6_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_15_valueOrError6_ = out0_
        if not(not((d_15_valueOrError6_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(959,15): " + _dafny.string_of(d_15_valueOrError6_))
        d_16_mpl_: MaterialProviders.MaterialProvidersClient
        d_16_mpl_ = (d_15_valueOrError6_).Extract()
        d_17_valueOrError7_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_17_valueOrError7_ = out1_
        if not(not((d_17_valueOrError7_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(961,21): " + _dafny.string_of(d_17_valueOrError7_))
        d_18_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_18_kmsClient_ = (d_17_valueOrError7_).Extract()
        d_19_encryptionContext_: _dafny.Map
        out2_: _dafny.Map
        out2_ = TestUtils.default__.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation_A())
        d_19_encryptionContext_ = out2_
        d_20_algorithmSuiteId_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId
        d_20_algorithmSuiteId_ = AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF())
        d_21_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_21_suite_ = AlgorithmSuites.default__.GetSuite(d_20_algorithmSuiteId_)
        d_22_valueOrError8_: Wrappers.Result = None
        d_22_valueOrError8_ = (d_16_mpl_).InitializeEncryptionMaterials(AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(d_20_algorithmSuiteId_, d_19_encryptionContext_, _dafny.Seq([]), Wrappers.Option_None(), Wrappers.Option_None()))
        if not(not((d_22_valueOrError8_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(967,33): " + _dafny.string_of(d_22_valueOrError8_))
        d_23_encryptionMaterialsIn_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_23_encryptionMaterialsIn_ = (d_22_valueOrError8_).Extract()
        d_24_valueOrError9_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = (d_16_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_5_senderKmsKey384_, Wrappers.Option_Some(d_2_senderPublicKey256_), d_4_recipientPublicKey256_)), default__.P256, d_18_kmsClient_, Wrappers.Option_None()))
        d_24_valueOrError9_ = out3_
        if not(not((d_24_valueOrError9_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(985,26): " + _dafny.string_of(d_24_valueOrError9_))
        d_25_kmsEcdhKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
        d_25_kmsEcdhKeyring_ = (d_24_valueOrError9_).Extract()
        d_26_encryptionMaterialsOut_: Wrappers.Result
        out4_: Wrappers.Result
        out4_ = (d_25_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_23_encryptionMaterialsIn_))
        d_26_encryptionMaterialsOut_ = out4_
        if not((d_26_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1002,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_27_valueOrError10_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = (d_16_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_10_senderKmsKey521_, Wrappers.Option_Some(d_2_senderPublicKey256_), d_4_recipientPublicKey256_)), default__.P256, d_18_kmsClient_, Wrappers.Option_None()))
        d_27_valueOrError10_ = out5_
        if not(not((d_27_valueOrError10_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1004,22): " + _dafny.string_of(d_27_valueOrError10_))
        d_25_kmsEcdhKeyring_ = (d_27_valueOrError10_).Extract()
        out6_: Wrappers.Result
        out6_ = (d_25_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_23_encryptionMaterialsIn_))
        d_26_encryptionMaterialsOut_ = out6_
        if not((d_26_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1021,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_28_valueOrError11_: Wrappers.Result = None
        out7_: Wrappers.Result
        out7_ = (d_16_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_0_senderKmsKey256_, Wrappers.Option_Some(d_7_senderPublicKey384_), d_9_recipientPublicKey384_)), default__.P384, d_18_kmsClient_, Wrappers.Option_None()))
        d_28_valueOrError11_ = out7_
        if not(not((d_28_valueOrError11_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1024,22): " + _dafny.string_of(d_28_valueOrError11_))
        d_25_kmsEcdhKeyring_ = (d_28_valueOrError11_).Extract()
        out8_: Wrappers.Result
        out8_ = (d_25_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_23_encryptionMaterialsIn_))
        d_26_encryptionMaterialsOut_ = out8_
        if not((d_26_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1041,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_29_valueOrError12_: Wrappers.Result = None
        out9_: Wrappers.Result
        out9_ = (d_16_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_10_senderKmsKey521_, Wrappers.Option_Some(d_7_senderPublicKey384_), d_9_recipientPublicKey384_)), default__.P384, d_18_kmsClient_, Wrappers.Option_None()))
        d_29_valueOrError12_ = out9_
        if not(not((d_29_valueOrError12_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1043,22): " + _dafny.string_of(d_29_valueOrError12_))
        d_25_kmsEcdhKeyring_ = (d_29_valueOrError12_).Extract()
        out10_: Wrappers.Result
        out10_ = (d_25_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_23_encryptionMaterialsIn_))
        d_26_encryptionMaterialsOut_ = out10_
        if not((d_26_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1060,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_30_valueOrError13_: Wrappers.Result = None
        out11_: Wrappers.Result
        out11_ = (d_16_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_0_senderKmsKey256_, Wrappers.Option_Some(d_12_senderPublicKey521_), d_14_recipientPublicKey521_)), default__.P521, d_18_kmsClient_, Wrappers.Option_None()))
        d_30_valueOrError13_ = out11_
        if not(not((d_30_valueOrError13_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1063,22): " + _dafny.string_of(d_30_valueOrError13_))
        d_25_kmsEcdhKeyring_ = (d_30_valueOrError13_).Extract()
        out12_: Wrappers.Result
        out12_ = (d_25_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_23_encryptionMaterialsIn_))
        d_26_encryptionMaterialsOut_ = out12_
        if not((d_26_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1080,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_31_valueOrError14_: Wrappers.Result = None
        out13_: Wrappers.Result
        out13_ = (d_16_mpl_).CreateAwsKmsEcdhKeyring(AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_5_senderKmsKey384_, Wrappers.Option_Some(d_12_senderPublicKey521_), d_14_recipientPublicKey521_)), default__.P521, d_18_kmsClient_, Wrappers.Option_None()))
        d_31_valueOrError14_ = out13_
        if not(not((d_31_valueOrError14_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1082,22): " + _dafny.string_of(d_31_valueOrError14_))
        d_25_kmsEcdhKeyring_ = (d_31_valueOrError14_).Extract()
        out14_: Wrappers.Result
        out14_ = (d_25_kmsEcdhKeyring_).OnEncrypt(AwsCryptographyMaterialProvidersTypes.OnEncryptInput_OnEncryptInput(d_23_encryptionMaterialsIn_))
        d_26_encryptionMaterialsOut_ = out14_
        if not((d_26_encryptionMaterialsOut_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/TestAwsKmsEcdhKeyring.dfy(1099,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def P256(instance):
        return AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()
    @_dafny.classproperty
    def P384(instance):
        return AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384()
    @_dafny.classproperty
    def P521(instance):
        return AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()
    @_dafny.classproperty
    def CURVES(instance):
        return _dafny.Seq([default__.P256, default__.P384, default__.P521])
    @_dafny.classproperty
    def TEST__DBE__ALG__SUITE__ID(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_DBE(AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384())
    @_dafny.classproperty
    def derKmsSenderPublicKeyStrings(instance):
        return _dafny.Seq([TestUtils.default__.KMS__ECC__256__PUBLIC__KEY__S, TestUtils.default__.KMS__ECC__384__PUBLIC__KEY__S, TestUtils.default__.KMS__ECC__521__PUBLIC__KEY__S])
    @_dafny.classproperty
    def derKmsRecipientPublicKeyStrings(instance):
        return _dafny.Seq([TestUtils.default__.KMS__ECC__256__PUBLIC__KEY__R, TestUtils.default__.KMS__ECC__384__PUBLIC__KEY__R, TestUtils.default__.KMS__ECC__521__PUBLIC__KEY__R])
    @_dafny.classproperty
    def senderKmsKeys(instance):
        return _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__S, TestUtils.default__.KMS__ECC__384__KEY__ARN__S, TestUtils.default__.KMS__ECC__521__KEY__ARN__S])
    @_dafny.classproperty
    def recipientKmsKeys(instance):
        return _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__R, TestUtils.default__.KMS__ECC__384__KEY__ARN__R, TestUtils.default__.KMS__ECC__521__KEY__ARN__R])
    @_dafny.classproperty
    def rawEccPrivateKeys(instance):
        return _dafny.Seq([TestUtils.default__.ECC__P256__PRIVATE, TestUtils.default__.ECC__P384__PRIVATE, TestUtils.default__.ECC__P521__PRIVATE])
    @_dafny.classproperty
    def rawEccPublicKeysB64der(instance):
        return _dafny.Seq([TestUtils.default__.ECC__P256__PUBLIC, TestUtils.default__.ECC__P384__PUBLIC, TestUtils.default__.ECC__P521__PUBLIC])
