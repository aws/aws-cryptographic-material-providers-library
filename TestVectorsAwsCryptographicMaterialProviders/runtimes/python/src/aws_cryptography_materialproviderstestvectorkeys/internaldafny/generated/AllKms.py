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

# Module: AllKms

class default__:
    def  __init__(self):
        pass

    @_dafny.classproperty
    def AllAwsKMSKeys(instance):
        return _dafny.Seq([_dafny.Seq("us-west-2-decryptable"), _dafny.Seq("us-west-2-mrk")])
    @_dafny.classproperty
    def KeyDescriptions(instance):
        def iife24_():
            coll8_ = _dafny.Set()
            compr_10_: _dafny.Seq
            for compr_10_ in (default__.AllAwsKMSKeys).Elements:
                d_676_key_: _dafny.Seq = compr_10_
                if (d_676_key_) in (default__.AllAwsKMSKeys):
                    coll8_ = coll8_.union(_dafny.Set([software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_Kms(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KMSInfo_KMSInfo(d_676_key_))]))
            return _dafny.Set(coll8_)
        return iife24_()
        
    @_dafny.classproperty
    def Tests(instance):
        def iife25_():
            coll9_ = _dafny.Set()
            compr_11_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription
            for compr_11_ in (default__.KeyDescriptions).Elements:
                d_677_keyDescription_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription = compr_11_
                compr_12_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
                for compr_12_ in (AllAlgorithmSuites.default__.AllAlgorithmSuites).Elements:
                    d_678_algorithmSuite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo = compr_12_
                    compr_13_: software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy
                    for compr_13_ in [AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_678_algorithmSuite_)]:
                        d_679_commitmentPolicy_: software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy = compr_13_
                        if (((d_677_keyDescription_) in (default__.KeyDescriptions)) and ((d_678_algorithmSuite_) in (AllAlgorithmSuites.default__.AllAlgorithmSuites))) and ((d_679_commitmentPolicy_) == (AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_678_algorithmSuite_))):
                            coll9_ = coll9_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptKeyringVector((_dafny.Seq("Generated KMS ")) + (((d_677_keyDescription_).Kms).keyId), Wrappers.Option_None(), _dafny.Map({}), d_679_commitmentPolicy_, d_678_algorithmSuite_, Wrappers.Option_None(), Wrappers.Option_None(), d_677_keyDescription_, d_677_keyDescription_, Wrappers.Option_None())]))
            return _dafny.Set(coll9_)
        return iife25_()
        
