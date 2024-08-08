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
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllKmsEcdh as AllKmsEcdh
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRawAES as AllRawAES
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRawRSA as AllRawRSA
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRawECDH as AllRawECDH
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllDefaultCmm as AllDefaultCmm

# Module: AllRequiredEncryptionContextCmm

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
        def iife79_():
            def iife81_():
                def lambda87_(d_691_a_, d_692_b_):
                    return (d_691_a_) < (d_692_b_)

                coll49_ = _dafny.Set()
                def lambda86_(d_691_a_, d_692_b_):
                    return (d_691_a_) < (d_692_b_)

                compr_88_: _dafny.Map
                for compr_88_ in (AllDefaultCmm.default__.SubSets(d_690_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_690_encryptionContext_).keys, lambda86_))).Elements:
                    d_695_s_: _dafny.Map = compr_88_
                    if (d_695_s_) in (AllDefaultCmm.default__.SubSets(d_690_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_690_encryptionContext_).keys, lambda87_))):
                        coll49_ = coll49_.union(_dafny.Set([(d_695_s_).keys]))
                return _dafny.Set(coll49_)
            def iife83_():
                def lambda91_(d_696_a_, d_697_b_):
                    return (d_696_a_) < (d_697_b_)

                coll51_ = _dafny.Set()
                def lambda90_(d_696_a_, d_697_b_):
                    return (d_696_a_) < (d_697_b_)

                compr_91_: _dafny.Map
                for compr_91_ in (AllDefaultCmm.default__.SubSets(d_690_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_690_encryptionContext_).keys, lambda90_))).Elements:
                    d_700_s_: _dafny.Map = compr_91_
                    if ((d_700_s_) in (AllDefaultCmm.default__.SubSets(d_690_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_690_encryptionContext_).keys, lambda91_)))) and ((((d_700_s_).keys).intersection(d_694_requiredEncryptionContextKeys_)) == (d_694_requiredEncryptionContextKeys_)):
                        coll51_ = coll51_.union(_dafny.Set([d_700_s_]))
                return _dafny.Set(coll51_)
            coll47_ = _dafny.Set()
            compr_85_: _dafny.Map
            for compr_85_ in (default__.encryptionContextsToTest).Elements:
                d_690_encryptionContext_: _dafny.Map = compr_85_
                if (d_690_encryptionContext_) in (default__.encryptionContextsToTest):
                    def iife80_():
                        def lambda85_(d_691_a_, d_692_b_):
                            return (d_691_a_) < (d_692_b_)

                        coll48_ = _dafny.Set()
                        def lambda84_(d_691_a_, d_692_b_):
                            return (d_691_a_) < (d_692_b_)

                        compr_87_: _dafny.Map
                        for compr_87_ in (AllDefaultCmm.default__.SubSets(d_690_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_690_encryptionContext_).keys, lambda84_))).Elements:
                            d_693_s_: _dafny.Map = compr_87_
                            if (d_693_s_) in (AllDefaultCmm.default__.SubSets(d_690_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_690_encryptionContext_).keys, lambda85_))):
                                coll48_ = coll48_.union(_dafny.Set([(d_693_s_).keys]))
                        return _dafny.Set(coll48_)
                    compr_86_: _dafny.Set
                    for compr_86_ in (iife80_()
                    ).Elements:
                        d_694_requiredEncryptionContextKeys_: _dafny.Set = compr_86_
                        if (d_694_requiredEncryptionContextKeys_) in (iife81_()
                        ):
                            def iife82_():
                                def lambda89_(d_696_a_, d_697_b_):
                                    return (d_696_a_) < (d_697_b_)

                                coll50_ = _dafny.Set()
                                def lambda88_(d_696_a_, d_697_b_):
                                    return (d_696_a_) < (d_697_b_)

                                compr_90_: _dafny.Map
                                for compr_90_ in (AllDefaultCmm.default__.SubSets(d_690_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_690_encryptionContext_).keys, lambda88_))).Elements:
                                    d_698_s_: _dafny.Map = compr_90_
                                    if ((d_698_s_) in (AllDefaultCmm.default__.SubSets(d_690_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_690_encryptionContext_).keys, lambda89_)))) and ((((d_698_s_).keys).intersection(d_694_requiredEncryptionContextKeys_)) == (d_694_requiredEncryptionContextKeys_)):
                                        coll50_ = coll50_.union(_dafny.Set([d_698_s_]))
                                return _dafny.Set(coll50_)
                            compr_89_: _dafny.Map
                            for compr_89_ in (iife82_()
                            ).Elements:
                                d_699_reproducedEncryptionContext_: _dafny.Map = compr_89_
                                if (d_699_reproducedEncryptionContext_) in (iife83_()
                                ):
                                    coll47_ = coll47_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(_dafny.Seq("Success testing requiredEncryptionContextKeys/reproducedEncryptionContext"), Wrappers.Option_None(), d_690_encryptionContext_, AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(AllDefaultCmm.default__.StaticAlgorithmSuite), AllDefaultCmm.default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_Some(SortedSets.default__.SetToSequence(d_694_requiredEncryptionContextKeys_)), AllDefaultCmm.default__.RawAesKeyring, AllDefaultCmm.default__.RawAesKeyring, Wrappers.Option_Some(d_699_reproducedEncryptionContext_))]))
            return _dafny.Set(coll47_)
        return iife79_()
        
    @_dafny.classproperty
    def FailureBadReproducedEncryptionContext(instance):
        def iife84_():
            def iife86_():
                def lambda95_(d_702_a_, d_703_b_):
                    return (d_702_a_) < (d_703_b_)

                coll54_ = _dafny.Set()
                def lambda94_(d_702_a_, d_703_b_):
                    return (d_702_a_) < (d_703_b_)

                compr_95_: _dafny.Map
                for compr_95_ in (AllDefaultCmm.default__.SubSets(d_701_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_701_encryptionContext_).keys, lambda94_))).Elements:
                    d_706_s_: _dafny.Map = compr_95_
                    if (d_706_s_) in (AllDefaultCmm.default__.SubSets(d_701_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_701_encryptionContext_).keys, lambda95_))):
                        coll54_ = coll54_.union(_dafny.Set([(d_706_s_).keys]))
                return _dafny.Set(coll54_)
            def iife88_():
                def lambda99_(d_707_a_, d_708_b_):
                    return (d_707_a_) < (d_708_b_)

                coll56_ = _dafny.Set()
                def lambda98_(d_707_a_, d_708_b_):
                    return (d_707_a_) < (d_708_b_)

                compr_98_: _dafny.Map
                for compr_98_ in (AllDefaultCmm.default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda98_))).Elements:
                    d_711_s_: _dafny.Map = compr_98_
                    if ((d_711_s_) in (AllDefaultCmm.default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda99_)))) and ((d_711_s_) != (_dafny.Map({}))):
                        coll56_ = coll56_.union(_dafny.Set([d_711_s_]))
                return _dafny.Set(coll56_)
            def iife90_():
                def lambda103_(d_712_a_, d_713_b_):
                    return (d_712_a_) < (d_713_b_)

                coll58_ = _dafny.Set()
                def lambda102_(d_712_a_, d_713_b_):
                    return (d_712_a_) < (d_713_b_)

                compr_101_: _dafny.Map
                for compr_101_ in (AllDefaultCmm.default__.SubSets(d_701_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_701_encryptionContext_).keys, lambda102_))).Elements:
                    d_716_s_: _dafny.Map = compr_101_
                    if (d_716_s_) in (AllDefaultCmm.default__.SubSets(d_701_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_701_encryptionContext_).keys, lambda103_))):
                        coll58_ = coll58_.union(_dafny.Set([(d_716_s_) | (d_710_incorrectEncryptionContext_)]))
                return _dafny.Set(coll58_)
            coll52_ = _dafny.Set()
            compr_92_: _dafny.Map
            for compr_92_ in (default__.encryptionContextsToTest).Elements:
                d_701_encryptionContext_: _dafny.Map = compr_92_
                if (d_701_encryptionContext_) in (default__.encryptionContextsToTest):
                    def iife85_():
                        def lambda93_(d_702_a_, d_703_b_):
                            return (d_702_a_) < (d_703_b_)

                        coll53_ = _dafny.Set()
                        def lambda92_(d_702_a_, d_703_b_):
                            return (d_702_a_) < (d_703_b_)

                        compr_94_: _dafny.Map
                        for compr_94_ in (AllDefaultCmm.default__.SubSets(d_701_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_701_encryptionContext_).keys, lambda92_))).Elements:
                            d_704_s_: _dafny.Map = compr_94_
                            if (d_704_s_) in (AllDefaultCmm.default__.SubSets(d_701_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_701_encryptionContext_).keys, lambda93_))):
                                coll53_ = coll53_.union(_dafny.Set([(d_704_s_).keys]))
                        return _dafny.Set(coll53_)
                    compr_93_: _dafny.Set
                    for compr_93_ in (iife85_()
                    ).Elements:
                        d_705_requiredEncryptionContextKeys_: _dafny.Set = compr_93_
                        if (d_705_requiredEncryptionContextKeys_) in (iife86_()
                        ):
                            def iife87_():
                                def lambda97_(d_707_a_, d_708_b_):
                                    return (d_707_a_) < (d_708_b_)

                                coll55_ = _dafny.Set()
                                def lambda96_(d_707_a_, d_708_b_):
                                    return (d_707_a_) < (d_708_b_)

                                compr_97_: _dafny.Map
                                for compr_97_ in (AllDefaultCmm.default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda96_))).Elements:
                                    d_709_s_: _dafny.Map = compr_97_
                                    if ((d_709_s_) in (AllDefaultCmm.default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda97_)))) and ((d_709_s_) != (_dafny.Map({}))):
                                        coll55_ = coll55_.union(_dafny.Set([d_709_s_]))
                                return _dafny.Set(coll55_)
                            compr_96_: _dafny.Map
                            for compr_96_ in (iife87_()
                            ).Elements:
                                d_710_incorrectEncryptionContext_: _dafny.Map = compr_96_
                                if (d_710_incorrectEncryptionContext_) in (iife88_()
                                ):
                                    def iife89_():
                                        def lambda101_(d_712_a_, d_713_b_):
                                            return (d_712_a_) < (d_713_b_)

                                        coll57_ = _dafny.Set()
                                        def lambda100_(d_712_a_, d_713_b_):
                                            return (d_712_a_) < (d_713_b_)

                                        compr_100_: _dafny.Map
                                        for compr_100_ in (AllDefaultCmm.default__.SubSets(d_701_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_701_encryptionContext_).keys, lambda100_))).Elements:
                                            d_714_s_: _dafny.Map = compr_100_
                                            if (d_714_s_) in (AllDefaultCmm.default__.SubSets(d_701_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_701_encryptionContext_).keys, lambda101_))):
                                                coll57_ = coll57_.union(_dafny.Set([(d_714_s_) | (d_710_incorrectEncryptionContext_)]))
                                        return _dafny.Set(coll57_)
                                    compr_99_: _dafny.Map
                                    for compr_99_ in (iife89_()
                                    ).Elements:
                                        d_715_reproducedEncryptionContext_: _dafny.Map = compr_99_
                                        if (d_715_reproducedEncryptionContext_) in (iife90_()
                                        ):
                                            coll52_ = coll52_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(_dafny.Seq("Failure of reproducedEncryptionContext"), Wrappers.Option_None(), d_701_encryptionContext_, AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(AllDefaultCmm.default__.StaticAlgorithmSuite), AllDefaultCmm.default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_Some(SortedSets.default__.SetToSequence(d_705_requiredEncryptionContextKeys_)), _dafny.Seq("The reproducedEncryptionContext is not correct"), AllDefaultCmm.default__.RawAesKeyring, AllDefaultCmm.default__.RawAesKeyring, Wrappers.Option_Some(d_715_reproducedEncryptionContext_))]))
            return _dafny.Set(coll52_)
        return iife84_()
        
    @_dafny.classproperty
    def Tests(instance):
        return (default__.SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext) | (default__.FailureBadReproducedEncryptionContext)
