// Class uint16
// Dafny class uint16 compiled into Java
package BoundedInts_Compile;

import Wrappers_Compile.*;
import Seq_mMergeSort_Compile.*;
import Math_Compile.*;
import Seq_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class uint16 {
  public uint16() {
  }
  public static java.util.ArrayList<java.lang.Short> IntegerRange(java.math.BigInteger lo, java.math.BigInteger hi) {
    java.util.ArrayList<java.lang.Short> arr = new java.util.ArrayList<>();
    for (java.math.BigInteger j = lo; j.compareTo(hi) < 0; j = j.add(java.math.BigInteger.ONE)) { arr.add(java.lang.Short.valueOf(j.shortValue())); }
    return arr;
  }
  public static boolean _Is(short __source) {
    return true;
  }
  private static final dafny.TypeDescriptor<java.lang.Short> _TYPE = dafny.TypeDescriptor.shortWithDefault((short)0);
  public static dafny.TypeDescriptor<java.lang.Short> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Short>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
