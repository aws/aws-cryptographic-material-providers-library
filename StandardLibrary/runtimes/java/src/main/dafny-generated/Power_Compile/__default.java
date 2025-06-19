// Class __default
// Dafny class __default compiled into Java
package Power_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static java.math.BigInteger Pow(java.math.BigInteger b, java.math.BigInteger e)
  {
    java.math.BigInteger _0___accumulator = java.math.BigInteger.ONE;
    TAIL_CALL_START: while (true) {
      if ((e).signum() == 0) {
        return (java.math.BigInteger.ONE).multiply(_0___accumulator);
      } else {
        _0___accumulator = (_0___accumulator).multiply(b);
        java.math.BigInteger _in0 = b;
        java.math.BigInteger _in1 = (e).subtract(java.math.BigInteger.ONE);
        b = _in0;
        e = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  @Override
  public java.lang.String toString() {
    return "Power._default";
  }
}
