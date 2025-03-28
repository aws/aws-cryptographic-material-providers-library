// Class __default
// Dafny class __default compiled into Java
package JSON_mSerializer_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ Bool(boolean b) {
    return JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(((b) ? (JSON_mGrammar_Compile.__default.TRUE()) : (JSON_mGrammar_Compile.__default.FALSE())));
  }
  public static <__T> Wrappers_Compile.Outcome<JSON_mErrors_Compile.SerializationError> CheckLength(dafny.TypeDescriptor<__T> _td___T, dafny.DafnySequence<? extends __T> s, JSON_mErrors_Compile.SerializationError err)
  {
    return Wrappers_Compile.__default.<JSON_mErrors_Compile.SerializationError>Need(JSON_mErrors_Compile.SerializationError._typeDescriptor(), (java.math.BigInteger.valueOf((s).length())).compareTo(BoundedInts_Compile.__default.TWO__TO__THE__32()) < 0, err);
  }
  public static Wrappers_Compile.Result<JSON_mGrammar_Compile.jstring, JSON_mErrors_Compile.SerializationError> String(dafny.DafnySequence<? extends Character> str) {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, JSON_mErrors_Compile.SerializationError> _0_valueOrError0 = JSON_mSpec_Compile.__default.EscapeToUTF8(str, java.math.BigInteger.ZERO);
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      return (_0_valueOrError0).<JSON_mGrammar_Compile.jstring>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.jstring._typeDescriptor());
    } else {
      dafny.DafnySequence<? extends java.lang.Byte> _1_bs = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
      Wrappers_Compile.Outcome<JSON_mErrors_Compile.SerializationError> _2_valueOrError1 = __default.<java.lang.Byte>CheckLength(BoundedInts_Compile.uint8._typeDescriptor(), _1_bs, JSON_mErrors_Compile.SerializationError.create_StringTooLong(str));
      if ((_2_valueOrError1).IsFailure(JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
        return (_2_valueOrError1).<JSON_mGrammar_Compile.jstring>PropagateFailure(JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.jstring._typeDescriptor());
      } else {
        return Wrappers_Compile.Result.<JSON_mGrammar_Compile.jstring, JSON_mErrors_Compile.SerializationError>create_Success(JSON_mGrammar_Compile.jstring._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.jstring.create(JSON_mGrammar_Compile.__default.DOUBLEQUOTE(), JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(_1_bs), JSON_mGrammar_Compile.__default.DOUBLEQUOTE()));
      }
    }
  }
  public static JSON_mUtils_mViews_mCore_Compile.View__ Sign(java.math.BigInteger n) {
    return JSON_mUtils_mViews_mCore_Compile.View__.OfBytes((((n).signum() == -1) ? (dafny.DafnySequence.<java.lang.Byte> of(((byte) ('-')))) : (dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()))));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Int_k(java.math.BigInteger n) {
    return JSON_mSerializer_mByteStrConversion_Compile.__default.OfInt__any(n, __default.DIGITS(), __default.MINUS());
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mErrors_Compile.SerializationError> Int(java.math.BigInteger n) {
    dafny.DafnySequence<? extends java.lang.Byte> _0_bs = __default.Int_k(n);
    Wrappers_Compile.Outcome<JSON_mErrors_Compile.SerializationError> _1_valueOrError0 = __default.<java.lang.Byte>CheckLength(BoundedInts_Compile.uint8._typeDescriptor(), _0_bs, JSON_mErrors_Compile.SerializationError.create_IntTooLarge(n));
    if ((_1_valueOrError0).IsFailure(JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      return (_1_valueOrError0).<JSON_mUtils_mViews_mCore_Compile.View__>PropagateFailure(JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor());
    } else {
      return Wrappers_Compile.Result.<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mErrors_Compile.SerializationError>create_Success(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(_0_bs));
    }
  }
  public static Wrappers_Compile.Result<JSON_mGrammar_Compile.jnumber, JSON_mErrors_Compile.SerializationError> Number(JSON_mValues_Compile.Decimal dec) {
    JSON_mValues_Compile.Decimal _pat_let_tv0 = dec;
    JSON_mValues_Compile.Decimal _pat_let_tv1 = dec;
    JSON_mUtils_mViews_mCore_Compile.View__ _0_minus = __default.Sign((dec).dtor_n());
    Wrappers_Compile.Result<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mErrors_Compile.SerializationError> _1_valueOrError0 = __default.Int(Math_Compile.__default.Abs((dec).dtor_n()));
    if ((_1_valueOrError0).IsFailure(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      return (_1_valueOrError0).<JSON_mGrammar_Compile.jnumber>PropagateFailure(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.jnumber._typeDescriptor());
    } else {
      JSON_mUtils_mViews_mCore_Compile.View__ _2_num = (_1_valueOrError0).Extract(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor());
      JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jfrac> _3_frac = JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jfrac>create_Empty(JSON_mGrammar_Compile.jfrac._typeDescriptor());
      Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError> _4_valueOrError1 = ((((dec).dtor_e10()).signum() == 0) ? (Wrappers_Compile.Result.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>create_Success(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>_typeDescriptor(JSON_mGrammar_Compile.jexp._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>create_Empty(JSON_mGrammar_Compile.jexp._typeDescriptor()))) : (((Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>)(java.lang.Object)(dafny.Helpers.<JSON_mUtils_mViews_mCore_Compile.View__, Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>>Let(JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(dafny.DafnySequence.<java.lang.Byte> of(((byte) ('e')))), boxed12 -> {
        JSON_mUtils_mViews_mCore_Compile.View__ _pat_let7_0 = ((JSON_mUtils_mViews_mCore_Compile.View__)(java.lang.Object)(boxed12));
        return ((Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>)(java.lang.Object)(dafny.Helpers.<JSON_mUtils_mViews_mCore_Compile.View__, Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>>Let(_pat_let7_0, boxed13 -> {
          JSON_mUtils_mViews_mCore_Compile.View__ _5_e = ((JSON_mUtils_mViews_mCore_Compile.View__)(java.lang.Object)(boxed13));
          return ((Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>)(java.lang.Object)(dafny.Helpers.<JSON_mUtils_mViews_mCore_Compile.View__, Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>>Let(__default.Sign((_pat_let_tv0).dtor_e10()), boxed14 -> {
            JSON_mUtils_mViews_mCore_Compile.View__ _pat_let8_0 = ((JSON_mUtils_mViews_mCore_Compile.View__)(java.lang.Object)(boxed14));
            return ((Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>)(java.lang.Object)(dafny.Helpers.<JSON_mUtils_mViews_mCore_Compile.View__, Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>>Let(_pat_let8_0, boxed15 -> {
              JSON_mUtils_mViews_mCore_Compile.View__ _6_sign = ((JSON_mUtils_mViews_mCore_Compile.View__)(java.lang.Object)(boxed15));
              return ((Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Result<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mErrors_Compile.SerializationError>, Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>>Let(__default.Int(Math_Compile.__default.Abs((_pat_let_tv1).dtor_e10())), boxed16 -> {
                Wrappers_Compile.Result<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mErrors_Compile.SerializationError> _pat_let9_0 = ((Wrappers_Compile.Result<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mErrors_Compile.SerializationError>)(java.lang.Object)(boxed16));
                return ((Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>)(java.lang.Object)(dafny.Helpers.<Wrappers_Compile.Result<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mErrors_Compile.SerializationError>, Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>>Let(_pat_let9_0, boxed17 -> {
                  Wrappers_Compile.Result<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mErrors_Compile.SerializationError> _7_valueOrError2 = ((Wrappers_Compile.Result<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mErrors_Compile.SerializationError>)(java.lang.Object)(boxed17));
                  return (((_7_valueOrError2).IsFailure(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor())) ? ((_7_valueOrError2).<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>>PropagateFailure(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>_typeDescriptor(JSON_mGrammar_Compile.jexp._typeDescriptor()))) : (((Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>)(java.lang.Object)(dafny.Helpers.<JSON_mUtils_mViews_mCore_Compile.View__, Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>>Let((_7_valueOrError2).Extract(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor()), boxed18 -> {
                    JSON_mUtils_mViews_mCore_Compile.View__ _pat_let10_0 = ((JSON_mUtils_mViews_mCore_Compile.View__)(java.lang.Object)(boxed18));
                    return ((Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>)(java.lang.Object)(dafny.Helpers.<JSON_mUtils_mViews_mCore_Compile.View__, Wrappers_Compile.Result<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>>Let(_pat_let10_0, boxed19 -> {
                      JSON_mUtils_mViews_mCore_Compile.View__ _8_num = ((JSON_mUtils_mViews_mCore_Compile.View__)(java.lang.Object)(boxed19));
                      return Wrappers_Compile.Result.<JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp>, JSON_mErrors_Compile.SerializationError>create_Success(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>_typeDescriptor(JSON_mGrammar_Compile.jexp._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>create_NonEmpty(JSON_mGrammar_Compile.jexp._typeDescriptor(), JSON_mGrammar_Compile.jexp.create(_5_e, _6_sign, _8_num)));
                    }
                    )));
                  }
                  )))));
                }
                )));
              }
              )));
            }
            )));
          }
          )));
        }
        )));
      }
      )))));
      if ((_4_valueOrError1).IsFailure(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>_typeDescriptor(JSON_mGrammar_Compile.jexp._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
        return (_4_valueOrError1).<JSON_mGrammar_Compile.jnumber>PropagateFailure(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>_typeDescriptor(JSON_mGrammar_Compile.jexp._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.jnumber._typeDescriptor());
      } else {
        JSON_mGrammar_Compile.Maybe<JSON_mGrammar_Compile.jexp> _9_exp = (_4_valueOrError1).Extract(JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jexp>_typeDescriptor(JSON_mGrammar_Compile.jexp._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
        return Wrappers_Compile.Result.<JSON_mGrammar_Compile.jnumber, JSON_mErrors_Compile.SerializationError>create_Success(JSON_mGrammar_Compile.jnumber._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.jnumber.create(_0_minus, _2_num, JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.jfrac>create_Empty(JSON_mGrammar_Compile.jfrac._typeDescriptor()), _9_exp));
      }
    }
  }
  public static <__T> JSON_mGrammar_Compile.Structural<__T> MkStructural(dafny.TypeDescriptor<__T> _td___T, __T v)
  {
    return JSON_mGrammar_Compile.Structural.<__T>create(_td___T, JSON_mGrammar_Compile.__default.EMPTY(), v, JSON_mGrammar_Compile.__default.EMPTY());
  }
  public static Wrappers_Compile.Result<JSON_mGrammar_Compile.jKeyValue, JSON_mErrors_Compile.SerializationError> KeyValue(dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON> kv) {
    Wrappers_Compile.Result<JSON_mGrammar_Compile.jstring, JSON_mErrors_Compile.SerializationError> _0_valueOrError0 = __default.String((kv).dtor__0());
    if ((_0_valueOrError0).IsFailure(JSON_mGrammar_Compile.jstring._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      return (_0_valueOrError0).<JSON_mGrammar_Compile.jKeyValue>PropagateFailure(JSON_mGrammar_Compile.jstring._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.jKeyValue._typeDescriptor());
    } else {
      JSON_mGrammar_Compile.jstring _1_k = (_0_valueOrError0).Extract(JSON_mGrammar_Compile.jstring._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor());
      Wrappers_Compile.Result<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.SerializationError> _2_valueOrError1 = __default.Value((kv).dtor__1());
      if ((_2_valueOrError1).IsFailure(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
        return (_2_valueOrError1).<JSON_mGrammar_Compile.jKeyValue>PropagateFailure(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.jKeyValue._typeDescriptor());
      } else {
        JSON_mGrammar_Compile.Value _3_v = (_2_valueOrError1).Extract(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor());
        return Wrappers_Compile.Result.<JSON_mGrammar_Compile.jKeyValue, JSON_mErrors_Compile.SerializationError>create_Success(JSON_mGrammar_Compile.jKeyValue._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.jKeyValue.create(_1_k, __default.COLON(), _3_v));
      }
    }
  }
  public static <__D, __S> dafny.DafnySequence<? extends JSON_mGrammar_Compile.Suffixed<__D, __S>> MkSuffixedSequence(dafny.TypeDescriptor<__D> _td___D, dafny.TypeDescriptor<__S> _td___S, dafny.DafnySequence<? extends __D> ds, JSON_mGrammar_Compile.Structural<__S> suffix, java.math.BigInteger start)
  {
    dafny.DafnySequence<? extends JSON_mGrammar_Compile.Suffixed<__D, __S>> _0___accumulator = dafny.DafnySequence.<JSON_mGrammar_Compile.Suffixed<__D, __S>> empty(JSON_mGrammar_Compile.Suffixed.<__D, __S>_typeDescriptor(_td___D, _td___S));
    TAIL_CALL_START: while (true) {
      if ((start).compareTo(java.math.BigInteger.valueOf((ds).length())) >= 0) {
        return dafny.DafnySequence.<JSON_mGrammar_Compile.Suffixed<__D, __S>>concatenate(_0___accumulator, dafny.DafnySequence.<JSON_mGrammar_Compile.Suffixed<__D, __S>> empty(JSON_mGrammar_Compile.Suffixed.<__D, __S>_typeDescriptor(_td___D, _td___S)));
      } else if (java.util.Objects.equals(start, (java.math.BigInteger.valueOf((ds).length())).subtract(java.math.BigInteger.ONE))) {
        return dafny.DafnySequence.<JSON_mGrammar_Compile.Suffixed<__D, __S>>concatenate(_0___accumulator, dafny.DafnySequence.<JSON_mGrammar_Compile.Suffixed<__D, __S>> of(JSON_mGrammar_Compile.Suffixed.<__D, __S>_typeDescriptor(_td___D, _td___S), JSON_mGrammar_Compile.Suffixed.<__D, __S>create(_td___D, _td___S, ((__D)(java.lang.Object)((ds).select(dafny.Helpers.toInt((start))))), JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.Structural<__S>>create_Empty(JSON_mGrammar_Compile.Structural.<__S>_typeDescriptor(_td___S)))));
      } else {
        _0___accumulator = dafny.DafnySequence.<JSON_mGrammar_Compile.Suffixed<__D, __S>>concatenate(_0___accumulator, dafny.DafnySequence.<JSON_mGrammar_Compile.Suffixed<__D, __S>> of(JSON_mGrammar_Compile.Suffixed.<__D, __S>_typeDescriptor(_td___D, _td___S), JSON_mGrammar_Compile.Suffixed.<__D, __S>create(_td___D, _td___S, ((__D)(java.lang.Object)((ds).select(dafny.Helpers.toInt((start))))), JSON_mGrammar_Compile.Maybe.<JSON_mGrammar_Compile.Structural<__S>>create_NonEmpty(JSON_mGrammar_Compile.Structural.<__S>_typeDescriptor(_td___S), suffix))));
        dafny.DafnySequence<? extends __D> _in0 = ds;
        JSON_mGrammar_Compile.Structural<__S> _in1 = suffix;
        java.math.BigInteger _in2 = (start).add(java.math.BigInteger.ONE);
        ds = _in0;
        suffix = _in1;
        start = _in2;
        continue TAIL_CALL_START;
      }
    }
  }
  public static Wrappers_Compile.Result<JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mErrors_Compile.SerializationError> Object(dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> obj) {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends JSON_mGrammar_Compile.jKeyValue>, JSON_mErrors_Compile.SerializationError> _0_valueOrError0 = Seq_Compile.__default.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>, JSON_mGrammar_Compile.jKeyValue, JSON_mErrors_Compile.SerializationError>MapWithResult(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()), JSON_mGrammar_Compile.jKeyValue._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>, java.util.function.Function<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>, Wrappers_Compile.Result<JSON_mGrammar_Compile.jKeyValue, JSON_mErrors_Compile.SerializationError>>>)(_1_obj) -> ((java.util.function.Function<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>, Wrappers_Compile.Result<JSON_mGrammar_Compile.jKeyValue, JSON_mErrors_Compile.SerializationError>>)(_2_v_boxed0) -> {
      dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON> _2_v = ((dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>)(java.lang.Object)(_2_v_boxed0));
      return __default.KeyValue(_2_v);
    })).apply(obj), obj);
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<JSON_mGrammar_Compile.jKeyValue>_typeDescriptor(JSON_mGrammar_Compile.jKeyValue._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      return (_0_valueOrError0).<JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>>PropagateFailure(dafny.DafnySequence.<JSON_mGrammar_Compile.jKeyValue>_typeDescriptor(JSON_mGrammar_Compile.jKeyValue._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Bracketed.<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mGrammar_Compile.jKeyValue._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()));
    } else {
      dafny.DafnySequence<? extends JSON_mGrammar_Compile.jKeyValue> _3_items = (_0_valueOrError0).Extract(dafny.DafnySequence.<JSON_mGrammar_Compile.jKeyValue>_typeDescriptor(JSON_mGrammar_Compile.jKeyValue._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
      return Wrappers_Compile.Result.<JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mErrors_Compile.SerializationError>create_Success(JSON_mGrammar_Compile.Bracketed.<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mGrammar_Compile.jKeyValue._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Bracketed.<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>create(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mGrammar_Compile.jKeyValue._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), __default.<JSON_mUtils_mViews_mCore_Compile.View__>MkStructural(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mGrammar_Compile.__default.LBRACE()), __default.<JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__>MkSuffixedSequence(JSON_mGrammar_Compile.jKeyValue._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), _3_items, __default.COMMA(), java.math.BigInteger.ZERO), __default.<JSON_mUtils_mViews_mCore_Compile.View__>MkStructural(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mGrammar_Compile.__default.RBRACE())));
    }
  }
  public static Wrappers_Compile.Result<JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mErrors_Compile.SerializationError> Array(dafny.DafnySequence<? extends JSON_mValues_Compile.JSON> arr) {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends JSON_mGrammar_Compile.Value>, JSON_mErrors_Compile.SerializationError> _0_valueOrError0 = Seq_Compile.__default.<JSON_mValues_Compile.JSON, JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.SerializationError>MapWithResult(JSON_mValues_Compile.JSON._typeDescriptor(), JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends JSON_mValues_Compile.JSON>, java.util.function.Function<JSON_mValues_Compile.JSON, Wrappers_Compile.Result<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.SerializationError>>>)(_1_arr) -> ((java.util.function.Function<JSON_mValues_Compile.JSON, Wrappers_Compile.Result<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.SerializationError>>)(_2_v_boxed0) -> {
      JSON_mValues_Compile.JSON _2_v = ((JSON_mValues_Compile.JSON)(java.lang.Object)(_2_v_boxed0));
      return __default.Value(_2_v);
    })).apply(arr), arr);
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      return (_0_valueOrError0).<JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>>PropagateFailure(dafny.DafnySequence.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Bracketed.<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()));
    } else {
      dafny.DafnySequence<? extends JSON_mGrammar_Compile.Value> _3_items = (_0_valueOrError0).Extract(dafny.DafnySequence.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
      return Wrappers_Compile.Result.<JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mErrors_Compile.SerializationError>create_Success(JSON_mGrammar_Compile.Bracketed.<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Bracketed.<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>create(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), __default.<JSON_mUtils_mViews_mCore_Compile.View__>MkStructural(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mGrammar_Compile.__default.LBRACKET()), __default.<JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__>MkSuffixedSequence(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), _3_items, __default.COMMA(), java.math.BigInteger.ZERO), __default.<JSON_mUtils_mViews_mCore_Compile.View__>MkStructural(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mGrammar_Compile.__default.RBRACKET())));
    }
  }
  public static Wrappers_Compile.Result<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.SerializationError> Value(JSON_mValues_Compile.JSON js) {
    JSON_mValues_Compile.JSON _source0 = js;
    if (_source0.is_Null()) {
      return Wrappers_Compile.Result.<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.SerializationError>create_Success(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Value.create_Null(JSON_mUtils_mViews_mCore_Compile.View__.OfBytes(JSON_mGrammar_Compile.__default.NULL())));
    } else if (_source0.is_Bool()) {
      boolean _0___mcc_h0 = ((JSON_mValues_Compile.JSON_Bool)_source0)._b;
      boolean _1_b = _0___mcc_h0;
      return Wrappers_Compile.Result.<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.SerializationError>create_Success(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Value.create_Bool(__default.Bool(_1_b)));
    } else if (_source0.is_String()) {
      dafny.DafnySequence<? extends Character> _2___mcc_h1 = ((JSON_mValues_Compile.JSON_String)_source0)._str;
      dafny.DafnySequence<? extends Character> _3_str = _2___mcc_h1;
      Wrappers_Compile.Result<JSON_mGrammar_Compile.jstring, JSON_mErrors_Compile.SerializationError> _4_valueOrError0 = __default.String(_3_str);
      if ((_4_valueOrError0).IsFailure(JSON_mGrammar_Compile.jstring._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
        return (_4_valueOrError0).<JSON_mGrammar_Compile.Value>PropagateFailure(JSON_mGrammar_Compile.jstring._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Value._typeDescriptor());
      } else {
        JSON_mGrammar_Compile.jstring _5_s = (_4_valueOrError0).Extract(JSON_mGrammar_Compile.jstring._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor());
        return Wrappers_Compile.Result.<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.SerializationError>create_Success(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Value.create_String(_5_s));
      }
    } else if (_source0.is_Number()) {
      JSON_mValues_Compile.Decimal _6___mcc_h2 = ((JSON_mValues_Compile.JSON_Number)_source0)._num;
      JSON_mValues_Compile.Decimal _7_dec = _6___mcc_h2;
      Wrappers_Compile.Result<JSON_mGrammar_Compile.jnumber, JSON_mErrors_Compile.SerializationError> _8_valueOrError1 = __default.Number(_7_dec);
      if ((_8_valueOrError1).IsFailure(JSON_mGrammar_Compile.jnumber._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
        return (_8_valueOrError1).<JSON_mGrammar_Compile.Value>PropagateFailure(JSON_mGrammar_Compile.jnumber._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Value._typeDescriptor());
      } else {
        JSON_mGrammar_Compile.jnumber _9_n = (_8_valueOrError1).Extract(JSON_mGrammar_Compile.jnumber._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor());
        return Wrappers_Compile.Result.<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.SerializationError>create_Success(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Value.create_Number(_9_n));
      }
    } else if (_source0.is_Object()) {
      dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> _10___mcc_h3 = ((JSON_mValues_Compile.JSON_Object)_source0)._obj;
      dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> _11_obj = _10___mcc_h3;
      Wrappers_Compile.Result<JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mErrors_Compile.SerializationError> _12_valueOrError2 = __default.Object(_11_obj);
      if ((_12_valueOrError2).IsFailure(JSON_mGrammar_Compile.Bracketed.<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jlbrace._typeDescriptor(), JSON_mGrammar_Compile.jKeyValue._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), JSON_mGrammar_Compile.jrbrace._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
        return (_12_valueOrError2).<JSON_mGrammar_Compile.Value>PropagateFailure(JSON_mGrammar_Compile.Bracketed.<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jlbrace._typeDescriptor(), JSON_mGrammar_Compile.jKeyValue._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), JSON_mGrammar_Compile.jrbrace._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Value._typeDescriptor());
      } else {
        JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _13_o = (_12_valueOrError2).Extract(JSON_mGrammar_Compile.Bracketed.<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jlbrace._typeDescriptor(), JSON_mGrammar_Compile.jKeyValue._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), JSON_mGrammar_Compile.jrbrace._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
        return Wrappers_Compile.Result.<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.SerializationError>create_Success(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Value.create_Object(_13_o));
      }
    } else {
      dafny.DafnySequence<? extends JSON_mValues_Compile.JSON> _14___mcc_h4 = ((JSON_mValues_Compile.JSON_Array)_source0)._arr;
      dafny.DafnySequence<? extends JSON_mValues_Compile.JSON> _15_arr = _14___mcc_h4;
      Wrappers_Compile.Result<JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mErrors_Compile.SerializationError> _16_valueOrError3 = __default.Array(_15_arr);
      if ((_16_valueOrError3).IsFailure(JSON_mGrammar_Compile.Bracketed.<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jlbracket._typeDescriptor(), JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), JSON_mGrammar_Compile.jrbracket._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
        return (_16_valueOrError3).<JSON_mGrammar_Compile.Value>PropagateFailure(JSON_mGrammar_Compile.Bracketed.<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jlbracket._typeDescriptor(), JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), JSON_mGrammar_Compile.jrbracket._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Value._typeDescriptor());
      } else {
        JSON_mGrammar_Compile.Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _17_a = (_16_valueOrError3).Extract(JSON_mGrammar_Compile.Bracketed.<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mGrammar_Compile.Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jlbracket._typeDescriptor(), JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mGrammar_Compile.jcomma._typeDescriptor(), JSON_mGrammar_Compile.jrbracket._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor());
        return Wrappers_Compile.Result.<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.SerializationError>create_Success(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Value.create_Array(_17_a));
      }
    }
  }
  public static Wrappers_Compile.Result<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>, JSON_mErrors_Compile.SerializationError> JSON(JSON_mValues_Compile.JSON js) {
    Wrappers_Compile.Result<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.SerializationError> _0_valueOrError0 = __default.Value(js);
    if ((_0_valueOrError0).IsFailure(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor())) {
      return (_0_valueOrError0).<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>>PropagateFailure(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor(), JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()));
    } else {
      JSON_mGrammar_Compile.Value _1_val = (_0_valueOrError0).Extract(JSON_mGrammar_Compile.Value._typeDescriptor(), JSON_mErrors_Compile.SerializationError._typeDescriptor());
      return Wrappers_Compile.Result.<JSON_mGrammar_Compile.Structural<JSON_mGrammar_Compile.Value>, JSON_mErrors_Compile.SerializationError>create_Success(JSON_mGrammar_Compile.Structural.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), __default.<JSON_mGrammar_Compile.Value>MkStructural(JSON_mGrammar_Compile.Value._typeDescriptor(), _1_val));
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> DIGITS()
  {
    return dafny.DafnySequence.<java.lang.Byte> of(((byte) ('0')), ((byte) ('1')), ((byte) ('2')), ((byte) ('3')), ((byte) ('4')), ((byte) ('5')), ((byte) ('6')), ((byte) ('7')), ((byte) ('8')), ((byte) ('9')));
  }
  public static byte MINUS()
  {
    return ((byte) ('-'));
  }
  public static JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__> COLON()
  {
    return __default.<JSON_mUtils_mViews_mCore_Compile.View__>MkStructural(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mGrammar_Compile.__default.COLON());
  }
  public static JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__> COMMA()
  {
    return __default.<JSON_mUtils_mViews_mCore_Compile.View__>MkStructural(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), JSON_mGrammar_Compile.__default.COMMA());
  }
  @Override
  public java.lang.String toString() {
    return "JSON.Serializer._default";
  }
}
