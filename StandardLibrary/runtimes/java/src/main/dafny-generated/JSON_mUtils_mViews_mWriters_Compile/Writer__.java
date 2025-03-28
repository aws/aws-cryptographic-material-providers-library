// Class Writer__
// Dafny class Writer__ compiled into Java
package JSON_mUtils_mViews_mWriters_Compile;

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
import Streams_Compile.*;
import Sorting_Compile.*;
import HexStrings_Compile.*;
import GetOpt_Compile.*;
import FloatCompare_Compile.*;
import ConcurrentCall.*;
import Base64_Compile.*;
import Actions_Compile.*;
import DafnyLibraries.*;
import JSON_mUtils_mViews_mCore_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class Writer__ {
  public int _length;
  public Chain _chain;
  public Writer__ (int length, Chain chain) {
    this._length = length;
    this._chain = chain;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Writer__ o = (Writer__)other;
    return true && this._length == o._length && java.util.Objects.equals(this._chain, o._chain);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._length);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._chain);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Writers.Writer_.Writer");
    s.append("(");
    s.append(this._length);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._chain));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Writer__> _TYPE = dafny.TypeDescriptor.<Writer__>referenceWithInitializer(Writer__.class, () -> Writer__.Default());
  public static dafny.TypeDescriptor<Writer__> _typeDescriptor() {
    return (dafny.TypeDescriptor<Writer__>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Writer__ theDefault = JSON_mUtils_mViews_mWriters_Compile.Writer__.create(0, Chain.Default());
  public static Writer__ Default() {
    return theDefault;
  }
  public static Writer__ create(int length, Chain chain) {
    return new Writer__(length, chain);
  }
  public static Writer__ create_Writer(int length, Chain chain) {
    return create(length, chain);
  }
  public boolean is_Writer() { return true; }
  public int dtor_length() {
    return this._length;
  }
  public Chain dtor_chain() {
    return this._chain;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> Bytes() {
    return ((this).dtor_chain()).Bytes();
  }
  public static int SaturatedAddU32(int a, int b)
  {
    if (java.lang.Integer.compareUnsigned(a, (int) ((BoundedInts_Compile.__default.UINT32__MAX()) - (b))) <= 0) {
      return (int) ((a) + (b));
    } else {
      return BoundedInts_Compile.__default.UINT32__MAX();
    }
  }
  public Writer__ Append(JSON_mUtils_mViews_mCore_Compile.View__ v_k) {
    return JSON_mUtils_mViews_mWriters_Compile.Writer__.create(Writer__.SaturatedAddU32((this).dtor_length(), (v_k).Length()), ((this).dtor_chain()).Append(v_k));
  }
  public Writer__ Then(java.util.function.Function<Writer__, Writer__> fn) {
    return ((Writer__)(java.lang.Object)((fn).apply(this)));
  }
  public void CopyTo(byte[] dest)
  {
    ((this).dtor_chain()).CopyTo(dest, (this).dtor_length());
  }
  public byte[] ToArray()
  {
    byte[] bs = new byte[0];
    if(true) {
      byte[] _nw0 = (byte[]) BoundedInts_Compile.uint8._typeDescriptor().fillThenReturnArray(BoundedInts_Compile.uint8._typeDescriptor().newArray(dafny.Helpers.toIntChecked(((this).dtor_length()), "Java arrays may be no larger than the maximum 32-bit signed int")), (byte) 0);
      bs = _nw0;
      (this).CopyTo(bs);
    }
    return bs;
  }
  public static Writer__ Empty()
  {
    return JSON_mUtils_mViews_mWriters_Compile.Writer__.create(0, JSON_mUtils_mViews_mWriters_Compile.Chain.create_Empty());
  }
  public boolean Unsaturated_q()
  {
    return ((this).dtor_length()) != (BoundedInts_Compile.__default.UINT32__MAX());
  }
  public boolean Empty_q()
  {
    return ((this).dtor_chain()).is_Empty();
  }
}
