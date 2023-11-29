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
import software_amazon_cryptography_keystore_internaldafny
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
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext

assert "IntermediateKeyWrapping" == __name__
IntermediateKeyWrapping = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IntermediateUnwrap(unwrap, wrappedMaterial, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_508_maybeCrypto_: Wrappers.Result
        out112_: Wrappers.Result
        out112_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_508_maybeCrypto_ = out112_
        d_509_cryptoPrimitives_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_510_valueOrError0_: Wrappers.Result = None
        def lambda44_(d_511_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_511_e_)

        d_510_valueOrError0_ = (d_508_maybeCrypto_).MapFailure(lambda44_)
        if (d_510_valueOrError0_).IsFailure():
            res = (d_510_valueOrError0_).PropagateFailure()
            return res
        d_509_cryptoPrimitives_ = (d_510_valueOrError0_).Extract()
        d_512_deserializedWrapped_: IntermediateKeyWrapping.DeserializedIntermediateWrappedMaterial
        d_513_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(IntermediateKeyWrapping.DeserializedIntermediateWrappedMaterial.default())()
        d_513_valueOrError1_ = IntermediateKeyWrapping.default__.DeserializeIntermediateWrappedMaterial(wrappedMaterial, algorithmSuite)
        if (d_513_valueOrError1_).IsFailure():
            res = (d_513_valueOrError1_).PropagateFailure()
            return res
        d_512_deserializedWrapped_ = (d_513_valueOrError1_).Extract()
        let_tmp_rhs6_ = d_512_deserializedWrapped_
        d_514_encryptedPdk_ = let_tmp_rhs6_.encryptedPdk
        d_515_providerWrappedIkm_ = let_tmp_rhs6_.providerWrappedIkm
        d_516_unwrapOutput_: MaterialWrapping.UnwrapOutput
        d_517_valueOrError2_: Wrappers.Result = None
        out113_: Wrappers.Result
        out113_ = (unwrap).Invoke(MaterialWrapping.UnwrapInput_UnwrapInput(d_515_providerWrappedIkm_, algorithmSuite, encryptionContext))
        d_517_valueOrError2_ = out113_
        if (d_517_valueOrError2_).IsFailure():
            res = (d_517_valueOrError2_).PropagateFailure()
            return res
        d_516_unwrapOutput_ = (d_517_valueOrError2_).Extract()
        let_tmp_rhs7_ = d_516_unwrapOutput_
        d_518_intermediateMaterial_ = let_tmp_rhs7_.unwrappedMaterial
        d_519_unwrapInfo_ = let_tmp_rhs7_.unwrapInfo
        d_520_derivedKeys_: IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys
        d_521_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys.default())()
        out114_: Wrappers.Result
        out114_ = IntermediateKeyWrapping.default__.DeriveKeysFromIntermediateMaterial(d_518_intermediateMaterial_, algorithmSuite, encryptionContext, d_509_cryptoPrimitives_)
        d_521_valueOrError3_ = out114_
        if (d_521_valueOrError3_).IsFailure():
            res = (d_521_valueOrError3_).PropagateFailure()
            return res
        d_520_derivedKeys_ = (d_521_valueOrError3_).Extract()
        let_tmp_rhs8_ = d_520_derivedKeys_
        d_522_pdkEncryptionKey_ = let_tmp_rhs8_.pdkEncryptionKey
        d_523_symmetricSigningKey_ = let_tmp_rhs8_.symmetricSigningKey
        d_524_iv_: _dafny.Seq
        d_524_iv_ = _dafny.Seq([0 for d_525___v0_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_526_tagIndex_: int
        d_526_tagIndex_ = (len(d_514_encryptedPdk_)) - (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))
        d_527_aad_: _dafny.Seq
        d_528_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_528_valueOrError4_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_528_valueOrError4_).IsFailure():
            res = (d_528_valueOrError4_).PropagateFailure()
            return res
        d_527_aad_ = (d_528_valueOrError4_).Extract()
        d_529_decInput_: software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput
        d_529_decInput_ = software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput(((algorithmSuite).encrypt).AES__GCM, d_522_pdkEncryptionKey_, _dafny.Seq((d_514_encryptedPdk_)[:d_526_tagIndex_:]), _dafny.Seq((d_514_encryptedPdk_)[d_526_tagIndex_::]), d_524_iv_, d_527_aad_)
        d_530_decOutR_: Wrappers.Result
        out115_: Wrappers.Result
        out115_ = (d_509_cryptoPrimitives_).AESDecrypt(d_529_decInput_)
        d_530_decOutR_ = out115_
        d_531_plaintextDataKey_: _dafny.Seq
        d_532_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda45_(d_533_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_533_e_)

        d_532_valueOrError5_ = (d_530_decOutR_).MapFailure(lambda45_)
        if (d_532_valueOrError5_).IsFailure():
            res = (d_532_valueOrError5_).PropagateFailure()
            return res
        d_531_plaintextDataKey_ = (d_532_valueOrError5_).Extract()
        d_534_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_534_valueOrError6_ = Wrappers.default__.Need((len(d_531_plaintextDataKey_)) == (AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Decrypt length")))
        if (d_534_valueOrError6_).IsFailure():
            res = (d_534_valueOrError6_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(IntermediateKeyWrapping.IntermediateUnwrapOutput_IntermediateUnwrapOutput(d_531_plaintextDataKey_, d_523_symmetricSigningKey_, d_519_unwrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateWrap(generateAndWrap, plaintextDataKey, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_535_maybeCrypto_: Wrappers.Result
        out116_: Wrappers.Result
        out116_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_535_maybeCrypto_ = out116_
        d_536_cryptoPrimitives_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_537_valueOrError0_: Wrappers.Result = None
        def lambda46_(d_538_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_538_e_)

        d_537_valueOrError0_ = (d_535_maybeCrypto_).MapFailure(lambda46_)
        if (d_537_valueOrError0_).IsFailure():
            res = (d_537_valueOrError0_).PropagateFailure()
            return res
        d_536_cryptoPrimitives_ = (d_537_valueOrError0_).Extract()
        d_539_generateAndWrapOutput_: MaterialWrapping.GenerateAndWrapOutput
        d_540_valueOrError1_: Wrappers.Result = None
        out117_: Wrappers.Result
        out117_ = (generateAndWrap).Invoke(MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput(algorithmSuite, encryptionContext))
        d_540_valueOrError1_ = out117_
        if (d_540_valueOrError1_).IsFailure():
            res = (d_540_valueOrError1_).PropagateFailure()
            return res
        d_539_generateAndWrapOutput_ = (d_540_valueOrError1_).Extract()
        let_tmp_rhs9_ = d_539_generateAndWrapOutput_
        d_541_intermediateMaterial_ = let_tmp_rhs9_.plaintextMaterial
        d_542_providerWrappedIkm_ = let_tmp_rhs9_.wrappedMaterial
        d_543_wrapInfo_ = let_tmp_rhs9_.wrapInfo
        d_544_derivedKeys_: IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys
        d_545_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys.default())()
        out118_: Wrappers.Result
        out118_ = IntermediateKeyWrapping.default__.DeriveKeysFromIntermediateMaterial(d_541_intermediateMaterial_, algorithmSuite, encryptionContext, d_536_cryptoPrimitives_)
        d_545_valueOrError2_ = out118_
        if (d_545_valueOrError2_).IsFailure():
            res = (d_545_valueOrError2_).PropagateFailure()
            return res
        d_544_derivedKeys_ = (d_545_valueOrError2_).Extract()
        let_tmp_rhs10_ = d_544_derivedKeys_
        d_546_pdkEncryptionKey_ = let_tmp_rhs10_.pdkEncryptionKey
        d_547_symmetricSigningKey_ = let_tmp_rhs10_.symmetricSigningKey
        d_548_iv_: _dafny.Seq
        d_548_iv_ = _dafny.Seq([0 for d_549___v1_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_550_aad_: _dafny.Seq
        d_551_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_551_valueOrError3_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_551_valueOrError3_).IsFailure():
            res = (d_551_valueOrError3_).PropagateFailure()
            return res
        d_550_aad_ = (d_551_valueOrError3_).Extract()
        d_552_encInput_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput
        d_552_encInput_ = software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput_AESEncryptInput(((algorithmSuite).encrypt).AES__GCM, d_548_iv_, d_546_pdkEncryptionKey_, plaintextDataKey, d_550_aad_)
        d_553_encOutR_: Wrappers.Result
        out119_: Wrappers.Result
        out119_ = (d_536_cryptoPrimitives_).AESEncrypt(d_552_encInput_)
        d_553_encOutR_ = out119_
        d_554_encryptedPdk_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_555_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        def lambda47_(d_556_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_556_e_)

        d_555_valueOrError4_ = (d_553_encOutR_).MapFailure(lambda47_)
        if (d_555_valueOrError4_).IsFailure():
            res = (d_555_valueOrError4_).PropagateFailure()
            return res
        d_554_encryptedPdk_ = (d_555_valueOrError4_).Extract()
        d_557_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_557_valueOrError5_ = Wrappers.default__.Need((len(((d_554_encryptedPdk_).cipherText) + ((d_554_encryptedPdk_).authTag))) == ((AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Encrypt length")))
        if (d_557_valueOrError5_).IsFailure():
            res = (d_557_valueOrError5_).PropagateFailure()
            return res
        d_558_serializedMaterial_: _dafny.Seq
        d_558_serializedMaterial_ = (((d_554_encryptedPdk_).cipherText) + ((d_554_encryptedPdk_).authTag)) + (d_542_providerWrappedIkm_)
        res = Wrappers.Result_Success(IntermediateKeyWrapping.IntermediateWrapOutput_IntermediateWrapOutput(d_558_serializedMaterial_, d_547_symmetricSigningKey_, d_543_wrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateGenerateAndWrap(generateAndWrap, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_559_maybeCrypto_: Wrappers.Result
        out120_: Wrappers.Result
        out120_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_559_maybeCrypto_ = out120_
        d_560_cryptoPrimitives_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_561_valueOrError0_: Wrappers.Result = None
        def lambda48_(d_562_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_562_e_)

        d_561_valueOrError0_ = (d_559_maybeCrypto_).MapFailure(lambda48_)
        if (d_561_valueOrError0_).IsFailure():
            res = (d_561_valueOrError0_).PropagateFailure()
            return res
        d_560_cryptoPrimitives_ = (d_561_valueOrError0_).Extract()
        d_563_generateBytesResult_: Wrappers.Result
        out121_: Wrappers.Result
        out121_ = (d_560_cryptoPrimitives_).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)))
        d_563_generateBytesResult_ = out121_
        d_564_plaintextDataKey_: _dafny.Seq
        d_565_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda49_(d_566_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_566_e_)

        d_565_valueOrError1_ = (d_563_generateBytesResult_).MapFailure(lambda49_)
        if (d_565_valueOrError1_).IsFailure():
            res = (d_565_valueOrError1_).PropagateFailure()
            return res
        d_564_plaintextDataKey_ = (d_565_valueOrError1_).Extract()
        d_567_wrapOutput_: IntermediateKeyWrapping.IntermediateWrapOutput
        d_568_valueOrError2_: Wrappers.Result = None
        out122_: Wrappers.Result
        out122_ = IntermediateKeyWrapping.default__.IntermediateWrap(generateAndWrap, d_564_plaintextDataKey_, algorithmSuite, encryptionContext)
        d_568_valueOrError2_ = out122_
        if (d_568_valueOrError2_).IsFailure():
            res = (d_568_valueOrError2_).PropagateFailure()
            return res
        d_567_wrapOutput_ = (d_568_valueOrError2_).Extract()
        res = Wrappers.Result_Success(IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput(d_564_plaintextDataKey_, (d_567_wrapOutput_).wrappedMaterial, (d_567_wrapOutput_).symmetricSigningKey, (d_567_wrapOutput_).wrapInfo))
        return res
        return res

    @staticmethod
    def DeserializeIntermediateWrappedMaterial(material, algSuite):
        d_569_valueOrError0_ = Wrappers.default__.Need((len(material)) >= ((AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to deserialize Intermediate Key Wrapped material: too short.")))
        if (d_569_valueOrError0_).IsFailure():
            return (d_569_valueOrError0_).PropagateFailure()
        elif True:
            d_570_encryptedPdkLen_ = (AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))
            return Wrappers.Result_Success(IntermediateKeyWrapping.DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial(_dafny.Seq((material)[:d_570_encryptedPdkLen_:]), _dafny.Seq((material)[d_570_encryptedPdkLen_::])))

    @staticmethod
    def DeriveKeysFromIntermediateMaterial(intermediateMaterial, algorithmSuite, encryptionContext, cryptoPrimitives):
        res: Wrappers.Result = Wrappers.Result_Success.default(IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys.default())()
        d_571_hkdfExtractInput_: software_amazon_cryptography_primitives_internaldafny_types.HkdfExtractInput
        d_571_hkdfExtractInput_ = software_amazon_cryptography_primitives_internaldafny_types.HkdfExtractInput_HkdfExtractInput((((algorithmSuite).commitment).HKDF).hmac, Wrappers.Option_None(), intermediateMaterial)
        d_572_maybePseudoRandomKey_: Wrappers.Result
        out123_: Wrappers.Result
        out123_ = (cryptoPrimitives).HkdfExtract(d_571_hkdfExtractInput_)
        d_572_maybePseudoRandomKey_ = out123_
        d_573_pseudoRandomKey_: _dafny.Seq
        d_574_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda50_(d_575_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_575_e_)

        d_574_valueOrError0_ = (d_572_maybePseudoRandomKey_).MapFailure(lambda50_)
        if (d_574_valueOrError0_).IsFailure():
            res = (d_574_valueOrError0_).PropagateFailure()
            return res
        d_573_pseudoRandomKey_ = (d_574_valueOrError0_).Extract()
        d_576_symmetricSigningKeyInput_: software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput
        d_576_symmetricSigningKeyInput_ = software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput_HkdfExpandInput((((algorithmSuite).commitment).HKDF).hmac, d_573_pseudoRandomKey_, (IntermediateKeyWrapping.default__).KEYWRAP__MAC__INFO, (((algorithmSuite).commitment).HKDF).outputKeyLength)
        d_577_pdkEncryptionKeyInput_: software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput
        def iife28_(_pat_let9_0):
            def iife29_(d_578_dt__update__tmp_h0_):
                def iife30_(_pat_let10_0):
                    def iife31_(d_579_dt__update_hinfo_h0_):
                        return software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput_HkdfExpandInput((d_578_dt__update__tmp_h0_).digestAlgorithm, (d_578_dt__update__tmp_h0_).prk, d_579_dt__update_hinfo_h0_, (d_578_dt__update__tmp_h0_).expectedLength)
                    return iife31_(_pat_let10_0)
                return iife30_((IntermediateKeyWrapping.default__).KEYWRAP__ENC__INFO)
            return iife29_(_pat_let9_0)
        d_577_pdkEncryptionKeyInput_ = iife28_(d_576_symmetricSigningKeyInput_)
        d_580_maybeSymmetricSigningKey_: Wrappers.Result
        out124_: Wrappers.Result
        out124_ = (cryptoPrimitives).HkdfExpand(d_576_symmetricSigningKeyInput_)
        d_580_maybeSymmetricSigningKey_ = out124_
        d_581_symmetricSigningKey_: _dafny.Seq
        d_582_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda51_(d_583_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_583_e_)

        d_582_valueOrError1_ = (d_580_maybeSymmetricSigningKey_).MapFailure(lambda51_)
        if (d_582_valueOrError1_).IsFailure():
            res = (d_582_valueOrError1_).PropagateFailure()
            return res
        d_581_symmetricSigningKey_ = (d_582_valueOrError1_).Extract()
        d_584_maybePdkEncryptionKey_: Wrappers.Result
        out125_: Wrappers.Result
        out125_ = (cryptoPrimitives).HkdfExpand(d_577_pdkEncryptionKeyInput_)
        d_584_maybePdkEncryptionKey_ = out125_
        d_585_pdkEncryptionKey_: _dafny.Seq
        d_586_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda52_(d_587_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_587_e_)

        d_586_valueOrError2_ = (d_584_maybePdkEncryptionKey_).MapFailure(lambda52_)
        if (d_586_valueOrError2_).IsFailure():
            res = (d_586_valueOrError2_).PropagateFailure()
            return res
        d_585_pdkEncryptionKey_ = (d_586_valueOrError2_).Extract()
        res = Wrappers.Result_Success(IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys(d_585_pdkEncryptionKey_, d_581_symmetricSigningKey_))
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
        return isinstance(self, IntermediateKeyWrapping.IntermediateUnwrapOutput_IntermediateUnwrapOutput)

class IntermediateUnwrapOutput_IntermediateUnwrapOutput(IntermediateUnwrapOutput, NamedTuple('IntermediateUnwrapOutput', [('plaintextDataKey', Any), ('symmetricSigningKey', Any), ('unwrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'IntermediateKeyWrapping.IntermediateUnwrapOutput.IntermediateUnwrapOutput({_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.unwrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, IntermediateKeyWrapping.IntermediateUnwrapOutput_IntermediateUnwrapOutput) and self.plaintextDataKey == __o.plaintextDataKey and self.symmetricSigningKey == __o.symmetricSigningKey and self.unwrapInfo == __o.unwrapInfo
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
        return isinstance(self, IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput)

class IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput(IntermediateGenerateAndWrapOutput, NamedTuple('IntermediateGenerateAndWrapOutput', [('plaintextDataKey', Any), ('wrappedMaterial', Any), ('symmetricSigningKey', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput.IntermediateGenerateAndWrapOutput({_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput) and self.plaintextDataKey == __o.plaintextDataKey and self.wrappedMaterial == __o.wrappedMaterial and self.symmetricSigningKey == __o.symmetricSigningKey and self.wrapInfo == __o.wrapInfo
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
        return isinstance(self, IntermediateKeyWrapping.IntermediateWrapOutput_IntermediateWrapOutput)

class IntermediateWrapOutput_IntermediateWrapOutput(IntermediateWrapOutput, NamedTuple('IntermediateWrapOutput', [('wrappedMaterial', Any), ('symmetricSigningKey', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'IntermediateKeyWrapping.IntermediateWrapOutput.IntermediateWrapOutput({_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.symmetricSigningKey)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, IntermediateKeyWrapping.IntermediateWrapOutput_IntermediateWrapOutput) and self.wrappedMaterial == __o.wrappedMaterial and self.symmetricSigningKey == __o.symmetricSigningKey and self.wrapInfo == __o.wrapInfo
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
        return isinstance(self, IntermediateKeyWrapping.DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial)

class DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial(DeserializedIntermediateWrappedMaterial, NamedTuple('DeserializedIntermediateWrappedMaterial', [('encryptedPdk', Any), ('providerWrappedIkm', Any)])):
    def __dafnystr__(self) -> str:
        return f'IntermediateKeyWrapping.DeserializedIntermediateWrappedMaterial.DeserializedIntermediateWrappedMaterial({_dafny.string_of(self.encryptedPdk)}, {_dafny.string_of(self.providerWrappedIkm)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, IntermediateKeyWrapping.DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial) and self.encryptedPdk == __o.encryptedPdk and self.providerWrappedIkm == __o.providerWrappedIkm
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
        return isinstance(self, IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys)

class PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys(PdkEncryptionAndSymmetricSigningKeys, NamedTuple('PdkEncryptionAndSymmetricSigningKeys', [('pdkEncryptionKey', Any), ('symmetricSigningKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys.PdkEncryptionAndSymmetricSigningKeys({_dafny.string_of(self.pdkEncryptionKey)}, {_dafny.string_of(self.symmetricSigningKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys) and self.pdkEncryptionKey == __o.pdkEncryptionKey and self.symmetricSigningKey == __o.symmetricSigningKey
    def __hash__(self) -> int:
        return super().__hash__()

