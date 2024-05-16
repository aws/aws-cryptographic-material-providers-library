import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_materialproviders.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
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
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt

# Module: aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StringifyEncryptionContext(utf8EncCtx):
        def lambda0_(exists_var_0_):
            d_76_r_: Wrappers.Result = exists_var_0_
            return ((d_76_r_) in ((d_74_stringifyResults_).values)) and ((d_76_r_).is_Failure)

        if (len(utf8EncCtx)) == (0):
            return Wrappers.Result_Success(_dafny.Map({}))
        elif True:
            def iife0_():
                coll0_ = _dafny.Map()
                compr_0_: _dafny.Seq
                for compr_0_ in ((utf8EncCtx).keys).Elements:
                    d_75_utf8Key_: _dafny.Seq = compr_0_
                    if UTF8.ValidUTF8Bytes._Is(d_75_utf8Key_):
                        if (d_75_utf8Key_) in ((utf8EncCtx).keys):
                            coll0_[d_75_utf8Key_] = default__.StringifyEncryptionContextPair(d_75_utf8Key_, (utf8EncCtx)[d_75_utf8Key_])
                return _dafny.Map(coll0_)
            d_74_stringifyResults_ = iife0_()

            if _dafny.quantifier(((d_74_stringifyResults_).values).Elements, False, lambda0_):
                return Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context contains invalid UTF8")))
            elif True:
                def lambda1_(forall_var_0_):
                    def lambda2_(forall_var_1_):
                        d_79_k_k_: _dafny.Seq = forall_var_1_
                        return not (((d_78_k_) in (d_74_stringifyResults_)) and ((d_79_k_k_) in (d_74_stringifyResults_))) or (not ((d_78_k_) != (d_79_k_k_)) or (((((d_74_stringifyResults_)[d_78_k_]).value)[0]) != ((((d_74_stringifyResults_)[d_79_k_k_]).value)[0])))

                    d_78_k_: _dafny.Seq = forall_var_0_
                    return _dafny.quantifier((d_74_stringifyResults_).keys.Elements, True, lambda2_)

                d_77_stringKeysUnique_ = _dafny.quantifier((d_74_stringifyResults_).keys.Elements, True, lambda1_)
                if not(d_77_stringKeysUnique_):
                    return Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context keys are not unique")))
                elif True:
                    def iife1_():
                        coll1_ = _dafny.Map()
                        compr_1_: Wrappers.Result
                        for compr_1_ in ((d_74_stringifyResults_).values).Elements:
                            d_80_r_: Wrappers.Result = compr_1_
                            if (d_80_r_) in ((d_74_stringifyResults_).values):
                                coll1_[((d_80_r_).value)[0]] = ((d_80_r_).value)[1]
                        return _dafny.Map(coll1_)
                    return Wrappers.Result_Success(iife1_()
)

    @staticmethod
    def StringifyEncryptionContextPair(utf8Key, utf8Value):
        d_81_valueOrError0_ = (UTF8.default__.Decode(utf8Key)).MapFailure(default__.WrapStringToError)
        if (d_81_valueOrError0_).IsFailure():
            return (d_81_valueOrError0_).PropagateFailure()
        elif True:
            d_82_key_ = (d_81_valueOrError0_).Extract()
            d_83_valueOrError1_ = (UTF8.default__.Decode(utf8Value)).MapFailure(default__.WrapStringToError)
            if (d_83_valueOrError1_).IsFailure():
                return (d_83_valueOrError1_).PropagateFailure()
            elif True:
                d_84_value_ = (d_83_valueOrError1_).Extract()
                return Wrappers.Result_Success((d_82_key_, d_84_value_))

    @staticmethod
    def WrapStringToError(e):
        return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(e)

    @staticmethod
    def ValidateKmsKeyId(keyId):
        d_85_valueOrError0_ = (AwsArnParsing.default__.ParseAwsKmsIdentifier(keyId)).MapFailure(default__.WrapStringToError)
        if (d_85_valueOrError0_).IsFailure():
            return (d_85_valueOrError0_).PropagateFailure()
        elif True:
            d_86___v0_ = (d_85_valueOrError0_).Extract()
            d_87_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(keyId), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key identifier is not ASCII")))
            if (d_87_valueOrError1_).IsFailure():
                return (d_87_valueOrError1_).PropagateFailure()
            elif True:
                d_88_valueOrError2_ = Wrappers.default__.Need(((0) < (len(keyId))) and ((len(keyId)) <= (AwsArnParsing.default__.MAX__AWS__KMS__IDENTIFIER__LENGTH)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key identifier is too long")))
                if (d_88_valueOrError2_).IsFailure():
                    return (d_88_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(())

    @staticmethod
    def GetValidGrantTokens(grantTokens):
        d_89_tokens_ = (grantTokens).UnwrapOr(_dafny.Seq([]))
        d_90_valueOrError0_ = Wrappers.default__.Need(((0) <= (len(d_89_tokens_))) and ((len(d_89_tokens_)) <= (10)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Grant token list can have no more than 10 tokens")))
        if (d_90_valueOrError0_).IsFailure():
            return (d_90_valueOrError0_).PropagateFailure()
        elif True:
            def lambda3_(forall_var_2_):
                d_92_token_: _dafny.Seq = forall_var_2_
                return not ((d_92_token_) in (d_89_tokens_)) or (((1) <= (len(d_92_token_))) and ((len(d_92_token_)) <= (8192)))

            d_91_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier((d_89_tokens_).UniqueElements, True, lambda3_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Grant token list contains a grant token with invalid length")))
            if (d_91_valueOrError1_).IsFailure():
                return (d_91_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_89_tokens_)

    @staticmethod
    def ParseKeyNamespaceAndName(keyNamespace, keyName):
        def lambda4_(d_94_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("Key namespace could not be UTF8-encoded")) + (d_94_e_))

        d_93_valueOrError0_ = (UTF8.default__.Encode(keyNamespace)).MapFailure(lambda4_)
        if (d_93_valueOrError0_).IsFailure():
            return (d_93_valueOrError0_).PropagateFailure()
        elif True:
            d_95_namespace_ = (d_93_valueOrError0_).Extract()
            d_96_valueOrError1_ = Wrappers.default__.Need((len(d_95_namespace_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key namespace too long")))
            if (d_96_valueOrError1_).IsFailure():
                return (d_96_valueOrError1_).PropagateFailure()
            elif True:
                def lambda5_(d_98_e_):
                    return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("Key name could not be UTF8-encoded")) + (d_98_e_))

                d_97_valueOrError2_ = (UTF8.default__.Encode(keyName)).MapFailure(lambda5_)
                if (d_97_valueOrError2_).IsFailure():
                    return (d_97_valueOrError2_).PropagateFailure()
                elif True:
                    d_99_name_ = (d_97_valueOrError2_).Extract()
                    d_100_valueOrError3_ = Wrappers.default__.Need((len(d_99_name_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key name too long")))
                    if (d_100_valueOrError3_).IsFailure():
                        return (d_100_valueOrError3_).PropagateFailure()
                    elif True:
                        return Wrappers.Result_Success((d_95_namespace_, d_99_name_))

    @staticmethod
    def ValidateDiscoveryFilter(filter):
        d_101_valueOrError0_ = Wrappers.default__.Need((len((filter).accountIds)) > (0), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Discovery filter must have at least one account ID")))
        if (d_101_valueOrError0_).IsFailure():
            return (d_101_valueOrError0_).PropagateFailure()
        elif True:
            def lambda6_(forall_var_3_):
                d_103_accountId_: _dafny.Seq = forall_var_3_
                return not ((d_103_accountId_) in ((filter).accountIds)) or ((len(d_103_accountId_)) > (0))

            d_102_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier(((filter).accountIds).UniqueElements, True, lambda6_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Discovery filter account IDs cannot be blank")))
            if (d_102_valueOrError1_).IsFailure():
                return (d_102_valueOrError1_).PropagateFailure()
            elif True:
                d_104_valueOrError2_ = Wrappers.default__.Need((len((filter).partition)) > (0), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Discovery filter partition cannot be blank")))
                if (d_104_valueOrError2_).IsFailure():
                    return (d_104_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(())


class OnDecryptMrkAwareEncryptedDataKeyFilter(Actions.DeterministicActionWithResult, Actions.DeterministicAction):
    def  __init__(self):
        self._awsKmsKey: AwsArnParsing.AwsKmsIdentifier = None
        self._providerId: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter"
    def ctor__(self, awsKmsKey, providerId):
        (self)._awsKmsKey = awsKmsKey
        (self)._providerId = providerId

    def Invoke(self, edk):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        if ((edk).keyProviderId) != ((self).providerId):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo)):
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
            return res
        d_105_keyId_: _dafny.Seq
        d_106_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_106_valueOrError0_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(default__.WrapStringToError)
        if (d_106_valueOrError0_).IsFailure():
            res = (d_106_valueOrError0_).PropagateFailure()
            return res
        d_105_keyId_ = (d_106_valueOrError0_).Extract()
        d_107_arn_: AwsArnParsing.AwsArn
        d_108_valueOrError1_: Wrappers.Result = None
        d_108_valueOrError1_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_105_keyId_)).MapFailure(default__.WrapStringToError)
        if (d_108_valueOrError1_).IsFailure():
            res = (d_108_valueOrError1_).PropagateFailure()
            return res
        d_107_arn_ = (d_108_valueOrError1_).Extract()
        res = Wrappers.Result_Success(AwsKmsMrkMatchForDecrypt.default__.AwsKmsMrkMatchForDecrypt((self).awsKmsKey, AwsArnParsing.AwsKmsIdentifier_AwsKmsArnIdentifier(d_107_arn_)))
        return res
        return res

    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def providerId(self):
        return self._providerId
