// Class __default
// Dafny class __default compiled into Java
package StandardLibrary_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static <__T> dafny.DafnySequence<? extends __T> Join(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends dafny.DafnySequence<? extends __T>> ss, dafny.DafnySequence<? extends __T> joiner)
  {
    dafny.DafnySequence<? extends __T> s = dafny.DafnySequence.<__T> empty(_td___T);
    long _0_size;
    _0_size = (long) (ss).cardinalityInt();
    dafny.DafnySequence<? extends __T> _1_result;
    _1_result = ((dafny.DafnySequence<? extends __T>)(java.lang.Object)((ss).select(dafny.Helpers.unsignedToInt((long) (long) ((_0_size) - ((long) 1L))))));
    long _2_i;
    _2_i = (long) (long) ((_0_size) - ((long) 1L));
    while (((_2_i) == 0 ? 0 : 1) == 1) {
      _2_i = (long) (long) ((_2_i) - ((long) 1L));
      _1_result = dafny.DafnySequence.<__T>concatenate(dafny.DafnySequence.<__T>concatenate(((dafny.DafnySequence<? extends __T>)(java.lang.Object)((ss).select(dafny.Helpers.unsignedToInt(_2_i)))), joiner), _1_result);
    }
    s = _1_result;
    return s;
  }
  public static <__T> dafny.DafnySequence<? extends dafny.DafnySequence<? extends __T>> Split(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> s, __T delim)
  {
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends __T>> _0___accumulator = dafny.DafnySequence.<dafny.DafnySequence<? extends __T>> empty(dafny.DafnySequence.<__T>_typeDescriptor(_td___T));
    TAIL_CALL_START: while (true) {
      Wrappers_Compile.Option<java.lang.Long> _1_i = __default.<__T>FindIndexMatching(_td___T, s, delim, (long) 0L);
      if ((_1_i).is_Some()) {
        _0___accumulator = dafny.DafnySequence.<dafny.DafnySequence<? extends __T>>concatenate(_0___accumulator, dafny.DafnySequence.<dafny.DafnySequence<? extends __T>> of(dafny.DafnySequence.<__T>_typeDescriptor(_td___T), (s).take((_1_i).dtor_value())));
        dafny.DafnySequence<? extends __T> _in0 = (s).drop(StandardLibrary_mMemoryMath_Compile.__default.Add((_1_i).dtor_value(), (long) 1L));
        __T _in1 = delim;
        s = _in0;
        delim = _in1;
        continue TAIL_CALL_START;
      } else {
        return dafny.DafnySequence.<dafny.DafnySequence<? extends __T>>concatenate(_0___accumulator, dafny.DafnySequence.<dafny.DafnySequence<? extends __T>> of(dafny.DafnySequence.<__T>_typeDescriptor(_td___T), s));
      }
    }
  }
  public static <__T> dafny.Tuple2<dafny.DafnySequence<? extends __T>, dafny.DafnySequence<? extends __T>> SplitOnce(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> s, __T delim)
  {
    Wrappers_Compile.Option<java.lang.Long> _0_i = __default.<__T>FindIndexMatching(_td___T, s, delim, (long) 0L);
    return dafny.Tuple2.<dafny.DafnySequence<? extends __T>, dafny.DafnySequence<? extends __T>>create((s).take((_0_i).dtor_value()), (s).drop(StandardLibrary_mMemoryMath_Compile.__default.Add((_0_i).dtor_value(), (long) 1L)));
  }
  public static <__T> Wrappers_Compile.Option<dafny.Tuple2<dafny.DafnySequence<? extends __T>, dafny.DafnySequence<? extends __T>>> SplitOnce_q(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> s, __T delim)
  {
    Wrappers_Compile.Option<java.lang.Long> _0_valueOrError0 = __default.<__T>FindIndexMatching(_td___T, s, delim, (long) 0L);
    if ((_0_valueOrError0).IsFailure(BoundedInts_Compile.uint64._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.Tuple2<dafny.DafnySequence<? extends __T>, dafny.DafnySequence<? extends __T>>>PropagateFailure(BoundedInts_Compile.uint64._typeDescriptor(), dafny.Tuple2.<dafny.DafnySequence<? extends __T>, dafny.DafnySequence<? extends __T>>_typeDescriptor(dafny.DafnySequence.<__T>_typeDescriptor(_td___T), dafny.DafnySequence.<__T>_typeDescriptor(_td___T)));
    } else {
      long _1_i = (_0_valueOrError0).Extract(BoundedInts_Compile.uint64._typeDescriptor());
      return Wrappers_Compile.Option.<dafny.Tuple2<dafny.DafnySequence<? extends __T>, dafny.DafnySequence<? extends __T>>>create_Some(dafny.Tuple2.<dafny.DafnySequence<? extends __T>, dafny.DafnySequence<? extends __T>>_typeDescriptor(dafny.DafnySequence.<__T>_typeDescriptor(_td___T), dafny.DafnySequence.<__T>_typeDescriptor(_td___T)), dafny.Tuple2.<dafny.DafnySequence<? extends __T>, dafny.DafnySequence<? extends __T>>create((s).take(_1_i), (s).drop(StandardLibrary_mMemoryMath_Compile.__default.Add(_1_i, (long) 1L))));
    }
  }
  public static <__T> Wrappers_Compile.Option<java.lang.Long> FindIndexMatching(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> s, __T c, long i)
  {
    return __default.<__T>FindIndex(_td___T, s, ((java.util.function.Function<__T, java.util.function.Function<__T, Boolean>>)(_0_c) -> ((java.util.function.Function<__T, Boolean>)(_1_x_boxed0) -> {
      __T _1_x = ((__T)(java.lang.Object)(_1_x_boxed0));
      return java.util.Objects.equals(_1_x, _0_c);
    })).apply(c), i);
  }
  public static <__T> Wrappers_Compile.Option<java.lang.Long> FindIndex(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> s, java.util.function.Function<__T, Boolean> f, long i)
  {
    TAIL_CALL_START: while (true) {
      if ((i) == ((long) (s).cardinalityInt())) {
        return Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.uint64._typeDescriptor());
      } else if (((boolean)(java.lang.Object)((f).apply(((__T)(java.lang.Object)((s).select(dafny.Helpers.unsignedToInt(i)))))))) {
        return Wrappers_Compile.Option.<java.lang.Long>create_Some(BoundedInts_Compile.uint64._typeDescriptor(), i);
      } else {
        dafny.DafnySequence<? extends __T> _in0 = s;
        java.util.function.Function<__T, Boolean> _in1 = f;
        long _in2 = (long) (long) ((i) + ((long) 1L));
        s = _in0;
        f = _in1;
        i = _in2;
        continue TAIL_CALL_START;
      }
    }
  }
  public static <__T> dafny.DafnySequence<? extends __T> Filter(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> s, java.util.function.Function<__T, Boolean> f)
  {
    dafny.DafnySequence<? extends __T> res = dafny.DafnySequence.<__T> empty(_td___T);
    dafny.DafnySequence<? extends __T> _0_result;
    _0_result = dafny.DafnySequence.<__T> empty(_td___T);
    long _1_i;
    _1_i = (long) (s).cardinalityInt();
    while (((_1_i) == 0 ? 0 : 1) == 1) {
      _1_i = (long) (long) ((_1_i) - ((long) 1L));
      if (((boolean)(java.lang.Object)((f).apply(((__T)(java.lang.Object)((s).select(dafny.Helpers.unsignedToInt(_1_i)))))))) {
        _0_result = dafny.DafnySequence.<__T>concatenate(dafny.DafnySequence.<__T> of(_td___T, ((__T)(java.lang.Object)((s).select(dafny.Helpers.unsignedToInt(_1_i))))), _0_result);
      }
    }
    res = _0_result;
    return res;
  }
  public static java.math.BigInteger Min(java.math.BigInteger a, java.math.BigInteger b)
  {
    if ((a).compareTo(b) < 0) {
      return a;
    } else {
      return b;
    }
  }
  public static <__T> dafny.DafnySequence<? extends __T> Fill(dafny.TypeDescriptor<__T> _td___T, __T value, java.math.BigInteger n)
  {
    return dafny.DafnySequence.Create(_td___T, n, ((java.util.function.Function<__T, java.util.function.Function<java.math.BigInteger, __T>>)(_0_value) -> ((java.util.function.Function<java.math.BigInteger, __T>)(_1___v0_boxed0) -> {
      java.math.BigInteger _1___v0 = ((java.math.BigInteger)(java.lang.Object)(_1___v0_boxed0));
      return _0_value;
    })).apply(value));
  }
  public static <__T> java.lang.Object SeqToArray(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> s)
  {
    java.lang.Object a = (java.lang.Object)_td___T.newArray(0);
    if(true) {
      java.util.function.Function<java.math.BigInteger, __T> _init0 = ((java.util.function.Function<dafny.DafnySequence<? extends __T>, java.util.function.Function<java.math.BigInteger, __T>>)(_0_s) -> ((java.util.function.Function<java.math.BigInteger, __T>)(_1_i_boxed0) -> {
        java.math.BigInteger _1_i = ((java.math.BigInteger)(java.lang.Object)(_1_i_boxed0));
        return ((__T)(java.lang.Object)((_0_s).select(dafny.Helpers.toInt((_1_i)))));
      })).apply(s);
      java.lang.Object _nw0 = (java.lang.Object) _td___T.newArray(dafny.Helpers.toIntChecked((java.math.BigInteger.valueOf((s).length())), "Java arrays may be no larger than the maximum 32-bit signed int"));
      for (java.math.BigInteger _i0_0 = java.math.BigInteger.ZERO; _i0_0.compareTo(java.math.BigInteger.valueOf(java.lang.reflect.Array.getLength(_nw0))) < 0; _i0_0 = _i0_0.add(java.math.BigInteger.ONE)) {
        _td___T.setArrayElement(_nw0, dafny.Helpers.toInt(_i0_0), ((__T)(java.lang.Object)(_init0.apply(_i0_0))));
      }
      a = _nw0;
    }
    return a;
  }
  public static <__T> boolean LexicographicLessOrEqual(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> a, dafny.DafnySequence<? extends __T> b, dafny.Function2<__T, __T, Boolean> less)
  {
    return ((dafny.Function3<dafny.DafnySequence<? extends __T>, dafny.DafnySequence<? extends __T>, dafny.Function2<__T, __T, Boolean>, Boolean>)(_0_a, _1_b, _2_less) -> dafny.Helpers.Quantifier(dafny.Helpers.IntegerRange(java.math.BigInteger.ZERO, (java.math.BigInteger.valueOf((_0_a).length())).add(java.math.BigInteger.ONE)), false, ((_exists_var_0_boxed0) -> {
      java.math.BigInteger _exists_var_0 = ((java.math.BigInteger)(java.lang.Object)(_exists_var_0_boxed0));
      java.math.BigInteger _3_k = (java.math.BigInteger)_exists_var_0;
      return (((_3_k).signum() != -1) && ((_3_k).compareTo(java.math.BigInteger.valueOf((_0_a).length())) <= 0)) && (__default.<__T>LexicographicLessOrEqualAux(_td___T, _0_a, _1_b, _2_less, _3_k));
    }))).apply(a, b, less);
  }
  public static <__T> boolean LexicographicLessOrEqualAux(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> a, dafny.DafnySequence<? extends __T> b, dafny.Function2<__T, __T, Boolean> less, java.math.BigInteger lengthOfCommonPrefix)
  {
    return (((lengthOfCommonPrefix).compareTo(java.math.BigInteger.valueOf((b).length())) <= 0) && (((dafny.Function3<java.math.BigInteger, dafny.DafnySequence<? extends __T>, dafny.DafnySequence<? extends __T>, Boolean>)(_0_lengthOfCommonPrefix, _1_a, _2_b) -> dafny.Helpers.Quantifier(dafny.Helpers.IntegerRange(java.math.BigInteger.ZERO, _0_lengthOfCommonPrefix), true, ((_forall_var_0_boxed0) -> {
      java.math.BigInteger _forall_var_0 = ((java.math.BigInteger)(java.lang.Object)(_forall_var_0_boxed0));
      java.math.BigInteger _3_i = (java.math.BigInteger)_forall_var_0;
      return !(((_3_i).signum() != -1) && ((_3_i).compareTo(_0_lengthOfCommonPrefix) < 0)) || (java.util.Objects.equals(((__T)(java.lang.Object)((_1_a).select(dafny.Helpers.toInt((_3_i))))), ((__T)(java.lang.Object)((_2_b).select(dafny.Helpers.toInt((_3_i)))))));
    }))).apply(lengthOfCommonPrefix, a, b))) && ((java.util.Objects.equals(lengthOfCommonPrefix, java.math.BigInteger.valueOf((a).length()))) || (((lengthOfCommonPrefix).compareTo(java.math.BigInteger.valueOf((b).length())) < 0) && (((boolean)(java.lang.Object)((less).apply(((__T)(java.lang.Object)((a).select(dafny.Helpers.toInt((lengthOfCommonPrefix))))), ((__T)(java.lang.Object)((b).select(dafny.Helpers.toInt((lengthOfCommonPrefix)))))))))));
  }
  public static <__T> boolean IsMinimum(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> a, dafny.DafnySet<? extends dafny.DafnySequence<? extends __T>> s, dafny.Function2<__T, __T, Boolean> less)
  {
    return ((s).<dafny.DafnySequence<? extends __T>>contains(a)) && (((dafny.Function3<dafny.DafnySet<? extends dafny.DafnySequence<? extends __T>>, dafny.DafnySequence<? extends __T>, dafny.Function2<__T, __T, Boolean>, Boolean>)(_0_s, _1_a, _2_less) -> dafny.Helpers.Quantifier((_0_s).Elements(), true, ((_forall_var_0_boxed0) -> {
      dafny.DafnySequence<? extends __T> _forall_var_0 = ((dafny.DafnySequence<? extends __T>)(java.lang.Object)(_forall_var_0_boxed0));
      dafny.DafnySequence<? extends __T> _3_z = (dafny.DafnySequence<? extends __T>)_forall_var_0;
      return !((_0_s).<dafny.DafnySequence<? extends __T>>contains(_3_z)) || (__default.<__T>LexicographicLessOrEqual(_td___T, _1_a, _3_z, _2_less));
    }))).apply(s, a, less));
  }
  @Override
  public java.lang.String toString() {
    return "StandardLibrary._default";
  }
}
