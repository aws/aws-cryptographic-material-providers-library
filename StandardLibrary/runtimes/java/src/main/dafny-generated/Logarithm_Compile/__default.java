// Class __default
// Dafny class __default compiled into Java
package Logarithm_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static java.math.BigInteger Log(java.math.BigInteger base, java.math.BigInteger pow)
  {
    java.math.BigInteger _0___accumulator = java.math.BigInteger.ZERO;
    TAIL_CALL_START: while (true) {
      if ((pow).compareTo(base) < 0) {
        return (java.math.BigInteger.ZERO).add(_0___accumulator);
      } else {
        _0___accumulator = (_0___accumulator).add(java.math.BigInteger.ONE);
        java.math.BigInteger _in0 = base;
        java.math.BigInteger _in1 = dafny.DafnyEuclidean.EuclideanDivision(pow, base);
        base = _in0;
        pow = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  @Override
  public java.lang.String toString() {
    return "Logarithm._default";
  }
}
