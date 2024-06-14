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
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws as Com_Amazonaws
import com_amazonaws_dynamodb.internaldafny.generated.Com as Com
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
import standard_library.internaldafny.generated.UUID as UUID
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialProviders as MaterialProviders
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
import standard_library.internaldafny.generated.JSON_Utils_Views as JSON_Utils_Views
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Lexers as JSON_Utils_Lexers
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import standard_library.internaldafny.generated.JSON_Utils as JSON_Utils
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
import standard_library.internaldafny.generated.JSON_ConcreteSyntax as JSON_ConcreteSyntax
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
import standard_library.internaldafny.generated.JSON_ZeroCopy as JSON_ZeroCopy
import standard_library.internaldafny.generated.JSON_API as JSON_API
import standard_library.internaldafny.generated.JSON as JSON
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.JSONHelpers as JSONHelpers
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyDescription as KeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyMaterial as KeyMaterial
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CreateStaticKeyrings as CreateStaticKeyrings
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CreateStaticKeyStores as CreateStaticKeyStores
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyringFromKeyDescription as KeyringFromKeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CmmFromKeyDescription as CmmFromKeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeysVectorOperations as KeysVectorOperations
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyVectors as KeyVectors
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.TestVectors as TestVectors
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllHierarchy as AllHierarchy
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllKms as AllKms
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllKmsMrkAware as AllKmsMrkAware
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllKmsMrkAwareDiscovery as AllKmsMrkAwareDiscovery
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllKmsRsa as AllKmsRsa
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRawAES as AllRawAES
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRawRSA as AllRawRSA

# Module: aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllDefaultCmm

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def SubSets(ec, keys):
        if (len(ec)) == (0):
            return _dafny.Set({_dafny.Map({})})
        elif True:
            d_717_subsets_ = default__.SubSets((ec) - (_dafny.Set({(keys)[0]})), _dafny.Seq((keys)[1::]))
            def iife55_():
                coll23_ = _dafny.Set()
                compr_41_: _dafny.Map
                for compr_41_ in (d_717_subsets_).Elements:
                    d_718_s_: _dafny.Map = compr_41_
                    if (d_718_s_) in (d_717_subsets_):
                        coll23_ = coll23_.union(_dafny.Set([(d_718_s_) | (_dafny.Map({(keys)[0]: (ec)[(keys)[0]]}))]))
                return _dafny.Set(coll23_)
            return (d_717_subsets_) | (iife55_()
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
        def iife56_():
            def iife59_():
                def lambda61_(d_720_a_, d_721_b_):
                    return (d_720_a_) < (d_721_b_)

                coll27_ = _dafny.Set()
                def lambda60_(d_720_a_, d_721_b_):
                    return (d_720_a_) < (d_721_b_)

                compr_47_: _dafny.Map
                for compr_47_ in (default__.SubSets(d_719_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_719_encryptionContext_).keys, lambda60_))).Elements:
                    d_728_s_: _dafny.Map = compr_47_
                    if (d_728_s_) in (default__.SubSets(d_719_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_719_encryptionContext_).keys, lambda61_))):
                        coll27_ = coll27_.union(_dafny.Set([(d_728_s_).keys]))
                return _dafny.Set(coll27_)
            def iife60_():
                def lambda63_(d_724_a_, d_725_b_):
                    return (d_724_a_) < (d_725_b_)

                coll28_ = _dafny.Set()
                def lambda62_(d_724_a_, d_725_b_):
                    return (d_724_a_) < (d_725_b_)

                compr_48_: _dafny.Map
                for compr_48_ in (default__.SubSets(d_719_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_719_encryptionContext_).keys, lambda62_))).Elements:
                    d_729_s_: _dafny.Map = compr_48_
                    if ((d_729_s_) in (default__.SubSets(d_719_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_719_encryptionContext_).keys, lambda63_)))) and ((((d_729_s_).keys).intersection(d_723_requiredEncryptionContextKeys_)) == (d_723_requiredEncryptionContextKeys_)):
                        coll28_ = coll28_.union(_dafny.Set([d_729_s_]))
                return _dafny.Set(coll28_)
            coll24_ = _dafny.Set()
            compr_42_: _dafny.Map
            for compr_42_ in (default__.encryptionContextsToTest).Elements:
                d_719_encryptionContext_: _dafny.Map = compr_42_
                def iife57_():
                    def lambda57_(d_720_a_, d_721_b_):
                        return (d_720_a_) < (d_721_b_)

                    coll25_ = _dafny.Set()
                    def lambda56_(d_720_a_, d_721_b_):
                        return (d_720_a_) < (d_721_b_)

                    compr_44_: _dafny.Map
                    for compr_44_ in (default__.SubSets(d_719_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_719_encryptionContext_).keys, lambda56_))).Elements:
                        d_722_s_: _dafny.Map = compr_44_
                        if (d_722_s_) in (default__.SubSets(d_719_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_719_encryptionContext_).keys, lambda57_))):
                            coll25_ = coll25_.union(_dafny.Set([(d_722_s_).keys]))
                    return _dafny.Set(coll25_)
                compr_43_: _dafny.Set
                for compr_43_ in (iife57_()
                ).Elements:
                    d_723_requiredEncryptionContextKeys_: _dafny.Set = compr_43_
                    def iife58_():
                        def lambda59_(d_724_a_, d_725_b_):
                            return (d_724_a_) < (d_725_b_)

                        coll26_ = _dafny.Set()
                        def lambda58_(d_724_a_, d_725_b_):
                            return (d_724_a_) < (d_725_b_)

                        compr_46_: _dafny.Map
                        for compr_46_ in (default__.SubSets(d_719_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_719_encryptionContext_).keys, lambda58_))).Elements:
                            d_726_s_: _dafny.Map = compr_46_
                            if ((d_726_s_) in (default__.SubSets(d_719_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_719_encryptionContext_).keys, lambda59_)))) and ((((d_726_s_).keys).intersection(d_723_requiredEncryptionContextKeys_)) == (d_723_requiredEncryptionContextKeys_)):
                                coll26_ = coll26_.union(_dafny.Set([d_726_s_]))
                        return _dafny.Set(coll26_)
                    compr_45_: _dafny.Map
                    for compr_45_ in (iife58_()
                    ).Elements:
                        d_727_reproducedEncryptionContext_: _dafny.Map = compr_45_
                        if (((d_719_encryptionContext_) in (default__.encryptionContextsToTest)) and ((d_723_requiredEncryptionContextKeys_) in (iife59_()
                        ))) and ((d_727_reproducedEncryptionContext_) in (iife60_()
                        )):
                            coll24_ = coll24_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(_dafny.Seq("Success testing requiredEncryptionContextKeys/reproducedEncryptionContext"), Wrappers.Option_None(), d_719_encryptionContext_, AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_Some(SortedSets.default__.SetToSequence(d_723_requiredEncryptionContextKeys_)), default__.RawAesKeyring, default__.RawAesKeyring, Wrappers.Option_Some(d_727_reproducedEncryptionContext_))]))
            return _dafny.Set(coll24_)
        return iife56_()
        
    @_dafny.classproperty
    def FailureBadReproducedEncryptionContext(instance):
        def iife61_():
            def iife65_():
                def lambda71_(d_731_a_, d_732_b_):
                    return (d_731_a_) < (d_732_b_)

                coll33_ = _dafny.Set()
                def lambda70_(d_731_a_, d_732_b_):
                    return (d_731_a_) < (d_732_b_)

                compr_56_: _dafny.Map
                for compr_56_ in (default__.SubSets(d_730_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_730_encryptionContext_).keys, lambda70_))).Elements:
                    d_743_s_: _dafny.Map = compr_56_
                    if (d_743_s_) in (default__.SubSets(d_730_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_730_encryptionContext_).keys, lambda71_))):
                        coll33_ = coll33_.union(_dafny.Set([(d_743_s_).keys]))
                return _dafny.Set(coll33_)
            def iife66_():
                def lambda73_(d_735_a_, d_736_b_):
                    return (d_735_a_) < (d_736_b_)

                coll34_ = _dafny.Set()
                def lambda72_(d_735_a_, d_736_b_):
                    return (d_735_a_) < (d_736_b_)

                compr_57_: _dafny.Map
                for compr_57_ in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda72_))).Elements:
                    d_744_s_: _dafny.Map = compr_57_
                    if ((d_744_s_) in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda73_)))) and ((d_744_s_) != (_dafny.Map({}))):
                        coll34_ = coll34_.union(_dafny.Set([d_744_s_]))
                return _dafny.Set(coll34_)
            def iife67_():
                def lambda75_(d_739_a_, d_740_b_):
                    return (d_739_a_) < (d_740_b_)

                coll35_ = _dafny.Set()
                def lambda74_(d_739_a_, d_740_b_):
                    return (d_739_a_) < (d_740_b_)

                compr_58_: _dafny.Map
                for compr_58_ in (default__.SubSets(d_730_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_730_encryptionContext_).keys, lambda74_))).Elements:
                    d_745_s_: _dafny.Map = compr_58_
                    if (d_745_s_) in (default__.SubSets(d_730_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_730_encryptionContext_).keys, lambda75_))):
                        coll35_ = coll35_.union(_dafny.Set([(d_745_s_) | (d_738_incorrectEncryptionContext_)]))
                return _dafny.Set(coll35_)
            coll29_ = _dafny.Set()
            compr_49_: _dafny.Map
            for compr_49_ in (default__.encryptionContextsToTest).Elements:
                d_730_encryptionContext_: _dafny.Map = compr_49_
                def iife62_():
                    def lambda65_(d_731_a_, d_732_b_):
                        return (d_731_a_) < (d_732_b_)

                    coll30_ = _dafny.Set()
                    def lambda64_(d_731_a_, d_732_b_):
                        return (d_731_a_) < (d_732_b_)

                    compr_51_: _dafny.Map
                    for compr_51_ in (default__.SubSets(d_730_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_730_encryptionContext_).keys, lambda64_))).Elements:
                        d_733_s_: _dafny.Map = compr_51_
                        if (d_733_s_) in (default__.SubSets(d_730_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_730_encryptionContext_).keys, lambda65_))):
                            coll30_ = coll30_.union(_dafny.Set([(d_733_s_).keys]))
                    return _dafny.Set(coll30_)
                compr_50_: _dafny.Set
                for compr_50_ in (iife62_()
                ).Elements:
                    d_734_requiredEncryptionContextKeys_: _dafny.Set = compr_50_
                    def iife63_():
                        def lambda67_(d_735_a_, d_736_b_):
                            return (d_735_a_) < (d_736_b_)

                        coll31_ = _dafny.Set()
                        def lambda66_(d_735_a_, d_736_b_):
                            return (d_735_a_) < (d_736_b_)

                        compr_53_: _dafny.Map
                        for compr_53_ in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda66_))).Elements:
                            d_737_s_: _dafny.Map = compr_53_
                            if ((d_737_s_) in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda67_)))) and ((d_737_s_) != (_dafny.Map({}))):
                                coll31_ = coll31_.union(_dafny.Set([d_737_s_]))
                        return _dafny.Set(coll31_)
                    compr_52_: _dafny.Map
                    for compr_52_ in (iife63_()
                    ).Elements:
                        d_738_incorrectEncryptionContext_: _dafny.Map = compr_52_
                        def iife64_():
                            def lambda69_(d_739_a_, d_740_b_):
                                return (d_739_a_) < (d_740_b_)

                            coll32_ = _dafny.Set()
                            def lambda68_(d_739_a_, d_740_b_):
                                return (d_739_a_) < (d_740_b_)

                            compr_55_: _dafny.Map
                            for compr_55_ in (default__.SubSets(d_730_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_730_encryptionContext_).keys, lambda68_))).Elements:
                                d_741_s_: _dafny.Map = compr_55_
                                if (d_741_s_) in (default__.SubSets(d_730_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_730_encryptionContext_).keys, lambda69_))):
                                    coll32_ = coll32_.union(_dafny.Set([(d_741_s_) | (d_738_incorrectEncryptionContext_)]))
                            return _dafny.Set(coll32_)
                        compr_54_: _dafny.Map
                        for compr_54_ in (iife64_()
                        ).Elements:
                            d_742_reproducedEncryptionContext_: _dafny.Map = compr_54_
                            if ((((d_730_encryptionContext_) in (default__.encryptionContextsToTest)) and ((d_734_requiredEncryptionContextKeys_) in (iife65_()
                            ))) and ((d_738_incorrectEncryptionContext_) in (iife66_()
                            ))) and ((d_742_reproducedEncryptionContext_) in (iife67_()
                            )):
                                coll29_ = coll29_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(_dafny.Seq("Failure of reproducedEncryptionContext"), Wrappers.Option_None(), d_730_encryptionContext_, AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_Some(SortedSets.default__.SetToSequence(d_734_requiredEncryptionContextKeys_)), _dafny.Seq("The reproducedEncryptionContext is not correct"), default__.RawAesKeyring, default__.RawAesKeyring, Wrappers.Option_Some(d_742_reproducedEncryptionContext_))]))
            return _dafny.Set(coll29_)
        return iife61_()
        
    @_dafny.classproperty
    def StaticPlaintextDataKey(instance):
        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Static(AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring_StaticKeyring(_dafny.Seq("static-plaintext-data-key")))
    @_dafny.classproperty
    def StaticNotPlaintextDataKey(instance):
        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Static(AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring_StaticKeyring(_dafny.Seq("no-plaintext-data-key")))
    @_dafny.classproperty
    def Tests(instance):
        return (((_dafny.Set({})) | (_dafny.Set({TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(_dafny.Seq("Simplest possible happy path"), Wrappers.Option_None(), _dafny.Map({}), AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_None(), default__.StaticPlaintextDataKey, default__.StaticPlaintextDataKey, Wrappers.Option_None()), TestVectors.EncryptTestVector_NegativeEncryptKeyringVector(_dafny.Seq("Missing plaintext data key on decrypt"), Wrappers.Option_None(), _dafny.Map({}), AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_None(), _dafny.Seq("No plaintext data key on encrypt fails"), default__.StaticNotPlaintextDataKey), TestVectors.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(_dafny.Seq("Missing plaintext data key on decrypt"), Wrappers.Option_None(), _dafny.Map({}), AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_None(), _dafny.Seq("No plaintext data key on encrypt fails"), default__.StaticPlaintextDataKey, default__.StaticNotPlaintextDataKey, Wrappers.Option_None())}))) | (default__.FailureBadReproducedEncryptionContext)) | (default__.SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext)
