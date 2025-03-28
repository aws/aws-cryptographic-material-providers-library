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

# Module: KeyDescription

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def printErr(e):
        hresult_: tuple = ()
        _dafny.print(_dafny.string_of(e))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        hresult_ = ()
        return hresult_
        return hresult_

    @staticmethod
    def printJSON(e):
        hresult_: tuple = ()
        _dafny.print(_dafny.string_of(e))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        hresult_ = ()
        return hresult_
        return hresult_

    @staticmethod
    def ToKeyDescription(json):
        if (json).is_Array:
            d_0_valueOrError0_ = Wrappers.default__.Need((1) <= (len((json).arr)), _dafny.Seq("Need at least one element in a JSON Array."))
            if (d_0_valueOrError0_).IsFailure():
                return (d_0_valueOrError0_).PropagateFailure()
            elif True:
                def lambda0_(forall_var_0_):
                    d_2_c_: JSON_Values.JSON = forall_var_0_
                    return not ((d_2_c_) in ((json).arr)) or ((d_2_c_).is_Object)

                d_1_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier(((json).arr).UniqueElements, True, lambda0_), _dafny.Seq("No nested arrays."))
                if (d_1_valueOrError1_).IsFailure():
                    return (d_1_valueOrError1_).PropagateFailure()
                elif True:
                    return default__.ToMultiKeyring(json, Wrappers.Option_Some(((json).arr)[0]), _dafny.Seq(((json).arr)[1::]))
        elif True:
            d_3_valueOrError2_ = Wrappers.default__.Need((json).is_Object, _dafny.Seq("KeyDescription not an object"))
            if (d_3_valueOrError2_).IsFailure():
                return (d_3_valueOrError2_).PropagateFailure()
            elif True:
                d_4_obj_ = (json).obj
                d_5_typString_ = _dafny.Seq("type")
                d_6_valueOrError3_ = JSONHelpers.default__.GetString(d_5_typString_, d_4_obj_)
                if (d_6_valueOrError3_).IsFailure():
                    return (d_6_valueOrError3_).PropagateFailure()
                elif True:
                    d_7_typ_ = (d_6_valueOrError3_).Extract()
                    d_8_valueOrError4_ = Wrappers.default__.Need(default__.KeyDescriptionString_q(d_7_typ_), (_dafny.Seq("Unsupported KeyDescription type:")) + (d_7_typ_))
                    if (d_8_valueOrError4_).IsFailure():
                        return (d_8_valueOrError4_).PropagateFailure()
                    elif True:
                        source0_ = d_7_typ_
                        if True:
                            if (source0_) == (_dafny.Seq("aws-kms-mrk-aware-discovery")):
                                return default__.ToAwsKmsMrkAwareDiscovery(d_4_obj_)
                        if True:
                            if (source0_) == (_dafny.Seq("multi-keyring")):
                                d_9_generatorJson_ = (JSONHelpers.default__.Get(_dafny.Seq("generator"), d_4_obj_)).ToOption()
                                d_10_valueOrError5_ = JSONHelpers.default__.GetArray(_dafny.Seq("childKeyrings"), d_4_obj_)
                                if (d_10_valueOrError5_).IsFailure():
                                    return (d_10_valueOrError5_).PropagateFailure()
                                elif True:
                                    d_11_childKeyringsJson_ = (d_10_valueOrError5_).Extract()
                                    return default__.ToMultiKeyring(json, d_9_generatorJson_, d_11_childKeyringsJson_)
                        if True:
                            if (source0_) == (_dafny.Seq("required-encryption-context-cmm")):
                                d_12_valueOrError6_ = JSONHelpers.default__.Get(_dafny.Seq("underlying"), d_4_obj_)
                                if (d_12_valueOrError6_).IsFailure():
                                    return (d_12_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_13_u_ = (d_12_valueOrError6_).Extract()
                                    d_14_valueOrError7_ = default__.ToKeyDescription(d_13_u_)
                                    if (d_14_valueOrError7_).IsFailure():
                                        return (d_14_valueOrError7_).PropagateFailure()
                                    elif True:
                                        d_15_underlying_ = (d_14_valueOrError7_).Extract()
                                        d_16_requiredEncryptionContextStrings_ = ((JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), d_4_obj_)).ToOption()).UnwrapOr(_dafny.Seq([]))
                                        d_17_valueOrError8_ = JSONHelpers.default__.utf8EncodeSeq(d_16_requiredEncryptionContextStrings_)
                                        if (d_17_valueOrError8_).IsFailure():
                                            return (d_17_valueOrError8_).PropagateFailure()
                                        elif True:
                                            d_18_requiredEncryptionContextKeys_ = (d_17_valueOrError8_).Extract()
                                            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_RequiredEncryptionContext(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RequiredEncryptionContextCMM_RequiredEncryptionContextCMM(d_15_underlying_, d_18_requiredEncryptionContextKeys_)))
                        if True:
                            if (source0_) == (_dafny.Seq("raw-ecdh")):
                                return default__.ToRawEcdh(d_4_obj_)
                        if True:
                            if (source0_) == (_dafny.Seq("aws-kms-ecdh")):
                                return default__.ToAwsKmsEcdh(d_4_obj_)
                        if True:
                            d_19_valueOrError9_ = JSONHelpers.default__.GetString(_dafny.Seq("key"), d_4_obj_)
                            if (d_19_valueOrError9_).IsFailure():
                                return (d_19_valueOrError9_).PropagateFailure()
                            elif True:
                                d_20_key_ = (d_19_valueOrError9_).Extract()
                                source1_ = d_7_typ_
                                if True:
                                    if (source1_) == (_dafny.Seq("static-material-keyring")):
                                        return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Static(AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring_StaticKeyring(d_20_key_)))
                                if True:
                                    if (source1_) == (_dafny.Seq("aws-kms")):
                                        return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Kms(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KMSInfo_KMSInfo(d_20_key_)))
                                if True:
                                    if (source1_) == (_dafny.Seq("aws-kms-mrk-aware")):
                                        return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsMrk(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAware_KmsMrkAware(d_20_key_)))
                                if True:
                                    if (source1_) == (_dafny.Seq("aws-kms-rsa")):
                                        return default__.ToAwsKmsRsa(d_20_key_, d_4_obj_)
                                if True:
                                    if (source1_) == (_dafny.Seq("aws-kms-hierarchy")):
                                        return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Hierarchy(AwsCryptographyMaterialProvidersTestVectorKeysTypes.HierarchyKeyring_HierarchyKeyring(d_20_key_)))
                                if True:
                                    d_21_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("encryption-algorithm"), d_4_obj_)
                                    if (d_21_valueOrError10_).IsFailure():
                                        return (d_21_valueOrError10_).PropagateFailure()
                                    elif True:
                                        d_22_algorithm_ = (d_21_valueOrError10_).Extract()
                                        d_23_valueOrError11_ = Wrappers.default__.Need(default__.RawAlgorithmString_q(d_22_algorithm_), (_dafny.Seq("Unsupported algorithm:")) + (d_22_algorithm_))
                                        if (d_23_valueOrError11_).IsFailure():
                                            return (d_23_valueOrError11_).PropagateFailure()
                                        elif True:
                                            source2_ = d_22_algorithm_
                                            if True:
                                                if (source2_) == (_dafny.Seq("aes")):
                                                    return default__.ToRawAes(d_20_key_, d_4_obj_)
                                            if True:
                                                return default__.ToRawRsa(d_20_key_, d_4_obj_)

    @staticmethod
    def ToDiscoveryFilter(obj):
        d_0_valueOrError0_ = (JSONHelpers.default__.GetObject(_dafny.Seq("aws-kms-discovery-filter"), obj)).ToOption()
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_filter_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = (JSONHelpers.default__.GetString(_dafny.Seq("partition"), d_1_filter_)).ToOption()
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_partition_ = (d_2_valueOrError1_).Extract()
                d_4_valueOrError2_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("account-ids"), d_1_filter_)).ToOption()
                if (d_4_valueOrError2_).IsFailure():
                    return (d_4_valueOrError2_).PropagateFailure()
                elif True:
                    d_5_accountIds_ = (d_4_valueOrError2_).Extract()
                    return Wrappers.Option_Some(AwsCryptographyMaterialProvidersTypes.DiscoveryFilter_DiscoveryFilter(d_5_accountIds_, d_3_partition_))

    @staticmethod
    def ToAwsKmsMrkAwareDiscovery(obj):
        d_0_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("default-mrk-region"), obj)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_defaultMrkRegion_ = (d_0_valueOrError0_).Extract()
            d_2_filter_ = JSONHelpers.default__.GetObject(_dafny.Seq("aws-kms-discovery-filter"), obj)
            d_3_awsKmsDiscoveryFilter_ = default__.ToDiscoveryFilter(obj)
            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsMrkDiscovery(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsMrkAwareDiscovery_KmsMrkAwareDiscovery(_dafny.Seq("aws-kms-mrk-aware-discovery"), d_1_defaultMrkRegion_, d_3_awsKmsDiscoveryFilter_)))

    @staticmethod
    def ToAwsKmsRsa(key, obj):
        d_0_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("encryption-algorithm"), obj)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_encryptionAlgorithmString_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = Wrappers.default__.Need((d_1_encryptionAlgorithmString_) in (default__.String2EncryptionAlgorithmSpec), (_dafny.Seq("Unsupported EncryptionAlgorithmSpec:")) + (d_1_encryptionAlgorithmString_))
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_encryptionAlgorithm_ = (default__.String2EncryptionAlgorithmSpec)[d_1_encryptionAlgorithmString_]
                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsRsa(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsRsaKeyring_KmsRsaKeyring(key, d_3_encryptionAlgorithm_)))

    @staticmethod
    def ToAwsKmsEcdh(obj):
        d_0_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("ecc-curve"), obj)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_eccCurve_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = Wrappers.default__.Need((d_1_eccCurve_) in (default__.KmsKey2EccAlgorithmSpec), (_dafny.Seq("Unsupported ECC Curve Spec:")) + (d_1_eccCurve_))
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_valueOrError2_ = JSONHelpers.default__.GetString(_dafny.Seq("schema"), obj)
                if (d_3_valueOrError2_).IsFailure():
                    return (d_3_valueOrError2_).PropagateFailure()
                elif True:
                    d_4_schema_ = (d_3_valueOrError2_).Extract()
                    d_5_valueOrError3_ = JSONHelpers.default__.GetString(_dafny.Seq("sender"), obj)
                    if (d_5_valueOrError3_).IsFailure():
                        return (d_5_valueOrError3_).PropagateFailure()
                    elif True:
                        d_6_sender_ = (d_5_valueOrError3_).Extract()
                        d_7_valueOrError4_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient"), obj)
                        if (d_7_valueOrError4_).IsFailure():
                            return (d_7_valueOrError4_).PropagateFailure()
                        elif True:
                            d_8_recipient_ = (d_7_valueOrError4_).Extract()
                            d_9_valueOrError5_ = JSONHelpers.default__.GetString(_dafny.Seq("sender-public-key"), obj)
                            if (d_9_valueOrError5_).IsFailure():
                                return (d_9_valueOrError5_).PropagateFailure()
                            elif True:
                                d_10_senderPublicKey_ = (d_9_valueOrError5_).Extract()
                                d_11_valueOrError6_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient-public-key"), obj)
                                if (d_11_valueOrError6_).IsFailure():
                                    return (d_11_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_12_recipientPublicKey_ = (d_11_valueOrError6_).Extract()
                                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_KmsECDH(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KmsEcdhKeyring_KmsEcdhKeyring(d_6_sender_, d_8_recipient_, d_10_senderPublicKey_, d_12_recipientPublicKey_, d_1_eccCurve_, d_4_schema_)))

    @staticmethod
    def ToRawAes(key, obj):
        d_0_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("provider-id"), obj)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_providerId_ = (d_0_valueOrError0_).Extract()
            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_AES(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawAES_RawAES(key, d_1_providerId_)))

    @staticmethod
    def ToRawRsa(key, obj):
        d_0_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("provider-id"), obj)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_providerId_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("padding-algorithm"), obj)
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_paddingAlgorithm_ = (d_2_valueOrError1_).Extract()
                d_4_valueOrError2_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("padding-hash"), obj)
                if (d_4_valueOrError2_).IsFailure():
                    return (d_4_valueOrError2_).PropagateFailure()
                elif True:
                    d_5_maybePaddingHash_ = (d_4_valueOrError2_).Extract()
                    d_6_valueOrError3_ = Wrappers.default__.Need(not ((d_5_maybePaddingHash_).is_None) or ((d_3_paddingAlgorithm_) == (_dafny.Seq("pkcs1"))), _dafny.Seq("oaep-mgf1 MUST define padding-hash"))
                    if (d_6_valueOrError3_).IsFailure():
                        return (d_6_valueOrError3_).PropagateFailure()
                    elif True:
                        d_7_paddingHash_ = (d_5_maybePaddingHash_).UnwrapOr(_dafny.Seq("sha1"))
                        d_8_valueOrError4_ = Wrappers.default__.Need(((d_3_paddingAlgorithm_, d_7_paddingHash_)) in (default__.String2PaddingAlgorithm), (((_dafny.Seq("Unsupported padding:")) + (d_3_paddingAlgorithm_)) + (_dafny.Seq(" hash:"))) + (d_7_paddingHash_))
                        if (d_8_valueOrError4_).IsFailure():
                            return (d_8_valueOrError4_).PropagateFailure()
                        elif True:
                            return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_RSA(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawRSA_RawRSA(key, d_1_providerId_, (default__.String2PaddingAlgorithm)[(d_3_paddingAlgorithm_, d_7_paddingHash_)])))

    @staticmethod
    def ToRawEcdh(obj):
        d_0_valueOrError0_ = JSONHelpers.default__.GetString(_dafny.Seq("provider-id"), obj)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_providerId_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("ecc-curve"), obj)
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_ecc__curve_ = (d_2_valueOrError1_).Extract()
                d_4_valueOrError2_ = JSONHelpers.default__.GetString(_dafny.Seq("sender"), obj)
                if (d_4_valueOrError2_).IsFailure():
                    return (d_4_valueOrError2_).PropagateFailure()
                elif True:
                    d_5_sender_ = (d_4_valueOrError2_).Extract()
                    d_6_valueOrError3_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient"), obj)
                    if (d_6_valueOrError3_).IsFailure():
                        return (d_6_valueOrError3_).PropagateFailure()
                    elif True:
                        d_7_recipient_ = (d_6_valueOrError3_).Extract()
                        d_8_valueOrError4_ = JSONHelpers.default__.GetString(_dafny.Seq("schema"), obj)
                        if (d_8_valueOrError4_).IsFailure():
                            return (d_8_valueOrError4_).PropagateFailure()
                        elif True:
                            d_9_schema_ = (d_8_valueOrError4_).Extract()
                            d_10_valueOrError5_ = JSONHelpers.default__.GetString(_dafny.Seq("sender-public-key"), obj)
                            if (d_10_valueOrError5_).IsFailure():
                                return (d_10_valueOrError5_).PropagateFailure()
                            elif True:
                                d_11_senderPublicKey_ = (d_10_valueOrError5_).Extract()
                                d_12_valueOrError6_ = JSONHelpers.default__.GetString(_dafny.Seq("recipient-public-key"), obj)
                                if (d_12_valueOrError6_).IsFailure():
                                    return (d_12_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_13_recipientPublicKey_ = (d_12_valueOrError6_).Extract()
                                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_ECDH(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawEcdh_RawEcdh(d_5_sender_, d_7_recipient_, d_11_senderPublicKey_, d_13_recipientPublicKey_, d_1_providerId_, d_3_ecc__curve_, d_9_schema_)))

    @staticmethod
    def ToMultiKeyring(json, generatorJson, childKeyringsJson):
        d_0_valueOrError0_ = Wrappers.default__.Need(not ((generatorJson).is_Some) or (((generatorJson).value).is_Object), _dafny.Seq("Not an object"))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            def iife0_(_pat_let0_0):
                def iife1_(d_2_valueOrError2_):
                    def iife2_(_pat_let1_0):
                        def iife3_(d_3_g_):
                            return Wrappers.Result_Success(Wrappers.Option_Some(d_3_g_))
                        return iife3_(_pat_let1_0)
                    return ((d_2_valueOrError2_).PropagateFailure() if (d_2_valueOrError2_).IsFailure() else iife2_((d_2_valueOrError2_).Extract()))
                return iife1_(_pat_let0_0)
            d_1_valueOrError1_ = (iife0_(default__.ToKeyDescription((generatorJson).value)) if (generatorJson).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
            if (d_1_valueOrError1_).IsFailure():
                return (d_1_valueOrError1_).PropagateFailure()
            elif True:
                d_4_generator_ = (d_1_valueOrError1_).Extract()
                def lambda0_(d_6_childKeyringsJson_):
                    def lambda1_(d_7_c_):
                        return default__.ToKeyDescription(d_7_c_)

                    return lambda1_

                d_5_valueOrError3_ = Seq.default__.MapWithResult(lambda0_(childKeyringsJson), childKeyringsJson)
                if (d_5_valueOrError3_).IsFailure():
                    return (d_5_valueOrError3_).PropagateFailure()
                elif True:
                    d_8_childKeyrings_ = (d_5_valueOrError3_).Extract()
                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Multi(AwsCryptographyMaterialProvidersTestVectorKeysTypes.MultiKeyring_MultiKeyring(d_4_generator_, d_8_childKeyrings_)))

    @staticmethod
    def KeyDescriptionString_q(s):
        return (((((((((((s) == (_dafny.Seq("static-material-keyring"))) or ((s) == (_dafny.Seq("aws-kms")))) or ((s) == (_dafny.Seq("aws-kms-mrk-aware")))) or ((s) == (_dafny.Seq("aws-kms-mrk-aware-discovery")))) or ((s) == (_dafny.Seq("raw")))) or ((s) == (_dafny.Seq("raw-ecdh")))) or ((s) == (_dafny.Seq("aws-kms-hierarchy")))) or ((s) == (_dafny.Seq("aws-kms-rsa")))) or ((s) == (_dafny.Seq("aws-kms-ecdh")))) or ((s) == (_dafny.Seq("required-encryption-context-cmm")))) or ((s) == (_dafny.Seq("multi-keyring")))

    @staticmethod
    def RawAlgorithmString_q(s):
        return ((s) == (_dafny.Seq("aes"))) or ((s) == (_dafny.Seq("rsa")))

    @staticmethod
    def KeyDescriptionVersion_q(v):
        return (((v) == (1)) or ((v) == (2))) or ((v) == (3))

    @staticmethod
    def ToJson(keyDescription, outputVersion):
        source0_ = keyDescription
        if True:
            if source0_.is_Kms:
                d_0_Kms_ = source0_.Kms
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_0_Kms_).keyId))])))
        if True:
            if source0_.is_KmsMrk:
                d_1_KmsMrk_ = source0_.KmsMrk
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-mrk-aware"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_1_KmsMrk_).keyId))])))
        if True:
            if source0_.is_KmsMrkDiscovery:
                d_2_KmsMrkDiscovery_ = source0_.KmsMrkDiscovery
                def lambda0_(d_4_s_):
                    return JSON_Values.JSON_String(d_4_s_)

                d_3_filter_ = (_dafny.Seq([(_dafny.Seq("aws-kms-discovery-filter"), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("partition"), JSON_Values.JSON_String((((d_2_KmsMrkDiscovery_).awsKmsDiscoveryFilter).value).partition)), (_dafny.Seq("account-ids"), JSON_Values.JSON_Array(Seq.default__.Map(lambda0_, (((d_2_KmsMrkDiscovery_).awsKmsDiscoveryFilter).value).accountIds)))])))]) if ((d_2_KmsMrkDiscovery_).awsKmsDiscoveryFilter).is_Some else _dafny.Seq([]))
                return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-mrk-aware-discovery"))), (_dafny.Seq("default-mrk-region"), JSON_Values.JSON_String((d_2_KmsMrkDiscovery_).defaultMrkRegion))])) + (d_3_filter_)))
        if True:
            if source0_.is_RSA:
                d_5_RSA_ = source0_.RSA
                d_6_padding_ = (default__.PaddingAlgorithmString2String)[(d_5_RSA_).padding]
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("raw"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_5_RSA_).keyId)), (_dafny.Seq("provider-id"), JSON_Values.JSON_String((d_5_RSA_).providerId)), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(_dafny.Seq("rsa"))), (_dafny.Seq("padding-algorithm"), JSON_Values.JSON_String((d_6_padding_)[0])), (_dafny.Seq("padding-hash"), JSON_Values.JSON_String((d_6_padding_)[1]))])))
        if True:
            if source0_.is_AES:
                d_7_AES_ = source0_.AES
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("raw"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_7_AES_).keyId)), (_dafny.Seq("provider-id"), JSON_Values.JSON_String((d_7_AES_).providerId)), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(_dafny.Seq("aes")))])))
        if True:
            if source0_.is_ECDH:
                d_8_ECDH_ = source0_.ECDH
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("raw-ecdh"))), (_dafny.Seq("sender"), JSON_Values.JSON_String((d_8_ECDH_).senderKeyId)), (_dafny.Seq("recipient"), JSON_Values.JSON_String((d_8_ECDH_).recipientKeyId)), (_dafny.Seq("sender-public-key"), JSON_Values.JSON_String((d_8_ECDH_).senderPublicKey)), (_dafny.Seq("recipient-public-key"), JSON_Values.JSON_String((d_8_ECDH_).recipientPublicKey)), (_dafny.Seq("provider-id"), JSON_Values.JSON_String((d_8_ECDH_).providerId)), (_dafny.Seq("ecc-curve"), JSON_Values.JSON_String((d_8_ECDH_).curveSpec)), (_dafny.Seq("schema"), JSON_Values.JSON_String((d_8_ECDH_).keyAgreementScheme))])))
        if True:
            if source0_.is_Static:
                d_9_Static_ = source0_.Static
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("static-material-keyring"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_9_Static_).keyId))])))
        if True:
            if source0_.is_KmsRsa:
                d_10_KmsRsa_ = source0_.KmsRsa
                d_11_valueOrError0_ = Wrappers.default__.Need(((d_10_KmsRsa_).encryptionAlgorithm) in (default__.EncryptionAlgorithmSpec2String), _dafny.Seq("Unsupported encryptionAlgorithm"))
                if (d_11_valueOrError0_).IsFailure():
                    return (d_11_valueOrError0_).PropagateFailure()
                elif True:
                    d_12_encryptionAlgorithm_ = (default__.EncryptionAlgorithmSpec2String)[(d_10_KmsRsa_).encryptionAlgorithm]
                    return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-rsa"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_10_KmsRsa_).keyId)), (_dafny.Seq("encryption-algorithm"), JSON_Values.JSON_String(d_12_encryptionAlgorithm_))])))
        if True:
            if source0_.is_KmsECDH:
                d_13_KmsECDH_ = source0_.KmsECDH
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-ecdh"))), (_dafny.Seq("sender"), JSON_Values.JSON_String((d_13_KmsECDH_).senderKeyId)), (_dafny.Seq("recipient"), JSON_Values.JSON_String((d_13_KmsECDH_).recipientKeyId)), (_dafny.Seq("sender-public-key"), JSON_Values.JSON_String((d_13_KmsECDH_).senderPublicKey)), (_dafny.Seq("recipient-public-key"), JSON_Values.JSON_String((d_13_KmsECDH_).recipientPublicKey)), (_dafny.Seq("ecc-curve"), JSON_Values.JSON_String((d_13_KmsECDH_).curveSpec)), (_dafny.Seq("schema"), JSON_Values.JSON_String((d_13_KmsECDH_).keyAgreementScheme))])))
        if True:
            if source0_.is_Hierarchy:
                d_14_Hierarchy_ = source0_.Hierarchy
                return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("aws-kms-hierarchy"))), (_dafny.Seq("key"), JSON_Values.JSON_String((d_14_Hierarchy_).keyId))])))
        if True:
            if source0_.is_Multi:
                d_15_MultiKeyring_ = source0_.Multi
                def lambda1_(forall_var_0_):
                    d_17_c_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = forall_var_0_
                    return not ((d_17_c_) in ((d_15_MultiKeyring_).childKeyrings)) or (default__.Keyring_q(d_17_c_))

                d_16_valueOrError1_ = Wrappers.default__.Need((not (((d_15_MultiKeyring_).generator).is_Some) or (default__.Keyring_q(((d_15_MultiKeyring_).generator).value))) and (_dafny.quantifier(((d_15_MultiKeyring_).childKeyrings).UniqueElements, True, lambda1_)), _dafny.Seq("CMMs not supported by Multi Keyrings"))
                if (d_16_valueOrError1_).IsFailure():
                    return (d_16_valueOrError1_).PropagateFailure()
                elif True:
                    source1_ = outputVersion
                    if True:
                        if (source1_) == (3):
                            def iife0_(_pat_let2_0):
                                def iife1_(d_19_valueOrError3_):
                                    def iife2_(_pat_let3_0):
                                        def iife3_(d_20_g_):
                                            return Wrappers.Result_Success(Wrappers.Option_Some(d_20_g_))
                                        return iife3_(_pat_let3_0)
                                    return ((d_19_valueOrError3_).PropagateFailure() if (d_19_valueOrError3_).IsFailure() else iife2_((d_19_valueOrError3_).Extract()))
                                return iife1_(_pat_let2_0)
                            d_18_valueOrError2_ = (iife0_(default__.ToJson(((d_15_MultiKeyring_).generator).value, outputVersion)) if ((d_15_MultiKeyring_).generator).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                            if (d_18_valueOrError2_).IsFailure():
                                return (d_18_valueOrError2_).PropagateFailure()
                            elif True:
                                d_21_generator_ = (d_18_valueOrError2_).Extract()
                                d_22_valueOrError4_ = default__.KeyDescriptionListToJson((d_15_MultiKeyring_).childKeyrings, outputVersion)
                                if (d_22_valueOrError4_).IsFailure():
                                    return (d_22_valueOrError4_).PropagateFailure()
                                elif True:
                                    d_23_childKeyrings_ = (d_22_valueOrError4_).Extract()
                                    return Wrappers.Result_Success(JSON_Values.JSON_Object((_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("multi-keyring"))), (_dafny.Seq("childKeyrings"), JSON_Values.JSON_Array(d_23_childKeyrings_))])) + ((_dafny.Seq([(_dafny.Seq("generator"), (d_21_generator_).value)]) if (d_21_generator_).is_Some else _dafny.Seq([])))))
                    if True:
                        d_24_valueOrError5_ = Wrappers.default__.Need(((d_15_MultiKeyring_).generator).is_Some, _dafny.Seq("Generator required for v1 or v2"))
                        if (d_24_valueOrError5_).IsFailure():
                            return (d_24_valueOrError5_).PropagateFailure()
                        elif True:
                            d_25_keyrings_ = (_dafny.Seq([((d_15_MultiKeyring_).generator).value])) + ((d_15_MultiKeyring_).childKeyrings)
                            def lambda2_(forall_var_1_):
                                d_27_c_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription = forall_var_1_
                                return not ((d_27_c_) in (d_25_keyrings_)) or (not((d_27_c_).is_Multi))

                            d_26_valueOrError6_ = Wrappers.default__.Need(_dafny.quantifier((d_25_keyrings_).UniqueElements, True, lambda2_), _dafny.Seq("Recursive structures not supported"))
                            if (d_26_valueOrError6_).IsFailure():
                                return (d_26_valueOrError6_).PropagateFailure()
                            elif True:
                                d_28_valueOrError7_ = default__.ToJson(((d_15_MultiKeyring_).generator).value, outputVersion)
                                if (d_28_valueOrError7_).IsFailure():
                                    return (d_28_valueOrError7_).PropagateFailure()
                                elif True:
                                    d_29_g_ = (d_28_valueOrError7_).Extract()
                                    d_30_valueOrError8_ = default__.KeyDescriptionListToJson((d_15_MultiKeyring_).childKeyrings, outputVersion)
                                    if (d_30_valueOrError8_).IsFailure():
                                        return (d_30_valueOrError8_).PropagateFailure()
                                    elif True:
                                        d_31_keyrings_ = (d_30_valueOrError8_).Extract()
                                        return Wrappers.Result_Success(JSON_Values.JSON_Array((_dafny.Seq([d_29_g_])) + (d_31_keyrings_)))
        if True:
            d_32_RequiredEncryptionContext_ = source0_.RequiredEncryptionContext
            d_33_valueOrError9_ = default__.ToJson((d_32_RequiredEncryptionContext_).underlying, outputVersion)
            if (d_33_valueOrError9_).IsFailure():
                return (d_33_valueOrError9_).PropagateFailure()
            elif True:
                d_34_underlying_ = (d_33_valueOrError9_).Extract()
                def lambda3_(d_36_key_):
                    def iife4_(_pat_let4_0):
                        def iife5_(d_37_valueOrError11_):
                            def iife6_(_pat_let5_0):
                                def iife7_(d_38_s_):
                                    return Wrappers.Result_Success(JSON_Values.JSON_String(d_38_s_))
                                return iife7_(_pat_let5_0)
                            return ((d_37_valueOrError11_).PropagateFailure() if (d_37_valueOrError11_).IsFailure() else iife6_((d_37_valueOrError11_).Extract()))
                        return iife5_(_pat_let4_0)
                    return iife4_(UTF8.default__.Decode(d_36_key_))

                d_35_valueOrError10_ = Seq.default__.MapWithResult(lambda3_, (d_32_RequiredEncryptionContext_).requiredEncryptionContextKeys)
                if (d_35_valueOrError10_).IsFailure():
                    return (d_35_valueOrError10_).PropagateFailure()
                elif True:
                    d_39_requiredEncryptionContextKeys_ = (d_35_valueOrError10_).Extract()
                    return Wrappers.Result_Success(JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("required-encryption-context-cmm"))), (_dafny.Seq("underlying"), d_34_underlying_), (_dafny.Seq("requiredEncryptionContextKeys"), JSON_Values.JSON_Array(d_39_requiredEncryptionContextKeys_))])))

    @staticmethod
    def Keyring_q(description):
        return (((((((((((description).is_Kms) or ((description).is_KmsMrk)) or ((description).is_KmsMrkDiscovery)) or ((description).is_RSA)) or ((description).is_AES)) or ((description).is_ECDH)) or ((description).is_Static)) or ((description).is_KmsRsa)) or ((description).is_KmsECDH)) or ((description).is_Hierarchy)) or ((description).is_Multi)

    @staticmethod
    def KeyDescriptionListToJson(childKeyrings, outputVersion):
        if (0) == (len(childKeyrings)):
            return Wrappers.Result_Success(_dafny.Seq([]))
        elif True:
            d_0_valueOrError0_ = default__.ToJson((childKeyrings)[0], outputVersion)
            if (d_0_valueOrError0_).IsFailure():
                return (d_0_valueOrError0_).PropagateFailure()
            elif True:
                d_1_json_ = (d_0_valueOrError0_).Extract()
                d_2_valueOrError1_ = default__.KeyDescriptionListToJson(_dafny.Seq((childKeyrings)[1::]), outputVersion)
                if (d_2_valueOrError1_).IsFailure():
                    return (d_2_valueOrError1_).PropagateFailure()
                elif True:
                    d_3_rest_ = (d_2_valueOrError1_).Extract()
                    return Wrappers.Result_Success((_dafny.Seq([d_1_json_])) + (d_3_rest_))

    @staticmethod
    def Invert(m):
        def iife0_():
            coll0_ = _dafny.Map()
            compr_0_: TypeVar('X__')
            for compr_0_ in (m).keys.Elements:
                d_0_k_: TypeVar('X__') = compr_0_
                if (d_0_k_) in (m):
                    coll0_[(m)[d_0_k_]] = d_0_k_
            return _dafny.Map(coll0_)
        return iife0_()
        

    @_dafny.classproperty
    def KmsKey2EccAlgorithmSpec(instance):
        return _dafny.Map({_dafny.Seq("us-west-2-256-ecc"): AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), _dafny.Seq("us-west-2-384-ecc"): AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384(), _dafny.Seq("us-west-2-521-ecc"): AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()})
    @_dafny.classproperty
    def EncryptionAlgorithmSpec2String(instance):
        return _dafny.Map({ComAmazonawsKmsTypes.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1(): _dafny.Seq("RSAES_OAEP_SHA_1"), ComAmazonawsKmsTypes.EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256(): _dafny.Seq("RSAES_OAEP_SHA_256")})
    @_dafny.classproperty
    def String2EncryptionAlgorithmSpec(instance):
        return default__.Invert(default__.EncryptionAlgorithmSpec2String)
    @_dafny.classproperty
    def PaddingAlgorithmString2String(instance):
        return _dafny.Map({AwsCryptographyMaterialProvidersTypes.PaddingScheme_PKCS1(): (_dafny.Seq("pkcs1"), _dafny.Seq("sha1")), AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA1__MGF1(): (_dafny.Seq("oaep-mgf1"), _dafny.Seq("sha1")), AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA256__MGF1(): (_dafny.Seq("oaep-mgf1"), _dafny.Seq("sha256")), AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA384__MGF1(): (_dafny.Seq("oaep-mgf1"), _dafny.Seq("sha384")), AwsCryptographyMaterialProvidersTypes.PaddingScheme_OAEP__SHA512__MGF1(): (_dafny.Seq("oaep-mgf1"), _dafny.Seq("sha512"))})
    @_dafny.classproperty
    def String2PaddingAlgorithm(instance):
        return default__.Invert(default__.PaddingAlgorithmString2String)
    @_dafny.classproperty
    def EccAlgorithmSpec2string(instance):
        return _dafny.Map({AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(): _dafny.Seq("secp256r1"), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384(): _dafny.Seq("secp384r1"), AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521(): _dafny.Seq("secp521r1")})
    @_dafny.classproperty
    def String2EccAlgorithmSpec(instance):
        return default__.Invert(default__.EccAlgorithmSpec2string)
    @_dafny.classproperty
    def Curve2EccAlgorithmSpec(instance):
        return _dafny.Map({_dafny.Seq("ecc-256"): AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P256(), _dafny.Seq("ecc-384"): AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P384(), _dafny.Seq("ecc-521"): AwsCryptographyPrimitivesTypes.ECDHCurveSpec_ECC__NIST__P521()})
    @_dafny.classproperty
    def EccAlgorithmSpec2Spec(instance):
        return default__.Invert(default__.Curve2EccAlgorithmSpec)

class KeyDescriptionVersion:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return 1
    def _Is(source__):
        d_0_v_: int = source__
        return default__.KeyDescriptionVersion_q(d_0_v_)
