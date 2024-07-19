import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_primitives.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
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
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random

# Module: AESEncryption

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionOutputFromByteSeq(s, encAlg):
        d_10_cipherText_ = _dafny.Seq((s)[:(len(s)) - ((encAlg).tagLength):])
        d_11_authTag_ = _dafny.Seq((s)[(len(s)) - ((encAlg).tagLength)::])
        return AwsCryptographyPrimitivesTypes.AESEncryptOutput_AESEncryptOutput(d_10_cipherText_, d_11_authTag_)

    @staticmethod
    def AESEncrypt(input):
        res: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        d_12_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_12_valueOrError0_ = Wrappers.default__.Need(((len((input).iv)) == (((input).encAlg).ivLength)) and ((len((input).key)) == (((input).encAlg).keyLength)), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Request does not match algorithm.")))
        if (d_12_valueOrError0_).IsFailure():
            res = (d_12_valueOrError0_).PropagateFailure()
            return res
        let_tmp_rhs0_ = input
        d_13_encAlg_ = let_tmp_rhs0_.encAlg
        d_14_iv_ = let_tmp_rhs0_.iv
        d_15_key_ = let_tmp_rhs0_.key
        d_16_msg_ = let_tmp_rhs0_.msg
        d_17_aad_ = let_tmp_rhs0_.aad
        d_18_valueOrError1_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        out1_: Wrappers.Result
        out1_ = AESEncryption.AES_GCM.AESEncryptExtern(d_13_encAlg_, d_14_iv_, d_15_key_, d_16_msg_, d_17_aad_)
        d_18_valueOrError1_ = out1_
        if (d_18_valueOrError1_).IsFailure():
            res = (d_18_valueOrError1_).PropagateFailure()
            return res
        d_19_value_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_19_value_ = (d_18_valueOrError1_).Extract()
        d_20_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_20_valueOrError2_ = Wrappers.default__.Need((len((d_19_value_).cipherText)) == (len(d_16_msg_)), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESEncrypt did not return cipherText of expected length")))
        if (d_20_valueOrError2_).IsFailure():
            res = (d_20_valueOrError2_).PropagateFailure()
            return res
        d_21_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_21_valueOrError3_ = Wrappers.default__.Need((len((d_19_value_).authTag)) == ((d_13_encAlg_).tagLength), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESEncryption did not return valid tag")))
        if (d_21_valueOrError3_).IsFailure():
            res = (d_21_valueOrError3_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_19_value_)
        return res
        return res

    @staticmethod
    def AESDecrypt(input):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_22_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_22_valueOrError0_ = Wrappers.default__.Need((((len((input).key)) == (((input).encAlg).keyLength)) and ((len((input).iv)) == (((input).encAlg).ivLength))) and ((len((input).authTag)) == (((input).encAlg).tagLength)), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Request does not match algorithm.")))
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
        d_29_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out2_: Wrappers.Result
        out2_ = AESEncryption.AES_GCM.AESDecryptExtern(d_23_encAlg_, d_24_key_, d_25_cipherTxt_, d_26_authTag_, d_27_iv_, d_28_aad_)
        d_29_valueOrError1_ = out2_
        if (d_29_valueOrError1_).IsFailure():
            res = (d_29_valueOrError1_).PropagateFailure()
            return res
        d_30_value_: _dafny.Seq
        d_30_value_ = (d_29_valueOrError1_).Extract()
        d_31_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_31_valueOrError2_ = Wrappers.default__.Need((len(d_25_cipherTxt_)) == (len(d_30_value_)), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("AESDecrypt did not return plaintext of expected length")))
        if (d_31_valueOrError2_).IsFailure():
            res = (d_31_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_30_value_)
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

