// Class nat32
// Dafny class nat32 compiled into Java
package BoundedInts_Compile;

import Wrappers_Compile.*;
import Seq_mMergeSort_Compile.*;
import Math_Compile.*;
import Seq_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class nat32 {
  public nat32() {
  }
  public static java.util.ArrayList<java.lang.Integer> IntegerRange(java.math.BigInteger lo, java.math.BigInteger hi) {
    java.util.ArrayList<java.lang.Integer> arr = new java.util.ArrayList<>();
    for (java.math.BigInteger j = lo; j.compareTo(hi) < 0; j = j.add(java.math.BigInteger.ONE)) { arr.add(java.lang.Integer.valueOf(j.intValue())); }
    return arr;
  }
  public static boolean _Is(int __source) {
    java.math.BigInteger _2_x = dafny.Helpers.unsignedToBigInteger(__source);
    return ((_2_x).signum() != -1) && ((_2_x).compareTo(java.math.BigInteger.valueOf(2147483648L)) < 0);
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(0);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
