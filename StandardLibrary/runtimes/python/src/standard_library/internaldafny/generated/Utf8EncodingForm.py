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

# Module: Utf8EncodingForm

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsMinimalWellFormedCodeUnitSubsequence(s):
        if (len(s)) == (1):
            d_56_b_ = default__.IsWellFormedSingleCodeUnitSequence(s)
            return d_56_b_
        elif (len(s)) == (2):
            d_57_b_ = default__.IsWellFormedDoubleCodeUnitSequence(s)
            return d_57_b_
        elif (len(s)) == (3):
            d_58_b_ = default__.IsWellFormedTripleCodeUnitSequence(s)
            return d_58_b_
        elif (len(s)) == (4):
            d_59_b_ = default__.IsWellFormedQuadrupleCodeUnitSequence(s)
            return d_59_b_
        elif True:
            return False

    @staticmethod
    def IsWellFormedSingleCodeUnitSequence(s):
        d_60_firstByte_ = (s)[0]
        return (True) and (((0) <= (d_60_firstByte_)) and ((d_60_firstByte_) <= (127)))

    @staticmethod
    def IsWellFormedDoubleCodeUnitSequence(s):
        d_61_firstByte_ = (s)[0]
        d_62_secondByte_ = (s)[1]
        return (((194) <= (d_61_firstByte_)) and ((d_61_firstByte_) <= (223))) and (((128) <= (d_62_secondByte_)) and ((d_62_secondByte_) <= (191)))

    @staticmethod
    def IsWellFormedTripleCodeUnitSequence(s):
        d_63_firstByte_ = (s)[0]
        d_64_secondByte_ = (s)[1]
        d_65_thirdByte_ = (s)[2]
        return ((((((d_63_firstByte_) == (224)) and (((160) <= (d_64_secondByte_)) and ((d_64_secondByte_) <= (191)))) or ((((225) <= (d_63_firstByte_)) and ((d_63_firstByte_) <= (236))) and (((128) <= (d_64_secondByte_)) and ((d_64_secondByte_) <= (191))))) or (((d_63_firstByte_) == (237)) and (((128) <= (d_64_secondByte_)) and ((d_64_secondByte_) <= (159))))) or ((((238) <= (d_63_firstByte_)) and ((d_63_firstByte_) <= (239))) and (((128) <= (d_64_secondByte_)) and ((d_64_secondByte_) <= (191))))) and (((128) <= (d_65_thirdByte_)) and ((d_65_thirdByte_) <= (191)))

    @staticmethod
    def IsWellFormedQuadrupleCodeUnitSequence(s):
        d_66_firstByte_ = (s)[0]
        d_67_secondByte_ = (s)[1]
        d_68_thirdByte_ = (s)[2]
        d_69_fourthByte_ = (s)[3]
        return ((((((d_66_firstByte_) == (240)) and (((144) <= (d_67_secondByte_)) and ((d_67_secondByte_) <= (191)))) or ((((241) <= (d_66_firstByte_)) and ((d_66_firstByte_) <= (243))) and (((128) <= (d_67_secondByte_)) and ((d_67_secondByte_) <= (191))))) or (((d_66_firstByte_) == (244)) and (((128) <= (d_67_secondByte_)) and ((d_67_secondByte_) <= (143))))) and (((128) <= (d_68_thirdByte_)) and ((d_68_thirdByte_) <= (191)))) and (((128) <= (d_69_fourthByte_)) and ((d_69_fourthByte_) <= (191)))

    @staticmethod
    def SplitPrefixMinimalWellFormedCodeUnitSubsequence(s):
        if ((len(s)) >= (1)) and (default__.IsWellFormedSingleCodeUnitSequence(_dafny.Seq((s)[:1:]))):
            return Wrappers.Option_Some(_dafny.Seq((s)[:1:]))
        elif ((len(s)) >= (2)) and (default__.IsWellFormedDoubleCodeUnitSequence(_dafny.Seq((s)[:2:]))):
            return Wrappers.Option_Some(_dafny.Seq((s)[:2:]))
        elif ((len(s)) >= (3)) and (default__.IsWellFormedTripleCodeUnitSequence(_dafny.Seq((s)[:3:]))):
            return Wrappers.Option_Some(_dafny.Seq((s)[:3:]))
        elif ((len(s)) >= (4)) and (default__.IsWellFormedQuadrupleCodeUnitSequence(_dafny.Seq((s)[:4:]))):
            return Wrappers.Option_Some(_dafny.Seq((s)[:4:]))
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def EncodeScalarValue(v):
        if (v) <= (127):
            return default__.EncodeScalarValueSingleByte(v)
        elif (v) <= (2047):
            return default__.EncodeScalarValueDoubleByte(v)
        elif (v) <= (65535):
            return default__.EncodeScalarValueTripleByte(v)
        elif True:
            return default__.EncodeScalarValueQuadrupleByte(v)

    @staticmethod
    def EncodeScalarValueSingleByte(v):
        d_70_x_ = (v) & (127)
        d_71_firstByte_ = d_70_x_
        return _dafny.Seq([d_71_firstByte_])

    @staticmethod
    def EncodeScalarValueDoubleByte(v):
        d_72_x_ = (v) & (63)
        d_73_y_ = ((v) & (1984)) >> (6)
        d_74_firstByte_ = (192) | (d_73_y_)
        d_75_secondByte_ = (128) | (d_72_x_)
        return _dafny.Seq([d_74_firstByte_, d_75_secondByte_])

    @staticmethod
    def EncodeScalarValueTripleByte(v):
        d_76_x_ = (v) & (63)
        d_77_y_ = ((v) & (4032)) >> (6)
        d_78_z_ = ((v) & (61440)) >> (12)
        d_79_firstByte_ = (224) | (d_78_z_)
        d_80_secondByte_ = (128) | (d_77_y_)
        d_81_thirdByte_ = (128) | (d_76_x_)
        return _dafny.Seq([d_79_firstByte_, d_80_secondByte_, d_81_thirdByte_])

    @staticmethod
    def EncodeScalarValueQuadrupleByte(v):
        d_82_x_ = (v) & (63)
        d_83_y_ = ((v) & (4032)) >> (6)
        d_84_z_ = ((v) & (61440)) >> (12)
        d_85_u2_ = ((v) & (196608)) >> (16)
        d_86_u1_ = ((v) & (1835008)) >> (18)
        d_87_firstByte_ = (240) | (d_86_u1_)
        d_88_secondByte_ = ((128) | (((d_85_u2_) << (4)) & ((1 << 8) - 1))) | (d_84_z_)
        d_89_thirdByte_ = (128) | (d_83_y_)
        d_90_fourthByte_ = (128) | (d_82_x_)
        return _dafny.Seq([d_87_firstByte_, d_88_secondByte_, d_89_thirdByte_, d_90_fourthByte_])

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequence(m):
        if (len(m)) == (1):
            return default__.DecodeMinimalWellFormedCodeUnitSubsequenceSingleByte(m)
        elif (len(m)) == (2):
            return default__.DecodeMinimalWellFormedCodeUnitSubsequenceDoubleByte(m)
        elif (len(m)) == (3):
            return default__.DecodeMinimalWellFormedCodeUnitSubsequenceTripleByte(m)
        elif True:
            return default__.DecodeMinimalWellFormedCodeUnitSubsequenceQuadrupleByte(m)

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceSingleByte(m):
        d_91_firstByte_ = (m)[0]
        d_92_x_ = d_91_firstByte_
        return d_92_x_

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceDoubleByte(m):
        d_93_firstByte_ = (m)[0]
        d_94_secondByte_ = (m)[1]
        d_95_y_ = (d_93_firstByte_) & (31)
        d_96_x_ = (d_94_secondByte_) & (63)
        return (((d_95_y_) << (6)) & ((1 << 24) - 1)) | (d_96_x_)

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceTripleByte(m):
        d_97_firstByte_ = (m)[0]
        d_98_secondByte_ = (m)[1]
        d_99_thirdByte_ = (m)[2]
        d_100_z_ = (d_97_firstByte_) & (15)
        d_101_y_ = (d_98_secondByte_) & (63)
        d_102_x_ = (d_99_thirdByte_) & (63)
        return ((((d_100_z_) << (12)) & ((1 << 24) - 1)) | (((d_101_y_) << (6)) & ((1 << 24) - 1))) | (d_102_x_)

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceQuadrupleByte(m):
        d_103_firstByte_ = (m)[0]
        d_104_secondByte_ = (m)[1]
        d_105_thirdByte_ = (m)[2]
        d_106_fourthByte_ = (m)[3]
        d_107_u1_ = (d_103_firstByte_) & (7)
        d_108_u2_ = ((d_104_secondByte_) & (48)) >> (4)
        d_109_z_ = (d_104_secondByte_) & (15)
        d_110_y_ = (d_105_thirdByte_) & (63)
        d_111_x_ = (d_106_fourthByte_) & (63)
        return ((((((d_107_u1_) << (18)) & ((1 << 24) - 1)) | (((d_108_u2_) << (16)) & ((1 << 24) - 1))) | (((d_109_z_) << (12)) & ((1 << 24) - 1))) | (((d_110_y_) << (6)) & ((1 << 24) - 1))) | (d_111_x_)

    @staticmethod
    def PartitionCodeUnitSequenceChecked(s):
        maybeParts: Wrappers.Option = Wrappers.Option.default()()
        if (s) == (_dafny.Seq([])):
            maybeParts = Wrappers.Option_Some(_dafny.Seq([]))
            return maybeParts
        d_112_result_: _dafny.Seq
        d_112_result_ = _dafny.Seq([])
        d_113_rest_: _dafny.Seq
        d_113_rest_ = s
        while (len(d_113_rest_)) > (0):
            d_114_prefix_: _dafny.Seq
            d_115_valueOrError0_: Wrappers.Option = Wrappers.Option.default()()
            d_115_valueOrError0_ = default__.SplitPrefixMinimalWellFormedCodeUnitSubsequence(d_113_rest_)
            if (d_115_valueOrError0_).IsFailure():
                maybeParts = (d_115_valueOrError0_).PropagateFailure()
                return maybeParts
            d_114_prefix_ = (d_115_valueOrError0_).Extract()
            d_112_result_ = (d_112_result_) + (_dafny.Seq([d_114_prefix_]))
            d_113_rest_ = _dafny.Seq((d_113_rest_)[len(d_114_prefix_)::])
        maybeParts = Wrappers.Option_Some(d_112_result_)
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
        lo1_ = 0
        for d_116_i_ in range(len(vs)-1, lo1_-1, -1):
            d_117_next_: _dafny.Seq
            d_117_next_ = default__.EncodeScalarValue((vs)[d_116_i_])
            s = (d_117_next_) + (s)
        return s

    @staticmethod
    def DecodeCodeUnitSequence(s):
        d_118_parts_ = default__.PartitionCodeUnitSequence(s)
        d_119_vs_ = Seq.default__.Map(default__.DecodeMinimalWellFormedCodeUnitSubsequence, d_118_parts_)
        return d_119_vs_

    @staticmethod
    def DecodeCodeUnitSequenceChecked(s):
        maybeVs: Wrappers.Option = Wrappers.Option.default()()
        d_120_maybeParts_: Wrappers.Option
        d_120_maybeParts_ = default__.PartitionCodeUnitSequenceChecked(s)
        if (d_120_maybeParts_).is_None:
            maybeVs = Wrappers.Option_None()
            return maybeVs
        d_121_parts_: _dafny.Seq
        d_121_parts_ = (d_120_maybeParts_).value
        d_122_vs_: _dafny.Seq
        d_122_vs_ = Seq.default__.Map(default__.DecodeMinimalWellFormedCodeUnitSubsequence, d_121_parts_)
        maybeVs = Wrappers.Option_Some(d_122_vs_)
        return maybeVs
        return maybeVs


class WellFormedCodeUnitSeq:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq([])
    def _Is(source__):
        d_123_s_: _dafny.Seq = source__
        return default__.IsWellFormedCodeUnitSequence(d_123_s_)

class MinimalWellFormedCodeUnitSeq:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_124_s_: _dafny.Seq = source__
        return default__.IsMinimalWellFormedCodeUnitSubsequence(d_124_s_)
