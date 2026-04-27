// Class __default
// Dafny class __default compiled into Java
package Base64_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean IsBase64Char(char c) {
    return (((((c) == ('+')) || ((c) == ('/'))) || ((('0') <= (c)) && ((c) <= ('9')))) || ((('A') <= (c)) && ((c) <= ('Z')))) || ((('a') <= (c)) && ((c) <= ('z')));
  }
  public static boolean IsUnpaddedBase64String(dafny.DafnySequence<? extends Character> s)
  {
    boolean _hresult = false;
    long _0_size;
    _0_size = (long) (s).cardinalityInt();
    if ((((long) java.lang.Long.remainderUnsigned(_0_size, (long) 4L)) == 0 ? 0 : 1) != 0) {
      _hresult = false;
      return _hresult;
    }
    long _hi0 = _0_size;
    for (long _1_i = (long) 0L; java.lang.Long.compareUnsigned(_1_i, _hi0) < 0; _1_i++) {
      if (!(__default.IsBase64Char(((char)(java.lang.Object)((s).select(dafny.Helpers.unsignedToInt(_1_i))))))) {
        _hresult = false;
        return _hresult;
      }
    }
    _hresult = true;
    return _hresult;
  }
  public static char IndexToChar(byte i) {
    if ((i) == ((byte) 63)) {
      return '/';
    } else if ((i) == ((byte) 62)) {
      return '+';
    } else if ((java.lang.Integer.compareUnsigned((byte) 52, i) <= 0) && (java.lang.Integer.compareUnsigned(i, (byte) 61) <= 0)) {
      return (char)java.lang.Byte.toUnsignedInt((byte) (byte) ((byte)((i) - ((byte) 4))));
    } else if ((java.lang.Integer.compareUnsigned((byte) 26, i) <= 0) && (java.lang.Integer.compareUnsigned(i, (byte) 51) <= 0)) {
      return (char)java.lang.Byte.toUnsignedInt((byte) (byte) ((byte)(((i)) + ((byte) 71))));
    } else {
      return (char)java.lang.Byte.toUnsignedInt((byte) (byte) ((byte)(((i)) + ((byte) 65))));
    }
  }
  public static byte CharToIndex(char c) {
    if ((c) == ('/')) {
      return (byte) 63;
    } else if ((c) == ('+')) {
      return (byte) 62;
    } else if ((('0') <= (c)) && ((c) <= ('9'))) {
      return ((byte) (byte) ((byte)((((byte) (c))) + ((byte) 4))));
    } else if ((('a') <= (c)) && ((c) <= ('z'))) {
      return ((byte) (byte) ((byte)((((byte) (c))) - ((byte) 71))));
    } else {
      return ((byte) (byte) ((byte)((((byte) (c))) - ((byte) 65))));
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
    return (int) (((int) (((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(0))))) * (65536))) + ((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(1))))) * (256))))) + (java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(2))))));
  }
  public static int SeqPosToUInt24(dafny.DafnySequence<? extends java.lang.Byte> s, long pos)
  {
    return (int) (((int) (((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.unsignedToInt(pos)))))) * (65536))) + ((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.unsignedToInt((long) (long) ((pos) + ((long) 1L)))))))) * (256))))) + (java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.unsignedToInt((long) (long) ((pos) + ((long) 2L)))))))));
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
    return (int) (((int) (((int) (((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(0))))) * (262144))) + ((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(1))))) * (4096))))) + ((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(2))))) * (64))))) + (java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(3))))));
  }
  public static int IndexSeqPosToUInt24(dafny.DafnySequence<? extends java.lang.Byte> s, long pos)
  {
    return (int) (((int) (((int) (((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.unsignedToInt(pos)))))) * (262144))) + ((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.unsignedToInt((long) (long) ((pos) + ((long) 1L)))))))) * (4096))))) + ((int) ((java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.unsignedToInt((long) (long) ((pos) + ((long) 2L)))))))) * (64))))) + (java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((s).select(dafny.Helpers.unsignedToInt((long) (long) ((pos) + ((long) 3L)))))))));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> DecodeBlock(dafny.DafnySequence<? extends java.lang.Byte> s) {
    return __default.UInt24ToSeq(__default.IndexSeqToUInt24(s));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> DecodeBlockPos(dafny.DafnySequence<? extends java.lang.Byte> s, long pos)
  {
    return __default.UInt24ToSeq(__default.IndexSeqPosToUInt24(s, pos));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> EncodeBlock(dafny.DafnySequence<? extends java.lang.Byte> s) {
    return __default.UInt24ToIndexSeq(__default.SeqToUInt24(s));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> EncodeBlockPos(dafny.DafnySequence<? extends java.lang.Byte> s, long pos)
  {
    return __default.UInt24ToIndexSeq(__default.SeqPosToUInt24(s, pos));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> DecodeRecursively(dafny.DafnySequence<? extends java.lang.Byte> s)
  {
    dafny.DafnySequence<? extends java.lang.Byte> b = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    long _0_i;
    _0_i = (long) (s).cardinalityInt();
    dafny.DafnySequence<? extends java.lang.Byte> _1_result;
    _1_result = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    while (((_0_i) == 0 ? 0 : 1) == 1) {
      _1_result = dafny.DafnySequence.<java.lang.Byte>concatenate(__default.DecodeBlockPos(s, (long) (long) ((_0_i) - ((long) 4L))), _1_result);
      _0_i = (long) (long) ((_0_i) - ((long) 4L));
    }
    b = _1_result;
    return b;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> EncodeRecursively(dafny.DafnySequence<? extends java.lang.Byte> b)
  {
    dafny.DafnySequence<? extends java.lang.Byte> s = dafny.DafnySequence.<java.lang.Byte> empty(index._typeDescriptor());
    long _0_i;
    _0_i = (long) (b).cardinalityInt();
    dafny.DafnySequence<? extends java.lang.Byte> _1_result;
    _1_result = dafny.DafnySequence.<java.lang.Byte> empty(index._typeDescriptor());
    while (((_0_i) == 0 ? 0 : 1) == 1) {
      _1_result = dafny.DafnySequence.<java.lang.Byte>concatenate(__default.EncodeBlockPos(b, (long) (long) ((_0_i) - ((long) 3L))), _1_result);
      _0_i = (long) (long) ((_0_i) - ((long) 3L));
    }
    s = _1_result;
    return s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> FromCharsToIndices(dafny.DafnySequence<? extends Character> s)
  {
    dafny.DafnySequence<? extends java.lang.Byte> b = dafny.DafnySequence.<java.lang.Byte> empty(index._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _0_result;
    _0_result = dafny.DafnySequence.<java.lang.Byte> empty(index._typeDescriptor());
    long _hi0 = (long) (s).cardinalityInt();
    for (long _1_i = (long) 0L; java.lang.Long.compareUnsigned(_1_i, _hi0) < 0; _1_i++) {
      _0_result = dafny.DafnySequence.<java.lang.Byte>concatenate(_0_result, dafny.DafnySequence.<java.lang.Byte> of(__default.CharToIndex(((char)(java.lang.Object)((s).select(dafny.Helpers.unsignedToInt(_1_i)))))));
    }
    b = _0_result;
    return b;
  }
  public static dafny.DafnySequence<? extends Character> FromIndicesToChars(dafny.DafnySequence<? extends java.lang.Byte> b)
  {
    dafny.DafnySequence<? extends Character> s = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    dafny.DafnySequence<? extends Character> _0_result;
    _0_result = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    long _hi0 = (long) (b).cardinalityInt();
    for (long _1_i = (long) 0L; java.lang.Long.compareUnsigned(_1_i, _hi0) < 0; _1_i++) {
      _0_result = dafny.DafnySequence.<Character>concatenate(_0_result, dafny.DafnySequence.<Character> of(__default.IndexToChar(((byte)(java.lang.Object)((b).select(dafny.Helpers.unsignedToInt(_1_i)))))));
    }
    s = _0_result;
    return s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> DecodeUnpadded(dafny.DafnySequence<? extends Character> s) {
    return __default.DecodeRecursively(__default.FromCharsToIndices(s));
  }
  public static dafny.DafnySequence<? extends Character> EncodeUnpadded(dafny.DafnySequence<? extends java.lang.Byte> b) {
    return __default.FromIndicesToChars(__default.EncodeRecursively(b));
  }
  public static boolean Is1Padding(dafny.DafnySequence<? extends Character> s) {
    return (((((((long) (s).cardinalityInt()) == ((long) 4L)) && (__default.IsBase64Char(((char)(java.lang.Object)((s).select(0)))))) && (__default.IsBase64Char(((char)(java.lang.Object)((s).select(1)))))) && (__default.IsBase64Char(((char)(java.lang.Object)((s).select(2)))))) && (((dafny.Helpers.remainderUnsignedByte(__default.CharToIndex(((char)(java.lang.Object)((s).select(2)))), (byte) 4)) == 0 ? 0 : 1) == 0)) && ((((char)(java.lang.Object)((s).select(3)))) == ('='));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Decode1Padding(dafny.DafnySequence<? extends Character> s) {
    dafny.DafnySequence<? extends java.lang.Byte> _0_d = __default.DecodeBlock(dafny.DafnySequence.<java.lang.Byte> of(__default.CharToIndex(((char)(java.lang.Object)((s).select(0)))), __default.CharToIndex(((char)(java.lang.Object)((s).select(1)))), __default.CharToIndex(((char)(java.lang.Object)((s).select(2)))), (byte) 0));
    return dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((_0_d).select(0))), ((byte)(java.lang.Object)((_0_d).select(1))));
  }
  public static dafny.DafnySequence<? extends Character> Encode1Padding(dafny.DafnySequence<? extends java.lang.Byte> b) {
    dafny.DafnySequence<? extends java.lang.Byte> _0_e = __default.EncodeBlock(dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((b).select(0))), ((byte)(java.lang.Object)((b).select(1))), (byte) 0));
    return dafny.DafnySequence.<Character> of(__default.IndexToChar(((byte)(java.lang.Object)((_0_e).select(0)))), __default.IndexToChar(((byte)(java.lang.Object)((_0_e).select(1)))), __default.IndexToChar(((byte)(java.lang.Object)((_0_e).select(2)))), '=');
  }
  public static boolean Is2Padding(dafny.DafnySequence<? extends Character> s) {
    return (((((((long) (s).cardinalityInt()) == ((long) 4L)) && (__default.IsBase64Char(((char)(java.lang.Object)((s).select(0)))))) && (__default.IsBase64Char(((char)(java.lang.Object)((s).select(1)))))) && (((dafny.Helpers.remainderUnsignedByte(__default.CharToIndex(((char)(java.lang.Object)((s).select(1)))), (byte) 16)) == 0 ? 0 : 1) == 0)) && ((((char)(java.lang.Object)((s).select(2)))) == ('='))) && ((((char)(java.lang.Object)((s).select(3)))) == ('='));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Decode2Padding(dafny.DafnySequence<? extends Character> s) {
    dafny.DafnySequence<? extends java.lang.Byte> _0_d = __default.DecodeBlock(dafny.DafnySequence.<java.lang.Byte> of(__default.CharToIndex(((char)(java.lang.Object)((s).select(0)))), __default.CharToIndex(((char)(java.lang.Object)((s).select(1)))), (byte) 0, (byte) 0));
    return dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((_0_d).select(0))));
  }
  public static dafny.DafnySequence<? extends Character> Encode2Padding(dafny.DafnySequence<? extends java.lang.Byte> b) {
    dafny.DafnySequence<? extends java.lang.Byte> _0_e = __default.EncodeBlock(dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((b).select(0))), (byte) 0, (byte) 0));
    return dafny.DafnySequence.<Character> of(__default.IndexToChar(((byte)(java.lang.Object)((_0_e).select(0)))), __default.IndexToChar(((byte)(java.lang.Object)((_0_e).select(1)))), '=', '=');
  }
  public static boolean IsBase64String(dafny.DafnySequence<? extends Character> s) {
    long _0_size = (long) (s).cardinalityInt();
    return ((((long) java.lang.Long.remainderUnsigned(_0_size, (long) 4L)) == 0 ? 0 : 1) == 0) && ((__default.IsUnpaddedBase64String(s)) || ((__default.IsUnpaddedBase64String((s).take((long) (long) ((_0_size) - ((long) 4L))))) && ((__default.Is1Padding((s).drop((long) (long) ((_0_size) - ((long) 4L))))) || (__default.Is2Padding((s).drop((long) (long) ((_0_size) - ((long) 4L))))))));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> DecodeValid(dafny.DafnySequence<? extends Character> s) {
    long _0_size = (long) (s).cardinalityInt();
    if (((_0_size) == 0 ? 0 : 1) == 0) {
      return dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    } else {
      long _1_finalBlockStart = (long) (long) ((_0_size) - ((long) 4L));
      dafny.DafnySequence<? extends Character> _2_prefix = (s).take(_1_finalBlockStart);
      dafny.DafnySequence<? extends Character> _3_suffix = (s).drop(_1_finalBlockStart);
      if (__default.Is1Padding(_3_suffix)) {
        return dafny.DafnySequence.<java.lang.Byte>concatenate(__default.DecodeUnpadded(_2_prefix), __default.Decode1Padding(_3_suffix));
      } else if (__default.Is2Padding(_3_suffix)) {
        return dafny.DafnySequence.<java.lang.Byte>concatenate(__default.DecodeUnpadded(_2_prefix), __default.Decode2Padding(_3_suffix));
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
    long _0_size = (long) (b).cardinalityInt();
    long _1_mod = (long) java.lang.Long.remainderUnsigned(_0_size, (long) 3L);
    if (((_1_mod) == 0 ? 0 : 1) == 0) {
      dafny.DafnySequence<? extends Character> _2_s = __default.EncodeUnpadded(b);
      return _2_s;
    } else if ((_1_mod) == ((long) 1L)) {
      dafny.DafnySequence<? extends Character> _3_s1 = __default.EncodeUnpadded((b).take((long) (long) ((_0_size) - ((long) 1L))));
      dafny.DafnySequence<? extends Character> _4_s2 = __default.Encode2Padding((b).drop((long) (long) ((_0_size) - ((long) 1L))));
      dafny.DafnySequence<? extends Character> _5_s = dafny.DafnySequence.<Character>concatenate(_3_s1, _4_s2);
      return _5_s;
    } else {
      dafny.DafnySequence<? extends Character> _6_s1 = __default.EncodeUnpadded((b).take((long) (long) ((_0_size) - ((long) 2L))));
      dafny.DafnySequence<? extends Character> _7_s2 = __default.Encode1Padding((b).drop((long) (long) ((_0_size) - ((long) 2L))));
      dafny.DafnySequence<? extends Character> _8_s = dafny.DafnySequence.<Character>concatenate(_6_s1, _7_s2);
      return _8_s;
    }
  }
  @Override
  public java.lang.String toString() {
    return "Base64._default";
  }
}
