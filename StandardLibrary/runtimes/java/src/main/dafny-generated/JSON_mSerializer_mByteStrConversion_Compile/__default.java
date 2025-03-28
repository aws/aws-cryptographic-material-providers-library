// Class __default
// Dafny class __default compiled into Java
package JSON_mSerializer_mByteStrConversion_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends java.math.BigInteger> Digits(java.math.BigInteger n, java.math.BigInteger base)
  {
    if ((n).signum() == 0) {
      return dafny.DafnySequence.<java.math.BigInteger> empty(dafny.TypeDescriptor.BIG_INTEGER);
    } else {
      dafny.DafnySequence<? extends java.math.BigInteger> _0_digits_k = __default.Digits(dafny.DafnyEuclidean.EuclideanDivision(n, base), base);
      dafny.DafnySequence<? extends java.math.BigInteger> _1_digits = dafny.DafnySequence.<java.math.BigInteger>concatenate(_0_digits_k, dafny.DafnySequence.<java.math.BigInteger> of(dafny.TypeDescriptor.BIG_INTEGER, dafny.DafnyEuclidean.EuclideanModulus(n, base)));
      return _1_digits;
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> OfDigits(dafny.DafnySequence<? extends java.math.BigInteger> digits, dafny.DafnySequence<? extends java.lang.Byte> chars)
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0___accumulator = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    TAIL_CALL_START: while (true) {
      if ((digits).equals(dafny.DafnySequence.<java.math.BigInteger> empty(dafny.TypeDescriptor.BIG_INTEGER))) {
        return dafny.DafnySequence.<java.lang.Byte>concatenate(_0___accumulator, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      } else {
        _0___accumulator = dafny.DafnySequence.<java.lang.Byte>concatenate(_0___accumulator, dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((chars).select(dafny.Helpers.toInt((((java.math.BigInteger)(java.lang.Object)((digits).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))))))));
        dafny.DafnySequence<? extends java.math.BigInteger> _in0 = (digits).drop(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends java.lang.Byte> _in1 = chars;
        digits = _in0;
        chars = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> OfNat__any(java.math.BigInteger n, dafny.DafnySequence<? extends java.lang.Byte> chars)
  {
    java.math.BigInteger _0_base = java.math.BigInteger.valueOf((chars).length());
    if ((n).signum() == 0) {
      return dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((chars).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))));
    } else {
      return __default.OfDigits(__default.Digits(n, _0_base), chars);
    }
  }
  public static boolean NumberStr(dafny.DafnySequence<? extends java.lang.Byte> str, byte minus, java.util.function.Function<java.lang.Byte, Boolean> is__digit)
  {
    return !(!(str).equals(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()))) || ((((((byte)(java.lang.Object)((str).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) == (minus)) || (((boolean)(java.lang.Object)((is__digit).apply(((byte)(java.lang.Object)((str).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))))))) && (((dafny.Function2<dafny.DafnySequence<? extends java.lang.Byte>, java.util.function.Function<java.lang.Byte, Boolean>, Boolean>)(_0_str, _1_is__digit) -> dafny.Helpers.Quantifier(((_0_str).drop(java.math.BigInteger.ONE)).UniqueElements(), true, ((_forall_var_0_boxed0) -> {
      byte _forall_var_0 = ((byte)(java.lang.Object)(_forall_var_0_boxed0));
      byte _2_c = (byte)_forall_var_0;
      return !(((_0_str).drop(java.math.BigInteger.ONE)).contains(_2_c)) || (((boolean)(java.lang.Object)((_1_is__digit).apply(_2_c))));
    }))).apply(str, is__digit)));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> OfInt__any(java.math.BigInteger n, dafny.DafnySequence<? extends java.lang.Byte> chars, byte minus)
  {
    if ((n).signum() != -1) {
      return __default.OfNat__any(n, chars);
    } else {
      return dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte> of(minus), __default.OfNat__any((java.math.BigInteger.ZERO).subtract(n), chars));
    }
  }
  public static java.math.BigInteger ToNat__any(dafny.DafnySequence<? extends java.lang.Byte> str, java.math.BigInteger base, dafny.DafnyMap<? extends java.lang.Byte, ? extends java.math.BigInteger> digits)
  {
    if ((str).equals(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()))) {
      return java.math.BigInteger.ZERO;
    } else {
      return ((__default.ToNat__any((str).take((java.math.BigInteger.valueOf((str).length())).subtract(java.math.BigInteger.ONE)), base, digits)).multiply(base)).add(((java.math.BigInteger)(java.lang.Object)((digits).get(((byte)(java.lang.Object)((str).select(dafny.Helpers.toInt(((java.math.BigInteger.valueOf((str).length())).subtract(java.math.BigInteger.ONE))))))))));
    }
  }
  public static java.math.BigInteger ToInt__any(dafny.DafnySequence<? extends java.lang.Byte> str, byte minus, java.math.BigInteger base, dafny.DafnyMap<? extends java.lang.Byte, ? extends java.math.BigInteger> digits)
  {
    if ((dafny.DafnySequence.<java.lang.Byte> of(minus)).isPrefixOf(str)) {
      return (java.math.BigInteger.ZERO).subtract(__default.ToNat__any((str).drop(java.math.BigInteger.ONE), base, digits));
    } else {
      return __default.ToNat__any(str, base, digits);
    }
  }
  @Override
  public java.lang.String toString() {
    return "JSON.Serializer.ByteStrConversion._default";
  }
}
