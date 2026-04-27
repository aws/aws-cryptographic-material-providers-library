// Class __default
// Dafny class __default compiled into Java
package HexStrings_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static char HexChar(byte x) {
    if (java.lang.Integer.compareUnsigned(x, (byte) 10) < 0) {
      return (char) (('0') + ((char)java.lang.Byte.toUnsignedInt(x)));
    } else {
      return (char) (('a') + ((char)java.lang.Byte.toUnsignedInt((byte) (byte) ((byte)((x) - ((byte) 10))))));
    }
  }
  public static boolean IsLooseHexChar(char ch) {
    return (((('0') <= (ch)) && ((ch) <= ('9'))) || ((('a') <= (ch)) && ((ch) <= ('f')))) || ((('A') <= (ch)) && ((ch) <= ('F')));
  }
  public static boolean IsHexChar(char ch) {
    return ((('0') <= (ch)) && ((ch) <= ('9'))) || ((('a') <= (ch)) && ((ch) <= ('f')));
  }
  public static boolean IsHexString(dafny.DafnySequence<? extends Character> s) {
    return ((java.util.function.Function<dafny.DafnySequence<? extends Character>, Boolean>)(_0_s) -> dafny.Helpers.Quantifier((_0_s).UniqueElements(), true, ((_forall_var_0_boxed0) -> {
      char _forall_var_0 = ((char)(java.lang.Object)(_forall_var_0_boxed0));
      char _1_ch = (char)_forall_var_0;
      return !((_0_s).contains(_1_ch)) || (__default.IsHexChar(_1_ch));
    }))).apply(s);
  }
  public static boolean IsLooseHexString(dafny.DafnySequence<? extends Character> s) {
    return ((java.util.function.Function<dafny.DafnySequence<? extends Character>, Boolean>)(_0_s) -> dafny.Helpers.Quantifier((_0_s).UniqueElements(), true, ((_forall_var_0_boxed0) -> {
      char _forall_var_0 = ((char)(java.lang.Object)(_forall_var_0_boxed0));
      char _1_ch = (char)_forall_var_0;
      return !((_0_s).contains(_1_ch)) || (__default.IsLooseHexChar(_1_ch));
    }))).apply(s);
  }
  public static byte HexVal(char ch) {
    if ((('0') <= (ch)) && ((ch) <= ('9'))) {
      return (byte) (byte) ((byte)((((byte) (ch))) - (((byte) ('0')))));
    } else if ((('a') <= (ch)) && ((ch) <= ('f'))) {
      return (byte) (byte) ((byte)(((byte) (byte) ((byte)((((byte) (ch))) - (((byte) ('a')))))) + ((byte) 10)));
    } else {
      return (byte) (byte) ((byte)(((byte) (byte) ((byte)((((byte) (ch))) - (((byte) ('A')))))) + ((byte) 10)));
    }
  }
  public static dafny.DafnySequence<? extends Character> HexStr(byte x) {
    if (java.lang.Integer.compareUnsigned(x, (byte) 16) < 0) {
      dafny.DafnySequence<? extends Character> _0_res = dafny.DafnySequence.<Character> of('0', __default.HexChar(x));
      return _0_res;
    } else {
      dafny.DafnySequence<? extends Character> _1_res = dafny.DafnySequence.<Character> of(__default.HexChar(dafny.Helpers.divideUnsignedByte(x, (byte) 16)), __default.HexChar(dafny.Helpers.remainderUnsignedByte(x, (byte) 16)));
      return _1_res;
    }
  }
  public static byte HexValue(dafny.DafnySequence<? extends Character> x) {
    return (byte) (byte) ((byte)(((byte) (byte) ((byte)((__default.HexVal(((char)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) * ((byte) 16)))) + (__default.HexVal(((char)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))))));
  }
  public static dafny.DafnySequence<? extends Character> ToHexString(dafny.DafnySequence<? extends java.lang.Byte> val) {
    dafny.DafnySequence<? extends Character> _0___accumulator = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((val).length())).signum() == 0) {
        return dafny.DafnySequence.<Character>concatenate(_0___accumulator, dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      } else {
        _0___accumulator = dafny.DafnySequence.<Character>concatenate(_0___accumulator, __default.HexStr(((byte)(java.lang.Object)((val).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))));
        dafny.DafnySequence<? extends java.lang.Byte> _in0 = (val).drop(java.math.BigInteger.ONE);
        val = _in0;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> FromHexString(dafny.DafnySequence<? extends Character> data) {
    dafny.DafnySequence<? extends java.lang.Byte> _0___accumulator = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((data).length())).signum() == 0) {
        return dafny.DafnySequence.<java.lang.Byte>concatenate(_0___accumulator, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      } else if (java.util.Objects.equals(dafny.DafnyEuclidean.EuclideanModulus(java.math.BigInteger.valueOf((data).length()), java.math.BigInteger.valueOf(2L)), java.math.BigInteger.ONE)) {
        _0___accumulator = dafny.DafnySequence.<java.lang.Byte>concatenate(_0___accumulator, dafny.DafnySequence.<java.lang.Byte> of(__default.HexVal(((char)(java.lang.Object)((data).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))));
        dafny.DafnySequence<? extends Character> _in0 = (data).drop(java.math.BigInteger.ONE);
        data = _in0;
        continue TAIL_CALL_START;
      } else {
        _0___accumulator = dafny.DafnySequence.<java.lang.Byte>concatenate(_0___accumulator, dafny.DafnySequence.<java.lang.Byte> of(__default.HexValue((data).take(java.math.BigInteger.valueOf(2L)))));
        dafny.DafnySequence<? extends Character> _in1 = (data).drop(java.math.BigInteger.valueOf(2L));
        data = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  @Override
  public java.lang.String toString() {
    return "HexStrings._default";
  }
}
