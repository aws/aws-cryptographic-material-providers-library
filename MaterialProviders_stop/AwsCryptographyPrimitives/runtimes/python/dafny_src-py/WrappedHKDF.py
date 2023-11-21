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
import software_amazon_cryptography_primitives_internaldafny_types
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF

assert "WrappedHKDF" == __name__
WrappedHKDF = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Extract(input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_46_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_46_valueOrError0_ = Wrappers.default__.Need(((((input).salt).is_None) or ((len(((input).salt).value)) != (0))) and ((len((input).ikm)) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("HKDF Extract needs a salt and reasonable ikm.")))
        if (d_46_valueOrError0_).IsFailure():
            output = (d_46_valueOrError0_).PropagateFailure()
            return output
        let_tmp_rhs3_ = input
        d_47_digestAlgorithm_ = let_tmp_rhs3_.digestAlgorithm
        d_48_salt_ = let_tmp_rhs3_.salt
        d_49_ikm_ = let_tmp_rhs3_.ikm
        d_50_hmac_: HMAC.HMac
        d_51_valueOrError1_: Wrappers.Result = None
        out9_: Wrappers.Result
        out9_ = HMAC.HMac.Build(d_47_digestAlgorithm_)
        d_51_valueOrError1_ = out9_
        if (d_51_valueOrError1_).IsFailure():
            output = (d_51_valueOrError1_).PropagateFailure()
            return output
        d_50_hmac_ = (d_51_valueOrError1_).Extract()
        d_52_prk_: _dafny.Seq
        out10_: _dafny.Seq
        out10_ = HKDF.default__.Extract(d_50_hmac_, (d_48_salt_).UnwrapOr(StandardLibrary.default__.Fill(0, Digest.default__.Length(d_47_digestAlgorithm_))), d_49_ikm_)
        d_52_prk_ = out10_
        output = Wrappers.Result_Success(d_52_prk_)
        return output
        return output

    @staticmethod
    def Expand(input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_53_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_53_valueOrError0_ = Wrappers.default__.Need(((((1) <= ((input).expectedLength)) and (((input).expectedLength) <= ((255) * (Digest.default__.Length((input).digestAlgorithm))))) and ((len((input).info)) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT))) and ((Digest.default__.Length((input).digestAlgorithm)) == (len((input).prk))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("HKDF Expand needs valid input.")))
        if (d_53_valueOrError0_).IsFailure():
            output = (d_53_valueOrError0_).PropagateFailure()
            return output
        let_tmp_rhs4_ = input
        d_54_digestAlgorithm_ = let_tmp_rhs4_.digestAlgorithm
        d_55_prk_ = let_tmp_rhs4_.prk
        d_56_info_ = let_tmp_rhs4_.info
        d_57_expectedLength_ = let_tmp_rhs4_.expectedLength
        d_58_hmac_: HMAC.HMac
        d_59_valueOrError1_: Wrappers.Result = None
        out11_: Wrappers.Result
        out11_ = HMAC.HMac.Build(d_54_digestAlgorithm_)
        d_59_valueOrError1_ = out11_
        if (d_59_valueOrError1_).IsFailure():
            output = (d_59_valueOrError1_).PropagateFailure()
            return output
        d_58_hmac_ = (d_59_valueOrError1_).Extract()
        d_60_omk_: _dafny.Seq
        out12_: _dafny.Seq
        out12_ = HKDF.default__.Expand(d_58_hmac_, d_55_prk_, d_56_info_, d_57_expectedLength_, d_54_digestAlgorithm_)
        d_60_omk_ = out12_
        output = Wrappers.Result_Success(d_60_omk_)
        return output
        return output

    @staticmethod
    def Hkdf(input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_61_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_61_valueOrError0_ = Wrappers.default__.Need((((((1) <= ((input).expectedLength)) and (((input).expectedLength) <= ((255) * (Digest.default__.Length((input).digestAlgorithm))))) and ((((input).salt).is_None) or ((len(((input).salt).value)) != (0)))) and ((len((input).info)) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT))) and ((len((input).ikm)) < ((StandardLibrary_mUInt.default__).INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Wrapped Hkdf input is invalid.")))
        if (d_61_valueOrError0_).IsFailure():
            output = (d_61_valueOrError0_).PropagateFailure()
            return output
        let_tmp_rhs5_ = input
        d_62_digest_ = let_tmp_rhs5_.digestAlgorithm
        d_63_salt_ = let_tmp_rhs5_.salt
        d_64_ikm_ = let_tmp_rhs5_.ikm
        d_65_info_ = let_tmp_rhs5_.info
        d_66_expectedLength_ = let_tmp_rhs5_.expectedLength
        d_67_okm_: _dafny.Seq
        out13_: _dafny.Seq
        out13_ = HKDF.default__.Hkdf(d_62_digest_, d_63_salt_, d_64_ikm_, d_65_info_, d_66_expectedLength_)
        d_67_okm_ = out13_
        output = Wrappers.Result_Success(d_67_okm_)
        return output
        return output

