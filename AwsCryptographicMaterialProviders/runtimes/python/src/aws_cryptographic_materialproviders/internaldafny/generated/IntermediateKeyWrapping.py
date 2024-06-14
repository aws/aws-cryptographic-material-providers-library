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
        d_438_maybeCrypto_: Wrappers.Result
        out63_: Wrappers.Result
        out63_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_438_maybeCrypto_ = out63_
        d_439_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_440_valueOrError0_: Wrappers.Result = None
        def lambda47_(d_441_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_441_e_)

        d_440_valueOrError0_ = (d_438_maybeCrypto_).MapFailure(lambda47_)
        if (d_440_valueOrError0_).IsFailure():
            res = (d_440_valueOrError0_).PropagateFailure()
            return res
        d_439_cryptoPrimitivesX_ = (d_440_valueOrError0_).Extract()
        d_442_cryptoPrimitives_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_442_cryptoPrimitives_ = d_439_cryptoPrimitivesX_
        d_443_deserializedWrapped_: DeserializedIntermediateWrappedMaterial
        d_444_valueOrError1_: Wrappers.Result = Wrappers.Result.default(DeserializedIntermediateWrappedMaterial.default())()
        d_444_valueOrError1_ = default__.DeserializeIntermediateWrappedMaterial(wrappedMaterial, algorithmSuite)
        if (d_444_valueOrError1_).IsFailure():
            res = (d_444_valueOrError1_).PropagateFailure()
            return res
        d_443_deserializedWrapped_ = (d_444_valueOrError1_).Extract()
        let_tmp_rhs0_ = d_443_deserializedWrapped_
        d_445_encryptedPdk_ = let_tmp_rhs0_.encryptedPdk
        d_446_providerWrappedIkm_ = let_tmp_rhs0_.providerWrappedIkm
        d_447_unwrapOutput_: MaterialWrapping.UnwrapOutput
        d_448_valueOrError2_: Wrappers.Result = None
        out64_: Wrappers.Result
        out64_ = (unwrap).Invoke(MaterialWrapping.UnwrapInput_UnwrapInput(d_446_providerWrappedIkm_, algorithmSuite, encryptionContext))
        d_448_valueOrError2_ = out64_
        if (d_448_valueOrError2_).IsFailure():
            res = (d_448_valueOrError2_).PropagateFailure()
            return res
        d_447_unwrapOutput_ = (d_448_valueOrError2_).Extract()
        let_tmp_rhs1_ = d_447_unwrapOutput_
        d_449_intermediateMaterial_ = let_tmp_rhs1_.unwrappedMaterial
        d_450_unwrapInfo_ = let_tmp_rhs1_.unwrapInfo
        d_451_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_452_valueOrError3_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out65_: Wrappers.Result
        out65_ = default__.DeriveKeysFromIntermediateMaterial(d_449_intermediateMaterial_, algorithmSuite, encryptionContext, d_442_cryptoPrimitives_)
        d_452_valueOrError3_ = out65_
        if (d_452_valueOrError3_).IsFailure():
            res = (d_452_valueOrError3_).PropagateFailure()
            return res
        d_451_derivedKeys_ = (d_452_valueOrError3_).Extract()
        let_tmp_rhs2_ = d_451_derivedKeys_
        d_453_pdkEncryptionKey_ = let_tmp_rhs2_.pdkEncryptionKey
        d_454_symmetricSigningKey_ = let_tmp_rhs2_.symmetricSigningKey
        d_455_iv_: _dafny.Seq
        d_455_iv_ = _dafny.Seq([0 for d_456___v0_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_457_tagIndex_: int
        d_457_tagIndex_ = (len(d_445_encryptedPdk_)) - (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))
        d_458_aad_: _dafny.Seq
        d_459_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_459_valueOrError4_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_459_valueOrError4_).IsFailure():
            res = (d_459_valueOrError4_).PropagateFailure()
            return res
        d_458_aad_ = (d_459_valueOrError4_).Extract()
        d_460_decInput_: AwsCryptographyPrimitivesTypes.AESDecryptInput
        d_460_decInput_ = AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput(((algorithmSuite).encrypt).AES__GCM, d_453_pdkEncryptionKey_, _dafny.Seq((d_445_encryptedPdk_)[:d_457_tagIndex_:]), _dafny.Seq((d_445_encryptedPdk_)[d_457_tagIndex_::]), d_455_iv_, d_458_aad_)
        d_461_decOutR_: Wrappers.Result
        out66_: Wrappers.Result
        out66_ = (d_442_cryptoPrimitives_).AESDecrypt(d_460_decInput_)
        d_461_decOutR_ = out66_
        d_462_plaintextDataKey_: _dafny.Seq
        d_463_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda48_(d_464_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_464_e_)

        d_463_valueOrError5_ = (d_461_decOutR_).MapFailure(lambda48_)
        if (d_463_valueOrError5_).IsFailure():
            res = (d_463_valueOrError5_).PropagateFailure()
            return res
        d_462_plaintextDataKey_ = (d_463_valueOrError5_).Extract()
        d_465_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_465_valueOrError6_ = Wrappers.default__.Need((len(d_462_plaintextDataKey_)) == (AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Decrypt length")))
        if (d_465_valueOrError6_).IsFailure():
            res = (d_465_valueOrError6_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(IntermediateUnwrapOutput_IntermediateUnwrapOutput(d_462_plaintextDataKey_, d_454_symmetricSigningKey_, d_450_unwrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateWrap(generateAndWrap, plaintextDataKey, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_466_maybeCrypto_: Wrappers.Result
        out67_: Wrappers.Result
        out67_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_466_maybeCrypto_ = out67_
        d_467_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_468_valueOrError0_: Wrappers.Result = None
        def lambda49_(d_469_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_469_e_)

        d_468_valueOrError0_ = (d_466_maybeCrypto_).MapFailure(lambda49_)
        if (d_468_valueOrError0_).IsFailure():
            res = (d_468_valueOrError0_).PropagateFailure()
            return res
        d_467_cryptoPrimitivesX_ = (d_468_valueOrError0_).Extract()
        d_470_cryptoPrimitives_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_470_cryptoPrimitives_ = d_467_cryptoPrimitivesX_
        d_471_generateAndWrapOutput_: MaterialWrapping.GenerateAndWrapOutput
        d_472_valueOrError1_: Wrappers.Result = None
        out68_: Wrappers.Result
        out68_ = (generateAndWrap).Invoke(MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput(algorithmSuite, encryptionContext))
        d_472_valueOrError1_ = out68_
        if (d_472_valueOrError1_).IsFailure():
            res = (d_472_valueOrError1_).PropagateFailure()
            return res
        d_471_generateAndWrapOutput_ = (d_472_valueOrError1_).Extract()
        let_tmp_rhs3_ = d_471_generateAndWrapOutput_
        d_473_intermediateMaterial_ = let_tmp_rhs3_.plaintextMaterial
        d_474_providerWrappedIkm_ = let_tmp_rhs3_.wrappedMaterial
        d_475_wrapInfo_ = let_tmp_rhs3_.wrapInfo
        d_476_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_477_valueOrError2_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out69_: Wrappers.Result
        out69_ = default__.DeriveKeysFromIntermediateMaterial(d_473_intermediateMaterial_, algorithmSuite, encryptionContext, d_470_cryptoPrimitives_)
        d_477_valueOrError2_ = out69_
        if (d_477_valueOrError2_).IsFailure():
            res = (d_477_valueOrError2_).PropagateFailure()
            return res
        d_476_derivedKeys_ = (d_477_valueOrError2_).Extract()
        let_tmp_rhs4_ = d_476_derivedKeys_
        d_478_pdkEncryptionKey_ = let_tmp_rhs4_.pdkEncryptionKey
        d_479_symmetricSigningKey_ = let_tmp_rhs4_.symmetricSigningKey
        d_480_iv_: _dafny.Seq
        d_480_iv_ = _dafny.Seq([0 for d_481___v1_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_482_aad_: _dafny.Seq
        d_483_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_483_valueOrError3_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_483_valueOrError3_).IsFailure():
            res = (d_483_valueOrError3_).PropagateFailure()
            return res
        d_482_aad_ = (d_483_valueOrError3_).Extract()
        d_484_encInput_: AwsCryptographyPrimitivesTypes.AESEncryptInput
        d_484_encInput_ = AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput(((algorithmSuite).encrypt).AES__GCM, d_480_iv_, d_478_pdkEncryptionKey_, plaintextDataKey, d_482_aad_)
        d_485_encOutR_: Wrappers.Result
        out70_: Wrappers.Result
        out70_ = (d_470_cryptoPrimitives_).AESEncrypt(d_484_encInput_)
        d_485_encOutR_ = out70_
        d_486_encryptedPdk_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_487_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        def lambda50_(d_488_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_488_e_)

        d_487_valueOrError4_ = (d_485_encOutR_).MapFailure(lambda50_)
        if (d_487_valueOrError4_).IsFailure():
            res = (d_487_valueOrError4_).PropagateFailure()
            return res
        d_486_encryptedPdk_ = (d_487_valueOrError4_).Extract()
        d_489_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_489_valueOrError5_ = Wrappers.default__.Need((len(((d_486_encryptedPdk_).cipherText) + ((d_486_encryptedPdk_).authTag))) == ((AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Encrypt length")))
        if (d_489_valueOrError5_).IsFailure():
            res = (d_489_valueOrError5_).PropagateFailure()
            return res
        d_490_serializedMaterial_: _dafny.Seq
        d_490_serializedMaterial_ = (((d_486_encryptedPdk_).cipherText) + ((d_486_encryptedPdk_).authTag)) + (d_474_providerWrappedIkm_)
        res = Wrappers.Result_Success(IntermediateWrapOutput_IntermediateWrapOutput(d_490_serializedMaterial_, d_479_symmetricSigningKey_, d_475_wrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateGenerateAndWrap(generateAndWrap, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_491_maybeCrypto_: Wrappers.Result
        out71_: Wrappers.Result
        out71_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_491_maybeCrypto_ = out71_
        d_492_cryptoPrimitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_493_valueOrError0_: Wrappers.Result = None
        def lambda51_(d_494_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_494_e_)

        d_493_valueOrError0_ = (d_491_maybeCrypto_).MapFailure(lambda51_)
        if (d_493_valueOrError0_).IsFailure():
            res = (d_493_valueOrError0_).PropagateFailure()
            return res
        d_492_cryptoPrimitives_ = (d_493_valueOrError0_).Extract()
        d_495_generateBytesResult_: Wrappers.Result
        out72_: Wrappers.Result
        out72_ = (d_492_cryptoPrimitives_).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)))
        d_495_generateBytesResult_ = out72_
        d_496_plaintextDataKey_: _dafny.Seq
        d_497_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda52_(d_498_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_498_e_)

        d_497_valueOrError1_ = (d_495_generateBytesResult_).MapFailure(lambda52_)
        if (d_497_valueOrError1_).IsFailure():
            res = (d_497_valueOrError1_).PropagateFailure()
            return res
        d_496_plaintextDataKey_ = (d_497_valueOrError1_).Extract()
        d_499_wrapOutput_: IntermediateWrapOutput
        d_500_valueOrError2_: Wrappers.Result = None
        out73_: Wrappers.Result
        out73_ = default__.IntermediateWrap(generateAndWrap, d_496_plaintextDataKey_, algorithmSuite, encryptionContext)
        d_500_valueOrError2_ = out73_
        if (d_500_valueOrError2_).IsFailure():
            res = (d_500_valueOrError2_).PropagateFailure()
            return res
        d_499_wrapOutput_ = (d_500_valueOrError2_).Extract()
        res = Wrappers.Result_Success(IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput(d_496_plaintextDataKey_, (d_499_wrapOutput_).wrappedMaterial, (d_499_wrapOutput_).symmetricSigningKey, (d_499_wrapOutput_).wrapInfo))
        return res
        return res

    @staticmethod
    def DeserializeIntermediateWrappedMaterial(material, algSuite):
        d_501_valueOrError0_ = Wrappers.default__.Need((len(material)) >= ((AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to deserialize Intermediate Key Wrapped material: too short.")))
        if (d_501_valueOrError0_).IsFailure():
            return (d_501_valueOrError0_).PropagateFailure()
        elif True:
            d_502_encryptedPdkLen_ = (AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))
            return Wrappers.Result_Success(DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial(_dafny.Seq((material)[:d_502_encryptedPdkLen_:]), _dafny.Seq((material)[d_502_encryptedPdkLen_::])))

    @staticmethod
    def DeriveKeysFromIntermediateMaterial(intermediateMaterial, algorithmSuite, encryptionContext, cryptoPrimitives):
        res: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        d_503_hkdfExtractInput_: AwsCryptographyPrimitivesTypes.HkdfExtractInput
        d_503_hkdfExtractInput_ = AwsCryptographyPrimitivesTypes.HkdfExtractInput_HkdfExtractInput((((algorithmSuite).commitment).HKDF).hmac, Wrappers.Option_None(), intermediateMaterial)
        d_504_maybePseudoRandomKey_: Wrappers.Result
        out74_: Wrappers.Result
        out74_ = (cryptoPrimitives).HkdfExtract(d_503_hkdfExtractInput_)
        d_504_maybePseudoRandomKey_ = out74_
        d_505_pseudoRandomKey_: _dafny.Seq
        d_506_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda53_(d_507_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_507_e_)

        d_506_valueOrError0_ = (d_504_maybePseudoRandomKey_).MapFailure(lambda53_)
        if (d_506_valueOrError0_).IsFailure():
            res = (d_506_valueOrError0_).PropagateFailure()
            return res
        d_505_pseudoRandomKey_ = (d_506_valueOrError0_).Extract()
        d_508_symmetricSigningKeyInput_: AwsCryptographyPrimitivesTypes.HkdfExpandInput
        d_508_symmetricSigningKeyInput_ = AwsCryptographyPrimitivesTypes.HkdfExpandInput_HkdfExpandInput((((algorithmSuite).commitment).HKDF).hmac, d_505_pseudoRandomKey_, default__.KEYWRAP__MAC__INFO, (((algorithmSuite).commitment).HKDF).outputKeyLength)
        d_509_pdkEncryptionKeyInput_: AwsCryptographyPrimitivesTypes.HkdfExpandInput
        def iife22_(_pat_let6_0):
            def iife23_(d_510_dt__update__tmp_h0_):
                def iife24_(_pat_let7_0):
                    def iife25_(d_511_dt__update_hinfo_h0_):
                        return AwsCryptographyPrimitivesTypes.HkdfExpandInput_HkdfExpandInput((d_510_dt__update__tmp_h0_).digestAlgorithm, (d_510_dt__update__tmp_h0_).prk, d_511_dt__update_hinfo_h0_, (d_510_dt__update__tmp_h0_).expectedLength)
                    return iife25_(_pat_let7_0)
                return iife24_(default__.KEYWRAP__ENC__INFO)
            return iife23_(_pat_let6_0)
        d_509_pdkEncryptionKeyInput_ = iife22_(d_508_symmetricSigningKeyInput_)
        d_512_maybeSymmetricSigningKey_: Wrappers.Result
        out75_: Wrappers.Result
        out75_ = (cryptoPrimitives).HkdfExpand(d_508_symmetricSigningKeyInput_)
        d_512_maybeSymmetricSigningKey_ = out75_
        d_513_symmetricSigningKey_: _dafny.Seq
        d_514_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda54_(d_515_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_515_e_)

        d_514_valueOrError1_ = (d_512_maybeSymmetricSigningKey_).MapFailure(lambda54_)
        if (d_514_valueOrError1_).IsFailure():
            res = (d_514_valueOrError1_).PropagateFailure()
            return res
        d_513_symmetricSigningKey_ = (d_514_valueOrError1_).Extract()
        d_516_maybePdkEncryptionKey_: Wrappers.Result
        out76_: Wrappers.Result
        out76_ = (cryptoPrimitives).HkdfExpand(d_509_pdkEncryptionKeyInput_)
        d_516_maybePdkEncryptionKey_ = out76_
        d_517_pdkEncryptionKey_: _dafny.Seq
        d_518_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda55_(d_519_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_519_e_)

        d_518_valueOrError2_ = (d_516_maybePdkEncryptionKey_).MapFailure(lambda55_)
        if (d_518_valueOrError2_).IsFailure():
            res = (d_518_valueOrError2_).PropagateFailure()
            return res
        d_517_pdkEncryptionKey_ = (d_518_valueOrError2_).Extract()
        res = Wrappers.Result_Success(PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys(d_517_pdkEncryptionKey_, d_513_symmetricSigningKey_))
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

