// Class __default
// Dafny class __default compiled into Java
package StandardLibrary_mString_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends java.math.BigInteger> Int2Digits(java.math.BigInteger n, java.math.BigInteger base)
  {
    dafny.DafnySequence<? extends java.math.BigInteger> _0___accumulator = dafny.DafnySequence.<java.math.BigInteger> empty(dafny.TypeDescriptor.BIG_INTEGER);
    TAIL_CALL_START: while (true) {
      if ((n).signum() == 0) {
        return dafny.DafnySequence.<java.math.BigInteger>concatenate(dafny.DafnySequence.<java.math.BigInteger> empty(dafny.TypeDescriptor.BIG_INTEGER), _0___accumulator);
      } else {
        _0___accumulator = dafny.DafnySequence.<java.math.BigInteger>concatenate(dafny.DafnySequence.<java.math.BigInteger> of(dafny.TypeDescriptor.BIG_INTEGER, dafny.DafnyEuclidean.EuclideanModulus(n, base)), _0___accumulator);
        java.math.BigInteger _in0 = dafny.DafnyEuclidean.EuclideanDivision(n, base);
        java.math.BigInteger _in1 = base;
        n = _in0;
        base = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> Digits2String(dafny.DafnySequence<? extends java.math.BigInteger> digits, dafny.DafnySequence<? extends Character> chars)
  {
    dafny.DafnySequence<? extends Character> _0___accumulator = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    TAIL_CALL_START: while (true) {
      if ((digits).equals(dafny.DafnySequence.<java.math.BigInteger> empty(dafny.TypeDescriptor.BIG_INTEGER))) {
        return dafny.DafnySequence.<Character>concatenate(_0___accumulator, dafny.DafnySequence.asString(""));
      } else {
        _0___accumulator = dafny.DafnySequence.<Character>concatenate(_0___accumulator, dafny.DafnySequence.<Character> of(((char)(java.lang.Object)((chars).select(dafny.Helpers.toInt((((java.math.BigInteger)(java.lang.Object)((digits).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))))))));
        dafny.DafnySequence<? extends java.math.BigInteger> _in0 = (digits).drop(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends Character> _in1 = chars;
        digits = _in0;
        chars = _in1;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> Int2String(java.math.BigInteger n, dafny.DafnySequence<? extends Character> chars)
  {
    java.math.BigInteger _0_base = java.math.BigInteger.valueOf((chars).length());
    if ((n).signum() == 0) {
      return dafny.DafnySequence.asString("0");
    } else if ((n).signum() == 1) {
      return __default.Digits2String(__default.Int2Digits(n, _0_base), chars);
    } else {
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("-"), __default.Digits2String(__default.Int2Digits((java.math.BigInteger.ZERO).subtract(n), _0_base), chars));
    }
  }
  public static dafny.DafnySequence<? extends Character> Base10Int2String(java.math.BigInteger n) {
    return __default.Int2String(n, __default.Base10());
  }
  public static Wrappers_Compile.Option<java.math.BigInteger> HasSubString(dafny.DafnySequence<? extends Character> haystack, dafny.DafnySequence<? extends Character> needle)
  {
    Wrappers_Compile.Option<java.math.BigInteger> o = Wrappers_Compile.Option.<java.math.BigInteger>Default(_System.nat._typeDescriptor());
    if ((java.math.BigInteger.valueOf((haystack).length())).compareTo(java.math.BigInteger.valueOf((needle).length())) < 0) {
      o = Wrappers_Compile.Option.<java.math.BigInteger>create_None(_System.nat._typeDescriptor());
      return o;
    }
    if (!((java.math.BigInteger.valueOf((haystack).length())).compareTo((StandardLibrary_mUInt_Compile.__default.UINT64__MAX__LIMIT()).subtract(java.math.BigInteger.ONE)) <= 0)) {
      throw new dafny.DafnyHaltException("src/String.dfy(75,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    long _0_size;
    _0_size = (long) (needle).cardinalityInt();
    long _1_limit;
    _1_limit = (long) (long) (((long) (long) (((long) (haystack).cardinalityInt()) - (_0_size))) + ((long) 1L));
    long _hi0 = _1_limit;
    for (long _2_index = (long) 0L; java.lang.Long.compareUnsigned(_2_index, _hi0) < 0; _2_index++) {
      if (StandardLibrary_mSequence_Compile.__default.<Character>SequenceEqual(dafny.TypeDescriptor.CHAR, haystack, needle, _2_index, (long) 0L, _0_size)) {
        o = Wrappers_Compile.Option.<java.math.BigInteger>create_Some(_System.nat._typeDescriptor(), dafny.Helpers.unsignedToBigInteger(_2_index));
        return o;
      }
    }
    o = Wrappers_Compile.Option.<java.math.BigInteger>create_None(_System.nat._typeDescriptor());
    return o;
  }
  public static dafny.DafnySequence<? extends Character> Base10()
  {
    return dafny.DafnySequence.<Character> of('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');
  }
  @Override
  public java.lang.String toString() {
    return "StandardLibrary.String._default";
  }
}
