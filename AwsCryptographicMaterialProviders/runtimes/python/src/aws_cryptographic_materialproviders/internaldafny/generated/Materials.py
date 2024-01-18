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

# Module: Materials

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def InitializeEncryptionMaterials(input):
        pat_let_tv123_ = input
        pat_let_tv124_ = input
        pat_let_tv125_ = input
        d_299_valueOrError0_ = Wrappers.default__.Need((default__.EC__PUBLIC__KEY__FIELD) not in ((input).encryptionContext), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption Context ")))
        if (d_299_valueOrError0_).IsFailure():
            return (d_299_valueOrError0_).PropagateFailure()
        elif True:
            def lambda31_(forall_var_8_):
                d_301_key_: _dafny.Seq = forall_var_8_
                return not ((d_301_key_) in ((input).requiredEncryptionContextKeys)) or ((d_301_key_) in ((input).encryptionContext))

            d_300_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier(((input).requiredEncryptionContextKeys).UniqueElements, True, lambda31_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Required encryption context keys do not exist in provided encryption context.")))
            if (d_300_valueOrError1_).IsFailure():
                return (d_300_valueOrError1_).PropagateFailure()
            elif True:
                d_302_suite_ = AlgorithmSuites.default__.GetSuite((input).algorithmSuiteId)
                d_303_valueOrError2_ = Wrappers.default__.Need((((d_302_suite_).signature).is_ECDSA) == ((((input).signingKey).is_Some) and (((input).verificationKey).is_Some)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Missing signature key for signed suite.")))
                if (d_303_valueOrError2_).IsFailure():
                    return (d_303_valueOrError2_).PropagateFailure()
                elif True:
                    d_304_valueOrError3_ = Wrappers.default__.Need((((d_302_suite_).signature).is_None) == ((((input).signingKey).is_None) and (((input).verificationKey).is_None)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Signature key not allowed for non-signed suites.")))
                    if (d_304_valueOrError3_).IsFailure():
                        return (d_304_valueOrError3_).PropagateFailure()
                    elif True:
                        def lambda32_(source17_):
                            if source17_.is_ECDSA:
                                d_306___mcc_h0_ = source17_.ECDSA
                                d_307_curve_ = d_306___mcc_h0_
                                def lambda33_(d_309_e_):
                                    return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_309_e_)

                                d_308_valueOrError5_ = (UTF8.default__.Encode(Base64.default__.Encode(((pat_let_tv123_).verificationKey).value))).MapFailure(lambda33_)
                                if (d_308_valueOrError5_).IsFailure():
                                    return (d_308_valueOrError5_).PropagateFailure()
                                elif True:
                                    d_310_enc__vk_ = (d_308_valueOrError5_).Extract()
                                    return Wrappers.Result_Success(((pat_let_tv124_).encryptionContext).set(default__.EC__PUBLIC__KEY__FIELD, d_310_enc__vk_))
                            elif True:
                                d_311___mcc_h2_ = source17_.None_
                                d_312_None_ = (d_302_suite_).signature
                                return Wrappers.Result_Success((pat_let_tv125_).encryptionContext)

                        d_305_valueOrError4_ = lambda32_((d_302_suite_).signature)
                        if (d_305_valueOrError4_).IsFailure():
                            return (d_305_valueOrError4_).PropagateFailure()
                        elif True:
                            d_313_encryptionContext_ = (d_305_valueOrError4_).Extract()
                            return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials(d_302_suite_, d_313_encryptionContext_, _dafny.Seq([]), (input).requiredEncryptionContextKeys, Wrappers.Option_None(), (input).signingKey, (Wrappers.Option_None() if ((d_302_suite_).symmetricSignature).is_None else Wrappers.Option_Some(_dafny.Seq([])))))

    @staticmethod
    def InitializeDecryptionMaterials(input):
        def lambda34_(forall_var_9_):
            d_315_key_: _dafny.Seq = forall_var_9_
            return not ((d_315_key_) in ((input).requiredEncryptionContextKeys)) or ((d_315_key_) in ((input).encryptionContext))

        d_314_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier(((input).requiredEncryptionContextKeys).UniqueElements, True, lambda34_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reporoduced encryption context key did not exist in provided encryption context.")))
        if (d_314_valueOrError0_).IsFailure():
            return (d_314_valueOrError0_).PropagateFailure()
        elif True:
            d_316_suite_ = AlgorithmSuites.default__.GetSuite((input).algorithmSuiteId)
            d_317_valueOrError1_ = Wrappers.default__.Need((((d_316_suite_).signature).is_ECDSA) == ((default__.EC__PUBLIC__KEY__FIELD) in ((input).encryptionContext)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption Context missing verification key.")))
            if (d_317_valueOrError1_).IsFailure():
                return (d_317_valueOrError1_).PropagateFailure()
            elif True:
                d_318_valueOrError2_ = Wrappers.default__.Need((((d_316_suite_).signature).is_None) == ((default__.EC__PUBLIC__KEY__FIELD) not in ((input).encryptionContext)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Verification key can not exist in non-signed Algorithm Suites.")))
                if (d_318_valueOrError2_).IsFailure():
                    return (d_318_valueOrError2_).PropagateFailure()
                elif True:
                    d_319_valueOrError3_ = default__.DecodeVerificationKey((input).encryptionContext)
                    if (d_319_valueOrError3_).IsFailure():
                        return (d_319_valueOrError3_).PropagateFailure()
                    elif True:
                        d_320_verificationKey_ = (d_319_valueOrError3_).Extract()
                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials(d_316_suite_, (input).encryptionContext, (input).requiredEncryptionContextKeys, Wrappers.Option_None(), d_320_verificationKey_, Wrappers.Option_None()))

    @staticmethod
    def DecodeVerificationKey(encryptionContext):
        if (default__.EC__PUBLIC__KEY__FIELD) in (encryptionContext):
            d_321_utf8Key_ = (encryptionContext)[default__.EC__PUBLIC__KEY__FIELD]
            def lambda35_(d_323_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_323_e_)

            d_322_valueOrError0_ = (UTF8.default__.Decode(d_321_utf8Key_)).MapFailure(lambda35_)
            if (d_322_valueOrError0_).IsFailure():
                return (d_322_valueOrError0_).PropagateFailure()
            elif True:
                d_324_base64Key_ = (d_322_valueOrError0_).Extract()
                def lambda36_(d_326_e_):
                    return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_326_e_)

                d_325_valueOrError1_ = (Base64.default__.Decode(d_324_base64Key_)).MapFailure(lambda36_)
                if (d_325_valueOrError1_).IsFailure():
                    return (d_325_valueOrError1_).PropagateFailure()
                elif True:
                    d_327_key_ = (d_325_valueOrError1_).Extract()
                    return Wrappers.Result_Success(Wrappers.Option_Some(d_327_key_))
        elif True:
            return Wrappers.Result_Success(Wrappers.Option_None())

    @staticmethod
    def ValidEncryptionMaterialsTransition(oldMat, newMat):
        return ((((((((((((newMat).algorithmSuite) == ((oldMat).algorithmSuite)) and (((newMat).encryptionContext) == ((oldMat).encryptionContext))) and (((newMat).requiredEncryptionContextKeys) == ((oldMat).requiredEncryptionContextKeys))) and (((newMat).signingKey) == ((oldMat).signingKey))) and (((((oldMat).plaintextDataKey).is_None) and (((newMat).plaintextDataKey).is_Some)) or (((oldMat).plaintextDataKey) == ((newMat).plaintextDataKey)))) and (((newMat).plaintextDataKey).is_Some)) and ((len((oldMat).encryptedDataKeys)) <= (len((newMat).encryptedDataKeys)))) and ((_dafny.MultiSet((oldMat).encryptedDataKeys)).issubset(_dafny.MultiSet((newMat).encryptedDataKeys)))) and (not (not((((oldMat).algorithmSuite).symmetricSignature).is_None)) or (((((newMat).symmetricSigningKeys).is_Some) and (((oldMat).symmetricSigningKeys).is_Some)) and ((_dafny.MultiSet(((oldMat).symmetricSigningKeys).value)).issubset(_dafny.MultiSet(((newMat).symmetricSigningKeys).value)))))) and (default__.ValidEncryptionMaterials(oldMat))) and (default__.ValidEncryptionMaterials(newMat))

    @staticmethod
    def ValidEncryptionMaterials(encryptionMaterials):
        pat_let_tv126_ = encryptionMaterials
        pat_let_tv127_ = encryptionMaterials
        pat_let_tv128_ = encryptionMaterials
        pat_let_tv129_ = encryptionMaterials
        pat_let_tv130_ = encryptionMaterials
        pat_let_tv131_ = encryptionMaterials
        pat_let_tv132_ = encryptionMaterials
        pat_let_tv133_ = encryptionMaterials
        pat_let_tv134_ = encryptionMaterials
        pat_let_tv135_ = encryptionMaterials
        pat_let_tv136_ = encryptionMaterials
        pat_let_tv137_ = encryptionMaterials
        pat_let_tv138_ = encryptionMaterials
        pat_let_tv139_ = encryptionMaterials
        pat_let_tv140_ = encryptionMaterials
        pat_let_tv141_ = encryptionMaterials
        def iife11_(_pat_let1_0):
            def iife12_(d_328_suite_):
                def lambda37_(forall_var_10_):
                    d_329_key_: _dafny.Seq = forall_var_10_
                    return not ((d_329_key_) in ((pat_let_tv140_).requiredEncryptionContextKeys)) or ((d_329_key_) in ((pat_let_tv141_).encryptionContext))

                return ((((((((((((d_328_suite_).signature).is_None) == (((pat_let_tv126_).signingKey).is_None)) and (not (((pat_let_tv127_).plaintextDataKey).is_Some) or ((AlgorithmSuites.default__.GetEncryptKeyLength(d_328_suite_)) == (len(((pat_let_tv128_).plaintextDataKey).value))))) and (not (((pat_let_tv129_).plaintextDataKey).is_None) or ((len((pat_let_tv130_).encryptedDataKeys)) == (0)))) and ((not(((d_328_suite_).signature).is_None)) == ((default__.EC__PUBLIC__KEY__FIELD) in ((pat_let_tv131_).encryptionContext)))) and ((((d_328_suite_).signature).is_ECDSA) == (((pat_let_tv132_).signingKey).is_Some))) and ((not(((d_328_suite_).signature).is_None)) == ((default__.EC__PUBLIC__KEY__FIELD) in ((pat_let_tv133_).encryptionContext)))) and (not ((((d_328_suite_).symmetricSignature).is_HMAC) and (((pat_let_tv134_).symmetricSigningKeys).is_Some)) or ((len(((pat_let_tv135_).symmetricSigningKeys).value)) == (len((pat_let_tv136_).encryptedDataKeys))))) and (not (((d_328_suite_).symmetricSignature).is_HMAC) or (((pat_let_tv137_).symmetricSigningKeys).is_Some))) and (not (((d_328_suite_).symmetricSignature).is_None) or (((pat_let_tv138_).symmetricSigningKeys).is_None))) and (_dafny.quantifier(((pat_let_tv139_).requiredEncryptionContextKeys).UniqueElements, True, lambda37_))
            return iife12_(_pat_let1_0)
        return (AlgorithmSuites.default__.AlgorithmSuite_q((encryptionMaterials).algorithmSuite)) and (iife11_((encryptionMaterials).algorithmSuite))

    @staticmethod
    def EncryptionMaterialsHasPlaintextDataKey(encryptionMaterials):
        return ((((encryptionMaterials).plaintextDataKey).is_Some) and ((len((encryptionMaterials).encryptedDataKeys)) > (0))) and (default__.ValidEncryptionMaterials(encryptionMaterials))

    @staticmethod
    def EncryptionMaterialAddEncryptedDataKeys(encryptionMaterials, encryptedDataKeysToAdd, symmetricSigningKeysToAdd):
        d_330_valueOrError0_ = Wrappers.default__.Need(default__.ValidEncryptionMaterials(encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Attempt to modify invalid encryption material.")))
        if (d_330_valueOrError0_).IsFailure():
            return (d_330_valueOrError0_).PropagateFailure()
        elif True:
            d_331_valueOrError1_ = Wrappers.default__.Need(((encryptionMaterials).plaintextDataKey).is_Some, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys without a plaintext data key is not allowed.")))
            if (d_331_valueOrError1_).IsFailure():
                return (d_331_valueOrError1_).PropagateFailure()
            elif True:
                d_332_valueOrError2_ = Wrappers.default__.Need(not ((symmetricSigningKeysToAdd).is_None) or ((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys without a symmetric signing key when using symmetric signing is not allowed.")))
                if (d_332_valueOrError2_).IsFailure():
                    return (d_332_valueOrError2_).PropagateFailure()
                elif True:
                    d_333_valueOrError3_ = Wrappers.default__.Need(not ((symmetricSigningKeysToAdd).is_Some) or (not((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys with a symmetric signing key when not using symmetric signing is not allowed.")))
                    if (d_333_valueOrError3_).IsFailure():
                        return (d_333_valueOrError3_).PropagateFailure()
                    elif True:
                        d_334_symmetricSigningKeys_ = ((encryptionMaterials).symmetricSigningKeys if (symmetricSigningKeysToAdd).is_None else Wrappers.Option_Some((((encryptionMaterials).symmetricSigningKeys).value) + ((symmetricSigningKeysToAdd).value)))
                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials((encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext, ((encryptionMaterials).encryptedDataKeys) + (encryptedDataKeysToAdd), (encryptionMaterials).requiredEncryptionContextKeys, (encryptionMaterials).plaintextDataKey, (encryptionMaterials).signingKey, d_334_symmetricSigningKeys_))

    @staticmethod
    def EncryptionMaterialAddDataKey(encryptionMaterials, plaintextDataKey, encryptedDataKeysToAdd, symmetricSigningKeysToAdd):
        d_335_suite_ = (encryptionMaterials).algorithmSuite
        d_336_valueOrError0_ = Wrappers.default__.Need(default__.ValidEncryptionMaterials(encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Attempt to modify invalid encryption material.")))
        if (d_336_valueOrError0_).IsFailure():
            return (d_336_valueOrError0_).PropagateFailure()
        elif True:
            d_337_valueOrError1_ = Wrappers.default__.Need(((encryptionMaterials).plaintextDataKey).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Attempt to modify plaintextDataKey.")))
            if (d_337_valueOrError1_).IsFailure():
                return (d_337_valueOrError1_).PropagateFailure()
            elif True:
                d_338_valueOrError2_ = Wrappers.default__.Need((AlgorithmSuites.default__.GetEncryptKeyLength(d_335_suite_)) == (len(plaintextDataKey)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("plaintextDataKey does not match Algorithm Suite specification.")))
                if (d_338_valueOrError2_).IsFailure():
                    return (d_338_valueOrError2_).PropagateFailure()
                elif True:
                    d_339_valueOrError3_ = Wrappers.default__.Need(((symmetricSigningKeysToAdd).is_None) == ((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys without a symmetric signing key when using symmetric signing is not allowed.")))
                    if (d_339_valueOrError3_).IsFailure():
                        return (d_339_valueOrError3_).PropagateFailure()
                    elif True:
                        d_340_valueOrError4_ = Wrappers.default__.Need(((symmetricSigningKeysToAdd).is_Some) == (not((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys with a symmetric signing key when not using symmetric signing is not allowed.")))
                        if (d_340_valueOrError4_).IsFailure():
                            return (d_340_valueOrError4_).PropagateFailure()
                        elif True:
                            d_341_symmetricSigningKeys_ = ((encryptionMaterials).symmetricSigningKeys if (symmetricSigningKeysToAdd).is_None else Wrappers.Option_Some((((encryptionMaterials).symmetricSigningKeys).value) + ((symmetricSigningKeysToAdd).value)))
                            return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials((encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext, ((encryptionMaterials).encryptedDataKeys) + (encryptedDataKeysToAdd), (encryptionMaterials).requiredEncryptionContextKeys, Wrappers.Option_Some(plaintextDataKey), (encryptionMaterials).signingKey, d_341_symmetricSigningKeys_))

    @staticmethod
    def DecryptionMaterialsTransitionIsValid(oldMat, newMat):
        return ((((((((((newMat).algorithmSuite) == ((oldMat).algorithmSuite)) and (((newMat).encryptionContext) == ((oldMat).encryptionContext))) and (((newMat).requiredEncryptionContextKeys) == ((oldMat).requiredEncryptionContextKeys))) and (((newMat).verificationKey) == ((oldMat).verificationKey))) and (((oldMat).plaintextDataKey).is_None)) and (((newMat).plaintextDataKey).is_Some)) and (((oldMat).symmetricSigningKey).is_None)) and (default__.ValidDecryptionMaterials(oldMat))) and (default__.ValidDecryptionMaterials(newMat))

    @staticmethod
    def ValidDecryptionMaterials(decryptionMaterials):
        pat_let_tv142_ = decryptionMaterials
        pat_let_tv143_ = decryptionMaterials
        pat_let_tv144_ = decryptionMaterials
        pat_let_tv145_ = decryptionMaterials
        pat_let_tv146_ = decryptionMaterials
        pat_let_tv147_ = decryptionMaterials
        pat_let_tv148_ = decryptionMaterials
        pat_let_tv149_ = decryptionMaterials
        pat_let_tv150_ = decryptionMaterials
        pat_let_tv151_ = decryptionMaterials
        pat_let_tv152_ = decryptionMaterials
        def iife13_(_pat_let2_0):
            def iife14_(d_342_suite_):
                def lambda38_(forall_var_11_):
                    d_343_k_: _dafny.Seq = forall_var_11_
                    return not ((d_343_k_) in ((pat_let_tv151_).requiredEncryptionContextKeys)) or ((d_343_k_) in ((pat_let_tv152_).encryptionContext))

                return ((((((not (((pat_let_tv142_).plaintextDataKey).is_Some) or ((AlgorithmSuites.default__.GetEncryptKeyLength(d_342_suite_)) == (len(((pat_let_tv143_).plaintextDataKey).value)))) and ((not(((d_342_suite_).signature).is_None)) == ((default__.EC__PUBLIC__KEY__FIELD) in ((pat_let_tv144_).encryptionContext)))) and ((((d_342_suite_).signature).is_ECDSA) == (((pat_let_tv145_).verificationKey).is_Some))) and ((not(((d_342_suite_).signature).is_None)) == ((default__.EC__PUBLIC__KEY__FIELD) in ((pat_let_tv146_).encryptionContext)))) and (not (not(((d_342_suite_).symmetricSignature).is_None)) or ((((pat_let_tv147_).plaintextDataKey).is_Some) == (((pat_let_tv148_).symmetricSigningKey).is_Some)))) and (not (((d_342_suite_).symmetricSignature).is_None) or (((pat_let_tv149_).symmetricSigningKey).is_None))) and (_dafny.quantifier(((pat_let_tv150_).requiredEncryptionContextKeys).UniqueElements, True, lambda38_))
            return iife14_(_pat_let2_0)
        return (AlgorithmSuites.default__.AlgorithmSuite_q((decryptionMaterials).algorithmSuite)) and (iife13_((decryptionMaterials).algorithmSuite))

    @staticmethod
    def DecryptionMaterialsAddDataKey(decryptionMaterials, plaintextDataKey, symmetricSigningKey):
        d_344_suite_ = (decryptionMaterials).algorithmSuite
        d_345_valueOrError0_ = Wrappers.default__.Need(default__.ValidDecryptionMaterials(decryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("Attempt to modify invalid decryption material.")))
        if (d_345_valueOrError0_).IsFailure():
            return (d_345_valueOrError0_).PropagateFailure()
        elif True:
            d_346_valueOrError1_ = Wrappers.default__.Need(((decryptionMaterials).plaintextDataKey).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("Attempt to modify plaintextDataKey.")))
            if (d_346_valueOrError1_).IsFailure():
                return (d_346_valueOrError1_).PropagateFailure()
            elif True:
                d_347_valueOrError2_ = Wrappers.default__.Need((AlgorithmSuites.default__.GetEncryptKeyLength(d_344_suite_)) == (len(plaintextDataKey)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("plaintextDataKey does not match Algorithm Suite specification.")))
                if (d_347_valueOrError2_).IsFailure():
                    return (d_347_valueOrError2_).PropagateFailure()
                elif True:
                    d_348_valueOrError3_ = Wrappers.default__.Need(((symmetricSigningKey).is_Some) == (not((((decryptionMaterials).algorithmSuite).symmetricSignature).is_None)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("symmetric signature key must be added with plaintextDataKey if using an algorithm suite with symmetric signing.")))
                    if (d_348_valueOrError3_).IsFailure():
                        return (d_348_valueOrError3_).PropagateFailure()
                    elif True:
                        d_349_valueOrError4_ = Wrappers.default__.Need(((symmetricSigningKey).is_None) == ((((decryptionMaterials).algorithmSuite).symmetricSignature).is_None), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("symmetric signature key cannot be added with plaintextDataKey if using an algorithm suite without symmetric signing.")))
                        if (d_349_valueOrError4_).IsFailure():
                            return (d_349_valueOrError4_).PropagateFailure()
                        elif True:
                            return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials((decryptionMaterials).algorithmSuite, (decryptionMaterials).encryptionContext, (decryptionMaterials).requiredEncryptionContextKeys, Wrappers.Option_Some(plaintextDataKey), (decryptionMaterials).verificationKey, symmetricSigningKey))

    @staticmethod
    def DecryptionMaterialsWithoutPlaintextDataKey(decryptionMaterials):
        return (((decryptionMaterials).plaintextDataKey).is_None) and (default__.ValidDecryptionMaterials(decryptionMaterials))

    @staticmethod
    def DecryptionMaterialsWithPlaintextDataKey(decryptionMaterials):
        return (((decryptionMaterials).plaintextDataKey).is_Some) and (default__.ValidDecryptionMaterials(decryptionMaterials))

    @_dafny.classproperty
    def EC__PUBLIC__KEY__FIELD(instance):
        d_350_s_ = _dafny.Seq([97, 119, 115, 45, 99, 114, 121, 112, 116, 111, 45, 112, 117, 98, 108, 105, 99, 45, 107, 101, 121])
        return d_350_s_
    @_dafny.classproperty
    def RESERVED__KEY__VALUES(instance):
        return _dafny.Set({default__.EC__PUBLIC__KEY__FIELD})

class DecryptionMaterialsPendingPlaintextDataKey:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials.default()()

class SealedDecryptionMaterials:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials.default()()
