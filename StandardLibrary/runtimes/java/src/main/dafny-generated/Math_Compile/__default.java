// Class __default
// Dafny class __default compiled into Java
package Math_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static java.math.BigInteger Min(java.math.BigInteger a, java.math.BigInteger b)
  {
    if ((a).compareTo(b) < 0) {
      return a;
    } else {
      return b;
    }
  }
  public static java.math.BigInteger Max(java.math.BigInteger a, java.math.BigInteger b)
  {
    if ((a).compareTo(b) < 0) {
      return b;
    } else {
      return a;
    }
  }
  public static java.math.BigInteger Abs(java.math.BigInteger a) {
    if ((a).signum() != -1) {
      return a;
    } else {
      return (java.math.BigInteger.ZERO).subtract(a);
    }
  }
  @Override
  public java.lang.String toString() {
    return "Math._default";
  }
}
