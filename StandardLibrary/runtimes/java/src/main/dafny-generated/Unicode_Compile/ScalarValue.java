// Class ScalarValue
// Dafny class ScalarValue compiled into Java
package Unicode_Compile;

import Wrappers_Compile.*;
import Seq_mMergeSort_Compile.*;
import Math_Compile.*;
import Seq_Compile.*;
import BoundedInts_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class ScalarValue {
  public ScalarValue() {
  }
  public static boolean _Is(int __source) {
    int _3_p = (__source);
    if (CodePoint._Is(_3_p)) {
      return ((java.lang.Integer.compareUnsigned(_3_p, __default.HIGH__SURROGATE__MIN()) < 0) || (java.lang.Integer.compareUnsigned(_3_p, __default.HIGH__SURROGATE__MAX()) > 0)) && ((java.lang.Integer.compareUnsigned(_3_p, __default.LOW__SURROGATE__MIN()) < 0) || (java.lang.Integer.compareUnsigned(_3_p, __default.LOW__SURROGATE__MAX()) > 0));
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(0);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
