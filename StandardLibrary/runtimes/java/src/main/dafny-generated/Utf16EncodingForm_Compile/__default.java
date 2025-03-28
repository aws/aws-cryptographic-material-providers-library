// Class __default
// Dafny class __default compiled into Java
package Utf16EncodingForm_Compile;

import Wrappers_Compile.*;
import Seq_mMergeSort_Compile.*;
import Math_Compile.*;
import Seq_Compile.*;
import BoundedInts_Compile.*;
import Unicode_Compile.*;
import Utf8EncodingForm_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean IsMinimalWellFormedCodeUnitSubsequence(dafny.DafnySequence<? extends java.lang.Short> s) {
    if (java.util.Objects.equals(java.math.BigInteger.valueOf((s).length()), java.math.BigInteger.ONE)) {
      return __default.IsWellFormedSingleCodeUnitSequence(s);
    } else if (java.util.Objects.equals(java.math.BigInteger.valueOf((s).length()), java.math.BigInteger.valueOf(2L))) {
      boolean _0_b = __default.IsWellFormedDoubleCodeUnitSequence(s);
      return _0_b;
    } else {
      return false;
    }
  }
  public static boolean IsWellFormedSingleCodeUnitSequence(dafny.DafnySequence<? extends java.lang.Short> s) {
    short _0_firstWord = ((short)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    return ((((_0_firstWord) == 0 ? 0 : 1) != -1) && (java.lang.Integer.compareUnsigned(_0_firstWord, (short) 55295) <= 0)) || ((java.lang.Integer.compareUnsigned((short) 57344, _0_firstWord) <= 0) && (java.lang.Integer.compareUnsigned(_0_firstWord, (short) 65535) <= 0));
  }
  public static boolean IsWellFormedDoubleCodeUnitSequence(dafny.DafnySequence<? extends java.lang.Short> s) {
    short _0_firstWord = ((short)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    short _1_secondWord = ((short)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))));
    return ((java.lang.Integer.compareUnsigned((short) 55296, _0_firstWord) <= 0) && (java.lang.Integer.compareUnsigned(_0_firstWord, (short) 56319) <= 0)) && ((java.lang.Integer.compareUnsigned((short) 56320, _1_secondWord) <= 0) && (java.lang.Integer.compareUnsigned(_1_secondWord, (short) 57343) <= 0));
  }
  public static Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Short>> SplitPrefixMinimalWellFormedCodeUnitSubsequence(dafny.DafnySequence<? extends java.lang.Short> s) {
    if (((java.math.BigInteger.valueOf((s).length())).compareTo(java.math.BigInteger.ONE) >= 0) && (__default.IsWellFormedSingleCodeUnitSequence((s).take(java.math.BigInteger.ONE)))) {
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Short>>create_Some(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(dafny.TypeDescriptor.SHORT), (s).take(java.math.BigInteger.ONE));
    } else if (((java.math.BigInteger.valueOf((s).length())).compareTo(java.math.BigInteger.valueOf(2L)) >= 0) && (__default.IsWellFormedDoubleCodeUnitSequence((s).take(java.math.BigInteger.valueOf(2L))))) {
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Short>>create_Some(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(dafny.TypeDescriptor.SHORT), (s).take(java.math.BigInteger.valueOf(2L)));
    } else {
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Short>>create_None(dafny.DafnySequence.<java.lang.Short>_typeDescriptor(dafny.TypeDescriptor.SHORT));
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Short> EncodeScalarValue(int v) {
    if (((((v) == 0 ? 0 : 1) != -1) && (java.lang.Integer.compareUnsigned(v, 55295) <= 0)) || ((java.lang.Integer.compareUnsigned(57344, v) <= 0) && (java.lang.Integer.compareUnsigned(v, 65535) <= 0))) {
      return __default.EncodeScalarValueSingleWord(v);
    } else {
      return __default.EncodeScalarValueDoubleWord(v);
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Short> EncodeScalarValueSingleWord(int v) {
    short _0_firstWord = ((short) (v));
    return dafny.DafnySequence.<java.lang.Short> of(_0_firstWord);
  }
  public static dafny.DafnySequence<? extends java.lang.Short> EncodeScalarValueDoubleWord(int v) {
    short _0_x2 = ((short) ((int) ((v) & (1023))));
    byte _1_x1 = ((byte) ((int) (((int) ((v) & (64512))) >>> ((byte) 10))));
    byte _2_u = ((byte) ((int) (((int) ((v) & (2031616))) >>> ((byte) 16))));
    byte _3_w = ((byte) (byte) (((byte) (byte) ((byte)((_2_u) - ((byte) 1)))) & (byte) 0x1F));
    short _4_firstWord = (short) (short) ((short)(((short) (short) ((short)(((short) 55296) | ((short) (short) (((short) (short) ((short)(((short) java.lang.Byte.toUnsignedInt(_3_w)) << ((byte) 6))))))))) | ((short) java.lang.Byte.toUnsignedInt(_1_x1))));
    short _5_secondWord = (short) (short) ((short)(((short) 56320) | ((_0_x2))));
    return dafny.DafnySequence.<java.lang.Short> of(_4_firstWord, _5_secondWord);
  }
  public static int DecodeMinimalWellFormedCodeUnitSubsequence(dafny.DafnySequence<? extends java.lang.Short> m) {
    if (java.util.Objects.equals(java.math.BigInteger.valueOf((m).length()), java.math.BigInteger.ONE)) {
      return __default.DecodeMinimalWellFormedCodeUnitSubsequenceSingleWord(m);
    } else {
      return __default.DecodeMinimalWellFormedCodeUnitSubsequenceDoubleWord(m);
    }
  }
  public static int DecodeMinimalWellFormedCodeUnitSubsequenceSingleWord(dafny.DafnySequence<? extends java.lang.Short> m) {
    short _0_firstWord = ((short)(java.lang.Object)((m).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    short _1_x = _0_firstWord;
    return java.lang.Short.toUnsignedInt(_1_x);
  }
  public static int DecodeMinimalWellFormedCodeUnitSubsequenceDoubleWord(dafny.DafnySequence<? extends java.lang.Short> m) {
    short _0_firstWord = ((short)(java.lang.Object)((m).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    short _1_secondWord = ((short)(java.lang.Object)((m).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))));
    int _2_x2 = java.lang.Short.toUnsignedInt((short) (short) ((short)((_1_secondWord) & ((short) 1023))));
    int _3_x1 = java.lang.Short.toUnsignedInt((short) (short) ((short)((_0_firstWord) & ((short) 63))));
    int _4_w = java.lang.Short.toUnsignedInt((short) dafny.Helpers.bv16ShiftRight((short) (short) ((short)((_0_firstWord) & ((short) 960))), (byte) 6));
    int _5_u = (int) (((int) ((_4_w) + (1))) & 0xFFFFFF);
    int _6_v = (int) (((int) (((int) (((int) ((_5_u) << ((byte) 16))) & 0xFFFFFF)) | ((int) (((int) ((_3_x1) << ((byte) 10))) & 0xFFFFFF)))) | ((_2_x2)));
    return _6_v;
  }
  public static Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Short>>> PartitionCodeUnitSequenceChecked(dafny.DafnySequence<? extends java.lang.Short> s)
  {
    Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Short>>> maybeParts = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Short>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Short>>_typeDescriptor(MinimalWellFormedCodeUnitSeq._typeDescriptor()));
    if ((s).equals(dafny.DafnySequence.<java.lang.Short> empty(dafny.TypeDescriptor.SHORT))) {
      maybeParts = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Short>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Short>>_typeDescriptor(MinimalWellFormedCodeUnitSeq._typeDescriptor()), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Short>> empty(MinimalWellFormedCodeUnitSeq._typeDescriptor()));
      return maybeParts;
    }
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Short>> _0_result;
    _0_result = dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Short>> empty(MinimalWellFormedCodeUnitSeq._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Short> _1_rest;
    _1_rest = s;
    while ((java.math.BigInteger.valueOf((_1_rest).length())).signum() == 1) {
      Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Short>> _2_valueOrError0 = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Short>>Default(MinimalWellFormedCodeUnitSeq._typeDescriptor());
      _2_valueOrError0 = __default.SplitPrefixMinimalWellFormedCodeUnitSubsequence(_1_rest);
      if ((_2_valueOrError0).IsFailure(MinimalWellFormedCodeUnitSeq._typeDescriptor())) {
        maybeParts = (_2_valueOrError0).<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Short>>>PropagateFailure(MinimalWellFormedCodeUnitSeq._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Short>>_typeDescriptor(MinimalWellFormedCodeUnitSeq._typeDescriptor()));
        return maybeParts;
      }
      dafny.DafnySequence<? extends java.lang.Short> _3_prefix;
      _3_prefix = (_2_valueOrError0).Extract(MinimalWellFormedCodeUnitSeq._typeDescriptor());
      _0_result = dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Short>>concatenate(_0_result, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Short>> of(MinimalWellFormedCodeUnitSeq._typeDescriptor(), _3_prefix));
      _1_rest = (_1_rest).drop(java.math.BigInteger.valueOf((_3_prefix).length()));
    }
    maybeParts = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Short>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Short>>_typeDescriptor(MinimalWellFormedCodeUnitSeq._typeDescriptor()), _0_result);
    return maybeParts;
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Short>> PartitionCodeUnitSequence(dafny.DafnySequence<? extends java.lang.Short> s) {
    return (__default.PartitionCodeUnitSequenceChecked(s)).Extract(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Short>>_typeDescriptor(MinimalWellFormedCodeUnitSeq._typeDescriptor()));
  }
  public static boolean IsWellFormedCodeUnitSequence(dafny.DafnySequence<? extends java.lang.Short> s) {
    return (__default.PartitionCodeUnitSequenceChecked(s)).is_Some();
  }
  public static dafny.DafnySequence<? extends java.lang.Short> EncodeScalarSequence(dafny.DafnySequence<? extends java.lang.Integer> vs)
  {
    dafny.DafnySequence<? extends java.lang.Short> s = WellFormedCodeUnitSeq.defaultValue();
    if(true) {
      s = dafny.DafnySequence.<java.lang.Short> empty(dafny.TypeDescriptor.SHORT);
      java.math.BigInteger _lo0 = java.math.BigInteger.ZERO;
      for (java.math.BigInteger _0_i = java.math.BigInteger.valueOf((vs).length()); _lo0.compareTo(_0_i) < 0; ) {
        _0_i = _0_i.subtract(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends java.lang.Short> _1_next;
        _1_next = __default.EncodeScalarValue(((int)(java.lang.Object)((vs).select(dafny.Helpers.toInt((_0_i))))));
        s = dafny.DafnySequence.<java.lang.Short>concatenate(_1_next, s);
      }
    }
    return s;
  }
  public static dafny.DafnySequence<? extends java.lang.Integer> DecodeCodeUnitSequence(dafny.DafnySequence<? extends java.lang.Short> s) {
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Short>> _0_parts = __default.PartitionCodeUnitSequence(s);
    dafny.DafnySequence<? extends java.lang.Integer> _1_vs = Seq_Compile.__default.<dafny.DafnySequence<? extends java.lang.Short>, java.lang.Integer>Map(MinimalWellFormedCodeUnitSeq._typeDescriptor(), Unicode_Compile.ScalarValue._typeDescriptor(), __default::DecodeMinimalWellFormedCodeUnitSubsequence, _0_parts);
    return _1_vs;
  }
  public static Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Integer>> DecodeCodeUnitSequenceChecked(dafny.DafnySequence<? extends java.lang.Short> s)
  {
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Integer>> maybeVs = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Integer>>Default(dafny.DafnySequence.<java.lang.Integer>_typeDescriptor(Unicode_Compile.ScalarValue._typeDescriptor()));
    Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Short>>> _0_maybeParts;
    _0_maybeParts = __default.PartitionCodeUnitSequenceChecked(s);
    if ((_0_maybeParts).is_None()) {
      maybeVs = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Integer>>create_None(dafny.DafnySequence.<java.lang.Integer>_typeDescriptor(Unicode_Compile.ScalarValue._typeDescriptor()));
      return maybeVs;
    }
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Short>> _1_parts;
    _1_parts = (_0_maybeParts).dtor_value();
    dafny.DafnySequence<? extends java.lang.Integer> _2_vs;
    _2_vs = Seq_Compile.__default.<dafny.DafnySequence<? extends java.lang.Short>, java.lang.Integer>Map(MinimalWellFormedCodeUnitSeq._typeDescriptor(), Unicode_Compile.ScalarValue._typeDescriptor(), __default::DecodeMinimalWellFormedCodeUnitSubsequence, _1_parts);
    maybeVs = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Integer>>create_Some(dafny.DafnySequence.<java.lang.Integer>_typeDescriptor(Unicode_Compile.ScalarValue._typeDescriptor()), _2_vs);
    return maybeVs;
  }
  @Override
  public java.lang.String toString() {
    return "Utf16EncodingForm._default";
  }
}
