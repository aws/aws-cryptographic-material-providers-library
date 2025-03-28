// Class __default
// Dafny class __default compiled into Java
package Seq_Compile;

import Wrappers_Compile.*;
import Seq_mMergeSort_Compile.*;
import Math_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static <__T> __T First(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> xs)
  {
    return ((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
  }
  public static <__T> dafny.DafnySequence<? extends __T> DropFirst(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> xs)
  {
    return (xs).drop(java.math.BigInteger.ONE);
  }
  public static <__T> __T Last(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> xs)
  {
    return ((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt(((java.math.BigInteger.valueOf((xs).length())).subtract(java.math.BigInteger.ONE))))));
  }
  public static <__T> dafny.DafnySequence<? extends __T> DropLast(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> xs)
  {
    return (xs).take((java.math.BigInteger.valueOf((xs).length())).subtract(java.math.BigInteger.ONE));
  }
  public static <__T> java.lang.Object ToArray(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> xs)
  {
    java.lang.Object a = (java.lang.Object)_td___T.newArray(0);
    if(true) {
      java.util.function.Function<java.math.BigInteger, __T> _init0 = ((java.util.function.Function<dafny.DafnySequence<? extends __T>, java.util.function.Function<java.math.BigInteger, __T>>)(_0_xs) -> ((java.util.function.Function<java.math.BigInteger, __T>)(_1_i_boxed0) -> {
        java.math.BigInteger _1_i = ((java.math.BigInteger)(java.lang.Object)(_1_i_boxed0));
        return ((__T)(java.lang.Object)((_0_xs).select(dafny.Helpers.toInt((_1_i)))));
      })).apply(xs);
      java.lang.Object _nw0 = (java.lang.Object) _td___T.newArray(dafny.Helpers.toIntChecked((java.math.BigInteger.valueOf((xs).length())), "Java arrays may be no larger than the maximum 32-bit signed int"));
      for (java.math.BigInteger _i0_0 = java.math.BigInteger.ZERO; _i0_0.compareTo(java.math.BigInteger.valueOf(java.lang.reflect.Array.getLength(_nw0))) < 0; _i0_0 = _i0_0.add(java.math.BigInteger.ONE)) {
        _td___T.setArrayElement(_nw0, dafny.Helpers.toInt(_i0_0), ((__T)(java.lang.Object)(_init0.apply(_i0_0))));
      }
      a = _nw0;
    }
    return a;
  }
  public static <__T> dafny.DafnySet<? extends __T> ToSet(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> xs)
  {
    return ((java.util.function.Function<dafny.DafnySequence<? extends __T>, dafny.DafnySet<? extends __T>>)(_0_xs) -> ((dafny.Function0<dafny.DafnySet<? extends __T>>)(() -> {
      java.util.ArrayList<__T> _coll0 = new java.util.ArrayList<>();
      for (__T _compr_0_boxed0 : (_0_xs).Elements()) {
        __T _compr_0 = ((__T)(java.lang.Object)(_compr_0_boxed0));
        __T _1_x = (__T)_compr_0;
        if ((_0_xs).contains(_1_x)) {
          _coll0.add(_1_x);
        }
      }
      return new dafny.DafnySet<__T>(_coll0);
    })).apply()).apply(xs);
  }
  public static <__T> java.math.BigInteger IndexOf(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> xs, __T v)
  {
    java.math.BigInteger _0___accumulator = java.math.BigInteger.ZERO;
    TAIL_CALL_START: while (true) {
      if (java.util.Objects.equals(((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), v)) {
        return (java.math.BigInteger.ZERO).add(_0___accumulator);
      } else {
        _0___accumulator = (_0___accumulator).add(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends __T> _in0 = (xs).drop(java.math.BigInteger.ONE);
        __T _in1 = v;
        xs = _in0;
        v = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static <__T> Wrappers_Compile.Option<java.math.BigInteger> IndexOfOption(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> xs, __T v)
  {
    if ((java.math.BigInteger.valueOf((xs).length())).signum() == 0) {
      return Wrappers_Compile.Option.<java.math.BigInteger>create_None(dafny.TypeDescriptor.BIG_INTEGER);
    } else if (java.util.Objects.equals(((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), v)) {
      return Wrappers_Compile.Option.<java.math.BigInteger>create_Some(dafny.TypeDescriptor.BIG_INTEGER, java.math.BigInteger.ZERO);
    } else {
      Wrappers_Compile.Option<java.math.BigInteger> _0_o_k = __default.<__T>IndexOfOption(_td___T, (xs).drop(java.math.BigInteger.ONE), v);
      if ((_0_o_k).is_Some()) {
        return Wrappers_Compile.Option.<java.math.BigInteger>create_Some(dafny.TypeDescriptor.BIG_INTEGER, ((_0_o_k).dtor_value()).add(java.math.BigInteger.ONE));
      } else {
        return Wrappers_Compile.Option.<java.math.BigInteger>create_None(dafny.TypeDescriptor.BIG_INTEGER);
      }
    }
  }
  public static <__T> java.math.BigInteger LastIndexOf(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> xs, __T v)
  {
    TAIL_CALL_START: while (true) {
      if (java.util.Objects.equals(((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt(((java.math.BigInteger.valueOf((xs).length())).subtract(java.math.BigInteger.ONE)))))), v)) {
        return (java.math.BigInteger.valueOf((xs).length())).subtract(java.math.BigInteger.ONE);
      } else {
        dafny.DafnySequence<? extends __T> _in0 = (xs).take((java.math.BigInteger.valueOf((xs).length())).subtract(java.math.BigInteger.ONE));
        __T _in1 = v;
        xs = _in0;
        v = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static <__T> Wrappers_Compile.Option<java.math.BigInteger> LastIndexOfOption(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> xs, __T v)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((xs).length())).signum() == 0) {
        return Wrappers_Compile.Option.<java.math.BigInteger>create_None(dafny.TypeDescriptor.BIG_INTEGER);
      } else if (java.util.Objects.equals(((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt(((java.math.BigInteger.valueOf((xs).length())).subtract(java.math.BigInteger.ONE)))))), v)) {
        return Wrappers_Compile.Option.<java.math.BigInteger>create_Some(dafny.TypeDescriptor.BIG_INTEGER, (java.math.BigInteger.valueOf((xs).length())).subtract(java.math.BigInteger.ONE));
      } else {
        dafny.DafnySequence<? extends __T> _in0 = (xs).take((java.math.BigInteger.valueOf((xs).length())).subtract(java.math.BigInteger.ONE));
        __T _in1 = v;
        xs = _in0;
        v = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static <__T> dafny.DafnySequence<? extends __T> Remove(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> xs, java.math.BigInteger pos)
  {
    return dafny.DafnySequence.<__T>concatenate((xs).take(pos), (xs).drop((pos).add(java.math.BigInteger.ONE)));
  }
  public static <__T> dafny.DafnySequence<? extends __T> RemoveValue(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> xs, __T v)
  {
    if (!(xs).contains(v)) {
      return xs;
    } else {
      java.math.BigInteger _0_i = __default.<__T>IndexOf(_td___T, xs, v);
      return dafny.DafnySequence.<__T>concatenate((xs).take(_0_i), (xs).drop((_0_i).add(java.math.BigInteger.ONE)));
    }
  }
  public static <__T> dafny.DafnySequence<? extends __T> Insert(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> xs, __T a, java.math.BigInteger pos)
  {
    return dafny.DafnySequence.<__T>concatenate(dafny.DafnySequence.<__T>concatenate((xs).take(pos), dafny.DafnySequence.<__T> of(_td___T, a)), (xs).drop(pos));
  }
  public static <__T> dafny.DafnySequence<? extends __T> Reverse(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> xs)
  {
    dafny.DafnySequence<? extends __T> _0___accumulator = dafny.DafnySequence.<__T> empty(_td___T);
    TAIL_CALL_START: while (true) {
      if ((xs).equals(dafny.DafnySequence.<__T> empty(_td___T))) {
        return dafny.DafnySequence.<__T>concatenate(_0___accumulator, dafny.DafnySequence.<__T> empty(_td___T));
      } else {
        _0___accumulator = dafny.DafnySequence.<__T>concatenate(_0___accumulator, dafny.DafnySequence.<__T> of(_td___T, ((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt(((java.math.BigInteger.valueOf((xs).length())).subtract(java.math.BigInteger.ONE))))))));
        dafny.DafnySequence<? extends __T> _in0 = (xs).subsequence(dafny.Helpers.toInt((java.math.BigInteger.ZERO)), dafny.Helpers.toInt(((java.math.BigInteger.valueOf((xs).length())).subtract(java.math.BigInteger.ONE))));
        xs = _in0;
        continue TAIL_CALL_START;
      }
    }
  }
  public static <__T> dafny.DafnySequence<? extends __T> Repeat(dafny.TypeDescriptor<__T> _td___T, __T v, java.math.BigInteger length)
  {
    dafny.DafnySequence<? extends __T> _0___accumulator = dafny.DafnySequence.<__T> empty(_td___T);
    TAIL_CALL_START: while (true) {
      if ((length).signum() == 0) {
        return dafny.DafnySequence.<__T>concatenate(_0___accumulator, dafny.DafnySequence.<__T> empty(_td___T));
      } else {
        _0___accumulator = dafny.DafnySequence.<__T>concatenate(_0___accumulator, dafny.DafnySequence.<__T> of(_td___T, v));
        __T _in0 = v;
        java.math.BigInteger _in1 = (length).subtract(java.math.BigInteger.ONE);
        v = _in0;
        length = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static <__A, __B> dafny.Tuple2<dafny.DafnySequence<? extends __A>, dafny.DafnySequence<? extends __B>> Unzip(dafny.TypeDescriptor<__A> _td___A, dafny.TypeDescriptor<__B> _td___B, dafny.DafnySequence<? extends dafny.Tuple2<__A, __B>> xs)
  {
    if ((java.math.BigInteger.valueOf((xs).length())).signum() == 0) {
      return dafny.Tuple2.<dafny.DafnySequence<? extends __A>, dafny.DafnySequence<? extends __B>>create(dafny.DafnySequence.<__A> empty(_td___A), dafny.DafnySequence.<__B> empty(_td___B));
    } else {
      dafny.Tuple2<dafny.DafnySequence<? extends __A>, dafny.DafnySequence<? extends __B>> _let_tmp_rhs0 = __default.<__A, __B>Unzip(_td___A, _td___B, __default.<dafny.Tuple2<__A, __B>>DropLast(dafny.Tuple2.<__A, __B>_typeDescriptor(_td___A, _td___B), xs));
      dafny.DafnySequence<? extends __A> _0_a = ((dafny.DafnySequence<? extends __A>)(java.lang.Object)(((dafny.Tuple2<dafny.DafnySequence<? extends __A>, dafny.DafnySequence<? extends __B>>)_let_tmp_rhs0).dtor__0()));
      dafny.DafnySequence<? extends __B> _1_b = ((dafny.DafnySequence<? extends __B>)(java.lang.Object)(((dafny.Tuple2<dafny.DafnySequence<? extends __A>, dafny.DafnySequence<? extends __B>>)_let_tmp_rhs0).dtor__1()));
      return dafny.Tuple2.<dafny.DafnySequence<? extends __A>, dafny.DafnySequence<? extends __B>>create(dafny.DafnySequence.<__A>concatenate(_0_a, dafny.DafnySequence.<__A> of(_td___A, (__default.<dafny.Tuple2<__A, __B>>Last(dafny.Tuple2.<__A, __B>_typeDescriptor(_td___A, _td___B), xs)).dtor__0())), dafny.DafnySequence.<__B>concatenate(_1_b, dafny.DafnySequence.<__B> of(_td___B, (__default.<dafny.Tuple2<__A, __B>>Last(dafny.Tuple2.<__A, __B>_typeDescriptor(_td___A, _td___B), xs)).dtor__1())));
    }
  }
  public static <__A, __B> dafny.DafnySequence<? extends dafny.Tuple2<__A, __B>> Zip(dafny.TypeDescriptor<__A> _td___A, dafny.TypeDescriptor<__B> _td___B, dafny.DafnySequence<? extends __A> xs, dafny.DafnySequence<? extends __B> ys)
  {
    dafny.DafnySequence<? extends dafny.Tuple2<__A, __B>> _0___accumulator = dafny.DafnySequence.<dafny.Tuple2<__A, __B>> empty(dafny.Tuple2.<__A, __B>_typeDescriptor(_td___A, _td___B));
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((xs).length())).signum() == 0) {
        return dafny.DafnySequence.<dafny.Tuple2<__A, __B>>concatenate(dafny.DafnySequence.<dafny.Tuple2<__A, __B>> empty(dafny.Tuple2.<__A, __B>_typeDescriptor(_td___A, _td___B)), _0___accumulator);
      } else {
        _0___accumulator = dafny.DafnySequence.<dafny.Tuple2<__A, __B>>concatenate(dafny.DafnySequence.<dafny.Tuple2<__A, __B>> of(dafny.Tuple2.<__A, __B>_typeDescriptor(_td___A, _td___B), dafny.Tuple2.<__A, __B>create(__default.<__A>Last(_td___A, xs), __default.<__B>Last(_td___B, ys))), _0___accumulator);
        dafny.DafnySequence<? extends __A> _in0 = __default.<__A>DropLast(_td___A, xs);
        dafny.DafnySequence<? extends __B> _in1 = __default.<__B>DropLast(_td___B, ys);
        xs = _in0;
        ys = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static java.math.BigInteger Max(dafny.DafnySequence<? extends java.math.BigInteger> xs) {
    if (java.util.Objects.equals(java.math.BigInteger.valueOf((xs).length()), java.math.BigInteger.ONE)) {
      return ((java.math.BigInteger)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    } else {
      return Math_Compile.__default.Max(((java.math.BigInteger)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), __default.Max((xs).drop(java.math.BigInteger.ONE)));
    }
  }
  public static java.math.BigInteger Min(dafny.DafnySequence<? extends java.math.BigInteger> xs) {
    if (java.util.Objects.equals(java.math.BigInteger.valueOf((xs).length()), java.math.BigInteger.ONE)) {
      return ((java.math.BigInteger)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    } else {
      return Math_Compile.__default.Min(((java.math.BigInteger)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), __default.Min((xs).drop(java.math.BigInteger.ONE)));
    }
  }
  public static <__T> dafny.DafnySequence<? extends __T> Flatten(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends dafny.DafnySequence<? extends __T>> xs)
  {
    dafny.DafnySequence<? extends __T> _0___accumulator = dafny.DafnySequence.<__T> empty(_td___T);
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((xs).length())).signum() == 0) {
        return dafny.DafnySequence.<__T>concatenate(_0___accumulator, dafny.DafnySequence.<__T> empty(_td___T));
      } else {
        _0___accumulator = dafny.DafnySequence.<__T>concatenate(_0___accumulator, ((dafny.DafnySequence<? extends __T>)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))));
        dafny.DafnySequence<? extends dafny.DafnySequence<? extends __T>> _in0 = (xs).drop(java.math.BigInteger.ONE);
        xs = _in0;
        continue TAIL_CALL_START;
      }
    }
  }
  public static <__T> dafny.DafnySequence<? extends __T> FlattenReverse(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends dafny.DafnySequence<? extends __T>> xs)
  {
    dafny.DafnySequence<? extends __T> _0___accumulator = dafny.DafnySequence.<__T> empty(_td___T);
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((xs).length())).signum() == 0) {
        return dafny.DafnySequence.<__T>concatenate(dafny.DafnySequence.<__T> empty(_td___T), _0___accumulator);
      } else {
        _0___accumulator = dafny.DafnySequence.<__T>concatenate(__default.<dafny.DafnySequence<? extends __T>>Last(dafny.DafnySequence.<__T>_typeDescriptor(_td___T), xs), _0___accumulator);
        dafny.DafnySequence<? extends dafny.DafnySequence<? extends __T>> _in0 = __default.<dafny.DafnySequence<? extends __T>>DropLast(dafny.DafnySequence.<__T>_typeDescriptor(_td___T), xs);
        xs = _in0;
        continue TAIL_CALL_START;
      }
    }
  }
  public static <__T, __R> dafny.DafnySequence<? extends __R> Map(dafny.TypeDescriptor<__T> _td___T, dafny.TypeDescriptor<__R> _td___R, java.util.function.Function<__T, __R> f, dafny.DafnySequence<? extends __T> xs)
  {
    return dafny.DafnySequence.Create(_td___R, java.math.BigInteger.valueOf((xs).length()), ((dafny.Function2<java.util.function.Function<__T, __R>, dafny.DafnySequence<? extends __T>, java.util.function.Function<java.math.BigInteger, __R>>)(_0_f, _1_xs) -> ((java.util.function.Function<java.math.BigInteger, __R>)(_2_i_boxed0) -> {
      java.math.BigInteger _2_i = ((java.math.BigInteger)(java.lang.Object)(_2_i_boxed0));
      return ((__R)(java.lang.Object)((_0_f).apply(((__T)(java.lang.Object)((_1_xs).select(dafny.Helpers.toInt((_2_i))))))));
    })).apply(f, xs));
  }
  public static <__T, __R, __E> Wrappers_Compile.Result<dafny.DafnySequence<? extends __R>, __E> MapWithResult(dafny.TypeDescriptor<__T> _td___T, dafny.TypeDescriptor<__R> _td___R, dafny.TypeDescriptor<__E> _td___E, java.util.function.Function<__T, Wrappers_Compile.Result<__R, __E>> f, dafny.DafnySequence<? extends __T> xs)
  {
    if ((java.math.BigInteger.valueOf((xs).length())).signum() == 0) {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends __R>, __E>create_Success(dafny.DafnySequence.<__R>_typeDescriptor(_td___R), _td___E, dafny.DafnySequence.<__R> empty(_td___R));
    } else {
      Wrappers_Compile.Result<__R, __E> _0_valueOrError0 = ((Wrappers_Compile.Result<__R, __E>)(java.lang.Object)((f).apply(((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))));
      if ((_0_valueOrError0).IsFailure(_td___R, _td___E)) {
        return (_0_valueOrError0).<dafny.DafnySequence<? extends __R>>PropagateFailure(_td___R, _td___E, dafny.DafnySequence.<__R>_typeDescriptor(_td___R));
      } else {
        __R _1_head = (_0_valueOrError0).Extract(_td___R, _td___E);
        Wrappers_Compile.Result<dafny.DafnySequence<? extends __R>, __E> _2_valueOrError1 = __default.<__T, __R, __E>MapWithResult(_td___T, _td___R, _td___E, f, (xs).drop(java.math.BigInteger.ONE));
        if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<__R>_typeDescriptor(_td___R), _td___E)) {
          return (_2_valueOrError1).<dafny.DafnySequence<? extends __R>>PropagateFailure(dafny.DafnySequence.<__R>_typeDescriptor(_td___R), _td___E, dafny.DafnySequence.<__R>_typeDescriptor(_td___R));
        } else {
          dafny.DafnySequence<? extends __R> _3_tail = (_2_valueOrError1).Extract(dafny.DafnySequence.<__R>_typeDescriptor(_td___R), _td___E);
          return Wrappers_Compile.Result.<dafny.DafnySequence<? extends __R>, __E>create_Success(dafny.DafnySequence.<__R>_typeDescriptor(_td___R), _td___E, dafny.DafnySequence.<__R>concatenate(dafny.DafnySequence.<__R> of(_td___R, _1_head), _3_tail));
        }
      }
    }
  }
  public static <__T> dafny.DafnySequence<? extends __T> Filter(dafny.TypeDescriptor<__T> _td___T, java.util.function.Function<__T, Boolean> f, dafny.DafnySequence<? extends __T> xs)
  {
    dafny.DafnySequence<? extends __T> _0___accumulator = dafny.DafnySequence.<__T> empty(_td___T);
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((xs).length())).signum() == 0) {
        return dafny.DafnySequence.<__T>concatenate(_0___accumulator, dafny.DafnySequence.<__T> empty(_td___T));
      } else {
        _0___accumulator = dafny.DafnySequence.<__T>concatenate(_0___accumulator, ((((boolean)(java.lang.Object)((f).apply(((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))))) ? (dafny.DafnySequence.<__T> of(_td___T, ((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) : (dafny.DafnySequence.<__T> empty(_td___T))));
        java.util.function.Function<__T, Boolean> _in0 = f;
        dafny.DafnySequence<? extends __T> _in1 = (xs).drop(java.math.BigInteger.ONE);
        f = _in0;
        xs = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static <__A, __T> __A FoldLeft(dafny.TypeDescriptor<__A> _td___A, dafny.TypeDescriptor<__T> _td___T, dafny.Function2<__A, __T, __A> f, __A init, dafny.DafnySequence<? extends __T> xs)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((xs).length())).signum() == 0) {
        return init;
      } else {
        dafny.Function2<__A, __T, __A> _in0 = f;
        __A _in1 = ((__A)(java.lang.Object)((f).apply(init, ((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))));
        dafny.DafnySequence<? extends __T> _in2 = (xs).drop(java.math.BigInteger.ONE);
        f = _in0;
        init = _in1;
        xs = _in2;
        continue TAIL_CALL_START;
      }
    }
  }
  public static <__A, __T> __A FoldRight(dafny.TypeDescriptor<__A> _td___A, dafny.TypeDescriptor<__T> _td___T, dafny.Function2<__T, __A, __A> f, dafny.DafnySequence<? extends __T> xs, __A init)
  {
    if ((java.math.BigInteger.valueOf((xs).length())).signum() == 0) {
      return init;
    } else {
      return ((__A)(java.lang.Object)((f).apply(((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), __default.<__A, __T>FoldRight(_td___A, _td___T, f, (xs).drop(java.math.BigInteger.ONE), init))));
    }
  }
  public static <__T, __R> dafny.DafnySequence<? extends __R> FlatMap(dafny.TypeDescriptor<__T> _td___T, dafny.TypeDescriptor<__R> _td___R, java.util.function.Function<__T, dafny.DafnySequence<? extends __R>> f, dafny.DafnySequence<? extends __T> xs)
  {
    dafny.DafnySequence<? extends __R> result = dafny.DafnySequence.<__R> empty(_td___R);
    if(true) {
      result = dafny.DafnySequence.<__R> empty(_td___R);
      java.math.BigInteger _lo0 = java.math.BigInteger.ZERO;
      for (java.math.BigInteger _0_i = java.math.BigInteger.valueOf((xs).length()); _lo0.compareTo(_0_i) < 0; ) {
        _0_i = _0_i.subtract(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends __R> _1_next;
        _1_next = ((dafny.DafnySequence<? extends __R>)(java.lang.Object)((f).apply(((__T)(java.lang.Object)((xs).select(dafny.Helpers.toInt((_0_i))))))));
        result = dafny.DafnySequence.<__R>concatenate(_1_next, result);
      }
    }
    return result;
  }
  @Override
  public java.lang.String toString() {
    return "Seq._default";
  }
}
