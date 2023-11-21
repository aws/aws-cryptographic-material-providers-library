import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_mUInt
import StandardLibrary
import UTF8
import TestUTF8
import Time
import TestTime
import HexStrings
import TestHexStrings
import Relations

assert "Seq_mMergeSort" == __name__
Seq_mMergeSort = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def MergeSortBy(a, lessThanOrEq):
        if (len(a)) <= (1):
            return a
        elif True:
            d_140_splitIndex_ = _dafny.euclidian_division(len(a), 2)
            d_141_left_ = _dafny.Seq((a)[:d_140_splitIndex_:])
            d_142_right_ = _dafny.Seq((a)[d_140_splitIndex_::])
            d_143_leftSorted_ = Seq_mMergeSort.default__.MergeSortBy(d_141_left_, lessThanOrEq)
            d_144_rightSorted_ = Seq_mMergeSort.default__.MergeSortBy(d_142_right_, lessThanOrEq)
            return Seq_mMergeSort.default__.MergeSortedWith(d_143_leftSorted_, d_144_rightSorted_, lessThanOrEq)

    @staticmethod
    def MergeSortedWith(left, right, lessThanOrEq):
        d_145___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(left)) == (0):
                    return (d_145___accumulator_) + (right)
                elif (len(right)) == (0):
                    return (d_145___accumulator_) + (left)
                elif lessThanOrEq((left)[0], (right)[0]):
                    d_145___accumulator_ = (d_145___accumulator_) + (_dafny.Seq([(left)[0]]))
                    in27_ = _dafny.Seq((left)[1::])
                    in28_ = right
                    in29_ = lessThanOrEq
                    left = in27_
                    right = in28_
                    lessThanOrEq = in29_
                    raise _dafny.TailCall()
                elif True:
                    d_145___accumulator_ = (d_145___accumulator_) + (_dafny.Seq([(right)[0]]))
                    in30_ = left
                    in31_ = _dafny.Seq((right)[1::])
                    in32_ = lessThanOrEq
                    left = in30_
                    right = in31_
                    lessThanOrEq = in32_
                    raise _dafny.TailCall()
                break

