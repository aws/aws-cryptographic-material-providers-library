// Class __default
// Dafny class __default compiled into Java
package StandardLibrary_mSequence_Compile;

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
import ModInternals_Compile.*;
import DivInternals_Compile.*;
import Power_Compile.*;
import Logarithm_Compile.*;
import StandardLibraryInterop_Compile.*;
import StandardLibrary_mUInt_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static <__T> boolean SequenceEqualNat(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> seq1, dafny.DafnySequence<? extends __T> seq2, java.math.BigInteger start1, java.math.BigInteger start2, java.math.BigInteger size)
  {
    if (((java.math.BigInteger.valueOf((seq1).length())).compareTo(StandardLibrary_mUInt_Compile.__default.UINT64__MAX__LIMIT()) > 0) || ((java.math.BigInteger.valueOf((seq2).length())).compareTo(StandardLibrary_mUInt_Compile.__default.UINT64__MAX__LIMIT()) > 0)) {
      return ((seq1).subsequence(dafny.Helpers.toInt((start1)), dafny.Helpers.toInt(((start1).add(size))))).equals((seq2).subsequence(dafny.Helpers.toInt((start2)), dafny.Helpers.toInt(((start2).add(size)))));
    } else {
      return __default.<__T>SequenceEqual(_td___T, seq1, seq2, (start1).longValue(), (start2).longValue(), (size).longValue());
    }
  }
  public static <__T> boolean SequenceEqual(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> seq1, dafny.DafnySequence<? extends __T> seq2, long start1, long start2, long size)
  {
    boolean ret = false;
    long _0_j;
    _0_j = start2;
    long _hi0 = (long) (long) ((start1) + (size));
    for (long _1_i = start1; java.lang.Long.compareUnsigned(_1_i, _hi0) < 0; _1_i++) {
      if (!java.util.Objects.equals(((__T)(java.lang.Object)((seq1).select(dafny.Helpers.unsignedToInt(_1_i)))), ((__T)(java.lang.Object)((seq2).select(dafny.Helpers.unsignedToInt(_0_j)))))) {
        ret = false;
        return ret;
      }
      _0_j = (long) (long) ((_0_j) + ((long) 1L));
    }
    ret = true;
    return ret;
  }
  @Override
  public java.lang.String toString() {
    return "StandardLibrary.Sequence._default";
  }
}
