import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UTF8
import software.amazon.cryptography.services.dynamodb.internaldafny.types
import software.amazon.cryptography.services.kms.internaldafny.types
import software.amazon.cryptography.primitives.internaldafny.types
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import AesKdfCtr
import Relations
import Seq_MergeSort
import Math
import Seq
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibraryInterop
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software.amazon.cryptography.keystore.internaldafny.types
import software.amazon.cryptography.materialproviders.internaldafny.types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext

# Module: IntermediateKeyWrapping

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IntermediateUnwrap(unwrap, wrappedMaterial, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_402_maybeCrypto_: Wrappers.Result
        out61_: Wrappers.Result
        out61_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_402_maybeCrypto_ = out61_
        d_403_cryptoPrimitivesX_: software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient
        d_404_valueOrError0_: Wrappers.Result = None
        def lambda44_(d_405_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives(d_405_e_)

        d_404_valueOrError0_ = (d_402_maybeCrypto_).MapFailure(lambda44_)
        if (d_404_valueOrError0_).IsFailure():
            res = (d_404_valueOrError0_).PropagateFailure()
            return res
        d_403_cryptoPrimitivesX_ = (d_404_valueOrError0_).Extract()
        d_406_cryptoPrimitives_: software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient
        d_406_cryptoPrimitives_ = d_403_cryptoPrimitivesX_
        d_407_deserializedWrapped_: DeserializedIntermediateWrappedMaterial
        d_408_valueOrError1_: Wrappers.Result = Wrappers.Result.default(DeserializedIntermediateWrappedMaterial.default())()
        d_408_valueOrError1_ = default__.DeserializeIntermediateWrappedMaterial(wrappedMaterial, algorithmSuite)
        if (d_408_valueOrError1_).IsFailure():
            res = (d_408_valueOrError1_).PropagateFailure()
            return res
        d_407_deserializedWrapped_ = (d_408_valueOrError1_).Extract()
        let_tmp_rhs0_ = d_407_deserializedWrapped_
        d_409_encryptedPdk_ = let_tmp_rhs0_.encryptedPdk
        d_410_providerWrappedIkm_ = let_tmp_rhs0_.providerWrappedIkm
        d_411_unwrapOutput_: MaterialWrapping.UnwrapOutput
        d_412_valueOrError2_: Wrappers.Result = None
        out62_: Wrappers.Result
        out62_ = (unwrap).Invoke(MaterialWrapping.UnwrapInput_UnwrapInput(d_410_providerWrappedIkm_, algorithmSuite, encryptionContext))
        d_412_valueOrError2_ = out62_
        if (d_412_valueOrError2_).IsFailure():
            res = (d_412_valueOrError2_).PropagateFailure()
            return res
        d_411_unwrapOutput_ = (d_412_valueOrError2_).Extract()
        let_tmp_rhs1_ = d_411_unwrapOutput_
        d_413_intermediateMaterial_ = let_tmp_rhs1_.unwrappedMaterial
        d_414_unwrapInfo_ = let_tmp_rhs1_.unwrapInfo
        d_415_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_416_valueOrError3_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out63_: Wrappers.Result
        out63_ = default__.DeriveKeysFromIntermediateMaterial(d_413_intermediateMaterial_, algorithmSuite, encryptionContext, d_406_cryptoPrimitives_)
        d_416_valueOrError3_ = out63_
        if (d_416_valueOrError3_).IsFailure():
            res = (d_416_valueOrError3_).PropagateFailure()
            return res
        d_415_derivedKeys_ = (d_416_valueOrError3_).Extract()
        let_tmp_rhs2_ = d_415_derivedKeys_
        d_417_pdkEncryptionKey_ = let_tmp_rhs2_.pdkEncryptionKey
        d_418_symmetricSigningKey_ = let_tmp_rhs2_.symmetricSigningKey
        d_419_iv_: _dafny.Seq
        d_419_iv_ = _dafny.Seq([0 for d_420___v0_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_421_tagIndex_: int
        d_421_tagIndex_ = (len(d_409_encryptedPdk_)) - (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))
        d_422_aad_: _dafny.Seq
        d_423_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_423_valueOrError4_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_423_valueOrError4_).IsFailure():
            res = (d_423_valueOrError4_).PropagateFailure()
            return res
        d_422_aad_ = (d_423_valueOrError4_).Extract()
        d_424_decInput_: software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput
        d_424_decInput_ = software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput_AESDecryptInput(((algorithmSuite).encrypt).AES__GCM, d_417_pdkEncryptionKey_, _dafny.Seq((d_409_encryptedPdk_)[:d_421_tagIndex_:]), _dafny.Seq((d_409_encryptedPdk_)[d_421_tagIndex_::]), d_419_iv_, d_422_aad_)
        d_425_decOutR_: Wrappers.Result
        out64_: Wrappers.Result
        out64_ = (d_406_cryptoPrimitives_).AESDecrypt(d_424_decInput_)
        d_425_decOutR_ = out64_
        d_426_plaintextDataKey_: _dafny.Seq
        d_427_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda45_(d_428_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives(d_428_e_)

        d_427_valueOrError5_ = (d_425_decOutR_).MapFailure(lambda45_)
        if (d_427_valueOrError5_).IsFailure():
            res = (d_427_valueOrError5_).PropagateFailure()
            return res
        d_426_plaintextDataKey_ = (d_427_valueOrError5_).Extract()
        d_429_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_429_valueOrError6_ = Wrappers.default__.Need((len(d_426_plaintextDataKey_)) == (AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Decrypt length")))
        if (d_429_valueOrError6_).IsFailure():
            res = (d_429_valueOrError6_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(IntermediateUnwrapOutput_IntermediateUnwrapOutput(d_426_plaintextDataKey_, d_418_symmetricSigningKey_, d_414_unwrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateWrap(generateAndWrap, plaintextDataKey, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_430_maybeCrypto_: Wrappers.Result
        out65_: Wrappers.Result
        out65_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_430_maybeCrypto_ = out65_
        d_431_cryptoPrimitivesX_: software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient
        d_432_valueOrError0_: Wrappers.Result = None
        def lambda46_(d_433_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives(d_433_e_)

        d_432_valueOrError0_ = (d_430_maybeCrypto_).MapFailure(lambda46_)
        if (d_432_valueOrError0_).IsFailure():
            res = (d_432_valueOrError0_).PropagateFailure()
            return res
        d_431_cryptoPrimitivesX_ = (d_432_valueOrError0_).Extract()
        d_434_cryptoPrimitives_: software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient
        d_434_cryptoPrimitives_ = d_431_cryptoPrimitivesX_
        d_435_generateAndWrapOutput_: MaterialWrapping.GenerateAndWrapOutput
        d_436_valueOrError1_: Wrappers.Result = None
        out66_: Wrappers.Result
        out66_ = (generateAndWrap).Invoke(MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput(algorithmSuite, encryptionContext))
        d_436_valueOrError1_ = out66_
        if (d_436_valueOrError1_).IsFailure():
            res = (d_436_valueOrError1_).PropagateFailure()
            return res
        d_435_generateAndWrapOutput_ = (d_436_valueOrError1_).Extract()
        let_tmp_rhs3_ = d_435_generateAndWrapOutput_
        d_437_intermediateMaterial_ = let_tmp_rhs3_.plaintextMaterial
        d_438_providerWrappedIkm_ = let_tmp_rhs3_.wrappedMaterial
        d_439_wrapInfo_ = let_tmp_rhs3_.wrapInfo
        d_440_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_441_valueOrError2_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out67_: Wrappers.Result
        out67_ = default__.DeriveKeysFromIntermediateMaterial(d_437_intermediateMaterial_, algorithmSuite, encryptionContext, d_434_cryptoPrimitives_)
        d_441_valueOrError2_ = out67_
        if (d_441_valueOrError2_).IsFailure():
            res = (d_441_valueOrError2_).PropagateFailure()
            return res
        d_440_derivedKeys_ = (d_441_valueOrError2_).Extract()
        let_tmp_rhs4_ = d_440_derivedKeys_
        d_442_pdkEncryptionKey_ = let_tmp_rhs4_.pdkEncryptionKey
        d_443_symmetricSigningKey_ = let_tmp_rhs4_.symmetricSigningKey
        d_444_iv_: _dafny.Seq
        d_444_iv_ = _dafny.Seq([0 for d_445___v1_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_446_aad_: _dafny.Seq
        d_447_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_447_valueOrError3_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_447_valueOrError3_).IsFailure():
            res = (d_447_valueOrError3_).PropagateFailure()
            return res
        d_446_aad_ = (d_447_valueOrError3_).Extract()
        d_448_encInput_: software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput
        d_448_encInput_ = software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput_AESEncryptInput(((algorithmSuite).encrypt).AES__GCM, d_444_iv_, d_442_pdkEncryptionKey_, plaintextDataKey, d_446_aad_)
        d_449_encOutR_: Wrappers.Result
        out68_: Wrappers.Result
        out68_ = (d_434_cryptoPrimitives_).AESEncrypt(d_448_encInput_)
        d_449_encOutR_ = out68_
        d_450_encryptedPdk_: software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput
        d_451_valueOrError4_: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput.default())()
        def lambda47_(d_452_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives(d_452_e_)

        d_451_valueOrError4_ = (d_449_encOutR_).MapFailure(lambda47_)
        if (d_451_valueOrError4_).IsFailure():
            res = (d_451_valueOrError4_).PropagateFailure()
            return res
        d_450_encryptedPdk_ = (d_451_valueOrError4_).Extract()
        d_453_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_453_valueOrError5_ = Wrappers.default__.Need((len(((d_450_encryptedPdk_).cipherText) + ((d_450_encryptedPdk_).authTag))) == ((AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Encrypt length")))
        if (d_453_valueOrError5_).IsFailure():
            res = (d_453_valueOrError5_).PropagateFailure()
            return res
        d_454_serializedMaterial_: _dafny.Seq
        d_454_serializedMaterial_ = (((d_450_encryptedPdk_).cipherText) + ((d_450_encryptedPdk_).authTag)) + (d_438_providerWrappedIkm_)
        res = Wrappers.Result_Success(IntermediateWrapOutput_IntermediateWrapOutput(d_454_serializedMaterial_, d_443_symmetricSigningKey_, d_439_wrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateGenerateAndWrap(generateAndWrap, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_455_maybeCrypto_: Wrappers.Result
        out69_: Wrappers.Result
        out69_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_455_maybeCrypto_ = out69_
        d_456_cryptoPrimitives_: software.amazon.cryptography.primitives.internaldafny.types.IAwsCryptographicPrimitivesClient
        d_457_valueOrError0_: Wrappers.Result = None
        def lambda48_(d_458_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives(d_458_e_)

        d_457_valueOrError0_ = (d_455_maybeCrypto_).MapFailure(lambda48_)
        if (d_457_valueOrError0_).IsFailure():
            res = (d_457_valueOrError0_).PropagateFailure()
            return res
        d_456_cryptoPrimitives_ = (d_457_valueOrError0_).Extract()
        d_459_generateBytesResult_: Wrappers.Result
        out70_: Wrappers.Result
        out70_ = (d_456_cryptoPrimitives_).GenerateRandomBytes(software.amazon.cryptography.primitives.internaldafny.types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)))
        d_459_generateBytesResult_ = out70_
        d_460_plaintextDataKey_: _dafny.Seq
        d_461_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda49_(d_462_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives(d_462_e_)

        d_461_valueOrError1_ = (d_459_generateBytesResult_).MapFailure(lambda49_)
        if (d_461_valueOrError1_).IsFailure():
            res = (d_461_valueOrError1_).PropagateFailure()
            return res
        d_460_plaintextDataKey_ = (d_461_valueOrError1_).Extract()
        d_463_wrapOutput_: IntermediateWrapOutput
        d_464_valueOrError2_: Wrappers.Result = None
        out71_: Wrappers.Result
        out71_ = default__.IntermediateWrap(generateAndWrap, d_460_plaintextDataKey_, algorithmSuite, encryptionContext)
        d_464_valueOrError2_ = out71_
        if (d_464_valueOrError2_).IsFailure():
            res = (d_464_valueOrError2_).PropagateFailure()
            return res
        d_463_wrapOutput_ = (d_464_valueOrError2_).Extract()
        res = Wrappers.Result_Success(IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput(d_460_plaintextDataKey_, (d_463_wrapOutput_).wrappedMaterial, (d_463_wrapOutput_).symmetricSigningKey, (d_463_wrapOutput_).wrapInfo))
        return res
        return res

    @staticmethod
    def DeserializeIntermediateWrappedMaterial(material, algSuite):
        d_465_valueOrError0_ = Wrappers.default__.Need((len(material)) >= ((AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to deserialize Intermediate Key Wrapped material: too short.")))
        if (d_465_valueOrError0_).IsFailure():
            return (d_465_valueOrError0_).PropagateFailure()
        elif True:
            d_466_encryptedPdkLen_ = (AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))
            return Wrappers.Result_Success(DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial(_dafny.Seq((material)[:d_466_encryptedPdkLen_:]), _dafny.Seq((material)[d_466_encryptedPdkLen_::])))

    @staticmethod
    def DeriveKeysFromIntermediateMaterial(intermediateMaterial, algorithmSuite, encryptionContext, cryptoPrimitives):
        res: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        d_467_hkdfExtractInput_: software.amazon.cryptography.primitives.internaldafny.types.HkdfExtractInput
        d_467_hkdfExtractInput_ = software.amazon.cryptography.primitives.internaldafny.types.HkdfExtractInput_HkdfExtractInput((((algorithmSuite).commitment).HKDF).hmac, Wrappers.Option_None(), intermediateMaterial)
        d_468_maybePseudoRandomKey_: Wrappers.Result
        out72_: Wrappers.Result
        out72_ = (cryptoPrimitives).HkdfExtract(d_467_hkdfExtractInput_)
        d_468_maybePseudoRandomKey_ = out72_
        d_469_pseudoRandomKey_: _dafny.Seq
        d_470_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda50_(d_471_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives(d_471_e_)

        d_470_valueOrError0_ = (d_468_maybePseudoRandomKey_).MapFailure(lambda50_)
        if (d_470_valueOrError0_).IsFailure():
            res = (d_470_valueOrError0_).PropagateFailure()
            return res
        d_469_pseudoRandomKey_ = (d_470_valueOrError0_).Extract()
        d_472_symmetricSigningKeyInput_: software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput
        d_472_symmetricSigningKeyInput_ = software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput_HkdfExpandInput((((algorithmSuite).commitment).HKDF).hmac, d_469_pseudoRandomKey_, default__.KEYWRAP__MAC__INFO, (((algorithmSuite).commitment).HKDF).outputKeyLength)
        d_473_pdkEncryptionKeyInput_: software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput
        def iife20_(_pat_let5_0):
            def iife21_(d_474_dt__update__tmp_h0_):
                def iife22_(_pat_let6_0):
                    def iife23_(d_475_dt__update_hinfo_h0_):
                        return software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput_HkdfExpandInput((d_474_dt__update__tmp_h0_).digestAlgorithm, (d_474_dt__update__tmp_h0_).prk, d_475_dt__update_hinfo_h0_, (d_474_dt__update__tmp_h0_).expectedLength)
                    return iife23_(_pat_let6_0)
                return iife22_(default__.KEYWRAP__ENC__INFO)
            return iife21_(_pat_let5_0)
        d_473_pdkEncryptionKeyInput_ = iife20_(d_472_symmetricSigningKeyInput_)
        d_476_maybeSymmetricSigningKey_: Wrappers.Result
        out73_: Wrappers.Result
        out73_ = (cryptoPrimitives).HkdfExpand(d_472_symmetricSigningKeyInput_)
        d_476_maybeSymmetricSigningKey_ = out73_
        d_477_symmetricSigningKey_: _dafny.Seq
        d_478_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda51_(d_479_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives(d_479_e_)

        d_478_valueOrError1_ = (d_476_maybeSymmetricSigningKey_).MapFailure(lambda51_)
        if (d_478_valueOrError1_).IsFailure():
            res = (d_478_valueOrError1_).PropagateFailure()
            return res
        d_477_symmetricSigningKey_ = (d_478_valueOrError1_).Extract()
        d_480_maybePdkEncryptionKey_: Wrappers.Result
        out74_: Wrappers.Result
        out74_ = (cryptoPrimitives).HkdfExpand(d_473_pdkEncryptionKeyInput_)
        d_480_maybePdkEncryptionKey_ = out74_
        d_481_pdkEncryptionKey_: _dafny.Seq
        d_482_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda52_(d_483_e_):
            return software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographyPrimitives(d_483_e_)

        d_482_valueOrError2_ = (d_480_maybePdkEncryptionKey_).MapFailure(lambda52_)
        if (d_482_valueOrError2_).IsFailure():
            res = (d_482_valueOrError2_).PropagateFailure()
            return res
        d_481_pdkEncryptionKey_ = (d_482_valueOrError2_).Extract()
        res = Wrappers.Result_Success(PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys(d_481_pdkEncryptionKey_, d_477_symmetricSigningKey_))
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

