import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_materialproviders.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
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
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
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
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
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
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext

# Module: IntermediateKeyWrapping

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IntermediateUnwrap(unwrap, wrappedMaterial, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_439_maybeCrypto_: Wrappers.Result
        out64_: Wrappers.Result
        out64_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_439_maybeCrypto_ = out64_
        d_440_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_441_valueOrError0_: Wrappers.Result = None
        def lambda48_(d_442_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_442_e_)

        d_441_valueOrError0_ = (d_439_maybeCrypto_).MapFailure(lambda48_)
        if (d_441_valueOrError0_).IsFailure():
            res = (d_441_valueOrError0_).PropagateFailure()
            return res
        d_440_cryptoPrimitivesX_ = (d_441_valueOrError0_).Extract()
        d_443_cryptoPrimitives_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_443_cryptoPrimitives_ = d_440_cryptoPrimitivesX_
        d_444_deserializedWrapped_: DeserializedIntermediateWrappedMaterial
        d_445_valueOrError1_: Wrappers.Result = Wrappers.Result.default(DeserializedIntermediateWrappedMaterial.default())()
        d_445_valueOrError1_ = default__.DeserializeIntermediateWrappedMaterial(wrappedMaterial, algorithmSuite)
        if (d_445_valueOrError1_).IsFailure():
            res = (d_445_valueOrError1_).PropagateFailure()
            return res
        d_444_deserializedWrapped_ = (d_445_valueOrError1_).Extract()
        let_tmp_rhs0_ = d_444_deserializedWrapped_
        d_446_encryptedPdk_ = let_tmp_rhs0_.encryptedPdk
        d_447_providerWrappedIkm_ = let_tmp_rhs0_.providerWrappedIkm
        d_448_unwrapOutput_: MaterialWrapping.UnwrapOutput
        d_449_valueOrError2_: Wrappers.Result = None
        out65_: Wrappers.Result
        out65_ = (unwrap).Invoke(MaterialWrapping.UnwrapInput_UnwrapInput(d_447_providerWrappedIkm_, algorithmSuite, encryptionContext))
        d_449_valueOrError2_ = out65_
        if (d_449_valueOrError2_).IsFailure():
            res = (d_449_valueOrError2_).PropagateFailure()
            return res
        d_448_unwrapOutput_ = (d_449_valueOrError2_).Extract()
        let_tmp_rhs1_ = d_448_unwrapOutput_
        d_450_intermediateMaterial_ = let_tmp_rhs1_.unwrappedMaterial
        d_451_unwrapInfo_ = let_tmp_rhs1_.unwrapInfo
        d_452_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_453_valueOrError3_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out66_: Wrappers.Result
        out66_ = default__.DeriveKeysFromIntermediateMaterial(d_450_intermediateMaterial_, algorithmSuite, encryptionContext, d_443_cryptoPrimitives_)
        d_453_valueOrError3_ = out66_
        if (d_453_valueOrError3_).IsFailure():
            res = (d_453_valueOrError3_).PropagateFailure()
            return res
        d_452_derivedKeys_ = (d_453_valueOrError3_).Extract()
        let_tmp_rhs2_ = d_452_derivedKeys_
        d_454_pdkEncryptionKey_ = let_tmp_rhs2_.pdkEncryptionKey
        d_455_symmetricSigningKey_ = let_tmp_rhs2_.symmetricSigningKey
        d_456_iv_: _dafny.Seq
        d_456_iv_ = _dafny.Seq([0 for d_457___v0_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_458_tagIndex_: int
        d_458_tagIndex_ = (len(d_446_encryptedPdk_)) - (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))
        d_459_aad_: _dafny.Seq
        d_460_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_460_valueOrError4_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_460_valueOrError4_).IsFailure():
            res = (d_460_valueOrError4_).PropagateFailure()
            return res
        d_459_aad_ = (d_460_valueOrError4_).Extract()
        d_461_decInput_: AwsCryptographyPrimitivesTypes.AESDecryptInput
        d_461_decInput_ = AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput(((algorithmSuite).encrypt).AES__GCM, d_454_pdkEncryptionKey_, _dafny.Seq((d_446_encryptedPdk_)[:d_458_tagIndex_:]), _dafny.Seq((d_446_encryptedPdk_)[d_458_tagIndex_::]), d_456_iv_, d_459_aad_)
        d_462_decOutR_: Wrappers.Result
        out67_: Wrappers.Result
        out67_ = (d_443_cryptoPrimitives_).AESDecrypt(d_461_decInput_)
        d_462_decOutR_ = out67_
        d_463_plaintextDataKey_: _dafny.Seq
        d_464_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda49_(d_465_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_465_e_)

        d_464_valueOrError5_ = (d_462_decOutR_).MapFailure(lambda49_)
        if (d_464_valueOrError5_).IsFailure():
            res = (d_464_valueOrError5_).PropagateFailure()
            return res
        d_463_plaintextDataKey_ = (d_464_valueOrError5_).Extract()
        d_466_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_466_valueOrError6_ = Wrappers.default__.Need((len(d_463_plaintextDataKey_)) == (AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Decrypt length")))
        if (d_466_valueOrError6_).IsFailure():
            res = (d_466_valueOrError6_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(IntermediateUnwrapOutput_IntermediateUnwrapOutput(d_463_plaintextDataKey_, d_455_symmetricSigningKey_, d_451_unwrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateWrap(generateAndWrap, plaintextDataKey, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_467_maybeCrypto_: Wrappers.Result
        out68_: Wrappers.Result
        out68_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_467_maybeCrypto_ = out68_
        d_468_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_469_valueOrError0_: Wrappers.Result = None
        def lambda50_(d_470_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_470_e_)

        d_469_valueOrError0_ = (d_467_maybeCrypto_).MapFailure(lambda50_)
        if (d_469_valueOrError0_).IsFailure():
            res = (d_469_valueOrError0_).PropagateFailure()
            return res
        d_468_cryptoPrimitivesX_ = (d_469_valueOrError0_).Extract()
        d_471_cryptoPrimitives_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_471_cryptoPrimitives_ = d_468_cryptoPrimitivesX_
        d_472_generateAndWrapOutput_: MaterialWrapping.GenerateAndWrapOutput
        d_473_valueOrError1_: Wrappers.Result = None
        out69_: Wrappers.Result
        out69_ = (generateAndWrap).Invoke(MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput(algorithmSuite, encryptionContext))
        d_473_valueOrError1_ = out69_
        if (d_473_valueOrError1_).IsFailure():
            res = (d_473_valueOrError1_).PropagateFailure()
            return res
        d_472_generateAndWrapOutput_ = (d_473_valueOrError1_).Extract()
        let_tmp_rhs3_ = d_472_generateAndWrapOutput_
        d_474_intermediateMaterial_ = let_tmp_rhs3_.plaintextMaterial
        d_475_providerWrappedIkm_ = let_tmp_rhs3_.wrappedMaterial
        d_476_wrapInfo_ = let_tmp_rhs3_.wrapInfo
        d_477_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_478_valueOrError2_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out70_: Wrappers.Result
        out70_ = default__.DeriveKeysFromIntermediateMaterial(d_474_intermediateMaterial_, algorithmSuite, encryptionContext, d_471_cryptoPrimitives_)
        d_478_valueOrError2_ = out70_
        if (d_478_valueOrError2_).IsFailure():
            res = (d_478_valueOrError2_).PropagateFailure()
            return res
        d_477_derivedKeys_ = (d_478_valueOrError2_).Extract()
        let_tmp_rhs4_ = d_477_derivedKeys_
        d_479_pdkEncryptionKey_ = let_tmp_rhs4_.pdkEncryptionKey
        d_480_symmetricSigningKey_ = let_tmp_rhs4_.symmetricSigningKey
        d_481_iv_: _dafny.Seq
        d_481_iv_ = _dafny.Seq([0 for d_482___v1_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_483_aad_: _dafny.Seq
        d_484_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_484_valueOrError3_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_484_valueOrError3_).IsFailure():
            res = (d_484_valueOrError3_).PropagateFailure()
            return res
        d_483_aad_ = (d_484_valueOrError3_).Extract()
        d_485_encInput_: AwsCryptographyPrimitivesTypes.AESEncryptInput
        d_485_encInput_ = AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput(((algorithmSuite).encrypt).AES__GCM, d_481_iv_, d_479_pdkEncryptionKey_, plaintextDataKey, d_483_aad_)
        d_486_encOutR_: Wrappers.Result
        out71_: Wrappers.Result
        out71_ = (d_471_cryptoPrimitives_).AESEncrypt(d_485_encInput_)
        d_486_encOutR_ = out71_
        d_487_encryptedPdk_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_488_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        def lambda51_(d_489_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_489_e_)

        d_488_valueOrError4_ = (d_486_encOutR_).MapFailure(lambda51_)
        if (d_488_valueOrError4_).IsFailure():
            res = (d_488_valueOrError4_).PropagateFailure()
            return res
        d_487_encryptedPdk_ = (d_488_valueOrError4_).Extract()
        d_490_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_490_valueOrError5_ = Wrappers.default__.Need((len(((d_487_encryptedPdk_).cipherText) + ((d_487_encryptedPdk_).authTag))) == ((AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Encrypt length")))
        if (d_490_valueOrError5_).IsFailure():
            res = (d_490_valueOrError5_).PropagateFailure()
            return res
        d_491_serializedMaterial_: _dafny.Seq
        d_491_serializedMaterial_ = (((d_487_encryptedPdk_).cipherText) + ((d_487_encryptedPdk_).authTag)) + (d_475_providerWrappedIkm_)
        res = Wrappers.Result_Success(IntermediateWrapOutput_IntermediateWrapOutput(d_491_serializedMaterial_, d_480_symmetricSigningKey_, d_476_wrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateGenerateAndWrap(generateAndWrap, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_492_maybeCrypto_: Wrappers.Result
        out72_: Wrappers.Result
        out72_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_492_maybeCrypto_ = out72_
        d_493_cryptoPrimitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_494_valueOrError0_: Wrappers.Result = None
        def lambda52_(d_495_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_495_e_)

        d_494_valueOrError0_ = (d_492_maybeCrypto_).MapFailure(lambda52_)
        if (d_494_valueOrError0_).IsFailure():
            res = (d_494_valueOrError0_).PropagateFailure()
            return res
        d_493_cryptoPrimitives_ = (d_494_valueOrError0_).Extract()
        d_496_generateBytesResult_: Wrappers.Result
        out73_: Wrappers.Result
        out73_ = (d_493_cryptoPrimitives_).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)))
        d_496_generateBytesResult_ = out73_
        d_497_plaintextDataKey_: _dafny.Seq
        d_498_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda53_(d_499_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_499_e_)

        d_498_valueOrError1_ = (d_496_generateBytesResult_).MapFailure(lambda53_)
        if (d_498_valueOrError1_).IsFailure():
            res = (d_498_valueOrError1_).PropagateFailure()
            return res
        d_497_plaintextDataKey_ = (d_498_valueOrError1_).Extract()
        d_500_wrapOutput_: IntermediateWrapOutput
        d_501_valueOrError2_: Wrappers.Result = None
        out74_: Wrappers.Result
        out74_ = default__.IntermediateWrap(generateAndWrap, d_497_plaintextDataKey_, algorithmSuite, encryptionContext)
        d_501_valueOrError2_ = out74_
        if (d_501_valueOrError2_).IsFailure():
            res = (d_501_valueOrError2_).PropagateFailure()
            return res
        d_500_wrapOutput_ = (d_501_valueOrError2_).Extract()
        res = Wrappers.Result_Success(IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput(d_497_plaintextDataKey_, (d_500_wrapOutput_).wrappedMaterial, (d_500_wrapOutput_).symmetricSigningKey, (d_500_wrapOutput_).wrapInfo))
        return res
        return res

    @staticmethod
    def DeserializeIntermediateWrappedMaterial(material, algSuite):
        d_502_valueOrError0_ = Wrappers.default__.Need((len(material)) >= ((AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to deserialize Intermediate Key Wrapped material: too short.")))
        if (d_502_valueOrError0_).IsFailure():
            return (d_502_valueOrError0_).PropagateFailure()
        elif True:
            d_503_encryptedPdkLen_ = (AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))
            return Wrappers.Result_Success(DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial(_dafny.Seq((material)[:d_503_encryptedPdkLen_:]), _dafny.Seq((material)[d_503_encryptedPdkLen_::])))

    @staticmethod
    def DeriveKeysFromIntermediateMaterial(intermediateMaterial, algorithmSuite, encryptionContext, cryptoPrimitives):
        res: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        d_504_hkdfExtractInput_: AwsCryptographyPrimitivesTypes.HkdfExtractInput
        d_504_hkdfExtractInput_ = AwsCryptographyPrimitivesTypes.HkdfExtractInput_HkdfExtractInput((((algorithmSuite).commitment).HKDF).hmac, Wrappers.Option_None(), intermediateMaterial)
        d_505_maybePseudoRandomKey_: Wrappers.Result
        out75_: Wrappers.Result
        out75_ = (cryptoPrimitives).HkdfExtract(d_504_hkdfExtractInput_)
        d_505_maybePseudoRandomKey_ = out75_
        d_506_pseudoRandomKey_: _dafny.Seq
        d_507_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda54_(d_508_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_508_e_)

        d_507_valueOrError0_ = (d_505_maybePseudoRandomKey_).MapFailure(lambda54_)
        if (d_507_valueOrError0_).IsFailure():
            res = (d_507_valueOrError0_).PropagateFailure()
            return res
        d_506_pseudoRandomKey_ = (d_507_valueOrError0_).Extract()
        d_509_symmetricSigningKeyInput_: AwsCryptographyPrimitivesTypes.HkdfExpandInput
        d_509_symmetricSigningKeyInput_ = AwsCryptographyPrimitivesTypes.HkdfExpandInput_HkdfExpandInput((((algorithmSuite).commitment).HKDF).hmac, d_506_pseudoRandomKey_, default__.KEYWRAP__MAC__INFO, (((algorithmSuite).commitment).HKDF).outputKeyLength)
        d_510_pdkEncryptionKeyInput_: AwsCryptographyPrimitivesTypes.HkdfExpandInput
        def iife22_(_pat_let6_0):
            def iife23_(d_511_dt__update__tmp_h0_):
                def iife24_(_pat_let7_0):
                    def iife25_(d_512_dt__update_hinfo_h0_):
                        return AwsCryptographyPrimitivesTypes.HkdfExpandInput_HkdfExpandInput((d_511_dt__update__tmp_h0_).digestAlgorithm, (d_511_dt__update__tmp_h0_).prk, d_512_dt__update_hinfo_h0_, (d_511_dt__update__tmp_h0_).expectedLength)
                    return iife25_(_pat_let7_0)
                return iife24_(default__.KEYWRAP__ENC__INFO)
            return iife23_(_pat_let6_0)
        d_510_pdkEncryptionKeyInput_ = iife22_(d_509_symmetricSigningKeyInput_)
        d_513_maybeSymmetricSigningKey_: Wrappers.Result
        out76_: Wrappers.Result
        out76_ = (cryptoPrimitives).HkdfExpand(d_509_symmetricSigningKeyInput_)
        d_513_maybeSymmetricSigningKey_ = out76_
        d_514_symmetricSigningKey_: _dafny.Seq
        d_515_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda55_(d_516_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_516_e_)

        d_515_valueOrError1_ = (d_513_maybeSymmetricSigningKey_).MapFailure(lambda55_)
        if (d_515_valueOrError1_).IsFailure():
            res = (d_515_valueOrError1_).PropagateFailure()
            return res
        d_514_symmetricSigningKey_ = (d_515_valueOrError1_).Extract()
        d_517_maybePdkEncryptionKey_: Wrappers.Result
        out77_: Wrappers.Result
        out77_ = (cryptoPrimitives).HkdfExpand(d_510_pdkEncryptionKeyInput_)
        d_517_maybePdkEncryptionKey_ = out77_
        d_518_pdkEncryptionKey_: _dafny.Seq
        d_519_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda56_(d_520_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_520_e_)

        d_519_valueOrError2_ = (d_517_maybePdkEncryptionKey_).MapFailure(lambda56_)
        if (d_519_valueOrError2_).IsFailure():
            res = (d_519_valueOrError2_).PropagateFailure()
            return res
        d_518_pdkEncryptionKey_ = (d_519_valueOrError2_).Extract()
        res = Wrappers.Result_Success(PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys(d_518_pdkEncryptionKey_, d_514_symmetricSigningKey_))
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

