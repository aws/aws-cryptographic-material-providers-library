// Class CompareType
// Dafny class CompareType compiled into Java
package FloatCompare_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class CompareType {
  public CompareType() {
  }
  public static java.util.ArrayList<java.lang.Byte> IntegerRange(java.math.BigInteger lo, java.math.BigInteger hi) {
    java.util.ArrayList<java.lang.Byte> arr = new java.util.ArrayList<>();
    for (java.math.BigInteger j = lo; j.compareTo(hi) < 0; j = j.add(java.math.BigInteger.ONE)) { arr.add(java.lang.Byte.valueOf(j.byteValue())); }
    return arr;
  }
  public static boolean _Is(byte __source) {
    java.math.BigInteger _0_x = java.math.BigInteger.valueOf(__source);
    return ((java.math.BigInteger.valueOf(-1L)).compareTo(_0_x) <= 0) && ((_0_x).compareTo(java.math.BigInteger.ONE) <= 0);
  }
  private static final dafny.TypeDescriptor<java.lang.Byte> _TYPE = dafny.TypeDescriptor.byteWithDefault((byte)0);
  public static dafny.TypeDescriptor<java.lang.Byte> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Byte>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
