// Class Value
// Dafny class Value compiled into Java
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
public abstract class Value {
  public Value() {
  }
  private static final dafny.TypeDescriptor<Value> _TYPE = dafny.TypeDescriptor.<Value>referenceWithInitializer(Value.class, () -> Value.Default());
  public static dafny.TypeDescriptor<Value> _typeDescriptor() {
    return (dafny.TypeDescriptor<Value>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Value theDefault = JSON_mGrammar_Compile.Value.create_Null(jnull.defaultValue());
  public static Value Default() {
    return theDefault;
  }
  public static Value create_Null(JSON_mUtils_mViews_mCore_Compile.View__ n) {
    return new Value_Null(n);
  }
  public static Value create_Bool(JSON_mUtils_mViews_mCore_Compile.View__ b) {
    return new Value_Bool(b);
  }
  public static Value create_String(jstring str) {
    return new Value_String(str);
  }
  public static Value create_Number(jnumber num) {
    return new Value_Number(num);
  }
  public static Value create_Object(Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> obj) {
    return new Value_Object(obj);
  }
  public static Value create_Array(Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> arr) {
    return new Value_Array(arr);
  }
  public boolean is_Null() { return this instanceof Value_Null; }
  public boolean is_Bool() { return this instanceof Value_Bool; }
  public boolean is_String() { return this instanceof Value_String; }
  public boolean is_Number() { return this instanceof Value_Number; }
  public boolean is_Object() { return this instanceof Value_Object; }
  public boolean is_Array() { return this instanceof Value_Array; }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_n() {
    Value d = this;
    return ((Value_Null)d)._n;
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ dtor_b() {
    Value d = this;
    return ((Value_Bool)d)._b;
  }
  public jstring dtor_str() {
    Value d = this;
    return ((Value_String)d)._str;
  }
  public jnumber dtor_num() {
    Value d = this;
    return ((Value_Number)d)._num;
  }
  public Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> dtor_obj() {
    Value d = this;
    return ((Value_Object)d)._obj;
  }
  public Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> dtor_arr() {
    Value d = this;
    return ((Value_Array)d)._arr;
  }
}
