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
import software.amazon.cryptography.primitives.internaldafny.types
import ExternRandom
import Random

# Module: AESEncryption

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionOutputFromByteSeq(s, encAlg):
        d_3_cipherText_ = _dafny.Seq((s)[:(len(s)) - ((encAlg).tagLength):])
        d_4_authTag_ = _dafny.Seq((s)[(len(s)) - ((encAlg).tagLength)::])
        return software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput_AESEncryptOutput(d_3_cipherText_, d_4_authTag_)

    @staticmethod
    def AESEncrypt(input):
        res: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput.default())()
        d_5_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_5_valueOrError0_ = Wrappers.default__.Need(((len((input).iv)) == (((input).encAlg).ivLength)) and ((len((input).key)) == (((input).encAlg).keyLength)), software.amazon.cryptography.primitives.internaldafny.types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Request does not match algorithm.")))
        if (d_5_valueOrError0_).IsFailure():
            res = (d_5_valueOrError0_).PropagateFailure()
            return res
        let_tmp_rhs0_ = input
        d_6_encAlg_ = let_tmp_rhs0_.encAlg
        d_7_iv_ = let_tmp_rhs0_.iv
        d_8_key_ = let_tmp_rhs0_.key
        d_9_msg_ = let_tmp_rhs0_.msg
        d_10_aad_ = let_tmp_rhs0_.aad
        d_11_value_: software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput
        d_12_valueOrError1_: Wrappers.Result = Wrappers.Result.default(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput.default())()
        out1_: Wrappers.Result
        out1_ = AESEncryption.AES_GCM.AESEncryptExtern(d_6_encAlg_, d_7_iv_, d_8_key_, d_9_msg_, d_10_aad_)
        d_12_valueOrError1_ = out1_
        if (d_12_valueOrError1_).IsFailure():
            res = (d_12_valueOrError1_).PropagateFailure()
            return res
        d_11_value_ = (d_12_valueOrError1_).Extract()
        d_13_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_13_valueOrError2_ = Wrappers.default__.Need((len((d_11_value_).cipherText)) == (len(d_9_msg_)), software.amazon.cryptography.primitives.internaldafny.types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESEncrypt did not return cipherText of expected length")))
        if (d_13_valueOrError2_).IsFailure():
            res = (d_13_valueOrError2_).PropagateFailure()
            return res
        d_14_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_14_valueOrError3_ = Wrappers.default__.Need((len((d_11_value_).authTag)) == ((d_6_encAlg_).tagLength), software.amazon.cryptography.primitives.internaldafny.types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESEncryption did not return valid tag")))
        if (d_14_valueOrError3_).IsFailure():
            res = (d_14_valueOrError3_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_11_value_)
        return res
        return res

    @staticmethod
    def AESDecrypt(input):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_15_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_15_valueOrError0_ = Wrappers.default__.Need((((len((input).key)) == (((input).encAlg).keyLength)) and ((len((input).iv)) == (((input).encAlg).ivLength))) and ((len((input).authTag)) == (((input).encAlg).tagLength)), software.amazon.cryptography.primitives.internaldafny.types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Request does not match algorithm.")))
        if (d_15_valueOrError0_).IsFailure():
            res = (d_15_valueOrError0_).PropagateFailure()
            return res
        let_tmp_rhs1_ = input
        d_16_encAlg_ = let_tmp_rhs1_.encAlg
        d_17_key_ = let_tmp_rhs1_.key
        d_18_cipherTxt_ = let_tmp_rhs1_.cipherTxt
        d_19_authTag_ = let_tmp_rhs1_.authTag
        d_20_iv_ = let_tmp_rhs1_.iv
        d_21_aad_ = let_tmp_rhs1_.aad
        d_22_value_: _dafny.Seq
        d_23_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out2_: Wrappers.Result
        out2_ = AESEncryption.AES_GCM.AESDecryptExtern(d_16_encAlg_, d_17_key_, d_18_cipherTxt_, d_19_authTag_, d_20_iv_, d_21_aad_)
        d_23_valueOrError1_ = out2_
        if (d_23_valueOrError1_).IsFailure():
            res = (d_23_valueOrError1_).PropagateFailure()
            return res
        d_22_value_ = (d_23_valueOrError1_).Extract()
        d_24_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_24_valueOrError2_ = Wrappers.default__.Need((len(d_18_cipherTxt_)) == (len(d_22_value_)), software.amazon.cryptography.primitives.internaldafny.types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESDecrypt did not return plaintext of expected length")))
        if (d_24_valueOrError2_).IsFailure():
            res = (d_24_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_22_value_)
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

