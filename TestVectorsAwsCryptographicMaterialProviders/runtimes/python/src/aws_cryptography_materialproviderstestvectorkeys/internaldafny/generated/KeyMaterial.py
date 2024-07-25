import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
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
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import standard_library.internaldafny.generated.Actions as Actions
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import standard_library.internaldafny.generated.UUID as UUID
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.Utils as Utils
import aws_cryptographic_materialproviders.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
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
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.MplManifestOptions as MplManifestOptions
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllAlgorithmSuites as AllAlgorithmSuites
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.WrappedMaterialProviders as WrappedMaterialProviders
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AwsCryptographyMaterialProvidersTestVectorKeysTypes as AwsCryptographyMaterialProvidersTestVectorKeysTypes
import standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import standard_library.internaldafny.generated.JSON_Values as JSON_Values
import standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import standard_library.internaldafny.generated.JSON_ZeroCopy_Serializer as JSON_ZeroCopy_Serializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Core as JSON_ZeroCopy_Deserializer_Core
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Strings as JSON_ZeroCopy_Deserializer_Strings
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Numbers as JSON_ZeroCopy_Deserializer_Numbers
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ObjectParams as JSON_ZeroCopy_Deserializer_ObjectParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Objects as JSON_ZeroCopy_Deserializer_Objects
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ArrayParams as JSON_ZeroCopy_Deserializer_ArrayParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Arrays as JSON_ZeroCopy_Deserializer_Arrays
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Constants as JSON_ZeroCopy_Deserializer_Constants
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Values as JSON_ZeroCopy_Deserializer_Values
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_API as JSON_ZeroCopy_Deserializer_API
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer as JSON_ZeroCopy_Deserializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_API as JSON_ZeroCopy_API
import standard_library.internaldafny.generated.JSON_API as JSON_API
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.JSONHelpers as JSONHelpers
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyDescription as KeyDescription

# Module: KeyMaterial

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BuildKeyMaterials(mpl, obj):
        if (len(obj)) == (0):
            return Wrappers.Result_Success(_dafny.Map({}))
        elif True:
            d_200_name_ = ((obj)[0])[0]
            d_201_valueOrError0_ = default__.ToKeyMaterial(mpl, d_200_name_, ((obj)[0])[1])
            if (d_201_valueOrError0_).IsFailure():
                return (d_201_valueOrError0_).PropagateFailure()
            elif True:
                d_202_keyMaterial_ = (d_201_valueOrError0_).Extract()
                d_203_valueOrError1_ = default__.BuildKeyMaterials(mpl, _dafny.Seq((obj)[1::]))
                if (d_203_valueOrError1_).IsFailure():
                    return (d_203_valueOrError1_).PropagateFailure()
                elif True:
                    d_204_tail_ = (d_203_valueOrError1_).Extract()
                    return Wrappers.Result_Success((_dafny.Map({d_200_name_: d_202_keyMaterial_})) | (d_204_tail_))

    @staticmethod
    def ToKeyMaterial(mpl, name, obj):
        pat_let_tv6_ = mpl
        pat_let_tv7_ = name
        pat_let_tv8_ = mpl
        pat_let_tv9_ = name
        pat_let_tv10_ = name
        pat_let_tv11_ = name
        pat_let_tv12_ = name
        pat_let_tv13_ = name
        pat_let_tv14_ = name
        pat_let_tv15_ = name
        pat_let_tv16_ = name
        pat_let_tv17_ = name
        d_205_valueOrError0_ = Wrappers.default__.Need((obj).is_Object, _dafny.Seq("KeyDescription not an object"))
        if (d_205_valueOrError0_).IsFailure():
            return (d_205_valueOrError0_).PropagateFailure()
        elif True:
            d_206_obj_ = (obj).obj
            d_207_typString_ = _dafny.Seq("type")
            d_208_valueOrError1_ = JSONHelpers.default__.GetString(d_207_typString_, d_206_obj_)
            if (d_208_valueOrError1_).IsFailure():
                return (d_208_valueOrError1_).PropagateFailure()
            elif True:
                d_209_typ_ = (d_208_valueOrError1_).Extract()
                d_210_valueOrError2_ = Wrappers.default__.Need(default__.KeyMaterialString_q(d_209_typ_), (_dafny.Seq("Unsupported KeyMaterial type:")) + (d_209_typ_))
                if (d_210_valueOrError2_).IsFailure():
                    return (d_210_valueOrError2_).PropagateFailure()
                elif True:
                    source6_ = d_209_typ_
                    unmatched6 = True
                    if unmatched6:
                        if (source6_) == (_dafny.Seq("static-material")):
                            unmatched6 = False
                            return default__.ToStaticMaterial(pat_let_tv6_, pat_let_tv7_, d_206_obj_)
                    if unmatched6:
                        if (source6_) == (_dafny.Seq("static-branch-key")):
                            unmatched6 = False
                            return default__.ToStaticBranchKey(pat_let_tv8_, pat_let_tv9_, d_206_obj_)
                    if unmatched6:
                        unmatched6 = False
                        d_211_valueOrError3_ = JSONHelpers.default__.GetBool(_dafny.Seq("encrypt"), d_206_obj_)
                        if (d_211_valueOrError3_).IsFailure():
                            return (d_211_valueOrError3_).PropagateFailure()
                        elif True:
                            d_212_encrypt_ = (d_211_valueOrError3_).Extract()
                            d_213_valueOrError4_ = JSONHelpers.default__.GetBool(_dafny.Seq("decrypt"), d_206_obj_)
                            if (d_213_valueOrError4_).IsFailure():
                                return (d_213_valueOrError4_).PropagateFailure()
                            elif True:
                                d_214_decrypt_ = (d_213_valueOrError4_).Extract()
                                d_215_valueOrError5_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("key-id"), d_206_obj_)
                                if (d_215_valueOrError5_).IsFailure():
                                    return (d_215_valueOrError5_).PropagateFailure()
                                elif True:
                                    d_216_keyIdentifierOption_ = (d_215_valueOrError5_).Extract()
                                    d_217_keyIdentifier_ = (d_216_keyIdentifierOption_).UnwrapOr(pat_let_tv10_)
                                    source7_ = d_209_typ_
                                    unmatched7 = True
                                    if unmatched7:
                                        if (source7_) == (_dafny.Seq("aws-kms")):
                                            unmatched7 = False
                                            return Wrappers.Result_Success(KeyMaterial_KMS(pat_let_tv11_, d_212_encrypt_, d_214_decrypt_, d_217_keyIdentifier_))
                                    if unmatched7:
                                        if (source7_) == (_dafny.Seq("aws-kms-ecdh")):
                                            unmatched7 = False
                                            d_218_valueOrError6_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithm"), d_206_obj_)
                                            if (d_218_valueOrError6_).IsFailure():
                                                return (d_218_valueOrError6_).PropagateFailure()
                                            elif True:
                                                d_219_algorithm_ = (d_218_valueOrError6_).Extract()
                                                d_220_valueOrError7_ = JSONHelpers.default__.GetString(_dafny.Seq("sender-material"), d_206_obj_)
                                                if (d_220_valueOrError7_).IsFailure():
                                                    return (d_220_valueOrError7_).PropagateFailure()
                                                elif True:
                                                    d_221_senderMaterial_ = (d_220_valueOrError7_).Extract()
                                                    d_222_valueOrError8_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient-material"), d_206_obj_)
                                                    if (d_222_valueOrError8_).IsFailure():
                                                        return (d_222_valueOrError8_).PropagateFailure()
                                                    elif True:
                                                        d_223_recipientMaterial_ = (d_222_valueOrError8_).Extract()
                                                        d_224_valueOrError9_ = JSONHelpers.default__.GetString(_dafny.Seq("encoding"), d_206_obj_)
                                                        if (d_224_valueOrError9_).IsFailure():
                                                            return (d_224_valueOrError9_).PropagateFailure()
                                                        elif True:
                                                            d_225_encoding_ = (d_224_valueOrError9_).Extract()
                                                            d_226_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("sender-material-public-key"), d_206_obj_)
                                                            if (d_226_valueOrError10_).IsFailure():
                                                                return (d_226_valueOrError10_).PropagateFailure()
                                                            elif True:
                                                                d_227_senderPublicKey_ = (d_226_valueOrError10_).Extract()
                                                                d_228_valueOrError11_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient-material-public-key"), d_206_obj_)
                                                                if (d_228_valueOrError11_).IsFailure():
                                                                    return (d_228_valueOrError11_).PropagateFailure()
                                                                elif True:
                                                                    d_229_recipientPublicKey_ = (d_228_valueOrError11_).Extract()
                                                                    return Wrappers.Result_Success(KeyMaterial_KMSEcdh(pat_let_tv12_, d_212_encrypt_, d_214_decrypt_, d_217_keyIdentifier_, d_219_algorithm_, d_221_senderMaterial_, d_223_recipientMaterial_, d_227_senderPublicKey_, d_229_recipientPublicKey_))
                                    if unmatched7:
                                        if (source7_) == (_dafny.Seq("ecc-private")):
                                            unmatched7 = False
                                            d_230_valueOrError12_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithm"), d_206_obj_)
                                            if (d_230_valueOrError12_).IsFailure():
                                                return (d_230_valueOrError12_).PropagateFailure()
                                            elif True:
                                                d_231_algorithm_ = (d_230_valueOrError12_).Extract()
                                                d_232_valueOrError13_ = JSONHelpers.default__.GetNat(_dafny.Seq("bits"), d_206_obj_)
                                                if (d_232_valueOrError13_).IsFailure():
                                                    return (d_232_valueOrError13_).PropagateFailure()
                                                elif True:
                                                    d_233_bits_ = (d_232_valueOrError13_).Extract()
                                                    d_234_valueOrError14_ = JSONHelpers.default__.GetString(_dafny.Seq("encoding"), d_206_obj_)
                                                    if (d_234_valueOrError14_).IsFailure():
                                                        return (d_234_valueOrError14_).PropagateFailure()
                                                    elif True:
                                                        d_235_encoding_ = (d_234_valueOrError14_).Extract()
                                                        d_236_valueOrError15_ = JSONHelpers.default__.GetString(_dafny.Seq("sender-material"), d_206_obj_)
                                                        if (d_236_valueOrError15_).IsFailure():
                                                            return (d_236_valueOrError15_).PropagateFailure()
                                                        elif True:
                                                            d_237_senderMaterial_ = (d_236_valueOrError15_).Extract()
                                                            d_238_valueOrError16_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient-material"), d_206_obj_)
                                                            if (d_238_valueOrError16_).IsFailure():
                                                                return (d_238_valueOrError16_).PropagateFailure()
                                                            elif True:
                                                                d_239_recipientMaterial_ = (d_238_valueOrError16_).Extract()
                                                                d_240_valueOrError17_ = JSONHelpers.default__.GetString(_dafny.Seq("sender-material-public-key"), d_206_obj_)
                                                                if (d_240_valueOrError17_).IsFailure():
                                                                    return (d_240_valueOrError17_).PropagateFailure()
                                                                elif True:
                                                                    d_241_senderPublicKey_ = (d_240_valueOrError17_).Extract()
                                                                    d_242_valueOrError18_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient-material-public-key"), d_206_obj_)
                                                                    if (d_242_valueOrError18_).IsFailure():
                                                                        return (d_242_valueOrError18_).PropagateFailure()
                                                                    elif True:
                                                                        d_243_recipientPublicKey_ = (d_242_valueOrError18_).Extract()
                                                                        return Wrappers.Result_Success(KeyMaterial_PrivateECDH(pat_let_tv13_, d_212_encrypt_, d_214_decrypt_, d_231_algorithm_, d_233_bits_, d_235_encoding_, d_237_senderMaterial_, d_239_recipientMaterial_, d_241_senderPublicKey_, d_243_recipientPublicKey_, d_217_keyIdentifier_))
                                    if unmatched7:
                                        unmatched7 = False
                                        d_244_valueOrError19_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithm"), d_206_obj_)
                                        if (d_244_valueOrError19_).IsFailure():
                                            return (d_244_valueOrError19_).PropagateFailure()
                                        elif True:
                                            d_245_algorithm_ = (d_244_valueOrError19_).Extract()
                                            d_246_valueOrError20_ = JSONHelpers.default__.GetNat(_dafny.Seq("bits"), d_206_obj_)
                                            if (d_246_valueOrError20_).IsFailure():
                                                return (d_246_valueOrError20_).PropagateFailure()
                                            elif True:
                                                d_247_bits_ = (d_246_valueOrError20_).Extract()
                                                d_248_valueOrError21_ = JSONHelpers.default__.GetString(_dafny.Seq("encoding"), d_206_obj_)
                                                if (d_248_valueOrError21_).IsFailure():
                                                    return (d_248_valueOrError21_).PropagateFailure()
                                                elif True:
                                                    d_249_encoding_ = (d_248_valueOrError21_).Extract()
                                                    d_250_valueOrError22_ = JSONHelpers.default__.Get(_dafny.Seq("material"), d_206_obj_)
                                                    if (d_250_valueOrError22_).IsFailure():
                                                        return (d_250_valueOrError22_).PropagateFailure()
                                                    elif True:
                                                        d_251_material_q_ = (d_250_valueOrError22_).Extract()
                                                        def lambda14_():
                                                            source8_ = d_251_material_q_
                                                            unmatched8 = True
                                                            if unmatched8:
                                                                if source8_.is_String:
                                                                    d_253_str_ = source8_.str
                                                                    unmatched8 = False
                                                                    return Wrappers.Result_Success(d_253_str_)
                                                            if unmatched8:
                                                                if source8_.is_Array:
                                                                    d_254_arr_ = source8_.arr
                                                                    unmatched8 = False
                                                                    def lambda15_(forall_var_10_):
                                                                        d_256_s_: JSON_Values.JSON = forall_var_10_
                                                                        return not ((d_256_s_) in (d_254_arr_)) or ((d_256_s_).is_String)

                                                                    d_255_valueOrError24_ = Wrappers.default__.Need(((0) < (len(d_254_arr_))) and (_dafny.quantifier((d_254_arr_).UniqueElements, True, lambda15_)), _dafny.Seq("Unsupported material shape."))
                                                                    if (d_255_valueOrError24_).IsFailure():
                                                                        return (d_255_valueOrError24_).PropagateFailure()
                                                                    elif True:
                                                                        def lambda16_(d_258_s_):
                                                                            return (d_258_s_).str

                                                                        d_257_strings_ = Seq.default__.Map(lambda16_, d_254_arr_)
                                                                        d_259_material_ = StandardLibrary.default__.Join(d_257_strings_, _dafny.Seq("\n"))
                                                                        return Wrappers.Result_Success(d_259_material_)
                                                            if unmatched8:
                                                                unmatched8 = False
                                                                return Wrappers.Result_Failure(_dafny.Seq("Unsupported material shape."))
                                                            raise Exception("unexpected control point")

                                                        d_252_valueOrError23_ = lambda14_()
                                                        if (d_252_valueOrError23_).IsFailure():
                                                            return (d_252_valueOrError23_).PropagateFailure()
                                                        elif True:
                                                            d_260_material_ = (d_252_valueOrError23_).Extract()
                                                            source9_ = d_209_typ_
                                                            unmatched9 = True
                                                            if unmatched9:
                                                                if (source9_) == (_dafny.Seq("symmetric")):
                                                                    unmatched9 = False
                                                                    d_261_valueOrError25_ = Base64.default__.Decode(d_260_material_)
                                                                    if (d_261_valueOrError25_).IsFailure():
                                                                        return (d_261_valueOrError25_).PropagateFailure()
                                                                    elif True:
                                                                        d_262_materialBytes_ = (d_261_valueOrError25_).Extract()
                                                                        return Wrappers.Result_Success(KeyMaterial_Symetric(pat_let_tv14_, d_212_encrypt_, d_214_decrypt_, d_245_algorithm_, d_247_bits_, d_249_encoding_, d_262_materialBytes_, d_217_keyIdentifier_))
                                                            if unmatched9:
                                                                if (source9_) == (_dafny.Seq("private")):
                                                                    unmatched9 = False
                                                                    return Wrappers.Result_Success(KeyMaterial_PrivateRSA(pat_let_tv15_, d_212_encrypt_, d_214_decrypt_, d_245_algorithm_, d_247_bits_, d_249_encoding_, d_260_material_, d_217_keyIdentifier_))
                                                            if unmatched9:
                                                                if (source9_) == (_dafny.Seq("public")):
                                                                    unmatched9 = False
                                                                    return Wrappers.Result_Success(KeyMaterial_PublicRSA(pat_let_tv16_, d_212_encrypt_, d_214_decrypt_, d_247_bits_, d_245_algorithm_, d_249_encoding_, d_260_material_, d_217_keyIdentifier_))
                                                            if unmatched9:
                                                                if (source9_) == (_dafny.Seq("aws-kms-rsa")):
                                                                    unmatched9 = False
                                                                    d_263_valueOrError26_ = UTF8.default__.Encode(d_260_material_)
                                                                    if (d_263_valueOrError26_).IsFailure():
                                                                        return (d_263_valueOrError26_).PropagateFailure()
                                                                    elif True:
                                                                        d_264_publicKey_ = (d_263_valueOrError26_).Extract()
                                                                        return Wrappers.Result_Success(KeyMaterial_KMSAsymetric(pat_let_tv17_, d_212_encrypt_, d_214_decrypt_, d_217_keyIdentifier_, d_247_bits_, d_245_algorithm_, d_249_encoding_, d_264_publicKey_))
                                                            raise Exception("unexpected control point")
                                    raise Exception("unexpected control point")
                    raise Exception("unexpected control point")

    @staticmethod
    def ToStaticMaterial(mpl, name, obj):
        d_265_valueOrError0_ = default__.GetAlgorithmSuiteInfo(mpl, obj)
        if (d_265_valueOrError0_).IsFailure():
            return (d_265_valueOrError0_).PropagateFailure()
        elif True:
            d_266_algorithmSuite_ = (d_265_valueOrError0_).Extract()
            d_267_valueOrError1_ = JSONHelpers.default__.SmallObjectToStringStringMap(_dafny.Seq("encryptionContext"), obj)
            if (d_267_valueOrError1_).IsFailure():
                return (d_267_valueOrError1_).PropagateFailure()
            elif True:
                d_268_encryptionContextStrings_ = (d_267_valueOrError1_).Extract()
                d_269_valueOrError2_ = JSONHelpers.default__.utf8EncodeMap(d_268_encryptionContextStrings_)
                if (d_269_valueOrError2_).IsFailure():
                    return (d_269_valueOrError2_).PropagateFailure()
                elif True:
                    d_270_encryptionContext_ = (d_269_valueOrError2_).Extract()
                    d_271_valueOrError3_ = JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), obj)
                    if (d_271_valueOrError3_).IsFailure():
                        return (d_271_valueOrError3_).PropagateFailure()
                    elif True:
                        d_272_keysAsStrings_ = (d_271_valueOrError3_).Extract()
                        d_273_valueOrError4_ = JSONHelpers.default__.utf8EncodeSeq(d_272_keysAsStrings_)
                        if (d_273_valueOrError4_).IsFailure():
                            return (d_273_valueOrError4_).PropagateFailure()
                        elif True:
                            d_274_requiredEncryptionContextKeys_ = (d_273_valueOrError4_).Extract()
                            d_275_valueOrError5_ = JSONHelpers.default__.GetArrayObject(_dafny.Seq("encryptedDataKeys"), obj)
                            if (d_275_valueOrError5_).IsFailure():
                                return (d_275_valueOrError5_).PropagateFailure()
                            elif True:
                                d_276_encryptedDataKeysJSON_ = (d_275_valueOrError5_).Extract()
                                d_277_valueOrError6_ = Seq.default__.MapWithResult(default__.ToEncryptedDataKey, d_276_encryptedDataKeysJSON_)
                                if (d_277_valueOrError6_).IsFailure():
                                    return (d_277_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_278_encryptedDataKeys_ = (d_277_valueOrError6_).Extract()
                                    d_279_valueOrError7_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("plaintextDataKey"), obj)
                                    if (d_279_valueOrError7_).IsFailure():
                                        return (d_279_valueOrError7_).PropagateFailure()
                                    elif True:
                                        d_280_plaintextDataKeyEncoded_ = (d_279_valueOrError7_).Extract()
                                        def iife18_(_pat_let6_0):
                                            def iife19_(d_282_result_):
                                                return (Wrappers.Result_Success(Wrappers.Option_Some((d_282_result_).value)) if (d_282_result_).is_Success else Wrappers.Result_Failure((d_282_result_).error))
                                            return iife19_(_pat_let6_0)
                                        d_281_valueOrError8_ = (iife18_(Base64.default__.Decode((d_280_plaintextDataKeyEncoded_).value)) if (d_280_plaintextDataKeyEncoded_).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                                        if (d_281_valueOrError8_).IsFailure():
                                            return (d_281_valueOrError8_).PropagateFailure()
                                        elif True:
                                            d_283_plaintextDataKey_ = (d_281_valueOrError8_).Extract()
                                            d_284_valueOrError9_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("signingKey"), obj)
                                            if (d_284_valueOrError9_).IsFailure():
                                                return (d_284_valueOrError9_).PropagateFailure()
                                            elif True:
                                                d_285_signingKey_ = (d_284_valueOrError9_).Extract()
                                                d_286_valueOrError10_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("verificationKey"), obj)
                                                if (d_286_valueOrError10_).IsFailure():
                                                    return (d_286_valueOrError10_).PropagateFailure()
                                                elif True:
                                                    d_287_verificationKey_ = (d_286_valueOrError10_).Extract()
                                                    d_288_symmetricSigningKeys_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("symmetricSigningKeys"), obj)).ToOption()
                                                    return Wrappers.Result_Success(KeyMaterial_StaticMaterial(name, d_266_algorithmSuite_, d_270_encryptionContext_, d_278_encryptedDataKeys_, d_274_requiredEncryptionContextKeys_, d_283_plaintextDataKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))

    @staticmethod
    def ToStaticBranchKey(mpl, name, obj):
        d_289_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("key-id"), obj)
        if (d_289_valueOrError0_).IsFailure():
            return (d_289_valueOrError0_).PropagateFailure()
        elif True:
            d_290_keyIdentifier_ = (d_289_valueOrError0_).Extract()
            d_291_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("branchKeyVersion"), obj)
            if (d_291_valueOrError1_).IsFailure():
                return (d_291_valueOrError1_).PropagateFailure()
            elif True:
                d_292_branchKeyVersionEncoded_ = (d_291_valueOrError1_).Extract()
                d_293_valueOrError2_ = UTF8.default__.Encode(d_292_branchKeyVersionEncoded_)
                if (d_293_valueOrError2_).IsFailure():
                    return (d_293_valueOrError2_).PropagateFailure()
                elif True:
                    d_294_branchKeyVersion_ = (d_293_valueOrError2_).Extract()
                    d_295_valueOrError3_ = JSONHelpers.default__.GetString(_dafny.Seq("branchKey"), obj)
                    if (d_295_valueOrError3_).IsFailure():
                        return (d_295_valueOrError3_).PropagateFailure()
                    elif True:
                        d_296_branchKeyEncoded_ = (d_295_valueOrError3_).Extract()
                        d_297_valueOrError4_ = Base64.default__.Decode(d_296_branchKeyEncoded_)
                        if (d_297_valueOrError4_).IsFailure():
                            return (d_297_valueOrError4_).PropagateFailure()
                        elif True:
                            d_298_branchKey_ = (d_297_valueOrError4_).Extract()
                            d_299_valueOrError5_ = JSONHelpers.default__.GetString(_dafny.Seq("beaconKey"), obj)
                            if (d_299_valueOrError5_).IsFailure():
                                return (d_299_valueOrError5_).PropagateFailure()
                            elif True:
                                d_300_beaconKeyEncoded_ = (d_299_valueOrError5_).Extract()
                                d_301_valueOrError6_ = Base64.default__.Decode(d_300_beaconKeyEncoded_)
                                if (d_301_valueOrError6_).IsFailure():
                                    return (d_301_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_302_beaconKey_ = (d_301_valueOrError6_).Extract()
                                    return Wrappers.Result_Success(KeyMaterial_StaticKeyStoreInformation(d_290_keyIdentifier_, d_294_branchKeyVersion_, d_298_branchKey_, d_302_beaconKey_))

    @staticmethod
    def ToEncryptedDataKey(obj):
        d_303_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderId"), obj)
        if (d_303_valueOrError0_).IsFailure():
            return (d_303_valueOrError0_).PropagateFailure()
        elif True:
            d_304_keyProviderIdJSON_ = (d_303_valueOrError0_).Extract()
            d_305_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderInfo"), obj)
            if (d_305_valueOrError1_).IsFailure():
                return (d_305_valueOrError1_).PropagateFailure()
            elif True:
                d_306_keyProviderInfoJSON_ = (d_305_valueOrError1_).Extract()
                d_307_valueOrError2_ = JSONHelpers.default__.GetString(_dafny.Seq("ciphertext"), obj)
                if (d_307_valueOrError2_).IsFailure():
                    return (d_307_valueOrError2_).PropagateFailure()
                elif True:
                    d_308_ciphertextJSON_ = (d_307_valueOrError2_).Extract()
                    d_309_valueOrError3_ = UTF8.default__.Encode(d_304_keyProviderIdJSON_)
                    if (d_309_valueOrError3_).IsFailure():
                        return (d_309_valueOrError3_).PropagateFailure()
                    elif True:
                        d_310_keyProviderId_ = (d_309_valueOrError3_).Extract()
                        d_311_valueOrError4_ = Base64.default__.Decode(d_306_keyProviderInfoJSON_)
                        if (d_311_valueOrError4_).IsFailure():
                            return (d_311_valueOrError4_).PropagateFailure()
                        elif True:
                            d_312_keyProviderInfo_ = (d_311_valueOrError4_).Extract()
                            d_313_valueOrError5_ = Base64.default__.Decode(d_308_ciphertextJSON_)
                            if (d_313_valueOrError5_).IsFailure():
                                return (d_313_valueOrError5_).PropagateFailure()
                            elif True:
                                d_314_ciphertext_ = (d_313_valueOrError5_).Extract()
                                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(d_310_keyProviderId_, d_312_keyProviderInfo_, d_314_ciphertext_))

    @staticmethod
    def GetAlgorithmSuiteInfo(mpl, obj):
        d_315_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithmSuiteId"), obj)
        if (d_315_valueOrError0_).IsFailure():
            return (d_315_valueOrError0_).PropagateFailure()
        elif True:
            d_316_algorithmSuiteHex_ = (d_315_valueOrError0_).Extract()
            d_317_valueOrError1_ = Wrappers.default__.Need(HexStrings.default__.IsLooseHexString(d_316_algorithmSuiteHex_), _dafny.Seq("Not hex encoded binary"))
            if (d_317_valueOrError1_).IsFailure():
                return (d_317_valueOrError1_).PropagateFailure()
            elif True:
                d_318_binaryId_ = HexStrings.default__.FromHexString(d_316_algorithmSuiteHex_)
                def lambda17_(d_319_algorithmSuiteHex_):
                    def lambda18_(d_320_e_):
                        return (_dafny.Seq("Invalid Suite:")) + (d_319_algorithmSuiteHex_)

                    return lambda18_

                return ((mpl).GetAlgorithmSuiteInfo(d_318_binaryId_)).MapFailure(lambda17_(d_316_algorithmSuiteHex_))

    @staticmethod
    def KeyMaterialString_q(s):
        return (((((((((s) == (_dafny.Seq("static-material"))) or ((s) == (_dafny.Seq("aws-kms")))) or ((s) == (_dafny.Seq("symmetric")))) or ((s) == (_dafny.Seq("private")))) or ((s) == (_dafny.Seq("public")))) or ((s) == (_dafny.Seq("static-branch-key")))) or ((s) == (_dafny.Seq("aws-kms-rsa")))) or ((s) == (_dafny.Seq("ecc-private")))) or ((s) == (_dafny.Seq("aws-kms-ecdh")))


class KeyMaterial:
    @classmethod
    def default(cls, ):
        return lambda: KeyMaterial_Symetric(_dafny.Seq(""), False, False, _dafny.Seq(""), int(0), _dafny.Seq(""), _dafny.Seq({}), _dafny.Seq(""))
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
    def is_PrivateECDH(self) -> bool:
        return isinstance(self, KeyMaterial_PrivateECDH)
    @property
    def is_KMS(self) -> bool:
        return isinstance(self, KeyMaterial_KMS)
    @property
    def is_KMSAsymetric(self) -> bool:
        return isinstance(self, KeyMaterial_KMSAsymetric)
    @property
    def is_KMSEcdh(self) -> bool:
        return isinstance(self, KeyMaterial_KMSEcdh)
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

class KeyMaterial_PrivateECDH(KeyMaterial, NamedTuple('PrivateECDH', [('name', Any), ('encrypt', Any), ('decrypt', Any), ('algorithm', Any), ('bits', Any), ('encoding', Any), ('senderMaterial', Any), ('recipientMaterial', Any), ('senderPublicKey', Any), ('recipientPublicKey', Any), ('keyIdentifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.PrivateECDH({_dafny.string_of(self.name)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.decrypt)}, {_dafny.string_of(self.algorithm)}, {_dafny.string_of(self.bits)}, {_dafny.string_of(self.encoding)}, {_dafny.string_of(self.senderMaterial)}, {_dafny.string_of(self.recipientMaterial)}, {_dafny.string_of(self.senderPublicKey)}, {_dafny.string_of(self.recipientPublicKey)}, {_dafny.string_of(self.keyIdentifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_PrivateECDH) and self.name == __o.name and self.encrypt == __o.encrypt and self.decrypt == __o.decrypt and self.algorithm == __o.algorithm and self.bits == __o.bits and self.encoding == __o.encoding and self.senderMaterial == __o.senderMaterial and self.recipientMaterial == __o.recipientMaterial and self.senderPublicKey == __o.senderPublicKey and self.recipientPublicKey == __o.recipientPublicKey and self.keyIdentifier == __o.keyIdentifier
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

class KeyMaterial_KMSEcdh(KeyMaterial, NamedTuple('KMSEcdh', [('name', Any), ('encrypt', Any), ('decrypt', Any), ('keyIdentifier', Any), ('algorithm', Any), ('senderMaterial', Any), ('recipientMaterial', Any), ('senderPublicKey', Any), ('recipientPublicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyMaterial.KeyMaterial.KMSEcdh({_dafny.string_of(self.name)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.decrypt)}, {_dafny.string_of(self.keyIdentifier)}, {_dafny.string_of(self.algorithm)}, {_dafny.string_of(self.senderMaterial)}, {_dafny.string_of(self.recipientMaterial)}, {_dafny.string_of(self.senderPublicKey)}, {_dafny.string_of(self.recipientPublicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyMaterial_KMSEcdh) and self.name == __o.name and self.encrypt == __o.encrypt and self.decrypt == __o.decrypt and self.keyIdentifier == __o.keyIdentifier and self.algorithm == __o.algorithm and self.senderMaterial == __o.senderMaterial and self.recipientMaterial == __o.recipientMaterial and self.senderPublicKey == __o.senderPublicKey and self.recipientPublicKey == __o.recipientPublicKey
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

