import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary
import UTF8
import TestUTF8
import Time
import TestTime
import HexStrings
import TestHexStrings
import Relations
import Seq_MergeSort
import Math

# Module: Seq

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def First(xs):
        return (xs)[0]

    @staticmethod
    def DropFirst(xs):
        return _dafny.Seq((xs)[1::])

    @staticmethod
    def Last(xs):
        return (xs)[(len(xs)) - (1)]

    @staticmethod
    def DropLast(xs):
        return _dafny.Seq((xs)[:(len(xs)) - (1):])

    @staticmethod
    def ToArray(xs):
        a: _dafny.Array = _dafny.Array(None, 0)
        def lambda10_(d_146_xs_):
            def lambda11_(d_147_i_):
                return (d_146_xs_)[d_147_i_]

            return lambda11_

        init1_ = lambda10_(xs)
        nw1_ = _dafny.Array(None, len(xs))
        for i0_1_ in range(nw1_.length(0)):
            nw1_[i0_1_] = init1_(i0_1_)
        a = nw1_
        return a

    @staticmethod
    def ToSet(xs):
        def iife1_():
            coll0_ = _dafny.Set()
            compr_0_: TypeVar('T__')
            for compr_0_ in (xs).Elements:
                d_148_x_: TypeVar('T__') = compr_0_
                if (d_148_x_) in (xs):
                    coll0_ = coll0_.union(_dafny.Set([d_148_x_]))
            return _dafny.Set(coll0_)
        return iife1_()
        

    @staticmethod
    def IndexOf(xs, v):
        d_149___accumulator_ = 0
        while True:
            with _dafny.label():
                if ((xs)[0]) == (v):
                    return (0) + (d_149___accumulator_)
                elif True:
                    d_149___accumulator_ = (d_149___accumulator_) + (1)
                    in33_ = _dafny.Seq((xs)[1::])
                    in34_ = v
                    xs = in33_
                    v = in34_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def IndexOfOption(xs, v):
        if (len(xs)) == (0):
            return Wrappers.Option_None()
        elif ((xs)[0]) == (v):
            return Wrappers.Option_Some(0)
        elif True:
            d_150_o_k_ = default__.IndexOfOption(_dafny.Seq((xs)[1::]), v)
            if (d_150_o_k_).is_Some:
                return Wrappers.Option_Some(((d_150_o_k_).value) + (1))
            elif True:
                return Wrappers.Option_None()

    @staticmethod
    def LastIndexOf(xs, v):
        while True:
            with _dafny.label():
                if ((xs)[(len(xs)) - (1)]) == (v):
                    return (len(xs)) - (1)
                elif True:
                    in35_ = _dafny.Seq((xs)[:(len(xs)) - (1):])
                    in36_ = v
                    xs = in35_
                    v = in36_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def LastIndexOfOption(xs, v):
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return Wrappers.Option_None()
                elif ((xs)[(len(xs)) - (1)]) == (v):
                    return Wrappers.Option_Some((len(xs)) - (1))
                elif True:
                    in37_ = _dafny.Seq((xs)[:(len(xs)) - (1):])
                    in38_ = v
                    xs = in37_
                    v = in38_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Remove(xs, pos):
        return (_dafny.Seq((xs)[:pos:])) + (_dafny.Seq((xs)[(pos) + (1)::]))

    @staticmethod
    def RemoveValue(xs, v):
        if (v) not in (xs):
            return xs
        elif True:
            d_151_i_ = default__.IndexOf(xs, v)
            return (_dafny.Seq((xs)[:d_151_i_:])) + (_dafny.Seq((xs)[(d_151_i_) + (1)::]))

    @staticmethod
    def Insert(xs, a, pos):
        return ((_dafny.Seq((xs)[:pos:])) + (_dafny.Seq([a]))) + (_dafny.Seq((xs)[pos::]))

    @staticmethod
    def Reverse(xs):
        d_152___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (xs) == (_dafny.Seq([])):
                    return (d_152___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_152___accumulator_ = (d_152___accumulator_) + (_dafny.Seq([(xs)[(len(xs)) - (1)]]))
                    in39_ = _dafny.Seq((xs)[0:(len(xs)) - (1):])
                    xs = in39_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Repeat(v, length):
        d_153___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (length) == (0):
                    return (d_153___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_153___accumulator_ = (d_153___accumulator_) + (_dafny.Seq([v]))
                    in40_ = v
                    in41_ = (length) - (1)
                    v = in40_
                    length = in41_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Unzip(xs):
        if (len(xs)) == (0):
            return (_dafny.Seq([]), _dafny.Seq([]))
        elif True:
            let_tmp_rhs0_ = default__.Unzip(default__.DropLast(xs))
            d_154_a_ = let_tmp_rhs0_[0]
            d_155_b_ = let_tmp_rhs0_[1]
            return ((d_154_a_) + (_dafny.Seq([(default__.Last(xs))[0]])), (d_155_b_) + (_dafny.Seq([(default__.Last(xs))[1]])))

    @staticmethod
    def Zip(xs, ys):
        d_156___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (_dafny.Seq([])) + (d_156___accumulator_)
                elif True:
                    d_156___accumulator_ = (_dafny.Seq([(default__.Last(xs), default__.Last(ys))])) + (d_156___accumulator_)
                    in42_ = default__.DropLast(xs)
                    in43_ = default__.DropLast(ys)
                    xs = in42_
                    ys = in43_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Max(xs):
        if (len(xs)) == (1):
            return (xs)[0]
        elif True:
            return Math.default__.Max((xs)[0], default__.Max(_dafny.Seq((xs)[1::])))

    @staticmethod
    def Min(xs):
        if (len(xs)) == (1):
            return (xs)[0]
        elif True:
            return Math.default__.Min((xs)[0], default__.Min(_dafny.Seq((xs)[1::])))

    @staticmethod
    def Flatten(xs):
        d_157___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (d_157___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_157___accumulator_ = (d_157___accumulator_) + ((xs)[0])
                    in44_ = _dafny.Seq((xs)[1::])
                    xs = in44_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FlattenReverse(xs):
        d_158___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (_dafny.Seq([])) + (d_158___accumulator_)
                elif True:
                    d_158___accumulator_ = (default__.Last(xs)) + (d_158___accumulator_)
                    in45_ = default__.DropLast(xs)
                    xs = in45_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Map(f, xs):
        return _dafny.Seq([f((xs)[d_159_i_]) for d_159_i_ in range(len(xs))])

    @staticmethod
    def MapWithResult(f, xs):
        if (len(xs)) == (0):
            return Wrappers.Result_Success(_dafny.Seq([]))
        elif True:
            d_160_valueOrError0_ = f((xs)[0])
            if (d_160_valueOrError0_).IsFailure():
                return (d_160_valueOrError0_).PropagateFailure()
            elif True:
                d_161_head_ = (d_160_valueOrError0_).Extract()
                d_162_valueOrError1_ = default__.MapWithResult(f, _dafny.Seq((xs)[1::]))
                if (d_162_valueOrError1_).IsFailure():
                    return (d_162_valueOrError1_).PropagateFailure()
                elif True:
                    d_163_tail_ = (d_162_valueOrError1_).Extract()
                    return Wrappers.Result_Success((_dafny.Seq([d_161_head_])) + (d_163_tail_))

    @staticmethod
    def Filter(f, xs):
        d_164___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (d_164___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_164___accumulator_ = (d_164___accumulator_) + ((_dafny.Seq([(xs)[0]]) if f((xs)[0]) else _dafny.Seq([])))
                    in46_ = f
                    in47_ = _dafny.Seq((xs)[1::])
                    f = in46_
                    xs = in47_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FoldLeft(f, init, xs):
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return init
                elif True:
                    in48_ = f
                    in49_ = f(init, (xs)[0])
                    in50_ = _dafny.Seq((xs)[1::])
                    f = in48_
                    init = in49_
                    xs = in50_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FoldRight(f, xs, init):
        if (len(xs)) == (0):
            return init
        elif True:
            return f((xs)[0], default__.FoldRight(f, _dafny.Seq((xs)[1::]), init))

    @staticmethod
    def FlatMap(f, xs):
        result: _dafny.Seq = _dafny.Seq({})
        result = _dafny.Seq([])
        lo0_ = 0
        for d_165_i_ in range(len(xs)-1, lo0_-1, -1):
            d_166_next_: _dafny.Seq
            d_166_next_ = f((xs)[d_165_i_])
            result = (d_166_next_) + (result)
        return result

    @staticmethod
    def SetToSeq(s):
        xs: _dafny.Seq = _dafny.Seq({})
        xs = _dafny.Seq([])
        d_167_left_: _dafny.Set
        d_167_left_ = s
        while (d_167_left_) != (_dafny.Set({})):
            d_168_x_: TypeVar('T__')
            with _dafny.label("_ASSIGN_SUCH_THAT_d_1"):
                assign_such_that_1_: TypeVar('T__')
                for assign_such_that_1_ in (d_167_left_).Elements:
                    d_168_x_ = assign_such_that_1_
                    if (d_168_x_) in (d_167_left_):
                        raise _dafny.Break("_ASSIGN_SUCH_THAT_d_1")
                raise Exception("assign-such-that search produced no value (line 872)")
                pass
            d_167_left_ = (d_167_left_) - (_dafny.Set({d_168_x_}))
            xs = (xs) + (_dafny.Seq([d_168_x_]))
        return xs

    @staticmethod
    def SetToSortedSeq(s, R):
        xs: _dafny.Seq = _dafny.Seq({})
        out4_: _dafny.Seq
        out4_ = default__.SetToSeq(s)
        xs = out4_
        xs = Seq_MergeSort.default__.MergeSortBy(xs, R)
        return xs

