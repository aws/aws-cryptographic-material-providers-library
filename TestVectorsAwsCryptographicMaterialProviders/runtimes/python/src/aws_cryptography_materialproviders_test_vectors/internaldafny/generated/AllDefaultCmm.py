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

# Module: AllDefaultCmm

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def SubSets(ec, keys):
        if (len(ec)) == (0):
            return _dafny.Set({_dafny.Map({})})
        elif True:
            d_0_subsets_ = default__.SubSets((ec) - (_dafny.Set({(keys)[0]})), _dafny.Seq((keys)[1::]))
            def iife0_():
                coll0_ = _dafny.Set()
                compr_0_: _dafny.Map
                for compr_0_ in (d_0_subsets_).Elements:
                    d_1_s_: _dafny.Map = compr_0_
                    if (d_1_s_) in (d_0_subsets_):
                        coll0_ = coll0_.union(_dafny.Set([(d_1_s_) | (_dafny.Map({(keys)[0]: (ec)[(keys)[0]]}))]))
                return _dafny.Set(coll0_)
            return (d_0_subsets_) | (iife0_()
            )

    @_dafny.classproperty
    def AesKey(instance):
        return (AllRawAES.default__.aesPersistentKeyNames)[(len(AllRawAES.default__.aesPersistentKeyNames)) - (1)]
    @_dafny.classproperty
    def RawAesKeyring(instance):
        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_AES(AwsCryptographyMaterialProvidersTestVectorKeysTypes.RawAES_RawAES(default__.AesKey, (_dafny.Seq("aws-raw-vectors-persistent-")) + (default__.AesKey)))
    @_dafny.classproperty
    def a(instance):
        return (UTF8.default__.Encode(_dafny.Seq("a"))).value
    @_dafny.classproperty
    def b(instance):
        return (UTF8.default__.Encode(_dafny.Seq("b"))).value
    @_dafny.classproperty
    def rootEncryptionContext(instance):
        return _dafny.Map({default__.a: default__.a, default__.b: default__.b})
    @_dafny.classproperty
    def encryptionContextsToTest(instance):
        return _dafny.Set({default__.rootEncryptionContext})
    @_dafny.classproperty
    def c(instance):
        return (UTF8.default__.Encode(_dafny.Seq("c"))).value
    @_dafny.classproperty
    def disjointEncryptionContext(instance):
        return _dafny.Map({default__.a: default__.c, default__.b: default__.c, default__.c: default__.c})
    @_dafny.classproperty
    def StaticAlgorithmSuite(instance):
        return AlgorithmSuites.default__.GetESDKSuite(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF())
    @_dafny.classproperty
    def SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext(instance):
        def iife0_():
            def iife2_():
                def lambda3_(d_1_a_, d_2_b_):
                    return (d_1_a_) < (d_2_b_)

                coll2_ = _dafny.Set()
                def lambda2_(d_1_a_, d_2_b_):
                    return (d_1_a_) < (d_2_b_)

                compr_3_: _dafny.Map
                for compr_3_ in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda2_))).Elements:
                    d_5_s_: _dafny.Map = compr_3_
                    if (d_5_s_) in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda3_))):
                        coll2_ = coll2_.union(_dafny.Set([(d_5_s_).keys]))
                return _dafny.Set(coll2_)
            def iife4_():
                def lambda7_(d_6_a_, d_7_b_):
                    return (d_6_a_) < (d_7_b_)

                coll4_ = _dafny.Set()
                def lambda6_(d_6_a_, d_7_b_):
                    return (d_6_a_) < (d_7_b_)

                compr_6_: _dafny.Map
                for compr_6_ in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda6_))).Elements:
                    d_10_s_: _dafny.Map = compr_6_
                    if ((d_10_s_) in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda7_)))) and ((((d_10_s_).keys).intersection(d_4_requiredEncryptionContextKeys_)) == (d_4_requiredEncryptionContextKeys_)):
                        coll4_ = coll4_.union(_dafny.Set([d_10_s_]))
                return _dafny.Set(coll4_)
            coll0_ = _dafny.Set()
            compr_0_: _dafny.Map
            for compr_0_ in (default__.encryptionContextsToTest).Elements:
                d_0_encryptionContext_: _dafny.Map = compr_0_
                if (d_0_encryptionContext_) in (default__.encryptionContextsToTest):
                    def iife1_():
                        def lambda1_(d_1_a_, d_2_b_):
                            return (d_1_a_) < (d_2_b_)

                        coll1_ = _dafny.Set()
                        def lambda0_(d_1_a_, d_2_b_):
                            return (d_1_a_) < (d_2_b_)

                        compr_2_: _dafny.Map
                        for compr_2_ in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda0_))).Elements:
                            d_3_s_: _dafny.Map = compr_2_
                            if (d_3_s_) in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda1_))):
                                coll1_ = coll1_.union(_dafny.Set([(d_3_s_).keys]))
                        return _dafny.Set(coll1_)
                    compr_1_: _dafny.Set
                    for compr_1_ in (iife1_()
                    ).Elements:
                        d_4_requiredEncryptionContextKeys_: _dafny.Set = compr_1_
                        if (d_4_requiredEncryptionContextKeys_) in (iife2_()
                        ):
                            def iife3_():
                                def lambda5_(d_6_a_, d_7_b_):
                                    return (d_6_a_) < (d_7_b_)

                                coll3_ = _dafny.Set()
                                def lambda4_(d_6_a_, d_7_b_):
                                    return (d_6_a_) < (d_7_b_)

                                compr_5_: _dafny.Map
                                for compr_5_ in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda4_))).Elements:
                                    d_8_s_: _dafny.Map = compr_5_
                                    if ((d_8_s_) in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda5_)))) and ((((d_8_s_).keys).intersection(d_4_requiredEncryptionContextKeys_)) == (d_4_requiredEncryptionContextKeys_)):
                                        coll3_ = coll3_.union(_dafny.Set([d_8_s_]))
                                return _dafny.Set(coll3_)
                            compr_4_: _dafny.Map
                            for compr_4_ in (iife3_()
                            ).Elements:
                                d_9_reproducedEncryptionContext_: _dafny.Map = compr_4_
                                if (d_9_reproducedEncryptionContext_) in (iife4_()
                                ):
                                    def lambda8_(d_11_a_, d_12_b_):
                                        return (d_11_a_) < (d_12_b_)

                                    coll0_ = coll0_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(_dafny.Seq("Success testing requiredEncryptionContextKeys/reproducedEncryptionContext"), Wrappers.Option_None(), d_0_encryptionContext_, AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_Some(SortedSets.default__.SetToOrderedSequence2(d_4_requiredEncryptionContextKeys_, lambda8_)), default__.RawAesKeyring, default__.RawAesKeyring, Wrappers.Option_Some(d_9_reproducedEncryptionContext_))]))
            return _dafny.Set(coll0_)
        return iife0_()
        
    @_dafny.classproperty
    def FailureBadReproducedEncryptionContext(instance):
        def iife0_():
            def iife2_():
                def lambda3_(d_1_a_, d_2_b_):
                    return (d_1_a_) < (d_2_b_)

                coll2_ = _dafny.Set()
                def lambda2_(d_1_a_, d_2_b_):
                    return (d_1_a_) < (d_2_b_)

                compr_3_: _dafny.Map
                for compr_3_ in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda2_))).Elements:
                    d_5_s_: _dafny.Map = compr_3_
                    if (d_5_s_) in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda3_))):
                        coll2_ = coll2_.union(_dafny.Set([(d_5_s_).keys]))
                return _dafny.Set(coll2_)
            def iife4_():
                def lambda7_(d_6_a_, d_7_b_):
                    return (d_6_a_) < (d_7_b_)

                coll4_ = _dafny.Set()
                def lambda6_(d_6_a_, d_7_b_):
                    return (d_6_a_) < (d_7_b_)

                compr_6_: _dafny.Map
                for compr_6_ in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda6_))).Elements:
                    d_10_s_: _dafny.Map = compr_6_
                    if ((d_10_s_) in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda7_)))) and ((d_10_s_) != (_dafny.Map({}))):
                        coll4_ = coll4_.union(_dafny.Set([d_10_s_]))
                return _dafny.Set(coll4_)
            def iife6_():
                def lambda11_(d_11_a_, d_12_b_):
                    return (d_11_a_) < (d_12_b_)

                coll6_ = _dafny.Set()
                def lambda10_(d_11_a_, d_12_b_):
                    return (d_11_a_) < (d_12_b_)

                compr_9_: _dafny.Map
                for compr_9_ in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda10_))).Elements:
                    d_15_s_: _dafny.Map = compr_9_
                    if (d_15_s_) in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda11_))):
                        coll6_ = coll6_.union(_dafny.Set([(d_15_s_) | (d_9_incorrectEncryptionContext_)]))
                return _dafny.Set(coll6_)
            coll0_ = _dafny.Set()
            compr_0_: _dafny.Map
            for compr_0_ in (default__.encryptionContextsToTest).Elements:
                d_0_encryptionContext_: _dafny.Map = compr_0_
                if (d_0_encryptionContext_) in (default__.encryptionContextsToTest):
                    def iife1_():
                        def lambda1_(d_1_a_, d_2_b_):
                            return (d_1_a_) < (d_2_b_)

                        coll1_ = _dafny.Set()
                        def lambda0_(d_1_a_, d_2_b_):
                            return (d_1_a_) < (d_2_b_)

                        compr_2_: _dafny.Map
                        for compr_2_ in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda0_))).Elements:
                            d_3_s_: _dafny.Map = compr_2_
                            if (d_3_s_) in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda1_))):
                                coll1_ = coll1_.union(_dafny.Set([(d_3_s_).keys]))
                        return _dafny.Set(coll1_)
                    compr_1_: _dafny.Set
                    for compr_1_ in (iife1_()
                    ).Elements:
                        d_4_requiredEncryptionContextKeys_: _dafny.Set = compr_1_
                        if (d_4_requiredEncryptionContextKeys_) in (iife2_()
                        ):
                            def iife3_():
                                def lambda5_(d_6_a_, d_7_b_):
                                    return (d_6_a_) < (d_7_b_)

                                coll3_ = _dafny.Set()
                                def lambda4_(d_6_a_, d_7_b_):
                                    return (d_6_a_) < (d_7_b_)

                                compr_5_: _dafny.Map
                                for compr_5_ in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda4_))).Elements:
                                    d_8_s_: _dafny.Map = compr_5_
                                    if ((d_8_s_) in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda5_)))) and ((d_8_s_) != (_dafny.Map({}))):
                                        coll3_ = coll3_.union(_dafny.Set([d_8_s_]))
                                return _dafny.Set(coll3_)
                            compr_4_: _dafny.Map
                            for compr_4_ in (iife3_()
                            ).Elements:
                                d_9_incorrectEncryptionContext_: _dafny.Map = compr_4_
                                if (d_9_incorrectEncryptionContext_) in (iife4_()
                                ):
                                    def iife5_():
                                        def lambda9_(d_11_a_, d_12_b_):
                                            return (d_11_a_) < (d_12_b_)

                                        coll5_ = _dafny.Set()
                                        def lambda8_(d_11_a_, d_12_b_):
                                            return (d_11_a_) < (d_12_b_)

                                        compr_8_: _dafny.Map
                                        for compr_8_ in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda8_))).Elements:
                                            d_13_s_: _dafny.Map = compr_8_
                                            if (d_13_s_) in (default__.SubSets(d_0_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_0_encryptionContext_).keys, lambda9_))):
                                                coll5_ = coll5_.union(_dafny.Set([(d_13_s_) | (d_9_incorrectEncryptionContext_)]))
                                        return _dafny.Set(coll5_)
                                    compr_7_: _dafny.Map
                                    for compr_7_ in (iife5_()
                                    ).Elements:
                                        d_14_reproducedEncryptionContext_: _dafny.Map = compr_7_
                                        if (d_14_reproducedEncryptionContext_) in (iife6_()
                                        ):
                                            def lambda12_(d_16_a_, d_17_b_):
                                                return (d_16_a_) < (d_17_b_)

                                            coll0_ = coll0_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(_dafny.Seq("Failure of reproducedEncryptionContext"), Wrappers.Option_None(), d_0_encryptionContext_, AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_Some(SortedSets.default__.SetToOrderedSequence2(d_4_requiredEncryptionContextKeys_, lambda12_)), _dafny.Seq("The reproducedEncryptionContext is not correct"), default__.RawAesKeyring, default__.RawAesKeyring, Wrappers.Option_Some(d_14_reproducedEncryptionContext_))]))
            return _dafny.Set(coll0_)
        return iife0_()
        
    @_dafny.classproperty
    def StaticPlaintextDataKey(instance):
        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Static(AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring_StaticKeyring(_dafny.Seq("static-plaintext-data-key")))
    @_dafny.classproperty
    def d(instance):
        return _dafny.Seq([240, 144, 128, 130])
    @_dafny.classproperty
    def StaticNotPlaintextDataKey(instance):
        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Static(AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring_StaticKeyring(_dafny.Seq("no-plaintext-data-key")))
    @_dafny.classproperty
    def Tests(instance):
        return (((_dafny.Set({})) | (_dafny.Set({TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(_dafny.Seq("Simplest possible happy path"), Wrappers.Option_None(), _dafny.Map({}), AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_None(), default__.StaticPlaintextDataKey, default__.StaticPlaintextDataKey, Wrappers.Option_None()), TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(_dafny.Seq("SurrogatePair Encryption Context Test"), Wrappers.Option_None(), _dafny.Map({default__.d: default__.d}), AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_None(), default__.RawAesKeyring, default__.RawAesKeyring, Wrappers.Option_None()), TestVectors.EncryptTestVector_NegativeEncryptKeyringVector(_dafny.Seq("Missing plaintext data key on decrypt"), Wrappers.Option_None(), _dafny.Map({}), AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_None(), _dafny.Seq("No plaintext data key on encrypt fails"), default__.StaticNotPlaintextDataKey), TestVectors.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(_dafny.Seq("Missing plaintext data key on decrypt"), Wrappers.Option_None(), _dafny.Map({}), AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_None(), _dafny.Seq("No plaintext data key on encrypt fails"), default__.StaticPlaintextDataKey, default__.StaticNotPlaintextDataKey, Wrappers.Option_None())}))) | (default__.FailureBadReproducedEncryptionContext)) | (default__.SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext)
