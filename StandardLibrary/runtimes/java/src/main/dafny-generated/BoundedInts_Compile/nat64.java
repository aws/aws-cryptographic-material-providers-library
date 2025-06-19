// Class nat64
// Dafny class nat64 compiled into Java
package BoundedInts_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class nat64 {
  public nat64() {
  }
  public static java.util.ArrayList<java.lang.Long> IntegerRange(java.math.BigInteger lo, java.math.BigInteger hi) {
    java.util.ArrayList<java.lang.Long> arr = new java.util.ArrayList<>();
    for (java.math.BigInteger j = lo; j.compareTo(hi) < 0; j = j.add(java.math.BigInteger.ONE)) { arr.add(java.lang.Long.valueOf(j.longValue())); }
    return arr;
  }
  public static boolean _Is(long __source) {
    java.math.BigInteger _3_x = dafny.Helpers.unsignedToBigInteger(__source);
    return ((_3_x).signum() != -1) && ((_3_x).compareTo(new java.math.BigInteger("9223372036854775808")) < 0);
  }
  private static final dafny.TypeDescriptor<java.lang.Long> _TYPE = dafny.TypeDescriptor.longWithDefault(0L);
  public static dafny.TypeDescriptor<java.lang.Long> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Long>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
