// Class __default
// Dafny class __default compiled into Java
package Unicode_Compile;

import Wrappers_Compile.*;
import Seq_mMergeSort_Compile.*;
import Math_Compile.*;
import Seq_Compile.*;
import BoundedInts_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static int HIGH__SURROGATE__MIN()
  {
    return 55296;
  }
  public static int HIGH__SURROGATE__MAX()
  {
    return 56319;
  }
  public static int LOW__SURROGATE__MIN()
  {
    return 56320;
  }
  public static int LOW__SURROGATE__MAX()
  {
    return 57343;
  }
  public static dafny.DafnySet<? extends java.lang.Byte> ASSIGNED__PLANES()
  {
    return dafny.DafnySet.<java.lang.Byte> of((byte) 0, (byte) 1, (byte) 2, (byte) 3, (byte) 14, (byte) 15, (byte) 16);
  }
  @Override
  public java.lang.String toString() {
    return "Unicode._default";
  }
}
