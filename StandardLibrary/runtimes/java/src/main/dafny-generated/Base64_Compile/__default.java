// Class __default
// Dafny class __default compiled into Java
package Base64_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean IsBase64Char(char c) {
    return (((((c) == ('+')) || ((c) == ('/'))) || ((('0') <= (c)) && ((c) <= ('9')))) || ((('A') <= (c)) && ((c) <= ('Z')))) || ((('a') <= (c)) && ((c) <= ('z')));
  }
  public static boolean IsUnpaddedBase64String(dafny.DafnySequence<? extends Character> s) {
    return ((dafny.DafnyEuclidean.EuclideanModulus(java.math.BigInteger.valueOf((s).length()), java.math.BigInteger.valueOf(4L))).signum() == 0) && (((java.util.function.Function<dafny.DafnySequence<? extends Character>, Boolean>)(_0_s) -> dafny.Helpers.Quantifier((_0_s).UniqueElements(), true, ((_forall_var_0_boxed0) -> {
      char _forall_var_0 = ((char)(java.lang.Object)(_forall_var_0_boxed0));
      char _1_k = (char)_forall_var_0;
      return !((_0_s).contains(_1_k)) || (__default.IsBase64Char(_1_k));
    }))).apply(s));
  }
  public static char IndexToChar(byte i) {
    if ((i) == ((byte) 63)) {
      return '/';
    } else if ((i) == ((byte) 62)) {
      return '+';
    } else if ((java.lang.Integer.compareUnsigned((byte) 52, i) <= 0) && (java.lang.Integer.compareUnsigned(i, (byte) 61) <= 0)) {
      return (char)java.lang.Byte.toUnsignedInt((byte) (byte) ((byte)((i) - ((byte) 4))));
    } else if ((java.lang.Integer.compareUnsigned((byte) 26, i) <= 0) && (java.lang.Integer.compareUnsigned(i, (byte) 51) <= 0)) {
      return (char) (((char)java.lang.Byte.toUnsignedInt(i)) + ((char)dafny.Helpers.toInt((java.math.BigInteger.valueOf(71L)))));
    } else {
      return (char) (((char)java.lang.Byte.toUnsignedInt(i)) + ((char)dafny.Helpers.toInt((java.math.BigInteger.valueOf(65L)))));
    }
  }
  public static byte CharToIndex(char c) {
    if ((c) == ('/')) {
      return (byte) 63;
    } else if ((c) == ('+')) {
      return (byte) 62;
    } else if ((('0') <= (c)) && ((c) <= ('9'))) {
      return ((byte) ((char) ((c) + ((char)dafny.Helpers.toInt((java.math.BigInteger.valueOf(4L)))))));
    } else if ((('a') <= (c)) && ((c) <= ('z'))) {
      return ((byte) ((char) ((c) - ((char)dafny.Helpers.toInt((java.math.BigInteger.valueOf(71L)))))));
    } else {
      return ((byte) ((char) ((c) - ((char)dafny.Helpers.toInt((java.math.BigInteger.valueOf(65L)))))));
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> UInt24ToSeq(int x) {
    byte _0_b0 = ((byte) (java.lang.Integer.divideUnsigned(x, 65536)));
    int _1_x0 = (int) ((x) - ((int) ((java.lang.Byte.toUnsignedInt(_0_b0)) * (65536))));
    byte _2_b1 = ((byte) (java.lang.Integer.divideUnsigned(_1_x0, 256)));
    byte _3_b2 = ((byte) (java.lang.Integer.remainderUnsigned(_1_x0, 256)));
    return dafny.DafnySequence.<java.lang.Byte> of(_0_b0, _2_b1, _3_b2);
  }
  public static int SeqToUInt24(dafny.DafnySequence<? extends java.lang.Byte> s) {
    return (int) (((int) (((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) * (65536))) + ((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))))) * (256))))) + (java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L)))))))));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> UInt24ToIndexSeq(int x) {
    byte _0_b0 = ((byte) (java.lang.Integer.divideUnsigned(x, 262144)));
    int _1_x0 = (int) ((x) - ((int) ((java.lang.Byte.toUnsignedInt(_0_b0)) * (262144))));
    byte _2_b1 = ((byte) (java.lang.Integer.divideUnsigned(_1_x0, 4096)));
    int _3_x1 = (int) ((_1_x0) - ((int) ((java.lang.Byte.toUnsignedInt(_2_b1)) * (4096))));
    byte _4_b2 = ((byte) (java.lang.Integer.divideUnsigned(_3_x1, 64)));
    byte _5_b3 = ((byte) (java.lang.Integer.remainderUnsigned(_3_x1, 64)));
    return dafny.DafnySequence.<java.lang.Byte> of(_0_b0, _2_b1, _4_b2, _5_b3);
  }
  public static int IndexSeqToUInt24(dafny.DafnySequence<? extends java.lang.Byte> s) {
    return (int) (((int) (((int) (((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))) * (262144))) + ((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))))) * (4096))))) + ((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L)))))))) * (64))))) + (java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(3L)))))))));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> DecodeBlock(dafny.DafnySequence<? extends java.lang.Byte> s) {
    return __default.UInt24ToSeq(__default.IndexSeqToUInt24(s));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> EncodeBlock(dafny.DafnySequence<? extends java.lang.Byte> s) {
    return __default.UInt24ToIndexSeq(__default.SeqToUInt24(s));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> DecodeRecursively(dafny.DafnySequence<? extends java.lang.Byte> s) {
    dafny.DafnySequence<? extends java.lang.Byte> _0___accumulator = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((s).length())).signum() == 0) {
        return dafny.DafnySequence.<java.lang.Byte>concatenate(_0___accumulator, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      } else {
        _0___accumulator = dafny.DafnySequence.<java.lang.Byte>concatenate(_0___accumulator, __default.DecodeBlock((s).take(java.math.BigInteger.valueOf(4L))));
        dafny.DafnySequence<? extends java.lang.Byte> _in0 = (s).drop(java.math.BigInteger.valueOf(4L));
        s = _in0;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> EncodeRecursively(dafny.DafnySequence<? extends java.lang.Byte> b) {
    dafny.DafnySequence<? extends java.lang.Byte> _0___accumulator = dafny.DafnySequence.<java.lang.Byte> empty(index._typeDescriptor());
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((b).length())).signum() == 0) {
        return dafny.DafnySequence.<java.lang.Byte>concatenate(_0___accumulator, dafny.DafnySequence.<java.lang.Byte> empty(index._typeDescriptor()));
      } else {
        _0___accumulator = dafny.DafnySequence.<java.lang.Byte>concatenate(_0___accumulator, __default.EncodeBlock((b).take(java.math.BigInteger.valueOf(3L))));
        dafny.DafnySequence<? extends java.lang.Byte> _in0 = (b).drop(java.math.BigInteger.valueOf(3L));
        b = _in0;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> FromCharsToIndices(dafny.DafnySequence<? extends Character> s) {
    return dafny.DafnySequence.Create(index._typeDescriptor(), java.math.BigInteger.valueOf((s).length()), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, java.util.function.Function<java.math.BigInteger, java.lang.Byte>>)(_0_s) -> ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_1_i_boxed0) -> {
      java.math.BigInteger _1_i = ((java.math.BigInteger)(java.lang.Object)(_1_i_boxed0));
      return __default.CharToIndex(((char)(java.lang.Object)((_0_s).select(dafny.Helpers.toInt((_1_i))))));
    })).apply(s));
  }
  public static dafny.DafnySequence<? extends Character> FromIndicesToChars(dafny.DafnySequence<? extends java.lang.Byte> b) {
    return dafny.DafnySequence.Create(dafny.TypeDescriptor.CHAR, java.math.BigInteger.valueOf((b).length()), ((java.util.function.Function<dafny.DafnySequence<? extends java.lang.Byte>, java.util.function.Function<java.math.BigInteger, Character>>)(_0_b) -> ((java.util.function.Function<java.math.BigInteger, Character>)(_1_i_boxed0) -> {
      java.math.BigInteger _1_i = ((java.math.BigInteger)(java.lang.Object)(_1_i_boxed0));
      return __default.IndexToChar(((byte)(java.lang.Object)((_0_b).select(dafny.Helpers.toInt((_1_i))))));
    })).apply(b));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> DecodeUnpadded(dafny.DafnySequence<? extends Character> s) {
    return __default.DecodeRecursively(__default.FromCharsToIndices(s));
  }
  public static dafny.DafnySequence<? extends Character> EncodeUnpadded(dafny.DafnySequence<? extends java.lang.Byte> b) {
    return __default.FromIndicesToChars(__default.EncodeRecursively(b));
  }
  public static boolean Is1Padding(dafny.DafnySequence<? extends Character> s) {
    return (((((java.util.Objects.equals(java.math.BigInteger.valueOf((s).length()), java.math.BigInteger.valueOf(4L))) && (__default.IsBase64Char(((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))))) && (__default.IsBase64Char(((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))))) && (__default.IsBase64Char(((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))))))) && (((dafny.Helpers.remainderUnsignedByte(__default.CharToIndex(((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))))), (byte) 4)) == 0 ? 0 : 1) == 0)) && ((((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(3L))))))) == ('='));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Decode1Padding(dafny.DafnySequence<? extends Character> s) {
    dafny.DafnySequence<? extends java.lang.Byte> _0_d = __default.DecodeBlock(dafny.DafnySequence.<java.lang.Byte> of(__default.CharToIndex(((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))), __default.CharToIndex(((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))), __default.CharToIndex(((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))))), (byte) 0));
    return dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((_0_d).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), ((byte)(java.lang.Object)((_0_d).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))));
  }
  public static dafny.DafnySequence<? extends Character> Encode1Padding(dafny.DafnySequence<? extends java.lang.Byte> b) {
    dafny.DafnySequence<? extends java.lang.Byte> _0_e = __default.EncodeBlock(dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((b).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), ((byte)(java.lang.Object)((b).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))), (byte) 0));
    return dafny.DafnySequence.<Character> of(__default.IndexToChar(((byte)(java.lang.Object)((_0_e).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))), __default.IndexToChar(((byte)(java.lang.Object)((_0_e).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))), __default.IndexToChar(((byte)(java.lang.Object)((_0_e).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))))), '=');
  }
  public static boolean Is2Padding(dafny.DafnySequence<? extends Character> s) {
    return (((((java.util.Objects.equals(java.math.BigInteger.valueOf((s).length()), java.math.BigInteger.valueOf(4L))) && (__default.IsBase64Char(((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))))) && (__default.IsBase64Char(((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))))) && (((dafny.Helpers.remainderUnsignedByte(__default.CharToIndex(((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))), (byte) 16)) == 0 ? 0 : 1) == 0)) && ((((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))))) == ('='))) && ((((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(3L))))))) == ('='));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Decode2Padding(dafny.DafnySequence<? extends Character> s) {
    dafny.DafnySequence<? extends java.lang.Byte> _0_d = __default.DecodeBlock(dafny.DafnySequence.<java.lang.Byte> of(__default.CharToIndex(((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))), __default.CharToIndex(((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))), (byte) 0, (byte) 0));
    return dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((_0_d).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))));
  }
  public static dafny.DafnySequence<? extends Character> Encode2Padding(dafny.DafnySequence<? extends java.lang.Byte> b) {
    dafny.DafnySequence<? extends java.lang.Byte> _0_e = __default.EncodeBlock(dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((b).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), (byte) 0, (byte) 0));
    return dafny.DafnySequence.<Character> of(__default.IndexToChar(((byte)(java.lang.Object)((_0_e).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))), __default.IndexToChar(((byte)(java.lang.Object)((_0_e).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))), '=', '=');
  }
  public static boolean IsBase64String(dafny.DafnySequence<? extends Character> s) {
    java.math.BigInteger _0_finalBlockStart = (java.math.BigInteger.valueOf((s).length())).subtract(java.math.BigInteger.valueOf(4L));
    return ((dafny.DafnyEuclidean.EuclideanModulus(java.math.BigInteger.valueOf((s).length()), java.math.BigInteger.valueOf(4L))).signum() == 0) && ((__default.IsUnpaddedBase64String(s)) || ((__default.IsUnpaddedBase64String((s).take(_0_finalBlockStart))) && ((__default.Is1Padding((s).drop(_0_finalBlockStart))) || (__default.Is2Padding((s).drop(_0_finalBlockStart))))));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> DecodeValid(dafny.DafnySequence<? extends Character> s) {
    if ((s).equals(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR))) {
      return dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    } else {
      java.math.BigInteger _0_finalBlockStart = (java.math.BigInteger.valueOf((s).length())).subtract(java.math.BigInteger.valueOf(4L));
      dafny.DafnySequence<? extends Character> _1_prefix = (s).take(_0_finalBlockStart);
      dafny.DafnySequence<? extends Character> _2_suffix = (s).drop(_0_finalBlockStart);
      if (__default.Is1Padding(_2_suffix)) {
        return dafny.DafnySequence.<java.lang.Byte>concatenate(__default.DecodeUnpadded(_1_prefix), __default.Decode1Padding(_2_suffix));
      } else if (__default.Is2Padding(_2_suffix)) {
        return dafny.DafnySequence.<java.lang.Byte>concatenate(__default.DecodeUnpadded(_1_prefix), __default.Decode2Padding(_2_suffix));
      } else {
        return __default.DecodeUnpadded(s);
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> Decode(dafny.DafnySequence<? extends Character> s) {
    if (__default.IsBase64String(s)) {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), __default.DecodeValid(s));
    } else {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("The encoding is malformed"));
    }
  }
  public static dafny.DafnySequence<? extends Character> Encode(dafny.DafnySequence<? extends java.lang.Byte> b) {
    if ((dafny.DafnyEuclidean.EuclideanModulus(java.math.BigInteger.valueOf((b).length()), java.math.BigInteger.valueOf(3L))).signum() == 0) {
      dafny.DafnySequence<? extends Character> _0_s = __default.EncodeUnpadded(b);
      return _0_s;
    } else if (java.util.Objects.equals(dafny.DafnyEuclidean.EuclideanModulus(java.math.BigInteger.valueOf((b).length()), java.math.BigInteger.valueOf(3L)), java.math.BigInteger.ONE)) {
      dafny.DafnySequence<? extends Character> _1_s1 = __default.EncodeUnpadded((b).take((java.math.BigInteger.valueOf((b).length())).subtract(java.math.BigInteger.ONE)));
      dafny.DafnySequence<? extends Character> _2_s2 = __default.Encode2Padding((b).drop((java.math.BigInteger.valueOf((b).length())).subtract(java.math.BigInteger.ONE)));
      dafny.DafnySequence<? extends Character> _3_s = dafny.DafnySequence.<Character>concatenate(_1_s1, _2_s2);
      return _3_s;
    } else {
      dafny.DafnySequence<? extends Character> _4_s1 = __default.EncodeUnpadded((b).take((java.math.BigInteger.valueOf((b).length())).subtract(java.math.BigInteger.valueOf(2L))));
      dafny.DafnySequence<? extends Character> _5_s2 = __default.Encode1Padding((b).drop((java.math.BigInteger.valueOf((b).length())).subtract(java.math.BigInteger.valueOf(2L))));
      dafny.DafnySequence<? extends Character> _6_s = dafny.DafnySequence.<Character>concatenate(_4_s1, _5_s2);
      return _6_s;
    }
  }
  @Override
  public java.lang.String toString() {
    return "Base64._default";
  }
}
