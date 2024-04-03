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

# Module: UnicodeStrings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsWellFormedString(s):
        def lambda2_(d_158_c_):
            return ord(d_158_c_)

        return Utf16EncodingForm.default__.IsWellFormedCodeUnitSequence(Seq.default__.Map(lambda2_, s))

    @staticmethod
    def ToUTF8Checked(s):
        def lambda3_(d_160_c_):
            return ord(d_160_c_)

        d_159_asCodeUnits_ = Seq.default__.Map(lambda3_, s)
        d_161_valueOrError0_ = Utf16EncodingForm.default__.DecodeCodeUnitSequenceChecked(d_159_asCodeUnits_)
        if (d_161_valueOrError0_).IsFailure():
            return (d_161_valueOrError0_).PropagateFailure()
        elif True:
            d_162_utf32_ = (d_161_valueOrError0_).Extract()
            d_163_asUtf8CodeUnits_ = Utf8EncodingForm.default__.EncodeScalarSequence(d_162_utf32_)
            def lambda4_(d_164_c_):
                return d_164_c_

            return Wrappers.Option_Some(Seq.default__.Map(lambda4_, d_163_asUtf8CodeUnits_))

    @staticmethod
    def FromUTF8Checked(bs):
        def lambda5_(d_166_c_):
            return d_166_c_

        d_165_asCodeUnits_ = Seq.default__.Map(lambda5_, bs)
        d_167_valueOrError0_ = Utf8EncodingForm.default__.DecodeCodeUnitSequenceChecked(d_165_asCodeUnits_)
        if (d_167_valueOrError0_).IsFailure():
            return (d_167_valueOrError0_).PropagateFailure()
        elif True:
            d_168_utf32_ = (d_167_valueOrError0_).Extract()
            d_169_asUtf16CodeUnits_ = Utf16EncodingForm.default__.EncodeScalarSequence(d_168_utf32_)
            def lambda6_(d_170_cu_):
                return chr(d_170_cu_)

            return Wrappers.Option_Some(Seq.default__.Map(lambda6_, d_169_asUtf16CodeUnits_))

    @staticmethod
    def ToUTF16Checked(s):
        def lambda7_(d_171_c_):
            return ord(d_171_c_)

        if Utf16EncodingForm.default__.IsWellFormedCodeUnitSequence(Seq.default__.Map(lambda7_, s)):
            def lambda8_(d_172_c_):
                return ord(d_172_c_)

            return Wrappers.Option_Some(Seq.default__.Map(lambda8_, s))
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def FromUTF16Checked(bs):
        def lambda9_(d_173_c_):
            return d_173_c_

        if Utf16EncodingForm.default__.IsWellFormedCodeUnitSequence(Seq.default__.Map(lambda9_, bs)):
            def lambda10_(d_174_c_):
                return chr(d_174_c_)

            return Wrappers.Option_Some(Seq.default__.Map(lambda10_, bs))
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def ASCIIToUTF8(s):
        def lambda11_(d_175_c_):
            return ord(d_175_c_)

        return Seq.default__.Map(lambda11_, s)

    @staticmethod
    def ASCIIToUTF16(s):
        def lambda12_(d_176_c_):
            return ord(d_176_c_)

        return Seq.default__.Map(lambda12_, s)

