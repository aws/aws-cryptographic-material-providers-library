// Class SerializationError
// Dafny class SerializationError compiled into Java
package JSON_mErrors_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class SerializationError {
  public SerializationError() {
  }
  private static final dafny.TypeDescriptor<SerializationError> _TYPE = dafny.TypeDescriptor.<SerializationError>referenceWithInitializer(SerializationError.class, () -> SerializationError.Default());
  public static dafny.TypeDescriptor<SerializationError> _typeDescriptor() {
    return (dafny.TypeDescriptor<SerializationError>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SerializationError theDefault = JSON_mErrors_Compile.SerializationError.create_OutOfMemory();
  public static SerializationError Default() {
    return theDefault;
  }
  public static SerializationError create_OutOfMemory() {
    return new SerializationError_OutOfMemory();
  }
  public static SerializationError create_IntTooLarge(java.math.BigInteger i) {
    return new SerializationError_IntTooLarge(i);
  }
  public static SerializationError create_StringTooLong(dafny.DafnySequence<? extends Character> s) {
    return new SerializationError_StringTooLong(s);
  }
  public static SerializationError create_InvalidUnicode() {
    return new SerializationError_InvalidUnicode();
  }
  public boolean is_OutOfMemory() { return this instanceof SerializationError_OutOfMemory; }
  public boolean is_IntTooLarge() { return this instanceof SerializationError_IntTooLarge; }
  public boolean is_StringTooLong() { return this instanceof SerializationError_StringTooLong; }
  public boolean is_InvalidUnicode() { return this instanceof SerializationError_InvalidUnicode; }
  public java.math.BigInteger dtor_i() {
    SerializationError d = this;
    return ((SerializationError_IntTooLarge)d)._i;
  }
  public dafny.DafnySequence<? extends Character> dtor_s() {
    SerializationError d = this;
    return ((SerializationError_StringTooLong)d)._s;
  }
  public dafny.DafnySequence<? extends Character> ToString() {
    SerializationError _source0 = this;
    if (_source0.is_OutOfMemory()) {
      return dafny.DafnySequence.asString("Out of memory");
    } else if (_source0.is_IntTooLarge()) {
      java.math.BigInteger _0___mcc_h0 = ((JSON_mErrors_Compile.SerializationError_IntTooLarge)_source0)._i;
      java.math.BigInteger _1_i = _0___mcc_h0;
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Integer too large: "), JSON_mUtils_mStr_Compile.__default.OfInt(_1_i, java.math.BigInteger.valueOf(10L)));
    } else if (_source0.is_StringTooLong()) {
      dafny.DafnySequence<? extends Character> _2___mcc_h1 = ((JSON_mErrors_Compile.SerializationError_StringTooLong)_source0)._s;
      dafny.DafnySequence<? extends Character> _3_s = _2___mcc_h1;
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("String too long: "), _3_s);
    } else {
      return dafny.DafnySequence.asString("Invalid Unicode sequence");
    }
  }
}
