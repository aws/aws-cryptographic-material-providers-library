// Class _ExternBase___default
// Dafny class __default compiled into Java
package UTF8;

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

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> CreateEncodeSuccess(dafny.DafnySequence<? extends java.lang.Byte> bytes) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>create_Success(ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), bytes);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> CreateEncodeFailure(dafny.DafnySequence<? extends Character> error) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>create_Failure(ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), error);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> CreateDecodeSuccess(dafny.DafnySequence<? extends Character> s) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), s);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> CreateDecodeFailure(dafny.DafnySequence<? extends Character> error) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>create_Failure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), error);
  }
  public static boolean IsASCIIString(dafny.DafnySequence<? extends Character> s) {
    return ((java.util.function.Function<dafny.DafnySequence<? extends Character>, Boolean>)(_0_s) -> dafny.Helpers.Quantifier(dafny.Helpers.IntegerRange(java.math.BigInteger.ZERO, java.math.BigInteger.valueOf((_0_s).length())), true, ((_forall_var_0_boxed0) -> {
      java.math.BigInteger _forall_var_0 = ((java.math.BigInteger)(java.lang.Object)(_forall_var_0_boxed0));
      java.math.BigInteger _1_i = (java.math.BigInteger)_forall_var_0;
      return !(((_1_i).signum() != -1) && ((_1_i).compareTo(java.math.BigInteger.valueOf((_0_s).length())) < 0)) || ((java.math.BigInteger.valueOf(((char)(java.lang.Object)((_0_s).select(dafny.Helpers.toInt((_1_i))))))).compareTo(java.math.BigInteger.valueOf(128L)) < 0);
    }))).apply(s);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> EncodeAscii(dafny.DafnySequence<? extends Character> s) {
    dafny.DafnySequence<? extends java.lang.Byte> _0___accumulator = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    TAIL_CALL_START: while (true) {
      if ((java.math.BigInteger.valueOf((s).length())).signum() == 0) {
        return dafny.DafnySequence.<java.lang.Byte>concatenate(_0___accumulator, dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      } else {
        dafny.DafnySequence<? extends java.lang.Byte> _1_x = dafny.DafnySequence.<java.lang.Byte> of(((byte) (((char)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))));
        _0___accumulator = dafny.DafnySequence.<java.lang.Byte>concatenate(_0___accumulator, _1_x);
        dafny.DafnySequence<? extends Character> _in0 = (s).drop(java.math.BigInteger.ONE);
        s = _in0;
        continue TAIL_CALL_START;
      }
    }
  }
  public static boolean Uses1Byte(dafny.DafnySequence<? extends java.lang.Byte> s) {
    return (((((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) == 0 ? 0 : 1) != -1) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), (byte) 127) <= 0);
  }
  public static boolean Uses2Bytes(dafny.DafnySequence<? extends java.lang.Byte> s) {
    return ((java.lang.Integer.compareUnsigned((byte) 194, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), (byte) 223) <= 0)) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))), (byte) 191) <= 0));
  }
  public static boolean Uses3Bytes(dafny.DafnySequence<? extends java.lang.Byte> s) {
    return ((((((((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) == ((byte) 224)) && ((java.lang.Integer.compareUnsigned((byte) 160, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))), (byte) 191) <= 0))) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L)))))), (byte) 191) <= 0))) || ((((java.lang.Integer.compareUnsigned((byte) 225, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), (byte) 236) <= 0)) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))), (byte) 191) <= 0))) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L)))))), (byte) 191) <= 0)))) || ((((((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) == ((byte) 237)) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))), (byte) 159) <= 0))) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L)))))), (byte) 191) <= 0)))) || ((((java.lang.Integer.compareUnsigned((byte) 238, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), (byte) 239) <= 0)) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))), (byte) 191) <= 0))) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L)))))), (byte) 191) <= 0)));
  }
  public static boolean Uses4Bytes(dafny.DafnySequence<? extends java.lang.Byte> s) {
    return ((((((((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) == ((byte) 240)) && ((java.lang.Integer.compareUnsigned((byte) 144, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))), (byte) 191) <= 0))) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L)))))), (byte) 191) <= 0))) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(3L))))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(3L)))))), (byte) 191) <= 0))) || (((((java.lang.Integer.compareUnsigned((byte) 241, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), (byte) 243) <= 0)) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))), (byte) 191) <= 0))) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L)))))), (byte) 191) <= 0))) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(3L))))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(3L)))))), (byte) 191) <= 0)))) || (((((((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) == ((byte) 244)) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))), (byte) 143) <= 0))) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L)))))), (byte) 191) <= 0))) && ((java.lang.Integer.compareUnsigned((byte) 128, ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(3L))))))) <= 0) && (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(3L)))))), (byte) 191) <= 0)));
  }
  public static boolean ValidUTF8Range(dafny.DafnySequence<? extends java.lang.Byte> a, java.math.BigInteger lo, java.math.BigInteger hi)
  {
    TAIL_CALL_START: while (true) {
      if (java.util.Objects.equals(lo, hi)) {
        return true;
      } else {
        dafny.DafnySequence<? extends java.lang.Byte> _0_r = (a).subsequence(dafny.Helpers.toInt((lo)), dafny.Helpers.toInt((hi)));
        if (__default.Uses1Byte(_0_r)) {
          dafny.DafnySequence<? extends java.lang.Byte> _in0 = a;
          java.math.BigInteger _in1 = (lo).add(java.math.BigInteger.ONE);
          java.math.BigInteger _in2 = hi;
          a = _in0;
          lo = _in1;
          hi = _in2;
          continue TAIL_CALL_START;
        } else if (((java.math.BigInteger.valueOf(2L)).compareTo(java.math.BigInteger.valueOf((_0_r).length())) <= 0) && (__default.Uses2Bytes(_0_r))) {
          dafny.DafnySequence<? extends java.lang.Byte> _in3 = a;
          java.math.BigInteger _in4 = (lo).add(java.math.BigInteger.valueOf(2L));
          java.math.BigInteger _in5 = hi;
          a = _in3;
          lo = _in4;
          hi = _in5;
          continue TAIL_CALL_START;
        } else if (((java.math.BigInteger.valueOf(3L)).compareTo(java.math.BigInteger.valueOf((_0_r).length())) <= 0) && (__default.Uses3Bytes(_0_r))) {
          dafny.DafnySequence<? extends java.lang.Byte> _in6 = a;
          java.math.BigInteger _in7 = (lo).add(java.math.BigInteger.valueOf(3L));
          java.math.BigInteger _in8 = hi;
          a = _in6;
          lo = _in7;
          hi = _in8;
          continue TAIL_CALL_START;
        } else if (((java.math.BigInteger.valueOf(4L)).compareTo(java.math.BigInteger.valueOf((_0_r).length())) <= 0) && (__default.Uses4Bytes(_0_r))) {
          dafny.DafnySequence<? extends java.lang.Byte> _in9 = a;
          java.math.BigInteger _in10 = (lo).add(java.math.BigInteger.valueOf(4L));
          java.math.BigInteger _in11 = hi;
          a = _in9;
          lo = _in10;
          hi = _in11;
          continue TAIL_CALL_START;
        } else {
          return false;
        }
      }
    }
  }
  public static boolean ValidUTF8Seq(dafny.DafnySequence<? extends java.lang.Byte> s) {
    return __default.ValidUTF8Range(s, java.math.BigInteger.ZERO, java.math.BigInteger.valueOf((s).length()));
  }
  @Override
  public java.lang.String toString() {
    return "UTF8._default";
  }
}
