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

# Module: AllDefaultCmm

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
        return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_AES(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawAES_RawAES(default__.AesKey, (_dafny.Seq("aws-raw-vectors-persistent-")) + (default__.AesKey)))
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
        return AlgorithmSuites.default__.GetESDKSuite(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF())
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
        return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Static(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.StaticKeyring_StaticKeyring(_dafny.Seq("static-plaintext-data-key")))
    @_dafny.classproperty
    def StaticNotPlaintextDataKey(instance):
        return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Static(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.StaticKeyring_StaticKeyring(_dafny.Seq("no-plaintext-data-key")))
    @_dafny.classproperty
    def Tests(instance):
        return (((_dafny.Set({})) | (_dafny.Set({TestVectors.EncryptTestVector_PositiveEncryptKeyringVector(_dafny.Seq("Simplest possible happy path"), Wrappers.Option_None(), _dafny.Map({}), AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_None(), default__.StaticPlaintextDataKey, default__.StaticPlaintextDataKey, Wrappers.Option_None()), TestVectors.EncryptTestVector_NegativeEncryptKeyringVector(_dafny.Seq("Missing plaintext data key on decrypt"), Wrappers.Option_None(), _dafny.Map({}), AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_None(), _dafny.Seq("No plaintext data key on encrypt fails"), default__.StaticNotPlaintextDataKey), TestVectors.EncryptTestVector_PositiveEncryptNegativeDecryptKeyringVector(_dafny.Seq("Missing plaintext data key on decrypt"), Wrappers.Option_None(), _dafny.Map({}), AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(default__.StaticAlgorithmSuite), default__.StaticAlgorithmSuite, Wrappers.Option_None(), Wrappers.Option_None(), _dafny.Seq("No plaintext data key on encrypt fails"), default__.StaticPlaintextDataKey, default__.StaticNotPlaintextDataKey, Wrappers.Option_None())}))) | (default__.FailureBadReproducedEncryptionContext)) | (default__.SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext)
