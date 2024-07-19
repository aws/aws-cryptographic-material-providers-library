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

# Module: Utf16EncodingForm

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsMinimalWellFormedCodeUnitSubsequence(s):
        if (len(s)) == (1):
            return default__.IsWellFormedSingleCodeUnitSequence(s)
        elif (len(s)) == (2):
            d_116_b_ = default__.IsWellFormedDoubleCodeUnitSequence(s)
            return d_116_b_
        elif True:
            return False

    @staticmethod
    def IsWellFormedSingleCodeUnitSequence(s):
        d_117_firstWord_ = (s)[0]
        return (((0) <= (d_117_firstWord_)) and ((d_117_firstWord_) <= (55295))) or (((57344) <= (d_117_firstWord_)) and ((d_117_firstWord_) <= (65535)))

    @staticmethod
    def IsWellFormedDoubleCodeUnitSequence(s):
        d_118_firstWord_ = (s)[0]
        d_119_secondWord_ = (s)[1]
        return (((55296) <= (d_118_firstWord_)) and ((d_118_firstWord_) <= (56319))) and (((56320) <= (d_119_secondWord_)) and ((d_119_secondWord_) <= (57343)))

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
        d_120_firstWord_ = v
        return _dafny.Seq([d_120_firstWord_])

    @staticmethod
    def EncodeScalarValueDoubleWord(v):
        d_121_x2_ = (v) & (1023)
        d_122_x1_ = ((v) & (64512)) >> (10)
        d_123_u_ = ((v) & (2031616)) >> (16)
        d_124_w_ = ((d_123_u_) - (1)) & ((1 << 5) - 1)
        d_125_firstWord_ = ((55296) | (((d_124_w_) << (6)) & ((1 << 16) - 1))) | (d_122_x1_)
        d_126_secondWord_ = (56320) | (d_121_x2_)
        return _dafny.Seq([d_125_firstWord_, d_126_secondWord_])

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequence(m):
        if (len(m)) == (1):
            return default__.DecodeMinimalWellFormedCodeUnitSubsequenceSingleWord(m)
        elif True:
            return default__.DecodeMinimalWellFormedCodeUnitSubsequenceDoubleWord(m)

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceSingleWord(m):
        d_127_firstWord_ = (m)[0]
        d_128_x_ = d_127_firstWord_
        return d_128_x_

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceDoubleWord(m):
        d_129_firstWord_ = (m)[0]
        d_130_secondWord_ = (m)[1]
        d_131_x2_ = (d_130_secondWord_) & (1023)
        d_132_x1_ = (d_129_firstWord_) & (63)
        d_133_w_ = ((d_129_firstWord_) & (960)) >> (6)
        d_134_u_ = ((d_133_w_) + (1)) & ((1 << 24) - 1)
        d_135_v_ = ((((d_134_u_) << (16)) & ((1 << 24) - 1)) | (((d_132_x1_) << (10)) & ((1 << 24) - 1))) | (d_131_x2_)
        return d_135_v_

    @staticmethod
    def PartitionCodeUnitSequenceChecked(s):
        maybeParts: Wrappers.Option = Wrappers.Option.default()()
        if (s) == (_dafny.Seq([])):
            maybeParts = Wrappers.Option_Some(_dafny.Seq([]))
            return maybeParts
        d_136_result_: _dafny.Seq
        d_136_result_ = _dafny.Seq([])
        d_137_rest_: _dafny.Seq
        d_137_rest_ = s
        while (len(d_137_rest_)) > (0):
            d_138_valueOrError0_: Wrappers.Option = Wrappers.Option.default()()
            d_138_valueOrError0_ = default__.SplitPrefixMinimalWellFormedCodeUnitSubsequence(d_137_rest_)
            if (d_138_valueOrError0_).IsFailure():
                maybeParts = (d_138_valueOrError0_).PropagateFailure()
                return maybeParts
            d_139_prefix_: _dafny.Seq
            d_139_prefix_ = (d_138_valueOrError0_).Extract()
            d_136_result_ = (d_136_result_) + (_dafny.Seq([d_139_prefix_]))
            d_137_rest_ = _dafny.Seq((d_137_rest_)[len(d_139_prefix_)::])
        maybeParts = Wrappers.Option_Some(d_136_result_)
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
        for d_140_i_ in range(len(vs)-1, lo2_-1, -1):
            d_141_next_: _dafny.Seq
            d_141_next_ = default__.EncodeScalarValue((vs)[d_140_i_])
            s = (d_141_next_) + (s)
        return s

    @staticmethod
    def DecodeCodeUnitSequence(s):
        d_142_parts_ = default__.PartitionCodeUnitSequence(s)
        d_143_vs_ = Seq.default__.Map(default__.DecodeMinimalWellFormedCodeUnitSubsequence, d_142_parts_)
        return d_143_vs_

    @staticmethod
    def DecodeCodeUnitSequenceChecked(s):
        maybeVs: Wrappers.Option = Wrappers.Option.default()()
        d_144_maybeParts_: Wrappers.Option
        d_144_maybeParts_ = default__.PartitionCodeUnitSequenceChecked(s)
        if (d_144_maybeParts_).is_None:
            maybeVs = Wrappers.Option_None()
            return maybeVs
        d_145_parts_: _dafny.Seq
        d_145_parts_ = (d_144_maybeParts_).value
        d_146_vs_: _dafny.Seq
        d_146_vs_ = Seq.default__.Map(default__.DecodeMinimalWellFormedCodeUnitSubsequence, d_145_parts_)
        maybeVs = Wrappers.Option_Some(d_146_vs_)
        return maybeVs
        return maybeVs


class WellFormedCodeUnitSeq:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq([])
    def _Is(source__):
        d_147_s_: _dafny.Seq = source__
        return default__.IsWellFormedCodeUnitSequence(d_147_s_)

class MinimalWellFormedCodeUnitSeq:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_148_s_: _dafny.Seq = source__
        return default__.IsMinimalWellFormedCodeUnitSubsequence(d_148_s_)
