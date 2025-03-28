import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_material_providers.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_Sequence as StandardLibrary_Sequence
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn

# Module: Structure

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BranchKeyContext_q(m):
        def lambda0_(forall_var_0_):
            d_0_k_: _dafny.Seq = forall_var_0_
            return not ((d_0_k_) in ((m).keys)) or (ComAmazonawsDynamodbTypes.default__.IsValid__AttributeName(d_0_k_))

        return ((((((((((((((default__.BRANCH__KEY__IDENTIFIER__FIELD) in (m)) and ((default__.TYPE__FIELD) in (m))) and ((default__.KEY__CREATE__TIME) in (m))) and ((default__.HIERARCHY__VERSION) in (m))) and ((default__.TABLE__FIELD) in (m))) and ((default__.KMS__FIELD) in (m))) and (ComAmazonawsKmsTypes.default__.IsValid__KeyIdType((m)[default__.KMS__FIELD]))) and ((default__.BRANCH__KEY__FIELD) not in ((m).keys))) and ((0) < (len((m)[default__.BRANCH__KEY__IDENTIFIER__FIELD])))) and ((0) < (len((m)[default__.TYPE__FIELD])))) and (_dafny.quantifier(((m).keys).Elements, True, lambda0_))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) == ((True) and (((m)[default__.TYPE__FIELD]) == (default__.BRANCH__KEY__ACTIVE__TYPE))))) and (not ((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) or ((True) and ((default__.BRANCH__KEY__TYPE__PREFIX) < ((m)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]))))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) not in (m)) == ((((m)[default__.TYPE__FIELD]) == (default__.BEACON__KEY__TYPE__VALUE)) or ((default__.BRANCH__KEY__TYPE__PREFIX) < ((m)[default__.TYPE__FIELD]))))

    @staticmethod
    def ToAttributeMap(encryptionContext, encryptedKey):
        def iife0_():
            coll0_ = _dafny.Map()
            compr_0_: _dafny.Seq
            for compr_0_ in ((((encryptionContext).keys) | (_dafny.Set({default__.BRANCH__KEY__FIELD}))) - (_dafny.Set({default__.TABLE__FIELD}))).Elements:
                d_0_k_: _dafny.Seq = compr_0_
                if ComAmazonawsDynamodbTypes.AttributeName._Is(d_0_k_):
                    if (d_0_k_) in ((((encryptionContext).keys) | (_dafny.Set({default__.BRANCH__KEY__FIELD}))) - (_dafny.Set({default__.TABLE__FIELD}))):
                        coll0_[d_0_k_] = (ComAmazonawsDynamodbTypes.AttributeValue_N((encryptionContext)[default__.HIERARCHY__VERSION]) if (d_0_k_) == (default__.HIERARCHY__VERSION) else (ComAmazonawsDynamodbTypes.AttributeValue_B(encryptedKey) if (d_0_k_) == (default__.BRANCH__KEY__FIELD) else ComAmazonawsDynamodbTypes.AttributeValue_S((encryptionContext)[d_0_k_])))
            return _dafny.Map(coll0_)
        return iife0_()
        

    @staticmethod
    def ToBranchKeyContext(item, logicalKeyStoreName):
        def iife0_():
            coll0_ = _dafny.Map()
            compr_0_: _dafny.Seq
            for compr_0_ in ((((item).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD}))) | (_dafny.Set({default__.TABLE__FIELD}))).Elements:
                d_0_k_: _dafny.Seq = compr_0_
                if (d_0_k_) in ((((item).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD}))) | (_dafny.Set({default__.TABLE__FIELD}))):
                    coll0_[d_0_k_] = (((item)[d_0_k_]).N if (d_0_k_) == (default__.HIERARCHY__VERSION) else (logicalKeyStoreName if (d_0_k_) == (default__.TABLE__FIELD) else ((item)[d_0_k_]).S))
            return _dafny.Map(coll0_)
        return iife0_()
        

    @staticmethod
    def ToBranchKeyMaterials(encryptionContext, plaintextKey):
        d_0_versionInformation_ = ((encryptionContext)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD] if (default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (encryptionContext) else (encryptionContext)[default__.TYPE__FIELD])
        d_1_branchKeyVersion_ = _dafny.Seq((d_0_versionInformation_)[len(default__.BRANCH__KEY__TYPE__PREFIX)::])
        def lambda0_(d_3_e_):
            return AwsCryptographyKeyStoreTypes.Error_KeyStoreException(d_3_e_)

        d_2_valueOrError0_ = (UTF8.default__.Encode(d_1_branchKeyVersion_)).MapFailure(lambda0_)
        if (d_2_valueOrError0_).IsFailure():
            return (d_2_valueOrError0_).PropagateFailure()
        elif True:
            d_4_branchKeyVersionUtf8_ = (d_2_valueOrError0_).Extract()
            d_5_valueOrError1_ = default__.ExtractCustomEncryptionContext(encryptionContext)
            if (d_5_valueOrError1_).IsFailure():
                return (d_5_valueOrError1_).PropagateFailure()
            elif True:
                d_6_customEncryptionContext_ = (d_5_valueOrError1_).Extract()
                return Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.BranchKeyMaterials_BranchKeyMaterials((encryptionContext)[default__.BRANCH__KEY__IDENTIFIER__FIELD], d_4_branchKeyVersionUtf8_, d_6_customEncryptionContext_, plaintextKey))

    @staticmethod
    def ToBeaconKeyMaterials(encryptionContext, plaintextKey):
        d_0_valueOrError0_ = default__.ExtractCustomEncryptionContext(encryptionContext)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_customEncryptionContext_ = (d_0_valueOrError0_).Extract()
            return Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.BeaconKeyMaterials_BeaconKeyMaterials((encryptionContext)[default__.BRANCH__KEY__IDENTIFIER__FIELD], d_1_customEncryptionContext_, Wrappers.Option_Some(plaintextKey), Wrappers.Option_None()))

    @staticmethod
    def ExtractCustomEncryptionContext(encryptionContext):
        def iife0_():
            coll0_ = _dafny.Set()
            compr_0_: _dafny.Seq
            for compr_0_ in (encryptionContext).keys.Elements:
                d_1_k_: _dafny.Seq = compr_0_
                if ((d_1_k_) in (encryptionContext)) and ((default__.ENCRYPTION__CONTEXT__PREFIX) < (d_1_k_)):
                    coll0_ = coll0_.union(_dafny.Set([(UTF8.default__.Encode(_dafny.Seq((d_1_k_)[len(default__.ENCRYPTION__CONTEXT__PREFIX)::])), UTF8.default__.Encode((encryptionContext)[d_1_k_]))]))
            return _dafny.Set(coll0_)
        d_0_encodedEncryptionContext_ = iife0_()

        def lambda0_(forall_var_0_):
            d_3_i_: tuple = forall_var_0_
            return not ((d_3_i_) in (d_0_encodedEncryptionContext_)) or ((((d_3_i_)[0]).is_Success) and (((d_3_i_)[1]).is_Success))

        d_2_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier((d_0_encodedEncryptionContext_).Elements, True, lambda0_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Unable to encode string")))
        if (d_2_valueOrError0_).IsFailure():
            return (d_2_valueOrError0_).PropagateFailure()
        elif True:
            def iife1_():
                coll1_ = _dafny.Map()
                compr_1_: tuple
                for compr_1_ in (d_0_encodedEncryptionContext_).Elements:
                    d_4_i_: tuple = compr_1_
                    if (d_4_i_) in (d_0_encodedEncryptionContext_):
                        coll1_[((d_4_i_)[0]).value] = ((d_4_i_)[1]).value
                return _dafny.Map(coll1_)
            return Wrappers.Result_Success(iife1_()
)

    @staticmethod
    def DecryptOnlyBranchKeyEncryptionContext(branchKeyId, branchKeyVersion, timestamp, logicalKeyStoreName, kmsKeyArn, customEncryptionContext):
        def iife0_():
            coll0_ = _dafny.Map()
            compr_0_: _dafny.Seq
            for compr_0_ in (customEncryptionContext).keys.Elements:
                d_0_k_: _dafny.Seq = compr_0_
                if (d_0_k_) in (customEncryptionContext):
                    coll0_[(default__.ENCRYPTION__CONTEXT__PREFIX) + (d_0_k_)] = (customEncryptionContext)[d_0_k_]
            return _dafny.Map(coll0_)
        return (_dafny.Map({default__.BRANCH__KEY__IDENTIFIER__FIELD: branchKeyId, default__.TYPE__FIELD: (default__.BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion), default__.KEY__CREATE__TIME: timestamp, default__.TABLE__FIELD: logicalKeyStoreName, default__.KMS__FIELD: kmsKeyArn, default__.HIERARCHY__VERSION: _dafny.Seq("1")})) | (iife0_()
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
        def lambda0_(forall_var_0_):
            d_0_k_: _dafny.Seq = forall_var_0_
            return not ((d_0_k_) in (((m).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD, default__.HIERARCHY__VERSION})))) or (((m)[d_0_k_]).is_S)

        return (((((((((((((((((((((default__.BRANCH__KEY__IDENTIFIER__FIELD) in (m)) and (((m)[default__.BRANCH__KEY__IDENTIFIER__FIELD]).is_S)) and ((default__.TYPE__FIELD) in (m))) and (((m)[default__.TYPE__FIELD]).is_S)) and ((default__.KEY__CREATE__TIME) in (m))) and (((m)[default__.KEY__CREATE__TIME]).is_S)) and ((default__.HIERARCHY__VERSION) in (m))) and (((m)[default__.HIERARCHY__VERSION]).is_N)) and ((default__.TABLE__FIELD) not in (m))) and ((default__.KMS__FIELD) in (m))) and (((m)[default__.KMS__FIELD]).is_S)) and (ComAmazonawsKmsTypes.default__.IsValid__KeyIdType(((m)[default__.KMS__FIELD]).S))) and ((default__.BRANCH__KEY__FIELD) in (m))) and (((m)[default__.BRANCH__KEY__FIELD]).is_B)) and ((0) < (len(((m)[default__.BRANCH__KEY__IDENTIFIER__FIELD]).S)))) and ((0) < (len(((m)[default__.TYPE__FIELD]).S)))) and (_dafny.quantifier((((m).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD, default__.HIERARCHY__VERSION}))).Elements, True, lambda0_))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) == ((True) and ((((m)[default__.TYPE__FIELD]).S) == (default__.BRANCH__KEY__ACTIVE__TYPE))))) and (not ((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) or ((True) and ((default__.BRANCH__KEY__TYPE__PREFIX) < (((m)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]).S))))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) not in (m)) == (((((m)[default__.TYPE__FIELD]).S) == (default__.BEACON__KEY__TYPE__VALUE)) or ((default__.BRANCH__KEY__TYPE__PREFIX) < (((m)[default__.TYPE__FIELD]).S))))) and (ComAmazonawsKmsTypes.default__.IsValid__CiphertextType(((m)[default__.BRANCH__KEY__FIELD]).B))

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
    def _Is(source__):
        d_0_m_: _dafny.Map = source__
        return default__.BranchKeyContext_q(d_0_m_)

class BranchKeyItem:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})
    def _Is(source__):
        d_1_m_: _dafny.Map = source__
        return default__.BranchKeyItem_q(d_1_m_)

class ActiveBranchKeyItem:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})
    def _Is(source__):
        d_2_m_: _dafny.Map = source__
        return default__.ActiveBranchKeyItem_q(d_2_m_)

class VersionBranchKeyItem:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})
    def _Is(source__):
        d_3_m_: _dafny.Map = source__
        return default__.VersionBranchKeyItem_q(d_3_m_)

class BeaconKeyItem:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})
    def _Is(source__):
        d_4_m_: _dafny.Map = source__
        return default__.BeaconKeyItem_q(d_4_m_)
