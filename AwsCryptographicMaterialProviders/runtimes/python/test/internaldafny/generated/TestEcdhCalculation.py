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
import TestAwsKmsEcdhKeyring as TestAwsKmsEcdhKeyring
import TestAwsKmsEncryptedDataKeyFilter as TestAwsKmsEncryptedDataKeyFilter
import TestLocalCMC as TestLocalCMC
import TestStormTracker as TestStormTracker

# Module: TestEcdhCalculation

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestKmsDeriveSharedSecretOfflineCalculation():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(32,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(33,22): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_primitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_3_primitives_ = (d_2_valueOrError1_).Extract()
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out2_: Wrappers.Result
        out2_ = (d_3_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256()))
        d_4_valueOrError2_ = out2_
        if not(not((d_4_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(35,19): " + _dafny.string_of(d_4_valueOrError2_))
        d_5_keyPair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_5_keyPair_ = (d_4_valueOrError2_).Extract()
        if not(((1) <= (len(((d_5_keyPair_).publicKey).der))) and ((len(((d_5_keyPair_).publicKey).der)) <= (8192))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(41,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_6_kmsSharedSecret_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_1_kmsClient_).DeriveSharedSecret(ComAmazonawsKmsTypes.DeriveSharedSecretRequest_DeriveSharedSecretRequest(default__.senderKmsKey, ComAmazonawsKmsTypes.KeyAgreementAlgorithmSpec_ECDH(), ((d_5_keyPair_).publicKey).der, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
        d_6_kmsSharedSecret_ = out3_
        if not((d_6_kmsSharedSecret_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(50,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_6_kmsSharedSecret_).value).SharedSecret).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(51,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_7_publicKeyResponse_: Wrappers.Result
        out4_: Wrappers.Result
        out4_ = (d_1_kmsClient_).GetPublicKey(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest(default__.senderKmsKey, Wrappers.Option_None()))
        d_7_publicKeyResponse_ = out4_
        if not((d_7_publicKeyResponse_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(59,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        let_tmp_rhs0_ = (d_7_publicKeyResponse_).value
        d_8___v0_ = let_tmp_rhs0_.KeyId
        d_9_PublicKey_ = let_tmp_rhs0_.PublicKey
        d_10___v1_ = let_tmp_rhs0_.CustomerMasterKeySpec
        d_11___v2_ = let_tmp_rhs0_.KeySpec
        d_12___v3_ = let_tmp_rhs0_.KeyUsage
        d_13___v4_ = let_tmp_rhs0_.EncryptionAlgorithms
        d_14___v5_ = let_tmp_rhs0_.SigningAlgorithms
        d_15___v6_ = let_tmp_rhs0_.KeyAgreementAlgorithms
        if not((d_9_PublicKey_).is_Some):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_16_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.default())()
        out5_: Wrappers.Result
        out5_ = (d_3_primitives_).DeriveSharedSecret(AwsCryptographyPrimitivesTypes.DeriveSharedSecretInput_DeriveSharedSecretInput(AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), (d_5_keyPair_).privateKey, AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey((d_9_PublicKey_).value)))
        d_16_valueOrError3_ = out5_
        if not(not((d_16_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(64,31): " + _dafny.string_of(d_16_valueOrError3_))
        d_17_offlineSharedSecret_: AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
        d_17_offlineSharedSecret_ = (d_16_valueOrError3_).Extract()
        if not(((((d_6_kmsSharedSecret_).value).SharedSecret).value) == ((d_17_offlineSharedSecret_).sharedSecret)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestKmsDeriveSharedSecretOfflineCalculationCurves():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(77,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(78,22): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_primitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_3_primitives_ = (d_2_valueOrError1_).Extract()
        hi0_ = len(default__.senderArns)
        for d_4_i_ in range(0, hi0_):
            d_5_valueOrError2_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out2_: Wrappers.Result
            out2_ = (d_3_primitives_).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput((default__.curveSpecs)[d_4_i_]))
            d_5_valueOrError2_ = out2_
            if not(not((d_5_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(82,21): " + _dafny.string_of(d_5_valueOrError2_))
            d_6_keyPair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_6_keyPair_ = (d_5_valueOrError2_).Extract()
            if not(((1) <= (len(((d_6_keyPair_).publicKey).der))) and ((len(((d_6_keyPair_).publicKey).der)) <= (8192))):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(87,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_7_kmsSharedSecret_: Wrappers.Result
            out3_: Wrappers.Result
            out3_ = (d_1_kmsClient_).DeriveSharedSecret(ComAmazonawsKmsTypes.DeriveSharedSecretRequest_DeriveSharedSecretRequest((default__.senderArns)[d_4_i_], ComAmazonawsKmsTypes.KeyAgreementAlgorithmSpec_ECDH(), ((d_6_keyPair_).publicKey).der, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
            d_7_kmsSharedSecret_ = out3_
            if not((d_7_kmsSharedSecret_).is_Success):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(96,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not((((d_7_kmsSharedSecret_).value).SharedSecret).is_Some):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(97,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_8_publicKeyResponse_: Wrappers.Result
            out4_: Wrappers.Result
            out4_ = (d_1_kmsClient_).GetPublicKey(ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest((default__.senderArns)[d_4_i_], Wrappers.Option_None()))
            d_8_publicKeyResponse_ = out4_
            if not((d_8_publicKeyResponse_).is_Success):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(105,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            let_tmp_rhs0_ = (d_8_publicKeyResponse_).value
            d_9___v7_ = let_tmp_rhs0_.KeyId
            d_10_PublicKey_ = let_tmp_rhs0_.PublicKey
            d_11___v8_ = let_tmp_rhs0_.CustomerMasterKeySpec
            d_12___v9_ = let_tmp_rhs0_.KeySpec
            d_13___v10_ = let_tmp_rhs0_.KeyUsage
            d_14___v11_ = let_tmp_rhs0_.EncryptionAlgorithms
            d_15___v12_ = let_tmp_rhs0_.SigningAlgorithms
            d_16___v13_ = let_tmp_rhs0_.KeyAgreementAlgorithms
            if not((d_10_PublicKey_).is_Some):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(108,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_17_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.default())()
            out5_: Wrappers.Result
            out5_ = (d_3_primitives_).DeriveSharedSecret(AwsCryptographyPrimitivesTypes.DeriveSharedSecretInput_DeriveSharedSecretInput((default__.curveSpecs)[d_4_i_], (d_6_keyPair_).privateKey, AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey((d_10_PublicKey_).value)))
            d_17_valueOrError3_ = out5_
            if not(not((d_17_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(110,33): " + _dafny.string_of(d_17_valueOrError3_))
            d_18_offlineSharedSecret_: AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
            d_18_offlineSharedSecret_ = (d_17_valueOrError3_).Extract()
            if not(((((d_7_kmsSharedSecret_).value).SharedSecret).value) == ((d_18_offlineSharedSecret_).sharedSecret)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(118,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOfflineDeriveSharedSecretStaticKeys():
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Kms.default__.KMSClient()
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(125,21): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
        d_1_kmsClient_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(126,22): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_primitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_3_primitives_ = (d_2_valueOrError1_).Extract()
        hi0_ = len(default__.curveSpecs)
        for d_4_i_ in range(0, hi0_):
            d_5_curve_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
            d_5_curve_ = (default__.curveSpecs)[d_4_i_]
            d_6_senderArn_: _dafny.Seq
            d_6_senderArn_ = (default__.senderArns)[d_4_i_]
            d_7_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_7_valueOrError2_ = Base64.default__.Decode((default__.senderArnPublicKeys)[d_4_i_])
            if not(not((d_7_valueOrError2_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(132,29): " + _dafny.string_of(d_7_valueOrError2_))
            d_8_senderPublicKey_: _dafny.Seq
            d_8_senderPublicKey_ = (d_7_valueOrError2_).Extract()
            d_9_valueOrError3_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
            d_9_valueOrError3_ = UTF8.default__.Encode((default__.privateKeyReceivers)[d_4_i_])
            if not(not((d_9_valueOrError3_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(133,33): " + _dafny.string_of(d_9_valueOrError3_))
            d_10_recipientPrivateKey_: _dafny.Seq
            d_10_recipientPrivateKey_ = (d_9_valueOrError3_).Extract()
            d_11_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_11_valueOrError4_ = Base64.default__.Decode((default__.publicKeyReceivers)[d_4_i_])
            if not(not((d_11_valueOrError4_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(134,32): " + _dafny.string_of(d_11_valueOrError4_))
            d_12_recipientPublicKey_: _dafny.Seq
            d_12_recipientPublicKey_ = (d_11_valueOrError4_).Extract()
            d_13_kmsSharedSecret_: Wrappers.Result
            out2_: Wrappers.Result
            out2_ = (d_1_kmsClient_).DeriveSharedSecret(ComAmazonawsKmsTypes.DeriveSharedSecretRequest_DeriveSharedSecretRequest(d_6_senderArn_, ComAmazonawsKmsTypes.KeyAgreementAlgorithmSpec_ECDH(), d_12_recipientPublicKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
            d_13_kmsSharedSecret_ = out2_
            if not((d_13_kmsSharedSecret_).is_Success):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(143,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not((((d_13_kmsSharedSecret_).value).SharedSecret).is_Some):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(144,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            d_14_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.default())()
            out3_: Wrappers.Result
            out3_ = (d_3_primitives_).DeriveSharedSecret(AwsCryptographyPrimitivesTypes.DeriveSharedSecretInput_DeriveSharedSecretInput((default__.curveSpecs)[d_4_i_], AwsCryptographyPrimitivesTypes.ECCPrivateKey_ECCPrivateKey(d_10_recipientPrivateKey_), AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_8_senderPublicKey_)))
            d_14_valueOrError5_ = out3_
            if not(not((d_14_valueOrError5_).IsFailure())):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(146,33): " + _dafny.string_of(d_14_valueOrError5_))
            d_15_offlineSharedSecret_: AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
            d_15_offlineSharedSecret_ = (d_14_valueOrError5_).Extract()
            if not(((((d_13_kmsSharedSecret_).value).SharedSecret).value) == ((d_15_offlineSharedSecret_).sharedSecret)):
                raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestEcdhCalculation.dfy(155,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def senderKmsKey(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/eabdf483-6be2-4d2d-8ee4-8c2583d416e9")
    @_dafny.classproperty
    def senderArns(instance):
        return _dafny.Seq([TestUtils.default__.KMS__ECC__256__KEY__ARN__S, TestUtils.default__.KMS__ECC__384__KEY__ARN__S, TestUtils.default__.KMS__ECC__521__KEY__ARN__S])
    @_dafny.classproperty
    def curveSpecs(instance):
        return _dafny.Seq([AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384(), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()])
    @_dafny.classproperty
    def senderArnPublicKeys(instance):
        return _dafny.Seq([TestUtils.default__.KMS__ECC__256__PUBLIC__KEY__S, TestUtils.default__.KMS__ECC__384__PUBLIC__KEY__S, TestUtils.default__.KMS__ECC__521__PUBLIC__KEY__S])
    @_dafny.classproperty
    def privateKeyReceivers(instance):
        return _dafny.Seq([TestUtils.default__.ECC__P256__PRIVATE, TestUtils.default__.ECC__P384__PRIVATE, TestUtils.default__.ECC__P521__PRIVATE])
    @_dafny.classproperty
    def publicKeyReceivers(instance):
        return _dafny.Seq([TestUtils.default__.ECC__P256__PUBLIC, TestUtils.default__.ECC__P384__PUBLIC, TestUtils.default__.ECC__P521__PUBLIC])
    @_dafny.classproperty
    def recipientKmsKey(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/0265c8e9-5b6a-4055-8f70-63719e09fda5")
