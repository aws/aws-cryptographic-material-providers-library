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
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
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
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws as Com_Amazonaws
import com_amazonaws_dynamodb.internaldafny.generated.Com as Com
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography as Aws_Cryptography
import aws_cryptography_primitives.internaldafny.generated.Aws as Aws
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext

# Module: aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IntermediateUnwrap(unwrap, wrappedMaterial, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_422_maybeCrypto_: Wrappers.Result
        out61_: Wrappers.Result
        out61_ = Aws_Cryptography_Primitives.default__.AtomicPrimitives(Aws_Cryptography_Primitives.default__.DefaultCryptoConfig())
        d_422_maybeCrypto_ = out61_
        d_423_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_424_valueOrError0_: Wrappers.Result = None
        def lambda44_(d_425_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_425_e_)

        d_424_valueOrError0_ = (d_422_maybeCrypto_).MapFailure(lambda44_)
        if (d_424_valueOrError0_).IsFailure():
            res = (d_424_valueOrError0_).PropagateFailure()
            return res
        d_423_cryptoPrimitivesX_ = (d_424_valueOrError0_).Extract()
        d_426_cryptoPrimitives_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_426_cryptoPrimitives_ = d_423_cryptoPrimitivesX_
        d_427_deserializedWrapped_: DeserializedIntermediateWrappedMaterial
        d_428_valueOrError1_: Wrappers.Result = Wrappers.Result.default(DeserializedIntermediateWrappedMaterial.default())()
        d_428_valueOrError1_ = default__.DeserializeIntermediateWrappedMaterial(wrappedMaterial, algorithmSuite)
        if (d_428_valueOrError1_).IsFailure():
            res = (d_428_valueOrError1_).PropagateFailure()
            return res
        d_427_deserializedWrapped_ = (d_428_valueOrError1_).Extract()
        let_tmp_rhs0_ = d_427_deserializedWrapped_
        d_429_encryptedPdk_ = let_tmp_rhs0_.encryptedPdk
        d_430_providerWrappedIkm_ = let_tmp_rhs0_.providerWrappedIkm
        d_431_unwrapOutput_: MaterialWrapping.UnwrapOutput
        d_432_valueOrError2_: Wrappers.Result = None
        out62_: Wrappers.Result
        out62_ = (unwrap).Invoke(MaterialWrapping.UnwrapInput_UnwrapInput(d_430_providerWrappedIkm_, algorithmSuite, encryptionContext))
        d_432_valueOrError2_ = out62_
        if (d_432_valueOrError2_).IsFailure():
            res = (d_432_valueOrError2_).PropagateFailure()
            return res
        d_431_unwrapOutput_ = (d_432_valueOrError2_).Extract()
        let_tmp_rhs1_ = d_431_unwrapOutput_
        d_433_intermediateMaterial_ = let_tmp_rhs1_.unwrappedMaterial
        d_434_unwrapInfo_ = let_tmp_rhs1_.unwrapInfo
        d_435_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_436_valueOrError3_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out63_: Wrappers.Result
        out63_ = default__.DeriveKeysFromIntermediateMaterial(d_433_intermediateMaterial_, algorithmSuite, encryptionContext, d_426_cryptoPrimitives_)
        d_436_valueOrError3_ = out63_
        if (d_436_valueOrError3_).IsFailure():
            res = (d_436_valueOrError3_).PropagateFailure()
            return res
        d_435_derivedKeys_ = (d_436_valueOrError3_).Extract()
        let_tmp_rhs2_ = d_435_derivedKeys_
        d_437_pdkEncryptionKey_ = let_tmp_rhs2_.pdkEncryptionKey
        d_438_symmetricSigningKey_ = let_tmp_rhs2_.symmetricSigningKey
        d_439_iv_: _dafny.Seq
        d_439_iv_ = _dafny.Seq([0 for d_440___v0_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_441_tagIndex_: int
        d_441_tagIndex_ = (len(d_429_encryptedPdk_)) - (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))
        d_442_aad_: _dafny.Seq
        d_443_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_443_valueOrError4_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_443_valueOrError4_).IsFailure():
            res = (d_443_valueOrError4_).PropagateFailure()
            return res
        d_442_aad_ = (d_443_valueOrError4_).Extract()
        d_444_decInput_: AwsCryptographyPrimitivesTypes.AESDecryptInput
        d_444_decInput_ = AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput(((algorithmSuite).encrypt).AES__GCM, d_437_pdkEncryptionKey_, _dafny.Seq((d_429_encryptedPdk_)[:d_441_tagIndex_:]), _dafny.Seq((d_429_encryptedPdk_)[d_441_tagIndex_::]), d_439_iv_, d_442_aad_)
        d_445_decOutR_: Wrappers.Result
        out64_: Wrappers.Result
        out64_ = (d_426_cryptoPrimitives_).AESDecrypt(d_444_decInput_)
        d_445_decOutR_ = out64_
        d_446_plaintextDataKey_: _dafny.Seq
        d_447_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda45_(d_448_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_448_e_)

        d_447_valueOrError5_ = (d_445_decOutR_).MapFailure(lambda45_)
        if (d_447_valueOrError5_).IsFailure():
            res = (d_447_valueOrError5_).PropagateFailure()
            return res
        d_446_plaintextDataKey_ = (d_447_valueOrError5_).Extract()
        d_449_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_449_valueOrError6_ = Wrappers.default__.Need((len(d_446_plaintextDataKey_)) == (AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Decrypt length")))
        if (d_449_valueOrError6_).IsFailure():
            res = (d_449_valueOrError6_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(IntermediateUnwrapOutput_IntermediateUnwrapOutput(d_446_plaintextDataKey_, d_438_symmetricSigningKey_, d_434_unwrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateWrap(generateAndWrap, plaintextDataKey, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_450_maybeCrypto_: Wrappers.Result
        out65_: Wrappers.Result
        out65_ = Aws_Cryptography_Primitives.default__.AtomicPrimitives(Aws_Cryptography_Primitives.default__.DefaultCryptoConfig())
        d_450_maybeCrypto_ = out65_
        d_451_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_452_valueOrError0_: Wrappers.Result = None
        def lambda46_(d_453_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_453_e_)

        d_452_valueOrError0_ = (d_450_maybeCrypto_).MapFailure(lambda46_)
        if (d_452_valueOrError0_).IsFailure():
            res = (d_452_valueOrError0_).PropagateFailure()
            return res
        d_451_cryptoPrimitivesX_ = (d_452_valueOrError0_).Extract()
        d_454_cryptoPrimitives_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_454_cryptoPrimitives_ = d_451_cryptoPrimitivesX_
        d_455_generateAndWrapOutput_: MaterialWrapping.GenerateAndWrapOutput
        d_456_valueOrError1_: Wrappers.Result = None
        out66_: Wrappers.Result
        out66_ = (generateAndWrap).Invoke(MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput(algorithmSuite, encryptionContext))
        d_456_valueOrError1_ = out66_
        if (d_456_valueOrError1_).IsFailure():
            res = (d_456_valueOrError1_).PropagateFailure()
            return res
        d_455_generateAndWrapOutput_ = (d_456_valueOrError1_).Extract()
        let_tmp_rhs3_ = d_455_generateAndWrapOutput_
        d_457_intermediateMaterial_ = let_tmp_rhs3_.plaintextMaterial
        d_458_providerWrappedIkm_ = let_tmp_rhs3_.wrappedMaterial
        d_459_wrapInfo_ = let_tmp_rhs3_.wrapInfo
        d_460_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_461_valueOrError2_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out67_: Wrappers.Result
        out67_ = default__.DeriveKeysFromIntermediateMaterial(d_457_intermediateMaterial_, algorithmSuite, encryptionContext, d_454_cryptoPrimitives_)
        d_461_valueOrError2_ = out67_
        if (d_461_valueOrError2_).IsFailure():
            res = (d_461_valueOrError2_).PropagateFailure()
            return res
        d_460_derivedKeys_ = (d_461_valueOrError2_).Extract()
        let_tmp_rhs4_ = d_460_derivedKeys_
        d_462_pdkEncryptionKey_ = let_tmp_rhs4_.pdkEncryptionKey
        d_463_symmetricSigningKey_ = let_tmp_rhs4_.symmetricSigningKey
        d_464_iv_: _dafny.Seq
        d_464_iv_ = _dafny.Seq([0 for d_465___v1_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_466_aad_: _dafny.Seq
        d_467_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_467_valueOrError3_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_467_valueOrError3_).IsFailure():
            res = (d_467_valueOrError3_).PropagateFailure()
            return res
        d_466_aad_ = (d_467_valueOrError3_).Extract()
        d_468_encInput_: AwsCryptographyPrimitivesTypes.AESEncryptInput
        d_468_encInput_ = AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput(((algorithmSuite).encrypt).AES__GCM, d_464_iv_, d_462_pdkEncryptionKey_, plaintextDataKey, d_466_aad_)
        d_469_encOutR_: Wrappers.Result
        out68_: Wrappers.Result
        out68_ = (d_454_cryptoPrimitives_).AESEncrypt(d_468_encInput_)
        d_469_encOutR_ = out68_
        d_470_encryptedPdk_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_471_valueOrError4_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        def lambda47_(d_472_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_472_e_)

        d_471_valueOrError4_ = (d_469_encOutR_).MapFailure(lambda47_)
        if (d_471_valueOrError4_).IsFailure():
            res = (d_471_valueOrError4_).PropagateFailure()
            return res
        d_470_encryptedPdk_ = (d_471_valueOrError4_).Extract()
        d_473_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_473_valueOrError5_ = Wrappers.default__.Need((len(((d_470_encryptedPdk_).cipherText) + ((d_470_encryptedPdk_).authTag))) == ((AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Encrypt length")))
        if (d_473_valueOrError5_).IsFailure():
            res = (d_473_valueOrError5_).PropagateFailure()
            return res
        d_474_serializedMaterial_: _dafny.Seq
        d_474_serializedMaterial_ = (((d_470_encryptedPdk_).cipherText) + ((d_470_encryptedPdk_).authTag)) + (d_458_providerWrappedIkm_)
        res = Wrappers.Result_Success(IntermediateWrapOutput_IntermediateWrapOutput(d_474_serializedMaterial_, d_463_symmetricSigningKey_, d_459_wrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateGenerateAndWrap(generateAndWrap, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_475_maybeCrypto_: Wrappers.Result
        out69_: Wrappers.Result
        out69_ = Aws_Cryptography_Primitives.default__.AtomicPrimitives(Aws_Cryptography_Primitives.default__.DefaultCryptoConfig())
        d_475_maybeCrypto_ = out69_
        d_476_cryptoPrimitives_: Aws_Cryptography_Primitives.AtomicPrimitivesClient
        d_477_valueOrError0_: Wrappers.Result = None
        def lambda48_(d_478_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_478_e_)

        d_477_valueOrError0_ = (d_475_maybeCrypto_).MapFailure(lambda48_)
        if (d_477_valueOrError0_).IsFailure():
            res = (d_477_valueOrError0_).PropagateFailure()
            return res
        d_476_cryptoPrimitives_ = (d_477_valueOrError0_).Extract()
        d_479_generateBytesResult_: Wrappers.Result
        out70_: Wrappers.Result
        out70_ = (d_476_cryptoPrimitives_).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)))
        d_479_generateBytesResult_ = out70_
        d_480_plaintextDataKey_: _dafny.Seq
        d_481_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda49_(d_482_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_482_e_)

        d_481_valueOrError1_ = (d_479_generateBytesResult_).MapFailure(lambda49_)
        if (d_481_valueOrError1_).IsFailure():
            res = (d_481_valueOrError1_).PropagateFailure()
            return res
        d_480_plaintextDataKey_ = (d_481_valueOrError1_).Extract()
        d_483_wrapOutput_: IntermediateWrapOutput
        d_484_valueOrError2_: Wrappers.Result = None
        out71_: Wrappers.Result
        out71_ = default__.IntermediateWrap(generateAndWrap, d_480_plaintextDataKey_, algorithmSuite, encryptionContext)
        d_484_valueOrError2_ = out71_
        if (d_484_valueOrError2_).IsFailure():
            res = (d_484_valueOrError2_).PropagateFailure()
            return res
        d_483_wrapOutput_ = (d_484_valueOrError2_).Extract()
        res = Wrappers.Result_Success(IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput(d_480_plaintextDataKey_, (d_483_wrapOutput_).wrappedMaterial, (d_483_wrapOutput_).symmetricSigningKey, (d_483_wrapOutput_).wrapInfo))
        return res
        return res

    @staticmethod
    def DeserializeIntermediateWrappedMaterial(material, algSuite):
        d_485_valueOrError0_ = Wrappers.default__.Need((len(material)) >= ((AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to deserialize Intermediate Key Wrapped material: too short.")))
        if (d_485_valueOrError0_).IsFailure():
            return (d_485_valueOrError0_).PropagateFailure()
        elif True:
            d_486_encryptedPdkLen_ = (AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))
            return Wrappers.Result_Success(DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial(_dafny.Seq((material)[:d_486_encryptedPdkLen_:]), _dafny.Seq((material)[d_486_encryptedPdkLen_::])))

    @staticmethod
    def DeriveKeysFromIntermediateMaterial(intermediateMaterial, algorithmSuite, encryptionContext, cryptoPrimitives):
        res: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        d_487_hkdfExtractInput_: AwsCryptographyPrimitivesTypes.HkdfExtractInput
        d_487_hkdfExtractInput_ = AwsCryptographyPrimitivesTypes.HkdfExtractInput_HkdfExtractInput((((algorithmSuite).commitment).HKDF).hmac, Wrappers.Option_None(), intermediateMaterial)
        d_488_maybePseudoRandomKey_: Wrappers.Result
        out72_: Wrappers.Result
        out72_ = (cryptoPrimitives).HkdfExtract(d_487_hkdfExtractInput_)
        d_488_maybePseudoRandomKey_ = out72_
        d_489_pseudoRandomKey_: _dafny.Seq
        d_490_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda50_(d_491_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_491_e_)

        d_490_valueOrError0_ = (d_488_maybePseudoRandomKey_).MapFailure(lambda50_)
        if (d_490_valueOrError0_).IsFailure():
            res = (d_490_valueOrError0_).PropagateFailure()
            return res
        d_489_pseudoRandomKey_ = (d_490_valueOrError0_).Extract()
        d_492_symmetricSigningKeyInput_: AwsCryptographyPrimitivesTypes.HkdfExpandInput
        d_492_symmetricSigningKeyInput_ = AwsCryptographyPrimitivesTypes.HkdfExpandInput_HkdfExpandInput((((algorithmSuite).commitment).HKDF).hmac, d_489_pseudoRandomKey_, default__.KEYWRAP__MAC__INFO, (((algorithmSuite).commitment).HKDF).outputKeyLength)
        d_493_pdkEncryptionKeyInput_: AwsCryptographyPrimitivesTypes.HkdfExpandInput
        def iife20_(_pat_let5_0):
            def iife21_(d_494_dt__update__tmp_h0_):
                def iife22_(_pat_let6_0):
                    def iife23_(d_495_dt__update_hinfo_h0_):
                        return AwsCryptographyPrimitivesTypes.HkdfExpandInput_HkdfExpandInput((d_494_dt__update__tmp_h0_).digestAlgorithm, (d_494_dt__update__tmp_h0_).prk, d_495_dt__update_hinfo_h0_, (d_494_dt__update__tmp_h0_).expectedLength)
                    return iife23_(_pat_let6_0)
                return iife22_(default__.KEYWRAP__ENC__INFO)
            return iife21_(_pat_let5_0)
        d_493_pdkEncryptionKeyInput_ = iife20_(d_492_symmetricSigningKeyInput_)
        d_496_maybeSymmetricSigningKey_: Wrappers.Result
        out73_: Wrappers.Result
        out73_ = (cryptoPrimitives).HkdfExpand(d_492_symmetricSigningKeyInput_)
        d_496_maybeSymmetricSigningKey_ = out73_
        d_497_symmetricSigningKey_: _dafny.Seq
        d_498_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda51_(d_499_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_499_e_)

        d_498_valueOrError1_ = (d_496_maybeSymmetricSigningKey_).MapFailure(lambda51_)
        if (d_498_valueOrError1_).IsFailure():
            res = (d_498_valueOrError1_).PropagateFailure()
            return res
        d_497_symmetricSigningKey_ = (d_498_valueOrError1_).Extract()
        d_500_maybePdkEncryptionKey_: Wrappers.Result
        out74_: Wrappers.Result
        out74_ = (cryptoPrimitives).HkdfExpand(d_493_pdkEncryptionKeyInput_)
        d_500_maybePdkEncryptionKey_ = out74_
        d_501_pdkEncryptionKey_: _dafny.Seq
        d_502_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda52_(d_503_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_503_e_)

        d_502_valueOrError2_ = (d_500_maybePdkEncryptionKey_).MapFailure(lambda52_)
        if (d_502_valueOrError2_).IsFailure():
            res = (d_502_valueOrError2_).PropagateFailure()
            return res
        d_501_pdkEncryptionKey_ = (d_502_valueOrError2_).Extract()
        res = Wrappers.Result_Success(PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys(d_501_pdkEncryptionKey_, d_497_symmetricSigningKey_))
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

