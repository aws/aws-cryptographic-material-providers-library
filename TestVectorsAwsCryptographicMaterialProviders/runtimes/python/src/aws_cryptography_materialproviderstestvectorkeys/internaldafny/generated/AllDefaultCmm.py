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
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRawAES as AllRawAES
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllRawRSA as AllRawRSA

# Module: AllDefaultCmm

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def SubSets(ec, keys):
        if (len(ec)) == (0):
            return _dafny.Set({_dafny.Map({})})
        elif True:
            d_608_subsets_ = default__.SubSets((ec) - (_dafny.Set({(keys)[0]})), _dafny.Seq((keys)[1::]))
            def iife55_():
                coll23_ = _dafny.Set()
                compr_41_: _dafny.Map
                for compr_41_ in (d_608_subsets_).Elements:
                    d_609_s_: _dafny.Map = compr_41_
                    if (d_609_s_) in (d_608_subsets_):
                        coll23_ = coll23_.union(_dafny.Set([(d_609_s_) | (_dafny.Map({(keys)[0]: (ec)[(keys)[0]]}))]))
                return _dafny.Set(coll23_)
            return (d_608_subsets_) | (iife55_()
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
            def iife58_():
                def lambda52_(d_611_a_, d_612_b_):
                    return (d_611_a_) < (d_612_b_)

                coll26_ = _dafny.Set()
                def lambda51_(d_611_a_, d_612_b_):
                    return (d_611_a_) < (d_612_b_)

                compr_45_: _dafny.Map
                for compr_45_ in (default__.SubSets(d_610_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_610_encryptionContext_).keys, lambda51_))).Elements:
                    d_615_s_: _dafny.Map = compr_45_
                    if (d_615_s_) in (default__.SubSets(d_610_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_610_encryptionContext_).keys, lambda52_))):
                        coll26_ = coll26_.union(_dafny.Set([(d_615_s_).keys]))
                return _dafny.Set(coll26_)
            def iife60_():
                def lambda56_(d_616_a_, d_617_b_):
                    return (d_616_a_) < (d_617_b_)

                coll28_ = _dafny.Set()
                def lambda55_(d_616_a_, d_617_b_):
                    return (d_616_a_) < (d_617_b_)

                compr_48_: _dafny.Map
                for compr_48_ in (default__.SubSets(d_610_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_610_encryptionContext_).keys, lambda55_))).Elements:
                    d_620_s_: _dafny.Map = compr_48_
                    if ((d_620_s_) in (default__.SubSets(d_610_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_610_encryptionContext_).keys, lambda56_)))) and ((((d_620_s_).keys).intersection(d_614_requiredEncryptionContextKeys_)) == (d_614_requiredEncryptionContextKeys_)):
                        coll28_ = coll28_.union(_dafny.Set([d_620_s_]))
                return _dafny.Set(coll28_)
            coll24_ = _dafny.Set()
            compr_42_: _dafny.Map
            for compr_42_ in (default__.encryptionContextsToTest).Elements:
                d_610_encryptionContext_: _dafny.Map = compr_42_
                if (d_610_encryptionContext_) in (default__.encryptionContextsToTest):
                    def iife57_():
                        def lambda50_(d_611_a_, d_612_b_):
                            return (d_611_a_) < (d_612_b_)

                        coll25_ = _dafny.Set()
                        def lambda49_(d_611_a_, d_612_b_):
                            return (d_611_a_) < (d_612_b_)

                        compr_44_: _dafny.Map
                        for compr_44_ in (default__.SubSets(d_610_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_610_encryptionContext_).keys, lambda49_))).Elements:
                            d_613_s_: _dafny.Map = compr_44_
                            if (d_613_s_) in (default__.SubSets(d_610_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_610_encryptionContext_).keys, lambda50_))):
                                coll25_ = coll25_.union(_dafny.Set([(d_613_s_).keys]))
                        return _dafny.Set(coll25_)
                    compr_43_: _dafny.Set
                    for compr_43_ in (iife57_()
                    ).Elements:
                        d_614_requiredEncryptionContextKeys_: _dafny.Set = compr_43_
                        if (d_614_requiredEncryptionContextKeys_) in (iife58_()
                        ):
                            def iife59_():
                                def lambda54_(d_616_a_, d_617_b_):
                                    return (d_616_a_) < (d_617_b_)

                                coll27_ = _dafny.Set()
                                def lambda53_(d_616_a_, d_617_b_):
                                    return (d_616_a_) < (d_617_b_)

                                compr_47_: _dafny.Map
                                for compr_47_ in (default__.SubSets(d_610_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_610_encryptionContext_).keys, lambda53_))).Elements:
                                    d_618_s_: _dafny.Map = compr_47_
                                    if ((d_618_s_) in (default__.SubSets(d_610_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_610_encryptionContext_).keys, lambda54_)))) and ((((d_618_s_).keys).intersection(d_614_requiredEncryptionContextKeys_)) == (d_614_requiredEncryptionContextKeys_)):
                                        coll27_ = coll27_.union(_dafny.Set([d_618_s_]))
                                return _dafny.Set(coll27_)
                            compr_46_: _dafny.Map
                            for compr_46_ in (iife59_()
                            ).Elements:
                                d_619_reproducedEncryptionContext_: _dafny.Map = compr_46_
                                if (d_619_reproducedEncryptionContext_) in (iife60_()
                                ):
                                    coll24_ = coll24_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(_dafny.Seq("Success testing requiredEncryptionContextKeys/reproducedEncryptionContext"), Wrappers.Option_None(), d_610_encryptionContext_, AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_Some(SortedSets.default__.SetToSequence(d_614_requiredEncryptionContextKeys_)), default__.RawAesKeyring, default__.RawAesKeyring, Wrappers.Option_Some(d_619_reproducedEncryptionContext_))]))
            return _dafny.Set(coll24_)
        return iife56_()
        
    @_dafny.classproperty
    def FailureBadReproducedEncryptionContext(instance):
        def iife61_():
            def iife63_():
                def lambda60_(d_622_a_, d_623_b_):
                    return (d_622_a_) < (d_623_b_)

                coll31_ = _dafny.Set()
                def lambda59_(d_622_a_, d_623_b_):
                    return (d_622_a_) < (d_623_b_)

                compr_52_: _dafny.Map
                for compr_52_ in (default__.SubSets(d_621_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_621_encryptionContext_).keys, lambda59_))).Elements:
                    d_626_s_: _dafny.Map = compr_52_
                    if (d_626_s_) in (default__.SubSets(d_621_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_621_encryptionContext_).keys, lambda60_))):
                        coll31_ = coll31_.union(_dafny.Set([(d_626_s_).keys]))
                return _dafny.Set(coll31_)
            def iife65_():
                def lambda64_(d_627_a_, d_628_b_):
                    return (d_627_a_) < (d_628_b_)

                coll33_ = _dafny.Set()
                def lambda63_(d_627_a_, d_628_b_):
                    return (d_627_a_) < (d_628_b_)

                compr_55_: _dafny.Map
                for compr_55_ in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda63_))).Elements:
                    d_631_s_: _dafny.Map = compr_55_
                    if ((d_631_s_) in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda64_)))) and ((d_631_s_) != (_dafny.Map({}))):
                        coll33_ = coll33_.union(_dafny.Set([d_631_s_]))
                return _dafny.Set(coll33_)
            def iife67_():
                def lambda68_(d_632_a_, d_633_b_):
                    return (d_632_a_) < (d_633_b_)

                coll35_ = _dafny.Set()
                def lambda67_(d_632_a_, d_633_b_):
                    return (d_632_a_) < (d_633_b_)

                compr_58_: _dafny.Map
                for compr_58_ in (default__.SubSets(d_621_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_621_encryptionContext_).keys, lambda67_))).Elements:
                    d_636_s_: _dafny.Map = compr_58_
                    if (d_636_s_) in (default__.SubSets(d_621_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_621_encryptionContext_).keys, lambda68_))):
                        coll35_ = coll35_.union(_dafny.Set([(d_636_s_) | (d_630_incorrectEncryptionContext_)]))
                return _dafny.Set(coll35_)
            coll29_ = _dafny.Set()
            compr_49_: _dafny.Map
            for compr_49_ in (default__.encryptionContextsToTest).Elements:
                d_621_encryptionContext_: _dafny.Map = compr_49_
                if (d_621_encryptionContext_) in (default__.encryptionContextsToTest):
                    def iife62_():
                        def lambda58_(d_622_a_, d_623_b_):
                            return (d_622_a_) < (d_623_b_)

                        coll30_ = _dafny.Set()
                        def lambda57_(d_622_a_, d_623_b_):
                            return (d_622_a_) < (d_623_b_)

                        compr_51_: _dafny.Map
                        for compr_51_ in (default__.SubSets(d_621_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_621_encryptionContext_).keys, lambda57_))).Elements:
                            d_624_s_: _dafny.Map = compr_51_
                            if (d_624_s_) in (default__.SubSets(d_621_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_621_encryptionContext_).keys, lambda58_))):
                                coll30_ = coll30_.union(_dafny.Set([(d_624_s_).keys]))
                        return _dafny.Set(coll30_)
                    compr_50_: _dafny.Set
                    for compr_50_ in (iife62_()
                    ).Elements:
                        d_625_requiredEncryptionContextKeys_: _dafny.Set = compr_50_
                        if (d_625_requiredEncryptionContextKeys_) in (iife63_()
                        ):
                            def iife64_():
                                def lambda62_(d_627_a_, d_628_b_):
                                    return (d_627_a_) < (d_628_b_)

                                coll32_ = _dafny.Set()
                                def lambda61_(d_627_a_, d_628_b_):
                                    return (d_627_a_) < (d_628_b_)

                                compr_54_: _dafny.Map
                                for compr_54_ in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda61_))).Elements:
                                    d_629_s_: _dafny.Map = compr_54_
                                    if ((d_629_s_) in (default__.SubSets(default__.disjointEncryptionContext, SortedSets.default__.SetToOrderedSequence2((default__.disjointEncryptionContext).keys, lambda62_)))) and ((d_629_s_) != (_dafny.Map({}))):
                                        coll32_ = coll32_.union(_dafny.Set([d_629_s_]))
                                return _dafny.Set(coll32_)
                            compr_53_: _dafny.Map
                            for compr_53_ in (iife64_()
                            ).Elements:
                                d_630_incorrectEncryptionContext_: _dafny.Map = compr_53_
                                if (d_630_incorrectEncryptionContext_) in (iife65_()
                                ):
                                    def iife66_():
                                        def lambda66_(d_632_a_, d_633_b_):
                                            return (d_632_a_) < (d_633_b_)

                                        coll34_ = _dafny.Set()
                                        def lambda65_(d_632_a_, d_633_b_):
                                            return (d_632_a_) < (d_633_b_)

                                        compr_57_: _dafny.Map
                                        for compr_57_ in (default__.SubSets(d_621_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_621_encryptionContext_).keys, lambda65_))).Elements:
                                            d_634_s_: _dafny.Map = compr_57_
                                            if (d_634_s_) in (default__.SubSets(d_621_encryptionContext_, SortedSets.default__.SetToOrderedSequence2((d_621_encryptionContext_).keys, lambda66_))):
                                                coll34_ = coll34_.union(_dafny.Set([(d_634_s_) | (d_630_incorrectEncryptionContext_)]))
                                        return _dafny.Set(coll34_)
                                    compr_56_: _dafny.Map
                                    for compr_56_ in (iife66_()
                                    ).Elements:
                                        d_635_reproducedEncryptionContext_: _dafny.Map = compr_56_
                                        if (d_635_reproducedEncryptionContext_) in (iife67_()
                                        ):
                                            coll29_ = coll29_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(_dafny.Seq("Failure of reproducedEncryptionContext"), Wrappers.Option_None(), d_621_encryptionContext_, AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_Some(SortedSets.default__.SetToSequence(d_625_requiredEncryptionContextKeys_)), _dafny.Seq("The reproducedEncryptionContext is not correct"), default__.RawAesKeyring, default__.RawAesKeyring, Wrappers.Option_Some(d_635_reproducedEncryptionContext_))]))
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
