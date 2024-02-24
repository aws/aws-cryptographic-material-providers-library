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
import DafnyLibraries
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
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
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

# Module: KdfCtr

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def KdfCounterMode(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_71_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_71_valueOrError0_ = Wrappers.default__.Need((((((((input).digestAlgorithm) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256())) and ((len((input).ikm)) == (32))) and (((input).nonce).is_Some)) and ((len(((input).nonce).value)) == (16))) and (((input).expectedLength) == (32))) and (((0) < (((input).expectedLength) * (8))) and ((((input).expectedLength) * (8)) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Kdf in Counter Mode input is invalid.")))
        if (d_71_valueOrError0_).IsFailure():
            output = (d_71_valueOrError0_).PropagateFailure()
            return output
        d_72_ikm_: _dafny.Seq
        d_72_ikm_ = (input).ikm
        d_73_label___: _dafny.Seq
        d_73_label___ = ((input).purpose).UnwrapOr(_dafny.Seq([]))
        d_74_info_: _dafny.Seq
        d_74_info_ = ((input).nonce).UnwrapOr(_dafny.Seq([]))
        d_75_okm_: _dafny.Seq
        d_75_okm_ = _dafny.Seq([])
        d_76_internalLength_: int
        d_76_internalLength_ = ((4) + (len(default__.SEPARATION__INDICATOR))) + (4)
        d_77_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_77_valueOrError1_ = Wrappers.default__.Need((True) and ((((d_76_internalLength_) + (len(d_73_label___))) + (len(d_74_info_))) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Input Length exceeds INT32_MAX_LIMIT")))
        if (d_77_valueOrError1_).IsFailure():
            output = (d_77_valueOrError1_).PropagateFailure()
            return output
        d_78_lengthBits_: _dafny.Seq
        d_78_lengthBits_ = StandardLibrary_UInt.default__.UInt32ToSeq(((input).expectedLength) * (8))
        d_79_explicitInfo_: _dafny.Seq
        d_79_explicitInfo_ = (((d_73_label___) + (default__.SEPARATION__INDICATOR)) + (d_74_info_)) + (d_78_lengthBits_)
        d_80_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_80_valueOrError2_ = Wrappers.default__.Need(((4) + (len(d_79_explicitInfo_))) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("PRF input length exceeds INT32_MAX_LIMIT.")))
        if (d_80_valueOrError2_).IsFailure():
            output = (d_80_valueOrError2_).PropagateFailure()
            return output
        d_81_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out15_: Wrappers.Result
        out15_ = default__.RawDerive(d_72_ikm_, d_79_explicitInfo_, (input).expectedLength, 0)
        d_81_valueOrError3_ = out15_
        if (d_81_valueOrError3_).IsFailure():
            output = (d_81_valueOrError3_).PropagateFailure()
            return output
        d_75_okm_ = (d_81_valueOrError3_).Extract()
        output = Wrappers.Result_Success(d_75_okm_)
        return output
        return output

    @staticmethod
    def RawDerive(ikm, explicitInfo, length, offset):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_82_derivationMac_: software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm
        d_82_derivationMac_ = software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()
        d_83_hmac_: HMAC.HMac
        d_84_valueOrError0_: Wrappers.Result = None
        out16_: Wrappers.Result
        out16_ = HMAC.HMac.Build(d_82_derivationMac_)
        d_84_valueOrError0_ = out16_
        if (d_84_valueOrError0_).IsFailure():
            output = (d_84_valueOrError0_).PropagateFailure()
            return output
        d_83_hmac_ = (d_84_valueOrError0_).Extract()
        (d_83_hmac_).Init(ikm)
        d_85_macLengthBytes_: int
        d_85_macLengthBytes_ = Digest.default__.Length(d_82_derivationMac_)
        d_86_iterations_: int
        d_86_iterations_ = _dafny.euclidian_division(((length) + (d_85_macLengthBytes_)) - (1), d_85_macLengthBytes_)
        d_87_buffer_: _dafny.Seq
        d_87_buffer_ = _dafny.Seq([])
        d_88_i_: _dafny.Seq
        d_88_i_ = StandardLibrary_UInt.default__.UInt32ToSeq(default__.COUNTER__START__VALUE)
        hi0_ = (d_86_iterations_) + (1)
        for d_89_iteration_ in range(1, hi0_):
            (d_83_hmac_).BlockUpdate(d_88_i_)
            (d_83_hmac_).BlockUpdate(explicitInfo)
            d_90_tmp_: _dafny.Seq
            out17_: _dafny.Seq
            out17_ = (d_83_hmac_).GetResult()
            d_90_tmp_ = out17_
            d_87_buffer_ = (d_87_buffer_) + (d_90_tmp_)
            d_91_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_91_valueOrError1_ = default__.Increment(d_88_i_)
            if (d_91_valueOrError1_).IsFailure():
                output = (d_91_valueOrError1_).PropagateFailure()
                return output
            d_88_i_ = (d_91_valueOrError1_).Extract()
        d_92_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_92_valueOrError2_ = Wrappers.default__.Need((len(d_87_buffer_)) >= (length), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Failed to derive key of requested length")))
        if (d_92_valueOrError2_).IsFailure():
            output = (d_92_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(_dafny.Seq((d_87_buffer_)[:length:]))
        return output
        return output

    @staticmethod
    def Increment(x):
        if ((x)[3]) < (255):
            return Wrappers.Result_Success(_dafny.Seq([(x)[0], (x)[1], (x)[2], ((x)[3]) + (1)]))
        elif ((x)[2]) < (255):
            return Wrappers.Result_Success(_dafny.Seq([(x)[0], (x)[1], ((x)[2]) + (1), 0]))
        elif ((x)[1]) < (255):
            return Wrappers.Result_Success(_dafny.Seq([(x)[0], ((x)[1]) + (1), 0, 0]))
        elif ((x)[0]) < (255):
            return Wrappers.Result_Success(_dafny.Seq([((x)[0]) + (1), 0, 0, 0]))
        elif True:
            return Wrappers.Result_Failure(software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Unable to derive key material; may have exceeded limit.")))

    @_dafny.classproperty
    def SEPARATION__INDICATOR(instance):
        return _dafny.Seq([0])
    @_dafny.classproperty
    def COUNTER__START__VALUE(instance):
        return 1
