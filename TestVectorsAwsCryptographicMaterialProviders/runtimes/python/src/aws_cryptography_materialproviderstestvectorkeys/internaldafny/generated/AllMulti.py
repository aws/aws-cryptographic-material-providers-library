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
import AllRequiredEncryptionContextCmm

# Module: AllMulti

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def getChildKeyrings(keys, key, i):
        d_773___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (i) == (len(keys)):
                    return (d_773___accumulator_) + (_dafny.Seq([]))
                elif ((keys)[i]) == (key):
                    in3_ = keys
                    in4_ = key
                    in5_ = (i) + (1)
                    keys = in3_
                    key = in4_
                    i = in5_
                    raise _dafny.TailCall()
                elif True:
                    d_773___accumulator_ = (d_773___accumulator_) + (_dafny.Seq([software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_AES(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawAES_RawAES((keys)[i], (_dafny.Seq("aws-raw-vectors-persistent-")) + ((keys)[i])))]))
                    in6_ = keys
                    in7_ = key
                    in8_ = (i) + (1)
                    keys = in6_
                    key = in7_
                    i = in8_
                    raise _dafny.TailCall()
                break

    @_dafny.classproperty
    def KeyDescriptionsGeneratorAndChildren(instance):
        def iife80_():
            coll48_ = _dafny.Set()
            compr_76_: _dafny.Seq
            for compr_76_ in (AllRawAES.default__.aesPersistentKeyNames).Elements:
                d_774_key_: _dafny.Seq = compr_76_
                if (d_774_key_) in (AllRawAES.default__.aesPersistentKeyNames):
                    coll48_ = coll48_.union(_dafny.Set([software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Multi(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.MultiKeyring_MultiKeyring(Wrappers.Option_Some(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_AES(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawAES_RawAES(d_774_key_, (_dafny.Seq("aws-raw-vectors-persistent-")) + (d_774_key_)))), default__.getChildKeyrings(AllRawAES.default__.aesPersistentKeyNames, d_774_key_, 0)))]))
            return _dafny.Set(coll48_)
        return iife80_()
        
    @_dafny.classproperty
    def OnlyGeneratorKeyDescriptions(instance):
        def iife81_():
            coll49_ = _dafny.Set()
            compr_77_: _dafny.Seq
            for compr_77_ in (AllRawAES.default__.aesPersistentKeyNames).Elements:
                d_775_key_: _dafny.Seq = compr_77_
                if (d_775_key_) in (AllRawAES.default__.aesPersistentKeyNames):
                    coll49_ = coll49_.union(_dafny.Set([software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Multi(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.MultiKeyring_MultiKeyring(Wrappers.Option_Some(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_AES(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.RawAES_RawAES(d_775_key_, (_dafny.Seq("aws-raw-vectors-persistent-")) + (d_775_key_)))), _dafny.Seq([])))]))
            return _dafny.Set(coll49_)
        return iife81_()
        
    @_dafny.classproperty
    def KeyDescriptions(instance):
        return (default__.OnlyGeneratorKeyDescriptions) | (default__.KeyDescriptionsGeneratorAndChildren)
    @_dafny.classproperty
    def Tests(instance):
        def iife82_():
            coll50_ = _dafny.Set()
            compr_78_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription
            for compr_78_ in (default__.KeyDescriptions).Elements:
                d_776_keyDescription_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription = compr_78_
                compr_79_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
                for compr_79_ in (AllAlgorithmSuites.default__.AllAlgorithmSuites).Elements:
                    d_777_algorithmSuite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo = compr_79_
                    compr_80_: software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy
                    for compr_80_ in [AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_777_algorithmSuite_)]:
                        d_778_commitmentPolicy_: software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy = compr_80_
                        if (((d_776_keyDescription_) in (default__.KeyDescriptions)) and ((d_777_algorithmSuite_) in (AllAlgorithmSuites.default__.AllAlgorithmSuites))) and ((d_778_commitmentPolicy_) == (AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_777_algorithmSuite_))):
                            coll50_ = coll50_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptKeyringVector((_dafny.Seq("MultiKeyring ")) + ((((((d_776_keyDescription_).Multi).generator).value).AES).keyId), Wrappers.Option_None(), _dafny.Map({}), d_778_commitmentPolicy_, d_777_algorithmSuite_, Wrappers.Option_None(), Wrappers.Option_None(), d_776_keyDescription_, d_776_keyDescription_, Wrappers.Option_None())]))
            return _dafny.Set(coll50_)
        return iife82_()
        
