import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
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
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
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
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Constants
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
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
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
        d_320_maybeCrypto_: Wrappers.Result
        out68_: Wrappers.Result
        out68_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_320_maybeCrypto_ = out68_
        d_321_cryptoPrimitives_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_322_valueOrError0_: Wrappers.Result = None
        def lambda22_(d_323_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_323_e_)

        d_322_valueOrError0_ = (d_320_maybeCrypto_).MapFailure(lambda22_)
        if (d_322_valueOrError0_).IsFailure():
            res = (d_322_valueOrError0_).PropagateFailure()
            return res
        d_321_cryptoPrimitives_ = (d_322_valueOrError0_).Extract()
        d_324_deserializedWrapped_: DeserializedIntermediateWrappedMaterial
        d_325_valueOrError1_: Wrappers.Result = Wrappers.Result.default(DeserializedIntermediateWrappedMaterial.default())()
        d_325_valueOrError1_ = default__.DeserializeIntermediateWrappedMaterial(wrappedMaterial, algorithmSuite)
        if (d_325_valueOrError1_).IsFailure():
            res = (d_325_valueOrError1_).PropagateFailure()
            return res
        d_324_deserializedWrapped_ = (d_325_valueOrError1_).Extract()
        let_tmp_rhs6_ = d_324_deserializedWrapped_
        d_326_encryptedPdk_ = let_tmp_rhs6_.encryptedPdk
        d_327_providerWrappedIkm_ = let_tmp_rhs6_.providerWrappedIkm
        d_328_unwrapOutput_: MaterialWrapping.UnwrapOutput
        d_329_valueOrError2_: Wrappers.Result = None
        out69_: Wrappers.Result
        out69_ = (unwrap).Invoke(MaterialWrapping.UnwrapInput_UnwrapInput(d_327_providerWrappedIkm_, algorithmSuite, encryptionContext))
        d_329_valueOrError2_ = out69_
        if (d_329_valueOrError2_).IsFailure():
            res = (d_329_valueOrError2_).PropagateFailure()
            return res
        d_328_unwrapOutput_ = (d_329_valueOrError2_).Extract()
        let_tmp_rhs7_ = d_328_unwrapOutput_
        d_330_intermediateMaterial_ = let_tmp_rhs7_.unwrappedMaterial
        d_331_unwrapInfo_ = let_tmp_rhs7_.unwrapInfo
        d_332_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_333_valueOrError3_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out70_: Wrappers.Result
        out70_ = default__.DeriveKeysFromIntermediateMaterial(d_330_intermediateMaterial_, algorithmSuite, encryptionContext, d_321_cryptoPrimitives_)
        d_333_valueOrError3_ = out70_
        if (d_333_valueOrError3_).IsFailure():
            res = (d_333_valueOrError3_).PropagateFailure()
            return res
        d_332_derivedKeys_ = (d_333_valueOrError3_).Extract()
        let_tmp_rhs8_ = d_332_derivedKeys_
        d_334_pdkEncryptionKey_ = let_tmp_rhs8_.pdkEncryptionKey
        d_335_symmetricSigningKey_ = let_tmp_rhs8_.symmetricSigningKey
        d_336_iv_: _dafny.Seq
        d_336_iv_ = _dafny.Seq([0 for d_337___v0_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_338_tagIndex_: int
        d_338_tagIndex_ = (len(d_326_encryptedPdk_)) - (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))
        d_339_aad_: _dafny.Seq
        d_340_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_340_valueOrError4_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_340_valueOrError4_).IsFailure():
            res = (d_340_valueOrError4_).PropagateFailure()
            return res
        d_339_aad_ = (d_340_valueOrError4_).Extract()
        d_341_decInput_: software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput
        d_341_decInput_ = software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput(((algorithmSuite).encrypt).AES__GCM, d_334_pdkEncryptionKey_, _dafny.Seq((d_326_encryptedPdk_)[:d_338_tagIndex_:]), _dafny.Seq((d_326_encryptedPdk_)[d_338_tagIndex_::]), d_336_iv_, d_339_aad_)
        d_342_decOutR_: Wrappers.Result
        out71_: Wrappers.Result
        out71_ = (d_321_cryptoPrimitives_).AESDecrypt(d_341_decInput_)
        d_342_decOutR_ = out71_
        d_343_plaintextDataKey_: _dafny.Seq
        d_344_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda23_(d_345_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_345_e_)

        d_344_valueOrError5_ = (d_342_decOutR_).MapFailure(lambda23_)
        if (d_344_valueOrError5_).IsFailure():
            res = (d_344_valueOrError5_).PropagateFailure()
            return res
        d_343_plaintextDataKey_ = (d_344_valueOrError5_).Extract()
        d_346_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_346_valueOrError6_ = Wrappers.default__.Need((len(d_343_plaintextDataKey_)) == (AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Decrypt length")))
        if (d_346_valueOrError6_).IsFailure():
            res = (d_346_valueOrError6_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(IntermediateUnwrapOutput_IntermediateUnwrapOutput(d_343_plaintextDataKey_, d_335_symmetricSigningKey_, d_331_unwrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateWrap(generateAndWrap, plaintextDataKey, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_347_maybeCrypto_: Wrappers.Result
        out72_: Wrappers.Result
        out72_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_347_maybeCrypto_ = out72_
        d_348_cryptoPrimitives_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_349_valueOrError0_: Wrappers.Result = None
        def lambda24_(d_350_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_350_e_)

        d_349_valueOrError0_ = (d_347_maybeCrypto_).MapFailure(lambda24_)
        if (d_349_valueOrError0_).IsFailure():
            res = (d_349_valueOrError0_).PropagateFailure()
            return res
        d_348_cryptoPrimitives_ = (d_349_valueOrError0_).Extract()
        d_351_generateAndWrapOutput_: MaterialWrapping.GenerateAndWrapOutput
        d_352_valueOrError1_: Wrappers.Result = None
        out73_: Wrappers.Result
        out73_ = (generateAndWrap).Invoke(MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput(algorithmSuite, encryptionContext))
        d_352_valueOrError1_ = out73_
        if (d_352_valueOrError1_).IsFailure():
            res = (d_352_valueOrError1_).PropagateFailure()
            return res
        d_351_generateAndWrapOutput_ = (d_352_valueOrError1_).Extract()
        let_tmp_rhs9_ = d_351_generateAndWrapOutput_
        d_353_intermediateMaterial_ = let_tmp_rhs9_.plaintextMaterial
        d_354_providerWrappedIkm_ = let_tmp_rhs9_.wrappedMaterial
        d_355_wrapInfo_ = let_tmp_rhs9_.wrapInfo
        d_356_derivedKeys_: PdkEncryptionAndSymmetricSigningKeys
        d_357_valueOrError2_: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        out74_: Wrappers.Result
        out74_ = default__.DeriveKeysFromIntermediateMaterial(d_353_intermediateMaterial_, algorithmSuite, encryptionContext, d_348_cryptoPrimitives_)
        d_357_valueOrError2_ = out74_
        if (d_357_valueOrError2_).IsFailure():
            res = (d_357_valueOrError2_).PropagateFailure()
            return res
        d_356_derivedKeys_ = (d_357_valueOrError2_).Extract()
        let_tmp_rhs10_ = d_356_derivedKeys_
        d_358_pdkEncryptionKey_ = let_tmp_rhs10_.pdkEncryptionKey
        d_359_symmetricSigningKey_ = let_tmp_rhs10_.symmetricSigningKey
        d_360_iv_: _dafny.Seq
        d_360_iv_ = _dafny.Seq([0 for d_361___v1_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_362_aad_: _dafny.Seq
        d_363_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_363_valueOrError3_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_363_valueOrError3_).IsFailure():
            res = (d_363_valueOrError3_).PropagateFailure()
            return res
        d_362_aad_ = (d_363_valueOrError3_).Extract()
        d_364_encInput_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput
        d_364_encInput_ = software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput_AESEncryptInput(((algorithmSuite).encrypt).AES__GCM, d_360_iv_, d_358_pdkEncryptionKey_, plaintextDataKey, d_362_aad_)
        d_365_encOutR_: Wrappers.Result
        out75_: Wrappers.Result
        out75_ = (d_348_cryptoPrimitives_).AESEncrypt(d_364_encInput_)
        d_365_encOutR_ = out75_
        d_366_encryptedPdk_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_367_valueOrError4_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        def lambda25_(d_368_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_368_e_)

        d_367_valueOrError4_ = (d_365_encOutR_).MapFailure(lambda25_)
        if (d_367_valueOrError4_).IsFailure():
            res = (d_367_valueOrError4_).PropagateFailure()
            return res
        d_366_encryptedPdk_ = (d_367_valueOrError4_).Extract()
        d_369_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_369_valueOrError5_ = Wrappers.default__.Need((len(((d_366_encryptedPdk_).cipherText) + ((d_366_encryptedPdk_).authTag))) == ((AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Encrypt length")))
        if (d_369_valueOrError5_).IsFailure():
            res = (d_369_valueOrError5_).PropagateFailure()
            return res
        d_370_serializedMaterial_: _dafny.Seq
        d_370_serializedMaterial_ = (((d_366_encryptedPdk_).cipherText) + ((d_366_encryptedPdk_).authTag)) + (d_354_providerWrappedIkm_)
        res = Wrappers.Result_Success(IntermediateWrapOutput_IntermediateWrapOutput(d_370_serializedMaterial_, d_359_symmetricSigningKey_, d_355_wrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateGenerateAndWrap(generateAndWrap, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_371_maybeCrypto_: Wrappers.Result
        out76_: Wrappers.Result
        out76_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_371_maybeCrypto_ = out76_
        d_372_cryptoPrimitives_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_373_valueOrError0_: Wrappers.Result = None
        def lambda26_(d_374_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_374_e_)

        d_373_valueOrError0_ = (d_371_maybeCrypto_).MapFailure(lambda26_)
        if (d_373_valueOrError0_).IsFailure():
            res = (d_373_valueOrError0_).PropagateFailure()
            return res
        d_372_cryptoPrimitives_ = (d_373_valueOrError0_).Extract()
        d_375_generateBytesResult_: Wrappers.Result
        out77_: Wrappers.Result
        out77_ = (d_372_cryptoPrimitives_).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)))
        d_375_generateBytesResult_ = out77_
        d_376_plaintextDataKey_: _dafny.Seq
        d_377_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda27_(d_378_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_378_e_)

        d_377_valueOrError1_ = (d_375_generateBytesResult_).MapFailure(lambda27_)
        if (d_377_valueOrError1_).IsFailure():
            res = (d_377_valueOrError1_).PropagateFailure()
            return res
        d_376_plaintextDataKey_ = (d_377_valueOrError1_).Extract()
        d_379_wrapOutput_: IntermediateWrapOutput
        d_380_valueOrError2_: Wrappers.Result = None
        out78_: Wrappers.Result
        out78_ = default__.IntermediateWrap(generateAndWrap, d_376_plaintextDataKey_, algorithmSuite, encryptionContext)
        d_380_valueOrError2_ = out78_
        if (d_380_valueOrError2_).IsFailure():
            res = (d_380_valueOrError2_).PropagateFailure()
            return res
        d_379_wrapOutput_ = (d_380_valueOrError2_).Extract()
        res = Wrappers.Result_Success(IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput(d_376_plaintextDataKey_, (d_379_wrapOutput_).wrappedMaterial, (d_379_wrapOutput_).symmetricSigningKey, (d_379_wrapOutput_).wrapInfo))
        return res
        return res

    @staticmethod
    def DeserializeIntermediateWrappedMaterial(material, algSuite):
        d_381_valueOrError0_ = Wrappers.default__.Need((len(material)) >= ((AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to deserialize Intermediate Key Wrapped material: too short.")))
        if (d_381_valueOrError0_).IsFailure():
            return (d_381_valueOrError0_).PropagateFailure()
        elif True:
            d_382_encryptedPdkLen_ = (AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))
            return Wrappers.Result_Success(DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial(_dafny.Seq((material)[:d_382_encryptedPdkLen_:]), _dafny.Seq((material)[d_382_encryptedPdkLen_::])))

    @staticmethod
    def DeriveKeysFromIntermediateMaterial(intermediateMaterial, algorithmSuite, encryptionContext, cryptoPrimitives):
        res: Wrappers.Result = Wrappers.Result.default(PdkEncryptionAndSymmetricSigningKeys.default())()
        d_383_hkdfExtractInput_: software_amazon_cryptography_primitives_internaldafny_types.HkdfExtractInput
        d_383_hkdfExtractInput_ = software_amazon_cryptography_primitives_internaldafny_types.HkdfExtractInput_HkdfExtractInput((((algorithmSuite).commitment).HKDF).hmac, Wrappers.Option_None(), intermediateMaterial)
        d_384_maybePseudoRandomKey_: Wrappers.Result
        out79_: Wrappers.Result
        out79_ = (cryptoPrimitives).HkdfExtract(d_383_hkdfExtractInput_)
        d_384_maybePseudoRandomKey_ = out79_
        d_385_pseudoRandomKey_: _dafny.Seq
        d_386_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda28_(d_387_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_387_e_)

        d_386_valueOrError0_ = (d_384_maybePseudoRandomKey_).MapFailure(lambda28_)
        if (d_386_valueOrError0_).IsFailure():
            res = (d_386_valueOrError0_).PropagateFailure()
            return res
        d_385_pseudoRandomKey_ = (d_386_valueOrError0_).Extract()
        d_388_symmetricSigningKeyInput_: software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput
        d_388_symmetricSigningKeyInput_ = software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput_HkdfExpandInput((((algorithmSuite).commitment).HKDF).hmac, d_385_pseudoRandomKey_, default__.KEYWRAP__MAC__INFO, (((algorithmSuite).commitment).HKDF).outputKeyLength)
        d_389_pdkEncryptionKeyInput_: software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput
        def iife19_(_pat_let8_0):
            def iife20_(d_390_dt__update__tmp_h0_):
                def iife21_(_pat_let9_0):
                    def iife22_(d_391_dt__update_hinfo_h0_):
                        return software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput_HkdfExpandInput((d_390_dt__update__tmp_h0_).digestAlgorithm, (d_390_dt__update__tmp_h0_).prk, d_391_dt__update_hinfo_h0_, (d_390_dt__update__tmp_h0_).expectedLength)
                    return iife22_(_pat_let9_0)
                return iife21_(default__.KEYWRAP__ENC__INFO)
            return iife20_(_pat_let8_0)
        d_389_pdkEncryptionKeyInput_ = iife19_(d_388_symmetricSigningKeyInput_)
        d_392_maybeSymmetricSigningKey_: Wrappers.Result
        out80_: Wrappers.Result
        out80_ = (cryptoPrimitives).HkdfExpand(d_388_symmetricSigningKeyInput_)
        d_392_maybeSymmetricSigningKey_ = out80_
        d_393_symmetricSigningKey_: _dafny.Seq
        d_394_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda29_(d_395_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_395_e_)

        d_394_valueOrError1_ = (d_392_maybeSymmetricSigningKey_).MapFailure(lambda29_)
        if (d_394_valueOrError1_).IsFailure():
            res = (d_394_valueOrError1_).PropagateFailure()
            return res
        d_393_symmetricSigningKey_ = (d_394_valueOrError1_).Extract()
        d_396_maybePdkEncryptionKey_: Wrappers.Result
        out81_: Wrappers.Result
        out81_ = (cryptoPrimitives).HkdfExpand(d_389_pdkEncryptionKeyInput_)
        d_396_maybePdkEncryptionKey_ = out81_
        d_397_pdkEncryptionKey_: _dafny.Seq
        d_398_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda30_(d_399_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_399_e_)

        d_398_valueOrError2_ = (d_396_maybePdkEncryptionKey_).MapFailure(lambda30_)
        if (d_398_valueOrError2_).IsFailure():
            res = (d_398_valueOrError2_).PropagateFailure()
            return res
        d_397_pdkEncryptionKey_ = (d_398_valueOrError2_).Extract()
        res = Wrappers.Result_Success(PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys(d_397_pdkEncryptionKey_, d_393_symmetricSigningKey_))
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

