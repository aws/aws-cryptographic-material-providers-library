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
        def lambda0_(d_0_xs_):
            def lambda1_(d_1_i_):
                return (d_0_xs_)[d_1_i_]

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
                d_0_x_: TypeVar('T__') = compr_0_
                if (d_0_x_) in (xs):
                    coll0_ = coll0_.union(_dafny.Set([d_0_x_]))
            return _dafny.Set(coll0_)
        return iife0_()
        

    @staticmethod
    def IndexOf(xs, v):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if ((xs)[0]) == (v):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (1)
                    in0_ = _dafny.Seq((xs)[1::])
                    in1_ = v
                    xs = in0_
                    v = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def IndexOfOption(xs, v):
        if (len(xs)) == (0):
            return Wrappers.Option_None()
        elif ((xs)[0]) == (v):
            return Wrappers.Option_Some(0)
        elif True:
            d_0_o_k_ = default__.IndexOfOption(_dafny.Seq((xs)[1::]), v)
            if (d_0_o_k_).is_Some:
                return Wrappers.Option_Some(((d_0_o_k_).value) + (1))
            elif True:
                return Wrappers.Option_None()

    @staticmethod
    def LastIndexOf(xs, v):
        while True:
            with _dafny.label():
                if ((xs)[(len(xs)) - (1)]) == (v):
                    return (len(xs)) - (1)
                elif True:
                    in0_ = _dafny.Seq((xs)[:(len(xs)) - (1):])
                    in1_ = v
                    xs = in0_
                    v = in1_
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
                    in0_ = _dafny.Seq((xs)[:(len(xs)) - (1):])
                    in1_ = v
                    xs = in0_
                    v = in1_
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
            d_0_i_ = default__.IndexOf(xs, v)
            return (_dafny.Seq((xs)[:d_0_i_:])) + (_dafny.Seq((xs)[(d_0_i_) + (1)::]))

    @staticmethod
    def Insert(xs, a, pos):
        return ((_dafny.Seq((xs)[:pos:])) + (_dafny.Seq([a]))) + (_dafny.Seq((xs)[pos::]))

    @staticmethod
    def Reverse(xs):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (xs) == (_dafny.Seq([])):
                    return (d_0___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.Seq([(xs)[(len(xs)) - (1)]]))
                    in0_ = _dafny.Seq((xs)[0:(len(xs)) - (1):])
                    xs = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Repeat(v, length):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (length) == (0):
                    return (d_0___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.Seq([v]))
                    in0_ = v
                    in1_ = (length) - (1)
                    v = in0_
                    length = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Unzip(xs):
        if (len(xs)) == (0):
            return (_dafny.Seq([]), _dafny.Seq([]))
        elif True:
            let_tmp_rhs0_ = default__.Unzip(default__.DropLast(xs))
            d_0_a_ = let_tmp_rhs0_[0]
            d_1_b_ = let_tmp_rhs0_[1]
            return ((d_0_a_) + (_dafny.Seq([(default__.Last(xs))[0]])), (d_1_b_) + (_dafny.Seq([(default__.Last(xs))[1]])))

    @staticmethod
    def Zip(xs, ys):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (_dafny.Seq([])) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (_dafny.Seq([(default__.Last(xs), default__.Last(ys))])) + (d_0___accumulator_)
                    in0_ = default__.DropLast(xs)
                    in1_ = default__.DropLast(ys)
                    xs = in0_
                    ys = in1_
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
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (d_0___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((xs)[0])
                    in0_ = _dafny.Seq((xs)[1::])
                    xs = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FlattenReverse(xs):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (_dafny.Seq([])) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (default__.Last(xs)) + (d_0___accumulator_)
                    in0_ = default__.DropLast(xs)
                    xs = in0_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Map(f, xs):
        return _dafny.Seq([f((xs)[d_0_i_]) for d_0_i_ in range(len(xs))])

    @staticmethod
    def MapWithResult(f, xs):
        if (len(xs)) == (0):
            return Wrappers.Result_Success(_dafny.Seq([]))
        elif True:
            d_0_valueOrError0_ = f((xs)[0])
            if (d_0_valueOrError0_).IsFailure():
                return (d_0_valueOrError0_).PropagateFailure()
            elif True:
                d_1_head_ = (d_0_valueOrError0_).Extract()
                d_2_valueOrError1_ = default__.MapWithResult(f, _dafny.Seq((xs)[1::]))
                if (d_2_valueOrError1_).IsFailure():
                    return (d_2_valueOrError1_).PropagateFailure()
                elif True:
                    d_3_tail_ = (d_2_valueOrError1_).Extract()
                    return Wrappers.Result_Success((_dafny.Seq([d_1_head_])) + (d_3_tail_))

    @staticmethod
    def Filter(f, xs):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (d_0___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((_dafny.Seq([(xs)[0]]) if f((xs)[0]) else _dafny.Seq([])))
                    in0_ = f
                    in1_ = _dafny.Seq((xs)[1::])
                    f = in0_
                    xs = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FoldLeft(f, init, xs):
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return init
                elif True:
                    in0_ = f
                    in1_ = f(init, (xs)[0])
                    in2_ = _dafny.Seq((xs)[1::])
                    f = in0_
                    init = in1_
                    xs = in2_
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
        for d_0_i_ in range(len(xs)-1, lo0_-1, -1):
            d_1_next_: _dafny.Seq
            d_1_next_ = f((xs)[d_0_i_])
            result = (d_1_next_) + (result)
        return result

