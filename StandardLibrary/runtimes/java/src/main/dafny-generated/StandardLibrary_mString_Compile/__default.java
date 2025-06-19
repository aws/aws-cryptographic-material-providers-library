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
  public static dafny.DafnySequence<? extends Character> Base10()
  {
    return dafny.DafnySequence.<Character> of('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');
  }
  @Override
  public java.lang.String toString() {
    return "StandardLibrary.String._default";
  }
}
