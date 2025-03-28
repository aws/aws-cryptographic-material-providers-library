// Class __default
// Dafny class __default compiled into Java
package MulInternals_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static java.math.BigInteger MulPos(java.math.BigInteger x, java.math.BigInteger y)
  {
    java.math.BigInteger _0___accumulator = java.math.BigInteger.ZERO;
    TAIL_CALL_START: while (true) {
      if ((x).signum() == 0) {
        return (java.math.BigInteger.ZERO).add(_0___accumulator);
      } else {
        _0___accumulator = (_0___accumulator).add(y);
        java.math.BigInteger _in0 = (x).subtract(java.math.BigInteger.ONE);
        java.math.BigInteger _in1 = y;
        x = _in0;
        y = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static java.math.BigInteger MulRecursive(java.math.BigInteger x, java.math.BigInteger y)
  {
    if ((x).signum() != -1) {
      return __default.MulPos(x, y);
    } else {
      return (java.math.BigInteger.valueOf(-1L)).multiply(__default.MulPos((java.math.BigInteger.valueOf(-1L)).multiply(x), y));
    }
  }
  @Override
  public java.lang.String toString() {
    return "MulInternals._default";
  }
}
