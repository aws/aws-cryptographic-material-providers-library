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

# Module: AllKmsRsa

class default__:
    def  __init__(self):
        pass

    @_dafny.classproperty
    def AllKmsRsaKeys(instance):
        return _dafny.Seq([_dafny.Seq("us-west-2-rsa-mrk")])
    @_dafny.classproperty
    def KeyDescriptions(instance):
        def iife30_():
            def iife32_():
                coll16_ = _dafny.Set()
                compr_27_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec
                for compr_27_ in software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec.AllSingletonConstructors:
                    d_695_e_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = compr_27_
                    if not((d_695_e_).is_SYMMETRIC__DEFAULT):
                        coll16_ = coll16_.union(_dafny.Set([d_695_e_]))
                return _dafny.Set(coll16_)
            coll14_ = _dafny.Set()
            compr_24_: _dafny.Seq
            for compr_24_ in (default__.AllKmsRsaKeys).Elements:
                d_692_key_: _dafny.Seq = compr_24_
                def iife31_():
                    coll15_ = _dafny.Set()
                    compr_26_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec
                    for compr_26_ in software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec.AllSingletonConstructors:
                        d_693_e_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = compr_26_
                        if not((d_693_e_).is_SYMMETRIC__DEFAULT):
                            coll15_ = coll15_.union(_dafny.Set([d_693_e_]))
                    return _dafny.Set(coll15_)
                compr_25_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec
                for compr_25_ in (iife31_()
                ).Elements:
                    d_694_encryptionAlgorithm_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec = compr_25_
                    if ((d_692_key_) in (default__.AllKmsRsaKeys)) and ((d_694_encryptionAlgorithm_) in (iife32_()
                    )):
                        coll14_ = coll14_.union(_dafny.Set([software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription_KmsRsa(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KmsRsaKeyring_KmsRsaKeyring(d_692_key_, d_694_encryptionAlgorithm_))]))
            return _dafny.Set(coll14_)
        return iife30_()
        
    @_dafny.classproperty
    def algorithmSuites(instance):
        def iife33_():
            coll17_ = _dafny.Set()
            compr_28_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
            for compr_28_ in (AllAlgorithmSuites.default__.AllAlgorithmSuites).Elements:
                d_696_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo = compr_28_
                if AlgorithmSuites.AlgorithmSuite._Is(d_696_suite_):
                    if ((d_696_suite_) in (AllAlgorithmSuites.default__.AllAlgorithmSuites)) and (not(((d_696_suite_).signature).is_ECDSA)):
                        coll17_ = coll17_.union(_dafny.Set([d_696_suite_]))
            return _dafny.Set(coll17_)
        return iife33_()
        
    @_dafny.classproperty
    def Tests(instance):
        def iife34_():
            coll18_ = _dafny.Set()
            compr_29_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription
            for compr_29_ in (default__.KeyDescriptions).Elements:
                d_697_keyDescription_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription = compr_29_
                compr_30_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
                for compr_30_ in (default__.algorithmSuites).Elements:
                    d_698_algorithmSuite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo = compr_30_
                    compr_31_: software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy
                    for compr_31_ in [AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_698_algorithmSuite_)]:
                        d_699_commitmentPolicy_: software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy = compr_31_
                        if (((d_697_keyDescription_) in (default__.KeyDescriptions)) and ((d_698_algorithmSuite_) in (default__.algorithmSuites))) and ((d_699_commitmentPolicy_) == (AllAlgorithmSuites.default__.GetCompatibleCommitmentPolicy(d_698_algorithmSuite_))):
                            coll18_ = coll18_.union(_dafny.Set([TestVectors.EncryptTestVector_PositiveEncryptKeyringVector((_dafny.Seq("Generated KMS RSA ")) + (((d_697_keyDescription_).KmsRsa).keyId), Wrappers.Option_None(), _dafny.Map({}), d_699_commitmentPolicy_, d_698_algorithmSuite_, Wrappers.Option_None(), Wrappers.Option_None(), d_697_keyDescription_, d_697_keyDescription_, Wrappers.Option_None())]))
            return _dafny.Set(coll18_)
        return iife34_()
        
