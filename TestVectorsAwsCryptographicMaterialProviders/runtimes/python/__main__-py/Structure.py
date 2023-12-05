import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
import Math
import Seq
import BoundedInts
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
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
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
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
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
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import TestVectorsUtils
import TestVectorConstants
import KeyringExpectations
import CreateAwsKmsKeyrings
import CreateAwsKmsMultiKeyrings
import CreateAwsKmsMrkKeyrings
import CreateAwsKmsMrkMultiKeyrings
import CreateRawAesKeyrings
import CreateRawRsaKeyrings
import CreateKeyrings
import software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types
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
import KeysVectorOperations
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny
import TestVectors
import CompleteVectors
import ParseJsonManifests
import TestManifests
import WrappedMaterialProvidersMain
import TestWrappedMaterialProvidersMain
import software_amazon_cryptography_services_dynamodb_internaldafny

# Module: Structure

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BranchKeyContext_q(m):
        def lambda130_(forall_var_22_):
            d_1951_k_: _dafny.Seq = forall_var_22_
            return not ((d_1951_k_) in ((m).keys)) or (software_amazon_cryptography_services_dynamodb_internaldafny_types.default__.IsValid__AttributeName(d_1951_k_))

        return (((((((((((((default__.BRANCH__KEY__IDENTIFIER__FIELD) in (m)) and ((default__.TYPE__FIELD) in (m))) and ((default__.KEY__CREATE__TIME) in (m))) and ((default__.HIERARCHY__VERSION) in (m))) and ((default__.TABLE__FIELD) in (m))) and ((default__.KMS__FIELD) in (m))) and ((default__.BRANCH__KEY__FIELD) not in ((m).keys))) and ((0) < (len((m)[default__.BRANCH__KEY__IDENTIFIER__FIELD])))) and ((0) < (len((m)[default__.TYPE__FIELD])))) and (_dafny.quantifier(((m).keys).Elements, True, lambda130_))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) == ((True) and (((m)[default__.TYPE__FIELD]) == (default__.BRANCH__KEY__ACTIVE__TYPE))))) and (not ((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) or ((True) and ((default__.BRANCH__KEY__TYPE__PREFIX) < ((m)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]))))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) not in (m)) == ((((m)[default__.TYPE__FIELD]) == (default__.BEACON__KEY__TYPE__VALUE)) or ((default__.BRANCH__KEY__TYPE__PREFIX) < ((m)[default__.TYPE__FIELD]))))

    @staticmethod
    def ToAttributeMap(encryptionContext, encryptedKey):
        def iife64_():
            coll20_ = _dafny.Map()
            compr_25_: _dafny.Seq
            for compr_25_ in ((((encryptionContext).keys) | (_dafny.Set({default__.BRANCH__KEY__FIELD}))) - (_dafny.Set({default__.TABLE__FIELD}))).Elements:
                d_1952_k_: _dafny.Seq = compr_25_
                if software_amazon_cryptography_services_dynamodb_internaldafny_types.default__.IsValid__AttributeName(d_1952_k_):
                    if (d_1952_k_) in ((((encryptionContext).keys) | (_dafny.Set({default__.BRANCH__KEY__FIELD}))) - (_dafny.Set({default__.TABLE__FIELD}))):
                        coll20_[d_1952_k_] = (software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_N((encryptionContext)[default__.HIERARCHY__VERSION]) if (d_1952_k_) == (default__.HIERARCHY__VERSION) else (software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_B(encryptedKey) if (d_1952_k_) == (default__.BRANCH__KEY__FIELD) else software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S((encryptionContext)[d_1952_k_])))
            return _dafny.Map(coll20_)
        return iife64_()
        

    @staticmethod
    def ToBranchKeyContext(item, logicalKeyStoreName):
        def iife65_():
            coll21_ = _dafny.Map()
            compr_26_: _dafny.Seq
            for compr_26_ in ((((item).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD}))) | (_dafny.Set({default__.TABLE__FIELD}))).Elements:
                d_1953_k_: _dafny.Seq = compr_26_
                if (d_1953_k_) in ((((item).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD}))) | (_dafny.Set({default__.TABLE__FIELD}))):
                    coll21_[d_1953_k_] = (((item)[d_1953_k_]).N if (d_1953_k_) == (default__.HIERARCHY__VERSION) else (logicalKeyStoreName if (d_1953_k_) == (default__.TABLE__FIELD) else ((item)[d_1953_k_]).S))
            return _dafny.Map(coll21_)
        return iife65_()
        

    @staticmethod
    def ToBranchKeyMaterials(encryptionContext, plaintextKey):
        d_1954_versionInformation_ = ((encryptionContext)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD] if (default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (encryptionContext) else (encryptionContext)[default__.TYPE__FIELD])
        d_1955_branchKeyVersion_ = _dafny.Seq((d_1954_versionInformation_)[len(default__.BRANCH__KEY__TYPE__PREFIX)::])
        def lambda131_(d_1957_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_1957_e_)

        d_1956_valueOrError0_ = (UTF8.default__.Encode(d_1955_branchKeyVersion_)).MapFailure(lambda131_)
        if (d_1956_valueOrError0_).IsFailure():
            return (d_1956_valueOrError0_).PropagateFailure()
        elif True:
            d_1958_branchKeyVersionUtf8_ = (d_1956_valueOrError0_).Extract()
            d_1959_valueOrError1_ = default__.ExtractCustomEncryptionContext(encryptionContext)
            if (d_1959_valueOrError1_).IsFailure():
                return (d_1959_valueOrError1_).PropagateFailure()
            elif True:
                d_1960_customEncryptionContext_ = (d_1959_valueOrError1_).Extract()
                return Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials_BranchKeyMaterials((encryptionContext)[default__.BRANCH__KEY__IDENTIFIER__FIELD], d_1958_branchKeyVersionUtf8_, d_1960_customEncryptionContext_, plaintextKey))

    @staticmethod
    def ToBeaconKeyMaterials(encryptionContext, plaintextKey):
        d_1961_valueOrError0_ = default__.ExtractCustomEncryptionContext(encryptionContext)
        if (d_1961_valueOrError0_).IsFailure():
            return (d_1961_valueOrError0_).PropagateFailure()
        elif True:
            d_1962_customEncryptionContext_ = (d_1961_valueOrError0_).Extract()
            return Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.BeaconKeyMaterials_BeaconKeyMaterials((encryptionContext)[default__.BRANCH__KEY__IDENTIFIER__FIELD], d_1962_customEncryptionContext_, Wrappers.Option_Some(plaintextKey), Wrappers.Option_None()))

    @staticmethod
    def ExtractCustomEncryptionContext(encryptionContext):
        def iife66_():
            coll22_ = _dafny.Set()
            compr_27_: _dafny.Seq
            for compr_27_ in (encryptionContext).keys.Elements:
                d_1964_k_: _dafny.Seq = compr_27_
                if ((d_1964_k_) in (encryptionContext)) and ((default__.ENCRYPTION__CONTEXT__PREFIX) < (d_1964_k_)):
                    coll22_ = coll22_.union(_dafny.Set([(UTF8.default__.Encode(_dafny.Seq((d_1964_k_)[len(default__.ENCRYPTION__CONTEXT__PREFIX)::])), UTF8.default__.Encode((encryptionContext)[d_1964_k_]))]))
            return _dafny.Set(coll22_)
        d_1963_encodedEncryptionContext_ = iife66_()

        def lambda132_(forall_var_23_):
            d_1966_i_: tuple = forall_var_23_
            return not ((d_1966_i_) in (d_1963_encodedEncryptionContext_)) or ((((d_1966_i_)[0]).is_Success) and (((d_1966_i_)[1]).is_Success))

        d_1965_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier((d_1963_encodedEncryptionContext_).Elements, True, lambda132_), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Unable to encode string")))
        if (d_1965_valueOrError0_).IsFailure():
            return (d_1965_valueOrError0_).PropagateFailure()
        elif True:
            def iife67_():
                coll23_ = _dafny.Map()
                compr_28_: tuple
                for compr_28_ in (d_1963_encodedEncryptionContext_).Elements:
                    d_1967_i_: tuple = compr_28_
                    if (d_1967_i_) in (d_1963_encodedEncryptionContext_):
                        coll23_[((d_1967_i_)[0]).value] = ((d_1967_i_)[1]).value
                return _dafny.Map(coll23_)
            return Wrappers.Result_Success(iife67_()
)

    @staticmethod
    def DecryptOnlyBranchKeyEncryptionContext(branchKeyId, branchKeyVersion, timestamp, logicalKeyStoreName, kmsKeyArn, customEncryptionContext):
        def iife68_():
            coll24_ = _dafny.Map()
            compr_29_: _dafny.Seq
            for compr_29_ in (customEncryptionContext).keys.Elements:
                d_1968_k_: _dafny.Seq = compr_29_
                if (d_1968_k_) in (customEncryptionContext):
                    coll24_[(default__.ENCRYPTION__CONTEXT__PREFIX) + (d_1968_k_)] = (customEncryptionContext)[d_1968_k_]
            return _dafny.Map(coll24_)
        return (_dafny.Map({default__.BRANCH__KEY__IDENTIFIER__FIELD: branchKeyId, default__.TYPE__FIELD: (default__.BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion), default__.KEY__CREATE__TIME: timestamp, default__.TABLE__FIELD: logicalKeyStoreName, default__.KMS__FIELD: kmsKeyArn, default__.HIERARCHY__VERSION: _dafny.Seq("1")})) | (iife68_()
        )

    @staticmethod
    def ActiveBranchKeyEncryptionContext(decryptOnlyEncryptionContext):
        return (decryptOnlyEncryptionContext) | (_dafny.Map({default__.BRANCH__KEY__ACTIVE__VERSION__FIELD: (decryptOnlyEncryptionContext)[default__.TYPE__FIELD], default__.TYPE__FIELD: default__.BRANCH__KEY__ACTIVE__TYPE}))

    @staticmethod
    def BeaconKeyEncryptionContext(decryptOnlyEncryptionContext):
        return (decryptOnlyEncryptionContext) | (_dafny.Map({default__.TYPE__FIELD: default__.BEACON__KEY__TYPE__VALUE}))

    @staticmethod
    def NewVersionFromActiveBranchKeyEncryptionContext(activeBranchKeyEncryptionContext, branchKeyVersion, timestamp):
        return ((activeBranchKeyEncryptionContext) | (_dafny.Map({default__.TYPE__FIELD: (default__.BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion), default__.KEY__CREATE__TIME: timestamp}))) - (_dafny.Set({default__.BRANCH__KEY__ACTIVE__VERSION__FIELD}))

    @staticmethod
    def BranchKeyItem_q(m):
        def lambda133_(forall_var_24_):
            d_1969_k_: _dafny.Seq = forall_var_24_
            return not ((d_1969_k_) in (((m).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD, default__.HIERARCHY__VERSION})))) or (((m)[d_1969_k_]).is_S)

        return ((((((((((((((((((((default__.BRANCH__KEY__IDENTIFIER__FIELD) in (m)) and (((m)[default__.BRANCH__KEY__IDENTIFIER__FIELD]).is_S)) and ((default__.TYPE__FIELD) in (m))) and (((m)[default__.TYPE__FIELD]).is_S)) and ((default__.KEY__CREATE__TIME) in (m))) and (((m)[default__.KEY__CREATE__TIME]).is_S)) and ((default__.HIERARCHY__VERSION) in (m))) and (((m)[default__.HIERARCHY__VERSION]).is_N)) and ((default__.TABLE__FIELD) not in (m))) and ((default__.KMS__FIELD) in (m))) and (((m)[default__.KMS__FIELD]).is_S)) and ((default__.BRANCH__KEY__FIELD) in (m))) and (((m)[default__.BRANCH__KEY__FIELD]).is_B)) and ((0) < (len(((m)[default__.BRANCH__KEY__IDENTIFIER__FIELD]).S)))) and ((0) < (len(((m)[default__.TYPE__FIELD]).S)))) and (_dafny.quantifier((((m).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD, default__.HIERARCHY__VERSION}))).Elements, True, lambda133_))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) == ((True) and ((((m)[default__.TYPE__FIELD]).S) == (default__.BRANCH__KEY__ACTIVE__TYPE))))) and (not ((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) or ((True) and ((default__.BRANCH__KEY__TYPE__PREFIX) < (((m)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]).S))))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) not in (m)) == (((((m)[default__.TYPE__FIELD]).S) == (default__.BEACON__KEY__TYPE__VALUE)) or ((default__.BRANCH__KEY__TYPE__PREFIX) < (((m)[default__.TYPE__FIELD]).S))))) and (software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType(((m)[default__.BRANCH__KEY__FIELD]).B))

    @staticmethod
    def ActiveBranchKeyItem_q(m):
        return ((((default__.BranchKeyItem_q(m)) and ((((m)[default__.TYPE__FIELD]).S) == (default__.BRANCH__KEY__ACTIVE__TYPE))) and ((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m))) and (((m)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]).is_S)) and ((default__.BRANCH__KEY__TYPE__PREFIX) < (((m)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]).S))

    @staticmethod
    def VersionBranchKeyItem_q(m):
        return ((default__.BranchKeyItem_q(m)) and ((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) not in (m))) and ((default__.BRANCH__KEY__TYPE__PREFIX) < (((m)[default__.TYPE__FIELD]).S))

    @staticmethod
    def BeaconKeyItem_q(m):
        return ((default__.BranchKeyItem_q(m)) and ((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) not in (m))) and ((((m)[default__.TYPE__FIELD]).S) == (default__.BEACON__KEY__TYPE__VALUE))

    @_dafny.classproperty
    def BRANCH__KEY__IDENTIFIER__FIELD(instance):
        return _dafny.Seq("branch-key-id")
    @_dafny.classproperty
    def TYPE__FIELD(instance):
        return _dafny.Seq("type")
    @_dafny.classproperty
    def KEY__CREATE__TIME(instance):
        return _dafny.Seq("create-time")
    @_dafny.classproperty
    def HIERARCHY__VERSION(instance):
        return _dafny.Seq("hierarchy-version")
    @_dafny.classproperty
    def TABLE__FIELD(instance):
        return _dafny.Seq("tablename")
    @_dafny.classproperty
    def KMS__FIELD(instance):
        return _dafny.Seq("kms-arn")
    @_dafny.classproperty
    def BRANCH__KEY__FIELD(instance):
        return _dafny.Seq("enc")
    @_dafny.classproperty
    def BRANCH__KEY__ACTIVE__VERSION__FIELD(instance):
        return _dafny.Seq("version")
    @_dafny.classproperty
    def BRANCH__KEY__ACTIVE__TYPE(instance):
        return _dafny.Seq("branch:ACTIVE")
    @_dafny.classproperty
    def BRANCH__KEY__TYPE__PREFIX(instance):
        return _dafny.Seq("branch:version:")
    @_dafny.classproperty
    def BEACON__KEY__TYPE__VALUE(instance):
        return _dafny.Seq("beacon:ACTIVE")
    @_dafny.classproperty
    def ENCRYPTION__CONTEXT__PREFIX(instance):
        return _dafny.Seq("aws-crypto-ec:")

class BranchKeyContext:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})

class BranchKeyItem:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})

class ActiveBranchKeyItem:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})

class VersionBranchKeyItem:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})

class BeaconKeyItem:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})
