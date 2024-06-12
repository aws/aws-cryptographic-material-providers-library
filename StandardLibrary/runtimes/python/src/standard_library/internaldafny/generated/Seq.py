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
        def lambda0_(d_15_xs_):
            def lambda1_(d_16_i_):
                return (d_15_xs_)[d_16_i_]

            return lambda1_

        init0_ = lambda0_(xs)
        nw0_ = _dafny.Array(None, len(xs))
        for i0_0_ in range(nw0_.length(0)):
            nw0_[i0_0_] = init0_(i0_0_)
        a = nw0_
        return a

    @staticmethod
    def ToSet(xs):
        def iife0_():
            coll0_ = _dafny.Set()
            compr_0_: TypeVar('T__')
            for compr_0_ in (xs).Elements:
                d_17_x_: TypeVar('T__') = compr_0_
                if (d_17_x_) in (xs):
                    coll0_ = coll0_.union(_dafny.Set([d_17_x_]))
            return _dafny.Set(coll0_)
        return iife0_()
        

    @staticmethod
    def IndexOf(xs, v):
        d_18___accumulator_ = 0
        while True:
            with _dafny.label():
                if ((xs)[0]) == (v):
                    return (0) + (d_18___accumulator_)
                elif True:
                    d_18___accumulator_ = (d_18___accumulator_) + (1)
                    in6_ = _dafny.Seq((xs)[1::])
                    in7_ = v
                    xs = in6_
                    v = in7_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def IndexOfOption(xs, v):
        if (len(xs)) == (0):
            return Wrappers.Option_None()
        elif ((xs)[0]) == (v):
            return Wrappers.Option_Some(0)
        elif True:
            d_19_o_k_ = default__.IndexOfOption(_dafny.Seq((xs)[1::]), v)
            if (d_19_o_k_).is_Some:
                return Wrappers.Option_Some(((d_19_o_k_).value) + (1))
            elif True:
                return Wrappers.Option_None()

    @staticmethod
    def LastIndexOf(xs, v):
        while True:
            with _dafny.label():
                if ((xs)[(len(xs)) - (1)]) == (v):
                    return (len(xs)) - (1)
                elif True:
                    in8_ = _dafny.Seq((xs)[:(len(xs)) - (1):])
                    in9_ = v
                    xs = in8_
                    v = in9_
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
                    in10_ = _dafny.Seq((xs)[:(len(xs)) - (1):])
                    in11_ = v
                    xs = in10_
                    v = in11_
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
            d_20_i_ = default__.IndexOf(xs, v)
            return (_dafny.Seq((xs)[:d_20_i_:])) + (_dafny.Seq((xs)[(d_20_i_) + (1)::]))

    @staticmethod
    def Insert(xs, a, pos):
        return ((_dafny.Seq((xs)[:pos:])) + (_dafny.Seq([a]))) + (_dafny.Seq((xs)[pos::]))

    @staticmethod
    def Reverse(xs):
        d_21___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (xs) == (_dafny.Seq([])):
                    return (d_21___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_21___accumulator_ = (d_21___accumulator_) + (_dafny.Seq([(xs)[(len(xs)) - (1)]]))
                    in12_ = _dafny.Seq((xs)[0:(len(xs)) - (1):])
                    xs = in12_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Repeat(v, length):
        d_22___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (length) == (0):
                    return (d_22___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_22___accumulator_ = (d_22___accumulator_) + (_dafny.Seq([v]))
                    in13_ = v
                    in14_ = (length) - (1)
                    v = in13_
                    length = in14_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Unzip(xs):
        if (len(xs)) == (0):
            return (_dafny.Seq([]), _dafny.Seq([]))
        elif True:
            let_tmp_rhs0_ = default__.Unzip(default__.DropLast(xs))
            d_23_a_ = let_tmp_rhs0_[0]
            d_24_b_ = let_tmp_rhs0_[1]
            return ((d_23_a_) + (_dafny.Seq([(default__.Last(xs))[0]])), (d_24_b_) + (_dafny.Seq([(default__.Last(xs))[1]])))

    @staticmethod
    def Zip(xs, ys):
        d_25___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (_dafny.Seq([])) + (d_25___accumulator_)
                elif True:
                    d_25___accumulator_ = (_dafny.Seq([(default__.Last(xs), default__.Last(ys))])) + (d_25___accumulator_)
                    in15_ = default__.DropLast(xs)
                    in16_ = default__.DropLast(ys)
                    xs = in15_
                    ys = in16_
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
        d_26___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (d_26___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_26___accumulator_ = (d_26___accumulator_) + ((xs)[0])
                    in17_ = _dafny.Seq((xs)[1::])
                    xs = in17_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FlattenReverse(xs):
        d_27___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (_dafny.Seq([])) + (d_27___accumulator_)
                elif True:
                    d_27___accumulator_ = (default__.Last(xs)) + (d_27___accumulator_)
                    in18_ = default__.DropLast(xs)
                    xs = in18_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Map(f, xs):
        return _dafny.Seq([f((xs)[d_28_i_]) for d_28_i_ in range(len(xs))])

    @staticmethod
    def MapWithResult(f, xs):
        if (len(xs)) == (0):
            return Wrappers.Result_Success(_dafny.Seq([]))
        elif True:
            d_29_valueOrError0_ = f((xs)[0])
            if (d_29_valueOrError0_).IsFailure():
                return (d_29_valueOrError0_).PropagateFailure()
            elif True:
                d_30_head_ = (d_29_valueOrError0_).Extract()
                d_31_valueOrError1_ = default__.MapWithResult(f, _dafny.Seq((xs)[1::]))
                if (d_31_valueOrError1_).IsFailure():
                    return (d_31_valueOrError1_).PropagateFailure()
                elif True:
                    d_32_tail_ = (d_31_valueOrError1_).Extract()
                    return Wrappers.Result_Success((_dafny.Seq([d_30_head_])) + (d_32_tail_))

    @staticmethod
    def Filter(f, xs):
        d_33___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (d_33___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_33___accumulator_ = (d_33___accumulator_) + ((_dafny.Seq([(xs)[0]]) if f((xs)[0]) else _dafny.Seq([])))
                    in19_ = f
                    in20_ = _dafny.Seq((xs)[1::])
                    f = in19_
                    xs = in20_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FoldLeft(f, init, xs):
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return init
                elif True:
                    in21_ = f
                    in22_ = f(init, (xs)[0])
                    in23_ = _dafny.Seq((xs)[1::])
                    f = in21_
                    init = in22_
                    xs = in23_
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
        for d_34_i_ in range(len(xs)-1, lo0_-1, -1):
            d_35_next_: _dafny.Seq
            d_35_next_ = f((xs)[d_34_i_])
            result = (d_35_next_) + (result)
        return result

    @staticmethod
    def SetToSeq(s):
        xs: _dafny.Seq = _dafny.Seq({})
        xs = _dafny.Seq([])
        d_36_left_: _dafny.Set
        d_36_left_ = s
        while (d_36_left_) != (_dafny.Set({})):
            d_37_x_: TypeVar('T__')
            with _dafny.label("_ASSIGN_SUCH_THAT_d_0"):
                assign_such_that_0_: TypeVar('T__')
                for assign_such_that_0_ in (d_36_left_).Elements:
                    d_37_x_ = assign_such_that_0_
                    if (d_37_x_) in (d_36_left_):
                        raise _dafny.Break("_ASSIGN_SUCH_THAT_d_0")
                raise Exception("assign-such-that search produced no value (line 872)")
                pass
            d_36_left_ = (d_36_left_) - (_dafny.Set({d_37_x_}))
            xs = (xs) + (_dafny.Seq([d_37_x_]))
        return xs

    @staticmethod
    def SetToSortedSeq(s, R):
        xs: _dafny.Seq = _dafny.Seq({})
        out0_: _dafny.Seq
        out0_ = default__.SetToSeq(s)
        xs = out0_
        xs = Seq_MergeSort.default__.MergeSortBy(xs, R)
        return xs

