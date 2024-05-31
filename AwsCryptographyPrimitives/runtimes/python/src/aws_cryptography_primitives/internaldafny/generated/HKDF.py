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

# Module: HKDF

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Extract(hmac, salt, ikm):
        prk: _dafny.Seq = _dafny.Seq({})
        (hmac).Init(salt)
        (hmac).BlockUpdate(ikm)
        out4_: _dafny.Seq
        out4_ = (hmac).GetResult()
        prk = out4_
        prk = prk
        return prk
        return prk

    @staticmethod
    def Expand(hmac, prk, info, expectedLength, digest):
        okm: _dafny.Seq = _dafny.Seq({})
        d_41_hashLength_: int
        d_41_hashLength_ = Digest.default__.Length(digest)
        d_42_n_: int
        d_42_n_ = _dafny.euclidian_division(((d_41_hashLength_) + (expectedLength)) - (1), d_41_hashLength_)
        (hmac).Init(prk)
        d_43_t__prev_: _dafny.Seq
        d_43_t__prev_ = _dafny.Seq([])
        d_44_t__n_: _dafny.Seq
        d_44_t__n_ = d_43_t__prev_
        d_45_i_: int
        d_45_i_ = 1
        while (d_45_i_) <= (d_42_n_):
            (hmac).BlockUpdate(d_43_t__prev_)
            (hmac).BlockUpdate(info)
            (hmac).BlockUpdate(_dafny.Seq([d_45_i_]))
            out5_: _dafny.Seq
            out5_ = (hmac).GetResult()
            d_43_t__prev_ = out5_
            d_44_t__n_ = (d_44_t__n_) + (d_43_t__prev_)
            d_45_i_ = (d_45_i_) + (1)
        okm = d_44_t__n_
        if (expectedLength) < (len(okm)):
            okm = _dafny.Seq((okm)[:expectedLength:])
        return okm

    @staticmethod
    def Hkdf(digest, salt, ikm, info, L):
        okm: _dafny.Seq = _dafny.Seq({})
        if (L) == (0):
            okm = _dafny.Seq([])
            return okm
        d_46_hmac_: HMAC.HMac
        d_47_valueOrError0_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = HMAC.HMac.Build(digest)
        d_47_valueOrError0_ = out6_
        if not(not((d_47_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("src/HKDF/HKDF.dfy(222,16): " + _dafny.string_of(d_47_valueOrError0_))
        d_46_hmac_ = (d_47_valueOrError0_).Extract()
        d_48_hashLength_: int
        d_48_hashLength_ = Digest.default__.Length(digest)
        d_49_nonEmptySalt_: _dafny.Seq = _dafny.Seq({})
        source1_ = salt
        if source1_.is_None:
            d_49_nonEmptySalt_ = StandardLibrary.default__.Fill(0, d_48_hashLength_)
        elif True:
            d_50___mcc_h0_ = source1_.value
            d_51_s_ = d_50___mcc_h0_
            d_49_nonEmptySalt_ = d_51_s_
        d_52_prk_: _dafny.Seq
        out7_: _dafny.Seq
        out7_ = default__.Extract(d_46_hmac_, d_49_nonEmptySalt_, ikm)
        d_52_prk_ = out7_
        out8_: _dafny.Seq
        out8_ = default__.Expand(d_46_hmac_, d_52_prk_, info, L, digest)
        okm = out8_
        return okm

