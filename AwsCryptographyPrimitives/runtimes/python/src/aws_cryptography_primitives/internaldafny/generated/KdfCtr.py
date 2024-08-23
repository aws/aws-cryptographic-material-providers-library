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
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature

# Module: KdfCtr

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def KdfCounterMode(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_77_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_77_valueOrError0_ = Wrappers.default__.Need(((((((((input).digestAlgorithm) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256())) or (((input).digestAlgorithm) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384()))) and ((((len((input).ikm)) == (32)) or ((len((input).ikm)) == (48))) or ((len((input).ikm)) == (66)))) and (((input).nonce).is_Some)) and (((len(((input).nonce).value)) == (16)) or ((len(((input).nonce).value)) == (32)))) and ((((input).expectedLength) == (32)) or (((input).expectedLength) == (64)))) and (((0) < (((input).expectedLength) * (8))) and ((((input).expectedLength) * (8)) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT))), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Kdf in Counter Mode input is invalid.")))
        if (d_77_valueOrError0_).IsFailure():
            output = (d_77_valueOrError0_).PropagateFailure()
            return output
        d_78_ikm_: _dafny.Seq
        d_78_ikm_ = (input).ikm
        d_79_label___: _dafny.Seq
        d_79_label___ = ((input).purpose).UnwrapOr(_dafny.Seq([]))
        d_80_info_: _dafny.Seq
        d_80_info_ = ((input).nonce).UnwrapOr(_dafny.Seq([]))
        d_81_okm_: _dafny.Seq
        d_81_okm_ = _dafny.Seq([])
        d_82_internalLength_: int
        d_82_internalLength_ = ((4) + (len(default__.SEPARATION__INDICATOR))) + (4)
        d_83_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_83_valueOrError1_ = Wrappers.default__.Need((True) and ((((d_82_internalLength_) + (len(d_79_label___))) + (len(d_80_info_))) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT)), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Input Length exceeds INT32_MAX_LIMIT")))
        if (d_83_valueOrError1_).IsFailure():
            output = (d_83_valueOrError1_).PropagateFailure()
            return output
        d_84_lengthBits_: _dafny.Seq
        d_84_lengthBits_ = StandardLibrary_UInt.default__.UInt32ToSeq(((input).expectedLength) * (8))
        d_85_explicitInfo_: _dafny.Seq
        d_85_explicitInfo_ = (((d_79_label___) + (default__.SEPARATION__INDICATOR)) + (d_80_info_)) + (d_84_lengthBits_)
        d_86_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_86_valueOrError2_ = Wrappers.default__.Need(((4) + (len(d_85_explicitInfo_))) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("PRF input length exceeds INT32_MAX_LIMIT.")))
        if (d_86_valueOrError2_).IsFailure():
            output = (d_86_valueOrError2_).PropagateFailure()
            return output
        d_87_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out15_: Wrappers.Result
        out15_ = default__.RawDerive(d_78_ikm_, d_85_explicitInfo_, (input).expectedLength, 0, (input).digestAlgorithm)
        d_87_valueOrError3_ = out15_
        if (d_87_valueOrError3_).IsFailure():
            output = (d_87_valueOrError3_).PropagateFailure()
            return output
        d_81_okm_ = (d_87_valueOrError3_).Extract()
        output = Wrappers.Result_Success(d_81_okm_)
        return output
        return output

    @staticmethod
    def RawDerive(ikm, explicitInfo, length, offset, digestAlgorithm):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_88_hmac_: HMAC.HMac
        d_89_valueOrError0_: Wrappers.Result = None
        out16_: Wrappers.Result
        out16_ = HMAC.HMac.Build(digestAlgorithm)
        d_89_valueOrError0_ = out16_
        if (d_89_valueOrError0_).IsFailure():
            output = (d_89_valueOrError0_).PropagateFailure()
            return output
        d_88_hmac_ = (d_89_valueOrError0_).Extract()
        (d_88_hmac_).Init(ikm)
        d_90_macLengthBytes_: int
        d_90_macLengthBytes_ = Digest.default__.Length(digestAlgorithm)
        d_91_iterations_: int
        d_91_iterations_ = _dafny.euclidian_division(((length) + (d_90_macLengthBytes_)) - (1), d_90_macLengthBytes_)
        d_92_buffer_: _dafny.Seq
        d_92_buffer_ = _dafny.Seq([])
        d_93_i_: _dafny.Seq
        d_93_i_ = StandardLibrary_UInt.default__.UInt32ToSeq(default__.COUNTER__START__VALUE)
        hi0_ = (d_91_iterations_) + (1)
        for d_94_iteration_ in range(1, hi0_):
            (d_88_hmac_).BlockUpdate(d_93_i_)
            (d_88_hmac_).BlockUpdate(explicitInfo)
            d_95_tmp_: _dafny.Seq
            out17_: _dafny.Seq
            out17_ = (d_88_hmac_).GetResult()
            d_95_tmp_ = out17_
            d_92_buffer_ = (d_92_buffer_) + (d_95_tmp_)
            d_96_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_96_valueOrError1_ = default__.Increment(d_93_i_)
            if (d_96_valueOrError1_).IsFailure():
                output = (d_96_valueOrError1_).PropagateFailure()
                return output
            d_93_i_ = (d_96_valueOrError1_).Extract()
        d_97_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_97_valueOrError2_ = Wrappers.default__.Need((len(d_92_buffer_)) >= (length), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Failed to derive key of requested length")))
        if (d_97_valueOrError2_).IsFailure():
            output = (d_97_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(_dafny.Seq((d_92_buffer_)[:length:]))
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
            return Wrappers.Result_Failure(AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Unable to derive key material; may have exceeded limit.")))

    @_dafny.classproperty
    def SEPARATION__INDICATOR(instance):
        return _dafny.Seq([0])
    @_dafny.classproperty
    def COUNTER__START__VALUE(instance):
        return 1
