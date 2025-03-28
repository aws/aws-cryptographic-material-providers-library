import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.module_ as module_
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
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_material_providers.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_material_providers.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_material_providers.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_material_providers.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_material_providers.internaldafny.generated.CacheConstants as CacheConstants
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_material_providers.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_material_providers.internaldafny.generated.CMM as CMM
import aws_cryptographic_material_providers.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_material_providers.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_material_providers.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_material_providers.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_material_providers.internaldafny.generated.Utils as Utils
import aws_cryptographic_material_providers.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_material_providers.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_material_providers.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
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
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.MplManifestOptions as MplManifestOptions
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllAlgorithmSuites as AllAlgorithmSuites
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.WrappedMaterialProviders as WrappedMaterialProviders
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AwsCryptographyMaterialProvidersTestVectorKeysTypes as AwsCryptographyMaterialProvidersTestVectorKeysTypes
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Values as JSON_Values
import smithy_dafny_standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import smithy_dafny_standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import smithy_dafny_standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import smithy_dafny_standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Serializer as JSON_ZeroCopy_Serializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Core as JSON_ZeroCopy_Deserializer_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Strings as JSON_ZeroCopy_Deserializer_Strings
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Numbers as JSON_ZeroCopy_Deserializer_Numbers
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ObjectParams as JSON_ZeroCopy_Deserializer_ObjectParams
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Objects as JSON_ZeroCopy_Deserializer_Objects
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ArrayParams as JSON_ZeroCopy_Deserializer_ArrayParams
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Arrays as JSON_ZeroCopy_Deserializer_Arrays
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Constants as JSON_ZeroCopy_Deserializer_Constants
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Values as JSON_ZeroCopy_Deserializer_Values
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_API as JSON_ZeroCopy_Deserializer_API
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer as JSON_ZeroCopy_Deserializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_API as JSON_ZeroCopy_API
import smithy_dafny_standard_library.internaldafny.generated.JSON_API as JSON_API
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.JSONHelpers as JSONHelpers
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.KeyDescription as KeyDescription

# Module: KeyMaterial

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BuildKeyMaterials(mpl, obj):
        if (len(obj)) == (0):
            return Wrappers.Result_Success(_dafny.Map({}))
        elif True:
            d_0_name_ = ((obj)[0])[0]
            d_1_valueOrError0_ = default__.ToKeyMaterial(mpl, d_0_name_, ((obj)[0])[1])
            if (d_1_valueOrError0_).IsFailure():
                return (d_1_valueOrError0_).PropagateFailure()
            elif True:
                d_2_keyMaterial_ = (d_1_valueOrError0_).Extract()
                d_3_valueOrError1_ = default__.BuildKeyMaterials(mpl, _dafny.Seq((obj)[1::]))
                if (d_3_valueOrError1_).IsFailure():
                    return (d_3_valueOrError1_).PropagateFailure()
                elif True:
                    d_4_tail_ = (d_3_valueOrError1_).Extract()
                    return Wrappers.Result_Success((_dafny.Map({d_0_name_: d_2_keyMaterial_})) | (d_4_tail_))

    @staticmethod
    def ToKeyMaterial(mpl, name, obj):
        d_0_valueOrError0_ = Wrappers.default__.Need((obj).is_Object, _dafny.Seq("KeyDescription not an object"))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_obj_ = (obj).obj
            d_2_typString_ = _dafny.Seq("type")
            d_3_valueOrError1_ = JSONHelpers.default__.GetString(d_2_typString_, d_1_obj_)
            if (d_3_valueOrError1_).IsFailure():
                return (d_3_valueOrError1_).PropagateFailure()
            elif True:
                d_4_typ_ = (d_3_valueOrError1_).Extract()
                d_5_valueOrError2_ = Wrappers.default__.Need(default__.KeyMaterialString_q(d_4_typ_), (_dafny.Seq("Unsupported KeyMaterial type:")) + (d_4_typ_))
                if (d_5_valueOrError2_).IsFailure():
                    return (d_5_valueOrError2_).PropagateFailure()
                elif True:
                    source0_ = d_4_typ_
                    if True:
                        if (source0_) == (_dafny.Seq("static-material")):
                            return default__.ToStaticMaterial(mpl, name, d_1_obj_)
                    if True:
                        if (source0_) == (_dafny.Seq("static-branch-key")):
                            return default__.ToStaticBranchKey(mpl, name, d_1_obj_)
                    if True:
                        d_6_valueOrError3_ = JSONHelpers.default__.GetBool(_dafny.Seq("encrypt"), d_1_obj_)
                        if (d_6_valueOrError3_).IsFailure():
                            return (d_6_valueOrError3_).PropagateFailure()
                        elif True:
                            d_7_encrypt_ = (d_6_valueOrError3_).Extract()
                            d_8_valueOrError4_ = JSONHelpers.default__.GetBool(_dafny.Seq("decrypt"), d_1_obj_)
                            if (d_8_valueOrError4_).IsFailure():
                                return (d_8_valueOrError4_).PropagateFailure()
                            elif True:
                                d_9_decrypt_ = (d_8_valueOrError4_).Extract()
                                d_10_valueOrError5_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("key-id"), d_1_obj_)
                                if (d_10_valueOrError5_).IsFailure():
                                    return (d_10_valueOrError5_).PropagateFailure()
                                elif True:
                                    d_11_keyIdentifierOption_ = (d_10_valueOrError5_).Extract()
                                    d_12_keyIdentifier_ = (d_11_keyIdentifierOption_).UnwrapOr(name)
                                    source1_ = d_4_typ_
                                    if True:
                                        if (source1_) == (_dafny.Seq("aws-kms")):
                                            return Wrappers.Result_Success(KeyMaterial_KMS(name, d_7_encrypt_, d_9_decrypt_, d_12_keyIdentifier_))
                                    if True:
                                        if (source1_) == (_dafny.Seq("aws-kms-ecdh")):
                                            d_13_valueOrError6_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithm"), d_1_obj_)
                                            if (d_13_valueOrError6_).IsFailure():
                                                return (d_13_valueOrError6_).PropagateFailure()
                                            elif True:
                                                d_14_algorithm_ = (d_13_valueOrError6_).Extract()
                                                d_15_valueOrError7_ = JSONHelpers.default__.GetString(_dafny.Seq("sender-material"), d_1_obj_)
                                                if (d_15_valueOrError7_).IsFailure():
                                                    return (d_15_valueOrError7_).PropagateFailure()
                                                elif True:
                                                    d_16_senderMaterial_ = (d_15_valueOrError7_).Extract()
                                                    d_17_valueOrError8_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient-material"), d_1_obj_)
                                                    if (d_17_valueOrError8_).IsFailure():
                                                        return (d_17_valueOrError8_).PropagateFailure()
                                                    elif True:
                                                        d_18_recipientMaterial_ = (d_17_valueOrError8_).Extract()
                                                        d_19_valueOrError9_ = JSONHelpers.default__.GetString(_dafny.Seq("encoding"), d_1_obj_)
                                                        if (d_19_valueOrError9_).IsFailure():
                                                            return (d_19_valueOrError9_).PropagateFailure()
                                                        elif True:
                                                            d_20_encoding_ = (d_19_valueOrError9_).Extract()
                                                            d_21_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("sender-material-public-key"), d_1_obj_)
                                                            if (d_21_valueOrError10_).IsFailure():
                                                                return (d_21_valueOrError10_).PropagateFailure()
                                                            elif True:
                                                                d_22_senderPublicKey_ = (d_21_valueOrError10_).Extract()
                                                                d_23_valueOrError11_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient-material-public-key"), d_1_obj_)
                                                                if (d_23_valueOrError11_).IsFailure():
                                                                    return (d_23_valueOrError11_).PropagateFailure()
                                                                elif True:
                                                                    d_24_recipientPublicKey_ = (d_23_valueOrError11_).Extract()
                                                                    return Wrappers.Result_Success(KeyMaterial_KMSEcdh(name, d_7_encrypt_, d_9_decrypt_, d_12_keyIdentifier_, d_14_algorithm_, d_16_senderMaterial_, d_18_recipientMaterial_, d_22_senderPublicKey_, d_24_recipientPublicKey_))
                                    if True:
                                        if (source1_) == (_dafny.Seq("ecc-private")):
                                            d_25_valueOrError12_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithm"), d_1_obj_)
                                            if (d_25_valueOrError12_).IsFailure():
                                                return (d_25_valueOrError12_).PropagateFailure()
                                            elif True:
                                                d_26_algorithm_ = (d_25_valueOrError12_).Extract()
                                                d_27_valueOrError13_ = JSONHelpers.default__.GetNat(_dafny.Seq("bits"), d_1_obj_)
                                                if (d_27_valueOrError13_).IsFailure():
                                                    return (d_27_valueOrError13_).PropagateFailure()
                                                elif True:
                                                    d_28_bits_ = (d_27_valueOrError13_).Extract()
                                                    d_29_valueOrError14_ = JSONHelpers.default__.GetString(_dafny.Seq("encoding"), d_1_obj_)
                                                    if (d_29_valueOrError14_).IsFailure():
                                                        return (d_29_valueOrError14_).PropagateFailure()
                                                    elif True:
                                                        d_30_encoding_ = (d_29_valueOrError14_).Extract()
                                                        d_31_valueOrError15_ = JSONHelpers.default__.GetString(_dafny.Seq("sender-material"), d_1_obj_)
                                                        if (d_31_valueOrError15_).IsFailure():
                                                            return (d_31_valueOrError15_).PropagateFailure()
                                                        elif True:
                                                            d_32_senderMaterial_ = (d_31_valueOrError15_).Extract()
                                                            d_33_valueOrError16_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient-material"), d_1_obj_)
                                                            if (d_33_valueOrError16_).IsFailure():
                                                                return (d_33_valueOrError16_).PropagateFailure()
                                                            elif True:
                                                                d_34_recipientMaterial_ = (d_33_valueOrError16_).Extract()
                                                                d_35_valueOrError17_ = JSONHelpers.default__.GetString(_dafny.Seq("sender-material-public-key"), d_1_obj_)
                                                                if (d_35_valueOrError17_).IsFailure():
                                                                    return (d_35_valueOrError17_).PropagateFailure()
                                                                elif True:
                                                                    d_36_senderPublicKey_ = (d_35_valueOrError17_).Extract()
                                                                    d_37_valueOrError18_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient-material-public-key"), d_1_obj_)
                                                                    if (d_37_valueOrError18_).IsFailure():
                                                                        return (d_37_valueOrError18_).PropagateFailure()
                                                                    elif True:
                                                                        d_38_recipientPublicKey_ = (d_37_valueOrError18_).Extract()
                                                                        return Wrappers.Result_Success(KeyMaterial_PrivateECDH(name, d_7_encrypt_, d_9_decrypt_, d_26_algorithm_, d_28_bits_, d_30_encoding_, d_32_senderMaterial_, d_34_recipientMaterial_, d_36_senderPublicKey_, d_38_recipientPublicKey_, d_12_keyIdentifier_))
                                    if True:
                                        d_39_valueOrError19_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithm"), d_1_obj_)
                                        if (d_39_valueOrError19_).IsFailure():
                                            return (d_39_valueOrError19_).PropagateFailure()
                                        elif True:
                                            d_40_algorithm_ = (d_39_valueOrError19_).Extract()
                                            d_41_valueOrError20_ = JSONHelpers.default__.GetNat(_dafny.Seq("bits"), d_1_obj_)
                                            if (d_41_valueOrError20_).IsFailure():
                                                return (d_41_valueOrError20_).PropagateFailure()
                                            elif True:
                                                d_42_bits_ = (d_41_valueOrError20_).Extract()
                                                d_43_valueOrError21_ = JSONHelpers.default__.GetString(_dafny.Seq("encoding"), d_1_obj_)
                                                if (d_43_valueOrError21_).IsFailure():
                                                    return (d_43_valueOrError21_).PropagateFailure()
                                                elif True:
                                                    d_44_encoding_ = (d_43_valueOrError21_).Extract()
                                                    d_45_valueOrError22_ = JSONHelpers.default__.Get(_dafny.Seq("material"), d_1_obj_)
                                                    if (d_45_valueOrError22_).IsFailure():
                                                        return (d_45_valueOrError22_).PropagateFailure()
                                                    elif True:
                                                        d_46_material_q_ = (d_45_valueOrError22_).Extract()
                                                        def lambda0_():
                                                            source2_ = d_46_material_q_
                                                            if True:
                                                                if source2_.is_String:
                                                                    d_48_str_ = source2_.str
                                                                    return Wrappers.Result_Success(d_48_str_)
                                                            if True:
                                                                if source2_.is_Array:
                                                                    d_49_arr_ = source2_.arr
                                                                    def lambda1_(forall_var_0_):
                                                                        d_51_s_: JSON_Values.JSON = forall_var_0_
                                                                        return not ((d_51_s_) in (d_49_arr_)) or ((d_51_s_).is_String)

                                                                    d_50_valueOrError24_ = Wrappers.default__.Need(((0) < (len(d_49_arr_))) and (_dafny.quantifier((d_49_arr_).UniqueElements, True, lambda1_)), _dafny.Seq("Unsupported material shape."))
                                                                    if (d_50_valueOrError24_).IsFailure():
                                                                        return (d_50_valueOrError24_).PropagateFailure()
                                                                    elif True:
                                                                        def lambda2_(d_53_s_):
                                                                            return (d_53_s_).str

                                                                        d_52_strings_ = Seq.default__.Map(lambda2_, d_49_arr_)
                                                                        d_54_material_ = StandardLibrary.default__.Join(d_52_strings_, _dafny.Seq("\n"))
                                                                        return Wrappers.Result_Success(d_54_material_)
                                                            if True:
                                                                return Wrappers.Result_Failure(_dafny.Seq("Unsupported material shape."))

                                                        d_47_valueOrError23_ = lambda0_()
                                                        if (d_47_valueOrError23_).IsFailure():
                                                            return (d_47_valueOrError23_).PropagateFailure()
                                                        elif True:
                                                            d_55_material_ = (d_47_valueOrError23_).Extract()
                                                            source3_ = d_4_typ_
                                                            if True:
                                                                if (source3_) == (_dafny.Seq("symmetric")):
                                                                    d_56_valueOrError25_ = Base64.default__.Decode(d_55_material_)
                                                                    if (d_56_valueOrError25_).IsFailure():
                                                                        return (d_56_valueOrError25_).PropagateFailure()
                                                                    elif True:
                                                                        d_57_materialBytes_ = (d_56_valueOrError25_).Extract()
                                                                        return Wrappers.Result_Success(KeyMaterial_Symetric(name, d_7_encrypt_, d_9_decrypt_, d_40_algorithm_, d_42_bits_, d_44_encoding_, d_57_materialBytes_, d_12_keyIdentifier_))
                                                            if True:
                                                                if (source3_) == (_dafny.Seq("private")):
                                                                    return Wrappers.Result_Success(KeyMaterial_PrivateRSA(name, d_7_encrypt_, d_9_decrypt_, d_40_algorithm_, d_42_bits_, d_44_encoding_, d_55_material_, d_12_keyIdentifier_))
                                                            if True:
                                                                if (source3_) == (_dafny.Seq("public")):
                                                                    return Wrappers.Result_Success(KeyMaterial_PublicRSA(name, d_7_encrypt_, d_9_decrypt_, d_42_bits_, d_40_algorithm_, d_44_encoding_, d_55_material_, d_12_keyIdentifier_))
                                                            if True:
                                                                d_58_valueOrError26_ = UTF8.default__.Encode(d_55_material_)
                                                                if (d_58_valueOrError26_).IsFailure():
                                                                    return (d_58_valueOrError26_).PropagateFailure()
                                                                elif True:
                                                                    d_59_publicKey_ = (d_58_valueOrError26_).Extract()
                                                                    return Wrappers.Result_Success(KeyMaterial_KMSAsymetric(name, d_7_encrypt_, d_9_decrypt_, d_12_keyIdentifier_, d_42_bits_, d_40_algorithm_, d_44_encoding_, d_59_publicKey_))

    @staticmethod
    def ToStaticMaterial(mpl, name, obj):
        d_0_valueOrError0_ = default__.GetAlgorithmSuiteInfo(mpl, obj)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_algorithmSuite_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = JSONHelpers.default__.SmallObjectToStringStringMap(_dafny.Seq("encryptionContext"), obj)
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_encryptionContextStrings_ = (d_2_valueOrError1_).Extract()
                d_4_valueOrError2_ = JSONHelpers.default__.utf8EncodeMap(d_3_encryptionContextStrings_)
                if (d_4_valueOrError2_).IsFailure():
                    return (d_4_valueOrError2_).PropagateFailure()
                elif True:
                    d_5_encryptionContext_ = (d_4_valueOrError2_).Extract()
                    d_6_valueOrError3_ = JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), obj)
                    if (d_6_valueOrError3_).IsFailure():
                        return (d_6_valueOrError3_).PropagateFailure()
                    elif True:
                        d_7_keysAsStrings_ = (d_6_valueOrError3_).Extract()
                        d_8_valueOrError4_ = JSONHelpers.default__.utf8EncodeSeq(d_7_keysAsStrings_)
                        if (d_8_valueOrError4_).IsFailure():
                            return (d_8_valueOrError4_).PropagateFailure()
                        elif True:
                            d_9_requiredEncryptionContextKeys_ = (d_8_valueOrError4_).Extract()
                            d_10_valueOrError5_ = JSONHelpers.default__.GetArrayObject(_dafny.Seq("encryptedDataKeys"), obj)
                            if (d_10_valueOrError5_).IsFailure():
                                return (d_10_valueOrError5_).PropagateFailure()
                            elif True:
                                d_11_encryptedDataKeysJSON_ = (d_10_valueOrError5_).Extract()
                                d_12_valueOrError6_ = Seq.default__.MapWithResult(default__.ToEncryptedDataKey, d_11_encryptedDataKeysJSON_)
                                if (d_12_valueOrError6_).IsFailure():
                                    return (d_12_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_13_encryptedDataKeys_ = (d_12_valueOrError6_).Extract()
                                    d_14_valueOrError7_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("plaintextDataKey"), obj)
                                    if (d_14_valueOrError7_).IsFailure():
                                        return (d_14_valueOrError7_).PropagateFailure()
                                    elif True:
                                        d_15_plaintextDataKeyEncoded_ = (d_14_valueOrError7_).Extract()
                                        def iife0_(_pat_let6_0):
                                            def iife1_(d_17_result_):
                                                return (Wrappers.Result_Success(Wrappers.Option_Some((d_17_result_).value)) if (d_17_result_).is_Success else Wrappers.Result_Failure((d_17_result_).error))
                                            return iife1_(_pat_let6_0)
                                        d_16_valueOrError8_ = (iife0_(Base64.default__.Decode((d_15_plaintextDataKeyEncoded_).value)) if (d_15_plaintextDataKeyEncoded_).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                                        if (d_16_valueOrError8_).IsFailure():
                                            return (d_16_valueOrError8_).PropagateFailure()
                                        elif True:
                                            d_18_plaintextDataKey_ = (d_16_valueOrError8_).Extract()
                                            d_19_valueOrError9_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("signingKey"), obj)
                                            if (d_19_valueOrError9_).IsFailure():
                                                return (d_19_valueOrError9_).PropagateFailure()
                                            elif True:
                                                d_20_signingKey_ = (d_19_valueOrError9_).Extract()
                                                d_21_valueOrError10_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("verificationKey"), obj)
                                                if (d_21_valueOrError10_).IsFailure():
                                                    return (d_21_valueOrError10_).PropagateFailure()
                                                elif True:
                                                    d_22_verificationKey_ = (d_21_valueOrError10_).Extract()
                                                    d_23_symmetricSigningKeys_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("symmetricSigningKeys"), obj)).ToOption()
                                                    return Wrappers.Result_Success(KeyMaterial_StaticMaterial(name, d_1_algorithmSuite_, d_5_encryptionContext_, d_13_encryptedDataKeys_, d_9_requiredEncryptionContextKeys_, d_18_plaintextDataKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))

    @staticmethod
    def ToStaticBranchKey(mpl, name, obj):
        d_0_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("key-id"), obj)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_keyIdentifier_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("branchKeyVersion"), obj)
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_branchKeyVersionEncoded_ = (d_2_valueOrError1_).Extract()
                d_4_valueOrError2_ = UTF8.default__.Encode(d_3_branchKeyVersionEncoded_)
                if (d_4_valueOrError2_).IsFailure():
                    return (d_4_valueOrError2_).PropagateFailure()
                elif True:
                    d_5_branchKeyVersion_ = (d_4_valueOrError2_).Extract()
                    d_6_valueOrError3_ = JSONHelpers.default__.GetString(_dafny.Seq("branchKey"), obj)
                    if (d_6_valueOrError3_).IsFailure():
                        return (d_6_valueOrError3_).PropagateFailure()
                    elif True:
                        d_7_branchKeyEncoded_ = (d_6_valueOrError3_).Extract()
                        d_8_valueOrError4_ = Base64.default__.Decode(d_7_branchKeyEncoded_)
                        if (d_8_valueOrError4_).IsFailure():
                            return (d_8_valueOrError4_).PropagateFailure()
                        elif True:
                            d_9_branchKey_ = (d_8_valueOrError4_).Extract()
                            d_10_valueOrError5_ = JSONHelpers.default__.GetString(_dafny.Seq("beaconKey"), obj)
                            if (d_10_valueOrError5_).IsFailure():
                                return (d_10_valueOrError5_).PropagateFailure()
                            elif True:
                                d_11_beaconKeyEncoded_ = (d_10_valueOrError5_).Extract()
                                d_12_valueOrError6_ = Base64.default__.Decode(d_11_beaconKeyEncoded_)
                                if (d_12_valueOrError6_).IsFailure():
                                    return (d_12_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_13_beaconKey_ = (d_12_valueOrError6_).Extract()
                                    return Wrappers.Result_Success(KeyMaterial_StaticKeyStoreInformation(d_1_keyIdentifier_, d_5_branchKeyVersion_, d_9_branchKey_, d_13_beaconKey_))

    @staticmethod
    def ToEncryptedDataKey(obj):
        d_0_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderId"), obj)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_keyProviderIdJSON_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderInfo"), obj)
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_keyProviderInfoJSON_ = (d_2_valueOrError1_).Extract()
                d_4_valueOrError2_ = JSONHelpers.default__.GetString(_dafny.Seq("ciphertext"), obj)
                if (d_4_valueOrError2_).IsFailure():
                    return (d_4_valueOrError2_).PropagateFailure()
                elif True:
                    d_5_ciphertextJSON_ = (d_4_valueOrError2_).Extract()
                    d_6_valueOrError3_ = UTF8.default__.Encode(d_1_keyProviderIdJSON_)
                    if (d_6_valueOrError3_).IsFailure():
                        return (d_6_valueOrError3_).PropagateFailure()
                    elif True:
                        d_7_keyProviderId_ = (d_6_valueOrError3_).Extract()
                        d_8_valueOrError4_ = Base64.default__.Decode(d_3_keyProviderInfoJSON_)
                        if (d_8_valueOrError4_).IsFailure():
                            return (d_8_valueOrError4_).PropagateFailure()
                        elif True:
                            d_9_keyProviderInfo_ = (d_8_valueOrError4_).Extract()
                            d_10_valueOrError5_ = Base64.default__.Decode(d_5_ciphertextJSON_)
                            if (d_10_valueOrError5_).IsFailure():
                                return (d_10_valueOrError5_).PropagateFailure()
                            elif True:
                                d_11_ciphertext_ = (d_10_valueOrError5_).Extract()
                                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(d_7_keyProviderId_, d_9_keyProviderInfo_, d_11_ciphertext_))

    @staticmethod
    def GetAlgorithmSuiteInfo(mpl, obj):
        d_0_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("algorithmSuiteId"), obj)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_algorithmSuiteHex_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = Wrappers.default__.Need(HexStrings.default__.IsLooseHexString(d_1_algorithmSuiteHex_), _dafny.Seq("Not hex encoded binary"))
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_binaryId_ = HexStrings.default__.FromHexString(d_1_algorithmSuiteHex_)
                def lambda0_(d_4_algorithmSuiteHex_):
                    def lambda1_(d_5_e_):
                        return (_dafny.Seq("Invalid Suite:")) + (d_4_algorithmSuiteHex_)

                    return lambda1_

                return ((mpl).GetAlgorithmSuiteInfo(d_3_binaryId_)).MapFailure(lambda0_(d_1_algorithmSuiteHex_))

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

