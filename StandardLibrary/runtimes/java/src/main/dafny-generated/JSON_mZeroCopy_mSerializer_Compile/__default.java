// Class __default
// Dafny class __default compiled into Java
package JSON_mZeroCopy_mSerializer_Compile;

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
import JSON_mConcreteSyntax_mSpec_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<byte[], JSON_mErrors_Compile.SerializationError> Serialize(JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> js)
  {
    Wrappers_Compile.Result<byte[], JSON_mErrors_Compile.SerializationError> rbs = Wrappers_Compile.Result.<byte[], JSON_mErrors_Compile.SerializationError>Default(dafny.TypeDescriptor.BYTE_ARRAY, JSON_mErrors_Compile.SerializationError._typeDescriptor(), new byte[0]);
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _0_writer;
    _0_writer = __default.Text(js);
    Wrappers_Compile.Outcome<JSON_mErrors_Compile.SerializationError> _1_valueOrError0 = Wrappers_Compile.Outcome.<JSON_mErrors_Compile.SerializationError>Default(JSON_mErrors_Compile.SerializationError._typeDescriptor());
    _1_valueOrError0 = Wrappers_Compile.__default.<JSON_mErrors_Compile.SerializationError>Need(JSON_mErrors_Compile.SerializationError._typeDescriptor(), (_0_writer).Unsaturated_q(), JSON_mErrors_Compile.SerializationError.create_OutOfMemory());
    if ((_1_valueOrError0).IsFailure(JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      rbs = (_1_valueOrError0).<byte[]>PropagateFailure(JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.TypeDescriptor.BYTE_ARRAY);
      return rbs;
    }
    byte[] _2_bs;
    byte[] _out0;
    _out0 = (_0_writer).ToArray();
    _2_bs = _out0;
    rbs = Wrappers_Compile.Result.<byte[], JSON_mErrors_Compile.SerializationError>create_Success(dafny.TypeDescriptor.BYTE_ARRAY, JSON_mErrors_Compile.SerializationError._typeDescriptor(), _2_bs);
    return rbs;
  }
  public static Wrappers_Compile.Result<java.lang.Integer, JSON_mErrors_Compile.SerializationError> SerializeTo(JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> js, byte[] dest)
  {
    Wrappers_Compile.Result<java.lang.Integer, JSON_mErrors_Compile.SerializationError> len = Wrappers_Compile.Result.<java.lang.Integer, JSON_mErrors_Compile.SerializationError>Default(BoundedInts_Compile.uint32._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), 0);
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _0_writer;
    _0_writer = __default.Text(js);
    Wrappers_Compile.Outcome<JSON_mErrors_Compile.SerializationError> _1_valueOrError0 = Wrappers_Compile.Outcome.<JSON_mErrors_Compile.SerializationError>Default(JSON_mErrors_Compile.SerializationError._typeDescriptor());
    _1_valueOrError0 = Wrappers_Compile.__default.<JSON_mErrors_Compile.SerializationError>Need(JSON_mErrors_Compile.SerializationError._typeDescriptor(), (_0_writer).Unsaturated_q(), JSON_mErrors_Compile.SerializationError.create_OutOfMemory());
    if ((_1_valueOrError0).IsFailure(JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      len = (_1_valueOrError0).<java.lang.Integer>PropagateFailure(JSON_mErrors_Compile.SerializationError._typeDescriptor(), BoundedInts_Compile.uint32._typeDescriptor());
      return len;
    }
    Wrappers_Compile.Outcome<JSON_mErrors_Compile.SerializationError> _2_valueOrError1 = Wrappers_Compile.Outcome.<JSON_mErrors_Compile.SerializationError>Default(JSON_mErrors_Compile.SerializationError._typeDescriptor());
    _2_valueOrError1 = Wrappers_Compile.__default.<JSON_mErrors_Compile.SerializationError>Need(JSON_mErrors_Compile.SerializationError._typeDescriptor(), (dafny.Helpers.unsignedToBigInteger((_0_writer).dtor_length())).compareTo(java.math.BigInteger.valueOf(java.lang.reflect.Array.getLength((dest)))) <= 0, JSON_mErrors_Compile.SerializationError.create_OutOfMemory());
    if ((_2_valueOrError1).IsFailure(JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      len = (_2_valueOrError1).<java.lang.Integer>PropagateFailure(JSON_mErrors_Compile.SerializationError._typeDescriptor(), BoundedInts_Compile.uint32._typeDescriptor());
      return len;
    }
    (_0_writer).CopyTo(dest);
    len = Wrappers_Compile.Result.<java.lang.Integer, JSON_mErrors_Compile.SerializationError>create_Success(BoundedInts_Compile.uint32._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), (_0_writer).dtor_length());
    return len;
  }
  public static JSON_mUtils_mViews_mWriters_Compile.Writer__ Text(JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> js) {
    return __default.JSON(js, JSON_mUtils_mViews_mWriters_Compile.Writer__.Empty());
  }
  public static JSON_mUtils_mViews_mWriters_Compile.Writer__ JSON(JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> js, JSON_mUtils_mViews_mWriters_Compile.Writer__ writer)
  {
    return (((writer).Append((js).dtor_before())).Then(((java.util.function.Function<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>, java.util.function.Function<JSON_mUtils_mViews_mWriters_Compile.Writer__, JSON_mUtils_mViews_mWriters_Compile.Writer__>>)(_0_js) -> ((java.util.function.Function<JSON_mUtils_mViews_mWriters_Compile.Writer__, JSON_mUtils_mViews_mWriters_Compile.Writer__>)(_1_wr_boxed0) -> {
      JSON_mUtils_mViews_mWriters_Compile.Writer__ _1_wr = ((JSON_mUtils_mViews_mWriters_Compile.Writer__)(java.lang.Object)(_1_wr_boxed0));
      return __default.Value((_0_js).dtor_t(), _1_wr);
    })).apply(js))).Append((js).dtor_after());
  }
  public static JSON_mUtils_mViews_mWriters_Compile.Writer__ Value(JSON_mGrammar_Compile.Value v, JSON_mUtils_mViews_mWriters_Compile.Writer__ writer)
  {
    JSON_mGrammar_Compile.Value _source0 = v;
    if (_source0.is_Null()) {
      JSON_mUtils_mViews_mCore_Compile.View__ _0___mcc_h0 = ((JSON_mGrammar_Compile.Value_Null)_source0)._n;
      JSON_mUtils_mViews_mCore_Compile.View__ _1_n = _0___mcc_h0;
      return (writer).Append(_1_n);
    } else if (_source0.is_Bool()) {
      JSON_mUtils_mViews_mCore_Compile.View__ _2___mcc_h1 = ((JSON_mGrammar_Compile.Value_Bool)_source0)._b;
      JSON_mUtils_mViews_mCore_Compile.View__ _3_b = _2___mcc_h1;
      JSON_mUtils_mViews_mWriters_Compile.Writer__ _4_wr = (writer).Append(_3_b);
      return _4_wr;
    } else if (_source0.is_String()) {
      JSON_mGrammar_Compile.jstring _5___mcc_h2 = ((JSON_mGrammar_Compile.Value_String)_source0)._str;
      JSON_mGrammar_Compile.jstring _6_str = _5___mcc_h2;
      JSON_mUtils_mViews_mWriters_Compile.Writer__ _7_wr = __default.String(_6_str, writer);
      return _7_wr;
    } else if (_source0.is_Number()) {
      JSON_mGrammar_Compile.jnumber _8___mcc_h3 = ((JSON_mGrammar_Compile.Value_Number)_source0)._num;
      JSON_mGrammar_Compile.jnumber _9_num = _8___mcc_h3;
      JSON_mUtils_mViews_mWriters_Compile.Writer__ _10_wr = __default.Number(_9_num, writer);
      return _10_wr;
    } else if (_source0.is_Object()) {
      JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _11___mcc_h4 = ((JSON_mGrammar_Compile.Value_Object)_source0)._obj;
      JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _12_obj = _11___mcc_h4;
      JSON_mUtils_mViews_mWriters_Compile.Writer__ _13_wr = __default.Object(_12_obj, writer);
      return _13_wr;
    } else {
      JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _14___mcc_h5 = ((JSON_mGrammar_Compile.Value_Array)_source0)._arr;
      JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _15_arr = _14___mcc_h5;
      JSON_mUtils_mViews_mWriters_Compile.Writer__ _16_wr = __default.Array(_15_arr, writer);
      return _16_wr;
    }
  }
  public static JSON_mUtils_mViews_mWriters_Compile.Writer__ String(JSON_mGrammar_Compile.jstring str, JSON_mUtils_mViews_mWriters_Compile.Writer__ writer)
  {
    return (((writer).Append((str).dtor_lq())).Append((str).dtor_contents())).Append((str).dtor_rq());
  }
  public static JSON_mUtils_mViews_mWriters_Compile.Writer__ Number(JSON_mGrammar_Compile.jnumber num, JSON_mUtils_mViews_mWriters_Compile.Writer__ writer)
  {
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _0_wr = ((writer).Append((num).dtor_minus())).Append((num).dtor_num());
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _1_wr = ((((num).dtor_frac()).is_NonEmpty()) ? (((_0_wr).Append((((num).dtor_frac()).dtor_t()).dtor_period())).Append((((num).dtor_frac()).dtor_t()).dtor_num())) : (_0_wr));
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _2_wr = ((((num).dtor_exp()).is_NonEmpty()) ? ((((_1_wr).Append((((num).dtor_exp()).dtor_t()).dtor_e())).Append((((num).dtor_exp()).dtor_t()).dtor_sign())).Append((((num).dtor_exp()).dtor_t()).dtor_num())) : (_1_wr));
    return _2_wr;
  }
  public static JSON_mUtils_mViews_mWriters_Compile.Writer__ StructuralView(JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__> st, JSON_mUtils_mViews_mWriters_Compile.Writer__ writer)
  {
    return (((writer).Append((st).dtor_before())).Append((st).dtor_t())).Append((st).dtor_after());
  }
  public static JSON_mUtils_mViews_mWriters_Compile.Writer__ Object(JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> obj, JSON_mUtils_mViews_mWriters_Compile.Writer__ writer)
  {
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _0_wr = __default.StructuralView((obj).dtor_l(), writer);
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _1_wr = __default.Members(obj, _0_wr);
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _2_wr = __default.StructuralView((obj).dtor_r(), _1_wr);
    return _2_wr;
  }
  public static JSON_mUtils_mViews_mWriters_Compile.Writer__ Array(JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> arr, JSON_mUtils_mViews_mWriters_Compile.Writer__ writer)
  {
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _0_wr = __default.StructuralView((arr).dtor_l(), writer);
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _1_wr = __default.Items(arr, _0_wr);
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _2_wr = __default.StructuralView((arr).dtor_r(), _1_wr);
    return _2_wr;
  }
  public static JSON_mUtils_mViews_mWriters_Compile.Writer__ Members(JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> obj, JSON_mUtils_mViews_mWriters_Compile.Writer__ writer)
  {
    JSON_mUtils_mViews_mWriters_Compile.Writer__ wr = JSON_mUtils_mViews_mWriters_Compile.Writer.defaultValue();
    if(true) {
      JSON_mUtils_mViews_mWriters_Compile.Writer__ _out0;
      _out0 = __default.MembersImpl(obj, writer);
      wr = _out0;
    }
    return wr;
  }
  public static JSON_mUtils_mViews_mWriters_Compile.Writer__ Items(JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> arr, JSON_mUtils_mViews_mWriters_Compile.Writer__ writer)
  {
    JSON_mUtils_mViews_mWriters_Compile.Writer__ wr = JSON_mUtils_mViews_mWriters_Compile.Writer.defaultValue();
    if(true) {
      JSON_mUtils_mViews_mWriters_Compile.Writer__ _out0;
      _out0 = __default.ItemsImpl(arr, writer);
      wr = _out0;
    }
    return wr;
  }
  public static JSON_mUtils_mViews_mWriters_Compile.Writer__ MembersImpl(JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> obj, JSON_mUtils_mViews_mWriters_Compile.Writer__ writer)
  {
    JSON_mUtils_mViews_mWriters_Compile.Writer__ wr = JSON_mUtils_mViews_mWriters_Compile.Writer.defaultValue();
    if(true) {
      wr = writer;
      dafny.DafnySequence<? extends JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__>> _0_members;
      _0_members = (obj).dtor_data();
      java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((_0_members).length());
      for (java.math.BigInteger _1_i = java.math.BigInteger.ZERO; _1_i.compareTo(_hi0) < 0; _1_i = _1_i.add(java.math.BigInteger.ONE)) {
        wr = __default.Member(((JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__>)(java.lang.Object)((_0_members).select(dafny.Helpers.toInt((_1_i))))), wr);
      }
    }
    return wr;
  }
  public static JSON_mUtils_mViews_mWriters_Compile.Writer__ ItemsImpl(JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> arr, JSON_mUtils_mViews_mWriters_Compile.Writer__ writer)
  {
    JSON_mUtils_mViews_mWriters_Compile.Writer__ wr = JSON_mUtils_mViews_mWriters_Compile.Writer.defaultValue();
    if(true) {
      wr = writer;
      dafny.DafnySequence<? extends JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__>> _0_items;
      _0_items = (arr).dtor_data();
      java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((_0_items).length());
      for (java.math.BigInteger _1_i = java.math.BigInteger.ZERO; _1_i.compareTo(_hi0) < 0; _1_i = _1_i.add(java.math.BigInteger.ONE)) {
        wr = __default.Item(((JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__>)(java.lang.Object)((_0_items).select(dafny.Helpers.toInt((_1_i))))), wr);
      }
    }
    return wr;
  }
  public static JSON_mUtils_mViews_mWriters_Compile.Writer__ Member(JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__> m, JSON_mUtils_mViews_mWriters_Compile.Writer__ writer)
  {
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _0_wr = __default.String(((m).dtor_t()).dtor_k(), writer);
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _1_wr = __default.StructuralView(((m).dtor_t()).dtor_colon(), _0_wr);
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _2_wr = __default.Value(((m).dtor_t()).dtor_v(), _1_wr);
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _3_wr = ((((m).dtor_suffix()).is_Empty()) ? (_2_wr) : (__default.StructuralView(((m).dtor_suffix()).dtor_t(), _2_wr)));
    return _3_wr;
  }
  public static JSON_mUtils_mViews_mWriters_Compile.Writer__ Item(JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__> m, JSON_mUtils_mViews_mWriters_Compile.Writer__ writer)
  {
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _0_wr = __default.Value((m).dtor_t(), writer);
    JSON_mUtils_mViews_mWriters_Compile.Writer__ _1_wr = ((((m).dtor_suffix()).is_Empty()) ? (_0_wr) : (__default.StructuralView(((m).dtor_suffix()).dtor_t(), _0_wr)));
    return _1_wr;
  }
  @Override
  public java.lang.String toString() {
    return "JSON.ZeroCopy.Serializer._default";
  }
}
