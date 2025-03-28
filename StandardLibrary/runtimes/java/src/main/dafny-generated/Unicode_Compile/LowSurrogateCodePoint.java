// Class LowSurrogateCodePoint
// Dafny class LowSurrogateCodePoint compiled into Java
package Unicode_Compile;

import Wrappers_Compile.*;
import Seq_mMergeSort_Compile.*;
import Math_Compile.*;
import Seq_Compile.*;
import BoundedInts_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class LowSurrogateCodePoint {
  public LowSurrogateCodePoint() {
  }
  public static int Witness = __default.LOW__SURROGATE__MIN();
  public static int defaultValue() {
    return Witness;
  }
  public static boolean _Is(int __source) {
    int _2_p = (__source);
    if (CodePoint._Is(_2_p)) {
      return (java.lang.Integer.compareUnsigned(__default.LOW__SURROGATE__MIN(), _2_p) <= 0) && (java.lang.Integer.compareUnsigned(_2_p, __default.LOW__SURROGATE__MAX()) <= 0);
    }
    return false;
  }
  private static final dafny.TypeDescriptor<java.lang.Integer> _TYPE = dafny.TypeDescriptor.intWithDefault(Witness);
  public static dafny.TypeDescriptor<java.lang.Integer> _typeDescriptor() {
    return (dafny.TypeDescriptor<java.lang.Integer>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
