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

# Module: AwsKmsUtils

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def OkForDecrypt(id, arn):
        if not((id).is_AwsKmsArnIdentifier):
            return Wrappers.Outcome_Fail(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("KeyID cannot be used for Decrypt : ")) + (arn)))
        elif ((((id).a).resource).resourceType) != (_dafny.Seq("key")):
            return Wrappers.Outcome_Fail(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("Alias cannot be used for Decrypt : ")) + (arn)))
        elif True:
            return Wrappers.Outcome_Pass()

    @staticmethod
    def StringifyEncryptionContext(utf8EncCtx):
        def lambda0_(exists_var_0_):
            d_2_r_: Wrappers.Result = exists_var_0_
            return ((d_2_r_) in ((d_0_stringifyResults_).values)) and ((d_2_r_).is_Failure)

        if (len(utf8EncCtx)) == (0):
            return Wrappers.Result_Success(_dafny.Map({}))
        elif True:
            def iife0_():
                coll0_ = _dafny.Map()
                compr_0_: _dafny.Seq
                for compr_0_ in ((utf8EncCtx).keys).Elements:
                    d_1_utf8Key_: _dafny.Seq = compr_0_
                    if UTF8.ValidUTF8Bytes._Is(d_1_utf8Key_):
                        if (d_1_utf8Key_) in ((utf8EncCtx).keys):
                            coll0_[d_1_utf8Key_] = default__.StringifyEncryptionContextPair(d_1_utf8Key_, (utf8EncCtx)[d_1_utf8Key_])
                return _dafny.Map(coll0_)
            d_0_stringifyResults_ = iife0_()

            if _dafny.quantifier(((d_0_stringifyResults_).values).Elements, False, lambda0_):
                return Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context contains invalid UTF8")))
            elif True:
                def lambda1_(forall_var_0_):
                    def lambda2_(forall_var_1_):
                        d_5_k_k_: _dafny.Seq = forall_var_1_
                        return not (((d_4_k_) in (d_0_stringifyResults_)) and ((d_5_k_k_) in (d_0_stringifyResults_))) or (not ((d_4_k_) != (d_5_k_k_)) or (((((d_0_stringifyResults_)[d_4_k_]).value)[0]) != ((((d_0_stringifyResults_)[d_5_k_k_]).value)[0])))

                    d_4_k_: _dafny.Seq = forall_var_0_
                    return _dafny.quantifier((d_0_stringifyResults_).keys.Elements, True, lambda2_)

                d_3_stringKeysUnique_ = _dafny.quantifier((d_0_stringifyResults_).keys.Elements, True, lambda1_)
                if not(d_3_stringKeysUnique_):
                    return Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context keys are not unique")))
                elif True:
                    def iife1_():
                        coll1_ = _dafny.Map()
                        compr_1_: Wrappers.Result
                        for compr_1_ in ((d_0_stringifyResults_).values).Elements:
                            d_6_r_: Wrappers.Result = compr_1_
                            if (d_6_r_) in ((d_0_stringifyResults_).values):
                                coll1_[((d_6_r_).value)[0]] = ((d_6_r_).value)[1]
                        return _dafny.Map(coll1_)
                    return Wrappers.Result_Success(iife1_()
)

    @staticmethod
    def StringifyEncryptionContextPair(utf8Key, utf8Value):
        d_0_valueOrError0_ = (UTF8.default__.Decode(utf8Key)).MapFailure(default__.WrapStringToError)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_key_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = (UTF8.default__.Decode(utf8Value)).MapFailure(default__.WrapStringToError)
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_value_ = (d_2_valueOrError1_).Extract()
                return Wrappers.Result_Success((d_1_key_, d_3_value_))

    @staticmethod
    def WrapStringToError(e):
        return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(e)

    @staticmethod
    def ValidateKmsKeyId(keyId):
        d_0_valueOrError0_ = (AwsArnParsing.default__.ParseAwsKmsIdentifier(keyId)).MapFailure(default__.WrapStringToError)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1___v0_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(keyId), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key identifier is not ASCII")))
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_valueOrError2_ = Wrappers.default__.Need(((0) < (len(keyId))) and ((len(keyId)) <= (AwsArnParsing.default__.MAX__AWS__KMS__IDENTIFIER__LENGTH)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key identifier is too long")))
                if (d_3_valueOrError2_).IsFailure():
                    return (d_3_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(())

    @staticmethod
    def GetValidGrantTokens(grantTokens):
        d_0_tokens_ = (grantTokens).UnwrapOr(_dafny.Seq([]))
        d_1_valueOrError0_ = Wrappers.default__.Need(((0) <= (len(d_0_tokens_))) and ((len(d_0_tokens_)) <= (10)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Grant token list can have no more than 10 tokens")))
        if (d_1_valueOrError0_).IsFailure():
            return (d_1_valueOrError0_).PropagateFailure()
        elif True:
            def lambda0_(forall_var_0_):
                d_3_token_: _dafny.Seq = forall_var_0_
                return not ((d_3_token_) in (d_0_tokens_)) or (((1) <= (len(d_3_token_))) and ((len(d_3_token_)) <= (8192)))

            d_2_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier((d_0_tokens_).UniqueElements, True, lambda0_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Grant token list contains a grant token with invalid length")))
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_0_tokens_)

    @staticmethod
    def GetEcdhPublicKey(client, awsKmsKey):
        res: Wrappers.Result = None
        d_0_getPublicKeyRequest_: ComAmazonawsKmsTypes.GetPublicKeyRequest
        d_0_getPublicKeyRequest_ = ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest(awsKmsKey, Wrappers.Option_None())
        d_1_maybePublicKeyResponse_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (client).GetPublicKey(d_0_getPublicKeyRequest_)
        d_1_maybePublicKeyResponse_ = out0_
        d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GetPublicKeyResponse.default())()
        def lambda0_(d_3_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_ComAmazonawsKms(d_3_e_)

        d_2_valueOrError0_ = (d_1_maybePublicKeyResponse_).MapFailure(lambda0_)
        if (d_2_valueOrError0_).IsFailure():
            res = (d_2_valueOrError0_).PropagateFailure()
            return res
        d_4_getPublicKeyResponse_: ComAmazonawsKmsTypes.GetPublicKeyResponse
        d_4_getPublicKeyResponse_ = (d_2_valueOrError0_).Extract()
        d_5_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_5_valueOrError1_ = Wrappers.default__.Need(((((((d_4_getPublicKeyResponse_).KeyId).is_Some) and ((((d_4_getPublicKeyResponse_).KeyId).value) == (awsKmsKey))) and (((d_4_getPublicKeyResponse_).KeyUsage).is_Some)) and ((((d_4_getPublicKeyResponse_).KeyUsage).value) == (ComAmazonawsKmsTypes.KeyUsageType_KEY__AGREEMENT()))) and (((d_4_getPublicKeyResponse_).PublicKey).is_Some), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS GetPublicKey")))
        if (d_5_valueOrError1_).IsFailure():
            res = (d_5_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(((d_4_getPublicKeyResponse_).PublicKey).value)
        return res
        return res

    @staticmethod
    def ParseKeyNamespaceAndName(keyNamespace, keyName):
        def lambda0_(d_1_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("Key namespace could not be UTF8-encoded")) + (d_1_e_))

        d_0_valueOrError0_ = (UTF8.default__.Encode(keyNamespace)).MapFailure(lambda0_)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_2_namespace_ = (d_0_valueOrError0_).Extract()
            d_3_valueOrError1_ = Wrappers.default__.Need((len(d_2_namespace_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key namespace too long")))
            if (d_3_valueOrError1_).IsFailure():
                return (d_3_valueOrError1_).PropagateFailure()
            elif True:
                def lambda1_(d_5_e_):
                    return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("Key name could not be UTF8-encoded")) + (d_5_e_))

                d_4_valueOrError2_ = (UTF8.default__.Encode(keyName)).MapFailure(lambda1_)
                if (d_4_valueOrError2_).IsFailure():
                    return (d_4_valueOrError2_).PropagateFailure()
                elif True:
                    d_6_name_ = (d_4_valueOrError2_).Extract()
                    d_7_valueOrError3_ = Wrappers.default__.Need((len(d_6_name_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key name too long")))
                    if (d_7_valueOrError3_).IsFailure():
                        return (d_7_valueOrError3_).PropagateFailure()
                    elif True:
                        return Wrappers.Result_Success((d_2_namespace_, d_6_name_))

    @staticmethod
    def ValidateDiscoveryFilter(filter):
        d_0_valueOrError0_ = Wrappers.default__.Need((len((filter).accountIds)) > (0), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Discovery filter must have at least one account ID")))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            def lambda0_(forall_var_0_):
                d_2_accountId_: _dafny.Seq = forall_var_0_
                return not ((d_2_accountId_) in ((filter).accountIds)) or ((len(d_2_accountId_)) > (0))

            d_1_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier(((filter).accountIds).UniqueElements, True, lambda0_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Discovery filter account IDs cannot be blank")))
            if (d_1_valueOrError1_).IsFailure():
                return (d_1_valueOrError1_).PropagateFailure()
            elif True:
                d_3_valueOrError2_ = Wrappers.default__.Need((len((filter).partition)) > (0), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Discovery filter partition cannot be blank")))
                if (d_3_valueOrError2_).IsFailure():
                    return (d_3_valueOrError2_).PropagateFailure()
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
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_valueOrError0_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(default__.WrapStringToError)
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_keyId_: _dafny.Seq
        d_1_keyId_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = None
        d_2_valueOrError1_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_1_keyId_)).MapFailure(default__.WrapStringToError)
        if (d_2_valueOrError1_).IsFailure():
            res = (d_2_valueOrError1_).PropagateFailure()
            return res
        d_3_arn_: AwsArnParsing.AwsArn
        d_3_arn_ = (d_2_valueOrError1_).Extract()
        res = Wrappers.Result_Success(AwsKmsMrkMatchForDecrypt.default__.AwsKmsMrkMatchForDecrypt((self).awsKmsKey, AwsArnParsing.AwsKmsIdentifier_AwsKmsArnIdentifier(d_3_arn_)))
        return res
        return res

    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def providerId(self):
        return self._providerId
