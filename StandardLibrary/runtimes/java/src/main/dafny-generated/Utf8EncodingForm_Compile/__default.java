// Class __default
// Dafny class __default compiled into Java
package Utf8EncodingForm_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean IsMinimalWellFormedCodeUnitSubsequence(dafny.DafnySequence<? extends java.lang.Byte> s) {
    if (java.util.Objects.equals(java.math.BigInteger.valueOf((s).length()), java.math.BigInteger.ONE)) {
      boolean _0_b = __default.IsWellFormedSingleCodeUnitSequence(s);
      return _0_b;
    } else if (java.util.Objects.equals(java.math.BigInteger.valueOf((s).length()), java.math.BigInteger.valueOf(2L))) {
      boolean _1_b = __default.IsWellFormedDoubleCodeUnitSequence(s);
      return _1_b;
    } else if (java.util.Objects.equals(java.math.BigInteger.valueOf((s).length()), java.math.BigInteger.valueOf(3L))) {
      boolean _2_b = __default.IsWellFormedTripleCodeUnitSequence(s);
      return _2_b;
    } else if (java.util.Objects.equals(java.math.BigInteger.valueOf((s).length()), java.math.BigInteger.valueOf(4L))) {
      boolean _3_b = __default.IsWellFormedQuadrupleCodeUnitSequence(s);
      return _3_b;
    } else {
      return false;
    }
  }
  public static boolean IsWellFormedSingleCodeUnitSequence(dafny.DafnySequence<? extends java.lang.Byte> s) {
    byte _0_firstByte = ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    return (true) && ((((_0_firstByte) == 0 ? 0 : 1) != -1) && (java.lang.Integer.compareUnsigned(_0_firstByte, (byte) 127) <= 0));
  }
  public static boolean IsWellFormedDoubleCodeUnitSequence(dafny.DafnySequence<? extends java.lang.Byte> s) {
    byte _0_firstByte = ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    byte _1_secondByte = ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))));
    return ((java.lang.Integer.compareUnsigned((byte) 194, _0_firstByte) <= 0) && (java.lang.Integer.compareUnsigned(_0_firstByte, (byte) 223) <= 0)) && ((java.lang.Integer.compareUnsigned((byte) 128, _1_secondByte) <= 0) && (java.lang.Integer.compareUnsigned(_1_secondByte, (byte) 191) <= 0));
  }
  public static boolean IsWellFormedTripleCodeUnitSequence(dafny.DafnySequence<? extends java.lang.Byte> s) {
    byte _0_firstByte = ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    byte _1_secondByte = ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))));
    byte _2_thirdByte = ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))));
    return ((((((_0_firstByte) == ((byte) 224)) && ((java.lang.Integer.compareUnsigned((byte) 160, _1_secondByte) <= 0) && (java.lang.Integer.compareUnsigned(_1_secondByte, (byte) 191) <= 0))) || (((java.lang.Integer.compareUnsigned((byte) 225, _0_firstByte) <= 0) && (java.lang.Integer.compareUnsigned(_0_firstByte, (byte) 236) <= 0)) && ((java.lang.Integer.compareUnsigned((byte) 128, _1_secondByte) <= 0) && (java.lang.Integer.compareUnsigned(_1_secondByte, (byte) 191) <= 0)))) || (((_0_firstByte) == ((byte) 237)) && ((java.lang.Integer.compareUnsigned((byte) 128, _1_secondByte) <= 0) && (java.lang.Integer.compareUnsigned(_1_secondByte, (byte) 159) <= 0)))) || (((java.lang.Integer.compareUnsigned((byte) 238, _0_firstByte) <= 0) && (java.lang.Integer.compareUnsigned(_0_firstByte, (byte) 239) <= 0)) && ((java.lang.Integer.compareUnsigned((byte) 128, _1_secondByte) <= 0) && (java.lang.Integer.compareUnsigned(_1_secondByte, (byte) 191) <= 0)))) && ((java.lang.Integer.compareUnsigned((byte) 128, _2_thirdByte) <= 0) && (java.lang.Integer.compareUnsigned(_2_thirdByte, (byte) 191) <= 0));
  }
  public static boolean IsWellFormedQuadrupleCodeUnitSequence(dafny.DafnySequence<? extends java.lang.Byte> s) {
    byte _0_firstByte = ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    byte _1_secondByte = ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))));
    byte _2_thirdByte = ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))));
    byte _3_fourthByte = ((byte)(java.lang.Object)((s).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(3L))))));
    return ((((((_0_firstByte) == ((byte) 240)) && ((java.lang.Integer.compareUnsigned((byte) 144, _1_secondByte) <= 0) && (java.lang.Integer.compareUnsigned(_1_secondByte, (byte) 191) <= 0))) || (((java.lang.Integer.compareUnsigned((byte) 241, _0_firstByte) <= 0) && (java.lang.Integer.compareUnsigned(_0_firstByte, (byte) 243) <= 0)) && ((java.lang.Integer.compareUnsigned((byte) 128, _1_secondByte) <= 0) && (java.lang.Integer.compareUnsigned(_1_secondByte, (byte) 191) <= 0)))) || (((_0_firstByte) == ((byte) 244)) && ((java.lang.Integer.compareUnsigned((byte) 128, _1_secondByte) <= 0) && (java.lang.Integer.compareUnsigned(_1_secondByte, (byte) 143) <= 0)))) && ((java.lang.Integer.compareUnsigned((byte) 128, _2_thirdByte) <= 0) && (java.lang.Integer.compareUnsigned(_2_thirdByte, (byte) 191) <= 0))) && ((java.lang.Integer.compareUnsigned((byte) 128, _3_fourthByte) <= 0) && (java.lang.Integer.compareUnsigned(_3_fourthByte, (byte) 191) <= 0));
  }
  public static Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> SplitPrefixMinimalWellFormedCodeUnitSubsequence(dafny.DafnySequence<? extends java.lang.Byte> s) {
    if (((java.math.BigInteger.valueOf((s).length())).compareTo(java.math.BigInteger.ONE) >= 0) && (__default.IsWellFormedSingleCodeUnitSequence((s).take(java.math.BigInteger.ONE)))) {
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(dafny.TypeDescriptor.BYTE), (s).take(java.math.BigInteger.ONE));
    } else if (((java.math.BigInteger.valueOf((s).length())).compareTo(java.math.BigInteger.valueOf(2L)) >= 0) && (__default.IsWellFormedDoubleCodeUnitSequence((s).take(java.math.BigInteger.valueOf(2L))))) {
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(dafny.TypeDescriptor.BYTE), (s).take(java.math.BigInteger.valueOf(2L)));
    } else if (((java.math.BigInteger.valueOf((s).length())).compareTo(java.math.BigInteger.valueOf(3L)) >= 0) && (__default.IsWellFormedTripleCodeUnitSequence((s).take(java.math.BigInteger.valueOf(3L))))) {
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(dafny.TypeDescriptor.BYTE), (s).take(java.math.BigInteger.valueOf(3L)));
    } else if (((java.math.BigInteger.valueOf((s).length())).compareTo(java.math.BigInteger.valueOf(4L)) >= 0) && (__default.IsWellFormedQuadrupleCodeUnitSequence((s).take(java.math.BigInteger.valueOf(4L))))) {
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(dafny.TypeDescriptor.BYTE), (s).take(java.math.BigInteger.valueOf(4L)));
    } else {
      return Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(dafny.TypeDescriptor.BYTE));
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> EncodeScalarValue(int v) {
    if (java.lang.Integer.compareUnsigned(v, 127) <= 0) {
      return __default.EncodeScalarValueSingleByte(v);
    } else if (java.lang.Integer.compareUnsigned(v, 2047) <= 0) {
      return __default.EncodeScalarValueDoubleByte(v);
    } else if (java.lang.Integer.compareUnsigned(v, 65535) <= 0) {
      return __default.EncodeScalarValueTripleByte(v);
    } else {
      return __default.EncodeScalarValueQuadrupleByte(v);
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> EncodeScalarValueSingleByte(int v) {
    byte _0_x = ((byte) ((int) ((v) & (127))));
    byte _1_firstByte = (_0_x);
    return dafny.DafnySequence.<java.lang.Byte> of(_1_firstByte);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> EncodeScalarValueDoubleByte(int v) {
    byte _0_x = ((byte) ((int) ((v) & (63))));
    byte _1_y = ((byte) ((int) (((int) ((v) & (1984))) >>> ((byte) 6))));
    byte _2_firstByte = (byte) (byte) ((byte)(((byte) 192) | ((_1_y))));
    byte _3_secondByte = (byte) (byte) ((byte)(((byte) 128) | ((_0_x))));
    return dafny.DafnySequence.<java.lang.Byte> of(_2_firstByte, _3_secondByte);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> EncodeScalarValueTripleByte(int v) {
    byte _0_x = ((byte) ((int) ((v) & (63))));
    byte _1_y = ((byte) ((int) (((int) ((v) & (4032))) >>> ((byte) 6))));
    byte _2_z = ((byte) ((int) (((int) ((v) & (61440))) >>> ((byte) 12))));
    byte _3_firstByte = (byte) (byte) ((byte)(((byte) 224) | ((_2_z))));
    byte _4_secondByte = (byte) (byte) ((byte)(((byte) 128) | ((_1_y))));
    byte _5_thirdByte = (byte) (byte) ((byte)(((byte) 128) | ((_0_x))));
    return dafny.DafnySequence.<java.lang.Byte> of(_3_firstByte, _4_secondByte, _5_thirdByte);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> EncodeScalarValueQuadrupleByte(int v) {
    byte _0_x = ((byte) ((int) ((v) & (63))));
    byte _1_y = ((byte) ((int) (((int) ((v) & (4032))) >>> ((byte) 6))));
    byte _2_z = ((byte) ((int) (((int) ((v) & (61440))) >>> ((byte) 12))));
    byte _3_u2 = ((byte) ((int) (((int) ((v) & (196608))) >>> ((byte) 16))));
    byte _4_u1 = ((byte) ((int) (((int) ((v) & (1835008))) >>> ((byte) 18))));
    byte _5_firstByte = (byte) (byte) ((byte)(((byte) 240) | ((_4_u1))));
    byte _6_secondByte = (byte) (byte) ((byte)(((byte) (byte) ((byte)(((byte) 128) | ((byte) (byte) (((byte) (byte) ((byte)(((_3_u2)) << ((byte) 4))))))))) | ((_2_z))));
    byte _7_thirdByte = (byte) (byte) ((byte)(((byte) 128) | ((_1_y))));
    byte _8_fourthByte = (byte) (byte) ((byte)(((byte) 128) | ((_0_x))));
    return dafny.DafnySequence.<java.lang.Byte> of(_5_firstByte, _6_secondByte, _7_thirdByte, _8_fourthByte);
  }
  public static int DecodeMinimalWellFormedCodeUnitSubsequence(dafny.DafnySequence<? extends java.lang.Byte> m) {
    if (java.util.Objects.equals(java.math.BigInteger.valueOf((m).length()), java.math.BigInteger.ONE)) {
      return __default.DecodeMinimalWellFormedCodeUnitSubsequenceSingleByte(m);
    } else if (java.util.Objects.equals(java.math.BigInteger.valueOf((m).length()), java.math.BigInteger.valueOf(2L))) {
      return __default.DecodeMinimalWellFormedCodeUnitSubsequenceDoubleByte(m);
    } else if (java.util.Objects.equals(java.math.BigInteger.valueOf((m).length()), java.math.BigInteger.valueOf(3L))) {
      return __default.DecodeMinimalWellFormedCodeUnitSubsequenceTripleByte(m);
    } else {
      return __default.DecodeMinimalWellFormedCodeUnitSubsequenceQuadrupleByte(m);
    }
  }
  public static int DecodeMinimalWellFormedCodeUnitSubsequenceSingleByte(dafny.DafnySequence<? extends java.lang.Byte> m) {
    byte _0_firstByte = ((byte)(java.lang.Object)((m).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    byte _1_x = (_0_firstByte);
    return java.lang.Byte.toUnsignedInt(_1_x);
  }
  public static int DecodeMinimalWellFormedCodeUnitSubsequenceDoubleByte(dafny.DafnySequence<? extends java.lang.Byte> m) {
    byte _0_firstByte = ((byte)(java.lang.Object)((m).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    byte _1_secondByte = ((byte)(java.lang.Object)((m).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))));
    int _2_y = java.lang.Byte.toUnsignedInt((byte) (byte) ((byte)((_0_firstByte) & ((byte) 31))));
    int _3_x = java.lang.Byte.toUnsignedInt((byte) (byte) ((byte)((_1_secondByte) & ((byte) 63))));
    return (int) (((int) (((int) ((_2_y) << ((byte) 6))) & 0xFFFFFF)) | ((_3_x)));
  }
  public static int DecodeMinimalWellFormedCodeUnitSubsequenceTripleByte(dafny.DafnySequence<? extends java.lang.Byte> m) {
    byte _0_firstByte = ((byte)(java.lang.Object)((m).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    byte _1_secondByte = ((byte)(java.lang.Object)((m).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))));
    byte _2_thirdByte = ((byte)(java.lang.Object)((m).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))));
    int _3_z = java.lang.Byte.toUnsignedInt((byte) (byte) ((byte)((_0_firstByte) & ((byte) 15))));
    int _4_y = java.lang.Byte.toUnsignedInt((byte) (byte) ((byte)((_1_secondByte) & ((byte) 63))));
    int _5_x = java.lang.Byte.toUnsignedInt((byte) (byte) ((byte)((_2_thirdByte) & ((byte) 63))));
    return (int) (((int) (((int) (((int) ((_3_z) << ((byte) 12))) & 0xFFFFFF)) | ((int) (((int) ((_4_y) << ((byte) 6))) & 0xFFFFFF)))) | ((_5_x)));
  }
  public static int DecodeMinimalWellFormedCodeUnitSubsequenceQuadrupleByte(dafny.DafnySequence<? extends java.lang.Byte> m) {
    byte _0_firstByte = ((byte)(java.lang.Object)((m).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))));
    byte _1_secondByte = ((byte)(java.lang.Object)((m).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))));
    byte _2_thirdByte = ((byte)(java.lang.Object)((m).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))));
    byte _3_fourthByte = ((byte)(java.lang.Object)((m).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(3L))))));
    int _4_u1 = java.lang.Byte.toUnsignedInt((byte) (byte) ((byte)((_0_firstByte) & ((byte) 7))));
    int _5_u2 = java.lang.Byte.toUnsignedInt((byte) dafny.Helpers.bv8ShiftRight((byte) (byte) ((byte)((_1_secondByte) & ((byte) 48))), (byte) 4));
    int _6_z = java.lang.Byte.toUnsignedInt((byte) (byte) ((byte)((_1_secondByte) & ((byte) 15))));
    int _7_y = java.lang.Byte.toUnsignedInt((byte) (byte) ((byte)((_2_thirdByte) & ((byte) 63))));
    int _8_x = java.lang.Byte.toUnsignedInt((byte) (byte) ((byte)((_3_fourthByte) & ((byte) 63))));
    return (int) (((int) (((int) (((int) (((int) (((int) ((_4_u1) << ((byte) 18))) & 0xFFFFFF)) | ((int) (((int) ((_5_u2) << ((byte) 16))) & 0xFFFFFF)))) | ((int) (((int) ((_6_z) << ((byte) 12))) & 0xFFFFFF)))) | ((int) (((int) ((_7_y) << ((byte) 6))) & 0xFFFFFF)))) | ((_8_x)));
  }
  public static Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> PartitionCodeUnitSequenceChecked(dafny.DafnySequence<? extends java.lang.Byte> s)
  {
    Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> maybeParts = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(MinimalWellFormedCodeUnitSeq._typeDescriptor()));
    if ((s).equals(dafny.DafnySequence.<java.lang.Byte> empty(dafny.TypeDescriptor.BYTE))) {
      maybeParts = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(MinimalWellFormedCodeUnitSeq._typeDescriptor()), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(MinimalWellFormedCodeUnitSeq._typeDescriptor()));
      return maybeParts;
    }
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _0_result;
    _0_result = dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> empty(MinimalWellFormedCodeUnitSeq._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _1_rest;
    _1_rest = s;
    while ((java.math.BigInteger.valueOf((_1_rest).length())).signum() == 1) {
      Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _2_valueOrError0 = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(MinimalWellFormedCodeUnitSeq._typeDescriptor());
      _2_valueOrError0 = __default.SplitPrefixMinimalWellFormedCodeUnitSubsequence(_1_rest);
      if ((_2_valueOrError0).IsFailure(MinimalWellFormedCodeUnitSeq._typeDescriptor())) {
        maybeParts = (_2_valueOrError0).<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>PropagateFailure(MinimalWellFormedCodeUnitSeq._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(MinimalWellFormedCodeUnitSeq._typeDescriptor()));
        return maybeParts;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _3_prefix;
      _3_prefix = (_2_valueOrError0).Extract(MinimalWellFormedCodeUnitSeq._typeDescriptor());
      _0_result = dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>concatenate(_0_result, dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> of(MinimalWellFormedCodeUnitSeq._typeDescriptor(), _3_prefix));
      _1_rest = (_1_rest).drop(java.math.BigInteger.valueOf((_3_prefix).length()));
    }
    maybeParts = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(MinimalWellFormedCodeUnitSeq._typeDescriptor()), _0_result);
    return maybeParts;
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> PartitionCodeUnitSequence(dafny.DafnySequence<? extends java.lang.Byte> s) {
    return (__default.PartitionCodeUnitSequenceChecked(s)).Extract(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(MinimalWellFormedCodeUnitSeq._typeDescriptor()));
  }
  public static boolean IsWellFormedCodeUnitSequence(dafny.DafnySequence<? extends java.lang.Byte> s) {
    return (__default.PartitionCodeUnitSequenceChecked(s)).is_Some();
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> EncodeScalarSequence(dafny.DafnySequence<? extends java.lang.Integer> vs)
  {
    dafny.DafnySequence<? extends java.lang.Byte> s = WellFormedCodeUnitSeq.defaultValue();
    if(true) {
      s = dafny.DafnySequence.<java.lang.Byte> empty(dafny.TypeDescriptor.BYTE);
      java.math.BigInteger _lo0 = java.math.BigInteger.ZERO;
      for (java.math.BigInteger _0_i = java.math.BigInteger.valueOf((vs).length()); _lo0.compareTo(_0_i) < 0; ) {
        _0_i = _0_i.subtract(java.math.BigInteger.ONE);
        dafny.DafnySequence<? extends java.lang.Byte> _1_next;
        _1_next = __default.EncodeScalarValue(((int)(java.lang.Object)((vs).select(dafny.Helpers.toInt((_0_i))))));
        s = dafny.DafnySequence.<java.lang.Byte>concatenate(_1_next, s);
      }
    }
    return s;
  }
  public static dafny.DafnySequence<? extends java.lang.Integer> DecodeCodeUnitSequence(dafny.DafnySequence<? extends java.lang.Byte> s) {
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _0_parts = __default.PartitionCodeUnitSequence(s);
    dafny.DafnySequence<? extends java.lang.Integer> _1_vs = Seq_Compile.__default.<dafny.DafnySequence<? extends java.lang.Byte>, java.lang.Integer>Map(MinimalWellFormedCodeUnitSeq._typeDescriptor(), Unicode_Compile.ScalarValue._typeDescriptor(), __default::DecodeMinimalWellFormedCodeUnitSubsequence, _0_parts);
    return _1_vs;
  }
  public static Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Integer>> DecodeCodeUnitSequenceChecked(dafny.DafnySequence<? extends java.lang.Byte> s)
  {
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Integer>> maybeVs = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Integer>>Default(dafny.DafnySequence.<java.lang.Integer>_typeDescriptor(Unicode_Compile.ScalarValue._typeDescriptor()));
    Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _0_maybeParts;
    _0_maybeParts = __default.PartitionCodeUnitSequenceChecked(s);
    if ((_0_maybeParts).is_None()) {
      maybeVs = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Integer>>create_None(dafny.DafnySequence.<java.lang.Integer>_typeDescriptor(Unicode_Compile.ScalarValue._typeDescriptor()));
      return maybeVs;
    }
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _1_parts;
    _1_parts = (_0_maybeParts).dtor_value();
    dafny.DafnySequence<? extends java.lang.Integer> _2_vs;
    _2_vs = Seq_Compile.__default.<dafny.DafnySequence<? extends java.lang.Byte>, java.lang.Integer>Map(MinimalWellFormedCodeUnitSeq._typeDescriptor(), Unicode_Compile.ScalarValue._typeDescriptor(), __default::DecodeMinimalWellFormedCodeUnitSubsequence, _1_parts);
    maybeVs = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Integer>>create_Some(dafny.DafnySequence.<java.lang.Integer>_typeDescriptor(Unicode_Compile.ScalarValue._typeDescriptor()), _2_vs);
    return maybeVs;
  }
  @Override
  public java.lang.String toString() {
    return "Utf8EncodingForm._default";
  }
}
