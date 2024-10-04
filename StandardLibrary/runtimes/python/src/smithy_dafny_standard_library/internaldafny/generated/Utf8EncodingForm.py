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

# Module: Utf8EncodingForm

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsMinimalWellFormedCodeUnitSubsequence(s):
        if (len(s)) == (1):
            d_0_b_ = default__.IsWellFormedSingleCodeUnitSequence(s)
            return d_0_b_
        elif (len(s)) == (2):
            d_1_b_ = default__.IsWellFormedDoubleCodeUnitSequence(s)
            return d_1_b_
        elif (len(s)) == (3):
            d_2_b_ = default__.IsWellFormedTripleCodeUnitSequence(s)
            return d_2_b_
        elif (len(s)) == (4):
            d_3_b_ = default__.IsWellFormedQuadrupleCodeUnitSequence(s)
            return d_3_b_
        elif True:
            return False

    @staticmethod
    def IsWellFormedSingleCodeUnitSequence(s):
        d_0_firstByte_ = (s)[0]
        return (True) and (((0) <= (d_0_firstByte_)) and ((d_0_firstByte_) <= (127)))

    @staticmethod
    def IsWellFormedDoubleCodeUnitSequence(s):
        d_0_firstByte_ = (s)[0]
        d_1_secondByte_ = (s)[1]
        return (((194) <= (d_0_firstByte_)) and ((d_0_firstByte_) <= (223))) and (((128) <= (d_1_secondByte_)) and ((d_1_secondByte_) <= (191)))

    @staticmethod
    def IsWellFormedTripleCodeUnitSequence(s):
        d_0_firstByte_ = (s)[0]
        d_1_secondByte_ = (s)[1]
        d_2_thirdByte_ = (s)[2]
        return ((((((d_0_firstByte_) == (224)) and (((160) <= (d_1_secondByte_)) and ((d_1_secondByte_) <= (191)))) or ((((225) <= (d_0_firstByte_)) and ((d_0_firstByte_) <= (236))) and (((128) <= (d_1_secondByte_)) and ((d_1_secondByte_) <= (191))))) or (((d_0_firstByte_) == (237)) and (((128) <= (d_1_secondByte_)) and ((d_1_secondByte_) <= (159))))) or ((((238) <= (d_0_firstByte_)) and ((d_0_firstByte_) <= (239))) and (((128) <= (d_1_secondByte_)) and ((d_1_secondByte_) <= (191))))) and (((128) <= (d_2_thirdByte_)) and ((d_2_thirdByte_) <= (191)))

    @staticmethod
    def IsWellFormedQuadrupleCodeUnitSequence(s):
        d_0_firstByte_ = (s)[0]
        d_1_secondByte_ = (s)[1]
        d_2_thirdByte_ = (s)[2]
        d_3_fourthByte_ = (s)[3]
        return ((((((d_0_firstByte_) == (240)) and (((144) <= (d_1_secondByte_)) and ((d_1_secondByte_) <= (191)))) or ((((241) <= (d_0_firstByte_)) and ((d_0_firstByte_) <= (243))) and (((128) <= (d_1_secondByte_)) and ((d_1_secondByte_) <= (191))))) or (((d_0_firstByte_) == (244)) and (((128) <= (d_1_secondByte_)) and ((d_1_secondByte_) <= (143))))) and (((128) <= (d_2_thirdByte_)) and ((d_2_thirdByte_) <= (191)))) and (((128) <= (d_3_fourthByte_)) and ((d_3_fourthByte_) <= (191)))

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
        d_0_x_ = (v) & (127)
        d_1_firstByte_ = d_0_x_
        return _dafny.Seq([d_1_firstByte_])

    @staticmethod
    def EncodeScalarValueDoubleByte(v):
        d_0_x_ = (v) & (63)
        d_1_y_ = ((v) & (1984)) >> (6)
        d_2_firstByte_ = (192) | (d_1_y_)
        d_3_secondByte_ = (128) | (d_0_x_)
        return _dafny.Seq([d_2_firstByte_, d_3_secondByte_])

    @staticmethod
    def EncodeScalarValueTripleByte(v):
        d_0_x_ = (v) & (63)
        d_1_y_ = ((v) & (4032)) >> (6)
        d_2_z_ = ((v) & (61440)) >> (12)
        d_3_firstByte_ = (224) | (d_2_z_)
        d_4_secondByte_ = (128) | (d_1_y_)
        d_5_thirdByte_ = (128) | (d_0_x_)
        return _dafny.Seq([d_3_firstByte_, d_4_secondByte_, d_5_thirdByte_])

    @staticmethod
    def EncodeScalarValueQuadrupleByte(v):
        d_0_x_ = (v) & (63)
        d_1_y_ = ((v) & (4032)) >> (6)
        d_2_z_ = ((v) & (61440)) >> (12)
        d_3_u2_ = ((v) & (196608)) >> (16)
        d_4_u1_ = ((v) & (1835008)) >> (18)
        d_5_firstByte_ = (240) | (d_4_u1_)
        d_6_secondByte_ = ((128) | (((d_3_u2_) << (4)) & ((1 << 8) - 1))) | (d_2_z_)
        d_7_thirdByte_ = (128) | (d_1_y_)
        d_8_fourthByte_ = (128) | (d_0_x_)
        return _dafny.Seq([d_5_firstByte_, d_6_secondByte_, d_7_thirdByte_, d_8_fourthByte_])

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
        d_0_firstByte_ = (m)[0]
        d_1_x_ = d_0_firstByte_
        return d_1_x_

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceDoubleByte(m):
        d_0_firstByte_ = (m)[0]
        d_1_secondByte_ = (m)[1]
        d_2_y_ = (d_0_firstByte_) & (31)
        d_3_x_ = (d_1_secondByte_) & (63)
        return (((d_2_y_) << (6)) & ((1 << 24) - 1)) | (d_3_x_)

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceTripleByte(m):
        d_0_firstByte_ = (m)[0]
        d_1_secondByte_ = (m)[1]
        d_2_thirdByte_ = (m)[2]
        d_3_z_ = (d_0_firstByte_) & (15)
        d_4_y_ = (d_1_secondByte_) & (63)
        d_5_x_ = (d_2_thirdByte_) & (63)
        return ((((d_3_z_) << (12)) & ((1 << 24) - 1)) | (((d_4_y_) << (6)) & ((1 << 24) - 1))) | (d_5_x_)

    @staticmethod
    def DecodeMinimalWellFormedCodeUnitSubsequenceQuadrupleByte(m):
        d_0_firstByte_ = (m)[0]
        d_1_secondByte_ = (m)[1]
        d_2_thirdByte_ = (m)[2]
        d_3_fourthByte_ = (m)[3]
        d_4_u1_ = (d_0_firstByte_) & (7)
        d_5_u2_ = ((d_1_secondByte_) & (48)) >> (4)
        d_6_z_ = (d_1_secondByte_) & (15)
        d_7_y_ = (d_2_thirdByte_) & (63)
        d_8_x_ = (d_3_fourthByte_) & (63)
        return ((((((d_4_u1_) << (18)) & ((1 << 24) - 1)) | (((d_5_u2_) << (16)) & ((1 << 24) - 1))) | (((d_6_z_) << (12)) & ((1 << 24) - 1))) | (((d_7_y_) << (6)) & ((1 << 24) - 1))) | (d_8_x_)

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
