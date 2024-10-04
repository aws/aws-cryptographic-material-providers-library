import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import smithy_dafny_standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations

# Module: Seq_MergeSort

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def MergeSortBy(a, lessThanOrEq):
        if (len(a)) <= (1):
            return a
        elif True:
            d_0_splitIndex_ = _dafny.euclidian_division(len(a), 2)
            d_1_left_ = _dafny.Seq((a)[:d_0_splitIndex_:])
            d_2_right_ = _dafny.Seq((a)[d_0_splitIndex_::])
            d_3_leftSorted_ = default__.MergeSortBy(d_1_left_, lessThanOrEq)
            d_4_rightSorted_ = default__.MergeSortBy(d_2_right_, lessThanOrEq)
            return default__.MergeSortedWith(d_3_leftSorted_, d_4_rightSorted_, lessThanOrEq)

    @staticmethod
    def MergeSortedWith(left, right, lessThanOrEq):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(left)) == (0):
                    return (d_0___accumulator_) + (right)
                elif (len(right)) == (0):
                    return (d_0___accumulator_) + (left)
                elif lessThanOrEq((left)[0], (right)[0]):
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.Seq([(left)[0]]))
                    in0_ = _dafny.Seq((left)[1::])
                    in1_ = right
                    in2_ = lessThanOrEq
                    left = in0_
                    right = in1_
                    lessThanOrEq = in2_
                    raise _dafny.TailCall()
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.Seq([(right)[0]]))
                    in3_ = left
                    in4_ = _dafny.Seq((right)[1::])
                    in5_ = lessThanOrEq
                    left = in3_
                    right = in4_
                    lessThanOrEq = in5_
                    raise _dafny.TailCall()
                break

