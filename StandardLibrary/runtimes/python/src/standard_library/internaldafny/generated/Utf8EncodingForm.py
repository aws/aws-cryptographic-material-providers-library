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
            d_47_b_ = default__.IsWellFormedSingleCodeUnitSequence(s)
            return d_47_b_
        elif (len(s)) == (2):
            d_48_b_ = default__.IsWellFormedDoubleCodeUnitSequence(s)
            return d_48_b_
        elif (len(s)) == (3):
            d_49_b_ = default__.IsWellFormedTripleCodeUnitSequence(s)
            return d_49_b_
        elif (len(s)) == (4):
            d_50_b_ = default__.IsWellFormedQuadrupleCodeUnitSequence(s)
            return d_50_b_
        elif True:
            return False

    @staticmethod
    def IsWellFormedSingleCodeUnitSequence(s):
        d_51_firstByte_ = (s)[0]
        return (True) and (((0) <= (d_51_firstByte_)) and ((d_51_firstByte_) <= (127)))

    @staticmethod
    def IsWellFormedDoubleCodeUnitSequence(s):
        d_52_firstByte_ = (s)[0]
        d_53_secondByte_ = (s)[1]
        return (((194) <= (d_52_firstByte_)) and ((d_52_firstByte_) <= (223))) and (((128) <= (d_53_secondByte_)) and ((d_53_secondByte_) <= (191)))

    @staticmethod
    def IsWellFormedTripleCodeUnitSequence(s):
        d_54_firstByte_ = (s)[0]
        d_55_secondByte_ = (s)[1]
        d_56_thirdByte_ = (s)[2]
        return ((((((d_54_firstByte_) == (224)) and (((160) <= (d_55_secondByte_)) and ((d_55_secondByte_) <= (191)))) or ((((225) <= (d_54_firstByte_)) and ((d_54_firstByte_) <= (236))) and (((128) <= (d_55_secondByte_)) and ((d_55_secondByte_) <= (191))))) or (((d_54_firstByte_) == (237)) and (((128) <= (d_55_secondByte_)) and ((d_55_secondByte_) <= (159))))) or ((((238) <= (d_54_firstByte_)) and ((d_54_firstByte_) <= (239))) and (((128) <= (d_55_secondByte_)) and ((d_55_secondByte_) <= (191))))) and (((128) <= (d_56_thirdByte_)) and ((d_56_thirdByte_) <= (191)))

    @staticmethod
    def IsWellFormedQuadrupleCodeUnitSequence(s):
        d_57_firstByte_ = (s)[0]
        d_58_secondByte_ = (s)[1]
        d_59_thirdByte_ = (s)[2]
        d_60_fourthByte_ = (s)[3]
        return ((((((d_57_firstByte_) == (240)) and (((144) <= (d_58_secondByte_)) and ((d_58_secondByte_) <= (191)))) or ((((241) <= (d_57_firstByte_)) and ((d_57_firstByte_) <= (243))) and (((128) <= (d_58_secondByte_)) and ((d_58_secondByte_) <= (191))))) or (((d_57_firstByte_) == (244)) and (((128) <= (d_58_secondByte_)) and ((d_58_secondByte_) <= (143))))) and (((128) <= (d_59_thirdByte_)) and ((d_59_thirdByte_) <= (191)))) and (((128) <= (d_60_fourthByte_)) and ((d_60_fourthByte_) <= (191)))

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
        d_61_x_ = (v) & (127)
        d_62_firstByte_ = d_61_x_
        return _dafny.Seq([d_62_firstByte_])

    @staticmethod
    def EncodeScalarValueDoubleByte(v):
        d_63_x_ = (v) & (63)
        d_64_y_ = ((v) & (1984)) >> (6)
        d_65_firstByte_ = (192) | (d_64_y_)
        d_66_secondByte_ = (128) | (d_63_x_)
        return _dafny.Seq([d_65_firstByte_, d_66_secondByte_])

    @staticmethod
    def EncodeScalarValueTripleByte(v):
        d_67_x_ = (v) & (63)
        d_68_y_ = ((v) & (4032)) >> (6)
        d_69_z_ = ((v) & (61440)) >> (12)
        d_70_firstByte_ = (224) | (d_69_z_)
        d_71_secondByte_ = (128) | (d_68_y_)
        d_72_thirdByte_ = (128) | (d_67_x_)
        return _dafny.Seq([d_70_firstByte_, d_71_secondByte_, d_72_thirdByte_])

    @staticmethod
    def EncodeScalarValueQuadrupleByte(v):
        d_73_x_ = (v) & (63)
        d_74_y_ = ((v) & (4032)) >> (6)
        d_75_z_ = ((v) & (61440)) >> (12)
        d_76_u2_ = ((v) & (196608)) >> (16)
        d_77_u1_ = ((v) & (1835008)) >> (18)
        d_78_firstByte_ = (240) | (d_77_u1_)
        d_79_secondByte_ = ((128) | (((d_76_u2_) << (4)) & ((1 << 8) - 1))) | (d_75_z_)
        d_80_thirdByte_ = (128) | (d_74_y_)
        d_81_fourthByte_ = (128) | (d_73_x_)
        return _dafny.Seq([d_78_firstByte_, d_79_secondByte_, d_80_thirdByte_, d_81_fourthByte_])

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
        d_82_firstByte_ = (m)[0]
        d_83_x_ = d_82_firstByte_
        return d_83_x_

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceDoubleByte(m):
        d_84_firstByte_ = (m)[0]
        d_85_secondByte_ = (m)[1]
        d_86_y_ = (d_84_firstByte_) & (31)
        d_87_x_ = (d_85_secondByte_) & (63)
        return (((d_86_y_) << (6)) & ((1 << 24) - 1)) | (d_87_x_)

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceTripleByte(m):
        d_88_firstByte_ = (m)[0]
        d_89_secondByte_ = (m)[1]
        d_90_thirdByte_ = (m)[2]
        d_91_z_ = (d_88_firstByte_) & (15)
        d_92_y_ = (d_89_secondByte_) & (63)
        d_93_x_ = (d_90_thirdByte_) & (63)
        return ((((d_91_z_) << (12)) & ((1 << 24) - 1)) | (((d_92_y_) << (6)) & ((1 << 24) - 1))) | (d_93_x_)

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceQuadrupleByte(m):
        d_94_firstByte_ = (m)[0]
        d_95_secondByte_ = (m)[1]
        d_96_thirdByte_ = (m)[2]
        d_97_fourthByte_ = (m)[3]
        d_98_u1_ = (d_94_firstByte_) & (7)
        d_99_u2_ = ((d_95_secondByte_) & (48)) >> (4)
        d_100_z_ = (d_95_secondByte_) & (15)
        d_101_y_ = (d_96_thirdByte_) & (63)
        d_102_x_ = (d_97_fourthByte_) & (63)
        return ((((((d_98_u1_) << (18)) & ((1 << 24) - 1)) | (((d_99_u2_) << (16)) & ((1 << 24) - 1))) | (((d_100_z_) << (12)) & ((1 << 24) - 1))) | (((d_101_y_) << (6)) & ((1 << 24) - 1))) | (d_102_x_)

    @staticmethod
    def PartitionCodeUnitSequenceChecked(s):
        maybeParts: Wrappers.Option = Wrappers.Option.default()()
        if (s) == (_dafny.Seq([])):
            maybeParts = Wrappers.Option_Some(_dafny.Seq([]))
            return maybeParts
        d_103_result_: _dafny.Seq
        d_103_result_ = _dafny.Seq([])
        d_104_rest_: _dafny.Seq
        d_104_rest_ = s
        while (len(d_104_rest_)) > (0):
            d_105_valueOrError0_: Wrappers.Option = Wrappers.Option.default()()
            d_105_valueOrError0_ = default__.SplitPrefixMinimalWellFormedCodeUnitSubsequence(d_104_rest_)
            if (d_105_valueOrError0_).IsFailure():
                maybeParts = (d_105_valueOrError0_).PropagateFailure()
                return maybeParts
            d_106_prefix_: _dafny.Seq
            d_106_prefix_ = (d_105_valueOrError0_).Extract()
            d_103_result_ = (d_103_result_) + (_dafny.Seq([d_106_prefix_]))
            d_104_rest_ = _dafny.Seq((d_104_rest_)[len(d_106_prefix_)::])
        maybeParts = Wrappers.Option_Some(d_103_result_)
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
        for d_107_i_ in range(len(vs)-1, lo1_-1, -1):
            d_108_next_: _dafny.Seq
            d_108_next_ = default__.EncodeScalarValue((vs)[d_107_i_])
            s = (d_108_next_) + (s)
        return s

    @staticmethod
    def DecodeCodeUnitSequence(s):
        d_109_parts_ = default__.PartitionCodeUnitSequence(s)
        d_110_vs_ = Seq.default__.Map(default__.DecodeMinimalWellFormedCodeUnitSubsequence, d_109_parts_)
        return d_110_vs_

    @staticmethod
    def DecodeCodeUnitSequenceChecked(s):
        maybeVs: Wrappers.Option = Wrappers.Option.default()()
        d_111_maybeParts_: Wrappers.Option
        d_111_maybeParts_ = default__.PartitionCodeUnitSequenceChecked(s)
        if (d_111_maybeParts_).is_None:
            maybeVs = Wrappers.Option_None()
            return maybeVs
        d_112_parts_: _dafny.Seq
        d_112_parts_ = (d_111_maybeParts_).value
        d_113_vs_: _dafny.Seq
        d_113_vs_ = Seq.default__.Map(default__.DecodeMinimalWellFormedCodeUnitSubsequence, d_112_parts_)
        maybeVs = Wrappers.Option_Some(d_113_vs_)
        return maybeVs
        return maybeVs


class WellFormedCodeUnitSeq:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq([])
    def _Is(source__):
        d_114_s_: _dafny.Seq = source__
        return default__.IsWellFormedCodeUnitSequence(d_114_s_)

class MinimalWellFormedCodeUnitSeq:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_115_s_: _dafny.Seq = source__
        return default__.IsMinimalWellFormedCodeUnitSubsequence(d_115_s_)
