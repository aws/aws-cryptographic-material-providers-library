// Class __default
// Dafny class __default compiled into Java
package JSON_mConcreteSyntax_mSpec_Compile;

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
import JSON_mGrammar_Compile.*;
import JSON_mSerializer_mByteStrConversion_Compile.*;
import JSON_mSerializer_Compile.*;
import JSON_mDeserializer_mUint16StrConversion_Compile.*;
import JSON_mDeserializer_mByteStrConversion_Compile.*;
import JSON_mDeserializer_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> View(JSON_mUtils_mViews_mCore_Compile.View__ v) {
    return (v).Bytes();
  }
  public static <__T> dafny.DafnySequence<? extends java.lang.Byte> Structural(dafny.TypeDescriptor<__T> _td___T, JSON_mGrammar_Compile.Structural<__T> self, java.util.function.Function<__T, dafny.DafnySequence<? extends java.lang.Byte>> fT)
  {
    return dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(__default.View((self).dtor_before()), ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((fT).apply((self).dtor_t())))), __default.View((self).dtor_after()));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> StructuralView(JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__> self) {
    return __default.<JSON_mUtils_mViews_mCore_Compile.View__>Structural(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), self, __default::View);
  }
  public static <__T> dafny.DafnySequence<? extends java.lang.Byte> Maybe(dafny.TypeDescriptor<__T> _td___T, JSON_mGrammar_Compile.Maybe<__T> self, java.util.function.Function<__T, dafny.DafnySequence<? extends java.lang.Byte>> fT)
  {
    if ((self).is_Empty()) {
      return dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    } else {
      return ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((fT).apply((self).dtor_t())));
    }
  }
  public static <__T> dafny.DafnySequence<? extends java.lang.Byte> ConcatBytes(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> ts, java.util.function.Function<__T, dafny.DafnySequence<? extends java.lang.Byte>> fT)
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0___accumulator = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((ts).length())).signum() == 0) {
        return dafny.DafnySequence.<java.lang.Byte>concatenate(_0___accumulator, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      } else {
        _0___accumulator = dafny.DafnySequence.<java.lang.Byte>concatenate(_0___accumulator, ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((fT).apply(((__T)(java.lang.Object)((ts).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))))));
        dafny.DafnySequence<? extends __T> _in0 = (ts).drop(java.math.BigInteger.ONE);
        java.util.function.Function<__T, dafny.DafnySequence<? extends java.lang.Byte>> _in1 = fT;
        ts = _in0;
        fT = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static <__D, __S> dafny.DafnySequence<? extends java.lang.Byte> Bracketed(dafny.TypeDescriptor<__D> _td___D, dafny.TypeDescriptor<__S> _td___S, JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, __D, __S, JSON_mUtils_mViews_mCore_Compile.View__> self, java.util.function.Function<JSON_mGrammar_Compile.Suffixed<__D, __S>, dafny.DafnySequence<? extends java.lang.Byte>> fDatum)
  {
    return dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(__default.StructuralView((self).dtor_l()), __default.<JSON_mGrammar_Compile.Suffixed<__D, __S>>ConcatBytes(JSON_mGrammar_Compile.Suffixed.<__D, __S>_typeDescriptor(_td___D, _td___S), (self).dtor_data(), fDatum)), __default.StructuralView((self).dtor_r()));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> KeyValue(JSON_mGrammar_Compile.jKeyValue self) {
    return dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(__default.String((self).dtor_k()), __default.StructuralView((self).dtor_colon())), __default.Value((self).dtor_v()));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Frac(JSON_mGrammar_Compile.jfrac self) {
    return dafny.DafnySequence.<java.lang.Byte>concatenate(__default.View((self).dtor_period()), __default.View((self).dtor_num()));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Exp(JSON_mGrammar_Compile.jexp self) {
    return dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(__default.View((self).dtor_e()), __default.View((self).dtor_sign())), __default.View((self).dtor_num()));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Number(JSON_mGrammar_Compile.jnumber self) {
    return dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(__default.View((self).dtor_minus()), __default.View((self).dtor_num())), __default.<JSON_mGrammar_Compile.jfrac>Maybe(JSON_mGrammar_Compile.jfrac._typeDescriptor(), (self).dtor_frac(), __default::Frac)), __default.<JSON_mGrammar_Compile.jexp>Maybe(JSON_mGrammar_Compile.jexp._typeDescriptor(), (self).dtor_exp(), __default::Exp));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> String(JSON_mGrammar_Compile.jstring self) {
    return dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(__default.View((self).dtor_lq()), __default.View((self).dtor_contents())), __default.View((self).dtor_rq()));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> CommaSuffix(JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>> c) {
    return __default.<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>>Maybe(JSON_mGrammar_Compile.Structural.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()), c, __default::StructuralView);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Member(JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__> self) {
    return dafny.DafnySequence.<java.lang.Byte>concatenate(__default.KeyValue((self).dtor_t()), __default.CommaSuffix((self).dtor_suffix()));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Item(JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__> self) {
    return dafny.DafnySequence.<java.lang.Byte>concatenate(__default.Value((self).dtor_t()), __default.CommaSuffix((self).dtor_suffix()));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Object(JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> obj) {
    return __default.<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__>Bracketed(JSON_mGrammar_Compile.jKeyValue._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), obj, ((java.util.function.Function<JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>, java.util.function.Function<JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__>, dafny.DafnySequence<? extends java.lang.Byte>>>)(_0_obj) -> ((java.util.function.Function<JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__>, dafny.DafnySequence<? extends java.lang.Byte>>)(_1_d_boxed0) -> {
      JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__> _1_d = ((JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__>)(java.lang.Object)(_1_d_boxed0));
      return __default.Member(_1_d);
    })).apply(obj));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Array(JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> arr) {
    return __default.<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__>Bracketed(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), arr, ((java.util.function.Function<JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>, java.util.function.Function<JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__>, dafny.DafnySequence<? extends java.lang.Byte>>>)(_0_arr) -> ((java.util.function.Function<JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__>, dafny.DafnySequence<? extends java.lang.Byte>>)(_1_d_boxed0) -> {
      JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__> _1_d = ((JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__>)(java.lang.Object)(_1_d_boxed0));
      return __default.Item(_1_d);
    })).apply(arr));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Value(JSON_mGrammar_Compile.Value self) {
    JSON_mGrammar_Compile.Value _source0 = self;
    if (_source0.is_Null()) {
      JSON_mUtils_mViews_mCore_Compile.View__ _0___mcc_h0 = ((JSON_mGrammar_Compile.Value_Null)_source0)._n;
      JSON_mUtils_mViews_mCore_Compile.View__ _1_n = _0___mcc_h0;
      return __default.View(_1_n);
    } else if (_source0.is_Bool()) {
      JSON_mUtils_mViews_mCore_Compile.View__ _2___mcc_h1 = ((JSON_mGrammar_Compile.Value_Bool)_source0)._b;
      JSON_mUtils_mViews_mCore_Compile.View__ _3_b = _2___mcc_h1;
      return __default.View(_3_b);
    } else if (_source0.is_String()) {
      JSON_mGrammar_Compile.jstring _4___mcc_h2 = ((JSON_mGrammar_Compile.Value_String)_source0)._str;
      JSON_mGrammar_Compile.jstring _5_str = _4___mcc_h2;
      return __default.String(_5_str);
    } else if (_source0.is_Number()) {
      JSON_mGrammar_Compile.jnumber _6___mcc_h3 = ((JSON_mGrammar_Compile.Value_Number)_source0)._num;
      JSON_mGrammar_Compile.jnumber _7_num = _6___mcc_h3;
      return __default.Number(_7_num);
    } else if (_source0.is_Object()) {
      JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _8___mcc_h4 = ((JSON_mGrammar_Compile.Value_Object)_source0)._obj;
      JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _9_obj = _8___mcc_h4;
      return __default.Object(_9_obj);
    } else {
      JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _10___mcc_h5 = ((JSON_mGrammar_Compile.Value_Array)_source0)._arr;
      JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _11_arr = _10___mcc_h5;
      return __default.Array(_11_arr);
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> JSON(JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> js) {
    return __default.<JSON_mGrammar_Compile.Value>Structural(JSON_mGrammar_Compile.Value._typeDescriptor(), js, __default::Value);
  }
  @Override
  public java.lang.String toString() {
    return "JSON.ConcreteSyntax.Spec._default";
  }
}
