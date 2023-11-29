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
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibrary_mUInt
import String

# Module: StandardLibrary

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Join(ss, joiner):
        d_210___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(ss)) == (1):
                    return (d_210___accumulator_) + ((ss)[0])
                elif True:
                    d_210___accumulator_ = (d_210___accumulator_) + (((ss)[0]) + (joiner))
                    in42_ = _dafny.Seq((ss)[1::])
                    in43_ = joiner
                    ss = in42_
                    joiner = in43_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Split(s, delim):
        d_211___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                d_212_i_ = default__.FindIndexMatching(s, delim, 0)
                if (d_212_i_).is_Some:
                    d_211___accumulator_ = (d_211___accumulator_) + (_dafny.Seq([_dafny.Seq((s)[:(d_212_i_).value:])]))
                    in44_ = _dafny.Seq((s)[((d_212_i_).value) + (1)::])
                    in45_ = delim
                    s = in44_
                    delim = in45_
                    raise _dafny.TailCall()
                elif True:
                    return (d_211___accumulator_) + (_dafny.Seq([s]))
                break

    @staticmethod
    def SplitOnce(s, delim):
        d_213_i_ = default__.FindIndexMatching(s, delim, 0)
        return (_dafny.Seq((s)[:(d_213_i_).value:]), _dafny.Seq((s)[((d_213_i_).value) + (1)::]))

    @staticmethod
    def SplitOnce_q(s, delim):
        d_214_valueOrError0_ = default__.FindIndexMatching(s, delim, 0)
        if (d_214_valueOrError0_).IsFailure():
            return (d_214_valueOrError0_).PropagateFailure()
        elif True:
            d_215_i_ = (d_214_valueOrError0_).Extract()
            return Wrappers.Option_Some((_dafny.Seq((s)[:d_215_i_:]), _dafny.Seq((s)[(d_215_i_) + (1)::])))

    @staticmethod
    def FindIndexMatching(s, c, i):
        def lambda13_(d_216_c_):
            def lambda14_(d_217_x_):
                return (d_217_x_) == (d_216_c_)

            return lambda14_

        return default__.FindIndex(s, lambda13_(c), i)

    @staticmethod
    def FindIndex(s, f, i):
        while True:
            with _dafny.label():
                if (i) == (len(s)):
                    return Wrappers.Option_None()
                elif f((s)[i]):
                    return Wrappers.Option_Some(i)
                elif True:
                    in46_ = s
                    in47_ = f
                    in48_ = (i) + (1)
                    s = in46_
                    f = in47_
                    i = in48_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Filter(s, f):
        d_218___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_218___accumulator_) + (_dafny.Seq([]))
                elif f((s)[0]):
                    d_218___accumulator_ = (d_218___accumulator_) + (_dafny.Seq([(s)[0]]))
                    in49_ = _dafny.Seq((s)[1::])
                    in50_ = f
                    s = in49_
                    f = in50_
                    raise _dafny.TailCall()
                elif True:
                    in51_ = _dafny.Seq((s)[1::])
                    in52_ = f
                    s = in51_
                    f = in52_
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
        return _dafny.Seq([value for d_219___v0_ in range(n)])

    @staticmethod
    def SeqToArray(s):
        a: _dafny.Array = _dafny.Array(None, 0)
        def lambda15_(d_220_s_):
            def lambda16_(d_221_i_):
                return (d_220_s_)[d_221_i_]

            return lambda16_

        init1_ = lambda15_(s)
        nw1_ = _dafny.Array(None, len(s))
        for i0_1_ in range(nw1_.length(0)):
            nw1_[i0_1_] = init1_(i0_1_)
        a = nw1_
        return a

    @staticmethod
    def LexicographicLessOrEqual(a, b, less):
        def lambda17_(exists_var_0_):
            d_222_k_: int = exists_var_0_
            return (((0) <= (d_222_k_)) and ((d_222_k_) <= (len(a)))) and (default__.LexicographicLessOrEqualAux(a, b, less, d_222_k_))

        return _dafny.quantifier(_dafny.IntegerRange(0, (len(a)) + (1)), False, lambda17_)

    @staticmethod
    def LexicographicLessOrEqualAux(a, b, less, lengthOfCommonPrefix):
        def lambda18_(forall_var_0_):
            d_223_i_: int = forall_var_0_
            return not (((0) <= (d_223_i_)) and ((d_223_i_) < (lengthOfCommonPrefix))) or (((a)[d_223_i_]) == ((b)[d_223_i_]))

        return (((lengthOfCommonPrefix) <= (len(b))) and (_dafny.quantifier(_dafny.IntegerRange(0, lengthOfCommonPrefix), True, lambda18_))) and (((lengthOfCommonPrefix) == (len(a))) or (((lengthOfCommonPrefix) < (len(b))) and (less((a)[lengthOfCommonPrefix], (b)[lengthOfCommonPrefix]))))

    @staticmethod
    def SetToOrderedSequence(s, less):
        d_224___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                pat_let_tv0_ = s
                pat_let_tv1_ = less
                if (s) == (_dafny.Set({})):
                    return (d_224___accumulator_) + (_dafny.Seq([]))
                elif True:
                    def iife1_(_let_dummy_0):
                        d_225_a_: _dafny.Seq = None
                        with _dafny.label("_ASSIGN_SUCH_THAT_d_1"):
                            assign_such_that_1_: _dafny.Seq
                            for assign_such_that_1_ in (s).Elements:
                                d_225_a_ = assign_such_that_1_
                                if ((d_225_a_) in (s)) and (default__.IsMinimum(d_225_a_, s, less)):
                                    raise _dafny.Break("_ASSIGN_SUCH_THAT_d_1")
                            raise Exception("assign-such-that search produced no value (line 369)")
                            pass
                        return (_dafny.Seq([d_225_a_])) + (default__.SetToOrderedSequence((pat_let_tv0_) - (_dafny.Set({d_225_a_})), pat_let_tv1_))
                    return iife1_(0)
                    
                break

    @staticmethod
    def IsMinimum(a, s, less):
        def lambda19_(forall_var_1_):
            d_226_z_: _dafny.Seq = forall_var_1_
            return not ((d_226_z_) in (s)) or (default__.LexicographicLessOrEqual(a, d_226_z_, less))

        return ((a) in (s)) and (_dafny.quantifier((s).Elements, True, lambda19_))

