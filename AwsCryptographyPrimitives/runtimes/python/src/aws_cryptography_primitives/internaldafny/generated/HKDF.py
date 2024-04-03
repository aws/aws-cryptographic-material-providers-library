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

