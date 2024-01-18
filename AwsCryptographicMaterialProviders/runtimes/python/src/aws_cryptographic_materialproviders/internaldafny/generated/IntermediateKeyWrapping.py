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
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
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
import Relations
import Seq_MergeSort
import Math
import Seq
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import DafnyLibraries
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
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
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
        d_403_cryptoPrimitives_: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient
        d_404_valueOrError0_: Wrappers.Result = None
        def lambda44_(d_405_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_405_e_)

        d_404_valueOrError0_ = (d_402_maybeCrypto_).MapFailure(lambda44_)
        if (d_404_valueOrError0_).IsFailure():
            res = (d_404_valueOrError0_).PropagateFailure()
            return res
        d_403_cryptoPrimitives_ = (d_404_valueOrError0_).Extract()
        d_406_deserializedWrapped_: DeserializedIntermediateWrappedMaterial
        d_407_valueOrError1_: Wrappers.Result = Wrappers.Result.default(DeserializedIntermediateWrappedMaterial.default())()
        d_407_valueOrError1_ = default__.DeserializeIntermediateWrappedMaterial(wrappedMaterial, algorithmSuite)
        if (d_407_valueOrError1_).IsFailure():
            res = (d_407_valueOrError1_).PropagateFailure()
            return res
        d_406_deserializedWrapped_ = (d_407_valueOrError1_).Extract()
        let_tmp_rhs0_ = d_406_deserializedWrapped_
        d_408_encryptedPdk_ = let_tmp_rhs0_.encryptedPdk
        d_409_providerWrappedIkm_ = let_tmp_rhs0_.providerWrappedIkm
        d_410_unwrapOutput_: MaterialWrapping.UnwrapOutput
        d_411_valueOrError2_: Wrappers.Result = None
        out62_: Wrappers.Result
        out62_ = (unwrap).Invoke(MaterialWrapping.UnwrapInput_UnwrapInput(d_409_providerWrappedIkm_, algorithmSuite, encryptionContext))
        d_411_valueOrError2_ = out62_
        if (d_411_valueOrError2_).IsFailure():
            res = (d_411_valueOrError2_).PropagateFailure()
            return res
        d_410_unwrapOutput_ = (d_411_valueOrError2_).Extract()
        let_tmp_rhs1_ = d_410_unwrapOutput_
        d_412_intermediateMaterial_ = let_tmp_rhs1_.unwrappedMaterial
        d_413_unwrapInfo_ = let_tmp_rhs1_.unwrapInfo
        d_414_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_415_valueOrError3_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out63_: Wrappers.Result
        out63_ = default__.DeriveKeysFromIntermediateMaterial(d_412_intermediateMaterial_, algorithmSuite, encryptionContext, d_403_cryptoPrimitives_)
        d_415_valueOrError3_ = out63_
        if (d_415_valueOrError3_).IsFailure():
            res = (d_415_valueOrError3_).PropagateFailure()
            return res
        d_414_derivedKeys_ = (d_415_valueOrError3_).Extract()
        let_tmp_rhs2_ = d_414_derivedKeys_
        d_416_pdkEncryptionKey_ = let_tmp_rhs2_.pdkEncryptionKey
        d_417_symmetricSigningKey_ = let_tmp_rhs2_.symmetricSigningKey
        d_418_iv_: _dafny.Seq
        d_418_iv_ = _dafny.Seq([0 for d_419___v0_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_420_tagIndex_: int
        d_420_tagIndex_ = (len(d_408_encryptedPdk_)) - (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))
        d_421_aad_: _dafny.Seq
        d_422_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_422_valueOrError4_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_422_valueOrError4_).IsFailure():
            res = (d_422_valueOrError4_).PropagateFailure()
            return res
        d_421_aad_ = (d_422_valueOrError4_).Extract()
        d_423_decInput_: software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput
        d_423_decInput_ = software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput(((algorithmSuite).encrypt).AES__GCM, d_416_pdkEncryptionKey_, _dafny.Seq((d_408_encryptedPdk_)[:d_420_tagIndex_:]), _dafny.Seq((d_408_encryptedPdk_)[d_420_tagIndex_::]), d_418_iv_, d_421_aad_)
        d_424_decOutR_: Wrappers.Result
        out64_: Wrappers.Result
        out64_ = (d_403_cryptoPrimitives_).AESDecrypt(d_423_decInput_)
        d_424_decOutR_ = out64_
        d_425_plaintextDataKey_: _dafny.Seq
        d_426_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda45_(d_427_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_427_e_)

        d_426_valueOrError5_ = (d_424_decOutR_).MapFailure(lambda45_)
        if (d_426_valueOrError5_).IsFailure():
            res = (d_426_valueOrError5_).PropagateFailure()
            return res
        d_425_plaintextDataKey_ = (d_426_valueOrError5_).Extract()
        d_428_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_428_valueOrError6_ = Wrappers.default__.Need((len(d_425_plaintextDataKey_)) == (AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Decrypt length")))
        if (d_428_valueOrError6_).IsFailure():
            res = (d_428_valueOrError6_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(IntermediateUnwrapOutput_IntermediateUnwrapOutput(d_425_plaintextDataKey_, d_417_symmetricSigningKey_, d_413_unwrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateWrap(generateAndWrap, plaintextDataKey, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_429_maybeCrypto_: Wrappers.Result
        out65_: Wrappers.Result
        out65_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_429_maybeCrypto_ = out65_
        d_430_cryptoPrimitives_: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient
        d_431_valueOrError0_: Wrappers.Result = None
        def lambda46_(d_432_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_432_e_)

        d_431_valueOrError0_ = (d_429_maybeCrypto_).MapFailure(lambda46_)
        if (d_431_valueOrError0_).IsFailure():
            res = (d_431_valueOrError0_).PropagateFailure()
            return res
        d_430_cryptoPrimitives_ = (d_431_valueOrError0_).Extract()
        d_433_generateAndWrapOutput_: MaterialWrapping.GenerateAndWrapOutput
        d_434_valueOrError1_: Wrappers.Result = None
        out66_: Wrappers.Result
        out66_ = (generateAndWrap).Invoke(MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput(algorithmSuite, encryptionContext))
        d_434_valueOrError1_ = out66_
        if (d_434_valueOrError1_).IsFailure():
            res = (d_434_valueOrError1_).PropagateFailure()
            return res
        d_433_generateAndWrapOutput_ = (d_434_valueOrError1_).Extract()
        let_tmp_rhs3_ = d_433_generateAndWrapOutput_
        d_435_intermediateMaterial_ = let_tmp_rhs3_.plaintextMaterial
        d_436_providerWrappedIkm_ = let_tmp_rhs3_.wrappedMaterial
        d_437_wrapInfo_ = let_tmp_rhs3_.wrapInfo
        d_438_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_439_valueOrError2_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out67_: Wrappers.Result
        out67_ = default__.DeriveKeysFromIntermediateMaterial(d_435_intermediateMaterial_, algorithmSuite, encryptionContext, d_430_cryptoPrimitives_)
        d_439_valueOrError2_ = out67_
        if (d_439_valueOrError2_).IsFailure():
            res = (d_439_valueOrError2_).PropagateFailure()
            return res
        d_438_derivedKeys_ = (d_439_valueOrError2_).Extract()
        let_tmp_rhs4_ = d_438_derivedKeys_
        d_440_pdkEncryptionKey_ = let_tmp_rhs4_.pdkEncryptionKey
        d_441_symmetricSigningKey_ = let_tmp_rhs4_.symmetricSigningKey
        d_442_iv_: _dafny.Seq
        d_442_iv_ = _dafny.Seq([0 for d_443___v1_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_444_aad_: _dafny.Seq
        d_445_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_445_valueOrError3_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_445_valueOrError3_).IsFailure():
            res = (d_445_valueOrError3_).PropagateFailure()
            return res
        d_444_aad_ = (d_445_valueOrError3_).Extract()
        d_446_encInput_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput
        d_446_encInput_ = software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput_AESEncryptInput(((algorithmSuite).encrypt).AES__GCM, d_442_iv_, d_440_pdkEncryptionKey_, plaintextDataKey, d_444_aad_)
        d_447_encOutR_: Wrappers.Result
        out68_: Wrappers.Result
        out68_ = (d_430_cryptoPrimitives_).AESEncrypt(d_446_encInput_)
        d_447_encOutR_ = out68_
        d_448_encryptedPdk_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_449_valueOrError4_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        def lambda47_(d_450_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_450_e_)

        d_449_valueOrError4_ = (d_447_encOutR_).MapFailure(lambda47_)
        if (d_449_valueOrError4_).IsFailure():
            res = (d_449_valueOrError4_).PropagateFailure()
            return res
        d_448_encryptedPdk_ = (d_449_valueOrError4_).Extract()
        d_451_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_451_valueOrError5_ = Wrappers.default__.Need((len(((d_448_encryptedPdk_).cipherText) + ((d_448_encryptedPdk_).authTag))) == ((AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Encrypt length")))
        if (d_451_valueOrError5_).IsFailure():
            res = (d_451_valueOrError5_).PropagateFailure()
            return res
        d_452_serializedMaterial_: _dafny.Seq
        d_452_serializedMaterial_ = (((d_448_encryptedPdk_).cipherText) + ((d_448_encryptedPdk_).authTag)) + (d_436_providerWrappedIkm_)
        res = Wrappers.Result_Success(IntermediateWrapOutput_IntermediateWrapOutput(d_452_serializedMaterial_, d_441_symmetricSigningKey_, d_437_wrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateGenerateAndWrap(generateAndWrap, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_453_maybeCrypto_: Wrappers.Result
        out69_: Wrappers.Result
        out69_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_453_maybeCrypto_ = out69_
        d_454_cryptoPrimitives_: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient
        d_455_valueOrError0_: Wrappers.Result = None
        def lambda48_(d_456_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_456_e_)

        d_455_valueOrError0_ = (d_453_maybeCrypto_).MapFailure(lambda48_)
        if (d_455_valueOrError0_).IsFailure():
            res = (d_455_valueOrError0_).PropagateFailure()
            return res
        d_454_cryptoPrimitives_ = (d_455_valueOrError0_).Extract()
        d_457_generateBytesResult_: Wrappers.Result
        out70_: Wrappers.Result
        out70_ = (d_454_cryptoPrimitives_).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)))
        d_457_generateBytesResult_ = out70_
        d_458_plaintextDataKey_: _dafny.Seq
        d_459_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda49_(d_460_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_460_e_)

        d_459_valueOrError1_ = (d_457_generateBytesResult_).MapFailure(lambda49_)
        if (d_459_valueOrError1_).IsFailure():
            res = (d_459_valueOrError1_).PropagateFailure()
            return res
        d_458_plaintextDataKey_ = (d_459_valueOrError1_).Extract()
        d_461_wrapOutput_: IntermediateWrapOutput
        d_462_valueOrError2_: Wrappers.Result = None
        out71_: Wrappers.Result
        out71_ = default__.IntermediateWrap(generateAndWrap, d_458_plaintextDataKey_, algorithmSuite, encryptionContext)
        d_462_valueOrError2_ = out71_
        if (d_462_valueOrError2_).IsFailure():
            res = (d_462_valueOrError2_).PropagateFailure()
            return res
        d_461_wrapOutput_ = (d_462_valueOrError2_).Extract()
        res = Wrappers.Result_Success(IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput(d_458_plaintextDataKey_, (d_461_wrapOutput_).wrappedMaterial, (d_461_wrapOutput_).symmetricSigningKey, (d_461_wrapOutput_).wrapInfo))
        return res
        return res

    @staticmethod
    def DeserializeIntermediateWrappedMaterial(material, algSuite):
        d_463_valueOrError0_ = Wrappers.default__.Need((len(material)) >= ((AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to deserialize Intermediate Key Wrapped material: too short.")))
        if (d_463_valueOrError0_).IsFailure():
            return (d_463_valueOrError0_).PropagateFailure()
        elif True:
            d_464_encryptedPdkLen_ = (AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))
            return Wrappers.Result_Success(DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial(_dafny.Seq((material)[:d_464_encryptedPdkLen_:]), _dafny.Seq((material)[d_464_encryptedPdkLen_::])))

    @staticmethod
    def DeriveKeysFromIntermediateMaterial(intermediateMaterial, algorithmSuite, encryptionContext, cryptoPrimitives):
        res: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        d_465_hkdfExtractInput_: software_amazon_cryptography_primitives_internaldafny_types.HkdfExtractInput
        d_465_hkdfExtractInput_ = software_amazon_cryptography_primitives_internaldafny_types.HkdfExtractInput_HkdfExtractInput((((algorithmSuite).commitment).HKDF).hmac, Wrappers.Option_None(), intermediateMaterial)
        d_466_maybePseudoRandomKey_: Wrappers.Result
        out72_: Wrappers.Result
        out72_ = (cryptoPrimitives).HkdfExtract(d_465_hkdfExtractInput_)
        d_466_maybePseudoRandomKey_ = out72_
        d_467_pseudoRandomKey_: _dafny.Seq
        d_468_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda50_(d_469_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_469_e_)

        d_468_valueOrError0_ = (d_466_maybePseudoRandomKey_).MapFailure(lambda50_)
        if (d_468_valueOrError0_).IsFailure():
            res = (d_468_valueOrError0_).PropagateFailure()
            return res
        d_467_pseudoRandomKey_ = (d_468_valueOrError0_).Extract()
        d_470_symmetricSigningKeyInput_: software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput
        d_470_symmetricSigningKeyInput_ = software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput_HkdfExpandInput((((algorithmSuite).commitment).HKDF).hmac, d_467_pseudoRandomKey_, default__.KEYWRAP__MAC__INFO, (((algorithmSuite).commitment).HKDF).outputKeyLength)
        d_471_pdkEncryptionKeyInput_: software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput
        def iife20_(_pat_let5_0):
            def iife21_(d_472_dt__update__tmp_h0_):
                def iife22_(_pat_let6_0):
                    def iife23_(d_473_dt__update_hinfo_h0_):
                        return software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput_HkdfExpandInput((d_472_dt__update__tmp_h0_).digestAlgorithm, (d_472_dt__update__tmp_h0_).prk, d_473_dt__update_hinfo_h0_, (d_472_dt__update__tmp_h0_).expectedLength)
                    return iife23_(_pat_let6_0)
                return iife22_(default__.KEYWRAP__ENC__INFO)
            return iife21_(_pat_let5_0)
        d_471_pdkEncryptionKeyInput_ = iife20_(d_470_symmetricSigningKeyInput_)
        d_474_maybeSymmetricSigningKey_: Wrappers.Result
        out73_: Wrappers.Result
        out73_ = (cryptoPrimitives).HkdfExpand(d_470_symmetricSigningKeyInput_)
        d_474_maybeSymmetricSigningKey_ = out73_
        d_475_symmetricSigningKey_: _dafny.Seq
        d_476_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda51_(d_477_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_477_e_)

        d_476_valueOrError1_ = (d_474_maybeSymmetricSigningKey_).MapFailure(lambda51_)
        if (d_476_valueOrError1_).IsFailure():
            res = (d_476_valueOrError1_).PropagateFailure()
            return res
        d_475_symmetricSigningKey_ = (d_476_valueOrError1_).Extract()
        d_478_maybePdkEncryptionKey_: Wrappers.Result
        out74_: Wrappers.Result
        out74_ = (cryptoPrimitives).HkdfExpand(d_471_pdkEncryptionKeyInput_)
        d_478_maybePdkEncryptionKey_ = out74_
        d_479_pdkEncryptionKey_: _dafny.Seq
        d_480_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda52_(d_481_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_481_e_)

        d_480_valueOrError2_ = (d_478_maybePdkEncryptionKey_).MapFailure(lambda52_)
        if (d_480_valueOrError2_).IsFailure():
            res = (d_480_valueOrError2_).PropagateFailure()
            return res
        d_479_pdkEncryptionKey_ = (d_480_valueOrError2_).Extract()
        res = Wrappers.Result_Success(PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys(d_479_pdkEncryptionKey_, d_475_symmetricSigningKey_))
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

