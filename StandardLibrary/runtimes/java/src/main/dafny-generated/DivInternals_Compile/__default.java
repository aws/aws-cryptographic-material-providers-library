// Class __default
// Dafny class __default compiled into Java
package DivInternals_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static java.math.BigInteger DivPos(java.math.BigInteger x, java.math.BigInteger d)
  {
    java.math.BigInteger _0___accumulator = java.math.BigInteger.ZERO;
    TAIL_CALL_START: while (true) {
      if ((x).signum() == -1) {
        _0___accumulator = (_0___accumulator).add(java.math.BigInteger.valueOf(-1L));
        java.math.BigInteger _in0 = (x).add(d);
        java.math.BigInteger _in1 = d;
        x = _in0;
        d = _in1;
        continue TAIL_CALL_START;
      } else if ((x).compareTo(d) < 0) {
        return (java.math.BigInteger.ZERO).add(_0___accumulator);
      } else {
        _0___accumulator = (_0___accumulator).add(java.math.BigInteger.ONE);
        java.math.BigInteger _in2 = (x).subtract(d);
        java.math.BigInteger _in3 = d;
        x = _in2;
        d = _in3;
        continue TAIL_CALL_START;
      }
    }
  }
  public static java.math.BigInteger DivRecursive(java.math.BigInteger x, java.math.BigInteger d)
  {
    if ((d).signum() == 1) {
      return __default.DivPos(x, d);
    } else {
      return (java.math.BigInteger.valueOf(-1L)).multiply(__default.DivPos(x, (java.math.BigInteger.valueOf(-1L)).multiply(d)));
    }
  }
  @Override
  public java.lang.String toString() {
    return "DivInternals._default";
  }
}
