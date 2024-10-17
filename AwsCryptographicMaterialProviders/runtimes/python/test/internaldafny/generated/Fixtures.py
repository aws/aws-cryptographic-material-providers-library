import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_material_providers.internaldafny.generated.GetKeys as GetKeys
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
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
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_material_providers.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_material_providers.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_material_providers.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_material_providers.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_material_providers.internaldafny.generated.CMM as CMM
import aws_cryptographic_material_providers.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_material_providers.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_material_providers.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_material_providers.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_material_providers.internaldafny.generated.Utils as Utils
import aws_cryptographic_material_providers.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_material_providers.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
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
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas

# Module: Fixtures

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncodeEncryptionContext(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_0_encodedEncryptionContext_: _dafny.Set
        def iife0_():
            coll0_ = _dafny.Set()
            compr_0_: _dafny.Seq
            for compr_0_ in (input).keys.Elements:
                d_1_k_: _dafny.Seq = compr_0_
                if (d_1_k_) in (input):
                    coll0_ = coll0_.union(_dafny.Set([(UTF8.default__.Encode(d_1_k_), UTF8.default__.Encode((input)[d_1_k_]), d_1_k_)]))
            return _dafny.Set(coll0_)
        d_0_encodedEncryptionContext_ = iife0_()
        
        d_2_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def lambda0_(forall_var_0_):
            def iife1_(_pat_let0_0):
                def iife2_(d_4_encoded_):
                    return ((d_4_encoded_).is_Success) and (((d_3_i_)[2]) == ((d_4_encoded_).value))
                return iife2_(_pat_let0_0)
            d_3_i_: tuple = forall_var_0_
            return not ((d_3_i_) in (d_0_encodedEncryptionContext_)) or (((((d_3_i_)[0]).is_Success) and (((d_3_i_)[1]).is_Success)) and (iife1_(UTF8.default__.Decode(((d_3_i_)[0]).value))))

        d_2_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier((d_0_encodedEncryptionContext_).Elements, True, lambda0_), _dafny.Seq("Unable to encode string"))
        if (d_2_valueOrError0_).IsFailure():
            output = (d_2_valueOrError0_).PropagateFailure()
            return output
        def iife3_():
            coll1_ = _dafny.Map()
            compr_1_: tuple
            for compr_1_ in (d_0_encodedEncryptionContext_).Elements:
                d_5_i_: tuple = compr_1_
                if (d_5_i_) in (d_0_encodedEncryptionContext_):
                    coll1_[((d_5_i_)[0]).value] = ((d_5_i_)[1]).value
            return _dafny.Map(coll1_)
        output = Wrappers.Result_Success(iife3_()
)
        return output

    @staticmethod
    def DecodeEncryptionContext(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_0_decodedEncryptionContext_: _dafny.Set
        def iife0_():
            coll0_ = _dafny.Set()
            compr_0_: _dafny.Seq
            for compr_0_ in (input).keys.Elements:
                d_1_k_: _dafny.Seq = compr_0_
                if (d_1_k_) in (input):
                    coll0_ = coll0_.union(_dafny.Set([(UTF8.default__.Decode(d_1_k_), UTF8.default__.Decode((input)[d_1_k_]), d_1_k_)]))
            return _dafny.Set(coll0_)
        d_0_decodedEncryptionContext_ = iife0_()
        
        d_2_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def lambda0_(forall_var_0_):
            def iife1_(_pat_let1_0):
                def iife2_(d_4_decoded_):
                    return ((d_4_decoded_).is_Success) and (((d_3_i_)[2]) == ((d_4_decoded_).value))
                return iife2_(_pat_let1_0)
            d_3_i_: tuple = forall_var_0_
            return not ((d_3_i_) in (d_0_decodedEncryptionContext_)) or (((((d_3_i_)[0]).is_Success) and (((d_3_i_)[1]).is_Success)) and (iife1_(UTF8.default__.Encode(((d_3_i_)[0]).value))))

        d_2_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier((d_0_decodedEncryptionContext_).Elements, True, lambda0_), _dafny.Seq("Unable to decode string"))
        if (d_2_valueOrError0_).IsFailure():
            output = (d_2_valueOrError0_).PropagateFailure()
            return output
        def iife3_():
            coll1_ = _dafny.Map()
            compr_1_: tuple
            for compr_1_ in (d_0_decodedEncryptionContext_).Elements:
                d_5_i_: tuple = compr_1_
                if (d_5_i_) in (d_0_decodedEncryptionContext_):
                    coll1_[((d_5_i_)[0]).value] = ((d_5_i_)[1]).value
            return _dafny.Map(coll1_)
        output = Wrappers.Result_Success(iife3_()
)
        return output

    @_dafny.classproperty
    def branchKeyStoreName(instance):
        return _dafny.Seq("KeyStoreDdbTable")
    @_dafny.classproperty
    def logicalKeyStoreName(instance):
        return default__.branchKeyStoreName
    @_dafny.classproperty
    def MrkArnEast(instance):
        return _dafny.Seq("arn:aws:kms:us-east-1:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7")
    @_dafny.classproperty
    def KmsConfigEast(instance):
        return AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(default__.MrkArnEast)
    @_dafny.classproperty
    def MrkArnWest(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7")
    @_dafny.classproperty
    def KmsConfigWest(instance):
        return AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(default__.MrkArnWest)
    @_dafny.classproperty
    def KmsMrkConfigEast(instance):
        return AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsMRKeyArn(default__.MrkArnEast)
    @_dafny.classproperty
    def KmsMrkConfigWest(instance):
        return AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsMRKeyArn(default__.MrkArnWest)
    @_dafny.classproperty
    def KmsSrkConfigEast(instance):
        return AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(default__.MrkArnEast)
    @_dafny.classproperty
    def KmsSrkConfigWest(instance):
        return AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsKeyArn(default__.MrkArnWest)
    @_dafny.classproperty
    def MrkArnAP(instance):
        return _dafny.Seq("arn:aws:kms:ap-south-2:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7")
    @_dafny.classproperty
    def KmsMrkConfigAP(instance):
        return AwsCryptographyKeyStoreTypes.KMSConfiguration_kmsMRKeyArn(default__.MrkArnAP)
    @_dafny.classproperty
    def branchKeyId(instance):
        return _dafny.Seq("75789115-1deb-4fe3-a2ec-be9e885d1945")
    @_dafny.classproperty
    def branchKeyIdActiveVersion(instance):
        return _dafny.Seq("fed7ad33-0774-4f97-aa5e-6c766fc8af9f")
    @_dafny.classproperty
    def branchKeyIdWithEC(instance):
        return _dafny.Seq("4bb57643-07c1-419e-92ad-0df0df149d7c")
    @_dafny.classproperty
    def branchKeyIdActiveVersionUtf8Bytes(instance):
        return _dafny.Seq([102, 101, 100, 55, 97, 100, 51, 51, 45, 48, 55, 55, 52, 45, 52, 102, 57, 55, 45, 97, 97, 53, 101, 45, 54, 99, 55, 54, 54, 102, 99, 56, 97, 102, 57, 102])
    @_dafny.classproperty
    def keyArn(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126")
    @_dafny.classproperty
    def keyId(instance):
        return _dafny.Seq("9d989aa2-2f9c-438c-a745-cc57d3ad0126")
    @_dafny.classproperty
    def mrkRsaKeyArn(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/mrk-63d386cb70614ea59b32ad65c9315297")
    @_dafny.classproperty
    def KmsMrkEC(instance):
        return _dafny.Map({UTF8.default__.EncodeAscii(_dafny.Seq("abc")): UTF8.default__.EncodeAscii(_dafny.Seq("123"))})
    @_dafny.classproperty
    def EastBranchKey(instance):
        return _dafny.Seq("MyEastBranch2")
    @_dafny.classproperty
    def WestBranchKey(instance):
        return _dafny.Seq("MyWestBranch2")
    @_dafny.classproperty
    def publicKeyArn(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f")
    @_dafny.classproperty
    def postalHornKeyArn(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8")
    @_dafny.classproperty
    def kmsKeyAlias(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:alias/postalHorn")
    @_dafny.classproperty
    def postalHornBranchKeyId(instance):
        return _dafny.Seq("682dfba7-4c35-491d-8d6a-5a9c56194061")
    @_dafny.classproperty
    def postalHornBranchKeyActiveVersion(instance):
        return _dafny.Seq("6b7a8ef4-8c1c-4f63-b196-a6ef7e496e50")
    @_dafny.classproperty
    def lyingBranchKeyId(instance):
        return _dafny.Seq("kms-arn-attribute-is-lying")
    @_dafny.classproperty
    def lyingBranchKeyDecryptOnlyVersion(instance):
        return _dafny.Seq("129c5c87-308a-41c9-8b9d-a27f66e915f4")
