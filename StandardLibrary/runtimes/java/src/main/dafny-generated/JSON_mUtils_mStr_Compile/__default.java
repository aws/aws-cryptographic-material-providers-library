// Class __default
// Dafny class __default compiled into Java
package JSON_mUtils_mStr_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends Character> OfNat(java.math.BigInteger n, java.math.BigInteger base)
  {
    return JSON_mUtils_mStr_mCharStrConversion_Compile.__default.OfNat__any(n, (__default.HEX__DIGITS()).take(base));
  }
  public static dafny.DafnySequence<? extends Character> OfInt(java.math.BigInteger n, java.math.BigInteger base)
  {
    return JSON_mUtils_mStr_mCharStrConversion_Compile.__default.OfInt__any(n, (__default.HEX__DIGITS()).take(base), '-');
  }
  public static java.math.BigInteger ToNat(dafny.DafnySequence<? extends Character> str, java.math.BigInteger base)
  {
    return JSON_mUtils_mStr_mCharStrConversion_Compile.__default.ToNat__any(str, base, __default.HEX__TABLE());
  }
  public static java.math.BigInteger ToInt(dafny.DafnySequence<? extends Character> str, java.math.BigInteger base)
  {
    return JSON_mUtils_mStr_mCharStrConversion_Compile.__default.ToInt__any(str, '-', base, __default.HEX__TABLE());
  }
  public static dafny.DafnySequence<? extends Character> EscapeQuotes(dafny.DafnySequence<? extends Character> str) {
    return JSON_mUtils_mStr_mCharStrEscaping_Compile.__default.Escape(str, dafny.DafnySet.<Character> of('\"', '\''), '\\');
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, JSON_mUtils_mStr_mCharStrEscaping_Compile.UnescapeError> UnescapeQuotes(dafny.DafnySequence<? extends Character> str) {
    return JSON_mUtils_mStr_mCharStrEscaping_Compile.__default.Unescape(str, '\\');
  }
  public static void Test()
  {
    if (!((__default.OfInt(java.math.BigInteger.ZERO, java.math.BigInteger.valueOf(10L))).equals(dafny.DafnySequence.asString("0")))) {
      throw new dafny.DafnyHaltException("/Users/ryanemer/workspace/MCMs/MCM-123211339/aws-cryptographic-material-providers-library/libraries/src/JSON/Utils/Str.dfy(229,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((__default.OfInt(java.math.BigInteger.valueOf(3L), java.math.BigInteger.valueOf(10L))).equals(dafny.DafnySequence.asString("3")))) {
      throw new dafny.DafnyHaltException("/Users/ryanemer/workspace/MCMs/MCM-123211339/aws-cryptographic-material-providers-library/libraries/src/JSON/Utils/Str.dfy(230,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((__default.OfInt(java.math.BigInteger.valueOf(302L), java.math.BigInteger.valueOf(10L))).equals(dafny.DafnySequence.asString("302")))) {
      throw new dafny.DafnyHaltException("/Users/ryanemer/workspace/MCMs/MCM-123211339/aws-cryptographic-material-providers-library/libraries/src/JSON/Utils/Str.dfy(231,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((__default.OfInt(java.math.BigInteger.valueOf(-3L), java.math.BigInteger.valueOf(10L))).equals(dafny.DafnySequence.asString("-3")))) {
      throw new dafny.DafnyHaltException("/Users/ryanemer/workspace/MCMs/MCM-123211339/aws-cryptographic-material-providers-library/libraries/src/JSON/Utils/Str.dfy(232,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!((__default.OfInt(java.math.BigInteger.valueOf(-302L), java.math.BigInteger.valueOf(10L))).equals(dafny.DafnySequence.asString("-302")))) {
      throw new dafny.DafnyHaltException("/Users/ryanemer/workspace/MCMs/MCM-123211339/aws-cryptographic-material-providers-library/libraries/src/JSON/Utils/Str.dfy(233,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static dafny.DafnySequence<? extends Character> OfBool(boolean b) {
    if (b) {
      return dafny.DafnySequence.asString("true");
    } else {
      return dafny.DafnySequence.asString("false");
    }
  }
  public static dafny.DafnySequence<? extends Character> OfChar(char c) {
    return dafny.DafnySequence.<Character> of(c);
  }
  public static dafny.DafnySequence<? extends Character> Join(dafny.DafnySequence<? extends Character> sep, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> strs)
  {
    dafny.DafnySequence<? extends Character> _0___accumulator = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((strs).length())).signum() == 0) {
        return dafny.DafnySequence.<Character>concatenate(_0___accumulator, dafny.DafnySequence.asString(""));
      } else if (java.util.Objects.equals(java.math.BigInteger.valueOf((strs).length()), java.math.BigInteger.ONE)) {
        return dafny.DafnySequence.<Character>concatenate(_0___accumulator, ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((strs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))));
      } else {
        _0___accumulator = dafny.DafnySequence.<Character>concatenate(_0___accumulator, dafny.DafnySequence.<Character>concatenate(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((strs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), sep));
        dafny.DafnySequence<? extends Character> _in0 = sep;
        dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _in1 = (strs).drop(java.math.BigInteger.ONE);
        sep = _in0;
        strs = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> Concat(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> strs) {
    dafny.DafnySequence<? extends Character> _0___accumulator = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((strs).length())).signum() == 0) {
        return dafny.DafnySequence.<Character>concatenate(_0___accumulator, dafny.DafnySequence.asString(""));
      } else {
        _0___accumulator = dafny.DafnySequence.<Character>concatenate(_0___accumulator, ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((strs).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))));
        dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _in0 = (strs).drop(java.math.BigInteger.ONE);
        strs = _in0;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> HEX__DIGITS()
  {
    return dafny.DafnySequence.asString("0123456789ABCDEF");
  }
  public static dafny.DafnyMap<? extends Character, ? extends java.math.BigInteger> HEX__TABLE()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2('0', java.math.BigInteger.ZERO), new dafny.Tuple2('1', java.math.BigInteger.ONE), new dafny.Tuple2('2', java.math.BigInteger.valueOf(2L)), new dafny.Tuple2('3', java.math.BigInteger.valueOf(3L)), new dafny.Tuple2('4', java.math.BigInteger.valueOf(4L)), new dafny.Tuple2('5', java.math.BigInteger.valueOf(5L)), new dafny.Tuple2('6', java.math.BigInteger.valueOf(6L)), new dafny.Tuple2('7', java.math.BigInteger.valueOf(7L)), new dafny.Tuple2('8', java.math.BigInteger.valueOf(8L)), new dafny.Tuple2('9', java.math.BigInteger.valueOf(9L)), new dafny.Tuple2('a', java.math.BigInteger.valueOf(10L)), new dafny.Tuple2('b', java.math.BigInteger.valueOf(11L)), new dafny.Tuple2('c', java.math.BigInteger.valueOf(12L)), new dafny.Tuple2('d', java.math.BigInteger.valueOf(13L)), new dafny.Tuple2('e', java.math.BigInteger.valueOf(14L)), new dafny.Tuple2('f', java.math.BigInteger.valueOf(15L)), new dafny.Tuple2('A', java.math.BigInteger.valueOf(10L)), new dafny.Tuple2('B', java.math.BigInteger.valueOf(11L)), new dafny.Tuple2('C', java.math.BigInteger.valueOf(12L)), new dafny.Tuple2('D', java.math.BigInteger.valueOf(13L)), new dafny.Tuple2('E', java.math.BigInteger.valueOf(14L)), new dafny.Tuple2('F', java.math.BigInteger.valueOf(15L)));
  }
  @Override
  public java.lang.String toString() {
    return "JSON.Utils.Str._default";
  }
}
