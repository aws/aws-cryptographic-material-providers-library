import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
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
import StandardLibrary_mUInt
import String
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

# Module: AwsKmsUtils

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StringifyEncryptionContext(utf8EncCtx):
        if (len(utf8EncCtx)) == (0):
            return Wrappers.Result_Success(_dafny.Map({}))
        elif True:
            def iife13_():
                coll1_ = _dafny.Map()
                compr_1_: _dafny.Seq
                for compr_1_ in ((utf8EncCtx).keys).Elements:
                    d_168_utf8Key_: _dafny.Seq = compr_1_
                    if (d_168_utf8Key_) in ((utf8EncCtx).keys):
                        coll1_[d_168_utf8Key_] = default__.StringifyEncryptionContextPair(d_168_utf8Key_, (utf8EncCtx)[d_168_utf8Key_])
                return _dafny.Map(coll1_)
            d_167_stringifyResults_ = iife13_()

            def lambda13_(exists_var_0_):
                d_169_r_: Wrappers.Result = exists_var_0_
                return ((d_169_r_) in ((d_167_stringifyResults_).values)) and ((d_169_r_).is_Failure)

            if _dafny.quantifier(((d_167_stringifyResults_).values).Elements, False, lambda13_):
                return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context contains invalid UTF8")))
            elif True:
                def lambda14_(forall_var_4_):
                    def lambda15_(forall_var_5_):
                        d_172_k_k_: _dafny.Seq = forall_var_5_
                        return not (((d_171_k_) in (d_167_stringifyResults_)) and ((d_172_k_k_) in (d_167_stringifyResults_))) or (not ((d_171_k_) != (d_172_k_k_)) or (((((d_167_stringifyResults_)[d_171_k_]).value)[0]) != ((((d_167_stringifyResults_)[d_172_k_k_]).value)[0])))

                    d_171_k_: _dafny.Seq = forall_var_4_
                    return _dafny.quantifier((d_167_stringifyResults_).keys.Elements, True, lambda15_)

                d_170_stringKeysUnique_ = _dafny.quantifier((d_167_stringifyResults_).keys.Elements, True, lambda14_)
                if not(d_170_stringKeysUnique_):
                    return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context keys are not unique")))
                elif True:
                    def iife14_():
                        coll2_ = _dafny.Map()
                        compr_2_: Wrappers.Result
                        for compr_2_ in ((d_167_stringifyResults_).values).Elements:
                            d_173_r_: Wrappers.Result = compr_2_
                            if (d_173_r_) in ((d_167_stringifyResults_).values):
                                coll2_[((d_173_r_).value)[0]] = ((d_173_r_).value)[1]
                        return _dafny.Map(coll2_)
                    return Wrappers.Result_Success(iife14_()
)

    @staticmethod
    def StringifyEncryptionContextPair(utf8Key, utf8Value):
        d_174_valueOrError0_ = (UTF8.default__.Decode(utf8Key)).MapFailure(default__.WrapStringToError)
        if (d_174_valueOrError0_).IsFailure():
            return (d_174_valueOrError0_).PropagateFailure()
        elif True:
            d_175_key_ = (d_174_valueOrError0_).Extract()
            d_176_valueOrError1_ = (UTF8.default__.Decode(utf8Value)).MapFailure(default__.WrapStringToError)
            if (d_176_valueOrError1_).IsFailure():
                return (d_176_valueOrError1_).PropagateFailure()
            elif True:
                d_177_value_ = (d_176_valueOrError1_).Extract()
                return Wrappers.Result_Success((d_175_key_, d_177_value_))

    @staticmethod
    def WrapStringToError(e):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(e)

    @staticmethod
    def ValidateKmsKeyId(keyId):
        d_178_valueOrError0_ = (AwsArnParsing.default__.ParseAwsKmsIdentifier(keyId)).MapFailure(default__.WrapStringToError)
        if (d_178_valueOrError0_).IsFailure():
            return (d_178_valueOrError0_).PropagateFailure()
        elif True:
            d_179___v0_ = (d_178_valueOrError0_).Extract()
            d_180_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(keyId), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key identifier is not ASCII")))
            if (d_180_valueOrError1_).IsFailure():
                return (d_180_valueOrError1_).PropagateFailure()
            elif True:
                d_181_valueOrError2_ = Wrappers.default__.Need(((0) < (len(keyId))) and ((len(keyId)) <= (AwsArnParsing.default__.MAX__AWS__KMS__IDENTIFIER__LENGTH)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key identifier is too long")))
                if (d_181_valueOrError2_).IsFailure():
                    return (d_181_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(())

    @staticmethod
    def GetValidGrantTokens(grantTokens):
        d_182_tokens_ = (grantTokens).UnwrapOr(_dafny.Seq([]))
        d_183_valueOrError0_ = Wrappers.default__.Need(((0) <= (len(d_182_tokens_))) and ((len(d_182_tokens_)) <= (10)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Grant token list can have no more than 10 tokens")))
        if (d_183_valueOrError0_).IsFailure():
            return (d_183_valueOrError0_).PropagateFailure()
        elif True:
            def lambda16_(forall_var_6_):
                d_185_token_: _dafny.Seq = forall_var_6_
                return not ((d_185_token_) in (d_182_tokens_)) or (((1) <= (len(d_185_token_))) and ((len(d_185_token_)) <= (8192)))

            d_184_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier((d_182_tokens_).UniqueElements, True, lambda16_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Grant token list contains a grant token with invalid length")))
            if (d_184_valueOrError1_).IsFailure():
                return (d_184_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_182_tokens_)

    @staticmethod
    def ParseKeyNamespaceAndName(keyNamespace, keyName):
        def lambda17_(d_187_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("Key namespace could not be UTF8-encoded")) + (d_187_e_))

        d_186_valueOrError0_ = (UTF8.default__.Encode(keyNamespace)).MapFailure(lambda17_)
        if (d_186_valueOrError0_).IsFailure():
            return (d_186_valueOrError0_).PropagateFailure()
        elif True:
            d_188_namespace_ = (d_186_valueOrError0_).Extract()
            d_189_valueOrError1_ = Wrappers.default__.Need((len(d_188_namespace_)) < (StandardLibrary_mUInt.default__.UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key namespace too long")))
            if (d_189_valueOrError1_).IsFailure():
                return (d_189_valueOrError1_).PropagateFailure()
            elif True:
                def lambda18_(d_191_e_):
                    return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("Key name could not be UTF8-encoded")) + (d_191_e_))

                d_190_valueOrError2_ = (UTF8.default__.Encode(keyName)).MapFailure(lambda18_)
                if (d_190_valueOrError2_).IsFailure():
                    return (d_190_valueOrError2_).PropagateFailure()
                elif True:
                    d_192_name_ = (d_190_valueOrError2_).Extract()
                    d_193_valueOrError3_ = Wrappers.default__.Need((len(d_192_name_)) < (StandardLibrary_mUInt.default__.UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Key name too long")))
                    if (d_193_valueOrError3_).IsFailure():
                        return (d_193_valueOrError3_).PropagateFailure()
                    elif True:
                        return Wrappers.Result_Success((d_188_namespace_, d_192_name_))

    @staticmethod
    def ValidateDiscoveryFilter(filter):
        d_194_valueOrError0_ = Wrappers.default__.Need((len((filter).accountIds)) > (0), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Discovery filter must have at least one account ID")))
        if (d_194_valueOrError0_).IsFailure():
            return (d_194_valueOrError0_).PropagateFailure()
        elif True:
            def lambda19_(forall_var_7_):
                d_196_accountId_: _dafny.Seq = forall_var_7_
                return not ((d_196_accountId_) in ((filter).accountIds)) or ((len(d_196_accountId_)) > (0))

            d_195_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier(((filter).accountIds).UniqueElements, True, lambda19_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Discovery filter account IDs cannot be blank")))
            if (d_195_valueOrError1_).IsFailure():
                return (d_195_valueOrError1_).PropagateFailure()
            elif True:
                d_197_valueOrError2_ = Wrappers.default__.Need((len((filter).partition)) > (0), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Discovery filter partition cannot be blank")))
                if (d_197_valueOrError2_).IsFailure():
                    return (d_197_valueOrError2_).PropagateFailure()
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
        d_198_keyId_: _dafny.Seq
        d_199_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_199_valueOrError0_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(default__.WrapStringToError)
        if (d_199_valueOrError0_).IsFailure():
            res = (d_199_valueOrError0_).PropagateFailure()
            return res
        d_198_keyId_ = (d_199_valueOrError0_).Extract()
        d_200_arn_: AwsArnParsing.AwsArn
        d_201_valueOrError1_: Wrappers.Result = None
        d_201_valueOrError1_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_198_keyId_)).MapFailure(default__.WrapStringToError)
        if (d_201_valueOrError1_).IsFailure():
            res = (d_201_valueOrError1_).PropagateFailure()
            return res
        d_200_arn_ = (d_201_valueOrError1_).Extract()
        res = Wrappers.Result_Success(AwsKmsMrkMatchForDecrypt.default__.AwsKmsMrkMatchForDecrypt((self).awsKmsKey, AwsArnParsing.AwsKmsIdentifier_AwsKmsArnIdentifier(d_200_arn_)))
        return res
        return res

    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def providerId(self):
        return self._providerId
