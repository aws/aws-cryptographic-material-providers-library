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
import StandardLibraryInterop
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
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_primitives_internaldafny_types
import ExternRandom
import Random

# Module: AESEncryption

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionOutputFromByteSeq(s, encAlg):
        d_10_cipherText_ = _dafny.Seq((s)[:(len(s)) - ((encAlg).tagLength):])
        d_11_authTag_ = _dafny.Seq((s)[(len(s)) - ((encAlg).tagLength)::])
        return software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput_AESEncryptOutput(d_10_cipherText_, d_11_authTag_)

    @staticmethod
    def AESEncrypt(input):
        res: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        d_12_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_12_valueOrError0_ = Wrappers.default__.Need(((len((input).iv)) == (((input).encAlg).ivLength)) and ((len((input).key)) == (((input).encAlg).keyLength)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Request does not match algorithm.")))
        if (d_12_valueOrError0_).IsFailure():
            res = (d_12_valueOrError0_).PropagateFailure()
            return res
        let_tmp_rhs0_ = input
        d_13_encAlg_ = let_tmp_rhs0_.encAlg
        d_14_iv_ = let_tmp_rhs0_.iv
        d_15_key_ = let_tmp_rhs0_.key
        d_16_msg_ = let_tmp_rhs0_.msg
        d_17_aad_ = let_tmp_rhs0_.aad
        d_18_value_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_19_valueOrError1_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        out1_: Wrappers.Result
        out1_ = AESEncryption.AES_GCM.AESEncryptExtern(d_13_encAlg_, d_14_iv_, d_15_key_, d_16_msg_, d_17_aad_)
        d_19_valueOrError1_ = out1_
        if (d_19_valueOrError1_).IsFailure():
            res = (d_19_valueOrError1_).PropagateFailure()
            return res
        d_18_value_ = (d_19_valueOrError1_).Extract()
        d_20_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_20_valueOrError2_ = Wrappers.default__.Need((len((d_18_value_).cipherText)) == (len(d_16_msg_)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESEncrypt did not return cipherText of expected length")))
        if (d_20_valueOrError2_).IsFailure():
            res = (d_20_valueOrError2_).PropagateFailure()
            return res
        d_21_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_21_valueOrError3_ = Wrappers.default__.Need((len((d_18_value_).authTag)) == ((d_13_encAlg_).tagLength), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESEncryption did not return valid tag")))
        if (d_21_valueOrError3_).IsFailure():
            res = (d_21_valueOrError3_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_18_value_)
        return res
        return res

    @staticmethod
    def AESDecrypt(input):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_22_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_22_valueOrError0_ = Wrappers.default__.Need((((len((input).key)) == (((input).encAlg).keyLength)) and ((len((input).iv)) == (((input).encAlg).ivLength))) and ((len((input).authTag)) == (((input).encAlg).tagLength)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Request does not match algorithm.")))
        if (d_22_valueOrError0_).IsFailure():
            res = (d_22_valueOrError0_).PropagateFailure()
            return res
        let_tmp_rhs1_ = input
        d_23_encAlg_ = let_tmp_rhs1_.encAlg
        d_24_key_ = let_tmp_rhs1_.key
        d_25_cipherTxt_ = let_tmp_rhs1_.cipherTxt
        d_26_authTag_ = let_tmp_rhs1_.authTag
        d_27_iv_ = let_tmp_rhs1_.iv
        d_28_aad_ = let_tmp_rhs1_.aad
        d_29_value_: _dafny.Seq
        d_30_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out2_: Wrappers.Result
        out2_ = AESEncryption.AES_GCM.AESDecryptExtern(d_23_encAlg_, d_24_key_, d_25_cipherTxt_, d_26_authTag_, d_27_iv_, d_28_aad_)
        d_30_valueOrError1_ = out2_
        if (d_30_valueOrError1_).IsFailure():
            res = (d_30_valueOrError1_).PropagateFailure()
            return res
        d_29_value_ = (d_30_valueOrError1_).Extract()
        d_31_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_31_valueOrError2_ = Wrappers.default__.Need((len(d_25_cipherTxt_)) == (len(d_29_value_)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESDecrypt did not return plaintext of expected length")))
        if (d_31_valueOrError2_).IsFailure():
            res = (d_31_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_29_value_)
        return res
        return res

    @staticmethod
    def CreateAESEncryptExternSuccess(output):
        return Wrappers.Result_Success(output)

    @staticmethod
    def CreateAESEncryptExternFailure(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateAESDecryptExternSuccess(bytes):
        return Wrappers.Result_Success(bytes)

    @staticmethod
    def CreateAESDecryptExternFailure(error):
        return Wrappers.Result_Failure(error)

