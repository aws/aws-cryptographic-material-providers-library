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
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllDefaultCmm as AllDefaultCmm

# Module: aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRequiredEncryptionContextCmm

class default__:
    def  __init__(self):
        pass

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
    def SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext(instance):
        def iife68_():
            def iife71_():
                def lambda81_(d_747_a_, d_748_b_):
                    return (d_747_a_) < (d_748_b_)

                coll39_ = _dafny.Set()
                def lambda80_(d_747_a_, d_748_b_):
                    return (d_747_a_) < (d_748_b_)

                compr_64_: _dafny.Map
                for compr_64_ in (AllDefaultCmm.default__.SubSets(d_746_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_746_encryptionContext_).keys, lambda80_))).Elements:
                    d_755_s_: _dafny.Map = compr_64_
                    if (d_755_s_) in (AllDefaultCmm.default__.SubSets(d_746_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_746_encryptionContext_).keys, lambda81_))):
                        coll39_ = coll39_.union(_dafny.Set([(d_755_s_).keys]))
                return _dafny.Set(coll39_)
            def iife72_():
                def lambda83_(d_751_a_, d_752_b_):
                    return (d_751_a_) < (d_752_b_)

                coll40_ = _dafny.Set()
                def lambda82_(d_751_a_, d_752_b_):
                    return (d_751_a_) < (d_752_b_)

                compr_65_: _dafny.Map
                for compr_65_ in (AllDefaultCmm.default__.SubSets(d_746_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_746_encryptionContext_).keys, lambda82_))).Elements:
                    d_756_s_: _dafny.Map = compr_65_
                    if ((d_756_s_) in (AllDefaultCmm.default__.SubSets(d_746_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_746_encryptionContext_).keys, lambda83_)))) and ((((d_756_s_).keys).intersection(d_750_requiredEncryptionContextKeys_)) == (d_750_requiredEncryptionContextKeys_)):
                        coll40_ = coll40_.union(_dafny.Set([d_756_s_]))
                return _dafny.Set(coll40_)
            coll36_ = _dafny.Set()
            compr_59_: _dafny.Map
            for compr_59_ in (default__.encryptionContextsToTest).Elements:
                d_746_encryptionContext_: _dafny.Map = compr_59_
                def iife69_():
                    def lambda77_(d_747_a_, d_748_b_):
                        return (d_747_a_) < (d_748_b_)

                    coll37_ = _dafny.Set()
                    def lambda76_(d_747_a_, d_748_b_):
                        return (d_747_a_) < (d_748_b_)

                    compr_61_: _dafny.Map
                    for compr_61_ in (AllDefaultCmm.default__.SubSets(d_746_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_746_encryptionContext_).keys, lambda76_))).Elements:
                        d_749_s_: _dafny.Map = compr_61_
                        if (d_749_s_) in (AllDefaultCmm.default__.SubSets(d_746_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_746_encryptionContext_).keys, lambda77_))):
                            coll37_ = coll37_.union(_dafny.Set([(d_749_s_).keys]))
                    return _dafny.Set(coll37_)
                compr_60_: _dafny.Set
                for compr_60_ in (iife69_()
                ).Elements:
                    d_750_requiredEncryptionContextKeys_: _dafny.Set = compr_60_
                    def iife70_():
                        def lambda79_(d_751_a_, d_752_b_):
                            return (d_751_a_) < (d_752_b_)

                        coll38_ = _dafny.Set()
                        def lambda78_(d_751_a_, d_752_b_):
                            return (d_751_a_) < (d_752_b_)

                        compr_63_: _dafny.Map
                        for compr_63_ in (AllDefaultCmm.default__.SubSets(d_746_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_746_encryptionContext_).keys, lambda78_))).Elements:
                            d_753_s_: _dafny.Map = compr_63_
                            if ((d_753_s_) in (AllDefaultCmm.default__.SubSets(d_746_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_746_encryptionContext_).keys, lambda79_)))) and ((((d_753_s_).keys).intersection(d_750_requiredEncryptionContextKeys_)) == (d_750_requiredEncryptionContextKeys_)):
                                coll38_ = coll38_.union(_dafny.Set([d_753_s_]))
                        return _dafny.Set(coll38_)
                    compr_62_: _dafny.Map
                    for compr_62_ in (iife70_()
                    ).Elements:
                        d_754_reproducedEncryptionContext_: _dafny.Map = compr_62_
                        if (((d_746_encryptionContext_) in (default__.encryptionContextsToTest)) and ((d_750_requiredEncryptionContextKeys_) in (iife71_()
                        ))) and ((d_754_reproducedEncryptionContext_) in (iife72_()
                        )):
                            coll36_ = coll36_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(_dafny.Seq("Success testing requiredEncryptionContextKeys/reproducedEncryptionContext"), Wrappers.Option_None(), d_746_encryptionContext_, AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(AllDefaultCmm.default__.StaticAlgorithmSuite), AllDefaultCmm.default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_Some(SortedSets.default__.SetToSequence(d_750_requiredEncryptionContextKeys_)), AllDefaultCmm.default__.RawAesKeyring, AllDefaultCmm.default__.RawAesKeyring, Wrappers.Option_Some(d_754_reproducedEncryptionContext_))]))
            return _dafny.Set(coll36_)
        return iife68_()
        
    @_dafny.classproperty
    def FailureBadReproducedEncryptionContext(instance):
        def iife73_():
            def iife77_():
                def lambda91_(d_758_a_, d_759_b_):
                    return (d_758_a_) < (d_759_b_)

                coll45_ = _dafny.Set()
                def lambda90_(d_758_a_, d_759_b_):
                    return (d_758_a_) < (d_759_b_)

                compr_73_: _dafny.Map
                for compr_73_ in (AllDefaultCmm.default__.SubSets(d_757_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_757_encryptionContext_).keys, lambda90_))).Elements:
                    d_770_s_: _dafny.Map = compr_73_
                    if (d_770_s_) in (AllDefaultCmm.default__.SubSets(d_757_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_757_encryptionContext_).keys, lambda91_))):
                        coll45_ = coll45_.union(_dafny.Set([(d_770_s_).keys]))
                return _dafny.Set(coll45_)
            def iife78_():
                def lambda93_(d_762_a_, d_763_b_):
                    return (d_762_a_) < (d_763_b_)

                coll46_ = _dafny.Set()
                def lambda92_(d_762_a_, d_763_b_):
                    return (d_762_a_) < (d_763_b_)

                compr_74_: _dafny.Map
                for compr_74_ in (AllDefaultCmm.default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda92_))).Elements:
                    d_771_s_: _dafny.Map = compr_74_
                    if ((d_771_s_) in (AllDefaultCmm.default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda93_)))) and ((d_771_s_) != (_dafny.Map({}))):
                        coll46_ = coll46_.union(_dafny.Set([d_771_s_]))
                return _dafny.Set(coll46_)
            def iife79_():
                def lambda95_(d_766_a_, d_767_b_):
                    return (d_766_a_) < (d_767_b_)

                coll47_ = _dafny.Set()
                def lambda94_(d_766_a_, d_767_b_):
                    return (d_766_a_) < (d_767_b_)

                compr_75_: _dafny.Map
                for compr_75_ in (AllDefaultCmm.default__.SubSets(d_757_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_757_encryptionContext_).keys, lambda94_))).Elements:
                    d_772_s_: _dafny.Map = compr_75_
                    if (d_772_s_) in (AllDefaultCmm.default__.SubSets(d_757_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_757_encryptionContext_).keys, lambda95_))):
                        coll47_ = coll47_.union(_dafny.Set([(d_772_s_) | (d_765_incorrectEncryptionContext_)]))
                return _dafny.Set(coll47_)
            coll41_ = _dafny.Set()
            compr_66_: _dafny.Map
            for compr_66_ in (default__.encryptionContextsToTest).Elements:
                d_757_encryptionContext_: _dafny.Map = compr_66_
                def iife74_():
                    def lambda85_(d_758_a_, d_759_b_):
                        return (d_758_a_) < (d_759_b_)

                    coll42_ = _dafny.Set()
                    def lambda84_(d_758_a_, d_759_b_):
                        return (d_758_a_) < (d_759_b_)

                    compr_68_: _dafny.Map
                    for compr_68_ in (AllDefaultCmm.default__.SubSets(d_757_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_757_encryptionContext_).keys, lambda84_))).Elements:
                        d_760_s_: _dafny.Map = compr_68_
                        if (d_760_s_) in (AllDefaultCmm.default__.SubSets(d_757_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_757_encryptionContext_).keys, lambda85_))):
                            coll42_ = coll42_.union(_dafny.Set([(d_760_s_).keys]))
                    return _dafny.Set(coll42_)
                compr_67_: _dafny.Set
                for compr_67_ in (iife74_()
                ).Elements:
                    d_761_requiredEncryptionContextKeys_: _dafny.Set = compr_67_
                    def iife75_():
                        def lambda87_(d_762_a_, d_763_b_):
                            return (d_762_a_) < (d_763_b_)

                        coll43_ = _dafny.Set()
                        def lambda86_(d_762_a_, d_763_b_):
                            return (d_762_a_) < (d_763_b_)

                        compr_70_: _dafny.Map
                        for compr_70_ in (AllDefaultCmm.default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda86_))).Elements:
                            d_764_s_: _dafny.Map = compr_70_
                            if ((d_764_s_) in (AllDefaultCmm.default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda87_)))) and ((d_764_s_) != (_dafny.Map({}))):
                                coll43_ = coll43_.union(_dafny.Set([d_764_s_]))
                        return _dafny.Set(coll43_)
                    compr_69_: _dafny.Map
                    for compr_69_ in (iife75_()
                    ).Elements:
                        d_765_incorrectEncryptionContext_: _dafny.Map = compr_69_
                        def iife76_():
                            def lambda89_(d_766_a_, d_767_b_):
                                return (d_766_a_) < (d_767_b_)

                            coll44_ = _dafny.Set()
                            def lambda88_(d_766_a_, d_767_b_):
                                return (d_766_a_) < (d_767_b_)

                            compr_72_: _dafny.Map
                            for compr_72_ in (AllDefaultCmm.default__.SubSets(d_757_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_757_encryptionContext_).keys, lambda88_))).Elements:
                                d_768_s_: _dafny.Map = compr_72_
                                if (d_768_s_) in (AllDefaultCmm.default__.SubSets(d_757_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_757_encryptionContext_).keys, lambda89_))):
                                    coll44_ = coll44_.union(_dafny.Set([(d_768_s_) | (d_765_incorrectEncryptionContext_)]))
                            return _dafny.Set(coll44_)
                        compr_71_: _dafny.Map
                        for compr_71_ in (iife76_()
                        ).Elements:
                            d_769_reproducedEncryptionContext_: _dafny.Map = compr_71_
                            if ((((d_757_encryptionContext_) in (default__.encryptionContextsToTest)) and ((d_761_requiredEncryptionContextKeys_) in (iife77_()
                            ))) and ((d_765_incorrectEncryptionContext_) in (iife78_()
                            ))) and ((d_769_reproducedEncryptionContext_) in (iife79_()
                            )):
                                coll41_ = coll41_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(_dafny.Seq("Failure of reproducedEncryptionContext"), Wrappers.Option_None(), d_757_encryptionContext_, AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(AllDefaultCmm.default__.StaticAlgorithmSuite), AllDefaultCmm.default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_Some(SortedSets.default__.SetToSequence(d_761_requiredEncryptionContextKeys_)), _dafny.Seq("The reproducedEncryptionContext is not correct"), AllDefaultCmm.default__.RawAesKeyring, AllDefaultCmm.default__.RawAesKeyring, Wrappers.Option_Some(d_769_reproducedEncryptionContext_))]))
            return _dafny.Set(coll41_)
        return iife73_()
        
    @_dafny.classproperty
    def Tests(instance):
        return (default__.SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext) | (default__.FailureBadReproducedEncryptionContext)
