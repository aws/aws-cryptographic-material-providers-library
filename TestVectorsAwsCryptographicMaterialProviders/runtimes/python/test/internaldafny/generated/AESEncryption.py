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
import AwsKmsUtils
import Constants
import ExternRandom
import Random

assert "AESEncryption" == __name__
AESEncryption = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionOutputFromByteSeq(s, encAlg):
        d_208_cipherText_ = _dafny.Seq((s)[:(len(s)) - ((encAlg).tagLength):])
        d_209_authTag_ = _dafny.Seq((s)[(len(s)) - ((encAlg).tagLength)::])
        return software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput_AESEncryptOutput(d_208_cipherText_, d_209_authTag_)

    @staticmethod
    def AESEncrypt(input):
        res: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        d_210_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_210_valueOrError0_ = Wrappers.default__.Need(((len((input).iv)) == (((input).encAlg).ivLength)) and ((len((input).key)) == (((input).encAlg).keyLength)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Request does not match algorithm.")))
        if (d_210_valueOrError0_).IsFailure():
            res = (d_210_valueOrError0_).PropagateFailure()
            return res
        let_tmp_rhs0_ = input
        d_211_encAlg_ = let_tmp_rhs0_.encAlg
        d_212_iv_ = let_tmp_rhs0_.iv
        d_213_key_ = let_tmp_rhs0_.key
        d_214_msg_ = let_tmp_rhs0_.msg
        d_215_aad_ = let_tmp_rhs0_.aad
        d_216_value_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_217_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        out18_: Wrappers.Result
        out18_ = AESEncryption.AES_GCM.AESEncryptExtern(d_211_encAlg_, d_212_iv_, d_213_key_, d_214_msg_, d_215_aad_)
        d_217_valueOrError1_ = out18_
        if (d_217_valueOrError1_).IsFailure():
            res = (d_217_valueOrError1_).PropagateFailure()
            return res
        d_216_value_ = (d_217_valueOrError1_).Extract()
        d_218_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_218_valueOrError2_ = Wrappers.default__.Need((len((d_216_value_).cipherText)) == (len(d_214_msg_)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESEncrypt did not return cipherText of expected length")))
        if (d_218_valueOrError2_).IsFailure():
            res = (d_218_valueOrError2_).PropagateFailure()
            return res
        d_219_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_219_valueOrError3_ = Wrappers.default__.Need((len((d_216_value_).authTag)) == ((d_211_encAlg_).tagLength), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESEncryption did not return valid tag")))
        if (d_219_valueOrError3_).IsFailure():
            res = (d_219_valueOrError3_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_216_value_)
        return res
        return res

    @staticmethod
    def AESDecrypt(input):
        res: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_220_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_220_valueOrError0_ = Wrappers.default__.Need((((len((input).key)) == (((input).encAlg).keyLength)) and ((len((input).iv)) == (((input).encAlg).ivLength))) and ((len((input).authTag)) == (((input).encAlg).tagLength)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Request does not match algorithm.")))
        if (d_220_valueOrError0_).IsFailure():
            res = (d_220_valueOrError0_).PropagateFailure()
            return res
        let_tmp_rhs1_ = input
        d_221_encAlg_ = let_tmp_rhs1_.encAlg
        d_222_key_ = let_tmp_rhs1_.key
        d_223_cipherTxt_ = let_tmp_rhs1_.cipherTxt
        d_224_authTag_ = let_tmp_rhs1_.authTag
        d_225_iv_ = let_tmp_rhs1_.iv
        d_226_aad_ = let_tmp_rhs1_.aad
        d_227_value_: _dafny.Seq
        d_228_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out19_: Wrappers.Result
        out19_ = AESEncryption.AES_GCM.AESDecryptExtern(d_221_encAlg_, d_222_key_, d_223_cipherTxt_, d_224_authTag_, d_225_iv_, d_226_aad_)
        d_228_valueOrError1_ = out19_
        if (d_228_valueOrError1_).IsFailure():
            res = (d_228_valueOrError1_).PropagateFailure()
            return res
        d_227_value_ = (d_228_valueOrError1_).Extract()
        d_229_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_229_valueOrError2_ = Wrappers.default__.Need((len(d_223_cipherTxt_)) == (len(d_227_value_)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESDecrypt did not return plaintext of expected length")))
        if (d_229_valueOrError2_).IsFailure():
            res = (d_229_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_227_value_)
        return res
        return res

