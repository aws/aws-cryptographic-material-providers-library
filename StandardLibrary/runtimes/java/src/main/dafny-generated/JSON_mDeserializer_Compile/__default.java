// Class __default
// Dafny class __default compiled into Java
package JSON_mDeserializer_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean Bool(JSON_mUtils_mViews_mCore_Compile.View__ js) {
    return ((js).At(0)) == (((byte) ('t')));
  }
  public static JSON_mErrors_Compile.DeserializationError UnsupportedEscape16(dafny.DafnySequence<? extends java.lang.Short> code) {
    return JSON_mErrors_Compile.DeserializationError.create_UnsupportedEscape((UnicodeStrings_Compile.__default.FromUTF16Checked(code)).UnwrapOr(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("Couldn't decode UTF-16")));
  }
  public static short ToNat16(dafny.DafnySequence<? extends java.lang.Short> str) {
    java.math.BigInteger _0_hd = JSON_mDeserializer_mUint16StrConversion_Compile.__default.ToNat__any(str, java.math.BigInteger.valueOf(16L), __default.HEX__TABLE__16());
    return (_0_hd).shortValue();
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Short>, JSON_mErrors_Compile.DeserializationError> Unescape(dafny.DafnySequence<? extends java.lang.Short> str, java.math.BigInteger start, dafny.DafnySequence<? extends java.lang.Short> prefix)
  {
    TAIL_CALL_START: while (true) {
      if ((start).compareTo(java.math.BigInteger.valueOf((str).length())) >= 0) {
        return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Short>, JSON_mErrors_Compile.DeserializationError>create_Success(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), prefix);
      } else if ((((short)(java.lang.Object)((str).select(dafny.Helpers.toInt((start)))))) == (((short) ('\\')))) {
        if (java.util.Objects.equals(java.math.BigInteger.valueOf((str).length()), (start).add(java.math.BigInteger.ONE))) {
          return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Short>, JSON_mErrors_Compile.DeserializationError>create_Failure(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mErrors_Compile.DeserializationError.create_EscapeAtEOS());
        } else {
          short _0_c = ((short)(java.lang.Object)((str).select(dafny.Helpers.toInt(((start).add(java.math.BigInteger.ONE))))));
          if ((_0_c) == (((short) ('u')))) {
            if ((java.math.BigInteger.valueOf((str).length())).compareTo((start).add(java.math.BigInteger.valueOf(6L))) <= 0) {
              return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Short>, JSON_mErrors_Compile.DeserializationError>create_Failure(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mErrors_Compile.DeserializationError.create_EscapeAtEOS());
            } else {
              dafny.DafnySequence<? extends java.lang.Short> _1_code = (str).subsequence(dafny.Helpers.toInt(((start).add(java.math.BigInteger.valueOf(2L)))), dafny.Helpers.toInt(((start).add(java.math.BigInteger.valueOf(6L)))));
              if (((java.util.function.Function<dafny.DafnySequence<? extends java.lang.Short>, Boolean>)(_2_code) -> dafny.Helpers.Quantifier((_2_code).UniqueElements(), false, ((_exists_var_0_boxed0) -> {
                short _exists_var_0 = ((short)(java.lang.Object)(_exists_var_0_boxed0));
                short _3_c = (short)_exists_var_0;
                return ((_2_code).contains(_3_c)) && (!(__default.HEX__TABLE__16()).<java.lang.Short>contains(_3_c));
              }))).apply(_1_code)) {
                return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Short>, JSON_mErrors_Compile.DeserializationError>create_Failure(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), __default.UnsupportedEscape16(_1_code));
              } else {
                short _4_hd = __default.ToNat16(_1_code);
                dafny.DafnySequence<? extends java.lang.Short> _in0 = str;
                java.math.BigInteger _in1 = (start).add(java.math.BigInteger.valueOf(6L));
                dafny.DafnySequence<? extends java.lang.Short> _in2 = dafny.DafnySequence.<java.lang.Short>concatenate(prefix, dafny.DafnySequence.<java.lang.Short> of(_4_hd));
                str = _in0;
                start = _in1;
                prefix = _in2;
                continue TAIL_CALL_START;
              }
            }
          } else {
            short _5_unescaped = (((_0_c) == ((short) 34)) ? ((short) 34) : ((((_0_c) == ((short) 92)) ? ((short) 92) : ((((_0_c) == ((short) 98)) ? ((short) 8) : ((((_0_c) == ((short) 102)) ? ((short) 12) : ((((_0_c) == ((short) 110)) ? ((short) 10) : ((((_0_c) == ((short) 114)) ? ((short) 13) : ((((_0_c) == ((short) 116)) ? ((short) 9) : ((short) 0))))))))))))));
            if ((dafny.Helpers.unsignedToBigInteger(_5_unescaped)).signum() == 0) {
              return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Short>, JSON_mErrors_Compile.DeserializationError>create_Failure(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), __default.UnsupportedEscape16((str).subsequence(dafny.Helpers.toInt((start)), dafny.Helpers.toInt(((start).add(java.math.BigInteger.valueOf(2L)))))));
            } else {
              dafny.DafnySequence<? extends java.lang.Short> _in3 = str;
              java.math.BigInteger _in4 = (start).add(java.math.BigInteger.valueOf(2L));
              dafny.DafnySequence<? extends java.lang.Short> _in5 = dafny.DafnySequence.<java.lang.Short>concatenate(prefix, dafny.DafnySequence.<java.lang.Short> of(_5_unescaped));
              str = _in3;
              start = _in4;
              prefix = _in5;
              continue TAIL_CALL_START;
            }
          }
        }
      } else {
        dafny.DafnySequence<? extends java.lang.Short> _in6 = str;
        java.math.BigInteger _in7 = (start).add(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends java.lang.Short> _in8 = dafny.DafnySequence.<java.lang.Short>concatenate(prefix, dafny.DafnySequence.<java.lang.Short> of(((short)(java.lang.Object)((str).select(dafny.Helpers.toInt((start)))))));
        str = _in6;
        start = _in7;
        prefix = _in8;
        continue TAIL_CALL_START;
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, JSON_mErrors_Compile.DeserializationError> String(JSON_mGrammar_Compile.jstring js) {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, JSON_mErrors_Compile.DeserializationError> _0_valueOrError0 = (UnicodeStrings_Compile.__default.FromUTF8Checked(((js).dtor_contents()).Bytes())).<JSON_mErrors_Compile.DeserializationError>ToResult_k(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mErrors_Compile.DeserializationError.create_InvalidUnicode());
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.DafnySequence<? extends Character>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    } else {
      dafny.DafnySequence<? extends Character> _1_asUtf32 = (_0_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mErrors_Compile.DeserializationError._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Short>, JSON_mErrors_Compile.DeserializationError> _2_valueOrError1 = (UnicodeStrings_Compile.__default.ToUTF16Checked(_1_asUtf32)).<JSON_mErrors_Compile.DeserializationError>ToResult_k(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mErrors_Compile.DeserializationError.create_InvalidUnicode());
      if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
        return (_2_valueOrError1).<dafny.DafnySequence<? extends Character>>PropagateFailure(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      } else {
        dafny.DafnySequence<? extends java.lang.Short> _3_asUint16 = (_2_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor());
        Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Short>, JSON_mErrors_Compile.DeserializationError> _4_valueOrError2 = __default.Unescape(_3_asUint16, java.math.BigInteger.ZERO, dafny.DafnySequence.<java.lang.Short> empty(BoundedInts_Compile.uint16._typeDescriptor()));
        if ((_4_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
          return (_4_valueOrError2).<dafny.DafnySequence<? extends Character>>PropagateFailure(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        } else {
          dafny.DafnySequence<? extends java.lang.Short> _5_unescaped = (_4_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor());
          return (UnicodeStrings_Compile.__default.FromUTF16Checked(_5_unescaped)).<JSON_mErrors_Compile.DeserializationError>ToResult_k(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mErrors_Compile.DeserializationError.create_InvalidUnicode());
        }
      }
    }
  }
  public static Wrappers_Compile.Result<java.math.BigInteger, JSON_mErrors_Compile.DeserializationError> ToInt(JSON_mUtils_mViews_mCore_Compile.View__ sign, JSON_mUtils_mViews_mCore_Compile.View__ n)
  {
    java.math.BigInteger _0_n = JSON_mDeserializer_mByteStrConversion_Compile.__default.ToNat__any((n).Bytes(), java.math.BigInteger.valueOf(10L), __default.DIGITS());
    return Wrappers_Compile.Result.<java.math.BigInteger, JSON_mErrors_Compile.DeserializationError>create_Success(dafny.TypeDescriptor.BIG_INTEGER, JSON_mErrors_Compile.DeserializationError._typeDescriptor(), (((sign).Char_q('-')) ? ((java.math.BigInteger.ZERO).subtract(_0_n)) : (_0_n)));
  }
  public static Wrappers_Compile.Result<JSON_mValues_Compile.Decimal, JSON_mErrors_Compile.DeserializationError> Number(JSON_mGrammar_Compile.jnumber js) {
    JSON_mGrammar_Compile.jnumber _let_tmp_rhs0 = js;
    JSON_mUtils_mViews_mCore_Compile.View__ _0_minus = ((JSON_mGrammar_Compile.jnumber)_let_tmp_rhs0)._minus;
    JSON_mUtils_mViews_mCore_Compile.View__ _1_num = ((JSON_mGrammar_Compile.jnumber)_let_tmp_rhs0)._num;
    JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac> _2_frac = ((JSON_mGrammar_Compile.jnumber)_let_tmp_rhs0)._frac;
    JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp> _3_exp = ((JSON_mGrammar_Compile.jnumber)_let_tmp_rhs0)._exp;
    Wrappers_Compile.Result<java.math.BigInteger, JSON_mErrors_Compile.DeserializationError> _4_valueOrError0 = __default.ToInt(_0_minus, _1_num);
    if ((_4_valueOrError0).IsFailure(dafny.TypeDescriptor.BIG_INTEGER, JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
      return (_4_valueOrError0).<JSON_mValues_Compile.Decimal>PropagateFailure(dafny.TypeDescriptor.BIG_INTEGER, JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.Decimal._typeDescriptor());
    } else {
      java.math.BigInteger _5_n = (_4_valueOrError0).Extract(dafny.TypeDescriptor.BIG_INTEGER, JSON_mErrors_Compile.DeserializationError._typeDescriptor());
      Wrappers_Compile.Result<java.math.BigInteger, JSON_mErrors_Compile.DeserializationError> _6_valueOrError1 = ((java.util.function.Function<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, Wrappers_Compile.Result<java.math.BigInteger, JSON_mErrors_Compile.DeserializationError>>)(_source0_boxed0) -> {
        JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp> _source0 = ((JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>)(java.lang.Object)(_source0_boxed0));
        if (_source0.is_Empty()) {
          return Wrappers_Compile.Result.<java.math.BigInteger, JSON_mErrors_Compile.DeserializationError>create_Success(dafny.TypeDescriptor.BIG_INTEGER, JSON_mErrors_Compile.DeserializationError._typeDescriptor(), java.math.BigInteger.ZERO);
        } else {
          JSON_mGrammar_Compile.jexp _7___mcc_h0 = ((JSON_mGrammar_Compile.Maybe_NonEmpty<JSON_mGrammar_Compile.jexp>)_source0)._t;
          JSON_mGrammar_Compile.jexp _source1 = _7___mcc_h0;
          JSON_mUtils_mViews_mCore_Compile.View__ _8___mcc_h1 = ((JSON_mGrammar_Compile.jexp)_source1)._e;
          JSON_mUtils_mViews_mCore_Compile.View__ _9___mcc_h2 = ((JSON_mGrammar_Compile.jexp)_source1)._sign;
          JSON_mUtils_mViews_mCore_Compile.View__ _10___mcc_h3 = ((JSON_mGrammar_Compile.jexp)_source1)._num;
          JSON_mUtils_mViews_mCore_Compile.View__ _11_num = _10___mcc_h3;
          JSON_mUtils_mViews_mCore_Compile.View__ _12_sign = _9___mcc_h2;
          return __default.ToInt(_12_sign, _11_num);
        }
      }).apply(_3_exp);
      if ((_6_valueOrError1).IsFailure(dafny.TypeDescriptor.BIG_INTEGER, JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
        return (_6_valueOrError1).<JSON_mValues_Compile.Decimal>PropagateFailure(dafny.TypeDescriptor.BIG_INTEGER, JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.Decimal._typeDescriptor());
      } else {
        java.math.BigInteger _13_e10 = (_6_valueOrError1).Extract(dafny.TypeDescriptor.BIG_INTEGER, JSON_mErrors_Compile.DeserializationError._typeDescriptor());
        JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac> _source2 = _2_frac;
        if (_source2.is_Empty()) {
          return Wrappers_Compile.Result.<JSON_mValues_Compile.Decimal, JSON_mErrors_Compile.DeserializationError>create_Success(JSON_mValues_Compile.Decimal._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.Decimal.create(_5_n, _13_e10));
        } else {
          JSON_mGrammar_Compile.jfrac _14___mcc_h4 = ((JSON_mGrammar_Compile.Maybe_NonEmpty<JSON_mGrammar_Compile.jfrac>)_source2)._t;
          JSON_mGrammar_Compile.jfrac _source3 = _14___mcc_h4;
          JSON_mUtils_mViews_mCore_Compile.View__ _15___mcc_h5 = ((JSON_mGrammar_Compile.jfrac)_source3)._period;
          JSON_mUtils_mViews_mCore_Compile.View__ _16___mcc_h6 = ((JSON_mGrammar_Compile.jfrac)_source3)._num;
          JSON_mUtils_mViews_mCore_Compile.View__ _17_num = _16___mcc_h6;
          java.math.BigInteger _18_pow10 = dafny.Helpers.unsignedToBigInteger((_17_num).Length());
          Wrappers_Compile.Result<java.math.BigInteger, JSON_mErrors_Compile.DeserializationError> _19_valueOrError2 = __default.ToInt(_0_minus, _17_num);
          if ((_19_valueOrError2).IsFailure(dafny.TypeDescriptor.BIG_INTEGER, JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
            return (_19_valueOrError2).<JSON_mValues_Compile.Decimal>PropagateFailure(dafny.TypeDescriptor.BIG_INTEGER, JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.Decimal._typeDescriptor());
          } else {
            java.math.BigInteger _20_frac = (_19_valueOrError2).Extract(dafny.TypeDescriptor.BIG_INTEGER, JSON_mErrors_Compile.DeserializationError._typeDescriptor());
            return Wrappers_Compile.Result.<JSON_mValues_Compile.Decimal, JSON_mErrors_Compile.DeserializationError>create_Success(JSON_mValues_Compile.Decimal._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.Decimal.create(((_5_n).multiply(Power_Compile.__default.Pow(java.math.BigInteger.valueOf(10L), _18_pow10))).add(_20_frac), (_13_e10).subtract(_18_pow10)));
          }
        }
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>, JSON_mErrors_Compile.DeserializationError> KeyValue(JSON_mGrammar_Compile.jKeyValue js) {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, JSON_mErrors_Compile.DeserializationError> _0_valueOrError0 = __default.String((js).dtor_k());
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()));
    } else {
      dafny.DafnySequence<? extends Character> _1_k = (_0_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mErrors_Compile.DeserializationError._typeDescriptor());
      Wrappers_Compile.Result<JSON_mValues_Compile.JSON, JSON_mErrors_Compile.DeserializationError> _2_valueOrError1 = __default.Value((js).dtor_v());
      if ((_2_valueOrError1).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
        return (_2_valueOrError1).<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>PropagateFailure(JSON_mValues_Compile.JSON._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()));
      } else {
        JSON_mValues_Compile.JSON _3_v = (_2_valueOrError1).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor());
        return Wrappers_Compile.Result.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>, JSON_mErrors_Compile.DeserializationError>create_Success(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>create(_1_k, _3_v));
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>, JSON_mErrors_Compile.DeserializationError> Object(JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> js) {
    return Seq_Compile.__default.<JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__>, dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>, JSON_mErrors_Compile.DeserializationError>MapWithResult(JSON_mGrammar_Compile.Suffixed.<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jKeyValue._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor()), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), ((java.util.function.Function<JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>, java.util.function.Function<JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__>, Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>, JSON_mErrors_Compile.DeserializationError>>>)(_0_js) -> ((java.util.function.Function<JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__>, Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>, JSON_mErrors_Compile.DeserializationError>>)(_1_d_boxed0) -> {
      JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__> _1_d = ((JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__>)(java.lang.Object)(_1_d_boxed0));
      return __default.KeyValue((_1_d).dtor_t());
    })).apply(js), (js).dtor_data());
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends JSON_mValues_Compile.JSON>, JSON_mErrors_Compile.DeserializationError> Array(JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> js) {
    return Seq_Compile.__default.<JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mValues_Compile.JSON, JSON_mErrors_Compile.DeserializationError>MapWithResult(JSON_mGrammar_Compile.Suffixed.<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor()), JSON_mValues_Compile.JSON._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), ((java.util.function.Function<JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>, java.util.function.Function<JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__>, Wrappers_Compile.Result<JSON_mValues_Compile.JSON, JSON_mErrors_Compile.DeserializationError>>>)(_0_js) -> ((java.util.function.Function<JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__>, Wrappers_Compile.Result<JSON_mValues_Compile.JSON, JSON_mErrors_Compile.DeserializationError>>)(_1_d_boxed0) -> {
      JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__> _1_d = ((JSON_mGrammar_Compile.Suffixed<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__>)(java.lang.Object)(_1_d_boxed0));
      return __default.Value((_1_d).dtor_t());
    })).apply(js), (js).dtor_data());
  }
  public static Wrappers_Compile.Result<JSON_mValues_Compile.JSON, JSON_mErrors_Compile.DeserializationError> Value(JSON_mGrammar_Compile.Value js) {
    JSON_mGrammar_Compile.Value _source0 = js;
    if (_source0.is_Null()) {
      JSON_mUtils_mViews_mCore_Compile.View__ _0___mcc_h0 = ((JSON_mGrammar_Compile.Value_Null)_source0)._n;
      return Wrappers_Compile.Result.<JSON_mValues_Compile.JSON, JSON_mErrors_Compile.DeserializationError>create_Success(JSON_mValues_Compile.JSON._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.JSON.create_Null());
    } else if (_source0.is_Bool()) {
      JSON_mUtils_mViews_mCore_Compile.View__ _1___mcc_h1 = ((JSON_mGrammar_Compile.Value_Bool)_source0)._b;
      JSON_mUtils_mViews_mCore_Compile.View__ _2_b = _1___mcc_h1;
      return Wrappers_Compile.Result.<JSON_mValues_Compile.JSON, JSON_mErrors_Compile.DeserializationError>create_Success(JSON_mValues_Compile.JSON._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.JSON.create_Bool(__default.Bool(_2_b)));
    } else if (_source0.is_String()) {
      JSON_mGrammar_Compile.jstring _3___mcc_h2 = ((JSON_mGrammar_Compile.Value_String)_source0)._str;
      JSON_mGrammar_Compile.jstring _4_str = _3___mcc_h2;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, JSON_mErrors_Compile.DeserializationError> _5_valueOrError0 = __default.String(_4_str);
      if ((_5_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
        return (_5_valueOrError0).<JSON_mValues_Compile.JSON>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.JSON._typeDescriptor());
      } else {
        dafny.DafnySequence<? extends Character> _6_s = (_5_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mErrors_Compile.DeserializationError._typeDescriptor());
        return Wrappers_Compile.Result.<JSON_mValues_Compile.JSON, JSON_mErrors_Compile.DeserializationError>create_Success(JSON_mValues_Compile.JSON._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.JSON.create_String(_6_s));
      }
    } else if (_source0.is_Number()) {
      JSON_mGrammar_Compile.jnumber _7___mcc_h3 = ((JSON_mGrammar_Compile.Value_Number)_source0)._num;
      JSON_mGrammar_Compile.jnumber _8_dec = _7___mcc_h3;
      Wrappers_Compile.Result<JSON_mValues_Compile.Decimal, JSON_mErrors_Compile.DeserializationError> _9_valueOrError1 = __default.Number(_8_dec);
      if ((_9_valueOrError1).IsFailure(JSON_mValues_Compile.Decimal._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
        return (_9_valueOrError1).<JSON_mValues_Compile.JSON>PropagateFailure(JSON_mValues_Compile.Decimal._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.JSON._typeDescriptor());
      } else {
        JSON_mValues_Compile.Decimal _10_n = (_9_valueOrError1).Extract(JSON_mValues_Compile.Decimal._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor());
        return Wrappers_Compile.Result.<JSON_mValues_Compile.JSON, JSON_mErrors_Compile.DeserializationError>create_Success(JSON_mValues_Compile.JSON._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.JSON.create_Number(_10_n));
      }
    } else if (_source0.is_Object()) {
      JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _11___mcc_h4 = ((JSON_mGrammar_Compile.Value_Object)_source0)._obj;
      JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _12_obj = _11___mcc_h4;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>, JSON_mErrors_Compile.DeserializationError> _13_valueOrError2 = __default.Object(_12_obj);
      if ((_13_valueOrError2).IsFailure(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())), JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
        return (_13_valueOrError2).<JSON_mValues_Compile.JSON>PropagateFailure(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.JSON._typeDescriptor());
      } else {
        dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> _14_o = (_13_valueOrError2).Extract(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())), JSON_mErrors_Compile.DeserializationError._typeDescriptor());
        return Wrappers_Compile.Result.<JSON_mValues_Compile.JSON, JSON_mErrors_Compile.DeserializationError>create_Success(JSON_mValues_Compile.JSON._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.JSON.create_Object(_14_o));
      }
    } else {
      JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _15___mcc_h5 = ((JSON_mGrammar_Compile.Value_Array)_source0)._arr;
      JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _16_arr = _15___mcc_h5;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends JSON_mValues_Compile.JSON>, JSON_mErrors_Compile.DeserializationError> _17_valueOrError3 = __default.Array(_16_arr);
      if ((_17_valueOrError3).IsFailure(dafny.DafnySequence.<JSON_mValues_Compile.JSON>_typeDescriptor(JSON_mValues_Compile.JSON._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor())) {
        return (_17_valueOrError3).<JSON_mValues_Compile.JSON>PropagateFailure(dafny.DafnySequence.<JSON_mValues_Compile.JSON>_typeDescriptor(JSON_mValues_Compile.JSON._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.JSON._typeDescriptor());
      } else {
        dafny.DafnySequence<? extends JSON_mValues_Compile.JSON> _18_a = (_17_valueOrError3).Extract(dafny.DafnySequence.<JSON_mValues_Compile.JSON>_typeDescriptor(JSON_mValues_Compile.JSON._typeDescriptor()), JSON_mErrors_Compile.DeserializationError._typeDescriptor());
        return Wrappers_Compile.Result.<JSON_mValues_Compile.JSON, JSON_mErrors_Compile.DeserializationError>create_Success(JSON_mValues_Compile.JSON._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), JSON_mValues_Compile.JSON.create_Array(_18_a));
      }
    }
  }
  public static Wrappers_Compile.Result<JSON_mValues_Compile.JSON, JSON_mErrors_Compile.DeserializationError> JSON(JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value> js) {
    return __default.Value((js).dtor_t());
  }
  public static dafny.DafnyMap<? extends java.lang.Short, ? extends java.math.BigInteger> HEX__TABLE__16()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(((short) ('0')), java.math.BigInteger.ZERO), new dafny.Tuple2(((short) ('1')), java.math.BigInteger.ONE), new dafny.Tuple2(((short) ('2')), java.math.BigInteger.valueOf(2L)), new dafny.Tuple2(((short) ('3')), java.math.BigInteger.valueOf(3L)), new dafny.Tuple2(((short) ('4')), java.math.BigInteger.valueOf(4L)), new dafny.Tuple2(((short) ('5')), java.math.BigInteger.valueOf(5L)), new dafny.Tuple2(((short) ('6')), java.math.BigInteger.valueOf(6L)), new dafny.Tuple2(((short) ('7')), java.math.BigInteger.valueOf(7L)), new dafny.Tuple2(((short) ('8')), java.math.BigInteger.valueOf(8L)), new dafny.Tuple2(((short) ('9')), java.math.BigInteger.valueOf(9L)), new dafny.Tuple2(((short) ('a')), java.math.BigInteger.valueOf(10L)), new dafny.Tuple2(((short) ('b')), java.math.BigInteger.valueOf(11L)), new dafny.Tuple2(((short) ('c')), java.math.BigInteger.valueOf(12L)), new dafny.Tuple2(((short) ('d')), java.math.BigInteger.valueOf(13L)), new dafny.Tuple2(((short) ('e')), java.math.BigInteger.valueOf(14L)), new dafny.Tuple2(((short) ('f')), java.math.BigInteger.valueOf(15L)), new dafny.Tuple2(((short) ('A')), java.math.BigInteger.valueOf(10L)), new dafny.Tuple2(((short) ('B')), java.math.BigInteger.valueOf(11L)), new dafny.Tuple2(((short) ('C')), java.math.BigInteger.valueOf(12L)), new dafny.Tuple2(((short) ('D')), java.math.BigInteger.valueOf(13L)), new dafny.Tuple2(((short) ('E')), java.math.BigInteger.valueOf(14L)), new dafny.Tuple2(((short) ('F')), java.math.BigInteger.valueOf(15L)));
  }
  public static dafny.DafnyMap<? extends java.lang.Byte, ? extends java.math.BigInteger> DIGITS()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(((byte) ('0')), java.math.BigInteger.ZERO), new dafny.Tuple2(((byte) ('1')), java.math.BigInteger.ONE), new dafny.Tuple2(((byte) ('2')), java.math.BigInteger.valueOf(2L)), new dafny.Tuple2(((byte) ('3')), java.math.BigInteger.valueOf(3L)), new dafny.Tuple2(((byte) ('4')), java.math.BigInteger.valueOf(4L)), new dafny.Tuple2(((byte) ('5')), java.math.BigInteger.valueOf(5L)), new dafny.Tuple2(((byte) ('6')), java.math.BigInteger.valueOf(6L)), new dafny.Tuple2(((byte) ('7')), java.math.BigInteger.valueOf(7L)), new dafny.Tuple2(((byte) ('8')), java.math.BigInteger.valueOf(8L)), new dafny.Tuple2(((byte) ('9')), java.math.BigInteger.valueOf(9L)));
  }
  public static byte MINUS()
  {
    return ((byte) ('-'));
  }
  @Override
  public java.lang.String toString() {
    return "JSON.Deserializer._default";
  }
}
