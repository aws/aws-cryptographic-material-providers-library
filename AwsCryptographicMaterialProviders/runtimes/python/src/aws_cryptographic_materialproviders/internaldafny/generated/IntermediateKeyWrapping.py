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
        d_441_maybeCrypto_: Wrappers.Result
        out66_: Wrappers.Result
        out66_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_441_maybeCrypto_ = out66_
        d_442_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_443_valueOrError0_: Wrappers.Result = None
        def lambda48_(d_444_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_444_e_)

        d_443_valueOrError0_ = (d_441_maybeCrypto_).MapFailure(lambda48_)
        if (d_443_valueOrError0_).IsFailure():
            res = (d_443_valueOrError0_).PropagateFailure()
            return res
        d_442_cryptoPrimitivesX_ = (d_443_valueOrError0_).Extract()
        d_445_cryptoPrimitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_445_cryptoPrimitives_ = d_442_cryptoPrimitivesX_
        d_446_deserializedWrapped_: DeserializedIntermediateWrappedMaterial
        d_447_valueOrError1_: Wrappers.Result = Wrappers.Result.default(DeserializedIntermediateWrappedMaterial.default())()
        d_447_valueOrError1_ = default__.DeserializeIntermediateWrappedMaterial(wrappedMaterial, algorithmSuite)
        if (d_447_valueOrError1_).IsFailure():
            res = (d_447_valueOrError1_).PropagateFailure()
            return res
        d_446_deserializedWrapped_ = (d_447_valueOrError1_).Extract()
        let_tmp_rhs0_ = d_446_deserializedWrapped_
        d_448_encryptedPdk_ = let_tmp_rhs0_.encryptedPdk
        d_449_providerWrappedIkm_ = let_tmp_rhs0_.providerWrappedIkm
        d_450_unwrapOutput_: MaterialWrapping.UnwrapOutput
        d_451_valueOrError2_: Wrappers.Result = None
        out67_: Wrappers.Result
        out67_ = (unwrap).Invoke(MaterialWrapping.UnwrapInput_UnwrapInput(d_449_providerWrappedIkm_, algorithmSuite, encryptionContext))
        d_451_valueOrError2_ = out67_
        if (d_451_valueOrError2_).IsFailure():
            res = (d_451_valueOrError2_).PropagateFailure()
            return res
        d_450_unwrapOutput_ = (d_451_valueOrError2_).Extract()
        let_tmp_rhs1_ = d_450_unwrapOutput_
        d_452_intermediateMaterial_ = let_tmp_rhs1_.unwrappedMaterial
        d_453_unwrapInfo_ = let_tmp_rhs1_.unwrapInfo
        d_454_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_455_valueOrError3_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out68_: Wrappers.Result
        out68_ = default__.DeriveKeysFromIntermediateMaterial(d_452_intermediateMaterial_, algorithmSuite, encryptionContext, d_445_cryptoPrimitives_)
        d_455_valueOrError3_ = out68_
        if (d_455_valueOrError3_).IsFailure():
            res = (d_455_valueOrError3_).PropagateFailure()
            return res
        d_454_derivedKeys_ = (d_455_valueOrError3_).Extract()
        let_tmp_rhs2_ = d_454_derivedKeys_
        d_456_pdkEncryptionKey_ = let_tmp_rhs2_.pdkEncryptionKey
        d_457_symmetricSigningKey_ = let_tmp_rhs2_.symmetricSigningKey
        d_458_iv_: _dafny.Seq
        d_458_iv_ = _dafny.Seq([0 for d_459___v0_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_460_tagIndex_: int
        d_460_tagIndex_ = (len(d_448_encryptedPdk_)) - (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))
        d_461_aad_: _dafny.Seq
        d_462_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_462_valueOrError4_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_462_valueOrError4_).IsFailure():
            res = (d_462_valueOrError4_).PropagateFailure()
            return res
        d_461_aad_ = (d_462_valueOrError4_).Extract()
        d_463_decInput_: AwsCryptographyPrimitivesTypes.AESDecryptInput
        d_463_decInput_ = AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput(((algorithmSuite).encrypt).AES__GCM, d_456_pdkEncryptionKey_, _dafny.Seq((d_448_encryptedPdk_)[:d_460_tagIndex_:]), _dafny.Seq((d_448_encryptedPdk_)[d_460_tagIndex_::]), d_458_iv_, d_461_aad_)
        d_464_decOutR_: Wrappers.Result
        out69_: Wrappers.Result
        out69_ = (d_445_cryptoPrimitives_).AESDecrypt(d_463_decInput_)
        d_464_decOutR_ = out69_
        d_465_plaintextDataKey_: _dafny.Seq
        d_466_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda49_(d_467_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_467_e_)

        d_466_valueOrError5_ = (d_464_decOutR_).MapFailure(lambda49_)
        if (d_466_valueOrError5_).IsFailure():
            res = (d_466_valueOrError5_).PropagateFailure()
            return res
        d_465_plaintextDataKey_ = (d_466_valueOrError5_).Extract()
        d_468_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_468_valueOrError6_ = Wrappers.default__.Need((len(d_465_plaintextDataKey_)) == (AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Decrypt length")))
        if (d_468_valueOrError6_).IsFailure():
            res = (d_468_valueOrError6_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(IntermediateUnwrapOutput_IntermediateUnwrapOutput(d_465_plaintextDataKey_, d_457_symmetricSigningKey_, d_453_unwrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateWrap(generateAndWrap, plaintextDataKey, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_469_maybeCrypto_: Wrappers.Result
        out70_: Wrappers.Result
        out70_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_469_maybeCrypto_ = out70_
        d_470_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_471_valueOrError0_: Wrappers.Result = None
        def lambda50_(d_472_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_472_e_)

        d_471_valueOrError0_ = (d_469_maybeCrypto_).MapFailure(lambda50_)
        if (d_471_valueOrError0_).IsFailure():
            res = (d_471_valueOrError0_).PropagateFailure()
            return res
        d_470_cryptoPrimitivesX_ = (d_471_valueOrError0_).Extract()
        d_473_cryptoPrimitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_473_cryptoPrimitives_ = d_470_cryptoPrimitivesX_
        d_474_generateAndWrapOutput_: MaterialWrapping.GenerateAndWrapOutput
        d_475_valueOrError1_: Wrappers.Result = None
        out71_: Wrappers.Result
        out71_ = (generateAndWrap).Invoke(MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput(algorithmSuite, encryptionContext))
        d_475_valueOrError1_ = out71_
        if (d_475_valueOrError1_).IsFailure():
            res = (d_475_valueOrError1_).PropagateFailure()
            return res
        d_474_generateAndWrapOutput_ = (d_475_valueOrError1_).Extract()
        let_tmp_rhs3_ = d_474_generateAndWrapOutput_
        d_476_intermediateMaterial_ = let_tmp_rhs3_.plaintextMaterial
        d_477_providerWrappedIkm_ = let_tmp_rhs3_.wrappedMaterial
        d_478_wrapInfo_ = let_tmp_rhs3_.wrapInfo
        d_479_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_480_valueOrError2_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out72_: Wrappers.Result
        out72_ = default__.DeriveKeysFromIntermediateMaterial(d_476_intermediateMaterial_, algorithmSuite, encryptionContext, d_473_cryptoPrimitives_)
        d_480_valueOrError2_ = out72_
        if (d_480_valueOrError2_).IsFailure():
            res = (d_480_valueOrError2_).PropagateFailure()
            return res
        d_479_derivedKeys_ = (d_480_valueOrError2_).Extract()
        let_tmp_rhs4_ = d_479_derivedKeys_
        d_481_pdkEncryptionKey_ = let_tmp_rhs4_.pdkEncryptionKey
        d_482_symmetricSigningKey_ = let_tmp_rhs4_.symmetricSigningKey
        d_483_iv_: _dafny.Seq
        d_483_iv_ = _dafny.Seq([0 for d_484___v1_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_485_aad_: _dafny.Seq
        d_486_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_486_valueOrError3_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_486_valueOrError3_).IsFailure():
            res = (d_486_valueOrError3_).PropagateFailure()
            return res
        d_485_aad_ = (d_486_valueOrError3_).Extract()
        d_487_encInput_: AwsCryptographyPrimitivesTypes.AESEncryptInput
        d_487_encInput_ = AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput(((algorithmSuite).encrypt).AES__GCM, d_483_iv_, d_481_pdkEncryptionKey_, plaintextDataKey, d_485_aad_)
        d_488_encOutR_: Wrappers.Result
        out73_: Wrappers.Result
        out73_ = (d_473_cryptoPrimitives_).AESEncrypt(d_487_encInput_)
        d_488_encOutR_ = out73_
        d_489_encryptedPdk_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_490_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        def lambda51_(d_491_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_491_e_)

        d_490_valueOrError4_ = (d_488_encOutR_).MapFailure(lambda51_)
        if (d_490_valueOrError4_).IsFailure():
            res = (d_490_valueOrError4_).PropagateFailure()
            return res
        d_489_encryptedPdk_ = (d_490_valueOrError4_).Extract()
        d_492_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_492_valueOrError5_ = Wrappers.default__.Need((len(((d_489_encryptedPdk_).cipherText) + ((d_489_encryptedPdk_).authTag))) == ((AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Encrypt length")))
        if (d_492_valueOrError5_).IsFailure():
            res = (d_492_valueOrError5_).PropagateFailure()
            return res
        d_493_serializedMaterial_: _dafny.Seq
        d_493_serializedMaterial_ = (((d_489_encryptedPdk_).cipherText) + ((d_489_encryptedPdk_).authTag)) + (d_477_providerWrappedIkm_)
        res = Wrappers.Result_Success(IntermediateWrapOutput_IntermediateWrapOutput(d_493_serializedMaterial_, d_482_symmetricSigningKey_, d_478_wrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateGenerateAndWrap(generateAndWrap, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_494_maybeCrypto_: Wrappers.Result
        out74_: Wrappers.Result
        out74_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_494_maybeCrypto_ = out74_
        d_495_cryptoPrimitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_496_valueOrError0_: Wrappers.Result = None
        def lambda52_(d_497_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_497_e_)

        d_496_valueOrError0_ = (d_494_maybeCrypto_).MapFailure(lambda52_)
        if (d_496_valueOrError0_).IsFailure():
            res = (d_496_valueOrError0_).PropagateFailure()
            return res
        d_495_cryptoPrimitives_ = (d_496_valueOrError0_).Extract()
        d_498_generateBytesResult_: Wrappers.Result
        out75_: Wrappers.Result
        out75_ = (d_495_cryptoPrimitives_).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)))
        d_498_generateBytesResult_ = out75_
        d_499_plaintextDataKey_: _dafny.Seq
        d_500_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda53_(d_501_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_501_e_)

        d_500_valueOrError1_ = (d_498_generateBytesResult_).MapFailure(lambda53_)
        if (d_500_valueOrError1_).IsFailure():
            res = (d_500_valueOrError1_).PropagateFailure()
            return res
        d_499_plaintextDataKey_ = (d_500_valueOrError1_).Extract()
        d_502_wrapOutput_: IntermediateWrapOutput
        d_503_valueOrError2_: Wrappers.Result = None
        out76_: Wrappers.Result
        out76_ = default__.IntermediateWrap(generateAndWrap, d_499_plaintextDataKey_, algorithmSuite, encryptionContext)
        d_503_valueOrError2_ = out76_
        if (d_503_valueOrError2_).IsFailure():
            res = (d_503_valueOrError2_).PropagateFailure()
            return res
        d_502_wrapOutput_ = (d_503_valueOrError2_).Extract()
        res = Wrappers.Result_Success(IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput(d_499_plaintextDataKey_, (d_502_wrapOutput_).wrappedMaterial, (d_502_wrapOutput_).symmetricSigningKey, (d_502_wrapOutput_).wrapInfo))
        return res
        return res

    @staticmethod
    def DeserializeIntermediateWrappedMaterial(material, algSuite):
        d_504_valueOrError0_ = Wrappers.default__.Need((len(material)) >= ((AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to deserialize Intermediate Key Wrapped material: too short.")))
        if (d_504_valueOrError0_).IsFailure():
            return (d_504_valueOrError0_).PropagateFailure()
        elif True:
            d_505_encryptedPdkLen_ = (AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))
            return Wrappers.Result_Success(DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial(_dafny.Seq((material)[:d_505_encryptedPdkLen_:]), _dafny.Seq((material)[d_505_encryptedPdkLen_::])))

    @staticmethod
    def DeriveKeysFromIntermediateMaterial(intermediateMaterial, algorithmSuite, encryptionContext, cryptoPrimitives):
        res: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        d_506_hkdfExtractInput_: AwsCryptographyPrimitivesTypes.HkdfExtractInput
        d_506_hkdfExtractInput_ = AwsCryptographyPrimitivesTypes.HkdfExtractInput_HkdfExtractInput((((algorithmSuite).commitment).HKDF).hmac, Wrappers.Option_None(), intermediateMaterial)
        d_507_maybePseudoRandomKey_: Wrappers.Result
        out77_: Wrappers.Result
        out77_ = (cryptoPrimitives).HkdfExtract(d_506_hkdfExtractInput_)
        d_507_maybePseudoRandomKey_ = out77_
        d_508_pseudoRandomKey_: _dafny.Seq
        d_509_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda54_(d_510_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_510_e_)

        d_509_valueOrError0_ = (d_507_maybePseudoRandomKey_).MapFailure(lambda54_)
        if (d_509_valueOrError0_).IsFailure():
            res = (d_509_valueOrError0_).PropagateFailure()
            return res
        d_508_pseudoRandomKey_ = (d_509_valueOrError0_).Extract()
        d_511_symmetricSigningKeyInput_: AwsCryptographyPrimitivesTypes.HkdfExpandInput
        d_511_symmetricSigningKeyInput_ = AwsCryptographyPrimitivesTypes.HkdfExpandInput_HkdfExpandInput((((algorithmSuite).commitment).HKDF).hmac, d_508_pseudoRandomKey_, default__.KEYWRAP__MAC__INFO, (((algorithmSuite).commitment).HKDF).outputKeyLength)
        d_512_pdkEncryptionKeyInput_: AwsCryptographyPrimitivesTypes.HkdfExpandInput
        def iife22_(_pat_let6_0):
            def iife23_(d_513_dt__update__tmp_h0_):
                def iife24_(_pat_let7_0):
                    def iife25_(d_514_dt__update_hinfo_h0_):
                        return AwsCryptographyPrimitivesTypes.HkdfExpandInput_HkdfExpandInput((d_513_dt__update__tmp_h0_).digestAlgorithm, (d_513_dt__update__tmp_h0_).prk, d_514_dt__update_hinfo_h0_, (d_513_dt__update__tmp_h0_).expectedLength)
                    return iife25_(_pat_let7_0)
                return iife24_(default__.KEYWRAP__ENC__INFO)
            return iife23_(_pat_let6_0)
        d_512_pdkEncryptionKeyInput_ = iife22_(d_511_symmetricSigningKeyInput_)
        d_515_maybeSymmetricSigningKey_: Wrappers.Result
        out78_: Wrappers.Result
        out78_ = (cryptoPrimitives).HkdfExpand(d_511_symmetricSigningKeyInput_)
        d_515_maybeSymmetricSigningKey_ = out78_
        d_516_symmetricSigningKey_: _dafny.Seq
        d_517_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda55_(d_518_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_518_e_)

        d_517_valueOrError1_ = (d_515_maybeSymmetricSigningKey_).MapFailure(lambda55_)
        if (d_517_valueOrError1_).IsFailure():
            res = (d_517_valueOrError1_).PropagateFailure()
            return res
        d_516_symmetricSigningKey_ = (d_517_valueOrError1_).Extract()
        d_519_maybePdkEncryptionKey_: Wrappers.Result
        out79_: Wrappers.Result
        out79_ = (cryptoPrimitives).HkdfExpand(d_512_pdkEncryptionKeyInput_)
        d_519_maybePdkEncryptionKey_ = out79_
        d_520_pdkEncryptionKey_: _dafny.Seq
        d_521_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda56_(d_522_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_522_e_)

        d_521_valueOrError2_ = (d_519_maybePdkEncryptionKey_).MapFailure(lambda56_)
        if (d_521_valueOrError2_).IsFailure():
            res = (d_521_valueOrError2_).PropagateFailure()
            return res
        d_520_pdkEncryptionKey_ = (d_521_valueOrError2_).Extract()
        res = Wrappers.Result_Success(PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys(d_520_pdkEncryptionKey_, d_516_symmetricSigningKey_))
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

