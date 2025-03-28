import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_material_providers.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_Sequence as StandardLibrary_Sequence
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
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
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
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
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
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
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext

# Module: IntermediateKeyWrapping

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IntermediateUnwrap(unwrap, wrappedMaterial, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_0_maybeCrypto_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_0_maybeCrypto_ = out0_
        d_1_valueOrError0_: Wrappers.Result = None
        def lambda0_(d_2_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_2_e_)

        d_1_valueOrError0_ = (d_0_maybeCrypto_).MapFailure(lambda0_)
        if (d_1_valueOrError0_).IsFailure():
            res = (d_1_valueOrError0_).PropagateFailure()
            return res
        d_3_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_3_cryptoPrimitivesX_ = (d_1_valueOrError0_).Extract()
        d_4_cryptoPrimitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_4_cryptoPrimitives_ = d_3_cryptoPrimitivesX_
        d_5_valueOrError1_: Wrappers.Result = Wrappers.Result.default(DeserializedIntermediateWrappedMaterial.default())()
        d_5_valueOrError1_ = default__.DeserializeIntermediateWrappedMaterial(wrappedMaterial, algorithmSuite)
        if (d_5_valueOrError1_).IsFailure():
            res = (d_5_valueOrError1_).PropagateFailure()
            return res
        d_6_deserializedWrapped_: DeserializedIntermediateWrappedMaterial
        d_6_deserializedWrapped_ = (d_5_valueOrError1_).Extract()
        let_tmp_rhs0_ = d_6_deserializedWrapped_
        d_7_encryptedPdk_ = let_tmp_rhs0_.encryptedPdk
        d_8_providerWrappedIkm_ = let_tmp_rhs0_.providerWrappedIkm
        d_9_valueOrError2_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = (unwrap).Invoke(MaterialWrapping.UnwrapInput_UnwrapInput(d_8_providerWrappedIkm_, algorithmSuite, encryptionContext))
        d_9_valueOrError2_ = out1_
        if (d_9_valueOrError2_).IsFailure():
            res = (d_9_valueOrError2_).PropagateFailure()
            return res
        d_10_unwrapOutput_: MaterialWrapping.UnwrapOutput
        d_10_unwrapOutput_ = (d_9_valueOrError2_).Extract()
        let_tmp_rhs1_ = d_10_unwrapOutput_
        d_11_intermediateMaterial_ = let_tmp_rhs1_.unwrappedMaterial
        d_12_unwrapInfo_ = let_tmp_rhs1_.unwrapInfo
        d_13_valueOrError3_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out2_: Wrappers.Result
        out2_ = default__.DeriveKeysFromIntermediateMaterial(d_11_intermediateMaterial_, algorithmSuite, encryptionContext, d_4_cryptoPrimitives_)
        d_13_valueOrError3_ = out2_
        if (d_13_valueOrError3_).IsFailure():
            res = (d_13_valueOrError3_).PropagateFailure()
            return res
        d_14_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_14_derivedKeys_ = (d_13_valueOrError3_).Extract()
        let_tmp_rhs2_ = d_14_derivedKeys_
        d_15_pdkEncryptionKey_ = let_tmp_rhs2_.pdkEncryptionKey
        d_16_symmetricSigningKey_ = let_tmp_rhs2_.symmetricSigningKey
        d_17_iv_: _dafny.Seq
        d_17_iv_ = _dafny.Seq([0 for d_18___v0_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_19_tagIndex_: int
        d_19_tagIndex_ = (len(d_7_encryptedPdk_)) - (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))
        d_20_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_20_valueOrError4_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_20_valueOrError4_).IsFailure():
            res = (d_20_valueOrError4_).PropagateFailure()
            return res
        d_21_aad_: _dafny.Seq
        d_21_aad_ = (d_20_valueOrError4_).Extract()
        d_22_decInput_: AwsCryptographyPrimitivesTypes.AESDecryptInput
        d_22_decInput_ = AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput(((algorithmSuite).encrypt).AES__GCM, d_15_pdkEncryptionKey_, _dafny.Seq((d_7_encryptedPdk_)[:d_19_tagIndex_:]), _dafny.Seq((d_7_encryptedPdk_)[d_19_tagIndex_::]), d_17_iv_, d_21_aad_)
        d_23_decOutR_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_4_cryptoPrimitives_).AESDecrypt(d_22_decInput_)
        d_23_decOutR_ = out3_
        d_24_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda1_(d_25_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_25_e_)

        d_24_valueOrError5_ = (d_23_decOutR_).MapFailure(lambda1_)
        if (d_24_valueOrError5_).IsFailure():
            res = (d_24_valueOrError5_).PropagateFailure()
            return res
        d_26_plaintextDataKey_: _dafny.Seq
        d_26_plaintextDataKey_ = (d_24_valueOrError5_).Extract()
        d_27_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_27_valueOrError6_ = Wrappers.default__.Need((len(d_26_plaintextDataKey_)) == (AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Decrypt length")))
        if (d_27_valueOrError6_).IsFailure():
            res = (d_27_valueOrError6_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(IntermediateUnwrapOutput_IntermediateUnwrapOutput(d_26_plaintextDataKey_, d_16_symmetricSigningKey_, d_12_unwrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateWrap(generateAndWrap, plaintextDataKey, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_0_maybeCrypto_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_0_maybeCrypto_ = out0_
        d_1_valueOrError0_: Wrappers.Result = None
        def lambda0_(d_2_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_2_e_)

        d_1_valueOrError0_ = (d_0_maybeCrypto_).MapFailure(lambda0_)
        if (d_1_valueOrError0_).IsFailure():
            res = (d_1_valueOrError0_).PropagateFailure()
            return res
        d_3_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_3_cryptoPrimitivesX_ = (d_1_valueOrError0_).Extract()
        d_4_cryptoPrimitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_4_cryptoPrimitives_ = d_3_cryptoPrimitivesX_
        d_5_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = (generateAndWrap).Invoke(MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput(algorithmSuite, encryptionContext))
        d_5_valueOrError1_ = out1_
        if (d_5_valueOrError1_).IsFailure():
            res = (d_5_valueOrError1_).PropagateFailure()
            return res
        d_6_generateAndWrapOutput_: MaterialWrapping.GenerateAndWrapOutput
        d_6_generateAndWrapOutput_ = (d_5_valueOrError1_).Extract()
        let_tmp_rhs0_ = d_6_generateAndWrapOutput_
        d_7_intermediateMaterial_ = let_tmp_rhs0_.plaintextMaterial
        d_8_providerWrappedIkm_ = let_tmp_rhs0_.wrappedMaterial
        d_9_wrapInfo_ = let_tmp_rhs0_.wrapInfo
        d_10_valueOrError2_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out2_: Wrappers.Result
        out2_ = default__.DeriveKeysFromIntermediateMaterial(d_7_intermediateMaterial_, algorithmSuite, encryptionContext, d_4_cryptoPrimitives_)
        d_10_valueOrError2_ = out2_
        if (d_10_valueOrError2_).IsFailure():
            res = (d_10_valueOrError2_).PropagateFailure()
            return res
        d_11_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_11_derivedKeys_ = (d_10_valueOrError2_).Extract()
        let_tmp_rhs1_ = d_11_derivedKeys_
        d_12_pdkEncryptionKey_ = let_tmp_rhs1_.pdkEncryptionKey
        d_13_symmetricSigningKey_ = let_tmp_rhs1_.symmetricSigningKey
        d_14_iv_: _dafny.Seq
        d_14_iv_ = _dafny.Seq([0 for d_15___v1_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_16_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_16_valueOrError3_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_16_valueOrError3_).IsFailure():
            res = (d_16_valueOrError3_).PropagateFailure()
            return res
        d_17_aad_: _dafny.Seq
        d_17_aad_ = (d_16_valueOrError3_).Extract()
        d_18_encInput_: AwsCryptographyPrimitivesTypes.AESEncryptInput
        d_18_encInput_ = AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput(((algorithmSuite).encrypt).AES__GCM, d_14_iv_, d_12_pdkEncryptionKey_, plaintextDataKey, d_17_aad_)
        d_19_encOutR_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_4_cryptoPrimitives_).AESEncrypt(d_18_encInput_)
        d_19_encOutR_ = out3_
        d_20_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        def lambda1_(d_21_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_21_e_)

        d_20_valueOrError4_ = (d_19_encOutR_).MapFailure(lambda1_)
        if (d_20_valueOrError4_).IsFailure():
            res = (d_20_valueOrError4_).PropagateFailure()
            return res
        d_22_encryptedPdk_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_22_encryptedPdk_ = (d_20_valueOrError4_).Extract()
        d_23_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_23_valueOrError5_ = Wrappers.default__.Need((len(((d_22_encryptedPdk_).cipherText) + ((d_22_encryptedPdk_).authTag))) == ((AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Encrypt length")))
        if (d_23_valueOrError5_).IsFailure():
            res = (d_23_valueOrError5_).PropagateFailure()
            return res
        d_24_serializedMaterial_: _dafny.Seq
        d_24_serializedMaterial_ = (((d_22_encryptedPdk_).cipherText) + ((d_22_encryptedPdk_).authTag)) + (d_8_providerWrappedIkm_)
        res = Wrappers.Result_Success(IntermediateWrapOutput_IntermediateWrapOutput(d_24_serializedMaterial_, d_13_symmetricSigningKey_, d_9_wrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateGenerateAndWrap(generateAndWrap, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_0_maybeCrypto_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_0_maybeCrypto_ = out0_
        d_1_valueOrError0_: Wrappers.Result = None
        def lambda0_(d_2_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_2_e_)

        d_1_valueOrError0_ = (d_0_maybeCrypto_).MapFailure(lambda0_)
        if (d_1_valueOrError0_).IsFailure():
            res = (d_1_valueOrError0_).PropagateFailure()
            return res
        d_3_cryptoPrimitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_3_cryptoPrimitives_ = (d_1_valueOrError0_).Extract()
        d_4_generateBytesResult_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = (d_3_cryptoPrimitives_).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)))
        d_4_generateBytesResult_ = out1_
        d_5_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda1_(d_6_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_6_e_)

        d_5_valueOrError1_ = (d_4_generateBytesResult_).MapFailure(lambda1_)
        if (d_5_valueOrError1_).IsFailure():
            res = (d_5_valueOrError1_).PropagateFailure()
            return res
        d_7_plaintextDataKey_: _dafny.Seq
        d_7_plaintextDataKey_ = (d_5_valueOrError1_).Extract()
        d_8_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = default__.IntermediateWrap(generateAndWrap, d_7_plaintextDataKey_, algorithmSuite, encryptionContext)
        d_8_valueOrError2_ = out2_
        if (d_8_valueOrError2_).IsFailure():
            res = (d_8_valueOrError2_).PropagateFailure()
            return res
        d_9_wrapOutput_: IntermediateWrapOutput
        d_9_wrapOutput_ = (d_8_valueOrError2_).Extract()
        res = Wrappers.Result_Success(IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput(d_7_plaintextDataKey_, (d_9_wrapOutput_).wrappedMaterial, (d_9_wrapOutput_).symmetricSigningKey, (d_9_wrapOutput_).wrapInfo))
        return res
        return res

    @staticmethod
    def DeserializeIntermediateWrappedMaterial(material, algSuite):
        d_0_valueOrError0_ = Wrappers.default__.Need((len(material)) >= ((AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to deserialize Intermediate Key Wrapped material: too short.")))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_encryptedPdkLen_ = (AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))
            return Wrappers.Result_Success(DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial(_dafny.Seq((material)[:d_1_encryptedPdkLen_:]), _dafny.Seq((material)[d_1_encryptedPdkLen_::])))

    @staticmethod
    def DeriveKeysFromIntermediateMaterial(intermediateMaterial, algorithmSuite, encryptionContext, cryptoPrimitives):
        res: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        d_0_hkdfExtractInput_: AwsCryptographyPrimitivesTypes.HkdfExtractInput
        d_0_hkdfExtractInput_ = AwsCryptographyPrimitivesTypes.HkdfExtractInput_HkdfExtractInput((((algorithmSuite).commitment).HKDF).hmac, Wrappers.Option_None(), intermediateMaterial)
        d_1_maybePseudoRandomKey_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (cryptoPrimitives).HkdfExtract(d_0_hkdfExtractInput_)
        d_1_maybePseudoRandomKey_ = out0_
        d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_3_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_3_e_)

        d_2_valueOrError0_ = (d_1_maybePseudoRandomKey_).MapFailure(lambda0_)
        if (d_2_valueOrError0_).IsFailure():
            res = (d_2_valueOrError0_).PropagateFailure()
            return res
        d_4_pseudoRandomKey_: _dafny.Seq
        d_4_pseudoRandomKey_ = (d_2_valueOrError0_).Extract()
        d_5_symmetricSigningKeyInput_: AwsCryptographyPrimitivesTypes.HkdfExpandInput
        d_5_symmetricSigningKeyInput_ = AwsCryptographyPrimitivesTypes.HkdfExpandInput_HkdfExpandInput((((algorithmSuite).commitment).HKDF).hmac, d_4_pseudoRandomKey_, default__.KEYWRAP__MAC__INFO, (((algorithmSuite).commitment).HKDF).outputKeyLength)
        d_6_pdkEncryptionKeyInput_: AwsCryptographyPrimitivesTypes.HkdfExpandInput
        d_7_dt__update__tmp_h0_ = d_5_symmetricSigningKeyInput_
        d_8_dt__update_hinfo_h0_ = default__.KEYWRAP__ENC__INFO
        d_6_pdkEncryptionKeyInput_ = AwsCryptographyPrimitivesTypes.HkdfExpandInput_HkdfExpandInput((d_7_dt__update__tmp_h0_).digestAlgorithm, (d_7_dt__update__tmp_h0_).prk, d_8_dt__update_hinfo_h0_, (d_7_dt__update__tmp_h0_).expectedLength)
        d_9_maybeSymmetricSigningKey_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = (cryptoPrimitives).HkdfExpand(d_5_symmetricSigningKeyInput_)
        d_9_maybeSymmetricSigningKey_ = out1_
        d_10_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda1_(d_11_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_11_e_)

        d_10_valueOrError1_ = (d_9_maybeSymmetricSigningKey_).MapFailure(lambda1_)
        if (d_10_valueOrError1_).IsFailure():
            res = (d_10_valueOrError1_).PropagateFailure()
            return res
        d_12_symmetricSigningKey_: _dafny.Seq
        d_12_symmetricSigningKey_ = (d_10_valueOrError1_).Extract()
        d_13_maybePdkEncryptionKey_: Wrappers.Result
        out2_: Wrappers.Result
        out2_ = (cryptoPrimitives).HkdfExpand(d_6_pdkEncryptionKeyInput_)
        d_13_maybePdkEncryptionKey_ = out2_
        d_14_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda2_(d_15_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_15_e_)

        d_14_valueOrError2_ = (d_13_maybePdkEncryptionKey_).MapFailure(lambda2_)
        if (d_14_valueOrError2_).IsFailure():
            res = (d_14_valueOrError2_).PropagateFailure()
            return res
        d_16_pdkEncryptionKey_: _dafny.Seq
        d_16_pdkEncryptionKey_ = (d_14_valueOrError2_).Extract()
        res = Wrappers.Result_Success(PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys(d_16_pdkEncryptionKey_, d_12_symmetricSigningKey_))
        return res
        return res

    @_dafny.classproperty
    def KEYWRAP__MAC__INFO(instance):
        return UTF8.default__.EncodeAscii(_dafny.Seq("AWS_MPL_INTERMEDIATE_KEYWRAP_MAC"))
    @_dafny.classproperty
    def KEYWRAP__ENC__INFO(instance):
        return UTF8.default__.EncodeAscii(_dafny.Seq("AWS_MPL_INTERMEDIATE_KEYWRAP_ENC"))

class IntermediateUnwrapOutput:
    @classmethod
    def default(cls, default_T):
        return lambda: IntermediateUnwrapOutput_IntermediateUnwrapOutput(_dafny.Seq({}), _dafny.Seq({}), default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_IntermediateUnwrapOutput(self) -> bool:
        return isinstance(self, IntermediateUnwrapOutput_IntermediateUnwrapOutput)

class IntermediateUnwrapOutput_IntermediateUnwrapOutput(IntermediateUnwrapOutput, NamedTuple('IntermediateUnwrapOutput', [('plaintextDataKey', Any), ('symmetricSigningKey', Any), ('unwrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'IntermediateKeyWrapping.IntermediateUnwrapOutput.IntermediateUnwrapOutput({_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.unwrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, IntermediateUnwrapOutput_IntermediateUnwrapOutput) and self.plaintextDataKey == __o.plaintextDataKey and self.symmetricSigningKey == __o.symmetricSigningKey and self.unwrapInfo == __o.unwrapInfo
    def __hash__(self) -> int:
        return super().__hash__()


class IntermediateGenerateAndWrapOutput:
    @classmethod
    def default(cls, default_T):
        return lambda: IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput(_dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}), default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_IntermediateGenerateAndWrapOutput(self) -> bool:
        return isinstance(self, IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput)

class IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput(IntermediateGenerateAndWrapOutput, NamedTuple('IntermediateGenerateAndWrapOutput', [('plaintextDataKey', Any), ('wrappedMaterial', Any), ('symmetricSigningKey', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput.IntermediateGenerateAndWrapOutput({_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput) and self.plaintextDataKey == __o.plaintextDataKey and self.wrappedMaterial == __o.wrappedMaterial and self.symmetricSigningKey == __o.symmetricSigningKey and self.wrapInfo == __o.wrapInfo
    def __hash__(self) -> int:
        return super().__hash__()


class IntermediateWrapOutput:
    @classmethod
    def default(cls, default_T):
        return lambda: IntermediateWrapOutput_IntermediateWrapOutput(_dafny.Seq({}), _dafny.Seq({}), default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_IntermediateWrapOutput(self) -> bool:
        return isinstance(self, IntermediateWrapOutput_IntermediateWrapOutput)

class IntermediateWrapOutput_IntermediateWrapOutput(IntermediateWrapOutput, NamedTuple('IntermediateWrapOutput', [('wrappedMaterial', Any), ('symmetricSigningKey', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'IntermediateKeyWrapping.IntermediateWrapOutput.IntermediateWrapOutput({_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, IntermediateWrapOutput_IntermediateWrapOutput) and self.wrappedMaterial == __o.wrappedMaterial and self.symmetricSigningKey == __o.symmetricSigningKey and self.wrapInfo == __o.wrapInfo
    def __hash__(self) -> int:
        return super().__hash__()


class DeserializedIntermediateWrappedMaterial:
    @classmethod
    def default(cls, ):
        return lambda: DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial(_dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeserializedIntermediateWrappedMaterial(self) -> bool:
        return isinstance(self, DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial)

class DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial(DeserializedIntermediateWrappedMaterial, NamedTuple('DeserializedIntermediateWrappedMaterial', [('encryptedPdk', Any), ('providerWrappedIkm', Any)])):
    def __dafnystr__(self) -> str:
        return f'IntermediateKeyWrapping.DeserializedIntermediateWrappedMaterial.DeserializedIntermediateWrappedMaterial({_dafny.string_of(self.encryptedPdk)}, {_dafny.string_of(self.providerWrappedIkm)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial) and self.encryptedPdk == __o.encryptedPdk and self.providerWrappedIkm == __o.providerWrappedIkm
    def __hash__(self) -> int:
        return super().__hash__()


class PdkEncryptionAndSymmetricSigningKeys:
    @classmethod
    def default(cls, ):
        return lambda: PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys(_dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PdkEncryptionAndSymmetricSigningKeys(self) -> bool:
        return isinstance(self, PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys)

class PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys(PdkEncryptionAndSymmetricSigningKeys, NamedTuple('PdkEncryptionAndSymmetricSigningKeys', [('pdkEncryptionKey', Any), ('symmetricSigningKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys.PdkEncryptionAndSymmetricSigningKeys({_dafny.string_of(self.pdkEncryptionKey)}, {_dafny.string_of(self.symmetricSigningKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys) and self.pdkEncryptionKey == __o.pdkEncryptionKey and self.symmetricSigningKey == __o.symmetricSigningKey
    def __hash__(self) -> int:
        return super().__hash__()

