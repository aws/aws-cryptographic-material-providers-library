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
        d_78_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_78_valueOrError0_ = Wrappers.default__.Need((((((((input).digestAlgorithm) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256())) and ((len((input).ikm)) == (32))) and (((input).nonce).is_Some)) and ((len(((input).nonce).value)) == (16))) and (((input).expectedLength) == (32))) and (((0) < (((input).expectedLength) * (8))) and ((((input).expectedLength) * (8)) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT))), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Kdf in Counter Mode input is invalid.")))
        if (d_78_valueOrError0_).IsFailure():
            output = (d_78_valueOrError0_).PropagateFailure()
            return output
        d_79_ikm_: _dafny.Seq
        d_79_ikm_ = (input).ikm
        d_80_label___: _dafny.Seq
        d_80_label___ = ((input).purpose).UnwrapOr(_dafny.Seq([]))
        d_81_info_: _dafny.Seq
        d_81_info_ = ((input).nonce).UnwrapOr(_dafny.Seq([]))
        d_82_okm_: _dafny.Seq
        d_82_okm_ = _dafny.Seq([])
        d_83_internalLength_: int
        d_83_internalLength_ = ((4) + (len(default__.SEPARATION__INDICATOR))) + (4)
        d_84_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_84_valueOrError1_ = Wrappers.default__.Need((True) and ((((d_83_internalLength_) + (len(d_80_label___))) + (len(d_81_info_))) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Input Length exceeds INT32_MAX_LIMIT")))
        if (d_84_valueOrError1_).IsFailure():
            output = (d_84_valueOrError1_).PropagateFailure()
            return output
        d_85_lengthBits_: _dafny.Seq
        d_85_lengthBits_ = StandardLibrary_UInt.default__.UInt32ToSeq(((input).expectedLength) * (8))
        d_86_explicitInfo_: _dafny.Seq
        d_86_explicitInfo_ = (((d_80_label___) + (default__.SEPARATION__INDICATOR)) + (d_81_info_)) + (d_85_lengthBits_)
        d_87_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_87_valueOrError2_ = Wrappers.default__.Need(((4) + (len(d_86_explicitInfo_))) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("PRF input length exceeds INT32_MAX_LIMIT.")))
        if (d_87_valueOrError2_).IsFailure():
            output = (d_87_valueOrError2_).PropagateFailure()
            return output
        d_88_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out15_: Wrappers.Result
        out15_ = default__.RawDerive(d_79_ikm_, d_86_explicitInfo_, (input).expectedLength, 0)
        d_88_valueOrError3_ = out15_
        if (d_88_valueOrError3_).IsFailure():
            output = (d_88_valueOrError3_).PropagateFailure()
            return output
        d_82_okm_ = (d_88_valueOrError3_).Extract()
        output = Wrappers.Result_Success(d_82_okm_)
        return output
        return output

    @staticmethod
    def RawDerive(ikm, explicitInfo, length, offset):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_89_derivationMac_: software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm
        d_89_derivationMac_ = software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()
        d_90_hmac_: HMAC.HMac
        d_91_valueOrError0_: Wrappers.Result = None
        out16_: Wrappers.Result
        out16_ = HMAC.HMac.Build(d_89_derivationMac_)
        d_91_valueOrError0_ = out16_
        if (d_91_valueOrError0_).IsFailure():
            output = (d_91_valueOrError0_).PropagateFailure()
            return output
        d_90_hmac_ = (d_91_valueOrError0_).Extract()
        (d_90_hmac_).Init(ikm)
        d_92_macLengthBytes_: int
        d_92_macLengthBytes_ = Digest.default__.Length(d_89_derivationMac_)
        d_93_iterations_: int
        d_93_iterations_ = _dafny.euclidian_division(((length) + (d_92_macLengthBytes_)) - (1), d_92_macLengthBytes_)
        d_94_buffer_: _dafny.Seq
        d_94_buffer_ = _dafny.Seq([])
        d_95_i_: _dafny.Seq
        d_95_i_ = StandardLibrary_UInt.default__.UInt32ToSeq(default__.COUNTER__START__VALUE)
        hi0_ = (d_93_iterations_) + (1)
        for d_96_iteration_ in range(1, hi0_):
            (d_90_hmac_).BlockUpdate(d_95_i_)
            (d_90_hmac_).BlockUpdate(explicitInfo)
            d_97_tmp_: _dafny.Seq
            out17_: _dafny.Seq
            out17_ = (d_90_hmac_).GetResult()
            d_97_tmp_ = out17_
            d_94_buffer_ = (d_94_buffer_) + (d_97_tmp_)
            d_98_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_98_valueOrError1_ = default__.Increment(d_95_i_)
            if (d_98_valueOrError1_).IsFailure():
                output = (d_98_valueOrError1_).PropagateFailure()
                return output
            d_95_i_ = (d_98_valueOrError1_).Extract()
        d_99_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_99_valueOrError2_ = Wrappers.default__.Need((len(d_94_buffer_)) >= (length), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Failed to derive key of requested length")))
        if (d_99_valueOrError2_).IsFailure():
            output = (d_99_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(_dafny.Seq((d_94_buffer_)[:length:]))
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
