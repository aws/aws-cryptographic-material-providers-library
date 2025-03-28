// Class SubParser__<T, R>
// Dafny class SubParser__<T, R> compiled into Java
package JSON_mUtils_mParsers_Compile;

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
import JSON_mUtils_mCursors_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class SubParser__<T, R> {
  public java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>> _fn;
  protected dafny.TypeDescriptor<T> _td_T;
  protected dafny.TypeDescriptor<R> _td_R;
  public SubParser__ (dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>> fn) {
    this._td_T = _td_T;
    this._td_R = _td_R;
    this._fn = fn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SubParser__<T, R> o = (SubParser__<T, R>)other;
    return true && java.util.Objects.equals(this._fn, o._fn);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._fn);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Parsers.SubParser_.SubParser");
    s.append("(");
    s.append(dafny.Helpers.toString(this._fn));
    s.append(")");
    return s.toString();
  }
  public static <T, R> dafny.TypeDescriptor<SubParser__<T, R>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    return (dafny.TypeDescriptor<SubParser__<T, R>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<SubParser__<T, R>>referenceWithInitializer(SubParser__.class, () -> SubParser__.<T, R>Default(_td_T, _td_R));
  }

  public static <T, R> SubParser__<T, R> Default(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    return JSON_mUtils_mParsers_Compile.SubParser__.<T, R>create(_td_T, _td_R, ((java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>>) null));
  }
  @Deprecated()
  public static <T, R> SubParser__<T, R> Default() {
    dafny.TypeDescriptor<T> _td_T = null;
    dafny.TypeDescriptor<R> _td_R = null;
    return JSON_mUtils_mParsers_Compile.SubParser__.<T, R>create(_td_T, _td_R, ((java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>>) null));
  }
  public static <T, R> SubParser__<T, R> create(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>> fn) {
    return new SubParser__<T, R>(_td_T, _td_R, fn);
  }
  @Deprecated()
  public static <T, R> SubParser__<T, R> create(java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>> fn) {
    return new SubParser__<T, R>(null, null, fn);
  }
  public static <T, R> SubParser__<T, R> create_SubParser(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>> fn) {
    return create(_td_T, _td_R, fn);
  }
  @Deprecated()
  public static <T, R> SubParser__<T, R> create_SubParser(java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>> fn) {
    return create(null, null, fn);
  }
  public boolean is_SubParser() { return true; }
  public java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>> dtor_fn() {
    return this._fn;
  }
}
