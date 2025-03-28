// Class CursorError<R>
// Dafny class CursorError<R> compiled into Java
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
public abstract class CursorError<R> {
  protected dafny.TypeDescriptor<R> _td_R;
  public CursorError(dafny.TypeDescriptor<R> _td_R) {
    this._td_R = _td_R;
  }
  public static <R> dafny.TypeDescriptor<CursorError<R>> _typeDescriptor(dafny.TypeDescriptor<R> _td_R) {
    return (dafny.TypeDescriptor<CursorError<R>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<CursorError<R>>referenceWithInitializer(CursorError.class, () -> CursorError.<R>Default(_td_R));
  }

  public static <R> CursorError<R> Default(dafny.TypeDescriptor<R> _td_R) {
    return JSON_mUtils_mCursors_Compile.CursorError.<R>create_EOF(_td_R);
  }
  @Deprecated()
  public static <R> CursorError<R> Default() {
    dafny.TypeDescriptor<R> _td_R = null;
    return JSON_mUtils_mCursors_Compile.CursorError.<R>create_EOF(_td_R);
  }
  public static <R> CursorError<R> create_EOF(dafny.TypeDescriptor<R> _td_R) {
    return new CursorError_EOF<R>(_td_R);
  }
  @Deprecated()
  public static <R> CursorError<R> create_EOF() {
    return new CursorError_EOF<R>(null);
  }
  public static <R> CursorError<R> create_ExpectingByte(dafny.TypeDescriptor<R> _td_R, byte expected, short b) {
    return new CursorError_ExpectingByte<R>(_td_R, expected, b);
  }
  @Deprecated()
  public static <R> CursorError<R> create_ExpectingByte(byte expected, short b) {
    return new CursorError_ExpectingByte<R>(null, expected, b);
  }
  public static <R> CursorError<R> create_ExpectingAnyByte(dafny.TypeDescriptor<R> _td_R, dafny.DafnySequence<? extends java.lang.Byte> expected__sq, short b) {
    return new CursorError_ExpectingAnyByte<R>(_td_R, expected__sq, b);
  }
  @Deprecated()
  public static <R> CursorError<R> create_ExpectingAnyByte(dafny.DafnySequence<? extends java.lang.Byte> expected__sq, short b) {
    return new CursorError_ExpectingAnyByte<R>(null, expected__sq, b);
  }
  public static <R> CursorError<R> create_OtherError(dafny.TypeDescriptor<R> _td_R, R err) {
    return new CursorError_OtherError<R>(_td_R, err);
  }
  @Deprecated()
  public static <R> CursorError<R> create_OtherError(R err) {
    return new CursorError_OtherError<R>(null, err);
  }
  public boolean is_EOF() { return this instanceof CursorError_EOF; }
  public boolean is_ExpectingByte() { return this instanceof CursorError_ExpectingByte; }
  public boolean is_ExpectingAnyByte() { return this instanceof CursorError_ExpectingAnyByte; }
  public boolean is_OtherError() { return this instanceof CursorError_OtherError; }
  public byte dtor_expected() {
    CursorError<R> d = this;
    return ((CursorError_ExpectingByte<R>)d)._expected;
  }
  public short dtor_b() {
    CursorError<R> d = this;
    if (d instanceof CursorError_ExpectingByte) { return ((CursorError_ExpectingByte<R>)d)._b; }
    return ((CursorError_ExpectingAnyByte<R>)d)._b;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_expected__sq() {
    CursorError<R> d = this;
    return ((CursorError_ExpectingAnyByte<R>)d)._expected__sq;
  }
  public R dtor_err() {
    CursorError<R> d = this;
    return ((CursorError_OtherError<R>)d)._err;
  }
  public dafny.DafnySequence<? extends Character> ToString(dafny.TypeDescriptor<R> _td_R, java.util.function.Function<R, dafny.DafnySequence<? extends Character>> pr)
  {
    CursorError<R> _source0 = this;
    if (_source0.is_EOF()) {
      return dafny.DafnySequence.asString("Reached EOF");
    } else if (_source0.is_ExpectingByte()) {
      byte _0___mcc_h0 = ((JSON_mUtils_mCursors_Compile.CursorError_ExpectingByte<R>)_source0)._expected;
      short _1___mcc_h1 = ((JSON_mUtils_mCursors_Compile.CursorError_ExpectingByte<R>)_source0)._b;
      short _2_b = _1___mcc_h1;
      byte _3_b0 = _0___mcc_h0;
      dafny.DafnySequence<? extends Character> _4_c = ((java.lang.Integer.signum((_2_b)) == 1) ? (dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("'"), dafny.DafnySequence.<Character> of((char)dafny.Helpers.toInt(_2_b))), dafny.DafnySequence.asString("'"))) : (dafny.DafnySequence.asString("EOF")));
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Expecting '"), dafny.DafnySequence.<Character> of((char)java.lang.Byte.toUnsignedInt(_3_b0))), dafny.DafnySequence.asString("', read ")), _4_c);
    } else if (_source0.is_ExpectingAnyByte()) {
      dafny.DafnySequence<? extends java.lang.Byte> _5___mcc_h2 = ((JSON_mUtils_mCursors_Compile.CursorError_ExpectingAnyByte<R>)_source0)._expected__sq;
      short _6___mcc_h3 = ((JSON_mUtils_mCursors_Compile.CursorError_ExpectingAnyByte<R>)_source0)._b;
      short _7_b = _6___mcc_h3;
      dafny.DafnySequence<? extends java.lang.Byte> _8_bs0 = _5___mcc_h2;
      dafny.DafnySequence<? extends Character> _9_c = ((java.lang.Integer.signum((_7_b)) == 1) ? (dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("'"), dafny.DafnySequence.<Character> of((char)dafny.Helpers.toInt(_7_b))), dafny.DafnySequence.asString("'"))) : (dafny.DafnySequence.asString("EOF")));
      dafny.DafnySequence<? extends Character> _10_c0s = dafny.DafnySequence.Create(dafny.TypeDescriptor.CHAR, java.math.BigInteger.valueOf((_8_bs0).length()), ((java.util.function.Function<dafny.DafnySequence<? extends java.lang.Byte>, java.util.function.Function<java.math.BigInteger, Character>>)(_11_bs0) -> ((java.util.function.Function<java.math.BigInteger, Character>)(_12_idx_boxed0) -> {
        java.math.BigInteger _12_idx = ((java.math.BigInteger)(java.lang.Object)(_12_idx_boxed0));
        return (char)java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((_11_bs0).select(dafny.Helpers.toInt((_12_idx))))));
      })).apply(_8_bs0));
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Expecting one of '"), _10_c0s), dafny.DafnySequence.asString("', read ")), _9_c);
    } else {
      R _13___mcc_h4 = ((JSON_mUtils_mCursors_Compile.CursorError_OtherError<R>)_source0)._err;
      R _14_err = _13___mcc_h4;
      return ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((pr).apply(_14_err)));
    }
  }
}
