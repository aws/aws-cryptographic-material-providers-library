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
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import Base64
import AlgorithmSuites
import Materials
import Keyring
import Relations
import Seq_MergeSort
import Math
import Seq
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import Actions
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
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import DafnyLibraries
import Time
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import UUID
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring
import CMM
import Defaults
import Commitment
import DefaultCMM
import DefaultClientSupplier
import RequiredEncryptionContextCMM
import AwsCryptographyMaterialProvidersOperations
import software_amazon_cryptography_materialproviders_internaldafny
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
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
import Streams
import Sorting
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64Lemmas
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import TestVectorsUtils
import TestVectorConstants
import KeyringExpectations
import CreateAwsKmsKeyrings
import CreateAwsKmsMultiKeyrings
import CreateAwsKmsMrkKeyrings
import CreateAwsKmsMrkMultiKeyrings
import CreateRawAesKeyrings
import CreateRawRsaKeyrings
import CreateKeyrings
import software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer
import JSON_Deserializer_Uint16StrConversion
import JSON_Deserializer_ByteStrConversion
import JSON_Deserializer
import JSON_ConcreteSyntax_Spec
import JSON_ConcreteSyntax_SpecProperties
import JSON_ConcreteSyntax
import JSON_ZeroCopy_Serializer
import JSON_ZeroCopy_Deserializer_Core
import JSON_ZeroCopy_Deserializer_Strings
import JSON_ZeroCopy_Deserializer_Numbers
import JSON_ZeroCopy_Deserializer_ObjectParams
import JSON_ZeroCopy_Deserializer_Objects
import JSON_ZeroCopy_Deserializer_ArrayParams
import JSON_ZeroCopy_Deserializer_Arrays
import JSON_ZeroCopy_Deserializer_Constants
import JSON_ZeroCopy_Deserializer_Values
import JSON_ZeroCopy_Deserializer_API
import JSON_ZeroCopy_Deserializer
import JSON_ZeroCopy_API
import JSON_ZeroCopy
import JSON_API
import JSON
import JSONHelpers
import KeyDescription

# Module: KeyMaterial

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BuildKeyMaterials(mpl, obj):
        if (len(obj)) == (0):
            return Wrappers.Result_Success(_dafny.Map({}))
        elif True:
            d_214_name_ = ((obj)[0])[0]
            d_215_valueOrError0_ = default__.ToKeyMaterial(mpl, d_214_name_, ((obj)[0])[1])
            if (d_215_valueOrError0_).IsFailure():
                return (d_215_valueOrError0_).PropagateFailure()
            elif True:
                d_216_keyMaterial_ = (d_215_valueOrError0_).Extract()
                d_217_valueOrError1_ = default__.BuildKeyMaterials(mpl, _dafny.Seq((obj)[1::]))
                if (d_217_valueOrError1_).IsFailure():
                    return (d_217_valueOrError1_).PropagateFailure()
                elif True:
                    d_218_tail_ = (d_217_valueOrError1_).Extract()
                    return Wrappers.Result_Success((_dafny.Map({d_214_name_: d_216_keyMaterial_})) | (d_218_tail_))

    @staticmethod
    def ToKeyMaterial(mpl, name, obj):
        d_219_valueOrError0_ = Wrappers.default__.Need((obj).is_Object, _dafny.Seq("KeyDescription not an object"))
        if (d_219_valueOrError0_).IsFailure():
            return (d_219_valueOrError0_).PropagateFailure()
        elif True:
            d_220_obj_ = (obj).obj
            d_221_typString_ = _dafny.Seq("type")
            d_222_valueOrError1_ = JSONHelpers.default__.GetString(d_221_typString_, d_220_obj_)
            if (d_222_valueOrError1_).IsFailure():
                return (d_222_valueOrError1_).PropagateFailure()
            elif True:
                d_223_typ_ = (d_222_valueOrError1_).Extract()
                d_224_valueOrError2_ = Wrappers.default__.Need(default__.KeyMaterialString_q(d_223_typ_), (_dafny.Seq("Unsupported KeyMaterial type:")) + (d_223_typ_))
                if (d_224_valueOrError2_).IsFailure():
                    return (d_224_valueOrError2_).PropagateFailure()
                elif True:
                    if (d_223_typ_) == (_dafny.Seq("static-material")):
                        d_225_valueOrError3_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithmSuiteId"), d_220_obj_)
                        if (d_225_valueOrError3_).IsFailure():
                            return (d_225_valueOrError3_).PropagateFailure()
                        elif True:
                            d_226_algorithmSuiteHex_ = (d_225_valueOrError3_).Extract()
                            d_227_valueOrError4_ = Wrappers.default__.Need(HexStrings.default__.IsLooseHexString(d_226_algorithmSuiteHex_), _dafny.Seq("Not hex encoded binnary"))
                            if (d_227_valueOrError4_).IsFailure():
                                return (d_227_valueOrError4_).PropagateFailure()
                            elif True:
                                d_228_binaryId_ = HexStrings.default__.FromHexString(d_226_algorithmSuiteHex_)
                                def lambda8_(d_230_algorithmSuiteHex_):
                                    def lambda9_(d_231_e_):
                                        return (_dafny.Seq("Invalid Suite:")) + (d_230_algorithmSuiteHex_)

                                    return lambda9_

                                d_229_valueOrError5_ = ((mpl).GetAlgorithmSuiteInfo(d_228_binaryId_)).MapFailure(lambda8_(d_226_algorithmSuiteHex_))
                                if (d_229_valueOrError5_).IsFailure():
                                    return (d_229_valueOrError5_).PropagateFailure()
                                elif True:
                                    d_232_algorithmSuite_ = (d_229_valueOrError5_).Extract()
                                    d_233_valueOrError6_ = JSONHelpers.default__.SmallObjectToStringStringMap(_dafny.Seq("encryptionContext"), d_220_obj_)
                                    if (d_233_valueOrError6_).IsFailure():
                                        return (d_233_valueOrError6_).PropagateFailure()
                                    elif True:
                                        d_234_encryptionContextStrings_ = (d_233_valueOrError6_).Extract()
                                        d_235_valueOrError7_ = JSONHelpers.default__.utf8EncodeMap(d_234_encryptionContextStrings_)
                                        if (d_235_valueOrError7_).IsFailure():
                                            return (d_235_valueOrError7_).PropagateFailure()
                                        elif True:
                                            d_236_encryptionContext_ = (d_235_valueOrError7_).Extract()
                                            d_237_valueOrError8_ = JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), d_220_obj_)
                                            if (d_237_valueOrError8_).IsFailure():
                                                return (d_237_valueOrError8_).PropagateFailure()
                                            elif True:
                                                d_238_keysAsStrings_ = (d_237_valueOrError8_).Extract()
                                                d_239_valueOrError9_ = JSONHelpers.default__.utf8EncodeSeq(d_238_keysAsStrings_)
                                                if (d_239_valueOrError9_).IsFailure():
                                                    return (d_239_valueOrError9_).PropagateFailure()
                                                elif True:
                                                    d_240_requiredEncryptionContextKeys_ = (d_239_valueOrError9_).Extract()
                                                    d_241_valueOrError10_ = JSONHelpers.default__.GetArrayObject(_dafny.Seq("encryptedDataKeys"), d_220_obj_)
                                                    if (d_241_valueOrError10_).IsFailure():
                                                        return (d_241_valueOrError10_).PropagateFailure()
                                                    elif True:
                                                        d_242_encryptedDataKeysJSON_ = (d_241_valueOrError10_).Extract()
                                                        d_243_valueOrError11_ = Seq.default__.MapWithResult(default__.ToEncryptedDataKey, d_242_encryptedDataKeysJSON_)
                                                        if (d_243_valueOrError11_).IsFailure():
                                                            return (d_243_valueOrError11_).PropagateFailure()
                                                        elif True:
                                                            d_244_encryptedDataKeys_ = (d_243_valueOrError11_).Extract()
                                                            d_245_valueOrError12_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("plaintextDataKey"), d_220_obj_)
                                                            if (d_245_valueOrError12_).IsFailure():
                                                                return (d_245_valueOrError12_).PropagateFailure()
                                                            elif True:
                                                                d_246_plaintextDataKeyEncoded_ = (d_245_valueOrError12_).Extract()
                                                                def iife5_(_pat_let0_0):
                                                                    def iife6_(d_248_result_):
                                                                        return (Wrappers.Result_Success(Wrappers.Option_Some((d_248_result_).value)) if (d_248_result_).is_Success else Wrappers.Result_Failure((d_248_result_).error))
                                                                    return iife6_(_pat_let0_0)
                                                                d_247_valueOrError13_ = (iife5_(Base64.default__.Decode((d_246_plaintextDataKeyEncoded_).value)) if (d_246_plaintextDataKeyEncoded_).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                                                                if (d_247_valueOrError13_).IsFailure():
                                                                    return (d_247_valueOrError13_).PropagateFailure()
                                                                elif True:
                                                                    d_249_plaintextDataKey_ = (d_247_valueOrError13_).Extract()
                                                                    d_250_valueOrError14_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("signingKey"), d_220_obj_)
                                                                    if (d_250_valueOrError14_).IsFailure():
                                                                        return (d_250_valueOrError14_).PropagateFailure()
                                                                    elif True:
                                                                        d_251_signingKey_ = (d_250_valueOrError14_).Extract()
                                                                        d_252_valueOrError15_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("verificationKey"), d_220_obj_)
                                                                        if (d_252_valueOrError15_).IsFailure():
                                                                            return (d_252_valueOrError15_).PropagateFailure()
                                                                        elif True:
                                                                            d_253_verificationKey_ = (d_252_valueOrError15_).Extract()
                                                                            d_254_symmetricSigningKeys_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("symmetricSigningKeys"), d_220_obj_)).ToOption()
                                                                            return Wrappers.Result_Success(KeyMaterial_StaticMaterial(name, d_232_algorithmSuite_, d_236_encryptionContext_, d_244_encryptedDataKeys_, d_240_requiredEncryptionContextKeys_, d_249_plaintextDataKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
                    elif (d_223_typ_) == (_dafny.Seq("static-branch-key")):
                        d_255_valueOrError16_ = JSONHelpers.default__.GetString(_dafny.Seq("key-id"), d_220_obj_)
                        if (d_255_valueOrError16_).IsFailure():
                            return (d_255_valueOrError16_).PropagateFailure()
                        elif True:
                            d_256_keyIdentifier_ = (d_255_valueOrError16_).Extract()
                            d_257_valueOrError17_ = JSONHelpers.default__.GetString(_dafny.Seq("branchKeyVersion"), d_220_obj_)
                            if (d_257_valueOrError17_).IsFailure():
                                return (d_257_valueOrError17_).PropagateFailure()
                            elif True:
                                d_258_branchKeyVersionEncoded_ = (d_257_valueOrError17_).Extract()
                                d_259_valueOrError18_ = UTF8.default__.Encode(d_258_branchKeyVersionEncoded_)
                                if (d_259_valueOrError18_).IsFailure():
                                    return (d_259_valueOrError18_).PropagateFailure()
                                elif True:
                                    d_260_branchKeyVersion_ = (d_259_valueOrError18_).Extract()
                                    d_261_valueOrError19_ = JSONHelpers.default__.GetString(_dafny.Seq("branchKey"), d_220_obj_)
                                    if (d_261_valueOrError19_).IsFailure():
                                        return (d_261_valueOrError19_).PropagateFailure()
                                    elif True:
                                        d_262_branchKeyEncoded_ = (d_261_valueOrError19_).Extract()
                                        d_263_valueOrError20_ = Base64.default__.Decode(d_262_branchKeyEncoded_)
                                        if (d_263_valueOrError20_).IsFailure():
                                            return (d_263_valueOrError20_).PropagateFailure()
                                        elif True:
                                            d_264_branchKey_ = (d_263_valueOrError20_).Extract()
                                            d_265_valueOrError21_ = JSONHelpers.default__.GetString(_dafny.Seq("beaconKey"), d_220_obj_)
                                            if (d_265_valueOrError21_).IsFailure():
                                                return (d_265_valueOrError21_).PropagateFailure()
                                            elif True:
                                                d_266_beaconKeyEncoded_ = (d_265_valueOrError21_).Extract()
                                                d_267_valueOrError22_ = Base64.default__.Decode(d_266_beaconKeyEncoded_)
                                                if (d_267_valueOrError22_).IsFailure():
                                                    return (d_267_valueOrError22_).PropagateFailure()
                                                elif True:
                                                    d_268_beaconKey_ = (d_267_valueOrError22_).Extract()
                                                    return Wrappers.Result_Success(KeyMaterial_StaticKeyStoreInformation(d_256_keyIdentifier_, d_260_branchKeyVersion_, d_264_branchKey_, d_268_beaconKey_))
                    elif True:
                        d_269_valueOrError23_ = JSONHelpers.default__.GetBool(_dafny.Seq("encrypt"), d_220_obj_)
                        if (d_269_valueOrError23_).IsFailure():
                            return (d_269_valueOrError23_).PropagateFailure()
                        elif True:
                            d_270_encrypt_ = (d_269_valueOrError23_).Extract()
                            d_271_valueOrError24_ = JSONHelpers.default__.GetBool(_dafny.Seq("decrypt"), d_220_obj_)
                            if (d_271_valueOrError24_).IsFailure():
                                return (d_271_valueOrError24_).PropagateFailure()
                            elif True:
                                d_272_decrypt_ = (d_271_valueOrError24_).Extract()
                                d_273_valueOrError25_ = JSONHelpers.default__.GetString(_dafny.Seq("key-id"), d_220_obj_)
                                if (d_273_valueOrError25_).IsFailure():
                                    return (d_273_valueOrError25_).PropagateFailure()
                                elif True:
                                    d_274_keyIdentifier_ = (d_273_valueOrError25_).Extract()
                                    if (d_223_typ_) == (_dafny.Seq("aws-kms")):
                                        return Wrappers.Result_Success(KeyMaterial_KMS(name, d_270_encrypt_, d_272_decrypt_, d_274_keyIdentifier_))
                                    elif True:
                                        d_275_valueOrError26_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithm"), d_220_obj_)
                                        if (d_275_valueOrError26_).IsFailure():
                                            return (d_275_valueOrError26_).PropagateFailure()
                                        elif True:
                                            d_276_algorithm_ = (d_275_valueOrError26_).Extract()
                                            d_277_valueOrError27_ = JSONHelpers.default__.GetNat(_dafny.Seq("bits"), d_220_obj_)
                                            if (d_277_valueOrError27_).IsFailure():
                                                return (d_277_valueOrError27_).PropagateFailure()
                                            elif True:
                                                d_278_bits_ = (d_277_valueOrError27_).Extract()
                                                d_279_valueOrError28_ = JSONHelpers.default__.GetString(_dafny.Seq("encoding"), d_220_obj_)
                                                if (d_279_valueOrError28_).IsFailure():
                                                    return (d_279_valueOrError28_).PropagateFailure()
                                                elif True:
                                                    d_280_encoding_ = (d_279_valueOrError28_).Extract()
                                                    d_281_valueOrError29_ = JSONHelpers.default__.GetString(_dafny.Seq("material"), d_220_obj_)
                                                    if (d_281_valueOrError29_).IsFailure():
                                                        return (d_281_valueOrError29_).PropagateFailure()
                                                    elif True:
                                                        d_282_material_ = (d_281_valueOrError29_).Extract()
                                                        if (d_223_typ_) == (_dafny.Seq("symmetric")):
                                                            d_283_valueOrError30_ = Base64.default__.Decode(d_282_material_)
                                                            if (d_283_valueOrError30_).IsFailure():
                                                                return (d_283_valueOrError30_).PropagateFailure()
                                                            elif True:
                                                                d_284_materialBytes_ = (d_283_valueOrError30_).Extract()
                                                                return Wrappers.Result_Success(KeyMaterial_Symetric(name, d_270_encrypt_, d_272_decrypt_, d_276_algorithm_, d_278_bits_, d_280_encoding_, d_284_materialBytes_, d_274_keyIdentifier_))
                                                        elif (d_223_typ_) == (_dafny.Seq("private")):
                                                            return Wrappers.Result_Success(KeyMaterial_PrivateRSA(name, d_270_encrypt_, d_272_decrypt_, d_276_algorithm_, d_278_bits_, d_280_encoding_, d_282_material_, d_274_keyIdentifier_))
                                                        elif (d_223_typ_) == (_dafny.Seq("public")):
                                                            return Wrappers.Result_Success(KeyMaterial_PublicRSA(name, d_270_encrypt_, d_272_decrypt_, d_278_bits_, d_276_algorithm_, d_280_encoding_, d_282_material_, d_274_keyIdentifier_))
                                                        elif True:
                                                            d_285_valueOrError31_ = UTF8.default__.Encode(d_282_material_)
                                                            if (d_285_valueOrError31_).IsFailure():
                                                                return (d_285_valueOrError31_).PropagateFailure()
                                                            elif True:
                                                                d_286_publicKey_ = (d_285_valueOrError31_).Extract()
                                                                return Wrappers.Result_Success(KeyMaterial_KMSAsymetric(name, d_270_encrypt_, d_272_decrypt_, d_274_keyIdentifier_, d_278_bits_, d_276_algorithm_, d_280_encoding_, d_286_publicKey_))

    @staticmethod
    def ToEncryptedDataKey(obj):
        d_287_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderId"), obj)
        if (d_287_valueOrError0_).IsFailure():
            return (d_287_valueOrError0_).PropagateFailure()
        elif True:
            d_288_keyProviderIdJSON_ = (d_287_valueOrError0_).Extract()
            d_289_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderInfo"), obj)
            if (d_289_valueOrError1_).IsFailure():
                return (d_289_valueOrError1_).PropagateFailure()
            elif True:
                d_290_keyProviderInfoJSON_ = (d_289_valueOrError1_).Extract()
                d_291_valueOrError2_ = JSONHelpers.default__.GetString(_dafny.Seq("ciphertext"), obj)
                if (d_291_valueOrError2_).IsFailure():
                    return (d_291_valueOrError2_).PropagateFailure()
                elif True:
                    d_292_ciphertextJSON_ = (d_291_valueOrError2_).Extract()
                    d_293_valueOrError3_ = UTF8.default__.Encode(d_288_keyProviderIdJSON_)
                    if (d_293_valueOrError3_).IsFailure():
                        return (d_293_valueOrError3_).PropagateFailure()
                    elif True:
                        d_294_keyProviderId_ = (d_293_valueOrError3_).Extract()
                        d_295_valueOrError4_ = Base64.default__.Decode(d_290_keyProviderInfoJSON_)
                        if (d_295_valueOrError4_).IsFailure():
                            return (d_295_valueOrError4_).PropagateFailure()
                        elif True:
                            d_296_keyProviderInfo_ = (d_295_valueOrError4_).Extract()
                            d_297_valueOrError5_ = Base64.default__.Decode(d_292_ciphertextJSON_)
                            if (d_297_valueOrError5_).IsFailure():
                                return (d_297_valueOrError5_).PropagateFailure()
                            elif True:
                                d_298_ciphertext_ = (d_297_valueOrError5_).Extract()
                                return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(d_294_keyProviderId_, d_296_keyProviderInfo_, d_298_ciphertext_))

    @staticmethod
    def KeyMaterialString_q(s):
        return (((((((s) == (_dafny.Seq("static-material"))) or ((s) == (_dafny.Seq("aws-kms")))) or ((s) == (_dafny.Seq("symmetric")))) or ((s) == (_dafny.Seq("private")))) or ((s) == (_dafny.Seq("public")))) or ((s) == (_dafny.Seq("static-branch-key")))) or ((s) == (_dafny.Seq("aws-kms-rsa")))


class KeyMaterial:
    @classmethod
    def default(cls, ):
        return lambda: KeyMaterial_Symetric(_dafny.Seq({}), False, False, _dafny.Seq({}), int(0), _dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Symetric(self) -> bool:
        return isinstance(self, KeyMaterial_Symetric)
    @property
    def is_PrivateRSA(self) -> bool:
        return isinstance(self, KeyMaterial_PrivateRSA)
    @property
    def is_PublicRSA(self) -> bool:
        return isinstance(self, KeyMaterial_PublicRSA)
    @property
    def is_KMS(self) -> bool:
        return isinstance(self, KeyMaterial_KMS)
    @property
    def is_KMSAsymetric(self) -> bool:
        return isinstance(self, KeyMaterial_KMSAsymetric)
    @property
    def is_StaticMaterial(self) -> bool:
        return isinstance(self, KeyMaterial_StaticMaterial)
    @property
    def is_StaticKeyStoreInformation(self) -> bool:
        return isinstance(self, KeyMaterial_StaticKeyStoreInformation)

class KeyMaterial_Symetric(KeyMaterial, NamedTuple('Symetric', [('name', Any), ('encrypt', Any), ('decrypt', Any), ('algorithm', Any), ('bits', Any), ('encoding', Any), ('wrappingKey', Any), ('keyIdentifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.Symetric({_dafny.string_of(self.name)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.decrypt)}, {_dafny.string_of(self.algorithm)}, {_dafny.string_of(self.bits)}, {_dafny.string_of(self.encoding)}, {_dafny.string_of(self.wrappingKey)}, {_dafny.string_of(self.keyIdentifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_Symetric) and self.name == __o.name and self.encrypt == __o.encrypt and self.decrypt == __o.decrypt and self.algorithm == __o.algorithm and self.bits == __o.bits and self.encoding == __o.encoding and self.wrappingKey == __o.wrappingKey and self.keyIdentifier == __o.keyIdentifier
    def __hash__(self) -> int:
        return super().__hash__()

class KeyMaterial_PrivateRSA(KeyMaterial, NamedTuple('PrivateRSA', [('name', Any), ('encrypt', Any), ('decrypt', Any), ('algorithm', Any), ('bits', Any), ('encoding', Any), ('material', Any), ('keyIdentifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.PrivateRSA({_dafny.string_of(self.name)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.decrypt)}, {_dafny.string_of(self.algorithm)}, {_dafny.string_of(self.bits)}, {_dafny.string_of(self.encoding)}, {_dafny.string_of(self.material)}, {_dafny.string_of(self.keyIdentifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_PrivateRSA) and self.name == __o.name and self.encrypt == __o.encrypt and self.decrypt == __o.decrypt and self.algorithm == __o.algorithm and self.bits == __o.bits and self.encoding == __o.encoding and self.material == __o.material and self.keyIdentifier == __o.keyIdentifier
    def __hash__(self) -> int:
        return super().__hash__()

class KeyMaterial_PublicRSA(KeyMaterial, NamedTuple('PublicRSA', [('name', Any), ('encrypt', Any), ('decrypt', Any), ('bits', Any), ('algorithm', Any), ('encoding', Any), ('material', Any), ('keyIdentifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.PublicRSA({_dafny.string_of(self.name)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.decrypt)}, {_dafny.string_of(self.bits)}, {_dafny.string_of(self.algorithm)}, {_dafny.string_of(self.encoding)}, {_dafny.string_of(self.material)}, {_dafny.string_of(self.keyIdentifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_PublicRSA) and self.name == __o.name and self.encrypt == __o.encrypt and self.decrypt == __o.decrypt and self.bits == __o.bits and self.algorithm == __o.algorithm and self.encoding == __o.encoding and self.material == __o.material and self.keyIdentifier == __o.keyIdentifier
    def __hash__(self) -> int:
        return super().__hash__()

class KeyMaterial_KMS(KeyMaterial, NamedTuple('KMS', [('name', Any), ('encrypt', Any), ('decrypt', Any), ('keyIdentifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.KMS({_dafny.string_of(self.name)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.decrypt)}, {_dafny.string_of(self.keyIdentifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_KMS) and self.name == __o.name and self.encrypt == __o.encrypt and self.decrypt == __o.decrypt and self.keyIdentifier == __o.keyIdentifier
    def __hash__(self) -> int:
        return super().__hash__()

class KeyMaterial_KMSAsymetric(KeyMaterial, NamedTuple('KMSAsymetric', [('name', Any), ('encrypt', Any), ('decrypt', Any), ('keyIdentifier', Any), ('bits', Any), ('algorithm', Any), ('encoding', Any), ('publicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.KMSAsymetric({_dafny.string_of(self.name)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.decrypt)}, {_dafny.string_of(self.keyIdentifier)}, {_dafny.string_of(self.bits)}, {_dafny.string_of(self.algorithm)}, {_dafny.string_of(self.encoding)}, {_dafny.string_of(self.publicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_KMSAsymetric) and self.name == __o.name and self.encrypt == __o.encrypt and self.decrypt == __o.decrypt and self.keyIdentifier == __o.keyIdentifier and self.bits == __o.bits and self.algorithm == __o.algorithm and self.encoding == __o.encoding and self.publicKey == __o.publicKey
    def __hash__(self) -> int:
        return super().__hash__()

class KeyMaterial_StaticMaterial(KeyMaterial, NamedTuple('StaticMaterial', [('name', Any), ('algorithmSuite', Any), ('encryptionContext', Any), ('encryptedDataKeys', Any), ('requiredEncryptionContextKeys', Any), ('plaintextDataKey', Any), ('signingKey', Any), ('verificationKey', Any), ('symmetricSigningKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.StaticMaterial({_dafny.string_of(self.name)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.encryptedDataKeys)}, {_dafny.string_of(self.requiredEncryptionContextKeys)}, {_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.signingKey)}, {_dafny.string_of(self.verificationKey)}, {_dafny.string_of(self.symmetricSigningKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_StaticMaterial) and self.name == __o.name and self.algorithmSuite == __o.algorithmSuite and self.encryptionContext == __o.encryptionContext and self.encryptedDataKeys == __o.encryptedDataKeys and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys and self.plaintextDataKey == __o.plaintextDataKey and self.signingKey == __o.signingKey and self.verificationKey == __o.verificationKey and self.symmetricSigningKeys == __o.symmetricSigningKeys
    def __hash__(self) -> int:
        return super().__hash__()

class KeyMaterial_StaticKeyStoreInformation(KeyMaterial, NamedTuple('StaticKeyStoreInformation', [('keyIdentifier', Any), ('branchKeyVersion', Any), ('branchKey', Any), ('beaconKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.StaticKeyStoreInformation({_dafny.string_of(self.keyIdentifier)}, {_dafny.string_of(self.branchKeyVersion)}, {_dafny.string_of(self.branchKey)}, {_dafny.string_of(self.beaconKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_StaticKeyStoreInformation) and self.keyIdentifier == __o.keyIdentifier and self.branchKeyVersion == __o.branchKeyVersion and self.branchKey == __o.branchKey and self.beaconKey == __o.beaconKey
    def __hash__(self) -> int:
        return super().__hash__()

