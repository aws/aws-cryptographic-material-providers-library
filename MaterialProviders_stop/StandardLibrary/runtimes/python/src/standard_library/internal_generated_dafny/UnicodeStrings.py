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

assert "UnicodeStrings" == __name__
UnicodeStrings = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsWellFormedString(s):
        def lambda2_(d_145_c_):
            return ord(d_145_c_)

        return Utf16EncodingForm.default__.IsWellFormedCodeUnitSequence(Seq.default__.Map(lambda2_, s))

    @staticmethod
    def ToUTF8Checked(s):
        def lambda3_(d_147_c_):
            return ord(d_147_c_)

        d_146_asCodeUnits_ = Seq.default__.Map(lambda3_, s)
        d_148_valueOrError0_ = Utf16EncodingForm.default__.DecodeCodeUnitSequenceChecked(d_146_asCodeUnits_)
        if (d_148_valueOrError0_).IsFailure():
            return (d_148_valueOrError0_).PropagateFailure()
        elif True:
            d_149_utf32_ = (d_148_valueOrError0_).Extract()
            d_150_asUtf8CodeUnits_ = Utf8EncodingForm.default__.EncodeScalarSequence(d_149_utf32_)
            def lambda4_(d_151_c_):
                return d_151_c_

            return Wrappers.Option_Some(Seq.default__.Map(lambda4_, d_150_asUtf8CodeUnits_))

    @staticmethod
    def FromUTF8Checked(bs):
        def lambda5_(d_153_c_):
            return d_153_c_

        d_152_asCodeUnits_ = Seq.default__.Map(lambda5_, bs)
        d_154_valueOrError0_ = Utf8EncodingForm.default__.DecodeCodeUnitSequenceChecked(d_152_asCodeUnits_)
        if (d_154_valueOrError0_).IsFailure():
            return (d_154_valueOrError0_).PropagateFailure()
        elif True:
            d_155_utf32_ = (d_154_valueOrError0_).Extract()
            d_156_asUtf16CodeUnits_ = Utf16EncodingForm.default__.EncodeScalarSequence(d_155_utf32_)
            def lambda6_(d_157_cu_):
                return chr(d_157_cu_)

            return Wrappers.Option_Some(Seq.default__.Map(lambda6_, d_156_asUtf16CodeUnits_))

    @staticmethod
    def ToUTF16Checked(s):
        def lambda7_(d_158_c_):
            return ord(d_158_c_)

        if Utf16EncodingForm.default__.IsWellFormedCodeUnitSequence(Seq.default__.Map(lambda7_, s)):
            def lambda8_(d_159_c_):
                return ord(d_159_c_)

            return Wrappers.Option_Some(Seq.default__.Map(lambda8_, s))
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def FromUTF16Checked(bs):
        def lambda9_(d_160_c_):
            return d_160_c_

        if Utf16EncodingForm.default__.IsWellFormedCodeUnitSequence(Seq.default__.Map(lambda9_, bs)):
            def lambda10_(d_161_c_):
                return chr(d_161_c_)

            return Wrappers.Option_Some(Seq.default__.Map(lambda10_, bs))
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def ASCIIToUTF8(s):
        def lambda11_(d_162_c_):
            return ord(d_162_c_)

        return Seq.default__.Map(lambda11_, s)

    @staticmethod
    def ASCIIToUTF16(s):
        def lambda12_(d_163_c_):
            return ord(d_163_c_)

        return Seq.default__.Map(lambda12_, s)

