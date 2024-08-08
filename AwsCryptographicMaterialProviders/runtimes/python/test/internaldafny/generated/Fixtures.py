import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.Actions as Actions
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
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
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.Utils as Utils
import aws_cryptographic_materialproviders.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas

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
        d_6_decodedEncryptionContext_: _dafny.Set
        def iife4_():
            coll2_ = _dafny.Set()
            compr_2_: _dafny.Seq
            for compr_2_ in (input).keys.Elements:
                d_7_k_: _dafny.Seq = compr_2_
                if (d_7_k_) in (input):
                    coll2_ = coll2_.union(_dafny.Set([(UTF8.default__.Decode(d_7_k_), UTF8.default__.Decode((input)[d_7_k_]), d_7_k_)]))
            return _dafny.Set(coll2_)
        d_6_decodedEncryptionContext_ = iife4_()
        
        d_8_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def lambda1_(forall_var_1_):
            def iife5_(_pat_let1_0):
                def iife6_(d_10_decoded_):
                    return ((d_10_decoded_).is_Success) and (((d_9_i_)[2]) == ((d_10_decoded_).value))
                return iife6_(_pat_let1_0)
            d_9_i_: tuple = forall_var_1_
            return not ((d_9_i_) in (d_6_decodedEncryptionContext_)) or (((((d_9_i_)[0]).is_Success) and (((d_9_i_)[1]).is_Success)) and (iife5_(UTF8.default__.Encode(((d_9_i_)[0]).value))))

        d_8_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier((d_6_decodedEncryptionContext_).Elements, True, lambda1_), _dafny.Seq("Unable to decode string"))
        if (d_8_valueOrError0_).IsFailure():
            output = (d_8_valueOrError0_).PropagateFailure()
            return output
        def iife7_():
            coll3_ = _dafny.Map()
            compr_3_: tuple
            for compr_3_ in (d_6_decodedEncryptionContext_).Elements:
                d_11_i_: tuple = compr_3_
                if (d_11_i_) in (d_6_decodedEncryptionContext_):
                    coll3_[((d_11_i_)[0]).value] = ((d_11_i_)[1]).value
            return _dafny.Map(coll3_)
        output = Wrappers.Result_Success(iife7_()
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
