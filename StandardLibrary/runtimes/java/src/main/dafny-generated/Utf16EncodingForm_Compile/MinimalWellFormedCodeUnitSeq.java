// Class MinimalWellFormedCodeUnitSeq
// Dafny class MinimalWellFormedCodeUnitSeq compiled into Java
package Utf16EncodingForm_Compile;

import Wrappers_Compile.*;
import Seq_mMergeSort_Compile.*;
import Math_Compile.*;
import Seq_Compile.*;
import BoundedInts_Compile.*;
import Unicode_Compile.*;
import Utf8EncodingForm_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class MinimalWellFormedCodeUnitSeq {
  public MinimalWellFormedCodeUnitSeq() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends java.lang.Short> __source) {
    dafny.DafnySequence<? extends java.lang.Short> _4_s = __source;
    return __default.IsMinimalWellFormedCodeUnitSubsequence(_4_s);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Short>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends java.lang.Short>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<java.lang.Short> empty(dafny.TypeDescriptor.SHORT));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Short>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Short>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
