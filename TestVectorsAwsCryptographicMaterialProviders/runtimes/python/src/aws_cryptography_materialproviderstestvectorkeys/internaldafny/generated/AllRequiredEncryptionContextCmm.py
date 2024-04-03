import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import Base64
import AlgorithmSuites
import Materials
import Keyring
import Relations
import Seq_MergeSort
import Math
import Seq
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import Actions
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Constants
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import DafnyLibraries
import Time
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import UUID
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring
import CMM
import Defaults
import Commitment
import DefaultCMM
import DefaultClientSupplier
import RequiredEncryptionContextCMM
import AwsCryptographyMaterialProvidersOperations
import software_amazon_cryptography_materialproviders_internaldafny
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import AesKdfCtr
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibraryInterop
import Streams
import Sorting
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64Lemmas
import MplManifestOptions
import AllAlgorithmSuites
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer
import JSON_Deserializer_Uint16StrConversion
import JSON_Deserializer_ByteStrConversion
import JSON_Deserializer
import JSON_ConcreteSyntax_Spec
import JSON_ConcreteSyntax_SpecProperties
import JSON_ConcreteSyntax
import JSON_ZeroCopy_Serializer
import JSON_ZeroCopy_Deserializer_Core
import JSON_ZeroCopy_Deserializer_Strings
import JSON_ZeroCopy_Deserializer_Numbers
import JSON_ZeroCopy_Deserializer_ObjectParams
import JSON_ZeroCopy_Deserializer_Objects
import JSON_ZeroCopy_Deserializer_ArrayParams
import JSON_ZeroCopy_Deserializer_Arrays
import JSON_ZeroCopy_Deserializer_Constants
import JSON_ZeroCopy_Deserializer_Values
import JSON_ZeroCopy_Deserializer_API
import JSON_ZeroCopy_Deserializer
import JSON_ZeroCopy_API
import JSON_ZeroCopy
import JSON_API
import JSON
import JSONHelpers
import KeyDescription
import KeyMaterial
import CreateStaticKeyrings
import CreateStaticKeyStores
import KeyringFromKeyDescription
import CmmFromKeyDescription
import KeysVectorOperations
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny
import TestVectors
import AllHierarchy
import AllKms
import AllKmsMrkAware
import AllKmsMrkAwareDiscovery
import AllKmsRsa
import AllRawAES
import AllRawRSA
import AllDefaultCmm

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
