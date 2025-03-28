// Class jnumber
// Dafny class jnumber compiled into Java
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
public class jnumber {
  public JSON_mUtils_mViews_mCore_Compile.View__ _minus;
  public JSON_mUtils_mViews_mCore_Compile.View__ _num;
  public Maybe<jfrac> _frac;
  public Maybe<jexp> _exp;
  public jnumber (JSON_mUtils_mViews_mCore_Compile.View__ minus, JSON_mUtils_mViews_mCore_Compile.View__ num, Maybe<jfrac> frac, Maybe<jexp> exp) {
    this._minus = minus;
    this._num = num;
    this._frac = frac;
    this._exp = exp;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    jnumber o = (jnumber)other;
    return true && java.util.Objects.equals(this._minus, o._minus) && java.util.Objects.equals(this._num, o._num) && java.util.Objects.equals(this._frac, o._frac) && java.util.Objects.equals(this._exp, o._exp);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._minus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._num);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._frac);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._exp);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.jnumber.JNumber");
    s.append("(");
    s.append(dafny.Helpers.toString(this._minus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._num));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._frac));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._exp));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<jnumber> _TYPE = dafny.TypeDescriptor.<jnumber>referenceWithInitializer(jnumber.class, () -> jnumber.Default());
  public static dafny.TypeDescriptor<jnumber> _typeDescriptor() {
    return (dafny.TypeDescriptor<jnumber>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final jnumber theDefault = JSON_mGrammar_Compile.jnumber.create(jminus.defaultValue(), jnum.defaultValue(), Maybe.<jfrac>Default(jfrac._typeDescriptor()), Maybe.<jexp>Default(jexp._typeDescriptor()));
  public static jnumber Default() {
    return theDefault;
  }
  public static jnumber create(JSON_mUtils_mViews_mCore_Compile.View__ minus, JSON_mUtils_mViews_mCore_Compile.View__ num, Maybe<jfrac> frac, Maybe<jexp> exp) {
    return new jnumber(minus, num, frac, exp);
  }
  public static jnumber create_JNumber(JSON_mUtils_mViews_mCore_Compile.View__ minus, JSON_mUtils_mViews_mCore_Compile.View__ num, Maybe<jfrac> frac, Maybe<jexp> exp) {
    return create(minus, num, frac, exp);
  }
  public boolean is_JNumber() { return true; }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_minus() {
    return this._minus;
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_num() {
    return this._num;
  }
  public Maybe<jfrac> dtor_frac() {
    return this._frac;
  }
  public Maybe<jexp> dtor_exp() {
    return this._exp;
  }
}
