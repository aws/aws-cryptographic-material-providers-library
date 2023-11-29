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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
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
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
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
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
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

# assert "IntermediateKeyWrapping" == __name__
IntermediateKeyWrapping = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IntermediateUnwrap(unwrap, wrappedMaterial, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_707_maybeCrypto_: Wrappers.Result
        out189_: Wrappers.Result
        out189_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_707_maybeCrypto_ = out189_
        d_708_cryptoPrimitives_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_709_valueOrError0_: Wrappers.Result = None
        def lambda45_(d_710_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_710_e_)

        d_709_valueOrError0_ = (d_707_maybeCrypto_).MapFailure(lambda45_)
        if (d_709_valueOrError0_).IsFailure():
            res = (d_709_valueOrError0_).PropagateFailure()
            return res
        d_708_cryptoPrimitives_ = (d_709_valueOrError0_).Extract()
        d_711_deserializedWrapped_: IntermediateKeyWrapping.DeserializedIntermediateWrappedMaterial
        d_712_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(IntermediateKeyWrapping.DeserializedIntermediateWrappedMaterial.default())()
        d_712_valueOrError1_ = IntermediateKeyWrapping.default__.DeserializeIntermediateWrappedMaterial(wrappedMaterial, algorithmSuite)
        if (d_712_valueOrError1_).IsFailure():
            res = (d_712_valueOrError1_).PropagateFailure()
            return res
        d_711_deserializedWrapped_ = (d_712_valueOrError1_).Extract()
        let_tmp_rhs6_ = d_711_deserializedWrapped_
        d_713_encryptedPdk_ = let_tmp_rhs6_.encryptedPdk
        d_714_providerWrappedIkm_ = let_tmp_rhs6_.providerWrappedIkm
        d_715_unwrapOutput_: MaterialWrapping.UnwrapOutput
        d_716_valueOrError2_: Wrappers.Result = None
        out190_: Wrappers.Result
        out190_ = (unwrap).Invoke(MaterialWrapping.UnwrapInput_UnwrapInput(d_714_providerWrappedIkm_, algorithmSuite, encryptionContext))
        d_716_valueOrError2_ = out190_
        if (d_716_valueOrError2_).IsFailure():
            res = (d_716_valueOrError2_).PropagateFailure()
            return res
        d_715_unwrapOutput_ = (d_716_valueOrError2_).Extract()
        let_tmp_rhs7_ = d_715_unwrapOutput_
        d_717_intermediateMaterial_ = let_tmp_rhs7_.unwrappedMaterial
        d_718_unwrapInfo_ = let_tmp_rhs7_.unwrapInfo
        d_719_derivedKeys_: IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys
        d_720_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys.default())()
        out191_: Wrappers.Result
        out191_ = IntermediateKeyWrapping.default__.DeriveKeysFromIntermediateMaterial(d_717_intermediateMaterial_, algorithmSuite, encryptionContext, d_708_cryptoPrimitives_)
        d_720_valueOrError3_ = out191_
        if (d_720_valueOrError3_).IsFailure():
            res = (d_720_valueOrError3_).PropagateFailure()
            return res
        d_719_derivedKeys_ = (d_720_valueOrError3_).Extract()
        let_tmp_rhs8_ = d_719_derivedKeys_
        d_721_pdkEncryptionKey_ = let_tmp_rhs8_.pdkEncryptionKey
        d_722_symmetricSigningKey_ = let_tmp_rhs8_.symmetricSigningKey
        d_723_iv_: _dafny.Seq
        d_723_iv_ = _dafny.Seq([0 for d_724___v0_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_725_tagIndex_: int
        d_725_tagIndex_ = (len(d_713_encryptedPdk_)) - (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))
        d_726_aad_: _dafny.Seq
        d_727_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_727_valueOrError4_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_727_valueOrError4_).IsFailure():
            res = (d_727_valueOrError4_).PropagateFailure()
            return res
        d_726_aad_ = (d_727_valueOrError4_).Extract()
        d_728_decInput_: software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput
        d_728_decInput_ = software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput(((algorithmSuite).encrypt).AES__GCM, d_721_pdkEncryptionKey_, _dafny.Seq((d_713_encryptedPdk_)[:d_725_tagIndex_:]), _dafny.Seq((d_713_encryptedPdk_)[d_725_tagIndex_::]), d_723_iv_, d_726_aad_)
        d_729_decOutR_: Wrappers.Result
        out192_: Wrappers.Result
        out192_ = (d_708_cryptoPrimitives_).AESDecrypt(d_728_decInput_)
        d_729_decOutR_ = out192_
        d_730_plaintextDataKey_: _dafny.Seq
        d_731_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda46_(d_732_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_732_e_)

        d_731_valueOrError5_ = (d_729_decOutR_).MapFailure(lambda46_)
        if (d_731_valueOrError5_).IsFailure():
            res = (d_731_valueOrError5_).PropagateFailure()
            return res
        d_730_plaintextDataKey_ = (d_731_valueOrError5_).Extract()
        d_733_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_733_valueOrError6_ = Wrappers.default__.Need((len(d_730_plaintextDataKey_)) == (AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Decrypt length")))
        if (d_733_valueOrError6_).IsFailure():
            res = (d_733_valueOrError6_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(IntermediateKeyWrapping.IntermediateUnwrapOutput_IntermediateUnwrapOutput(d_730_plaintextDataKey_, d_722_symmetricSigningKey_, d_718_unwrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateWrap(generateAndWrap, plaintextDataKey, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_734_maybeCrypto_: Wrappers.Result
        out193_: Wrappers.Result
        out193_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_734_maybeCrypto_ = out193_
        d_735_cryptoPrimitives_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_736_valueOrError0_: Wrappers.Result = None
        def lambda47_(d_737_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_737_e_)

        d_736_valueOrError0_ = (d_734_maybeCrypto_).MapFailure(lambda47_)
        if (d_736_valueOrError0_).IsFailure():
            res = (d_736_valueOrError0_).PropagateFailure()
            return res
        d_735_cryptoPrimitives_ = (d_736_valueOrError0_).Extract()
        d_738_generateAndWrapOutput_: MaterialWrapping.GenerateAndWrapOutput
        d_739_valueOrError1_: Wrappers.Result = None
        out194_: Wrappers.Result
        out194_ = (generateAndWrap).Invoke(MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput(algorithmSuite, encryptionContext))
        d_739_valueOrError1_ = out194_
        if (d_739_valueOrError1_).IsFailure():
            res = (d_739_valueOrError1_).PropagateFailure()
            return res
        d_738_generateAndWrapOutput_ = (d_739_valueOrError1_).Extract()
        let_tmp_rhs9_ = d_738_generateAndWrapOutput_
        d_740_intermediateMaterial_ = let_tmp_rhs9_.plaintextMaterial
        d_741_providerWrappedIkm_ = let_tmp_rhs9_.wrappedMaterial
        d_742_wrapInfo_ = let_tmp_rhs9_.wrapInfo
        d_743_derivedKeys_: IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys
        d_744_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys.default())()
        out195_: Wrappers.Result
        out195_ = IntermediateKeyWrapping.default__.DeriveKeysFromIntermediateMaterial(d_740_intermediateMaterial_, algorithmSuite, encryptionContext, d_735_cryptoPrimitives_)
        d_744_valueOrError2_ = out195_
        if (d_744_valueOrError2_).IsFailure():
            res = (d_744_valueOrError2_).PropagateFailure()
            return res
        d_743_derivedKeys_ = (d_744_valueOrError2_).Extract()
        let_tmp_rhs10_ = d_743_derivedKeys_
        d_745_pdkEncryptionKey_ = let_tmp_rhs10_.pdkEncryptionKey
        d_746_symmetricSigningKey_ = let_tmp_rhs10_.symmetricSigningKey
        d_747_iv_: _dafny.Seq
        d_747_iv_ = _dafny.Seq([0 for d_748___v1_ in range(AlgorithmSuites.default__.GetEncryptIvLength(algorithmSuite))])
        d_749_aad_: _dafny.Seq
        d_750_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_750_valueOrError3_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_750_valueOrError3_).IsFailure():
            res = (d_750_valueOrError3_).PropagateFailure()
            return res
        d_749_aad_ = (d_750_valueOrError3_).Extract()
        d_751_encInput_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput
        d_751_encInput_ = software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput_AESEncryptInput(((algorithmSuite).encrypt).AES__GCM, d_747_iv_, d_745_pdkEncryptionKey_, plaintextDataKey, d_749_aad_)
        d_752_encOutR_: Wrappers.Result
        out196_: Wrappers.Result
        out196_ = (d_735_cryptoPrimitives_).AESEncrypt(d_751_encInput_)
        d_752_encOutR_ = out196_
        d_753_encryptedPdk_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_754_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        def lambda48_(d_755_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_755_e_)

        d_754_valueOrError4_ = (d_752_encOutR_).MapFailure(lambda48_)
        if (d_754_valueOrError4_).IsFailure():
            res = (d_754_valueOrError4_).PropagateFailure()
            return res
        d_753_encryptedPdk_ = (d_754_valueOrError4_).Extract()
        d_756_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_756_valueOrError5_ = Wrappers.default__.Need((len(((d_753_encryptedPdk_).cipherText) + ((d_753_encryptedPdk_).authTag))) == ((AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algorithmSuite))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unexpected AES_GCM Encrypt length")))
        if (d_756_valueOrError5_).IsFailure():
            res = (d_756_valueOrError5_).PropagateFailure()
            return res
        d_757_serializedMaterial_: _dafny.Seq
        d_757_serializedMaterial_ = (((d_753_encryptedPdk_).cipherText) + ((d_753_encryptedPdk_).authTag)) + (d_741_providerWrappedIkm_)
        res = Wrappers.Result_Success(IntermediateKeyWrapping.IntermediateWrapOutput_IntermediateWrapOutput(d_757_serializedMaterial_, d_746_symmetricSigningKey_, d_742_wrapInfo_))
        return res
        return res

    @staticmethod
    def IntermediateGenerateAndWrap(generateAndWrap, algorithmSuite, encryptionContext):
        res: Wrappers.Result = None
        d_758_maybeCrypto_: Wrappers.Result
        out197_: Wrappers.Result
        out197_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_758_maybeCrypto_ = out197_
        d_759_cryptoPrimitives_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_760_valueOrError0_: Wrappers.Result = None
        def lambda49_(d_761_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_761_e_)

        d_760_valueOrError0_ = (d_758_maybeCrypto_).MapFailure(lambda49_)
        if (d_760_valueOrError0_).IsFailure():
            res = (d_760_valueOrError0_).PropagateFailure()
            return res
        d_759_cryptoPrimitives_ = (d_760_valueOrError0_).Extract()
        d_762_generateBytesResult_: Wrappers.Result
        out198_: Wrappers.Result
        out198_ = (d_759_cryptoPrimitives_).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(algorithmSuite)))
        d_762_generateBytesResult_ = out198_
        d_763_plaintextDataKey_: _dafny.Seq
        d_764_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda50_(d_765_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_765_e_)

        d_764_valueOrError1_ = (d_762_generateBytesResult_).MapFailure(lambda50_)
        if (d_764_valueOrError1_).IsFailure():
            res = (d_764_valueOrError1_).PropagateFailure()
            return res
        d_763_plaintextDataKey_ = (d_764_valueOrError1_).Extract()
        d_766_wrapOutput_: IntermediateKeyWrapping.IntermediateWrapOutput
        d_767_valueOrError2_: Wrappers.Result = None
        out199_: Wrappers.Result
        out199_ = IntermediateKeyWrapping.default__.IntermediateWrap(generateAndWrap, d_763_plaintextDataKey_, algorithmSuite, encryptionContext)
        d_767_valueOrError2_ = out199_
        if (d_767_valueOrError2_).IsFailure():
            res = (d_767_valueOrError2_).PropagateFailure()
            return res
        d_766_wrapOutput_ = (d_767_valueOrError2_).Extract()
        res = Wrappers.Result_Success(IntermediateKeyWrapping.IntermediateGenerateAndWrapOutput_IntermediateGenerateAndWrapOutput(d_763_plaintextDataKey_, (d_766_wrapOutput_).wrappedMaterial, (d_766_wrapOutput_).symmetricSigningKey, (d_766_wrapOutput_).wrapInfo))
        return res
        return res

    @staticmethod
    def DeserializeIntermediateWrappedMaterial(material, algSuite):
        d_768_valueOrError0_ = Wrappers.default__.Need((len(material)) >= ((AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to deserialize Intermediate Key Wrapped material: too short.")))
        if (d_768_valueOrError0_).IsFailure():
            return (d_768_valueOrError0_).PropagateFailure()
        elif True:
            d_769_encryptedPdkLen_ = (AlgorithmSuites.default__.GetEncryptKeyLength(algSuite)) + (AlgorithmSuites.default__.GetEncryptTagLength(algSuite))
            return Wrappers.Result_Success(IntermediateKeyWrapping.DeserializedIntermediateWrappedMaterial_DeserializedIntermediateWrappedMaterial(_dafny.Seq((material)[:d_769_encryptedPdkLen_:]), _dafny.Seq((material)[d_769_encryptedPdkLen_::])))

    @staticmethod
    def DeriveKeysFromIntermediateMaterial(intermediateMaterial, algorithmSuite, encryptionContext, cryptoPrimitives):
        res: Wrappers.Result = Wrappers.Result_Success.default(IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys.default())()
        d_770_hkdfExtractInput_: software_amazon_cryptography_primitives_internaldafny_types.HkdfExtractInput
        d_770_hkdfExtractInput_ = software_amazon_cryptography_primitives_internaldafny_types.HkdfExtractInput_HkdfExtractInput((((algorithmSuite).commitment).HKDF).hmac, Wrappers.Option_None(), intermediateMaterial)
        d_771_maybePseudoRandomKey_: Wrappers.Result
        out200_: Wrappers.Result
        out200_ = (cryptoPrimitives).HkdfExtract(d_770_hkdfExtractInput_)
        d_771_maybePseudoRandomKey_ = out200_
        d_772_pseudoRandomKey_: _dafny.Seq
        d_773_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda51_(d_774_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_774_e_)

        d_773_valueOrError0_ = (d_771_maybePseudoRandomKey_).MapFailure(lambda51_)
        if (d_773_valueOrError0_).IsFailure():
            res = (d_773_valueOrError0_).PropagateFailure()
            return res
        d_772_pseudoRandomKey_ = (d_773_valueOrError0_).Extract()
        d_775_symmetricSigningKeyInput_: software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput
        d_775_symmetricSigningKeyInput_ = software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput_HkdfExpandInput((((algorithmSuite).commitment).HKDF).hmac, d_772_pseudoRandomKey_, (IntermediateKeyWrapping.default__).KEYWRAP__MAC__INFO, (((algorithmSuite).commitment).HKDF).outputKeyLength)
        d_776_pdkEncryptionKeyInput_: software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput
        def iife32_(_pat_let10_0):
            def iife33_(d_777_dt__update__tmp_h0_):
                def iife34_(_pat_let11_0):
                    def iife35_(d_778_dt__update_hinfo_h0_):
                        return software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput_HkdfExpandInput((d_777_dt__update__tmp_h0_).digestAlgorithm, (d_777_dt__update__tmp_h0_).prk, d_778_dt__update_hinfo_h0_, (d_777_dt__update__tmp_h0_).expectedLength)
                    return iife35_(_pat_let11_0)
                return iife34_((IntermediateKeyWrapping.default__).KEYWRAP__ENC__INFO)
            return iife33_(_pat_let10_0)
        d_776_pdkEncryptionKeyInput_ = iife32_(d_775_symmetricSigningKeyInput_)
        d_779_maybeSymmetricSigningKey_: Wrappers.Result
        out201_: Wrappers.Result
        out201_ = (cryptoPrimitives).HkdfExpand(d_775_symmetricSigningKeyInput_)
        d_779_maybeSymmetricSigningKey_ = out201_
        d_780_symmetricSigningKey_: _dafny.Seq
        d_781_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda52_(d_782_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_782_e_)

        d_781_valueOrError1_ = (d_779_maybeSymmetricSigningKey_).MapFailure(lambda52_)
        if (d_781_valueOrError1_).IsFailure():
            res = (d_781_valueOrError1_).PropagateFailure()
            return res
        d_780_symmetricSigningKey_ = (d_781_valueOrError1_).Extract()
        d_783_maybePdkEncryptionKey_: Wrappers.Result
        out202_: Wrappers.Result
        out202_ = (cryptoPrimitives).HkdfExpand(d_776_pdkEncryptionKeyInput_)
        d_783_maybePdkEncryptionKey_ = out202_
        d_784_pdkEncryptionKey_: _dafny.Seq
        d_785_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda53_(d_786_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_786_e_)

        d_785_valueOrError2_ = (d_783_maybePdkEncryptionKey_).MapFailure(lambda53_)
        if (d_785_valueOrError2_).IsFailure():
            res = (d_785_valueOrError2_).PropagateFailure()
            return res
        d_784_pdkEncryptionKey_ = (d_785_valueOrError2_).Extract()
        res = Wrappers.Result_Success(IntermediateKeyWrapping.PdkEncryptionAndSymmetricSigningKeys_PdkEncryptionAndSymmetricSigningKeys(d_784_pdkEncryptionKey_, d_780_symmetricSigningKey_))
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

