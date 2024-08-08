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

# Module: AllDefaultCmm

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def SubSets(ec, keys):
        if (len(ec)) == (0):
            return _dafny.Set({_dafny.Map({})})
        elif True:
            d_661_subsets_ = default__.SubSets((ec) - (_dafny.Set({(keys)[0]})), _dafny.Seq((keys)[1::]))
            def iife66_():
                coll34_ = _dafny.Set()
                compr_67_: _dafny.Map
                for compr_67_ in (d_661_subsets_).Elements:
                    d_662_s_: _dafny.Map = compr_67_
                    if (d_662_s_) in (d_661_subsets_):
                        coll34_ = coll34_.union(_dafny.Set([(d_662_s_) | (_dafny.Map({(keys)[0]: (ec)[(keys)[0]]}))]))
                return _dafny.Set(coll34_)
            return (d_661_subsets_) | (iife66_()
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
        def iife67_():
            def iife69_():
                def lambda67_(d_664_a_, d_665_b_):
                    return (d_664_a_) < (d_665_b_)

                coll37_ = _dafny.Set()
                def lambda66_(d_664_a_, d_665_b_):
                    return (d_664_a_) < (d_665_b_)

                compr_71_: _dafny.Map
                for compr_71_ in (default__.SubSets(d_663_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_663_encryptionContext_).keys, lambda66_))).Elements:
                    d_668_s_: _dafny.Map = compr_71_
                    if (d_668_s_) in (default__.SubSets(d_663_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_663_encryptionContext_).keys, lambda67_))):
                        coll37_ = coll37_.union(_dafny.Set([(d_668_s_).keys]))
                return _dafny.Set(coll37_)
            def iife71_():
                def lambda71_(d_669_a_, d_670_b_):
                    return (d_669_a_) < (d_670_b_)

                coll39_ = _dafny.Set()
                def lambda70_(d_669_a_, d_670_b_):
                    return (d_669_a_) < (d_670_b_)

                compr_74_: _dafny.Map
                for compr_74_ in (default__.SubSets(d_663_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_663_encryptionContext_).keys, lambda70_))).Elements:
                    d_673_s_: _dafny.Map = compr_74_
                    if ((d_673_s_) in (default__.SubSets(d_663_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_663_encryptionContext_).keys, lambda71_)))) and ((((d_673_s_).keys).intersection(d_667_requiredEncryptionContextKeys_)) == (d_667_requiredEncryptionContextKeys_)):
                        coll39_ = coll39_.union(_dafny.Set([d_673_s_]))
                return _dafny.Set(coll39_)
            coll35_ = _dafny.Set()
            compr_68_: _dafny.Map
            for compr_68_ in (default__.encryptionContextsToTest).Elements:
                d_663_encryptionContext_: _dafny.Map = compr_68_
                if (d_663_encryptionContext_) in (default__.encryptionContextsToTest):
                    def iife68_():
                        def lambda65_(d_664_a_, d_665_b_):
                            return (d_664_a_) < (d_665_b_)

                        coll36_ = _dafny.Set()
                        def lambda64_(d_664_a_, d_665_b_):
                            return (d_664_a_) < (d_665_b_)

                        compr_70_: _dafny.Map
                        for compr_70_ in (default__.SubSets(d_663_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_663_encryptionContext_).keys, lambda64_))).Elements:
                            d_666_s_: _dafny.Map = compr_70_
                            if (d_666_s_) in (default__.SubSets(d_663_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_663_encryptionContext_).keys, lambda65_))):
                                coll36_ = coll36_.union(_dafny.Set([(d_666_s_).keys]))
                        return _dafny.Set(coll36_)
                    compr_69_: _dafny.Set
                    for compr_69_ in (iife68_()
                    ).Elements:
                        d_667_requiredEncryptionContextKeys_: _dafny.Set = compr_69_
                        if (d_667_requiredEncryptionContextKeys_) in (iife69_()
                        ):
                            def iife70_():
                                def lambda69_(d_669_a_, d_670_b_):
                                    return (d_669_a_) < (d_670_b_)

                                coll38_ = _dafny.Set()
                                def lambda68_(d_669_a_, d_670_b_):
                                    return (d_669_a_) < (d_670_b_)

                                compr_73_: _dafny.Map
                                for compr_73_ in (default__.SubSets(d_663_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_663_encryptionContext_).keys, lambda68_))).Elements:
                                    d_671_s_: _dafny.Map = compr_73_
                                    if ((d_671_s_) in (default__.SubSets(d_663_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_663_encryptionContext_).keys, lambda69_)))) and ((((d_671_s_).keys).intersection(d_667_requiredEncryptionContextKeys_)) == (d_667_requiredEncryptionContextKeys_)):
                                        coll38_ = coll38_.union(_dafny.Set([d_671_s_]))
                                return _dafny.Set(coll38_)
                            compr_72_: _dafny.Map
                            for compr_72_ in (iife70_()
                            ).Elements:
                                d_672_reproducedEncryptionContext_: _dafny.Map = compr_72_
                                if (d_672_reproducedEncryptionContext_) in (iife71_()
                                ):
                                    coll35_ = coll35_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(_dafny.Seq("Success testing requiredEncryptionContextKeys/reproducedEncryptionContext"), Wrappers.Option_None(), d_663_encryptionContext_, AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_Some(SortedSets.default__.SetToSequence(d_667_requiredEncryptionContextKeys_)), default__.RawAesKeyring, default__.RawAesKeyring, Wrappers.Option_Some(d_672_reproducedEncryptionContext_))]))
            return _dafny.Set(coll35_)
        return iife67_()
        
    @_dafny.classproperty
    def FailureBadReproducedEncryptionContext(instance):
        def iife72_():
            def iife74_():
                def lambda75_(d_675_a_, d_676_b_):
                    return (d_675_a_) < (d_676_b_)

                coll42_ = _dafny.Set()
                def lambda74_(d_675_a_, d_676_b_):
                    return (d_675_a_) < (d_676_b_)

                compr_78_: _dafny.Map
                for compr_78_ in (default__.SubSets(d_674_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_674_encryptionContext_).keys, lambda74_))).Elements:
                    d_679_s_: _dafny.Map = compr_78_
                    if (d_679_s_) in (default__.SubSets(d_674_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_674_encryptionContext_).keys, lambda75_))):
                        coll42_ = coll42_.union(_dafny.Set([(d_679_s_).keys]))
                return _dafny.Set(coll42_)
            def iife76_():
                def lambda79_(d_680_a_, d_681_b_):
                    return (d_680_a_) < (d_681_b_)

                coll44_ = _dafny.Set()
                def lambda78_(d_680_a_, d_681_b_):
                    return (d_680_a_) < (d_681_b_)

                compr_81_: _dafny.Map
                for compr_81_ in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda78_))).Elements:
                    d_684_s_: _dafny.Map = compr_81_
                    if ((d_684_s_) in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda79_)))) and ((d_684_s_) != (_dafny.Map({}))):
                        coll44_ = coll44_.union(_dafny.Set([d_684_s_]))
                return _dafny.Set(coll44_)
            def iife78_():
                def lambda83_(d_685_a_, d_686_b_):
                    return (d_685_a_) < (d_686_b_)

                coll46_ = _dafny.Set()
                def lambda82_(d_685_a_, d_686_b_):
                    return (d_685_a_) < (d_686_b_)

                compr_84_: _dafny.Map
                for compr_84_ in (default__.SubSets(d_674_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_674_encryptionContext_).keys, lambda82_))).Elements:
                    d_689_s_: _dafny.Map = compr_84_
                    if (d_689_s_) in (default__.SubSets(d_674_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_674_encryptionContext_).keys, lambda83_))):
                        coll46_ = coll46_.union(_dafny.Set([(d_689_s_) | (d_683_incorrectEncryptionContext_)]))
                return _dafny.Set(coll46_)
            coll40_ = _dafny.Set()
            compr_75_: _dafny.Map
            for compr_75_ in (default__.encryptionContextsToTest).Elements:
                d_674_encryptionContext_: _dafny.Map = compr_75_
                if (d_674_encryptionContext_) in (default__.encryptionContextsToTest):
                    def iife73_():
                        def lambda73_(d_675_a_, d_676_b_):
                            return (d_675_a_) < (d_676_b_)

                        coll41_ = _dafny.Set()
                        def lambda72_(d_675_a_, d_676_b_):
                            return (d_675_a_) < (d_676_b_)

                        compr_77_: _dafny.Map
                        for compr_77_ in (default__.SubSets(d_674_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_674_encryptionContext_).keys, lambda72_))).Elements:
                            d_677_s_: _dafny.Map = compr_77_
                            if (d_677_s_) in (default__.SubSets(d_674_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_674_encryptionContext_).keys, lambda73_))):
                                coll41_ = coll41_.union(_dafny.Set([(d_677_s_).keys]))
                        return _dafny.Set(coll41_)
                    compr_76_: _dafny.Set
                    for compr_76_ in (iife73_()
                    ).Elements:
                        d_678_requiredEncryptionContextKeys_: _dafny.Set = compr_76_
                        if (d_678_requiredEncryptionContextKeys_) in (iife74_()
                        ):
                            def iife75_():
                                def lambda77_(d_680_a_, d_681_b_):
                                    return (d_680_a_) < (d_681_b_)

                                coll43_ = _dafny.Set()
                                def lambda76_(d_680_a_, d_681_b_):
                                    return (d_680_a_) < (d_681_b_)

                                compr_80_: _dafny.Map
                                for compr_80_ in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda76_))).Elements:
                                    d_682_s_: _dafny.Map = compr_80_
                                    if ((d_682_s_) in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda77_)))) and ((d_682_s_) != (_dafny.Map({}))):
                                        coll43_ = coll43_.union(_dafny.Set([d_682_s_]))
                                return _dafny.Set(coll43_)
                            compr_79_: _dafny.Map
                            for compr_79_ in (iife75_()
                            ).Elements:
                                d_683_incorrectEncryptionContext_: _dafny.Map = compr_79_
                                if (d_683_incorrectEncryptionContext_) in (iife76_()
                                ):
                                    def iife77_():
                                        def lambda81_(d_685_a_, d_686_b_):
                                            return (d_685_a_) < (d_686_b_)

                                        coll45_ = _dafny.Set()
                                        def lambda80_(d_685_a_, d_686_b_):
                                            return (d_685_a_) < (d_686_b_)

                                        compr_83_: _dafny.Map
                                        for compr_83_ in (default__.SubSets(d_674_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_674_encryptionContext_).keys, lambda80_))).Elements:
                                            d_687_s_: _dafny.Map = compr_83_
                                            if (d_687_s_) in (default__.SubSets(d_674_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_674_encryptionContext_).keys, lambda81_))):
                                                coll45_ = coll45_.union(_dafny.Set([(d_687_s_) | (d_683_incorrectEncryptionContext_)]))
                                        return _dafny.Set(coll45_)
                                    compr_82_: _dafny.Map
                                    for compr_82_ in (iife77_()
                                    ).Elements:
                                        d_688_reproducedEncryptionContext_: _dafny.Map = compr_82_
                                        if (d_688_reproducedEncryptionContext_) in (iife78_()
                                        ):
                                            coll40_ = coll40_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(_dafny.Seq("Failure of reproducedEncryptionContext"), Wrappers.Option_None(), d_674_encryptionContext_, AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_Some(SortedSets.default__.SetToSequence(d_678_requiredEncryptionContextKeys_)), _dafny.Seq("The reproducedEncryptionContext is not correct"), default__.RawAesKeyring, default__.RawAesKeyring, Wrappers.Option_Some(d_688_reproducedEncryptionContext_))]))
            return _dafny.Set(coll40_)
        return iife72_()
        
    @_dafny.classproperty
    def StaticPlaintextDataKey(instance):
        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Static(AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring_StaticKeyring(_dafny.Seq("static-plaintext-data-key")))
    @_dafny.classproperty
    def StaticNotPlaintextDataKey(instance):
        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription_Static(AwsCryptographyMaterialProvidersTestVectorKeysTypes.StaticKeyring_StaticKeyring(_dafny.Seq("no-plaintext-data-key")))
    @_dafny.classproperty
    def Tests(instance):
        return (((_dafny.Set({})) | (_dafny.Set({TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(_dafny.Seq("Simplest possible happy path"), Wrappers.Option_None(), _dafny.Map({}), AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_None(), default__.StaticPlaintextDataKey, default__.StaticPlaintextDataKey, Wrappers.Option_None()), TestVectors.EncryptTestVector_NegativeEncryptKeyringVector(_dafny.Seq("Missing plaintext data key on decrypt"), Wrappers.Option_None(), _dafny.Map({}), AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_None(), _dafny.Seq("No plaintext data key on encrypt fails"), default__.StaticNotPlaintextDataKey), TestVectors.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(_dafny.Seq("Missing plaintext data key on decrypt"), Wrappers.Option_None(), _dafny.Map({}), AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_None(), _dafny.Seq("No plaintext data key on encrypt fails"), default__.StaticPlaintextDataKey, default__.StaticNotPlaintextDataKey, Wrappers.Option_None())}))) | (default__.FailureBadReproducedEncryptionContext)) | (default__.SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext)
