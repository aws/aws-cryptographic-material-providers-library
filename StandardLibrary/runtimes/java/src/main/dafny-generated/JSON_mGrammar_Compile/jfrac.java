// Class jfrac
// Dafny class jfrac compiled into Java
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
public class jfrac {
  public JSON_mUtils_mViews_mCore_Compile.View__ _period;
  public JSON_mUtils_mViews_mCore_Compile.View__ _num;
  public jfrac (JSON_mUtils_mViews_mCore_Compile.View__ period, JSON_mUtils_mViews_mCore_Compile.View__ num) {
    this._period = period;
    this._num = num;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    jfrac o = (jfrac)other;
    return true && java.util.Objects.equals(this._period, o._period) && java.util.Objects.equals(this._num, o._num);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._period);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._num);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.jfrac.JFrac");
    s.append("(");
    s.append(dafny.Helpers.toString(this._period));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._num));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<jfrac> _TYPE = dafny.TypeDescriptor.<jfrac>referenceWithInitializer(jfrac.class, () -> jfrac.Default());
  public static dafny.TypeDescriptor<jfrac> _typeDescriptor() {
    return (dafny.TypeDescriptor<jfrac>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final jfrac theDefault = JSON_mGrammar_Compile.jfrac.create(jperiod.defaultValue(), jnum.defaultValue());
  public static jfrac Default() {
    return theDefault;
  }
  public static jfrac create(JSON_mUtils_mViews_mCore_Compile.View__ period, JSON_mUtils_mViews_mCore_Compile.View__ num) {
    return new jfrac(period, num);
  }
  public static jfrac create_JFrac(JSON_mUtils_mViews_mCore_Compile.View__ period, JSON_mUtils_mViews_mCore_Compile.View__ num) {
    return create(period, num);
  }
  public boolean is_JFrac() { return true; }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_period() {
    return this._period;
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_num() {
    return this._num;
  }
}
