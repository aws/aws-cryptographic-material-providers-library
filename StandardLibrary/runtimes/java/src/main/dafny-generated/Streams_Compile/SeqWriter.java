// Class SeqWriter
// Dafny class SeqWriter compiled into Java
package Streams_Compile;

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
import StandardLibrary_mSequence_Compile.*;
import StandardLibrary_mString_Compile.*;
import StandardLibrary_Compile.*;
import UUID.*;
import UTF8.*;
import OsLang.*;
import Time.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class SeqWriter<T> {
  protected dafny.TypeDescriptor<T> _td_T;
  public SeqWriter(dafny.TypeDescriptor<T> _td_T) {
    this._td_T = _td_T;
    this.data = dafny.DafnySequence.<T> empty(_td_T);
  }
  public dafny.DafnySequence<? extends T> data;
  public void __ctor()
  {
    (this).data = dafny.DafnySequence.<T> empty(_td_T);
  }
  public java.math.BigInteger WriteElements(dafny.DafnySequence<? extends T> elems)
  {
    java.math.BigInteger n = java.math.BigInteger.ZERO;
    (this).data = dafny.DafnySequence.<T>concatenate(this.data, elems);
    n = java.math.BigInteger.valueOf((elems).length());
    return n;
  }
  public static <T> dafny.TypeDescriptor<SeqWriter<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<SeqWriter<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<SeqWriter<T>>referenceWithInitializer(SeqWriter.class, () -> (SeqWriter<T>) null);
  }
  @Override
  public java.lang.String toString() {
    return "Streams.SeqWriter";
  }
}
