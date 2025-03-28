// Class Maybe<T>
// Dafny class Maybe<T> compiled into Java
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
public abstract class Maybe<T> {
  protected dafny.TypeDescriptor<T> _td_T;
  public Maybe(dafny.TypeDescriptor<T> _td_T) {
    this._td_T = _td_T;
  }
  public static <T> dafny.TypeDescriptor<Maybe<T>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T) {
    return (dafny.TypeDescriptor<Maybe<T>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<Maybe<T>>referenceWithInitializer(Maybe.class, () -> Maybe.<T>Default(_td_T));
  }

  public static <T> Maybe<T> Default(dafny.TypeDescriptor<T> _td_T) {
    return JSON_mGrammar_Compile.Maybe.<T>create_Empty(_td_T);
  }
  @Deprecated()
  public static <T> Maybe<T> Default() {
    dafny.TypeDescriptor<T> _td_T = null;
    return JSON_mGrammar_Compile.Maybe.<T>create_Empty(_td_T);
  }
  public static <T> Maybe<T> create_Empty(dafny.TypeDescriptor<T> _td_T) {
    return new Maybe_Empty<T>(_td_T);
  }
  @Deprecated()
  public static <T> Maybe<T> create_Empty() {
    return new Maybe_Empty<T>(null);
  }
  public static <T> Maybe<T> create_NonEmpty(dafny.TypeDescriptor<T> _td_T, T t) {
    return new Maybe_NonEmpty<T>(_td_T, t);
  }
  @Deprecated()
  public static <T> Maybe<T> create_NonEmpty(T t) {
    return new Maybe_NonEmpty<T>(null, t);
  }
  public boolean is_Empty() { return this instanceof Maybe_Empty; }
  public boolean is_NonEmpty() { return this instanceof Maybe_NonEmpty; }
  public T dtor_t() {
    Maybe<T> d = this;
    return ((Maybe_NonEmpty<T>)d)._t;
  }
}
