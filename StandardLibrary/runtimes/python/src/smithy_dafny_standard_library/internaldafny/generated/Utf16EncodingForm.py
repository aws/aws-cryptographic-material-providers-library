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

# Module: Utf16EncodingForm

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsMinimalWellFormedCodeUnitSubsequence(s):
        if (len(s)) == (1):
            return default__.IsWellFormedSingleCodeUnitSequence(s)
        elif (len(s)) == (2):
            d_0_b_ = default__.IsWellFormedDoubleCodeUnitSequence(s)
            return d_0_b_
        elif True:
            return False

    @staticmethod
    def IsWellFormedSingleCodeUnitSequence(s):
        d_0_firstWord_ = (s)[0]
        return (((0) <= (d_0_firstWord_)) and ((d_0_firstWord_) <= (55295))) or (((57344) <= (d_0_firstWord_)) and ((d_0_firstWord_) <= (65535)))

    @staticmethod
    def IsWellFormedDoubleCodeUnitSequence(s):
        d_0_firstWord_ = (s)[0]
        d_1_secondWord_ = (s)[1]
        return (((55296) <= (d_0_firstWord_)) and ((d_0_firstWord_) <= (56319))) and (((56320) <= (d_1_secondWord_)) and ((d_1_secondWord_) <= (57343)))

    @staticmethod
    def SplitPrefixMinimalWellFormedCodeUnitSubsequence(s):
        if ((len(s)) >= (1)) and (default__.IsWellFormedSingleCodeUnitSequence(_dafny.Seq((s)[:1:]))):
            return Wrappers.Option_Some(_dafny.Seq((s)[:1:]))
        elif ((len(s)) >= (2)) and (default__.IsWellFormedDoubleCodeUnitSequence(_dafny.Seq((s)[:2:]))):
            return Wrappers.Option_Some(_dafny.Seq((s)[:2:]))
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def EncodeScalarValue(v):
        if (((0) <= (v)) and ((v) <= (55295))) or (((57344) <= (v)) and ((v) <= (65535))):
            return default__.EncodeScalarValueSingleWord(v)
        elif True:
            return default__.EncodeScalarValueDoubleWord(v)

    @staticmethod
    def EncodeScalarValueSingleWord(v):
        d_0_firstWord_ = v
        return _dafny.Seq([d_0_firstWord_])

    @staticmethod
    def EncodeScalarValueDoubleWord(v):
        d_0_x2_ = (v) & (1023)
        d_1_x1_ = ((v) & (64512)) >> (10)
        d_2_u_ = ((v) & (2031616)) >> (16)
        d_3_w_ = ((d_2_u_) - (1)) & ((1 << 5) - 1)
        d_4_firstWord_ = ((55296) | (((d_3_w_) << (6)) & ((1 << 16) - 1))) | (d_1_x1_)
        d_5_secondWord_ = (56320) | (d_0_x2_)
        return _dafny.Seq([d_4_firstWord_, d_5_secondWord_])

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequence(m):
        if (len(m)) == (1):
            return default__.DecodeMinimalWellFormedCodeUnitSubsequenceSingleWord(m)
        elif True:
            return default__.DecodeMinimalWellFormedCodeUnitSubsequenceDoubleWord(m)

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceSingleWord(m):
        d_0_firstWord_ = (m)[0]
        d_1_x_ = d_0_firstWord_
        return d_1_x_

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceDoubleWord(m):
        d_0_firstWord_ = (m)[0]
        d_1_secondWord_ = (m)[1]
        d_2_x2_ = (d_1_secondWord_) & (1023)
        d_3_x1_ = (d_0_firstWord_) & (63)
        d_4_w_ = ((d_0_firstWord_) & (960)) >> (6)
        d_5_u_ = ((d_4_w_) + (1)) & ((1 << 24) - 1)
        d_6_v_ = ((((d_5_u_) << (16)) & ((1 << 24) - 1)) | (((d_3_x1_) << (10)) & ((1 << 24) - 1))) | (d_2_x2_)
        return d_6_v_

    @staticmethod
    def PartitionCodeUnitSequenceChecked(s):
        maybeParts: Wrappers.Option = Wrappers.Option.default()()
        if (s) == (_dafny.Seq([])):
            maybeParts = Wrappers.Option_Some(_dafny.Seq([]))
            return maybeParts
        d_0_result_: _dafny.Seq
        d_0_result_ = _dafny.Seq([])
        d_1_rest_: _dafny.Seq
        d_1_rest_ = s
        while (len(d_1_rest_)) > (0):
            d_2_valueOrError0_: Wrappers.Option = Wrappers.Option.default()()
            d_2_valueOrError0_ = default__.SplitPrefixMinimalWellFormedCodeUnitSubsequence(d_1_rest_)
            if (d_2_valueOrError0_).IsFailure():
                maybeParts = (d_2_valueOrError0_).PropagateFailure()
                return maybeParts
            d_3_prefix_: _dafny.Seq
            d_3_prefix_ = (d_2_valueOrError0_).Extract()
            d_0_result_ = (d_0_result_) + (_dafny.Seq([d_3_prefix_]))
            d_1_rest_ = _dafny.Seq((d_1_rest_)[len(d_3_prefix_)::])
        maybeParts = Wrappers.Option_Some(d_0_result_)
        return maybeParts
        return maybeParts

    @staticmethod
    def PartitionCodeUnitSequence(s):
        return (default__.PartitionCodeUnitSequenceChecked(s)).Extract()

    @staticmethod
    def IsWellFormedCodeUnitSequence(s):
        return (default__.PartitionCodeUnitSequenceChecked(s)).is_Some

    @staticmethod
    def EncodeScalarSequence(vs):
        s: _dafny.Seq = WellFormedCodeUnitSeq.default()
        s = _dafny.Seq([])
        lo0_ = 0
        for d_0_i_ in range(len(vs)-1, lo0_-1, -1):
            d_1_next_: _dafny.Seq
            d_1_next_ = default__.EncodeScalarValue((vs)[d_0_i_])
            s = (d_1_next_) + (s)
        return s

    @staticmethod
    def DecodeCodeUnitSequence(s):
        d_0_parts_ = default__.PartitionCodeUnitSequence(s)
        d_1_vs_ = Seq.default__.Map(default__.DecodeMinimalWellFormedCodeUnitSubsequence, d_0_parts_)
        return d_1_vs_

    @staticmethod
    def DecodeCodeUnitSequenceChecked(s):
        maybeVs: Wrappers.Option = Wrappers.Option.default()()
        d_0_maybeParts_: Wrappers.Option
        d_0_maybeParts_ = default__.PartitionCodeUnitSequenceChecked(s)
        if (d_0_maybeParts_).is_None:
            maybeVs = Wrappers.Option_None()
            return maybeVs
        d_1_parts_: _dafny.Seq
        d_1_parts_ = (d_0_maybeParts_).value
        d_2_vs_: _dafny.Seq
        d_2_vs_ = Seq.default__.Map(default__.DecodeMinimalWellFormedCodeUnitSubsequence, d_1_parts_)
        maybeVs = Wrappers.Option_Some(d_2_vs_)
        return maybeVs
        return maybeVs


class WellFormedCodeUnitSeq:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq([])
    def _Is(source__):
        d_3_s_: _dafny.Seq = source__
        return default__.IsWellFormedCodeUnitSequence(d_3_s_)

class MinimalWellFormedCodeUnitSeq:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_4_s_: _dafny.Seq = source__
        return default__.IsMinimalWellFormedCodeUnitSubsequence(d_4_s_)
