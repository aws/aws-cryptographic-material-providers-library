import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_material_providers.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_Sequence as StandardLibrary_Sequence
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_material_providers.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites

# Module: Materials

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def InitializeEncryptionMaterials(input):
        d_0_valueOrError0_ = Wrappers.default__.Need((default__.EC__PUBLIC__KEY__FIELD) not in ((input).encryptionContext), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption Context ")))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            def lambda0_(forall_var_0_):
                d_2_key_: _dafny.Seq = forall_var_0_
                if UTF8.ValidUTF8Bytes._Is(d_2_key_):
                    return not ((d_2_key_) in ((input).requiredEncryptionContextKeys)) or ((d_2_key_) in ((input).encryptionContext))
                elif True:
                    return True

            d_1_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier(((input).requiredEncryptionContextKeys).UniqueElements, True, lambda0_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Required encryption context keys do not exist in provided encryption context.")))
            if (d_1_valueOrError1_).IsFailure():
                return (d_1_valueOrError1_).PropagateFailure()
            elif True:
                d_3_suite_ = AlgorithmSuites.default__.GetSuite((input).algorithmSuiteId)
                d_4_valueOrError2_ = Wrappers.default__.Need((((d_3_suite_).signature).is_ECDSA) == ((((input).signingKey).is_Some) and (((input).verificationKey).is_Some)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Missing signature key for signed suite.")))
                if (d_4_valueOrError2_).IsFailure():
                    return (d_4_valueOrError2_).PropagateFailure()
                elif True:
                    d_5_valueOrError3_ = Wrappers.default__.Need((((d_3_suite_).signature).is_None) == ((((input).signingKey).is_None) and (((input).verificationKey).is_None)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Signature key not allowed for non-signed suites.")))
                    if (d_5_valueOrError3_).IsFailure():
                        return (d_5_valueOrError3_).PropagateFailure()
                    elif True:
                        def lambda1_():
                            source0_ = (d_3_suite_).signature
                            if True:
                                if source0_.is_ECDSA:
                                    d_7_curve_ = source0_.ECDSA
                                    def lambda2_(d_9_e_):
                                        return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_9_e_)

                                    d_8_valueOrError5_ = (UTF8.default__.Encode(Base64.default__.Encode(((input).verificationKey).value))).MapFailure(lambda2_)
                                    if (d_8_valueOrError5_).IsFailure():
                                        return (d_8_valueOrError5_).PropagateFailure()
                                    elif True:
                                        d_10_enc__vk_ = (d_8_valueOrError5_).Extract()
                                        return Wrappers.Result_Success(((input).encryptionContext).set(default__.EC__PUBLIC__KEY__FIELD, d_10_enc__vk_))
                            if True:
                                d_11_None_ = source0_
                                return Wrappers.Result_Success((input).encryptionContext)

                        d_6_valueOrError4_ = lambda1_()
                        if (d_6_valueOrError4_).IsFailure():
                            return (d_6_valueOrError4_).PropagateFailure()
                        elif True:
                            d_12_encryptionContext_ = (d_6_valueOrError4_).Extract()
                            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials(d_3_suite_, d_12_encryptionContext_, _dafny.Seq([]), (input).requiredEncryptionContextKeys, Wrappers.Option_None(), (input).signingKey, (Wrappers.Option_None() if ((d_3_suite_).symmetricSignature).is_None else Wrappers.Option_Some(_dafny.Seq([])))))

    @staticmethod
    def InitializeDecryptionMaterials(input):
        def lambda0_(forall_var_0_):
            d_1_key_: _dafny.Seq = forall_var_0_
            if UTF8.ValidUTF8Bytes._Is(d_1_key_):
                return not ((d_1_key_) in ((input).requiredEncryptionContextKeys)) or ((d_1_key_) in ((input).encryptionContext))
            elif True:
                return True

        d_0_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier(((input).requiredEncryptionContextKeys).UniqueElements, True, lambda0_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reporoduced encryption context key did not exist in provided encryption context.")))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_2_suite_ = AlgorithmSuites.default__.GetSuite((input).algorithmSuiteId)
            d_3_valueOrError1_ = Wrappers.default__.Need((((d_2_suite_).signature).is_ECDSA) == ((default__.EC__PUBLIC__KEY__FIELD) in ((input).encryptionContext)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption Context missing verification key.")))
            if (d_3_valueOrError1_).IsFailure():
                return (d_3_valueOrError1_).PropagateFailure()
            elif True:
                d_4_valueOrError2_ = Wrappers.default__.Need((((d_2_suite_).signature).is_None) == ((default__.EC__PUBLIC__KEY__FIELD) not in ((input).encryptionContext)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Verification key can not exist in non-signed Algorithm Suites.")))
                if (d_4_valueOrError2_).IsFailure():
                    return (d_4_valueOrError2_).PropagateFailure()
                elif True:
                    d_5_valueOrError3_ = default__.DecodeVerificationKey((input).encryptionContext)
                    if (d_5_valueOrError3_).IsFailure():
                        return (d_5_valueOrError3_).PropagateFailure()
                    elif True:
                        d_6_verificationKey_ = (d_5_valueOrError3_).Extract()
                        return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.DecryptionMaterials_DecryptionMaterials(d_2_suite_, (input).encryptionContext, (input).requiredEncryptionContextKeys, Wrappers.Option_None(), d_6_verificationKey_, Wrappers.Option_None()))

    @staticmethod
    def DecodeVerificationKey(encryptionContext):
        if (default__.EC__PUBLIC__KEY__FIELD) in (encryptionContext):
            d_0_utf8Key_ = (encryptionContext)[default__.EC__PUBLIC__KEY__FIELD]
            def lambda0_(d_2_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_2_e_)

            d_1_valueOrError0_ = (UTF8.default__.Decode(d_0_utf8Key_)).MapFailure(lambda0_)
            if (d_1_valueOrError0_).IsFailure():
                return (d_1_valueOrError0_).PropagateFailure()
            elif True:
                d_3_base64Key_ = (d_1_valueOrError0_).Extract()
                def lambda1_(d_5_e_):
                    return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_5_e_)

                d_4_valueOrError1_ = (Base64.default__.Decode(d_3_base64Key_)).MapFailure(lambda1_)
                if (d_4_valueOrError1_).IsFailure():
                    return (d_4_valueOrError1_).PropagateFailure()
                elif True:
                    d_6_key_ = (d_4_valueOrError1_).Extract()
                    return Wrappers.Result_Success(Wrappers.Option_Some(d_6_key_))
        elif True:
            return Wrappers.Result_Success(Wrappers.Option_None())

    @staticmethod
    def ValidEncryptionMaterialsTransition(oldMat, newMat):
        return ((((((((((((newMat).algorithmSuite) == ((oldMat).algorithmSuite)) and (((newMat).encryptionContext) == ((oldMat).encryptionContext))) and (((newMat).requiredEncryptionContextKeys) == ((oldMat).requiredEncryptionContextKeys))) and (((newMat).signingKey) == ((oldMat).signingKey))) and (((((oldMat).plaintextDataKey).is_None) and (((newMat).plaintextDataKey).is_Some)) or (((oldMat).plaintextDataKey) == ((newMat).plaintextDataKey)))) and (((newMat).plaintextDataKey).is_Some)) and ((len((oldMat).encryptedDataKeys)) <= (len((newMat).encryptedDataKeys)))) and ((_dafny.MultiSet((oldMat).encryptedDataKeys)).issubset(_dafny.MultiSet((newMat).encryptedDataKeys)))) and (not (not((((oldMat).algorithmSuite).symmetricSignature).is_None)) or (((((newMat).symmetricSigningKeys).is_Some) and ((((oldMat).symmetricSigningKeys).is_Some) or ((((oldMat).symmetricSigningKeys).is_None) and ((len((oldMat).encryptedDataKeys)) == (0))))) and ((_dafny.MultiSet(((oldMat).symmetricSigningKeys).UnwrapOr(_dafny.Seq([])))).issubset(_dafny.MultiSet(((newMat).symmetricSigningKeys).value)))))) and (default__.ValidEncryptionMaterials(oldMat))) and (default__.ValidEncryptionMaterials(newMat))

    @staticmethod
    def ValidEncryptionMaterials(encryptionMaterials):
        pat_let_tv0_ = encryptionMaterials
        pat_let_tv1_ = encryptionMaterials
        pat_let_tv2_ = encryptionMaterials
        pat_let_tv3_ = encryptionMaterials
        pat_let_tv4_ = encryptionMaterials
        pat_let_tv5_ = encryptionMaterials
        pat_let_tv6_ = encryptionMaterials
        pat_let_tv7_ = encryptionMaterials
        pat_let_tv8_ = encryptionMaterials
        pat_let_tv9_ = encryptionMaterials
        pat_let_tv10_ = encryptionMaterials
        pat_let_tv11_ = encryptionMaterials
        pat_let_tv12_ = encryptionMaterials
        pat_let_tv13_ = encryptionMaterials
        pat_let_tv14_ = encryptionMaterials
        pat_let_tv15_ = encryptionMaterials
        pat_let_tv16_ = encryptionMaterials
        pat_let_tv17_ = encryptionMaterials
        def iife0_(_pat_let2_0):
            def iife1_(d_0_suite_):
                def lambda0_(forall_var_0_):
                    d_1_key_: _dafny.Seq = forall_var_0_
                    if UTF8.ValidUTF8Bytes._Is(d_1_key_):
                        return not ((d_1_key_) in ((pat_let_tv16_).requiredEncryptionContextKeys)) or ((d_1_key_) in ((pat_let_tv17_).encryptionContext))
                    elif True:
                        return True

                return ((((((((((((d_0_suite_).signature).is_None) == (((pat_let_tv0_).signingKey).is_None)) and (not (((pat_let_tv1_).plaintextDataKey).is_Some) or ((AlgorithmSuites.default__.GetEncryptKeyLength(d_0_suite_)) == (len(((pat_let_tv2_).plaintextDataKey).value))))) and (not (((pat_let_tv3_).plaintextDataKey).is_None) or ((len((pat_let_tv4_).encryptedDataKeys)) == (0)))) and ((not(((d_0_suite_).signature).is_None)) == ((default__.EC__PUBLIC__KEY__FIELD) in ((pat_let_tv5_).encryptionContext)))) and ((((d_0_suite_).signature).is_ECDSA) == (((pat_let_tv6_).signingKey).is_Some))) and ((not(((d_0_suite_).signature).is_None)) == ((default__.EC__PUBLIC__KEY__FIELD) in ((pat_let_tv7_).encryptionContext)))) and (not ((((d_0_suite_).symmetricSignature).is_HMAC) and (((pat_let_tv8_).symmetricSigningKeys).is_Some)) or ((len(((pat_let_tv9_).symmetricSigningKeys).value)) == (len((pat_let_tv10_).encryptedDataKeys))))) and (not (((d_0_suite_).symmetricSignature).is_HMAC) or ((((pat_let_tv11_).symmetricSigningKeys).is_Some) or (((len((pat_let_tv12_).encryptedDataKeys)) == (0)) and (((pat_let_tv13_).symmetricSigningKeys).is_None))))) and (not (((d_0_suite_).symmetricSignature).is_None) or (((pat_let_tv14_).symmetricSigningKeys).is_None))) and (_dafny.quantifier(((pat_let_tv15_).requiredEncryptionContextKeys).UniqueElements, True, lambda0_))
            return iife1_(_pat_let2_0)
        return (AlgorithmSuites.default__.AlgorithmSuite_q((encryptionMaterials).algorithmSuite)) and (iife0_((encryptionMaterials).algorithmSuite))

    @staticmethod
    def EncryptionMaterialsHasPlaintextDataKey(encryptionMaterials):
        return ((((encryptionMaterials).plaintextDataKey).is_Some) and ((len((encryptionMaterials).encryptedDataKeys)) > (0))) and (default__.ValidEncryptionMaterials(encryptionMaterials))

    @staticmethod
    def EncryptionMaterialAddEncryptedDataKeys(encryptionMaterials, encryptedDataKeysToAdd, symmetricSigningKeysToAdd):
        d_0_valueOrError0_ = Wrappers.default__.Need(default__.ValidEncryptionMaterials(encryptionMaterials), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Attempt to modify invalid encryption material.")))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_valueOrError1_ = Wrappers.default__.Need(((encryptionMaterials).plaintextDataKey).is_Some, AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys without a plaintext data key is not allowed.")))
            if (d_1_valueOrError1_).IsFailure():
                return (d_1_valueOrError1_).PropagateFailure()
            elif True:
                d_2_valueOrError2_ = Wrappers.default__.Need(not ((symmetricSigningKeysToAdd).is_None) or ((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys without a symmetric signing key when using symmetric signing is not allowed.")))
                if (d_2_valueOrError2_).IsFailure():
                    return (d_2_valueOrError2_).PropagateFailure()
                elif True:
                    d_3_valueOrError3_ = Wrappers.default__.Need(not ((symmetricSigningKeysToAdd).is_Some) or (not((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None)), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys with a symmetric signing key when not using symmetric signing is not allowed.")))
                    if (d_3_valueOrError3_).IsFailure():
                        return (d_3_valueOrError3_).PropagateFailure()
                    elif True:
                        d_4_symmetricSigningKeys_ = ((encryptionMaterials).symmetricSigningKeys if (symmetricSigningKeysToAdd).is_None else Wrappers.Option_Some((((encryptionMaterials).symmetricSigningKeys).UnwrapOr(_dafny.Seq([]))) + ((symmetricSigningKeysToAdd).value)))
                        return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext, ((encryptionMaterials).encryptedDataKeys) + (encryptedDataKeysToAdd), (encryptionMaterials).requiredEncryptionContextKeys, (encryptionMaterials).plaintextDataKey, (encryptionMaterials).signingKey, d_4_symmetricSigningKeys_))

    @staticmethod
    def EncryptionMaterialAddDataKey(encryptionMaterials, plaintextDataKey, encryptedDataKeysToAdd, symmetricSigningKeysToAdd):
        d_0_suite_ = (encryptionMaterials).algorithmSuite
        d_1_valueOrError0_ = Wrappers.default__.Need(default__.ValidEncryptionMaterials(encryptionMaterials), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Attempt to modify invalid encryption material.")))
        if (d_1_valueOrError0_).IsFailure():
            return (d_1_valueOrError0_).PropagateFailure()
        elif True:
            d_2_valueOrError1_ = Wrappers.default__.Need(((encryptionMaterials).plaintextDataKey).is_None, AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Attempt to modify plaintextDataKey.")))
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_valueOrError2_ = Wrappers.default__.Need((AlgorithmSuites.default__.GetEncryptKeyLength(d_0_suite_)) == (len(plaintextDataKey)), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("plaintextDataKey does not match Algorithm Suite specification.")))
                if (d_3_valueOrError2_).IsFailure():
                    return (d_3_valueOrError2_).PropagateFailure()
                elif True:
                    d_4_valueOrError3_ = Wrappers.default__.Need(((symmetricSigningKeysToAdd).is_None) == ((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys without a symmetric signing key when using symmetric signing is not allowed.")))
                    if (d_4_valueOrError3_).IsFailure():
                        return (d_4_valueOrError3_).PropagateFailure()
                    elif True:
                        d_5_valueOrError4_ = Wrappers.default__.Need(((symmetricSigningKeysToAdd).is_Some) == (not((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None)), AwsCryptographyMaterialProvidersTypes.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys with a symmetric signing key when not using symmetric signing is not allowed.")))
                        if (d_5_valueOrError4_).IsFailure():
                            return (d_5_valueOrError4_).PropagateFailure()
                        elif True:
                            d_6_symmetricSigningKeys_ = ((encryptionMaterials).symmetricSigningKeys if (symmetricSigningKeysToAdd).is_None else Wrappers.Option_Some((((encryptionMaterials).symmetricSigningKeys).UnwrapOr(_dafny.Seq([]))) + ((symmetricSigningKeysToAdd).value)))
                            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials((encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext, ((encryptionMaterials).encryptedDataKeys) + (encryptedDataKeysToAdd), (encryptionMaterials).requiredEncryptionContextKeys, Wrappers.Option_Some(plaintextDataKey), (encryptionMaterials).signingKey, d_6_symmetricSigningKeys_))

    @staticmethod
    def DecryptionMaterialsTransitionIsValid(oldMat, newMat):
        return ((((((((((newMat).algorithmSuite) == ((oldMat).algorithmSuite)) and (((newMat).encryptionContext) == ((oldMat).encryptionContext))) and (((newMat).requiredEncryptionContextKeys) == ((oldMat).requiredEncryptionContextKeys))) and (((newMat).verificationKey) == ((oldMat).verificationKey))) and (((oldMat).plaintextDataKey).is_None)) and (((newMat).plaintextDataKey).is_Some)) and (((oldMat).symmetricSigningKey).is_None)) and (default__.ValidDecryptionMaterials(oldMat))) and (default__.ValidDecryptionMaterials(newMat))

    @staticmethod
    def ValidDecryptionMaterials(decryptionMaterials):
        pat_let_tv0_ = decryptionMaterials
        pat_let_tv1_ = decryptionMaterials
        pat_let_tv2_ = decryptionMaterials
        pat_let_tv3_ = decryptionMaterials
        pat_let_tv4_ = decryptionMaterials
        pat_let_tv5_ = decryptionMaterials
        pat_let_tv6_ = decryptionMaterials
        pat_let_tv7_ = decryptionMaterials
        pat_let_tv8_ = decryptionMaterials
        pat_let_tv9_ = decryptionMaterials
        pat_let_tv10_ = decryptionMaterials
        def iife0_(_pat_let3_0):
            def iife1_(d_0_suite_):
                def lambda0_(forall_var_0_):
                    d_1_k_: _dafny.Seq = forall_var_0_
                    if UTF8.ValidUTF8Bytes._Is(d_1_k_):
                        return not ((d_1_k_) in ((pat_let_tv9_).requiredEncryptionContextKeys)) or ((d_1_k_) in ((pat_let_tv10_).encryptionContext))
                    elif True:
                        return True

                return ((((((not (((pat_let_tv0_).plaintextDataKey).is_Some) or ((AlgorithmSuites.default__.GetEncryptKeyLength(d_0_suite_)) == (len(((pat_let_tv1_).plaintextDataKey).value)))) and ((not(((d_0_suite_).signature).is_None)) == ((default__.EC__PUBLIC__KEY__FIELD) in ((pat_let_tv2_).encryptionContext)))) and ((((d_0_suite_).signature).is_ECDSA) == (((pat_let_tv3_).verificationKey).is_Some))) and ((not(((d_0_suite_).signature).is_None)) == ((default__.EC__PUBLIC__KEY__FIELD) in ((pat_let_tv4_).encryptionContext)))) and (not (not(((d_0_suite_).symmetricSignature).is_None)) or ((((pat_let_tv5_).plaintextDataKey).is_Some) == (((pat_let_tv6_).symmetricSigningKey).is_Some)))) and (not (((d_0_suite_).symmetricSignature).is_None) or (((pat_let_tv7_).symmetricSigningKey).is_None))) and (_dafny.quantifier(((pat_let_tv8_).requiredEncryptionContextKeys).UniqueElements, True, lambda0_))
            return iife1_(_pat_let3_0)
        return (AlgorithmSuites.default__.AlgorithmSuite_q((decryptionMaterials).algorithmSuite)) and (iife0_((decryptionMaterials).algorithmSuite))

    @staticmethod
    def DecryptionMaterialsAddDataKey(decryptionMaterials, plaintextDataKey, symmetricSigningKey):
        d_0_suite_ = (decryptionMaterials).algorithmSuite
        d_1_valueOrError0_ = Wrappers.default__.Need(default__.ValidDecryptionMaterials(decryptionMaterials), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("Attempt to modify invalid decryption material.")))
        if (d_1_valueOrError0_).IsFailure():
            return (d_1_valueOrError0_).PropagateFailure()
        elif True:
            d_2_valueOrError1_ = Wrappers.default__.Need(((decryptionMaterials).plaintextDataKey).is_None, AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("Attempt to modify plaintextDataKey.")))
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_valueOrError2_ = Wrappers.default__.Need((AlgorithmSuites.default__.GetEncryptKeyLength(d_0_suite_)) == (len(plaintextDataKey)), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("plaintextDataKey does not match Algorithm Suite specification.")))
                if (d_3_valueOrError2_).IsFailure():
                    return (d_3_valueOrError2_).PropagateFailure()
                elif True:
                    d_4_valueOrError3_ = Wrappers.default__.Need(((symmetricSigningKey).is_Some) == (not((((decryptionMaterials).algorithmSuite).symmetricSignature).is_None)), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("symmetric signature key must be added with plaintextDataKey if using an algorithm suite with symmetric signing.")))
                    if (d_4_valueOrError3_).IsFailure():
                        return (d_4_valueOrError3_).PropagateFailure()
                    elif True:
                        d_5_valueOrError4_ = Wrappers.default__.Need(((symmetricSigningKey).is_None) == ((((decryptionMaterials).algorithmSuite).symmetricSignature).is_None), AwsCryptographyMaterialProvidersTypes.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("symmetric signature key cannot be added with plaintextDataKey if using an algorithm suite without symmetric signing.")))
                        if (d_5_valueOrError4_).IsFailure():
                            return (d_5_valueOrError4_).PropagateFailure()
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
        d_0_s_ = _dafny.Seq([97, 119, 115, 45, 99, 114, 121, 112, 116, 111, 45, 112, 117, 98, 108, 105, 99, 45, 107, 101, 121])
        return d_0_s_
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
        d_0_d_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = source__
        return default__.DecryptionMaterialsWithoutPlaintextDataKey(d_0_d_)

class SealedDecryptionMaterials:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return AwsCryptographyMaterialProvidersTypes.DecryptionMaterials.default()()
    def _Is(source__):
        d_1_d_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = source__
        return default__.DecryptionMaterialsWithPlaintextDataKey(d_1_d_)
