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
import software_amazon_cryptography_primitives_internaldafny_types
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
import AesKdfCtr
import Relations
import Seq_MergeSort
import Math
import Seq
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
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils

# Module: Structure

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BranchKeyContext_q(m):
        def lambda7_(forall_var_4_):
            d_99_k_: _dafny.Seq = forall_var_4_
            return not ((d_99_k_) in ((m).keys)) or (software_amazon_cryptography_services_dynamodb_internaldafny_types.default__.IsValid__AttributeName(d_99_k_))

        return (((((((((((((default__.BRANCH__KEY__IDENTIFIER__FIELD) in (m)) and ((default__.TYPE__FIELD) in (m))) and ((default__.KEY__CREATE__TIME) in (m))) and ((default__.HIERARCHY__VERSION) in (m))) and ((default__.TABLE__FIELD) in (m))) and ((default__.KMS__FIELD) in (m))) and ((default__.BRANCH__KEY__FIELD) not in ((m).keys))) and ((0) < (len((m)[default__.BRANCH__KEY__IDENTIFIER__FIELD])))) and ((0) < (len((m)[default__.TYPE__FIELD])))) and (_dafny.quantifier(((m).keys).Elements, True, lambda7_))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) == ((True) and (((m)[default__.TYPE__FIELD]) == (default__.BRANCH__KEY__ACTIVE__TYPE))))) and (not ((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) or ((True) and ((default__.BRANCH__KEY__TYPE__PREFIX) < ((m)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]))))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) not in (m)) == ((((m)[default__.TYPE__FIELD]) == (default__.BEACON__KEY__TYPE__VALUE)) or ((default__.BRANCH__KEY__TYPE__PREFIX) < ((m)[default__.TYPE__FIELD]))))

    @staticmethod
    def ToAttributeMap(encryptionContext, encryptedKey):
        def iife2_():
            coll2_ = _dafny.Map()
            compr_2_: _dafny.Seq
            for compr_2_ in ((((encryptionContext).keys) | (_dafny.Set({default__.BRANCH__KEY__FIELD}))) - (_dafny.Set({default__.TABLE__FIELD}))).Elements:
                d_100_k_: _dafny.Seq = compr_2_
                if software_amazon_cryptography_services_dynamodb_internaldafny_types.default__.IsValid__AttributeName(d_100_k_):
                    if (d_100_k_) in ((((encryptionContext).keys) | (_dafny.Set({default__.BRANCH__KEY__FIELD}))) - (_dafny.Set({default__.TABLE__FIELD}))):
                        coll2_[d_100_k_] = (software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_N((encryptionContext)[default__.HIERARCHY__VERSION]) if (d_100_k_) == (default__.HIERARCHY__VERSION) else (software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_B(encryptedKey) if (d_100_k_) == (default__.BRANCH__KEY__FIELD) else software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S((encryptionContext)[d_100_k_])))
            return _dafny.Map(coll2_)
        return iife2_()
        

    @staticmethod
    def ToBranchKeyContext(item, logicalKeyStoreName):
        def iife3_():
            coll3_ = _dafny.Map()
            compr_3_: _dafny.Seq
            for compr_3_ in ((((item).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD}))) | (_dafny.Set({default__.TABLE__FIELD}))).Elements:
                d_101_k_: _dafny.Seq = compr_3_
                if (d_101_k_) in ((((item).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD}))) | (_dafny.Set({default__.TABLE__FIELD}))):
                    coll3_[d_101_k_] = (((item)[d_101_k_]).N if (d_101_k_) == (default__.HIERARCHY__VERSION) else (logicalKeyStoreName if (d_101_k_) == (default__.TABLE__FIELD) else ((item)[d_101_k_]).S))
            return _dafny.Map(coll3_)
        return iife3_()
        

    @staticmethod
    def ToBranchKeyMaterials(encryptionContext, plaintextKey):
        d_102_versionInformation_ = ((encryptionContext)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD] if (default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (encryptionContext) else (encryptionContext)[default__.TYPE__FIELD])
        d_103_branchKeyVersion_ = _dafny.Seq((d_102_versionInformation_)[len(default__.BRANCH__KEY__TYPE__PREFIX)::])
        def lambda8_(d_105_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(d_105_e_)

        d_104_valueOrError0_ = (UTF8.default__.Encode(d_103_branchKeyVersion_)).MapFailure(lambda8_)
        if (d_104_valueOrError0_).IsFailure():
            return (d_104_valueOrError0_).PropagateFailure()
        elif True:
            d_106_branchKeyVersionUtf8_ = (d_104_valueOrError0_).Extract()
            d_107_valueOrError1_ = default__.ExtractCustomEncryptionContext(encryptionContext)
            if (d_107_valueOrError1_).IsFailure():
                return (d_107_valueOrError1_).PropagateFailure()
            elif True:
                d_108_customEncryptionContext_ = (d_107_valueOrError1_).Extract()
                return Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials_BranchKeyMaterials((encryptionContext)[default__.BRANCH__KEY__IDENTIFIER__FIELD], d_106_branchKeyVersionUtf8_, d_108_customEncryptionContext_, plaintextKey))

    @staticmethod
    def ToBeaconKeyMaterials(encryptionContext, plaintextKey):
        d_109_valueOrError0_ = default__.ExtractCustomEncryptionContext(encryptionContext)
        if (d_109_valueOrError0_).IsFailure():
            return (d_109_valueOrError0_).PropagateFailure()
        elif True:
            d_110_customEncryptionContext_ = (d_109_valueOrError0_).Extract()
            return Wrappers.Result_Success(software_amazon_cryptography_keystore_internaldafny_types.BeaconKeyMaterials_BeaconKeyMaterials((encryptionContext)[default__.BRANCH__KEY__IDENTIFIER__FIELD], d_110_customEncryptionContext_, Wrappers.Option_Some(plaintextKey), Wrappers.Option_None()))

    @staticmethod
    def ExtractCustomEncryptionContext(encryptionContext):
        def iife4_():
            coll4_ = _dafny.Set()
            compr_4_: _dafny.Seq
            for compr_4_ in (encryptionContext).keys.Elements:
                d_112_k_: _dafny.Seq = compr_4_
                if ((d_112_k_) in (encryptionContext)) and ((default__.ENCRYPTION__CONTEXT__PREFIX) < (d_112_k_)):
                    coll4_ = coll4_.union(_dafny.Set([(UTF8.default__.Encode(_dafny.Seq((d_112_k_)[len(default__.ENCRYPTION__CONTEXT__PREFIX)::])), UTF8.default__.Encode((encryptionContext)[d_112_k_]))]))
            return _dafny.Set(coll4_)
        d_111_encodedEncryptionContext_ = iife4_()

        def lambda9_(forall_var_5_):
            d_114_i_: tuple = forall_var_5_
            return not ((d_114_i_) in (d_111_encodedEncryptionContext_)) or ((((d_114_i_)[0]).is_Success) and (((d_114_i_)[1]).is_Success))

        d_113_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier((d_111_encodedEncryptionContext_).Elements, True, lambda9_), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Unable to encode string")))
        if (d_113_valueOrError0_).IsFailure():
            return (d_113_valueOrError0_).PropagateFailure()
        elif True:
            def iife5_():
                coll5_ = _dafny.Map()
                compr_5_: tuple
                for compr_5_ in (d_111_encodedEncryptionContext_).Elements:
                    d_115_i_: tuple = compr_5_
                    if (d_115_i_) in (d_111_encodedEncryptionContext_):
                        coll5_[((d_115_i_)[0]).value] = ((d_115_i_)[1]).value
                return _dafny.Map(coll5_)
            return Wrappers.Result_Success(iife5_()
)

    @staticmethod
    def DecryptOnlyBranchKeyEncryptionContext(branchKeyId, branchKeyVersion, timestamp, logicalKeyStoreName, kmsKeyArn, customEncryptionContext):
        def iife6_():
            coll6_ = _dafny.Map()
            compr_6_: _dafny.Seq
            for compr_6_ in (customEncryptionContext).keys.Elements:
                d_116_k_: _dafny.Seq = compr_6_
                if (d_116_k_) in (customEncryptionContext):
                    coll6_[(default__.ENCRYPTION__CONTEXT__PREFIX) + (d_116_k_)] = (customEncryptionContext)[d_116_k_]
            return _dafny.Map(coll6_)
        return (_dafny.Map({default__.BRANCH__KEY__IDENTIFIER__FIELD: branchKeyId, default__.TYPE__FIELD: (default__.BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion), default__.KEY__CREATE__TIME: timestamp, default__.TABLE__FIELD: logicalKeyStoreName, default__.KMS__FIELD: kmsKeyArn, default__.HIERARCHY__VERSION: _dafny.Seq("1")})) | (iife6_()
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
        def lambda10_(forall_var_6_):
            d_117_k_: _dafny.Seq = forall_var_6_
            return not ((d_117_k_) in (((m).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD, default__.HIERARCHY__VERSION})))) or (((m)[d_117_k_]).is_S)

        return ((((((((((((((((((((default__.BRANCH__KEY__IDENTIFIER__FIELD) in (m)) and (((m)[default__.BRANCH__KEY__IDENTIFIER__FIELD]).is_S)) and ((default__.TYPE__FIELD) in (m))) and (((m)[default__.TYPE__FIELD]).is_S)) and ((default__.KEY__CREATE__TIME) in (m))) and (((m)[default__.KEY__CREATE__TIME]).is_S)) and ((default__.HIERARCHY__VERSION) in (m))) and (((m)[default__.HIERARCHY__VERSION]).is_N)) and ((default__.TABLE__FIELD) not in (m))) and ((default__.KMS__FIELD) in (m))) and (((m)[default__.KMS__FIELD]).is_S)) and ((default__.BRANCH__KEY__FIELD) in (m))) and (((m)[default__.BRANCH__KEY__FIELD]).is_B)) and ((0) < (len(((m)[default__.BRANCH__KEY__IDENTIFIER__FIELD]).S)))) and ((0) < (len(((m)[default__.TYPE__FIELD]).S)))) and (_dafny.quantifier((((m).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD, default__.HIERARCHY__VERSION}))).Elements, True, lambda10_))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) == ((True) and ((((m)[default__.TYPE__FIELD]).S) == (default__.BRANCH__KEY__ACTIVE__TYPE))))) and (not ((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) or ((True) and ((default__.BRANCH__KEY__TYPE__PREFIX) < (((m)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]).S))))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) not in (m)) == (((((m)[default__.TYPE__FIELD]).S) == (default__.BEACON__KEY__TYPE__VALUE)) or ((default__.BRANCH__KEY__TYPE__PREFIX) < (((m)[default__.TYPE__FIELD]).S))))) and (software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType(((m)[default__.BRANCH__KEY__FIELD]).B))

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
