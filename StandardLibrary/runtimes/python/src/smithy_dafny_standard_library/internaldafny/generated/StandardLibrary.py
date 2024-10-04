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
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String

# Module: StandardLibrary

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Join(ss, joiner):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(ss)) == (1):
                    return (d_0___accumulator_) + ((ss)[0])
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (((ss)[0]) + (joiner))
                    in0_ = _dafny.Seq((ss)[1::])
                    in1_ = joiner
                    ss = in0_
                    joiner = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Split(s, delim):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                d_1_i_ = default__.FindIndexMatching(s, delim, 0)
                if (d_1_i_).is_Some:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.Seq([_dafny.Seq((s)[:(d_1_i_).value:])]))
                    in0_ = _dafny.Seq((s)[((d_1_i_).value) + (1)::])
                    in1_ = delim
                    s = in0_
                    delim = in1_
                    raise _dafny.TailCall()
                elif True:
                    return (d_0___accumulator_) + (_dafny.Seq([s]))
                break

    @staticmethod
    def SplitOnce(s, delim):
        d_0_i_ = default__.FindIndexMatching(s, delim, 0)
        return (_dafny.Seq((s)[:(d_0_i_).value:]), _dafny.Seq((s)[((d_0_i_).value) + (1)::]))

    @staticmethod
    def SplitOnce_q(s, delim):
        d_0_valueOrError0_ = default__.FindIndexMatching(s, delim, 0)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_i_ = (d_0_valueOrError0_).Extract()
            return Wrappers.Option_Some((_dafny.Seq((s)[:d_1_i_:]), _dafny.Seq((s)[(d_1_i_) + (1)::])))

    @staticmethod
    def FindIndexMatching(s, c, i):
        def lambda0_(d_0_c_):
            def lambda1_(d_1_x_):
                return (d_1_x_) == (d_0_c_)

            return lambda1_

        return default__.FindIndex(s, lambda0_(c), i)

    @staticmethod
    def FindIndex(s, f, i):
        while True:
            with _dafny.label():
                if (i) == (len(s)):
                    return Wrappers.Option_None()
                elif f((s)[i]):
                    return Wrappers.Option_Some(i)
                elif True:
                    in0_ = s
                    in1_ = f
                    in2_ = (i) + (1)
                    s = in0_
                    f = in1_
                    i = in2_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Filter(s, f):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_0___accumulator_) + (_dafny.Seq([]))
                elif f((s)[0]):
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.Seq([(s)[0]]))
                    in0_ = _dafny.Seq((s)[1::])
                    in1_ = f
                    s = in0_
                    f = in1_
                    raise _dafny.TailCall()
                elif True:
                    in2_ = _dafny.Seq((s)[1::])
                    in3_ = f
                    s = in2_
                    f = in3_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Min(a, b):
        if (a) < (b):
            return a
        elif True:
            return b

    @staticmethod
    def Fill(value, n):
        return _dafny.Seq([value for d_0___v0_ in range(n)])

    @staticmethod
    def SeqToArray(s):
        a: _dafny.Array = _dafny.Array(None, 0)
        def lambda0_(d_0_s_):
            def lambda1_(d_1_i_):
                return (d_0_s_)[d_1_i_]

            return lambda1_

        init0_ = lambda0_(s)
        nw0_ = _dafny.Array(None, len(s))
        for i0_0_ in range(nw0_.length(0)):
            nw0_[i0_0_] = init0_(i0_0_)
        a = nw0_
        return a

    @staticmethod
    def LexicographicLessOrEqual(a, b, less):
        def lambda0_(exists_var_0_):
            d_0_k_: int = exists_var_0_
            return (((0) <= (d_0_k_)) and ((d_0_k_) <= (len(a)))) and (default__.LexicographicLessOrEqualAux(a, b, less, d_0_k_))

        return _dafny.quantifier(_dafny.IntegerRange(0, (len(a)) + (1)), False, lambda0_)

    @staticmethod
    def LexicographicLessOrEqualAux(a, b, less, lengthOfCommonPrefix):
        def lambda0_(forall_var_0_):
            d_0_i_: int = forall_var_0_
            return not (((0) <= (d_0_i_)) and ((d_0_i_) < (lengthOfCommonPrefix))) or (((a)[d_0_i_]) == ((b)[d_0_i_]))

        return (((lengthOfCommonPrefix) <= (len(b))) and (_dafny.quantifier(_dafny.IntegerRange(0, lengthOfCommonPrefix), True, lambda0_))) and (((lengthOfCommonPrefix) == (len(a))) or (((lengthOfCommonPrefix) < (len(b))) and (less((a)[lengthOfCommonPrefix], (b)[lengthOfCommonPrefix]))))

    @staticmethod
    def SetToOrderedSequence(s, less):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                pat_let_tv0_ = s
                pat_let_tv1_ = less
                if (s) == (_dafny.Set({})):
                    return (d_0___accumulator_) + (_dafny.Seq([]))
                elif True:
                    def iife0_(_let_dummy_0):
                        d_1_a_: _dafny.Seq = None
                        with _dafny.label("_ASSIGN_SUCH_THAT_d_0"):
                            assign_such_that_0_: _dafny.Seq
                            for assign_such_that_0_ in (s).Elements:
                                d_1_a_ = assign_such_that_0_
                                if ((d_1_a_) in (s)) and (default__.IsMinimum(d_1_a_, s, less)):
                                    raise _dafny.Break("_ASSIGN_SUCH_THAT_d_0")
                            raise Exception("assign-such-that search produced no value (line 369)")
                            pass
                        return (_dafny.Seq([d_1_a_])) + (default__.SetToOrderedSequence((pat_let_tv0_) - (_dafny.Set({d_1_a_})), pat_let_tv1_))
                    return iife0_(0)
                    
                break

    @staticmethod
    def IsMinimum(a, s, less):
        def lambda0_(forall_var_0_):
            d_0_z_: _dafny.Seq = forall_var_0_
            return not ((d_0_z_) in (s)) or (default__.LexicographicLessOrEqual(a, d_0_z_, less))

        return ((a) in (s)) and (_dafny.quantifier((s).Elements, True, lambda0_))

