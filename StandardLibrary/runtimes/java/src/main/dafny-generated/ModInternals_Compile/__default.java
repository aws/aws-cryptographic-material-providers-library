// Class __default
// Dafny class __default compiled into Java
package ModInternals_Compile;

import Wrappers_Compile.*;
import Seq_mMergeSort_Compile.*;
import Math_Compile.*;
import Seq_Compile.*;
import BoundedInts_Compile.*;
import Unicode_Compile.*;
import Utf8EncodingForm_Compile.*;
import Utf16EncodingForm_Compile.*;
import UnicodeStrings_Compile.*;
import FileIO_Compile.*;
import MulInternals_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static java.math.BigInteger ModRecursive(java.math.BigInteger x, java.math.BigInteger d)
  {
    TAIL_CALL_START: while (true) {
      if ((x).signum() == -1) {
        java.math.BigInteger _in0 = (d).add(x);
        java.math.BigInteger _in1 = d;
        x = _in0;
        d = _in1;
        continue TAIL_CALL_START;
      } else if ((x).compareTo(d) < 0) {
        return x;
      } else {
        java.math.BigInteger _in2 = (x).subtract(d);
        java.math.BigInteger _in3 = d;
        x = _in2;
        d = _in3;
        continue TAIL_CALL_START;
      }
    }
  }
  @Override
  public java.lang.String toString() {
    return "ModInternals._default";
  }
}
