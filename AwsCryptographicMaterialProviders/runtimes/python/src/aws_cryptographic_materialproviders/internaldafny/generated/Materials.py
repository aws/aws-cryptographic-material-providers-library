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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
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

# Module: Materials

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def InitializeEncryptionMaterials(input):
        pat_let_tv133_ = input
        pat_let_tv134_ = input
        pat_let_tv135_ = input
        d_337_valueOrError0_ = Wrappers.default__.Need((default__.EC__PUBLIC__KEY__FIELD) not in ((input).encryptionContext), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption Context ")))
        if (d_337_valueOrError0_).IsFailure():
            return (d_337_valueOrError0_).PropagateFailure()
        elif True:
            def lambda35_(forall_var_8_):
                d_339_key_: _dafny.Seq = forall_var_8_
                if UTF8.ValidUTF8Bytes._Is(d_339_key_):
                    return not ((d_339_key_) in ((input).requiredEncryptionContextKeys)) or ((d_339_key_) in ((input).encryptionContext))
                elif True:
                    return True

            d_338_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier(((input).requiredEncryptionContextKeys).UniqueElements, True, lambda35_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Required encryption context keys do not exist in provided encryption context.")))
            if (d_338_valueOrError1_).IsFailure():
                return (d_338_valueOrError1_).PropagateFailure()
            elif True:
                d_340_suite_ = AlgorithmSuites.default__.GetSuite((input).algorithmSuiteId)
                d_341_valueOrError2_ = Wrappers.default__.Need((((d_340_suite_).signature).is_ECDSA) == ((((input).signingKey).is_Some) and (((input).verificationKey).is_Some)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Missing signature key for signed suite.")))
                if (d_341_valueOrError2_).IsFailure():
                    return (d_341_valueOrError2_).PropagateFailure()
                elif True:
                    d_342_valueOrError3_ = Wrappers.default__.Need((((d_340_suite_).signature).is_None) == ((((input).signingKey).is_None) and (((input).verificationKey).is_None)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Signature key not allowed for non-signed suites.")))
                    if (d_342_valueOrError3_).IsFailure():
                        return (d_342_valueOrError3_).PropagateFailure()
                    elif True:
                        def lambda36_():
                            source18_ = (d_340_suite_).signature
                            unmatched18 = True
                            if unmatched18:
                                if source18_.is_ECDSA:
                                    d_344_curve_ = source18_.ECDSA
                                    unmatched18 = False
                                    def lambda37_(d_346_e_):
                                        return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_346_e_)

                                    d_345_valueOrError5_ = (UTF8.default__.Encode(Base64.default__.Encode(((pat_let_tv133_).verificationKey).value))).MapFailure(lambda37_)
                                    if (d_345_valueOrError5_).IsFailure():
                                        return (d_345_valueOrError5_).PropagateFailure()
                                    elif True:
                                        d_347_enc__vk_ = (d_345_valueOrError5_).Extract()
                                        return Wrappers.Result_Success(((pat_let_tv134_).encryptionContext).set(default__.EC__PUBLIC__KEY__FIELD, d_347_enc__vk_))
                            if unmatched18:
                                d_348_None_ = source18_
                                unmatched18 = False
                                return Wrappers.Result_Success((pat_let_tv135_).encryptionContext)
                            raise Exception("unexpected control point")

                        d_343_valueOrError4_ = lambda36_()
                        if (d_343_valueOrError4_).IsFailure():
                            return (d_343_valueOrError4_).PropagateFailure()
                        elif True:
                            d_349_encryptionContext_ = (d_343_valueOrError4_).Extract()
                            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials(d_340_suite_, d_349_encryptionContext_, _dafny.Seq([]), (input).requiredEncryptionContextKeys, Wrappers.Option_None(), (input).signingKey, (Wrappers.Option_None() if ((d_340_suite_).symmetricSignature).is_None else Wrappers.Option_Some(_dafny.Seq([])))))

    @staticmethod
    def InitializeDecryptionMaterials(input):
        def lambda38_(forall_var_9_):
            d_351_key_: _dafny.Seq = forall_var_9_
            if UTF8.ValidUTF8Bytes._Is(d_351_key_):
                return not ((d_351_key_) in ((input).requiredEncryptionContextKeys)) or ((d_351_key_) in ((input).encryptionContext))
            elif True:
                return True

        d_350_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier(((input).requiredEncryptionContextKeys).UniqueElements, True, lambda38_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reporoduced encryption context key did not exist in provided encryption context.")))
        if (d_350_valueOrError0_).IsFailure():
            return (d_350_valueOrError0_).PropagateFailure()
        elif True:
            d_352_suite_ = AlgorithmSuites.default__.GetSuite((input).algorithmSuiteId)
            d_353_valueOrError1_ = Wrappers.default__.Need((((d_352_suite_).signature).is_ECDSA) == ((default__.EC__PUBLIC__KEY__FIELD) in ((input).encryptionContext)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption Context missing verification key.")))
            if (d_353_valueOrError1_).IsFailure():
                return (d_353_valueOrError1_).PropagateFailure()
            elif True:
                d_354_valueOrError2_ = Wrappers.default__.Need((((d_352_suite_).signature).is_None) == ((default__.EC__PUBLIC__KEY__FIELD) not in ((input).encryptionContext)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Verification key can not exist in non-signed Algorithm Suites.")))
                if (d_354_valueOrError2_).IsFailure():
                    return (d_354_valueOrError2_).PropagateFailure()
                elif True:
                    d_355_valueOrError3_ = default__.DecodeVerificationKey((input).encryptionContext)
                    if (d_355_valueOrError3_).IsFailure():
                        return (d_355_valueOrError3_).PropagateFailure()
                    elif True:
                        d_356_verificationKey_ = (d_355_valueOrError3_).Extract()
                        return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.DecryptionMaterials_DecryptionMaterials(d_352_suite_, (input).encryptionContext, (input).requiredEncryptionContextKeys, Wrappers.Option_None(), d_356_verificationKey_, Wrappers.Option_None()))

    @staticmethod
    def DecodeVerificationKey(encryptionContext):
        if (default__.EC__PUBLIC__KEY__FIELD) in (encryptionContext):
            d_357_utf8Key_ = (encryptionContext)[default__.EC__PUBLIC__KEY__FIELD]
            def lambda39_(d_359_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_359_e_)

            d_358_valueOrError0_ = (UTF8.default__.Decode(d_357_utf8Key_)).MapFailure(lambda39_)
            if (d_358_valueOrError0_).IsFailure():
                return (d_358_valueOrError0_).PropagateFailure()
            elif True:
                d_360_base64Key_ = (d_358_valueOrError0_).Extract()
                def lambda40_(d_362_e_):
                    return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_362_e_)

                d_361_valueOrError1_ = (Base64.default__.Decode(d_360_base64Key_)).MapFailure(lambda40_)
                if (d_361_valueOrError1_).IsFailure():
                    return (d_361_valueOrError1_).PropagateFailure()
                elif True:
                    d_363_key_ = (d_361_valueOrError1_).Extract()
                    return Wrappers.Result_Success(Wrappers.Option_Some(d_363_key_))
        elif True:
            return Wrappers.Result_Success(Wrappers.Option_None())

    @staticmethod
    def ValidEncryptionMaterialsTransition(oldMat, newMat):
        return ((((((((((((newMat).algorithmSuite) == ((oldMat).algorithmSuite)) and (((newMat).encryptionContext) == ((oldMat).encryptionContext))) and (((newMat).requiredEncryptionContextKeys) == ((oldMat).requiredEncryptionContextKeys))) and (((newMat).signingKey) == ((oldMat).signingKey))) and (((((oldMat).plaintextDataKey).is_None) and (((newMat).plaintextDataKey).is_Some)) or (((oldMat).plaintextDataKey) == ((newMat).plaintextDataKey)))) and (((newMat).plaintextDataKey).is_Some)) and ((len((oldMat).encryptedDataKeys)) <= (len((newMat).encryptedDataKeys)))) and ((_dafny.MultiSet((oldMat).encryptedDataKeys)).issubset(_dafny.MultiSet((newMat).encryptedDataKeys)))) and (not (not((((oldMat).algorithmSuite).symmetricSignature).is_None)) or (((((newMat).symmetricSigningKeys).is_Some) and (((oldMat).symmetricSigningKeys).is_Some)) and ((_dafny.MultiSet(((oldMat).symmetricSigningKeys).value)).issubset(_dafny.MultiSet(((newMat).symmetricSigningKeys).value)))))) and (default__.ValidEncryptionMaterials(oldMat))) and (default__.ValidEncryptionMaterials(newMat))

    @staticmethod
    def ValidEncryptionMaterials(encryptionMaterials):
        pat_let_tv136_ = encryptionMaterials
        pat_let_tv137_ = encryptionMaterials
        pat_let_tv138_ = encryptionMaterials
        pat_let_tv139_ = encryptionMaterials
        pat_let_tv140_ = encryptionMaterials
        pat_let_tv141_ = encryptionMaterials
        pat_let_tv142_ = encryptionMaterials
        pat_let_tv143_ = encryptionMaterials
        pat_let_tv144_ = encryptionMaterials
        pat_let_tv145_ = encryptionMaterials
        pat_let_tv146_ = encryptionMaterials
        pat_let_tv147_ = encryptionMaterials
        pat_let_tv148_ = encryptionMaterials
        pat_let_tv149_ = encryptionMaterials
        pat_let_tv150_ = encryptionMaterials
        pat_let_tv151_ = encryptionMaterials
        def iife13_(_pat_let2_0):
            def iife14_(d_364_suite_):
                def lambda41_(forall_var_10_):
                    d_365_key_: _dafny.Seq = forall_var_10_
                    if UTF8.ValidUTF8Bytes._Is(d_365_key_):
                        return not ((d_365_key_) in ((pat_let_tv150_).requiredEncryptionContextKeys)) or ((d_365_key_) in ((pat_let_tv151_).encryptionContext))
                    elif True:
                        return True

                return ((((((((((((d_364_suite_).signature).is_None) == (((pat_let_tv136_).signingKey).is_None)) and (not (((pat_let_tv137_).plaintextDataKey).is_Some) or ((AlgorithmSuites.default__.GetEncryptKeyLength(d_364_suite_)) == (len(((pat_let_tv138_).plaintextDataKey).value))))) and (not (((pat_let_tv139_).plaintextDataKey).is_None) or ((len((pat_let_tv140_).encryptedDataKeys)) == (0)))) and ((not(((d_364_suite_).signature).is_None)) == ((default__.EC__PUBLIC__KEY__FIELD) in ((pat_let_tv141_).encryptionContext)))) and ((((d_364_suite_).signature).is_ECDSA) == (((pat_let_tv142_).signingKey).is_Some))) and ((not(((d_364_suite_).signature).is_None)) == ((default__.EC__PUBLIC__KEY__FIELD) in ((pat_let_tv143_).encryptionContext)))) and (not ((((d_364_suite_).symmetricSignature).is_HMAC) and (((pat_let_tv144_).symmetricSigningKeys).is_Some)) or ((len(((pat_let_tv145_).symmetricSigningKeys).value)) == (len((pat_let_tv146_).encryptedDataKeys))))) and (not (((d_364_suite_).symmetricSignature).is_HMAC) or (((pat_let_tv147_).symmetricSigningKeys).is_Some))) and (not (((d_364_suite_).symmetricSignature).is_None) or (((pat_let_tv148_).symmetricSigningKeys).is_None))) and (_dafny.quantifier(((pat_let_tv149_).requiredEncryptionContextKeys).UniqueElements, True, lambda41_))
            return iife14_(_pat_let2_0)
        return (AlgorithmSuites.default__.AlgorithmSuite_q((encryptionMaterials).algorithmSuite)) and (iife13_((encryptionMaterials).algorithmSuite))

    @staticmethod
    def EncryptionMaterialsHasPlaintextDataKey(encryptionMaterials):
        return ((((encryptionMaterials).plaintextDataKey).is_Some) and ((len((encryptionMaterials).encryptedDataKeys)) > (0))) and (default__.ValidEncryptionMaterials(encryptionMaterials))

    @staticmethod
    def EncryptionMaterialAddEncryptedDataKeys(encryptionMaterials, encryptedDataKeysToAdd, symmetricSigningKeysToAdd):
        d_366_valueOrError0_ = Wrappers.default__.Need(default__.ValidEncryptionMaterials(encryptionMaterials), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Attempt to modify invalid encryption material.")))
        if (d_366_valueOrError0_).IsFailure():
            return (d_366_valueOrError0_).PropagateFailure()
        elif True:
            d_367_valueOrError1_ = Wrappers.default__.Need(((encryptionMaterials).plaintextDataKey).is_Some, AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys without a plaintext data key is not allowed.")))
            if (d_367_valueOrError1_).IsFailure():
                return (d_367_valueOrError1_).PropagateFailure()
            elif True:
                d_368_valueOrError2_ = Wrappers.default__.Need(not ((symmetricSigningKeysToAdd).is_None) or ((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys without a symmetric signing key when using symmetric signing is not allowed.")))
                if (d_368_valueOrError2_).IsFailure():
                    return (d_368_valueOrError2_).PropagateFailure()
                elif True:
                    d_369_valueOrError3_ = Wrappers.default__.Need(not ((symmetricSigningKeysToAdd).is_Some) or (not((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None)), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys with a symmetric signing key when not using symmetric signing is not allowed.")))
                    if (d_369_valueOrError3_).IsFailure():
                        return (d_369_valueOrError3_).PropagateFailure()
                    elif True:
                        d_370_symmetricSigningKeys_ = ((encryptionMaterials).symmetricSigningKeys if (symmetricSigningKeysToAdd).is_None else Wrappers.Option_Some((((encryptionMaterials).symmetricSigningKeys).value) + ((symmetricSigningKeysToAdd).value)))
                        return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext, ((encryptionMaterials).encryptedDataKeys) + (encryptedDataKeysToAdd), (encryptionMaterials).requiredEncryptionContextKeys, (encryptionMaterials).plaintextDataKey, (encryptionMaterials).signingKey, d_370_symmetricSigningKeys_))

    @staticmethod
    def EncryptionMaterialAddDataKey(encryptionMaterials, plaintextDataKey, encryptedDataKeysToAdd, symmetricSigningKeysToAdd):
        d_371_suite_ = (encryptionMaterials).algorithmSuite
        d_372_valueOrError0_ = Wrappers.default__.Need(default__.ValidEncryptionMaterials(encryptionMaterials), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Attempt to modify invalid encryption material.")))
        if (d_372_valueOrError0_).IsFailure():
            return (d_372_valueOrError0_).PropagateFailure()
        elif True:
            d_373_valueOrError1_ = Wrappers.default__.Need(((encryptionMaterials).plaintextDataKey).is_None, AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Attempt to modify plaintextDataKey.")))
            if (d_373_valueOrError1_).IsFailure():
                return (d_373_valueOrError1_).PropagateFailure()
            elif True:
                d_374_valueOrError2_ = Wrappers.default__.Need((AlgorithmSuites.default__.GetEncryptKeyLength(d_371_suite_)) == (len(plaintextDataKey)), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("plaintextDataKey does not match Algorithm Suite specification.")))
                if (d_374_valueOrError2_).IsFailure():
                    return (d_374_valueOrError2_).PropagateFailure()
                elif True:
                    d_375_valueOrError3_ = Wrappers.default__.Need(((symmetricSigningKeysToAdd).is_None) == ((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys without a symmetric signing key when using symmetric signing is not allowed.")))
                    if (d_375_valueOrError3_).IsFailure():
                        return (d_375_valueOrError3_).PropagateFailure()
                    elif True:
                        d_376_valueOrError4_ = Wrappers.default__.Need(((symmetricSigningKeysToAdd).is_Some) == (not((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None)), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys with a symmetric signing key when not using symmetric signing is not allowed.")))
                        if (d_376_valueOrError4_).IsFailure():
                            return (d_376_valueOrError4_).PropagateFailure()
                        elif True:
                            d_377_symmetricSigningKeys_ = ((encryptionMaterials).symmetricSigningKeys if (symmetricSigningKeysToAdd).is_None else Wrappers.Option_Some((((encryptionMaterials).symmetricSigningKeys).value) + ((symmetricSigningKeysToAdd).value)))
                            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext, ((encryptionMaterials).encryptedDataKeys) + (encryptedDataKeysToAdd), (encryptionMaterials).requiredEncryptionContextKeys, Wrappers.Option_Some(plaintextDataKey), (encryptionMaterials).signingKey, d_377_symmetricSigningKeys_))

    @staticmethod
    def DecryptionMaterialsTransitionIsValid(oldMat, newMat):
        return ((((((((((newMat).algorithmSuite) == ((oldMat).algorithmSuite)) and (((newMat).encryptionContext) == ((oldMat).encryptionContext))) and (((newMat).requiredEncryptionContextKeys) == ((oldMat).requiredEncryptionContextKeys))) and (((newMat).verificationKey) == ((oldMat).verificationKey))) and (((oldMat).plaintextDataKey).is_None)) and (((newMat).plaintextDataKey).is_Some)) and (((oldMat).symmetricSigningKey).is_None)) and (default__.ValidDecryptionMaterials(oldMat))) and (default__.ValidDecryptionMaterials(newMat))

    @staticmethod
    def ValidDecryptionMaterials(decryptionMaterials):
        pat_let_tv152_ = decryptionMaterials
        pat_let_tv153_ = decryptionMaterials
        pat_let_tv154_ = decryptionMaterials
        pat_let_tv155_ = decryptionMaterials
        pat_let_tv156_ = decryptionMaterials
        pat_let_tv157_ = decryptionMaterials
        pat_let_tv158_ = decryptionMaterials
        pat_let_tv159_ = decryptionMaterials
        pat_let_tv160_ = decryptionMaterials
        pat_let_tv161_ = decryptionMaterials
        pat_let_tv162_ = decryptionMaterials
        def iife15_(_pat_let3_0):
            def iife16_(d_378_suite_):
                def lambda42_(forall_var_11_):
                    d_379_k_: _dafny.Seq = forall_var_11_
                    if UTF8.ValidUTF8Bytes._Is(d_379_k_):
                        return not ((d_379_k_) in ((pat_let_tv161_).requiredEncryptionContextKeys)) or ((d_379_k_) in ((pat_let_tv162_).encryptionContext))
                    elif True:
                        return True

                return ((((((not (((pat_let_tv152_).plaintextDataKey).is_Some) or ((AlgorithmSuites.default__.GetEncryptKeyLength(d_378_suite_)) == (len(((pat_let_tv153_).plaintextDataKey).value)))) and ((not(((d_378_suite_).signature).is_None)) == ((default__.EC__PUBLIC__KEY__FIELD) in ((pat_let_tv154_).encryptionContext)))) and ((((d_378_suite_).signature).is_ECDSA) == (((pat_let_tv155_).verificationKey).is_Some))) and ((not(((d_378_suite_).signature).is_None)) == ((default__.EC__PUBLIC__KEY__FIELD) in ((pat_let_tv156_).encryptionContext)))) and (not (not(((d_378_suite_).symmetricSignature).is_None)) or ((((pat_let_tv157_).plaintextDataKey).is_Some) == (((pat_let_tv158_).symmetricSigningKey).is_Some)))) and (not (((d_378_suite_).symmetricSignature).is_None) or (((pat_let_tv159_).symmetricSigningKey).is_None))) and (_dafny.quantifier(((pat_let_tv160_).requiredEncryptionContextKeys).UniqueElements, True, lambda42_))
            return iife16_(_pat_let3_0)
        return (AlgorithmSuites.default__.AlgorithmSuite_q((decryptionMaterials).algorithmSuite)) and (iife15_((decryptionMaterials).algorithmSuite))

    @staticmethod
    def DecryptionMaterialsAddDataKey(decryptionMaterials, plaintextDataKey, symmetricSigningKey):
        d_380_suite_ = (decryptionMaterials).algorithmSuite
        d_381_valueOrError0_ = Wrappers.default__.Need(default__.ValidDecryptionMaterials(decryptionMaterials), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("Attempt to modify invalid decryption material.")))
        if (d_381_valueOrError0_).IsFailure():
            return (d_381_valueOrError0_).PropagateFailure()
        elif True:
            d_382_valueOrError1_ = Wrappers.default__.Need(((decryptionMaterials).plaintextDataKey).is_None, AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("Attempt to modify plaintextDataKey.")))
            if (d_382_valueOrError1_).IsFailure():
                return (d_382_valueOrError1_).PropagateFailure()
            elif True:
                d_383_valueOrError2_ = Wrappers.default__.Need((AlgorithmSuites.default__.GetEncryptKeyLength(d_380_suite_)) == (len(plaintextDataKey)), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("plaintextDataKey does not match Algorithm Suite specification.")))
                if (d_383_valueOrError2_).IsFailure():
                    return (d_383_valueOrError2_).PropagateFailure()
                elif True:
                    d_384_valueOrError3_ = Wrappers.default__.Need(((symmetricSigningKey).is_Some) == (not((((decryptionMaterials).algorithmSuite).symmetricSignature).is_None)), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("symmetric signature key must be added with plaintextDataKey if using an algorithm suite with symmetric signing.")))
                    if (d_384_valueOrError3_).IsFailure():
                        return (d_384_valueOrError3_).PropagateFailure()
                    elif True:
                        d_385_valueOrError4_ = Wrappers.default__.Need(((symmetricSigningKey).is_None) == ((((decryptionMaterials).algorithmSuite).symmetricSignature).is_None), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("symmetric signature key cannot be added with plaintextDataKey if using an algorithm suite without symmetric signing.")))
                        if (d_385_valueOrError4_).IsFailure():
                            return (d_385_valueOrError4_).PropagateFailure()
                        elif True:
                            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.DecryptionMaterials_DecryptionMaterials((decryptionMaterials).algorithmSuite, (decryptionMaterials).encryptionContext, (decryptionMaterials).requiredEncryptionContextKeys, Wrappers.Option_Some(plaintextDataKey), (decryptionMaterials).verificationKey, symmetricSigningKey))

    @staticmethod
    def DecryptionMaterialsWithoutPlaintextDataKey(decryptionMaterials):
        return (((decryptionMaterials).plaintextDataKey).is_None) and (default__.ValidDecryptionMaterials(decryptionMaterials))

    @staticmethod
    def DecryptionMaterialsWithPlaintextDataKey(decryptionMaterials):
        return (((decryptionMaterials).plaintextDataKey).is_Some) and (default__.ValidDecryptionMaterials(decryptionMaterials))

    @_dafny.classproperty
    def EC__PUBLIC__KEY__FIELD(instance):
        d_386_s_ = _dafny.Seq([97, 119, 115, 45, 99, 114, 121, 112, 116, 111, 45, 112, 117, 98, 108, 105, 99, 45, 107, 101, 121])
        return d_386_s_
    @_dafny.classproperty
    def RESERVED__KEY__VALUES(instance):
        return _dafny.Set({default__.EC__PUBLIC__KEY__FIELD})

class DecryptionMaterialsPendingPlaintextDataKey:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return AwsCryptographyMaterialProvidersTypes.DecryptionMaterials.default()()
    def _Is(source__):
        d_387_d_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = source__
        return default__.DecryptionMaterialsWithoutPlaintextDataKey(d_387_d_)

class SealedDecryptionMaterials:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return AwsCryptographyMaterialProvidersTypes.DecryptionMaterials.default()()
    def _Is(source__):
        d_388_d_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = source__
        return default__.DecryptionMaterialsWithPlaintextDataKey(d_388_d_)
