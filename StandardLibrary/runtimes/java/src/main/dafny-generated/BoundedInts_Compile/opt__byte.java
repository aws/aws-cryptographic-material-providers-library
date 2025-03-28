// Class opt__byte
// Dafny class opt__byte compiled into Java
package BoundedInts_Compile;

import Wrappers_Compile.*;
import Seq_mMergeSort_Compile.*;
import Math_Compile.*;
import Seq_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class opt__byte {
  public opt__byte() {
  }
  public static java.util.ArrayList<java.lang.Short> IntegerRange(java.math.BigInteger lo, java.math.BigInteger hi) {
    java.util.ArrayList<java.lang.Short> arr = new java.util.ArrayList<>();
    for (java.math.BigInteger j = lo; j.compareTo(hi) < 0; j = j.add(java.math.BigInteger.ONE)) { arr.add(java.lang.Short.valueOf(j.shortValue())); }
    return arr;
  }
  public static boolean _Is(short __source) {
    java.math.BigInteger _4_c = java.math.BigInteger.valueOf(__source);
    return ((java.math.BigInteger.valueOf(-1L)).compareTo(_4_c) <= 0) && ((_4_c).compareTo(__default.TWO__TO__THE__8()) < 0);
  }
  private static final dafny.TypeDescriptor<java.lang.Short> _TYPE = dafny.TypeDescriptor.shortWithDefault((short)0);
  public static dafny.TypeDescriptor<java.lang.Short> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Short>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
