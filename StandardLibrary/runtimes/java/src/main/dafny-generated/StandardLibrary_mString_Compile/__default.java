// Class __default
// Dafny class __default compiled into Java
package StandardLibrary_mString_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends java.math.BigInteger> Int2Digits(java.math.BigInteger n, java.math.BigInteger base)
  {
    dafny.DafnySequence<? extends java.math.BigInteger> _0___accumulator = dafny.DafnySequence.<java.math.BigInteger> empty(dafny.TypeDescriptor.BIG_INTEGER);
    TAIL_CALL_START: while (true) {
      if ((n).signum() == 0) {
        return dafny.DafnySequence.<java.math.BigInteger>concatenate(dafny.DafnySequence.<java.math.BigInteger> empty(dafny.TypeDescriptor.BIG_INTEGER), _0___accumulator);
      } else {
        _0___accumulator = dafny.DafnySequence.<java.math.BigInteger>concatenate(dafny.DafnySequence.<java.math.BigInteger> of(dafny.TypeDescriptor.BIG_INTEGER, dafny.DafnyEuclidean.EuclideanModulus(n, base)), _0___accumulator);
        java.math.BigInteger _in0 = dafny.DafnyEuclidean.EuclideanDivision(n, base);
        java.math.BigInteger _in1 = base;
        n = _in0;
        base = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> Digits2String(dafny.DafnySequence<? extends java.math.BigInteger> digits, dafny.DafnySequence<? extends Character> chars)
  {
    dafny.DafnySequence<? extends Character> _0___accumulator = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    TAIL_CALL_START: while (true) {
      if ((digits).equals(dafny.DafnySequence.<java.math.BigInteger> empty(dafny.TypeDescriptor.BIG_INTEGER))) {
        return dafny.DafnySequence.<Character>concatenate(_0___accumulator, dafny.DafnySequence.asString(""));
      } else {
        _0___accumulator = dafny.DafnySequence.<Character>concatenate(_0___accumulator, dafny.DafnySequence.<Character> of(((char)(java.lang.Object)((chars).select(dafny.Helpers.toInt((((java.math.BigInteger)(java.lang.Object)((digits).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))))))));
        dafny.DafnySequence<? extends java.math.BigInteger> _in0 = (digits).drop(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends Character> _in1 = chars;
        digits = _in0;
        chars = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> Int2String(java.math.BigInteger n, dafny.DafnySequence<? extends Character> chars)
  {
    java.math.BigInteger _0_base = java.math.BigInteger.valueOf((chars).length());
    if ((n).signum() == 0) {
      return dafny.DafnySequence.asString("0");
    } else if ((n).signum() == 1) {
      return __default.Digits2String(__default.Int2Digits(n, _0_base), chars);
    } else {
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("-"), __default.Digits2String(__default.Int2Digits((java.math.BigInteger.ZERO).subtract(n), _0_base), chars));
    }
  }
  public static dafny.DafnySequence<? extends Character> Base10Int2String(java.math.BigInteger n) {
    return __default.Int2String(n, __default.Base10());
  }
  public static <__T> dafny.DafnySequence<? extends __T> SearchAndReplace(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> source, dafny.DafnySequence<? extends __T> old__str, dafny.DafnySequence<? extends __T> new__str)
  {
    dafny.DafnySequence<? extends __T> o = dafny.DafnySequence.<__T> empty(_td___T);
    dafny.Tuple2<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>> _0_x;
    dafny.Tuple2<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>> _out0;
    _out0 = __default.<__T>SearchAndReplacePos(_td___T, source, old__str, new__str, (long) 0L);
    _0_x = _out0;
    o = (_0_x).dtor__0();
    return o;
  }
  public static <__T> dafny.Tuple2<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>> SearchAndReplacePos(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> source, dafny.DafnySequence<? extends __T> old__str, dafny.DafnySequence<? extends __T> new__str, long pos)
  {
    dafny.Tuple2<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>> o = dafny.Tuple2.<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>>Default(dafny.DafnySequence.<__T> empty(_td___T), Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.uint64._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Option<java.lang.Long> _0_old__pos;
      Wrappers_Compile.Option<java.lang.Long> _out0;
      _out0 = __default.<__T>HasSubStringPos(_td___T, source, old__str, pos);
      _0_old__pos = _out0;
      if ((_0_old__pos).is_None()) {
        o = dafny.Tuple2.<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>>create(source, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.uint64._typeDescriptor()));
        return o;
      } else {
        long _1_source__len;
        _1_source__len = (long) (source).cardinalityInt();
        long _2_old__str__len;
        _2_old__str__len = (long) (old__str).cardinalityInt();
        long _3_new__str__len;
        _3_new__str__len = (long) (new__str).cardinalityInt();
        o = dafny.Tuple2.<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>>create(dafny.DafnySequence.<__T>concatenate(dafny.DafnySequence.<__T>concatenate((source).take((_0_old__pos).dtor_value()), new__str), (source).drop((long) (long) (((_0_old__pos).dtor_value()) + (_2_old__str__len)))), Wrappers_Compile.Option.<java.lang.Long>create_Some(BoundedInts_Compile.uint64._typeDescriptor(), StandardLibrary_mMemoryMath_Compile.__default.Add((_0_old__pos).dtor_value(), _3_new__str__len)));
        o = o;
        return o;
      }
    }
    return o;
  }
  public static <__T> boolean BadStart(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> source, long pos, dafny.DafnySequence<? extends __T> chars)
  {
    if (((pos) == 0 ? 0 : 1) == 0) {
      return false;
    } else {
      return (chars).contains(((__T)(java.lang.Object)((source).select(dafny.Helpers.unsignedToInt((long) (long) ((pos) - ((long) 1L)))))));
    }
  }
  public static <__T> boolean BadEnd(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> source, long pos, long match__len, dafny.DafnySequence<? extends __T> chars)
  {
    long _0_source__len = (long) (source).cardinalityInt();
    if (java.lang.Long.compareUnsigned(StandardLibrary_mMemoryMath_Compile.__default.Add(pos, match__len), _0_source__len) >= 0) {
      return false;
    } else {
      return (chars).contains(((__T)(java.lang.Object)((source).select(dafny.Helpers.unsignedToInt((long) (long) ((pos) + (match__len)))))));
    }
  }
  public static <__T> boolean BadMatch(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> source, long pos, long match__len, dafny.DafnySequence<? extends __T> chars)
  {
    return (__default.<__T>BadStart(_td___T, source, pos, chars)) || (__default.<__T>BadEnd(_td___T, source, pos, match__len, chars));
  }
  public static <__T> dafny.Tuple2<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>> SearchAndReplacePosWhole(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> source, dafny.DafnySequence<? extends __T> old__str, dafny.DafnySequence<? extends __T> new__str, long xpos, dafny.DafnySequence<? extends __T> chars)
  {
    dafny.Tuple2<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>> o = dafny.Tuple2.<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>>Default(dafny.DafnySequence.<__T> empty(_td___T), Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.uint64._typeDescriptor()));
    long _0_old__str__len;
    _0_old__str__len = (long) (old__str).cardinalityInt();
    long _1_pos;
    _1_pos = xpos;
    while (java.lang.Long.compareUnsigned(_1_pos, (long) (source).cardinalityInt()) < 0) {
      Wrappers_Compile.Option<java.lang.Long> _2_old__pos;
      Wrappers_Compile.Option<java.lang.Long> _out0;
      _out0 = __default.<__T>HasSubStringPos(_td___T, source, old__str, _1_pos);
      _2_old__pos = _out0;
      if ((_2_old__pos).is_None()) {
        o = dafny.Tuple2.<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>>create(source, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.uint64._typeDescriptor()));
        return o;
      } else if (__default.<__T>BadMatch(_td___T, source, (_2_old__pos).dtor_value(), _0_old__str__len, chars)) {
        _1_pos = (long) (long) (((_2_old__pos).dtor_value()) + ((long) 1L));
      } else {
        long _3_source__len;
        _3_source__len = (long) (source).cardinalityInt();
        long _4_new__str__len;
        _4_new__str__len = (long) (new__str).cardinalityInt();
        o = dafny.Tuple2.<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>>create(dafny.DafnySequence.<__T>concatenate(dafny.DafnySequence.<__T>concatenate((source).take((_2_old__pos).dtor_value()), new__str), (source).drop((long) (long) (((_2_old__pos).dtor_value()) + (_0_old__str__len)))), Wrappers_Compile.Option.<java.lang.Long>create_Some(BoundedInts_Compile.uint64._typeDescriptor(), StandardLibrary_mMemoryMath_Compile.__default.Add((_2_old__pos).dtor_value(), _4_new__str__len)));
        o = o;
        return o;
      }
    }
    o = dafny.Tuple2.<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>>create(source, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.uint64._typeDescriptor()));
    return o;
  }
  public static <__T> dafny.Tuple2<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>> SearchAndReplaceWhole(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> source, dafny.DafnySequence<? extends __T> old__str, dafny.DafnySequence<? extends __T> new__str, dafny.DafnySequence<? extends __T> chars)
  {
    dafny.Tuple2<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>> o = dafny.Tuple2.<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>>Default(dafny.DafnySequence.<__T> empty(_td___T), Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.uint64._typeDescriptor()));
    if(true) {
      dafny.Tuple2<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>> _out0;
      _out0 = __default.<__T>SearchAndReplacePosWhole(_td___T, source, old__str, new__str, (long) 0L, chars);
      o = _out0;
    }
    return o;
  }
  public static <__T> dafny.DafnySequence<? extends __T> SearchAndReplaceAll(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> source__in, dafny.DafnySequence<? extends __T> old__str, dafny.DafnySequence<? extends __T> new__str)
  {
    dafny.DafnySequence<? extends __T> o = dafny.DafnySequence.<__T> empty(_td___T);
    if(true) {
      long _0_pos;
      _0_pos = (long) 0L;
      dafny.DafnySequence<? extends __T> _1_source;
      _1_source = source__in;
      while (true) {
        dafny.Tuple2<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>> _2_res;
        dafny.Tuple2<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>> _out0;
        _out0 = __default.<__T>SearchAndReplacePos(_td___T, _1_source, old__str, new__str, _0_pos);
        _2_res = _out0;
        if (((_2_res).dtor__1()).is_None()) {
          _0_pos = (long) (_1_source).cardinalityInt();
          o = (_2_res).dtor__0();
          return o;
        }
        _1_source = (_2_res).dtor__0();
        _0_pos = ((_2_res).dtor__1()).dtor_value();
      }
    }
    return o;
  }
  public static <__T> dafny.DafnySequence<? extends __T> SearchAndReplaceAllWhole(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> source__in, dafny.DafnySequence<? extends __T> old__str, dafny.DafnySequence<? extends __T> new__str, dafny.DafnySequence<? extends __T> chars)
  {
    dafny.DafnySequence<? extends __T> o = dafny.DafnySequence.<__T> empty(_td___T);
    if(true) {
      long _0_pos;
      _0_pos = (long) 0L;
      dafny.DafnySequence<? extends __T> _1_source;
      _1_source = source__in;
      while (true) {
        dafny.Tuple2<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>> _2_res;
        dafny.Tuple2<dafny.DafnySequence<? extends __T>, Wrappers_Compile.Option<java.lang.Long>> _out0;
        _out0 = __default.<__T>SearchAndReplacePosWhole(_td___T, _1_source, old__str, new__str, _0_pos, chars);
        _2_res = _out0;
        if (((_2_res).dtor__1()).is_None()) {
          _0_pos = (long) (_1_source).cardinalityInt();
          o = (_2_res).dtor__0();
          return o;
        }
        _1_source = (_2_res).dtor__0();
        _0_pos = ((_2_res).dtor__1()).dtor_value();
      }
    }
    return o;
  }
  public static <__T> Wrappers_Compile.Option<java.math.BigInteger> HasSubString(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> haystack, dafny.DafnySequence<? extends __T> needle)
  {
    Wrappers_Compile.Option<java.math.BigInteger> o = Wrappers_Compile.Option.<java.math.BigInteger>Default(_System.nat._typeDescriptor());
    if (java.lang.Long.compareUnsigned((long) (haystack).cardinalityInt(), (long) (needle).cardinalityInt()) < 0) {
      o = Wrappers_Compile.Option.<java.math.BigInteger>create_None(_System.nat._typeDescriptor());
      return o;
    }
    long _0_size;
    _0_size = (long) (needle).cardinalityInt();
    long _1_limit;
    _1_limit = StandardLibrary_mMemoryMath_Compile.__default.Add((long) (long) (((long) (haystack).cardinalityInt()) - (_0_size)), (long) 1L);
    long _hi0 = _1_limit;
    for (long _2_index = (long) 0L; java.lang.Long.compareUnsigned(_2_index, _hi0) < 0; _2_index++) {
      if (StandardLibrary_mSequence_Compile.__default.<__T>SequenceEqual(_td___T, haystack, needle, _2_index, (long) 0L, _0_size)) {
        o = Wrappers_Compile.Option.<java.math.BigInteger>create_Some(_System.nat._typeDescriptor(), dafny.Helpers.unsignedToBigInteger(_2_index));
        return o;
      }
    }
    o = Wrappers_Compile.Option.<java.math.BigInteger>create_None(_System.nat._typeDescriptor());
    return o;
  }
  public static <__T> Wrappers_Compile.Option<java.lang.Long> HasSubStringPos(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> haystack, dafny.DafnySequence<? extends __T> needle, long pos)
  {
    Wrappers_Compile.Option<java.lang.Long> o = Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.uint64._typeDescriptor());
    if (java.lang.Long.compareUnsigned((long) (long) (((long) (haystack).cardinalityInt()) - (pos)), (long) (needle).cardinalityInt()) < 0) {
      o = Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.uint64._typeDescriptor());
      return o;
    }
    long _0_size;
    _0_size = (long) (needle).cardinalityInt();
    long _1_limit;
    _1_limit = StandardLibrary_mMemoryMath_Compile.__default.Add((long) (long) (((long) (haystack).cardinalityInt()) - (_0_size)), (long) 1L);
    long _hi0 = _1_limit;
    for (long _2_index = pos; java.lang.Long.compareUnsigned(_2_index, _hi0) < 0; _2_index++) {
      if (StandardLibrary_mSequence_Compile.__default.<__T>SequenceEqual(_td___T, haystack, needle, _2_index, (long) 0L, _0_size)) {
        o = Wrappers_Compile.Option.<java.lang.Long>create_Some(BoundedInts_Compile.uint64._typeDescriptor(), _2_index);
        return o;
      }
    }
    o = Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.uint64._typeDescriptor());
    return o;
  }
  public static dafny.DafnySequence<? extends Character> Base10()
  {
    return dafny.DafnySequence.<Character> of('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');
  }
  public static dafny.DafnySequence<? extends Character> AlphaNumeric()
  {
    return dafny.DafnySequence.asString("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789");
  }
  public static dafny.DafnySequence<? extends Character> AlphaNumericUnder()
  {
    return dafny.DafnySequence.asString("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_");
  }
  @Override
  public java.lang.String toString() {
    return "StandardLibrary.String._default";
  }
}
