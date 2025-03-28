import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import smithy_dafny_standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm

# Module: UnicodeStrings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsWellFormedString(s):
        def lambda0_(d_0_c_):
            return ord(d_0_c_)

        return Utf16EncodingForm.default__.IsWellFormedCodeUnitSequence(Seq.default__.Map(lambda0_, s))

    @staticmethod
    def ToUTF8Checked(s):
        def lambda0_(d_1_c_):
            return ord(d_1_c_)

        d_0_asCodeUnits_ = Seq.default__.Map(lambda0_, s)
        d_2_valueOrError0_ = Utf16EncodingForm.default__.DecodeCodeUnitSequenceChecked(d_0_asCodeUnits_)
        if (d_2_valueOrError0_).IsFailure():
            return (d_2_valueOrError0_).PropagateFailure()
        elif True:
            d_3_utf32_ = (d_2_valueOrError0_).Extract()
            d_4_asUtf8CodeUnits_ = Utf8EncodingForm.default__.EncodeScalarSequence(d_3_utf32_)
            def lambda1_(d_5_c_):
                return d_5_c_

            return Wrappers.Option_Some(Seq.default__.Map(lambda1_, d_4_asUtf8CodeUnits_))

    @staticmethod
    def FromUTF8Checked(bs):
        def lambda0_(d_1_c_):
            return d_1_c_

        d_0_asCodeUnits_ = Seq.default__.Map(lambda0_, bs)
        d_2_valueOrError0_ = Utf8EncodingForm.default__.DecodeCodeUnitSequenceChecked(d_0_asCodeUnits_)
        if (d_2_valueOrError0_).IsFailure():
            return (d_2_valueOrError0_).PropagateFailure()
        elif True:
            d_3_utf32_ = (d_2_valueOrError0_).Extract()
            d_4_asUtf16CodeUnits_ = Utf16EncodingForm.default__.EncodeScalarSequence(d_3_utf32_)
            def lambda1_(d_5_cu_):
                return chr(d_5_cu_)

            return Wrappers.Option_Some(Seq.default__.Map(lambda1_, d_4_asUtf16CodeUnits_))

    @staticmethod
    def ToUTF16Checked(s):
        def lambda0_(d_0_c_):
            return ord(d_0_c_)

        if Utf16EncodingForm.default__.IsWellFormedCodeUnitSequence(Seq.default__.Map(lambda0_, s)):
            def lambda1_(d_1_c_):
                return ord(d_1_c_)

            return Wrappers.Option_Some(Seq.default__.Map(lambda1_, s))
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def FromUTF16Checked(bs):
        def lambda0_(d_0_c_):
            return d_0_c_

        if Utf16EncodingForm.default__.IsWellFormedCodeUnitSequence(Seq.default__.Map(lambda0_, bs)):
            def lambda1_(d_1_c_):
                return chr(d_1_c_)

            return Wrappers.Option_Some(Seq.default__.Map(lambda1_, bs))
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def ASCIIToUTF8(s):
        def lambda0_(d_0_c_):
            return ord(d_0_c_)

        return Seq.default__.Map(lambda0_, s)

    @staticmethod
    def ASCIIToUTF16(s):
        def lambda0_(d_0_c_):
            return ord(d_0_c_)

        return Seq.default__.Map(lambda0_, s)

