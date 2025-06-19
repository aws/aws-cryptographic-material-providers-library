// Class __default
// Dafny class __default compiled into Java
package JSON_mUtils_mStr_mCharStrConversion_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends java.math.BigInteger> Digits(java.math.BigInteger n, java.math.BigInteger base)
  {
    if ((n).signum() == 0) {
      return dafny.DafnySequence.<java.math.BigInteger> empty(dafny.TypeDescriptor.BIG_INTEGER);
    } else {
      dafny.DafnySequence<? extends java.math.BigInteger> _0_digits_k = __default.Digits(dafny.DafnyEuclidean.EuclideanDivision(n, base), base);
      dafny.DafnySequence<? extends java.math.BigInteger> _1_digits = dafny.DafnySequence.<java.math.BigInteger>concatenate(_0_digits_k, dafny.DafnySequence.<java.math.BigInteger> of(dafny.TypeDescriptor.BIG_INTEGER, dafny.DafnyEuclidean.EuclideanModulus(n, base)));
      return _1_digits;
    }
  }
  public static dafny.DafnySequence<? extends Character> OfDigits(dafny.DafnySequence<? extends java.math.BigInteger> digits, dafny.DafnySequence<? extends Character> chars)
  {
    dafny.DafnySequence<? extends Character> _0___accumulator = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    TAIL_CALL_START: while (true) {
      if ((digits).equals(dafny.DafnySequence.<java.math.BigInteger> empty(dafny.TypeDescriptor.BIG_INTEGER))) {
        return dafny.DafnySequence.<Character>concatenate(_0___accumulator, dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
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
  public static dafny.DafnySequence<? extends Character> OfNat__any(java.math.BigInteger n, dafny.DafnySequence<? extends Character> chars)
  {
    java.math.BigInteger _0_base = java.math.BigInteger.valueOf((chars).length());
    if ((n).signum() == 0) {
      return dafny.DafnySequence.<Character> of(((char)(java.lang.Object)((chars).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))));
    } else {
      return __default.OfDigits(__default.Digits(n, _0_base), chars);
    }
  }
  public static boolean NumberStr(dafny.DafnySequence<? extends Character> str, char minus, java.util.function.Function<Character, Boolean> is__digit)
  {
    return !(!(str).equals(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR))) || ((((((char)(java.lang.Object)((str).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) == (minus)) || (((boolean)(java.lang.Object)((is__digit).apply(((char)(java.lang.Object)((str).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))))))) && (((dafny.Function2<dafny.DafnySequence<? extends Character>, java.util.function.Function<Character, Boolean>, Boolean>)(_0_str, _1_is__digit) -> dafny.Helpers.Quantifier(((_0_str).drop(java.math.BigInteger.ONE)).UniqueElements(), true, ((_forall_var_0_boxed0) -> {
      char _forall_var_0 = ((char)(java.lang.Object)(_forall_var_0_boxed0));
      char _2_c = (char)_forall_var_0;
      return !(((_0_str).drop(java.math.BigInteger.ONE)).contains(_2_c)) || (((boolean)(java.lang.Object)((_1_is__digit).apply(_2_c))));
    }))).apply(str, is__digit)));
  }
  public static dafny.DafnySequence<? extends Character> OfInt__any(java.math.BigInteger n, dafny.DafnySequence<? extends Character> chars, char minus)
  {
    if ((n).signum() != -1) {
      return __default.OfNat__any(n, chars);
    } else {
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character> of(minus), __default.OfNat__any((java.math.BigInteger.ZERO).subtract(n), chars));
    }
  }
  public static java.math.BigInteger ToNat__any(dafny.DafnySequence<? extends Character> str, java.math.BigInteger base, dafny.DafnyMap<? extends Character, ? extends java.math.BigInteger> digits)
  {
    if ((str).equals(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR))) {
      return java.math.BigInteger.ZERO;
    } else {
      return ((__default.ToNat__any((str).take((java.math.BigInteger.valueOf((str).length())).subtract(java.math.BigInteger.ONE)), base, digits)).multiply(base)).add(((java.math.BigInteger)(java.lang.Object)((digits).get(((char)(java.lang.Object)((str).select(dafny.Helpers.toInt(((java.math.BigInteger.valueOf((str).length())).subtract(java.math.BigInteger.ONE))))))))));
    }
  }
  public static java.math.BigInteger ToInt__any(dafny.DafnySequence<? extends Character> str, char minus, java.math.BigInteger base, dafny.DafnyMap<? extends Character, ? extends java.math.BigInteger> digits)
  {
    if ((dafny.DafnySequence.<Character> of(minus)).isPrefixOf(str)) {
      return (java.math.BigInteger.ZERO).subtract(__default.ToNat__any((str).drop(java.math.BigInteger.ONE), base, digits));
    } else {
      return __default.ToNat__any(str, base, digits);
    }
  }
  @Override
  public java.lang.String toString() {
    return "JSON.Utils.Str.CharStrConversion._default";
  }
}
