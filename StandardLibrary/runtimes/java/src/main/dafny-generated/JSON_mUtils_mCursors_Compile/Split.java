// Class Split<T>
// Dafny class Split<T> compiled into Java
package JSON_mUtils_mCursors_Compile;

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
import JSON_mUtils_mViews_mWriters_Compile.*;
import JSON_mUtils_mLexers_mCore_Compile.*;
import JSON_mUtils_mLexers_mStrings_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class Split<T> {
  public T _t;
  public Cursor__ _cs;
  protected dafny.TypeDescriptor<T> _td_T;
  public Split (dafny.TypeDescriptor<T> _td_T, T t, Cursor__ cs) {
    this._td_T = _td_T;
    this._t = t;
    this._cs = cs;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Split<T> o = (Split<T>)other;
    return true && java.util.Objects.equals(this._t, o._t) && java.util.Objects.equals(this._cs, o._cs);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._t);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._cs);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Cursors.Split.SP");
    s.append("(");
    s.append(dafny.Helpers.toString(this._t));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._cs));
    s.append(")");
    return s.toString();
  }
  public static <T> dafny.TypeDescriptor<Split<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<Split<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<Split<T>>referenceWithInitializer(Split.class, () -> Split.<T>Default(_td_T, _td_T.defaultValue()));
  }

  public static <T> Split<T> Default(dafny.TypeDescriptor<T> _td_T, T _default_T) {
    return JSON_mUtils_mCursors_Compile.Split.<T>create(_td_T, _default_T, FreshCursor.defaultValue());
  }
  @Deprecated()
  public static <T> Split<T> Default(T _default_T) {
    dafny.TypeDescriptor<T> _td_T = null;
    return JSON_mUtils_mCursors_Compile.Split.<T>create(_td_T, _default_T, FreshCursor.defaultValue());
  }
  public static <T> Split<T> create(dafny.TypeDescriptor<T> _td_T, T t, Cursor__ cs) {
    return new Split<T>(_td_T, t, cs);
  }
  @Deprecated()
  public static <T> Split<T> create(T t, Cursor__ cs) {
    return new Split<T>(null, t, cs);
  }
  public static <T> Split<T> create_SP(dafny.TypeDescriptor<T> _td_T, T t, Cursor__ cs) {
    return create(_td_T, t, cs);
  }
  @Deprecated()
  public static <T> Split<T> create_SP(T t, Cursor__ cs) {
    return create(null, t, cs);
  }
  public boolean is_SP() { return true; }
  public T dtor_t() {
    return this._t;
  }
  public Cursor__ dtor_cs() {
    return this._cs;
  }
}
