// Class seq16
// Dafny class seq16 compiled into Java
package StandardLibrary_mUInt_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class seq16<T> {
  protected dafny.TypeDescriptor<T> _td_T;
  public seq16(dafny.TypeDescriptor<T> _td_T) {
    this._td_T = _td_T;
  }
  public static <T> boolean _Is(dafny.TypeDescriptor<T> _td_T, dafny.DafnySequence<? extends T> __source) {
    dafny.DafnySequence<? extends T> _0_s = __source;
    return __default.<T>HasUint16Len(_td_T, _0_s);
  }
  public static <T> dafny.TypeDescriptor<dafny.DafnySequence<? extends T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<dafny.DafnySequence<? extends T>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<T> empty(_td_T));
  }
}
