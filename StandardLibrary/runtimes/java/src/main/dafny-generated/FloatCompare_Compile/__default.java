// Class __default
// Dafny class __default compiled into Java
package FloatCompare_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static java.math.BigInteger StrToIntInner(dafny.DafnySequence<? extends Character> s, java.math.BigInteger acc)
  {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((s).length())).signum() == 0) {
        return acc;
      } else if ((('0') <= (((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) && ((((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) <= ('9'))) {
        dafny.DafnySequence<? extends Character> _in0 = (s).drop(java.math.BigInteger.ONE);
        java.math.BigInteger _in1 = (((acc).multiply(java.math.BigInteger.valueOf(10L))).add(java.math.BigInteger.valueOf(((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))))).subtract(java.math.BigInteger.valueOf('0'));
        s = _in0;
        acc = _in1;
        continue TAIL_CALL_START;
      } else {
        dafny.DafnySequence<? extends Character> _in2 = (s).drop(java.math.BigInteger.ONE);
        java.math.BigInteger _in3 = acc;
        s = _in2;
        acc = _in3;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> SkipLeadingSpace(dafny.DafnySequence<? extends Character> val) {
    TAIL_CALL_START: while (true) {
      if (((java.math.BigInteger.valueOf((val).length())).signum() == 1) && ((((char)(java.lang.Object)((val).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) <= (' '))) {
        dafny.DafnySequence<? extends Character> _in0 = (val).drop(java.math.BigInteger.ONE);
        val = _in0;
        continue TAIL_CALL_START;
      } else {
        return val;
      }
    }
  }
  public static java.math.BigInteger StrToInt(dafny.DafnySequence<? extends Character> s, java.math.BigInteger acc)
  {
    dafny.DafnySequence<? extends Character> _0_tmp = __default.SkipLeadingSpace(s);
    if ((java.math.BigInteger.valueOf((_0_tmp).length())).signum() == 0) {
      return java.math.BigInteger.ZERO;
    } else if ((((char)(java.lang.Object)((_0_tmp).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) == ('-')) {
      return (java.math.BigInteger.ZERO).subtract(__default.StrToIntInner(s, java.math.BigInteger.ZERO));
    } else {
      return __default.StrToIntInner(s, java.math.BigInteger.ZERO);
    }
  }
  public static Wrappers_Compile.Option<dafny.Tuple2<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>> SplitE(dafny.DafnySequence<? extends Character> x) {
    Wrappers_Compile.Option<dafny.Tuple2<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>> _0_parts = StandardLibrary_Compile.__default.<Character>SplitOnce_q(dafny.TypeDescriptor.CHAR, x, 'e');
    if ((_0_parts).is_Some()) {
      return _0_parts;
    } else {
      return StandardLibrary_Compile.__default.<Character>SplitOnce_q(dafny.TypeDescriptor.CHAR, x, 'E');
    }
  }
  public static dafny.Tuple2<dafny.DafnySequence<? extends Character>, java.math.BigInteger> SplitExp(dafny.DafnySequence<? extends Character> x) {
    Wrappers_Compile.Option<dafny.Tuple2<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>> _0_parts = __default.SplitE(x);
    if ((_0_parts).is_Some()) {
      return dafny.Tuple2.<dafny.DafnySequence<? extends Character>, java.math.BigInteger>create(((_0_parts).dtor_value()).dtor__0(), __default.StrToInt(((_0_parts).dtor_value()).dtor__1(), java.math.BigInteger.ZERO));
    } else {
      return dafny.Tuple2.<dafny.DafnySequence<? extends Character>, java.math.BigInteger>create(x, java.math.BigInteger.ZERO);
    }
  }
  public static dafny.DafnySequence<? extends Character> SkipLeadingZeros(dafny.DafnySequence<? extends Character> val) {
    TAIL_CALL_START: while (true) {
      if (((java.math.BigInteger.valueOf((val).length())).signum() == 1) && ((((char)(java.lang.Object)((val).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) == ('0'))) {
        dafny.DafnySequence<? extends Character> _in0 = (val).drop(java.math.BigInteger.ONE);
        val = _in0;
        continue TAIL_CALL_START;
      } else {
        return val;
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> SkipTrailingZeros(dafny.DafnySequence<? extends Character> val) {
    TAIL_CALL_START: while (true) {
      if (((java.math.BigInteger.valueOf((val).length())).signum() == 1) && ((((char)(java.lang.Object)((val).select(dafny.Helpers.toInt(((java.math.BigInteger.valueOf((val).length())).subtract(java.math.BigInteger.ONE))))))) == ('0'))) {
        dafny.DafnySequence<? extends Character> _in0 = (val).take((java.math.BigInteger.valueOf((val).length())).subtract(java.math.BigInteger.ONE));
        val = _in0;
        continue TAIL_CALL_START;
      } else {
        return val;
      }
    }
  }
  public static dafny.Tuple2<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> SplitDot(dafny.DafnySequence<? extends Character> x) {
    Wrappers_Compile.Option<dafny.Tuple2<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>> _0_parts = StandardLibrary_Compile.__default.<Character>SplitOnce_q(dafny.TypeDescriptor.CHAR, x, '.');
    if ((_0_parts).is_Some()) {
      return dafny.Tuple2.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>create(__default.SkipLeadingZeros(((_0_parts).dtor_value()).dtor__0()), __default.SkipTrailingZeros(((_0_parts).dtor_value()).dtor__1()));
    } else {
      return dafny.Tuple2.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>create(__default.SkipLeadingZeros(x), dafny.DafnySequence.asString(""));
    }
  }
  public static byte StrCmp(dafny.DafnySequence<? extends Character> x, dafny.DafnySequence<? extends Character> y)
  {
    TAIL_CALL_START: while (true) {
      if (((java.math.BigInteger.valueOf((x).length())).signum() == 0) && ((java.math.BigInteger.valueOf((y).length())).signum() == 0)) {
        return (byte) 0;
      } else if ((java.math.BigInteger.valueOf((x).length())).signum() == 0) {
        return (byte) -1;
      } else if ((java.math.BigInteger.valueOf((y).length())).signum() == 0) {
        return (byte) 1;
      } else if ((((char)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) < (((char)(java.lang.Object)((y).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) {
        return (byte) -1;
      } else if ((((char)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) > (((char)(java.lang.Object)((y).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) {
        return (byte) 1;
      } else {
        dafny.DafnySequence<? extends Character> _in0 = (x).drop(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends Character> _in1 = (y).drop(java.math.BigInteger.ONE);
        x = _in0;
        y = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> AppendZeros(dafny.DafnySequence<? extends Character> x, java.math.BigInteger newLength)
  {
    return dafny.DafnySequence.<Character>concatenate(x, dafny.DafnySequence.Create(dafny.TypeDescriptor.CHAR, (newLength).subtract(java.math.BigInteger.valueOf((x).length())), ((java.util.function.Function<java.math.BigInteger, Character>)(_0_i_boxed0) -> {
      java.math.BigInteger _0_i = ((java.math.BigInteger)(java.lang.Object)(_0_i_boxed0));
      return '0';
    })));
  }
  public static byte CompareFloatInner(dafny.DafnySequence<? extends Character> x, dafny.DafnySequence<? extends Character> y)
  {
    dafny.Tuple2<dafny.DafnySequence<? extends Character>, java.math.BigInteger> _0_xParts = __default.SplitExp(x);
    dafny.Tuple2<dafny.DafnySequence<? extends Character>, java.math.BigInteger> _1_yParts = __default.SplitExp(y);
    dafny.Tuple2<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _2_xNum = __default.SplitDot((_0_xParts).dtor__0());
    dafny.Tuple2<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _3_yNum = __default.SplitDot((_1_yParts).dtor__0());
    dafny.DafnySequence<? extends Character> _4_xDigits = __default.SkipLeadingZeros(dafny.DafnySequence.<Character>concatenate((_2_xNum).dtor__0(), (_2_xNum).dtor__1()));
    dafny.DafnySequence<? extends Character> _5_yDigits = __default.SkipLeadingZeros(dafny.DafnySequence.<Character>concatenate((_3_yNum).dtor__0(), (_3_yNum).dtor__1()));
    java.math.BigInteger _6_xExp = ((_0_xParts).dtor__1()).subtract(java.math.BigInteger.valueOf(((_2_xNum).dtor__1()).length()));
    java.math.BigInteger _7_yExp = ((_1_yParts).dtor__1()).subtract(java.math.BigInteger.valueOf(((_3_yNum).dtor__1()).length()));
    java.math.BigInteger _8_logX = (_6_xExp).add(java.math.BigInteger.valueOf((_4_xDigits).length()));
    java.math.BigInteger _9_logY = (_7_yExp).add(java.math.BigInteger.valueOf((_5_yDigits).length()));
    if ((_8_logX).compareTo(_9_logY) > 0) {
      return (byte) 1;
    } else if ((_9_logY).compareTo(_8_logX) > 0) {
      return (byte) -1;
    } else if ((java.math.BigInteger.valueOf((_4_xDigits).length())).compareTo(java.math.BigInteger.valueOf((_5_yDigits).length())) < 0) {
      return __default.StrCmp(__default.AppendZeros(_4_xDigits, java.math.BigInteger.valueOf((_5_yDigits).length())), _5_yDigits);
    } else if ((java.math.BigInteger.valueOf((_5_yDigits).length())).compareTo(java.math.BigInteger.valueOf((_4_xDigits).length())) < 0) {
      return __default.StrCmp(_4_xDigits, __default.AppendZeros(_5_yDigits, java.math.BigInteger.valueOf((_4_xDigits).length())));
    } else {
      return __default.StrCmp(_4_xDigits, _5_yDigits);
    }
  }
  public static boolean IsNegative(dafny.DafnySequence<? extends Character> x) {
    return ((java.math.BigInteger.valueOf((x).length())).signum() == 1) && ((((char)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) == ('-'));
  }
  public static dafny.DafnySequence<? extends Character> SkipLeadingPlus(dafny.DafnySequence<? extends Character> x) {
    if (((java.math.BigInteger.valueOf((x).length())).signum() == 1) && ((((char)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) == ('+'))) {
      return (x).drop(java.math.BigInteger.ONE);
    } else {
      return x;
    }
  }
  public static boolean IsZero(dafny.DafnySequence<? extends Character> x) {
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((x).length())).signum() == 0) {
        return true;
      } else if (((((char)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) == ('0')) || ((((char)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) == ('.'))) {
        dafny.DafnySequence<? extends Character> _in0 = (x).drop(java.math.BigInteger.ONE);
        x = _in0;
        continue TAIL_CALL_START;
      } else if ((('1') <= (((char)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) && ((((char)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) <= ('9'))) {
        return false;
      } else {
        return true;
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> RecognizeZero(dafny.DafnySequence<? extends Character> x) {
    if (__default.IsNegative(x)) {
      if (__default.IsZero((x).drop(java.math.BigInteger.ONE))) {
        return dafny.DafnySequence.asString("0");
      } else {
        return x;
      }
    } else if (__default.IsZero(x)) {
      return dafny.DafnySequence.asString("0");
    } else {
      return x;
    }
  }
  public static dafny.DafnySequence<? extends Character> CleanNumber(dafny.DafnySequence<? extends Character> x) {
    return __default.RecognizeZero(__default.SkipLeadingPlus(__default.SkipLeadingSpace(x)));
  }
  public static byte CompareFloat(dafny.DafnySequence<? extends Character> x, dafny.DafnySequence<? extends Character> y)
  {
    dafny.DafnySequence<? extends Character> _0_x = __default.CleanNumber(x);
    dafny.DafnySequence<? extends Character> _1_y = __default.CleanNumber(y);
    if ((__default.IsNegative(_0_x)) && (__default.IsNegative(_1_y))) {
      return __default.CompareFloatInner((_1_y).drop(java.math.BigInteger.ONE), (_0_x).drop(java.math.BigInteger.ONE));
    } else if (__default.IsNegative(_0_x)) {
      return (byte) -1;
    } else if (__default.IsNegative(_1_y)) {
      return (byte) 1;
    } else {
      return __default.CompareFloatInner(_0_x, _1_y);
    }
  }
  public static byte Less()
  {
    return (byte) -1;
  }
  public static byte Equal()
  {
    return (byte) 0;
  }
  public static byte Greater()
  {
    return (byte) 1;
  }
  @Override
  public java.lang.String toString() {
    return "FloatCompare._default";
  }
}
