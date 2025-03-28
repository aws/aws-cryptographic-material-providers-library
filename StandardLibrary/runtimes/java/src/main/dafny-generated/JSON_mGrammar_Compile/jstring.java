// Class jstring
// Dafny class jstring compiled into Java
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
public class jstring {
  public JSON_mUtils_mViews_mCore_Compile.View__ _lq;
  public JSON_mUtils_mViews_mCore_Compile.View__ _contents;
  public JSON_mUtils_mViews_mCore_Compile.View__ _rq;
  public jstring (JSON_mUtils_mViews_mCore_Compile.View__ lq, JSON_mUtils_mViews_mCore_Compile.View__ contents, JSON_mUtils_mViews_mCore_Compile.View__ rq) {
    this._lq = lq;
    this._contents = contents;
    this._rq = rq;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    jstring o = (jstring)other;
    return true && java.util.Objects.equals(this._lq, o._lq) && java.util.Objects.equals(this._contents, o._contents) && java.util.Objects.equals(this._rq, o._rq);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._lq);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._contents);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._rq);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.jstring.JString");
    s.append("(");
    s.append(dafny.Helpers.toString(this._lq));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._contents));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._rq));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<jstring> _TYPE = dafny.TypeDescriptor.<jstring>referenceWithInitializer(jstring.class, () -> jstring.Default());
  public static dafny.TypeDescriptor<jstring> _typeDescriptor() {
    return (dafny.TypeDescriptor<jstring>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final jstring theDefault = JSON_mGrammar_Compile.jstring.create(jquote.defaultValue(), jstr.defaultValue(), jquote.defaultValue());
  public static jstring Default() {
    return theDefault;
  }
  public static jstring create(JSON_mUtils_mViews_mCore_Compile.View__ lq, JSON_mUtils_mViews_mCore_Compile.View__ contents, JSON_mUtils_mViews_mCore_Compile.View__ rq) {
    return new jstring(lq, contents, rq);
  }
  public static jstring create_JString(JSON_mUtils_mViews_mCore_Compile.View__ lq, JSON_mUtils_mViews_mCore_Compile.View__ contents, JSON_mUtils_mViews_mCore_Compile.View__ rq) {
    return create(lq, contents, rq);
  }
  public boolean is_JString() { return true; }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_lq() {
    return this._lq;
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_contents() {
    return this._contents;
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_rq() {
    return this._rq;
  }
}
