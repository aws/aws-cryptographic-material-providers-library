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
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String

# Module: StandardLibrary

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Join(ss, joiner):
        d_217___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(ss)) == (1):
                    return (d_217___accumulator_) + ((ss)[0])
                elif True:
                    d_217___accumulator_ = (d_217___accumulator_) + (((ss)[0]) + (joiner))
                    in42_ = _dafny.Seq((ss)[1::])
                    in43_ = joiner
                    ss = in42_
                    joiner = in43_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Split(s, delim):
        d_218___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                d_219_i_ = default__.FindIndexMatching(s, delim, 0)
                if (d_219_i_).is_Some:
                    d_218___accumulator_ = (d_218___accumulator_) + (_dafny.Seq([_dafny.Seq((s)[:(d_219_i_).value:])]))
                    in44_ = _dafny.Seq((s)[((d_219_i_).value) + (1)::])
                    in45_ = delim
                    s = in44_
                    delim = in45_
                    raise _dafny.TailCall()
                elif True:
                    return (d_218___accumulator_) + (_dafny.Seq([s]))
                break

    @staticmethod
    def SplitOnce(s, delim):
        d_220_i_ = default__.FindIndexMatching(s, delim, 0)
        return (_dafny.Seq((s)[:(d_220_i_).value:]), _dafny.Seq((s)[((d_220_i_).value) + (1)::]))

    @staticmethod
    def SplitOnce_q(s, delim):
        d_221_valueOrError0_ = default__.FindIndexMatching(s, delim, 0)
        if (d_221_valueOrError0_).IsFailure():
            return (d_221_valueOrError0_).PropagateFailure()
        elif True:
            d_222_i_ = (d_221_valueOrError0_).Extract()
            return Wrappers.Option_Some((_dafny.Seq((s)[:d_222_i_:]), _dafny.Seq((s)[(d_222_i_) + (1)::])))

    @staticmethod
    def FindIndexMatching(s, c, i):
        def lambda13_(d_223_c_):
            def lambda14_(d_224_x_):
                return (d_224_x_) == (d_223_c_)

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
        d_225___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_225___accumulator_) + (_dafny.Seq([]))
                elif f((s)[0]):
                    d_225___accumulator_ = (d_225___accumulator_) + (_dafny.Seq([(s)[0]]))
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
        return _dafny.Seq([value for d_226___v0_ in range(n)])

    @staticmethod
    def SeqToArray(s):
        a: _dafny.Array = _dafny.Array(None, 0)
        def lambda15_(d_227_s_):
            def lambda16_(d_228_i_):
                return (d_227_s_)[d_228_i_]

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
            d_229_k_: int = exists_var_0_
            return (((0) <= (d_229_k_)) and ((d_229_k_) <= (len(a)))) and (default__.LexicographicLessOrEqualAux(a, b, less, d_229_k_))

        return _dafny.quantifier(_dafny.IntegerRange(0, (len(a)) + (1)), False, lambda17_)

    @staticmethod
    def LexicographicLessOrEqualAux(a, b, less, lengthOfCommonPrefix):
        def lambda18_(forall_var_0_):
            d_230_i_: int = forall_var_0_
            return not (((0) <= (d_230_i_)) and ((d_230_i_) < (lengthOfCommonPrefix))) or (((a)[d_230_i_]) == ((b)[d_230_i_]))

        return (((lengthOfCommonPrefix) <= (len(b))) and (_dafny.quantifier(_dafny.IntegerRange(0, lengthOfCommonPrefix), True, lambda18_))) and (((lengthOfCommonPrefix) == (len(a))) or (((lengthOfCommonPrefix) < (len(b))) and (less((a)[lengthOfCommonPrefix], (b)[lengthOfCommonPrefix]))))

    @staticmethod
    def SetToOrderedSequence(s, less):
        d_231___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                pat_let_tv0_ = s
                pat_let_tv1_ = less
                if (s) == (_dafny.Set({})):
                    return (d_231___accumulator_) + (_dafny.Seq([]))
                elif True:
                    def iife1_(_let_dummy_0):
                        d_232_a_: _dafny.Seq = None
                        with _dafny.label("_ASSIGN_SUCH_THAT_d_1"):
                            assign_such_that_1_: _dafny.Seq
                            for assign_such_that_1_ in (s).Elements:
                                d_232_a_ = assign_such_that_1_
                                if ((d_232_a_) in (s)) and (default__.IsMinimum(d_232_a_, s, less)):
                                    raise _dafny.Break("_ASSIGN_SUCH_THAT_d_1")
                            raise Exception("assign-such-that search produced no value (line 369)")
                            pass
                        return (_dafny.Seq([d_232_a_])) + (default__.SetToOrderedSequence((pat_let_tv0_) - (_dafny.Set({d_232_a_})), pat_let_tv1_))
                    return iife1_(0)
                    
                break

    @staticmethod
    def IsMinimum(a, s, less):
        def lambda19_(forall_var_1_):
            d_233_z_: _dafny.Seq = forall_var_1_
            return not ((d_233_z_) in (s)) or (default__.LexicographicLessOrEqual(a, d_233_z_, less))

        return ((a) in (s)) and (_dafny.quantifier((s).Elements, True, lambda19_))

