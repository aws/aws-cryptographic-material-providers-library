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

# Module: Digest

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Length(digestAlgorithm):
        source0_ = digestAlgorithm
        if source0_.is_SHA__512:
            return 64
        elif source0_.is_SHA__384:
            return 48
        elif True:
            return 32

    @staticmethod
    def Digest(input):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        let_tmp_rhs2_ = input
        d_32_digestAlgorithm_ = let_tmp_rhs2_.digestAlgorithm
        d_33_message_ = let_tmp_rhs2_.message
        d_34_value_: _dafny.Seq
        d_35_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out3_: Wrappers.Result
        out3_ = ExternDigest.default__.Digest(d_32_digestAlgorithm_, d_33_message_)
        d_35_valueOrError0_ = out3_
        if (d_35_valueOrError0_).IsFailure():
            res = (d_35_valueOrError0_).PropagateFailure()
            return res
        d_34_value_ = (d_35_valueOrError0_).Extract()
        d_36_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_36_valueOrError1_ = Wrappers.default__.Need((len(d_34_value_)) == (default__.Length(d_32_digestAlgorithm_)), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Incorrect length digest from ExternDigest.")))
        if (d_36_valueOrError1_).IsFailure():
            res = (d_36_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_34_value_)
        return res
        return res

