import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import standard_library.internaldafny.generated.module_ as module_
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

# Module: UnicodeStrings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsWellFormedString(s):
        def lambda2_(d_149_c_):
            return ord(d_149_c_)

        return Utf16EncodingForm.default__.IsWellFormedCodeUnitSequence(Seq.default__.Map(lambda2_, s))

    @staticmethod
    def ToUTF8Checked(s):
        def lambda3_(d_151_c_):
            return ord(d_151_c_)

        d_150_asCodeUnits_ = Seq.default__.Map(lambda3_, s)
        d_152_valueOrError0_ = Utf16EncodingForm.default__.DecodeCodeUnitSequenceChecked(d_150_asCodeUnits_)
        if (d_152_valueOrError0_).IsFailure():
            return (d_152_valueOrError0_).PropagateFailure()
        elif True:
            d_153_utf32_ = (d_152_valueOrError0_).Extract()
            d_154_asUtf8CodeUnits_ = Utf8EncodingForm.default__.EncodeScalarSequence(d_153_utf32_)
            def lambda4_(d_155_c_):
                return d_155_c_

            return Wrappers.Option_Some(Seq.default__.Map(lambda4_, d_154_asUtf8CodeUnits_))

    @staticmethod
    def FromUTF8Checked(bs):
        def lambda5_(d_157_c_):
            return d_157_c_

        d_156_asCodeUnits_ = Seq.default__.Map(lambda5_, bs)
        d_158_valueOrError0_ = Utf8EncodingForm.default__.DecodeCodeUnitSequenceChecked(d_156_asCodeUnits_)
        if (d_158_valueOrError0_).IsFailure():
            return (d_158_valueOrError0_).PropagateFailure()
        elif True:
            d_159_utf32_ = (d_158_valueOrError0_).Extract()
            d_160_asUtf16CodeUnits_ = Utf16EncodingForm.default__.EncodeScalarSequence(d_159_utf32_)
            def lambda6_(d_161_cu_):
                return chr(d_161_cu_)

            return Wrappers.Option_Some(Seq.default__.Map(lambda6_, d_160_asUtf16CodeUnits_))

    @staticmethod
    def ToUTF16Checked(s):
        def lambda7_(d_162_c_):
            return ord(d_162_c_)

        if Utf16EncodingForm.default__.IsWellFormedCodeUnitSequence(Seq.default__.Map(lambda7_, s)):
            def lambda8_(d_163_c_):
                return ord(d_163_c_)

            return Wrappers.Option_Some(Seq.default__.Map(lambda8_, s))
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def FromUTF16Checked(bs):
        def lambda9_(d_164_c_):
            return d_164_c_

        if Utf16EncodingForm.default__.IsWellFormedCodeUnitSequence(Seq.default__.Map(lambda9_, bs)):
            def lambda10_(d_165_c_):
                return chr(d_165_c_)

            return Wrappers.Option_Some(Seq.default__.Map(lambda10_, bs))
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def ASCIIToUTF8(s):
        def lambda11_(d_166_c_):
            return ord(d_166_c_)

        return Seq.default__.Map(lambda11_, s)

    @staticmethod
    def ASCIIToUTF16(s):
        def lambda12_(d_167_c_):
            return ord(d_167_c_)

        return Seq.default__.Map(lambda12_, s)

