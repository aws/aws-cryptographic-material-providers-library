// Class LexerResult<T, R>
// Dafny class LexerResult<T, R> compiled into Java
package JSON_mUtils_mLexers_mCore_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class LexerResult<T, R> {
  protected dafny.TypeDescriptor<T> _td_T;
  protected dafny.TypeDescriptor<R> _td_R;
  public LexerResult(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    this._td_T = _td_T;
    this._td_R = _td_R;
  }
  public static <T, R> dafny.TypeDescriptor<LexerResult<T, R>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    return (dafny.TypeDescriptor<LexerResult<T, R>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<LexerResult<T, R>>referenceWithInitializer(LexerResult.class, () -> LexerResult.<T, R>Default(_td_T, _td_R));
  }

  public static <T, R> LexerResult<T, R> Default(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    return JSON_mUtils_mLexers_mCore_Compile.LexerResult.<T, R>create_Accept(_td_T, _td_R);
  }
  @Deprecated()
  public static <T, R> LexerResult<T, R> Default() {
    dafny.TypeDescriptor<T> _td_T = null;
    dafny.TypeDescriptor<R> _td_R = null;
    return JSON_mUtils_mLexers_mCore_Compile.LexerResult.<T, R>create_Accept(_td_T, _td_R);
  }
  public static <T, R> LexerResult<T, R> create_Accept(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    return new LexerResult_Accept<T, R>(_td_T, _td_R);
  }
  @Deprecated()
  public static <T, R> LexerResult<T, R> create_Accept() {
    return new LexerResult_Accept<T, R>(null, null);
  }
  public static <T, R> LexerResult<T, R> create_Reject(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, R err) {
    return new LexerResult_Reject<T, R>(_td_T, _td_R, err);
  }
  @Deprecated()
  public static <T, R> LexerResult<T, R> create_Reject(R err) {
    return new LexerResult_Reject<T, R>(null, null, err);
  }
  public static <T, R> LexerResult<T, R> create_Partial(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, T st) {
    return new LexerResult_Partial<T, R>(_td_T, _td_R, st);
  }
  @Deprecated()
  public static <T, R> LexerResult<T, R> create_Partial(T st) {
    return new LexerResult_Partial<T, R>(null, null, st);
  }
  public boolean is_Accept() { return this instanceof LexerResult_Accept; }
  public boolean is_Reject() { return this instanceof LexerResult_Reject; }
  public boolean is_Partial() { return this instanceof LexerResult_Partial; }
  public R dtor_err() {
    LexerResult<T, R> d = this;
    return ((LexerResult_Reject<T, R>)d)._err;
  }
  public T dtor_st() {
    LexerResult<T, R> d = this;
    return ((LexerResult_Partial<T, R>)d)._st;
  }
}
