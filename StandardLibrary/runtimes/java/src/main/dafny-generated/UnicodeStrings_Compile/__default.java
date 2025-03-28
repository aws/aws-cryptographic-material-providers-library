// Class __default
// Dafny class __default compiled into Java
package UnicodeStrings_Compile;

import Wrappers_Compile.*;
import Seq_mMergeSort_Compile.*;
import Math_Compile.*;
import Seq_Compile.*;
import BoundedInts_Compile.*;
import Unicode_Compile.*;
import Utf8EncodingForm_Compile.*;
import Utf16EncodingForm_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean IsWellFormedString(dafny.DafnySequence<? extends Character> s) {
    return Utf16EncodingForm_Compile.__default.IsWellFormedCodeUnitSequence(Seq_Compile.__default.<Character, java.lang.Short>Map(dafny.TypeDescriptor.CHAR, dafny.TypeDescriptor.SHORT, ((java.util.function.Function<Character, java.lang.Short>)(_0_c_boxed0) -> {
      char _0_c = ((char)(java.lang.Object)(_0_c_boxed0));
      return ((short) (_0_c));
    }), s));
  }
  public static Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> ToUTF8Checked(dafny.DafnySequence<? extends Character> s) {
    dafny.DafnySequence<? extends java.lang.Short> _0_asCodeUnits = Seq_Compile.__default.<Character, java.lang.Short>Map(dafny.TypeDescriptor.CHAR, dafny.TypeDescriptor.SHORT, ((java.util.function.Function<Character, java.lang.Short>)(_1_c_boxed0) -> {
      char _1_c = ((char)(java.lang.Object)(_1_c_boxed0));
      return ((short) (_1_c));
    }), s);
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Integer>> _2_valueOrError0 = Utf16EncodingForm_Compile.__default.DecodeCodeUnitSequenceChecked(_0_asCodeUnits);
    if ((_2_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Integer>_typeDescriptor(Unicode_Compile.ScalarValue._typeDescriptor()))) {
      return (_2_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Integer>_typeDescriptor(Unicode_Compile.ScalarValue._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    } else {
      dafny.DafnySequence<? extends java.lang.Integer> _3_utf32 = (_2_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Integer>_typeDescriptor(Unicode_Compile.ScalarValue._typeDescriptor()));
      dafny.DafnySequence<? extends java.lang.Byte> _4_asUtf8CodeUnits = Utf8EncodingForm_Compile.__default.EncodeScalarSequence(_3_utf32);
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), Seq_Compile.__default.<java.lang.Byte, java.lang.Byte>Map(dafny.TypeDescriptor.BYTE, BoundedInts_Compile.uint8._typeDescriptor(), ((java.util.function.Function<java.lang.Byte, java.lang.Byte>)(_5_c_boxed0) -> {
  byte _5_c = ((byte)(java.lang.Object)(_5_c_boxed0));
  return (_5_c);
}), _4_asUtf8CodeUnits));
    }
  }
  public static Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FromUTF8Checked(dafny.DafnySequence<? extends java.lang.Byte> bs) {
    dafny.DafnySequence<? extends java.lang.Byte> _0_asCodeUnits = Seq_Compile.__default.<java.lang.Byte, java.lang.Byte>Map(BoundedInts_Compile.uint8._typeDescriptor(), dafny.TypeDescriptor.BYTE, ((java.util.function.Function<java.lang.Byte, java.lang.Byte>)(_1_c_boxed0) -> {
      byte _1_c = ((byte)(java.lang.Object)(_1_c_boxed0));
      return (_1_c);
    }), bs);
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Integer>> _2_valueOrError0 = Utf8EncodingForm_Compile.__default.DecodeCodeUnitSequenceChecked(_0_asCodeUnits);
    if ((_2_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Integer>_typeDescriptor(Unicode_Compile.ScalarValue._typeDescriptor()))) {
      return (_2_valueOrError0).<dafny.DafnySequence<? extends Character>>PropagateFailure(dafny.DafnySequence.<java.lang.Integer>_typeDescriptor(Unicode_Compile.ScalarValue._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    } else {
      dafny.DafnySequence<? extends java.lang.Integer> _3_utf32 = (_2_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Integer>_typeDescriptor(Unicode_Compile.ScalarValue._typeDescriptor()));
      dafny.DafnySequence<? extends java.lang.Short> _4_asUtf16CodeUnits = Utf16EncodingForm_Compile.__default.EncodeScalarSequence(_3_utf32);
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Seq_Compile.__default.<java.lang.Short, Character>Map(dafny.TypeDescriptor.SHORT, dafny.TypeDescriptor.CHAR, ((java.util.function.Function<java.lang.Short, Character>)(_5_cu_boxed0) -> {
  short _5_cu = ((short)(java.lang.Object)(_5_cu_boxed0));
  return (char)dafny.Helpers.unsignedToInt(_5_cu);
}), _4_asUtf16CodeUnits));
    }
  }
  public static Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Short>> ToUTF16Checked(dafny.DafnySequence<? extends Character> s) {
    if (Utf16EncodingForm_Compile.__default.IsWellFormedCodeUnitSequence(Seq_Compile.__default.<Character, java.lang.Short>Map(dafny.TypeDescriptor.CHAR, dafny.TypeDescriptor.SHORT, ((java.util.function.Function<Character, java.lang.Short>)(_0_c_boxed0) -> {
      char _0_c = ((char)(java.lang.Object)(_0_c_boxed0));
      return ((short) (_0_c));
    }), s))) {
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Short>>create_Some(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()), Seq_Compile.__default.<Character, java.lang.Short>Map(dafny.TypeDescriptor.CHAR, BoundedInts_Compile.uint16._typeDescriptor(), ((java.util.function.Function<Character, java.lang.Short>)(_1_c_boxed0) -> {
  char _1_c = ((char)(java.lang.Object)(_1_c_boxed0));
  return ((short) (_1_c));
}), s));
    } else {
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Short>>create_None(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(BoundedInts_Compile.uint16._typeDescriptor()));
    }
  }
  public static Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FromUTF16Checked(dafny.DafnySequence<? extends java.lang.Short> bs) {
    if (Utf16EncodingForm_Compile.__default.IsWellFormedCodeUnitSequence(Seq_Compile.__default.<java.lang.Short, java.lang.Short>Map(BoundedInts_Compile.uint16._typeDescriptor(), dafny.TypeDescriptor.SHORT, ((java.util.function.Function<java.lang.Short, java.lang.Short>)(_0_c_boxed0) -> {
      short _0_c = ((short)(java.lang.Object)(_0_c_boxed0));
      return (_0_c);
    }), bs))) {
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), Seq_Compile.__default.<java.lang.Short, Character>Map(BoundedInts_Compile.uint16._typeDescriptor(), dafny.TypeDescriptor.CHAR, ((java.util.function.Function<java.lang.Short, Character>)(_1_c_boxed0) -> {
  short _1_c = ((short)(java.lang.Object)(_1_c_boxed0));
  return (char)dafny.Helpers.unsignedToInt(_1_c);
}), bs));
    } else {
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ASCIIToUTF8(dafny.DafnySequence<? extends Character> s) {
    return Seq_Compile.__default.<Character, java.lang.Byte>Map(dafny.TypeDescriptor.CHAR, BoundedInts_Compile.uint8._typeDescriptor(), ((java.util.function.Function<Character, java.lang.Byte>)(_0_c_boxed0) -> {
      char _0_c = ((char)(java.lang.Object)(_0_c_boxed0));
      return ((byte) (_0_c));
    }), s);
  }
  public static dafny.DafnySequence<? extends java.lang.Short> ASCIIToUTF16(dafny.DafnySequence<? extends Character> s) {
    return Seq_Compile.__default.<Character, java.lang.Short>Map(dafny.TypeDescriptor.CHAR, BoundedInts_Compile.uint16._typeDescriptor(), ((java.util.function.Function<Character, java.lang.Short>)(_0_c_boxed0) -> {
      char _0_c = ((char)(java.lang.Object)(_0_c_boxed0));
      return ((short) (_0_c));
    }), s);
  }
  @Override
  public java.lang.String toString() {
    return "UnicodeStrings._default";
  }
}
