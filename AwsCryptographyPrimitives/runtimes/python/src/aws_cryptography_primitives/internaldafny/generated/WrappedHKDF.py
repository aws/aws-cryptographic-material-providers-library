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

# Module: WrappedHKDF

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Extract(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_52_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_52_valueOrError0_ = Wrappers.default__.Need(((((input).salt).is_None) or ((len(((input).salt).value)) != (0))) and ((len((input).ikm)) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT)), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("HKDF Extract needs a salt and reasonable ikm.")))
        if (d_52_valueOrError0_).IsFailure():
            output = (d_52_valueOrError0_).PropagateFailure()
            return output
        let_tmp_rhs3_ = input
        d_53_digestAlgorithm_ = let_tmp_rhs3_.digestAlgorithm
        d_54_salt_ = let_tmp_rhs3_.salt
        d_55_ikm_ = let_tmp_rhs3_.ikm
        d_56_hmac_: HMAC.HMac
        d_57_valueOrError1_: Wrappers.Result = None
        out9_: Wrappers.Result
        out9_ = HMAC.HMac.Build(d_53_digestAlgorithm_)
        d_57_valueOrError1_ = out9_
        if (d_57_valueOrError1_).IsFailure():
            output = (d_57_valueOrError1_).PropagateFailure()
            return output
        d_56_hmac_ = (d_57_valueOrError1_).Extract()
        d_58_prk_: _dafny.Seq
        out10_: _dafny.Seq
        out10_ = HKDF.default__.Extract(d_56_hmac_, (d_54_salt_).UnwrapOr(StandardLibrary.default__.Fill(0, Digest.default__.Length(d_53_digestAlgorithm_))), d_55_ikm_)
        d_58_prk_ = out10_
        output = Wrappers.Result_Success(d_58_prk_)
        return output
        return output

    @staticmethod
    def Expand(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_59_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_59_valueOrError0_ = Wrappers.default__.Need(((((1) <= ((input).expectedLength)) and (((input).expectedLength) <= ((255) * (Digest.default__.Length((input).digestAlgorithm))))) and ((len((input).info)) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT))) and ((Digest.default__.Length((input).digestAlgorithm)) == (len((input).prk))), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("HKDF Expand needs valid input.")))
        if (d_59_valueOrError0_).IsFailure():
            output = (d_59_valueOrError0_).PropagateFailure()
            return output
        let_tmp_rhs4_ = input
        d_60_digestAlgorithm_ = let_tmp_rhs4_.digestAlgorithm
        d_61_prk_ = let_tmp_rhs4_.prk
        d_62_info_ = let_tmp_rhs4_.info
        d_63_expectedLength_ = let_tmp_rhs4_.expectedLength
        d_64_hmac_: HMAC.HMac
        d_65_valueOrError1_: Wrappers.Result = None
        out11_: Wrappers.Result
        out11_ = HMAC.HMac.Build(d_60_digestAlgorithm_)
        d_65_valueOrError1_ = out11_
        if (d_65_valueOrError1_).IsFailure():
            output = (d_65_valueOrError1_).PropagateFailure()
            return output
        d_64_hmac_ = (d_65_valueOrError1_).Extract()
        d_66_omk_: _dafny.Seq
        out12_: _dafny.Seq
        out12_ = HKDF.default__.Expand(d_64_hmac_, d_61_prk_, d_62_info_, d_63_expectedLength_, d_60_digestAlgorithm_)
        d_66_omk_ = out12_
        output = Wrappers.Result_Success(d_66_omk_)
        return output
        return output

    @staticmethod
    def Hkdf(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_67_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_67_valueOrError0_ = Wrappers.default__.Need((((((1) <= ((input).expectedLength)) and (((input).expectedLength) <= ((255) * (Digest.default__.Length((input).digestAlgorithm))))) and ((((input).salt).is_None) or ((len(((input).salt).value)) != (0)))) and ((len((input).info)) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT))) and ((len((input).ikm)) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT)), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Wrapped Hkdf input is invalid.")))
        if (d_67_valueOrError0_).IsFailure():
            output = (d_67_valueOrError0_).PropagateFailure()
            return output
        let_tmp_rhs5_ = input
        d_68_digest_ = let_tmp_rhs5_.digestAlgorithm
        d_69_salt_ = let_tmp_rhs5_.salt
        d_70_ikm_ = let_tmp_rhs5_.ikm
        d_71_info_ = let_tmp_rhs5_.info
        d_72_expectedLength_ = let_tmp_rhs5_.expectedLength
        d_73_okm_: _dafny.Seq
        out13_: _dafny.Seq
        out13_ = HKDF.default__.Hkdf(d_68_digest_, d_69_salt_, d_70_ikm_, d_71_info_, d_72_expectedLength_)
        d_73_okm_ = out13_
        output = Wrappers.Result_Success(d_73_okm_)
        return output
        return output

