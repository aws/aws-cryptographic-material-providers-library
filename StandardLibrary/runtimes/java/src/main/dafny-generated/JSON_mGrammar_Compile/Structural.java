// Class Structural<T>
// Dafny class Structural<T> compiled into Java
package JSON_mGrammar_Compile;

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
import JSON_mUtils_mParsers_Compile.*;
import JSON_mUtils_mStr_mCharStrConversion_Compile.*;
import JSON_mUtils_mStr_mCharStrEscaping_Compile.*;
import JSON_mUtils_mStr_Compile.*;
import JSON_mUtils_mVectors_Compile.*;
import JSON_mErrors_Compile.*;
import JSON_mValues_Compile.*;
import JSON_mSpec_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class Structural<T> {
  public JSON_mUtils_mViews_mCore_Compile.View__ _before;
  public T _t;
  public JSON_mUtils_mViews_mCore_Compile.View__ _after;
  protected dafny.TypeDescriptor<T> _td_T;
  public Structural (dafny.TypeDescriptor<T> _td_T, JSON_mUtils_mViews_mCore_Compile.View__ before, T t, JSON_mUtils_mViews_mCore_Compile.View__ after) {
    this._td_T = _td_T;
    this._before = before;
    this._t = t;
    this._after = after;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Structural<T> o = (Structural<T>)other;
    return true && java.util.Objects.equals(this._before, o._before) && java.util.Objects.equals(this._t, o._t) && java.util.Objects.equals(this._after, o._after);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._before);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._t);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._after);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.Structural.Structural");
    s.append("(");
    s.append(dafny.Helpers.toString(this._before));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._t));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._after));
    s.append(")");
    return s.toString();
  }
  public static <T> dafny.TypeDescriptor<Structural<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<Structural<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<Structural<T>>referenceWithInitializer(Structural.class, () -> Structural.<T>Default(_td_T, _td_T.defaultValue()));
  }

  public static <T> Structural<T> Default(dafny.TypeDescriptor<T> _td_T, T _default_T) {
    return JSON_mGrammar_Compile.Structural.<T>create(_td_T, jblanks.defaultValue(), _default_T, jblanks.defaultValue());
  }
  @Deprecated()
  public static <T> Structural<T> Default(T _default_T) {
    dafny.TypeDescriptor<T> _td_T = null;
    return JSON_mGrammar_Compile.Structural.<T>create(_td_T, jblanks.defaultValue(), _default_T, jblanks.defaultValue());
  }
  public static <T> Structural<T> create(dafny.TypeDescriptor<T> _td_T, JSON_mUtils_mViews_mCore_Compile.View__ before, T t, JSON_mUtils_mViews_mCore_Compile.View__ after) {
    return new Structural<T>(_td_T, before, t, after);
  }
  @Deprecated()
  public static <T> Structural<T> create(JSON_mUtils_mViews_mCore_Compile.View__ before, T t, JSON_mUtils_mViews_mCore_Compile.View__ after) {
    return new Structural<T>(null, before, t, after);
  }
  public static <T> Structural<T> create_Structural(dafny.TypeDescriptor<T> _td_T, JSON_mUtils_mViews_mCore_Compile.View__ before, T t, JSON_mUtils_mViews_mCore_Compile.View__ after) {
    return create(_td_T, before, t, after);
  }
  @Deprecated()
  public static <T> Structural<T> create_Structural(JSON_mUtils_mViews_mCore_Compile.View__ before, T t, JSON_mUtils_mViews_mCore_Compile.View__ after) {
    return create(null, before, t, after);
  }
  public boolean is_Structural() { return true; }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_before() {
    return this._before;
  }
  public T dtor_t() {
    return this._t;
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_after() {
    return this._after;
  }
}
