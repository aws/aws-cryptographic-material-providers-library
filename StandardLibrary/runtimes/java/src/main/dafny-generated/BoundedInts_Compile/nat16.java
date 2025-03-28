// Class nat16
// Dafny class nat16 compiled into Java
package BoundedInts_Compile;

import Wrappers_Compile.*;
import Seq_mMergeSort_Compile.*;
import Math_Compile.*;
import Seq_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class nat16 {
  public nat16() {
  }
  public static java.util.ArrayList<java.lang.Short> IntegerRange(java.math.BigInteger lo, java.math.BigInteger hi) {
    java.util.ArrayList<java.lang.Short> arr = new java.util.ArrayList<>();
    for (java.math.BigInteger j = lo; j.compareTo(hi) < 0; j = j.add(java.math.BigInteger.ONE)) { arr.add(java.lang.Short.valueOf(j.shortValue())); }
    return arr;
  }
  public static boolean _Is(short __source) {
    java.math.BigInteger _1_x = dafny.Helpers.unsignedToBigInteger(__source);
    return ((_1_x).signum() != -1) && ((_1_x).compareTo(java.math.BigInteger.valueOf(32768L)) < 0);
  }
  private static final dafny.TypeDescriptor<java.lang.Short> _TYPE = dafny.TypeDescriptor.shortWithDefault((short)0);
  public static dafny.TypeDescriptor<java.lang.Short> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Short>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
