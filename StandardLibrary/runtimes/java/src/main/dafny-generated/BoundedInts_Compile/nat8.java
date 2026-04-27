// Class nat8
// Dafny class nat8 compiled into Java
package BoundedInts_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class nat8 {
  public nat8() {
  }
  public static java.util.ArrayList<java.lang.Byte> IntegerRange(java.math.BigInteger lo, java.math.BigInteger hi) {
    java.util.ArrayList<java.lang.Byte> arr = new java.util.ArrayList<>();
    for (java.math.BigInteger j = lo; j.compareTo(hi) < 0; j = j.add(java.math.BigInteger.ONE)) { arr.add(java.lang.Byte.valueOf(j.byteValue())); }
    return arr;
  }
  public static boolean _Is(byte __source) {
    java.math.BigInteger _0_x = dafny.Helpers.unsignedToBigInteger(__source);
    return ((_0_x).signum() != -1) && ((_0_x).compareTo(java.math.BigInteger.valueOf(128L)) < 0);
  }
  private static final dafny.TypeDescriptor<java.lang.Byte> _TYPE = dafny.TypeDescriptor.byteWithDefault((byte)0);
  public static dafny.TypeDescriptor<java.lang.Byte> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Byte>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
