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

# Module: AwsKmsUtils

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StringifyEncryptionContext(utf8EncCtx):
        if (len(utf8EncCtx)) == (0):
            return Wrappers.Result_Success(_dafny.Map({}))
        elif True:
            def iife0_():
                coll0_ = _dafny.Map()
                compr_0_: _dafny.Seq
                for compr_0_ in ((utf8EncCtx).keys).Elements:
                    d_65_utf8Key_: _dafny.Seq = compr_0_
                    if (d_65_utf8Key_) in ((utf8EncCtx).keys):
                        coll0_[d_65_utf8Key_] = default__.StringifyEncryptionContextPair(d_65_utf8Key_, (utf8EncCtx)[d_65_utf8Key_])
                return _dafny.Map(coll0_)
            d_64_stringifyResults_ = iife0_()

            def lambda0_(exists_var_0_):
                d_66_r_: Wrappers.Result = exists_var_0_
                return ((d_66_r_) in ((d_64_stringifyResults_).values)) and ((d_66_r_).is_Failure)

            if _dafny.quantifier(((d_64_stringifyResults_).values).Elements, False, lambda0_):
                return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context contains invalid UTF8")))
            elif True:
                def lambda1_(forall_var_0_):
                    def lambda2_(forall_var_1_):
                        d_69_k_k_: _dafny.Seq = forall_var_1_
                        return not (((d_68_k_) in (d_64_stringifyResults_)) and ((d_69_k_k_) in (d_64_stringifyResults_))) or (not ((d_68_k_) != (d_69_k_k_)) or (((((d_64_stringifyResults_)[d_68_k_]).value)[0]) != ((((d_64_stringifyResults_)[d_69_k_k_]).value)[0])))

                    d_68_k_: _dafny.Seq = forall_var_0_
                    return _dafny.quantifier((d_64_stringifyResults_).keys.Elements, True, lambda2_)

                d_67_stringKeysUnique_ = _dafny.quantifier((d_64_stringifyResults_).keys.Elements, True, lambda1_)
                if not(d_67_stringKeysUnique_):
                    return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context keys are not unique")))
                elif True:
                    def iife1_():
                        coll1_ = _dafny.Map()
                        compr_1_: Wrappers.Result
                        for compr_1_ in ((d_64_stringifyResults_).values).Elements:
                            d_70_r_: Wrappers.Result = compr_1_
                            if (d_70_r_) in ((d_64_stringifyResults_).values):
                                coll1_[((d_70_r_).value)[0]] = ((d_70_r_).value)[1]
                        return _dafny.Map(coll1_)
                    return Wrappers.Result_Success(iife1_()
)

    @staticmethod
    def StringifyEncryptionContextPair(utf8Key, utf8Value):
        d_71_valueOrError0_ = (UTF8.default__.Decode(utf8Key)).MapFailure(default__.WrapStringToError)
        if (d_71_valueOrError0_).IsFailure():
            return (d_71_valueOrError0_).PropagateFailure()
        elif True:
            d_72_key_ = (d_71_valueOrError0_).Extract()
            d_73_valueOrError1_ = (UTF8.default__.Decode(utf8Value)).MapFailure(default__.WrapStringToError)
            if (d_73_valueOrError1_).IsFailure():
                return (d_73_valueOrError1_).PropagateFailure()
            elif True:
                d_74_value_ = (d_73_valueOrError1_).Extract()
                return Wrappers.Result_Success((d_72_key_, d_74_value_))

    @staticmethod
    def WrapStringToError(e):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(e)

    @staticmethod
    def ValidateKmsKeyId(keyId):
        d_75_valueOrError0_ = (AwsArnParsing.default__.ParseAwsKmsIdentifier(keyId)).MapFailure(default__.WrapStringToError)
        if (d_75_valueOrError0_).IsFailure():
            return (d_75_valueOrError0_).PropagateFailure()
        elif True:
            d_76___v0_ = (d_75_valueOrError0_).Extract()
            d_77_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(keyId), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key identifier is not ASCII")))
            if (d_77_valueOrError1_).IsFailure():
                return (d_77_valueOrError1_).PropagateFailure()
            elif True:
                d_78_valueOrError2_ = Wrappers.default__.Need(((0) < (len(keyId))) and ((len(keyId)) <= (AwsArnParsing.default__.MAX__AWS__KMS__IDENTIFIER__LENGTH)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key identifier is too long")))
                if (d_78_valueOrError2_).IsFailure():
                    return (d_78_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(())

    @staticmethod
    def GetValidGrantTokens(grantTokens):
        d_79_tokens_ = (grantTokens).UnwrapOr(_dafny.Seq([]))
        d_80_valueOrError0_ = Wrappers.default__.Need(((0) <= (len(d_79_tokens_))) and ((len(d_79_tokens_)) <= (10)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Grant token list can have no more than 10 tokens")))
        if (d_80_valueOrError0_).IsFailure():
            return (d_80_valueOrError0_).PropagateFailure()
        elif True:
            def lambda3_(forall_var_2_):
                d_82_token_: _dafny.Seq = forall_var_2_
                return not ((d_82_token_) in (d_79_tokens_)) or (((1) <= (len(d_82_token_))) and ((len(d_82_token_)) <= (8192)))

            d_81_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier((d_79_tokens_).UniqueElements, True, lambda3_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Grant token list contains a grant token with invalid length")))
            if (d_81_valueOrError1_).IsFailure():
                return (d_81_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_79_tokens_)

    @staticmethod
    def ParseKeyNamespaceAndName(keyNamespace, keyName):
        def lambda4_(d_84_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("Key namespace could not be UTF8-encoded")) + (d_84_e_))

        d_83_valueOrError0_ = (UTF8.default__.Encode(keyNamespace)).MapFailure(lambda4_)
        if (d_83_valueOrError0_).IsFailure():
            return (d_83_valueOrError0_).PropagateFailure()
        elif True:
            d_85_namespace_ = (d_83_valueOrError0_).Extract()
            d_86_valueOrError1_ = Wrappers.default__.Need((len(d_85_namespace_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key namespace too long")))
            if (d_86_valueOrError1_).IsFailure():
                return (d_86_valueOrError1_).PropagateFailure()
            elif True:
                def lambda5_(d_88_e_):
                    return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("Key name could not be UTF8-encoded")) + (d_88_e_))

                d_87_valueOrError2_ = (UTF8.default__.Encode(keyName)).MapFailure(lambda5_)
                if (d_87_valueOrError2_).IsFailure():
                    return (d_87_valueOrError2_).PropagateFailure()
                elif True:
                    d_89_name_ = (d_87_valueOrError2_).Extract()
                    d_90_valueOrError3_ = Wrappers.default__.Need((len(d_89_name_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key name too long")))
                    if (d_90_valueOrError3_).IsFailure():
                        return (d_90_valueOrError3_).PropagateFailure()
                    elif True:
                        return Wrappers.Result_Success((d_85_namespace_, d_89_name_))

    @staticmethod
    def ValidateDiscoveryFilter(filter):
        d_91_valueOrError0_ = Wrappers.default__.Need((len((filter).accountIds)) > (0), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Discovery filter must have at least one account ID")))
        if (d_91_valueOrError0_).IsFailure():
            return (d_91_valueOrError0_).PropagateFailure()
        elif True:
            def lambda6_(forall_var_3_):
                d_93_accountId_: _dafny.Seq = forall_var_3_
                return not ((d_93_accountId_) in ((filter).accountIds)) or ((len(d_93_accountId_)) > (0))

            d_92_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier(((filter).accountIds).UniqueElements, True, lambda6_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Discovery filter account IDs cannot be blank")))
            if (d_92_valueOrError1_).IsFailure():
                return (d_92_valueOrError1_).PropagateFailure()
            elif True:
                d_94_valueOrError2_ = Wrappers.default__.Need((len((filter).partition)) > (0), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Discovery filter partition cannot be blank")))
                if (d_94_valueOrError2_).IsFailure():
                    return (d_94_valueOrError2_).PropagateFailure()
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
            res = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
            return res
        d_95_keyId_: _dafny.Seq
        d_96_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_96_valueOrError0_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(default__.WrapStringToError)
        if (d_96_valueOrError0_).IsFailure():
            res = (d_96_valueOrError0_).PropagateFailure()
            return res
        d_95_keyId_ = (d_96_valueOrError0_).Extract()
        d_97_arn_: AwsArnParsing.AwsArn
        d_98_valueOrError1_: Wrappers.Result = None
        d_98_valueOrError1_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_95_keyId_)).MapFailure(default__.WrapStringToError)
        if (d_98_valueOrError1_).IsFailure():
            res = (d_98_valueOrError1_).PropagateFailure()
            return res
        d_97_arn_ = (d_98_valueOrError1_).Extract()
        res = Wrappers.Result_Success(AwsKmsMrkMatchForDecrypt.default__.AwsKmsMrkMatchForDecrypt((self).awsKmsKey, AwsArnParsing.AwsKmsIdentifier_AwsKmsArnIdentifier(d_97_arn_)))
        return res
        return res

    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def providerId(self):
        return self._providerId
