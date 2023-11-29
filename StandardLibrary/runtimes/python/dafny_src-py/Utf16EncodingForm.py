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

# Module: Utf16EncodingForm

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsMinimalWellFormedCodeUnitSubsequence(s):
        if (len(s)) == (1):
            return default__.IsWellFormedSingleCodeUnitSequence(s)
        elif (len(s)) == (2):
            d_114_b_ = default__.IsWellFormedDoubleCodeUnitSequence(s)
            return d_114_b_
        elif True:
            return False

    @staticmethod
    def IsWellFormedSingleCodeUnitSequence(s):
        d_115_firstWord_ = (s)[0]
        return (((0) <= (d_115_firstWord_)) and ((d_115_firstWord_) <= (55295))) or (((57344) <= (d_115_firstWord_)) and ((d_115_firstWord_) <= (65535)))

    @staticmethod
    def IsWellFormedDoubleCodeUnitSequence(s):
        d_116_firstWord_ = (s)[0]
        d_117_secondWord_ = (s)[1]
        return (((55296) <= (d_116_firstWord_)) and ((d_116_firstWord_) <= (56319))) and (((56320) <= (d_117_secondWord_)) and ((d_117_secondWord_) <= (57343)))

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
        d_118_firstWord_ = v
        return _dafny.Seq([d_118_firstWord_])

    @staticmethod
    def EncodeScalarValueDoubleWord(v):
        d_119_x2_ = (v) & (1023)
        d_120_x1_ = ((v) & (64512)) >> (10)
        d_121_u_ = ((v) & (2031616)) >> (16)
        d_122_w_ = ((d_121_u_) - (1)) & ((1 << 5) - 1)
        d_123_firstWord_ = ((55296) | (((d_122_w_) << (6)) & ((1 << 16) - 1))) | (d_120_x1_)
        d_124_secondWord_ = (56320) | (d_119_x2_)
        return _dafny.Seq([d_123_firstWord_, d_124_secondWord_])

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequence(m):
        if (len(m)) == (1):
            return default__.DecodeMinimalWellFormedCodeUnitSubsequenceSingleWord(m)
        elif True:
            return default__.DecodeMinimalWellFormedCodeUnitSubsequenceDoubleWord(m)

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceSingleWord(m):
        d_125_firstWord_ = (m)[0]
        d_126_x_ = d_125_firstWord_
        return d_126_x_

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceDoubleWord(m):
        d_127_firstWord_ = (m)[0]
        d_128_secondWord_ = (m)[1]
        d_129_x2_ = (d_128_secondWord_) & (1023)
        d_130_x1_ = (d_127_firstWord_) & (63)
        d_131_w_ = ((d_127_firstWord_) & (960)) >> (6)
        d_132_u_ = ((d_131_w_) + (1)) & ((1 << 24) - 1)
        d_133_v_ = ((((d_132_u_) << (16)) & ((1 << 24) - 1)) | (((d_130_x1_) << (10)) & ((1 << 24) - 1))) | (d_129_x2_)
        return d_133_v_

    @staticmethod
    def PartitionCodeUnitSequenceChecked(s):
        maybeParts: Wrappers.Option = Wrappers.Option.default()()
        if (s) == (_dafny.Seq([])):
            maybeParts = Wrappers.Option_Some(_dafny.Seq([]))
            return maybeParts
        d_134_result_: _dafny.Seq
        d_134_result_ = _dafny.Seq([])
        d_135_rest_: _dafny.Seq
        d_135_rest_ = s
        while (len(d_135_rest_)) > (0):
            d_136_prefix_: _dafny.Seq
            d_137_valueOrError0_: Wrappers.Option = Wrappers.Option.default()()
            d_137_valueOrError0_ = default__.SplitPrefixMinimalWellFormedCodeUnitSubsequence(d_135_rest_)
            if (d_137_valueOrError0_).IsFailure():
                maybeParts = (d_137_valueOrError0_).PropagateFailure()
                return maybeParts
            d_136_prefix_ = (d_137_valueOrError0_).Extract()
            d_134_result_ = (d_134_result_) + (_dafny.Seq([d_136_prefix_]))
            d_135_rest_ = _dafny.Seq((d_135_rest_)[len(d_136_prefix_)::])
        maybeParts = Wrappers.Option_Some(d_134_result_)
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
        lo2_ = 0
        for d_138_i_ in range(len(vs)-1, lo2_-1, -1):
            d_139_next_: _dafny.Seq
            d_139_next_ = default__.EncodeScalarValue((vs)[d_138_i_])
            s = (d_139_next_) + (s)
        return s

    @staticmethod
    def DecodeCodeUnitSequence(s):
        d_140_parts_ = default__.PartitionCodeUnitSequence(s)
        d_141_vs_ = Seq.default__.Map(default__.DecodeMinimalWellFormedCodeUnitSubsequence, d_140_parts_)
        return d_141_vs_

    @staticmethod
    def DecodeCodeUnitSequenceChecked(s):
        maybeVs: Wrappers.Option = Wrappers.Option.default()()
        d_142_maybeParts_: Wrappers.Option
        d_142_maybeParts_ = default__.PartitionCodeUnitSequenceChecked(s)
        if (d_142_maybeParts_).is_None:
            maybeVs = Wrappers.Option_None()
            return maybeVs
        d_143_parts_: _dafny.Seq
        d_143_parts_ = (d_142_maybeParts_).value
        d_144_vs_: _dafny.Seq
        d_144_vs_ = Seq.default__.Map(default__.DecodeMinimalWellFormedCodeUnitSubsequence, d_143_parts_)
        maybeVs = Wrappers.Option_Some(d_144_vs_)
        return maybeVs
        return maybeVs


class WellFormedCodeUnitSeq:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq([])

class MinimalWellFormedCodeUnitSeq:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
