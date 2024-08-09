package String_Compile;

/**
 * This is a thunk for the actual Dafny-generated StandardLibrary_mString_Compile.__default class.
 * 
 * The module names generated for Java changed between Dafny 4.2 and 4.7,
 * and although `--legacy-module-names` mostly retains the old names,
 * StandardLibrary.String was previously compiled to String_Compile instead of the expected
 * StandardLibrary_mString_Compile because of a bug,
 * and it would have been very difficult to reproduce the exact bug behavior with `--legacy-module-names`.
 * 
 * Instead we just create an "alias" for this case.
 */
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends java.math.BigInteger> Int2Digits(java.math.BigInteger n, java.math.BigInteger base)
  {
    return StandardLibrary_mString_Compile.__default.Int2Digits(n, base);
  }
  public static dafny.DafnySequence<? extends Character> Digits2String(dafny.DafnySequence<? extends java.math.BigInteger> digits, dafny.DafnySequence<? extends Character> chars)
  {
    return StandardLibrary_mString_Compile.__default.Digits2String(digits, chars);
  }
  public static dafny.DafnySequence<? extends Character> Int2String(java.math.BigInteger n, dafny.DafnySequence<? extends Character> chars)
  {
    return StandardLibrary_mString_Compile.__default.Int2String(n, chars);
  }
  public static dafny.DafnySequence<? extends Character> Base10Int2String(java.math.BigInteger n)
  {
    return StandardLibrary_mString_Compile.__default.Base10Int2String(n);
  }
  public static dafny.DafnySequence<? extends Character> Base10()
  {
    return StandardLibrary_mString_Compile.__default.Base10();
  }
}
