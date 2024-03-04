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

# Module: AllRawRSA

class default__:
    def  __init__(self):
        pass

    @_dafny.classproperty
    def rsaPersistentKeyNamesWithoutPublicPrivate(instance):
        return _dafny.Seq([_dafny.Seq("rsa-4096")])
    @_dafny.classproperty
    def KeyDescriptions(instance):
        def iife37_():
            coll21_ = _dafny.Set()
            compr_36_: _dafny.Seq
            for compr_36_ in (default__.rsaPersistentKeyNamesWithoutPublicPrivate).Elements:
                d_702_key_: _dafny.Seq = compr_36_
                compr_37_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme
                for compr_37_ in software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme.AllSingletonConstructors:
                    d_703_padding_: software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme = compr_37_
                    if (d_702_key_) in (default__.rsaPersistentKeyNamesWithoutPublicPrivate):
                        coll21_ = coll21_.union(_dafny.Set([software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_RSA(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawRSA_RawRSA(d_702_key_, (_dafny.Seq("aws-raw-vectors-persistent-")) + (d_702_key_), d_703_padding_))]))
            return _dafny.Set(coll21_)
        return iife37_()
        
    @_dafny.classproperty
    def Tests(instance):
        def iife38_():
            coll22_ = _dafny.Set()
            compr_38_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription
            for compr_38_ in (default__.KeyDescriptions).Elements:
                d_704_keyDescription_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription = compr_38_
                compr_39_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
                for compr_39_ in (AllAlgorithmSuites.default__.AllAlgorithmSuites).Elements:
                    d_705_algorithmSuite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo = compr_39_
                    compr_40_: software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy
                    for compr_40_ in [AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_705_algorithmSuite_)]:
                        d_706_commitmentPolicy_: software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy = compr_40_
                        if (((d_704_keyDescription_) in (default__.KeyDescriptions)) and ((d_705_algorithmSuite_) in (AllAlgorithmSuites.default__.AllAlgorithmSuites))) and ((d_706_commitmentPolicy_) == (AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_705_algorithmSuite_))):
                            def iife39_(_pat_let8_0):
                                def iife40_(d_707_dt__update__tmp_h0_):
                                    def iife42_(_pat_let10_0):
                                        def iife43_(d_708_dt__update__tmp_h1_):
                                            def iife44_(_pat_let11_0):
                                                def iife45_(d_709_dt__update_hkeyId_h0_):
                                                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawRSA_RawRSA(d_709_dt__update_hkeyId_h0_, (d_708_dt__update__tmp_h1_).providerId, (d_708_dt__update__tmp_h1_).padding)
                                                return iife45_(_pat_let11_0)
                                            return iife44_((((d_704_keyDescription_).RSA).keyId) + (_dafny.Seq("-public")))
                                        return iife43_(_pat_let10_0)
                                    def iife41_(_pat_let9_0):
                                        def iife46_(d_710_dt__update_hRSA_h0_):
                                            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_RSA(d_710_dt__update_hRSA_h0_)
                                        return iife46_(_pat_let9_0)
                                    return iife41_(iife42_((d_704_keyDescription_).RSA))
                                return iife40_(_pat_let8_0)
                            def iife47_(_pat_let12_0):
                                def iife48_(d_711_dt__update__tmp_h2_):
                                    def iife50_(_pat_let14_0):
                                        def iife51_(d_712_dt__update__tmp_h3_):
                                            def iife52_(_pat_let15_0):
                                                def iife53_(d_713_dt__update_hkeyId_h1_):
                                                    return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawRSA_RawRSA(d_713_dt__update_hkeyId_h1_, (d_712_dt__update__tmp_h3_).providerId, (d_712_dt__update__tmp_h3_).padding)
                                                return iife53_(_pat_let15_0)
                                            return iife52_((((d_704_keyDescription_).RSA).keyId) + (_dafny.Seq("-private")))
                                        return iife51_(_pat_let14_0)
                                    def iife49_(_pat_let13_0):
                                        def iife54_(d_714_dt__update_hRSA_h1_):
                                            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_RSA(d_714_dt__update_hRSA_h1_)
                                        return iife54_(_pat_let13_0)
                                    return iife49_(iife50_((d_704_keyDescription_).RSA))
                                return iife48_(_pat_let12_0)
                            coll22_ = coll22_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptKeyringVector((_dafny.Seq("Generated RawRSA ")) + (((d_704_keyDescription_).RSA).keyId), Wrappers.Option_None(), _dafny.Map({}), d_706_commitmentPolicy_, d_705_algorithmSuite_, Wrappers.Option_None(), Wrappers.Option_None(), iife39_(d_704_keyDescription_), iife47_(d_704_keyDescription_), Wrappers.Option_None())]))
            return _dafny.Set(coll22_)
        return iife38_()
        
