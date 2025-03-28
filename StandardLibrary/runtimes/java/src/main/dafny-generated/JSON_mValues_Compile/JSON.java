// Class JSON
// Dafny class JSON compiled into Java
package JSON_mValues_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class JSON {
  public JSON() {
  }
  private static final dafny.TypeDescriptor<JSON> _TYPE = dafny.TypeDescriptor.<JSON>referenceWithInitializer(JSON.class, () -> JSON.Default());
  public static dafny.TypeDescriptor<JSON> _typeDescriptor() {
    return (dafny.TypeDescriptor<JSON>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final JSON theDefault = JSON_mValues_Compile.JSON.create_Null();
  public static JSON Default() {
    return theDefault;
  }
  public static JSON create_Null() {
    return new JSON_Null();
  }
  public static JSON create_Bool(boolean b) {
    return new JSON_Bool(b);
  }
  public static JSON create_String(dafny.DafnySequence<? extends Character> str) {
    return new JSON_String(str);
  }
  public static JSON create_Number(Decimal num) {
    return new JSON_Number(num);
  }
  public static JSON create_Object(dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON>> obj) {
    return new JSON_Object(obj);
  }
  public static JSON create_Array(dafny.DafnySequence<? extends JSON> arr) {
    return new JSON_Array(arr);
  }
  public boolean is_Null() { return this instanceof JSON_Null; }
  public boolean is_Bool() { return this instanceof JSON_Bool; }
  public boolean is_String() { return this instanceof JSON_String; }
  public boolean is_Number() { return this instanceof JSON_Number; }
  public boolean is_Object() { return this instanceof JSON_Object; }
  public boolean is_Array() { return this instanceof JSON_Array; }
  public boolean dtor_b() {
    JSON d = this;
    return ((JSON_Bool)d)._b;
  }
  public dafny.DafnySequence<? extends Character> dtor_str() {
    JSON d = this;
    return ((JSON_String)d)._str;
  }
  public Decimal dtor_num() {
    JSON d = this;
    return ((JSON_Number)d)._num;
  }
  public dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON>> dtor_obj() {
    JSON d = this;
    return ((JSON_Object)d)._obj;
  }
  public dafny.DafnySequence<? extends JSON> dtor_arr() {
    JSON d = this;
    return ((JSON_Array)d)._arr;
  }
}
