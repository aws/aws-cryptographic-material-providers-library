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
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.KeyMaterial as KeyMaterial
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.CreateStaticKeyrings as CreateStaticKeyrings
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.CreateStaticKeyStores as CreateStaticKeyStores
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.KeyringFromKeyDescription as KeyringFromKeyDescription
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.CmmFromKeyDescription as CmmFromKeyDescription
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.KeysVectorOperations as KeysVectorOperations
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.KeyVectors as KeyVectors
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.TestVectors as TestVectors
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllHierarchy as AllHierarchy
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.EncryptionContextUtils as EncryptionContextUtils
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllKms as AllKms
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllKmsMrkAware as AllKmsMrkAware
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllKmsMrkAwareDiscovery as AllKmsMrkAwareDiscovery
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllKmsRsa as AllKmsRsa
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllKmsEcdh as AllKmsEcdh
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllRawAES as AllRawAES
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllRawRSA as AllRawRSA
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllRawECDH as AllRawECDH
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllDefaultCmm as AllDefaultCmm
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllRequiredEncryptionContextCmm as AllRequiredEncryptionContextCmm
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllMulti as AllMulti
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.WriteJsonManifests as WriteJsonManifests
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.CompleteVectors as CompleteVectors

# Module: ParseJsonManifests

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BuildEncryptTestVector(keys, obj):
        hresult_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_i_: int
        d_0_i_ = len(obj)
        d_1_vectors_: _dafny.Seq
        d_1_vectors_ = _dafny.Seq([])
        while (d_0_i_) != (0):
            d_0_i_ = (d_0_i_) - (1)
            d_2_test_: Wrappers.Result
            d_2_test_ = default__.ToEncryptTestVector(keys, ((obj)[d_0_i_])[0], ((obj)[d_0_i_])[1])
            if (d_2_test_).is_Failure:
                hresult_ = Wrappers.Result_Failure((d_2_test_).error)
                return hresult_
            d_1_vectors_ = (_dafny.Seq([(d_2_test_).value])) + (d_1_vectors_)
        hresult_ = Wrappers.Result_Success(d_1_vectors_)
        return hresult_
        return hresult_

    @staticmethod
    def ToEncryptTestVector(keys, name, obj):
        d_0_valueOrError0_ = Wrappers.default__.Need((obj).is_Object, _dafny.Seq("EncryptTestVector not an object"))
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
                d_5_description_ = (JSONHelpers.default__.GetString(_dafny.Seq("description"), d_1_obj_)).ToOption()
                d_6_valueOrError2_ = JSONHelpers.default__.SmallObjectToStringStringMap(_dafny.Seq("encryptionContext"), d_1_obj_)
                if (d_6_valueOrError2_).IsFailure():
                    return (d_6_valueOrError2_).PropagateFailure()
                elif True:
                    d_7_encryptionContextStrings_ = (d_6_valueOrError2_).Extract()
                    d_8_valueOrError3_ = JSONHelpers.default__.utf8EncodeMap(d_7_encryptionContextStrings_)
                    if (d_8_valueOrError3_).IsFailure():
                        return (d_8_valueOrError3_).PropagateFailure()
                    elif True:
                        d_9_encryptionContext_ = (d_8_valueOrError3_).Extract()
                        d_10_valueOrError4_ = default__.GetAlgorithmSuiteInfo(d_1_obj_)
                        if (d_10_valueOrError4_).IsFailure():
                            return (d_10_valueOrError4_).PropagateFailure()
                        elif True:
                            d_11_algorithmSuite_ = (d_10_valueOrError4_).Extract()
                            d_12_valueOrError5_ = default__.GetRequiredEncryptionContextKeys(d_1_obj_)
                            if (d_12_valueOrError5_).IsFailure():
                                return (d_12_valueOrError5_).PropagateFailure()
                            elif True:
                                d_13_requiredEncryptionContextKeys_ = (d_12_valueOrError5_).Extract()
                                d_14_valueOrError6_ = default__.GetReproducedEncryptionContext(d_1_obj_)
                                if (d_14_valueOrError6_).IsFailure():
                                    return (d_14_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_15_reproducedEncryptionContext_ = (d_14_valueOrError6_).Extract()
                                    d_16_commitmentPolicy_ = AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_11_algorithmSuite_)
                                    d_17_maxPlaintextLength_ = (JSONHelpers.default__.GetPositiveLong(_dafny.Seq("maxPlaintextLength"), d_1_obj_)).ToOption()
                                    source0_ = d_4_typ_
                                    if True:
                                        if (source0_) == (_dafny.Seq("positive-keyring")):
                                            d_18_valueOrError7_ = default__.GetKeyDescription(keys, _dafny.Seq("encryptKeyDescription"), d_1_obj_)
                                            if (d_18_valueOrError7_).IsFailure():
                                                return (d_18_valueOrError7_).PropagateFailure()
                                            elif True:
                                                d_19_encryptKeyDescription_ = (d_18_valueOrError7_).Extract()
                                                d_20_valueOrError8_ = default__.GetKeyDescription(keys, _dafny.Seq("decryptKeyDescription"), d_1_obj_)
                                                if (d_20_valueOrError8_).IsFailure():
                                                    return (d_20_valueOrError8_).PropagateFailure()
                                                elif True:
                                                    d_21_decryptKeyDescription_ = (d_20_valueOrError8_).Extract()
                                                    return Wrappers.Result_Success(TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(name, d_5_description_, d_9_encryptionContext_, d_16_commitmentPolicy_, d_11_algorithmSuite_, d_17_maxPlaintextLength_, d_13_requiredEncryptionContextKeys_, d_19_encryptKeyDescription_, d_21_decryptKeyDescription_, d_15_reproducedEncryptionContext_))
                                    if True:
                                        if (source0_) == (_dafny.Seq("negative-encrypt-keyring")):
                                            d_22_valueOrError9_ = default__.GetKeyDescription(keys, _dafny.Seq("keyDescription"), d_1_obj_)
                                            if (d_22_valueOrError9_).IsFailure():
                                                return (d_22_valueOrError9_).PropagateFailure()
                                            elif True:
                                                d_23_keyDescription_ = (d_22_valueOrError9_).Extract()
                                                d_24_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("errorDescription"), d_1_obj_)
                                                if (d_24_valueOrError10_).IsFailure():
                                                    return (d_24_valueOrError10_).PropagateFailure()
                                                elif True:
                                                    d_25_errorDescription_ = (d_24_valueOrError10_).Extract()
                                                    d_26_valueOrError11_ = Wrappers.default__.Need((d_15_reproducedEncryptionContext_).is_None, _dafny.Seq("reproducedEncryptionContext not supported"))
                                                    if (d_26_valueOrError11_).IsFailure():
                                                        return (d_26_valueOrError11_).PropagateFailure()
                                                    elif True:
                                                        return Wrappers.Result_Success(TestVectors.EncryptTestVector_NegativeEncryptKeyringVector(name, d_5_description_, d_9_encryptionContext_, d_16_commitmentPolicy_, d_11_algorithmSuite_, d_17_maxPlaintextLength_, d_13_requiredEncryptionContextKeys_, d_25_errorDescription_, d_23_keyDescription_))
                                    if True:
                                        if (source0_) == (_dafny.Seq("negative-decrypt-keyring")):
                                            d_27_valueOrError12_ = default__.GetKeyDescription(keys, _dafny.Seq("encryptKeyDescription"), d_1_obj_)
                                            if (d_27_valueOrError12_).IsFailure():
                                                return (d_27_valueOrError12_).PropagateFailure()
                                            elif True:
                                                d_28_encryptKeyDescription_ = (d_27_valueOrError12_).Extract()
                                                d_29_valueOrError13_ = default__.GetKeyDescription(keys, _dafny.Seq("decryptKeyDescription"), d_1_obj_)
                                                if (d_29_valueOrError13_).IsFailure():
                                                    return (d_29_valueOrError13_).PropagateFailure()
                                                elif True:
                                                    d_30_decryptKeyDescription_ = (d_29_valueOrError13_).Extract()
                                                    d_31_valueOrError14_ = JSONHelpers.default__.GetString(_dafny.Seq("decryptErrorDescription"), d_1_obj_)
                                                    if (d_31_valueOrError14_).IsFailure():
                                                        return (d_31_valueOrError14_).PropagateFailure()
                                                    elif True:
                                                        d_32_decryptErrorDescription_ = (d_31_valueOrError14_).Extract()
                                                        return Wrappers.Result_Success(TestVectors.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(name, d_5_description_, d_9_encryptionContext_, d_16_commitmentPolicy_, d_11_algorithmSuite_, d_17_maxPlaintextLength_, d_13_requiredEncryptionContextKeys_, d_32_decryptErrorDescription_, d_28_encryptKeyDescription_, d_30_decryptKeyDescription_, d_15_reproducedEncryptionContext_))
                                    if True:
                                        return Wrappers.Result_Failure((_dafny.Seq("Unsupported EncryptTestVector type:")) + (d_4_typ_))

    @staticmethod
    def GetKeyDescription(keyVectorClient, key, obj):
        d_0_valueOrError0_ = JSONHelpers.default__.Get(key, obj)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_keyDescriptionObject_ = (d_0_valueOrError0_).Extract()
            def lambda0_(d_3_e_):
                return (d_3_e_).ToString()

            d_2_valueOrError1_ = (JSON_API.default__.Serialize(d_1_keyDescriptionObject_)).MapFailure(lambda0_)
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_4_descriptionStr_ = (d_2_valueOrError1_).Extract()
                d_5_valueOrError2_ = ((keyVectorClient).GetKeyDescription(AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionInput_GetKeyDescriptionInput(d_4_descriptionStr_))).MapFailure(default__.ErrorToString)
                if (d_5_valueOrError2_).IsFailure():
                    return (d_5_valueOrError2_).PropagateFailure()
                elif True:
                    d_6_keyDescriptionOutput_ = (d_5_valueOrError2_).Extract()
                    return Wrappers.Result_Success((d_6_keyDescriptionOutput_).keyDescription)

    @staticmethod
    def GetAlgorithmSuiteInfo(obj):
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

                return (AlgorithmSuites.default__.GetAlgorithmSuiteInfo(d_3_binaryId_)).MapFailure(lambda0_(d_1_algorithmSuiteHex_))

    @staticmethod
    def GetRequiredEncryptionContextKeys(obj):
        d_0_keysAsStrings_ = (JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), obj)).ToOption()
        source0_ = d_0_keysAsStrings_
        if True:
            if source0_.is_Some:
                d_1_s_ = source0_.value
                d_2_valueOrError0_ = JSONHelpers.default__.utf8EncodeSeq((d_0_keysAsStrings_).value)
                if (d_2_valueOrError0_).IsFailure():
                    return (d_2_valueOrError0_).PropagateFailure()
                elif True:
                    d_3_k_ = (d_2_valueOrError0_).Extract()
                    return Wrappers.Result_Success(Wrappers.Option_Some(d_3_k_))
        if True:
            return Wrappers.Result_Success(Wrappers.Option_None())

    @staticmethod
    def GetReproducedEncryptionContext(obj):
        d_0_valueOrError0_ = JSONHelpers.default__.GetOptionalSmallObjectToStringStringMap(_dafny.Seq("reproducedEncryptionContext"), obj)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_reproducedEncryptionContextStrings_ = (d_0_valueOrError0_).Extract()
            source0_ = d_1_reproducedEncryptionContextStrings_
            if True:
                if source0_.is_Some:
                    d_2_r_ = source0_.value
                    d_3_valueOrError1_ = JSONHelpers.default__.utf8EncodeMap(d_2_r_)
                    if (d_3_valueOrError1_).IsFailure():
                        return (d_3_valueOrError1_).PropagateFailure()
                    elif True:
                        d_4_e_ = (d_3_valueOrError1_).Extract()
                        return Wrappers.Result_Success(Wrappers.Option_Some(d_4_e_))
            if True:
                return Wrappers.Result_Success(Wrappers.Option_None())

    @staticmethod
    def ErrorToString(e):
        source0_ = e
        if True:
            if source0_.is_KeyVectorException:
                d_0_message_ = source0_.message
                return d_0_message_
        if True:
            if source0_.is_AwsCryptographyMaterialProviders:
                d_1_mplError_ = source0_.AwsCryptographyMaterialProviders
                source1_ = d_1_mplError_
                if True:
                    if source1_.is_AwsCryptographicMaterialProvidersException:
                        d_2_message_ = source1_.message
                        return d_2_message_
                if True:
                    return _dafny.Seq("Unmapped AwsCryptographyMaterialProviders")
        if True:
            return _dafny.Seq("Unmapped KeyVectorException")

    @staticmethod
    def BuildDecryptTestVector(keys, obj):
        hresult_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_i_: int
        d_0_i_ = len(obj)
        d_1_vectors_: _dafny.Seq
        d_1_vectors_ = _dafny.Seq([])
        while (d_0_i_) != (0):
            d_0_i_ = (d_0_i_) - (1)
            d_2_test_: Wrappers.Result
            d_2_test_ = default__.ToDecryptTestVector(keys, ((obj)[d_0_i_])[0], ((obj)[d_0_i_])[1])
            if (d_2_test_).is_Failure:
                hresult_ = Wrappers.Result_Failure((d_2_test_).error)
                return hresult_
            d_1_vectors_ = (_dafny.Seq([(d_2_test_).value])) + (d_1_vectors_)
        hresult_ = Wrappers.Result_Success(d_1_vectors_)
        return hresult_
        return hresult_

    @staticmethod
    def printJson(j):
        hresult_: tuple = ()
        _dafny.print(_dafny.string_of(j))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        hresult_ = ()
        return hresult_
        return hresult_

    @staticmethod
    def GetEncryptedDataKeys(obj):
        d_0_valueOrError0_ = JSONHelpers.default__.GetArray(_dafny.Seq("encryptedDataKeys"), obj)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_encryptedDataKeysJson_ = (d_0_valueOrError0_).Extract()
            return Seq.default__.MapWithResult(default__.GetEncryptedDataKey, d_1_encryptedDataKeysJson_)

    @staticmethod
    def GetEncryptedDataKey(json):
        d_0_valueOrError0_ = Wrappers.default__.Need((json).is_Object, _dafny.Seq("Encrypted data key is not an object"))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_valueOrError1_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderId"), (json).obj)
            if (d_1_valueOrError1_).IsFailure():
                return (d_1_valueOrError1_).PropagateFailure()
            elif True:
                d_2_keyProviderId_ = (d_1_valueOrError1_).Extract()
                d_3_valueOrError2_ = JSONHelpers.default__.GetString(_dafny.Seq("keyProviderInfo"), (json).obj)
                if (d_3_valueOrError2_).IsFailure():
                    return (d_3_valueOrError2_).PropagateFailure()
                elif True:
                    d_4_keyProviderInfo_ = (d_3_valueOrError2_).Extract()
                    d_5_valueOrError3_ = JSONHelpers.default__.GetString(_dafny.Seq("ciphertext"), (json).obj)
                    if (d_5_valueOrError3_).IsFailure():
                        return (d_5_valueOrError3_).PropagateFailure()
                    elif True:
                        d_6_ciphertext_ = (d_5_valueOrError3_).Extract()
                        d_7_valueOrError4_ = UTF8.default__.Encode(d_2_keyProviderId_)
                        if (d_7_valueOrError4_).IsFailure():
                            return (d_7_valueOrError4_).PropagateFailure()
                        elif True:
                            d_8_keyProviderId_ = (d_7_valueOrError4_).Extract()
                            d_9_valueOrError5_ = Base64.default__.Decode(d_4_keyProviderInfo_)
                            if (d_9_valueOrError5_).IsFailure():
                                return (d_9_valueOrError5_).PropagateFailure()
                            elif True:
                                d_10_keyProviderInfo_ = (d_9_valueOrError5_).Extract()
                                d_11_valueOrError6_ = Base64.default__.Decode(d_6_ciphertext_)
                                if (d_11_valueOrError6_).IsFailure():
                                    return (d_11_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_12_ciphertext_ = (d_11_valueOrError6_).Extract()
                                    return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(d_8_keyProviderId_, d_10_keyProviderInfo_, d_12_ciphertext_))

    @staticmethod
    def GetExpectedResult(obj):
        d_0_valueOrError0_ = JSONHelpers.default__.GetObject(_dafny.Seq("result"), obj)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_result_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("plaintextDataKey"), d_1_result_)
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_plaintextDataKey_ = (d_2_valueOrError1_).Extract()
                d_4_valueOrError2_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("symmetricSigningKey"), d_1_result_)
                if (d_4_valueOrError2_).IsFailure():
                    return (d_4_valueOrError2_).PropagateFailure()
                elif True:
                    d_5_symmetricSigningKey_ = (d_4_valueOrError2_).Extract()
                    d_6_valueOrError3_ = JSONHelpers.default__.GetArrayString(_dafny.Seq("requiredEncryptionContextKeys"), d_1_result_)
                    if (d_6_valueOrError3_).IsFailure():
                        return (d_6_valueOrError3_).PropagateFailure()
                    elif True:
                        d_7_requiredEncryptionContextKeys_ = (d_6_valueOrError3_).Extract()
                        def iife0_(_pat_let22_0):
                            def iife1_(d_9_valueOrError5_):
                                def iife2_(_pat_let23_0):
                                    def iife3_(d_10_p_):
                                        return Wrappers.Result_Success(Wrappers.Option_Some(d_10_p_))
                                    return iife3_(_pat_let23_0)
                                return ((d_9_valueOrError5_).PropagateFailure() if (d_9_valueOrError5_).IsFailure() else iife2_((d_9_valueOrError5_).Extract()))
                            return iife1_(_pat_let22_0)
                        d_8_valueOrError4_ = (iife0_(Base64.default__.Decode((d_3_plaintextDataKey_).value)) if (d_3_plaintextDataKey_).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                        if (d_8_valueOrError4_).IsFailure():
                            return (d_8_valueOrError4_).PropagateFailure()
                        elif True:
                            d_11_plaintextDataKey_ = (d_8_valueOrError4_).Extract()
                            def iife4_(_pat_let24_0):
                                def iife5_(d_13_valueOrError7_):
                                    def iife6_(_pat_let25_0):
                                        def iife7_(d_14_p_):
                                            return Wrappers.Result_Success(Wrappers.Option_Some(d_14_p_))
                                        return iife7_(_pat_let25_0)
                                    return ((d_13_valueOrError7_).PropagateFailure() if (d_13_valueOrError7_).IsFailure() else iife6_((d_13_valueOrError7_).Extract()))
                                return iife5_(_pat_let24_0)
                            d_12_valueOrError6_ = (iife4_(Base64.default__.Decode((d_5_symmetricSigningKey_).value)) if (d_5_symmetricSigningKey_).is_Some else Wrappers.Result_Success(Wrappers.Option_None()))
                            if (d_12_valueOrError6_).IsFailure():
                                return (d_12_valueOrError6_).PropagateFailure()
                            elif True:
                                d_15_symmetricSigningKey_ = (d_12_valueOrError6_).Extract()
                                d_16_valueOrError8_ = JSONHelpers.default__.utf8EncodeSeq(d_7_requiredEncryptionContextKeys_)
                                if (d_16_valueOrError8_).IsFailure():
                                    return (d_16_valueOrError8_).PropagateFailure()
                                elif True:
                                    d_17_requiredEncryptionContextKeys_ = (d_16_valueOrError8_).Extract()
                                    return Wrappers.Result_Success(TestVectors.DecryptResult_DecryptResult(d_11_plaintextDataKey_, d_15_symmetricSigningKey_, d_17_requiredEncryptionContextKeys_))

    @staticmethod
    def ToDecryptTestVector(keys, name, json):
        d_0_valueOrError0_ = Wrappers.default__.Need((json).is_Object, _dafny.Seq("DecryptTestVector not an object"))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_obj_ = (json).obj
            d_2_typString_ = _dafny.Seq("type")
            d_3_valueOrError1_ = JSONHelpers.default__.GetString(d_2_typString_, d_1_obj_)
            if (d_3_valueOrError1_).IsFailure():
                return (d_3_valueOrError1_).PropagateFailure()
            elif True:
                d_4_typ_ = (d_3_valueOrError1_).Extract()
                d_5_valueOrError2_ = JSONHelpers.default__.GetOptionalString(_dafny.Seq("description"), d_1_obj_)
                if (d_5_valueOrError2_).IsFailure():
                    return (d_5_valueOrError2_).PropagateFailure()
                elif True:
                    d_6_description_ = (d_5_valueOrError2_).Extract()
                    d_7_valueOrError3_ = JSONHelpers.default__.SmallObjectToStringStringMap(_dafny.Seq("encryptionContext"), d_1_obj_)
                    if (d_7_valueOrError3_).IsFailure():
                        return (d_7_valueOrError3_).PropagateFailure()
                    elif True:
                        d_8_encryptionContextStrings_ = (d_7_valueOrError3_).Extract()
                        d_9_valueOrError4_ = JSONHelpers.default__.utf8EncodeMap(d_8_encryptionContextStrings_)
                        if (d_9_valueOrError4_).IsFailure():
                            return (d_9_valueOrError4_).PropagateFailure()
                        elif True:
                            d_10_encryptionContext_ = (d_9_valueOrError4_).Extract()
                            d_11_valueOrError5_ = default__.GetAlgorithmSuiteInfo(d_1_obj_)
                            if (d_11_valueOrError5_).IsFailure():
                                return (d_11_valueOrError5_).PropagateFailure()
                            elif True:
                                d_12_algorithmSuite_ = (d_11_valueOrError5_).Extract()
                                d_13_valueOrError6_ = default__.GetReproducedEncryptionContext(d_1_obj_)
                                if (d_13_valueOrError6_).IsFailure():
                                    return (d_13_valueOrError6_).PropagateFailure()
                                elif True:
                                    d_14_reproducedEncryptionContext_ = (d_13_valueOrError6_).Extract()
                                    d_15_commitmentPolicy_ = AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_12_algorithmSuite_)
                                    d_16_valueOrError7_ = default__.GetKeyDescription(keys, _dafny.Seq("keyDescription"), d_1_obj_)
                                    if (d_16_valueOrError7_).IsFailure():
                                        return (d_16_valueOrError7_).PropagateFailure()
                                    elif True:
                                        d_17_keyDescription_ = (d_16_valueOrError7_).Extract()
                                        d_18_valueOrError8_ = default__.GetEncryptedDataKeys(d_1_obj_)
                                        if (d_18_valueOrError8_).IsFailure():
                                            return (d_18_valueOrError8_).PropagateFailure()
                                        elif True:
                                            d_19_encryptedDataKeys_ = (d_18_valueOrError8_).Extract()
                                            source0_ = d_4_typ_
                                            if True:
                                                if (source0_) == (_dafny.Seq("positive-keyring")):
                                                    d_20_valueOrError9_ = default__.GetExpectedResult(d_1_obj_)
                                                    if (d_20_valueOrError9_).IsFailure():
                                                        return (d_20_valueOrError9_).PropagateFailure()
                                                    elif True:
                                                        d_21_expectedResult_ = (d_20_valueOrError9_).Extract()
                                                        return Wrappers.Result_Success(TestVectors.DecryptTestVector_PositiveDecryptKeyringTest(name, d_12_algorithmSuite_, d_15_commitmentPolicy_, d_19_encryptedDataKeys_, d_10_encryptionContext_, d_17_keyDescription_, d_21_expectedResult_, d_6_description_, d_14_reproducedEncryptionContext_))
                                            if True:
                                                if (source0_) == (_dafny.Seq("negative-keyring")):
                                                    d_22_valueOrError10_ = JSONHelpers.default__.GetString(_dafny.Seq("errorDescription"), d_1_obj_)
                                                    if (d_22_valueOrError10_).IsFailure():
                                                        return (d_22_valueOrError10_).PropagateFailure()
                                                    elif True:
                                                        d_23_errorDescription_ = (d_22_valueOrError10_).Extract()
                                                        return Wrappers.Result_Success(TestVectors.DecryptTestVector_NegativeDecryptKeyringTest(name, d_12_algorithmSuite_, d_15_commitmentPolicy_, d_19_encryptedDataKeys_, d_10_encryptionContext_, d_23_errorDescription_, d_17_keyDescription_, d_14_reproducedEncryptionContext_, d_6_description_))
                                            if True:
                                                return Wrappers.Result_Failure((_dafny.Seq("Unsupported DecryptTestVector type:")) + (d_4_typ_))

