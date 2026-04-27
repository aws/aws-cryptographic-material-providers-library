// Class DeserializationError
// Dafny class DeserializationError compiled into Java
package JSON_mErrors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class DeserializationError {
  public DeserializationError() {
  }
  private static final dafny.TypeDescriptor<DeserializationError> _TYPE = dafny.TypeDescriptor.<DeserializationError>referenceWithInitializer(DeserializationError.class, () -> DeserializationError.Default());
  public static dafny.TypeDescriptor<DeserializationError> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeserializationError>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeserializationError theDefault = DeserializationError.create_UnterminatedSequence();
  public static DeserializationError Default() {
    return theDefault;
  }
  public static DeserializationError create_UnterminatedSequence() {
    return new DeserializationError_UnterminatedSequence();
  }
  public static DeserializationError create_UnsupportedEscape(dafny.DafnySequence<? extends Character> str) {
    return new DeserializationError_UnsupportedEscape(str);
  }
  public static DeserializationError create_EscapeAtEOS() {
    return new DeserializationError_EscapeAtEOS();
  }
  public static DeserializationError create_EmptyNumber() {
    return new DeserializationError_EmptyNumber();
  }
  public static DeserializationError create_ExpectingEOF() {
    return new DeserializationError_ExpectingEOF();
  }
  public static DeserializationError create_IntOverflow() {
    return new DeserializationError_IntOverflow();
  }
  public static DeserializationError create_ReachedEOF() {
    return new DeserializationError_ReachedEOF();
  }
  public static DeserializationError create_ExpectingByte(byte expected, short b) {
    return new DeserializationError_ExpectingByte(expected, b);
  }
  public static DeserializationError create_ExpectingAnyByte(dafny.DafnySequence<? extends java.lang.Byte> expected__sq, short b) {
    return new DeserializationError_ExpectingAnyByte(expected__sq, b);
  }
  public static DeserializationError create_InvalidUnicode() {
    return new DeserializationError_InvalidUnicode();
  }
  public boolean is_UnterminatedSequence() { return this instanceof DeserializationError_UnterminatedSequence; }
  public boolean is_UnsupportedEscape() { return this instanceof DeserializationError_UnsupportedEscape; }
  public boolean is_EscapeAtEOS() { return this instanceof DeserializationError_EscapeAtEOS; }
  public boolean is_EmptyNumber() { return this instanceof DeserializationError_EmptyNumber; }
  public boolean is_ExpectingEOF() { return this instanceof DeserializationError_ExpectingEOF; }
  public boolean is_IntOverflow() { return this instanceof DeserializationError_IntOverflow; }
  public boolean is_ReachedEOF() { return this instanceof DeserializationError_ReachedEOF; }
  public boolean is_ExpectingByte() { return this instanceof DeserializationError_ExpectingByte; }
  public boolean is_ExpectingAnyByte() { return this instanceof DeserializationError_ExpectingAnyByte; }
  public boolean is_InvalidUnicode() { return this instanceof DeserializationError_InvalidUnicode; }
  public dafny.DafnySequence<? extends Character> dtor_str() {
    DeserializationError d = this;
    return ((DeserializationError_UnsupportedEscape)d)._str;
  }
  public byte dtor_expected() {
    DeserializationError d = this;
    return ((DeserializationError_ExpectingByte)d)._expected;
  }
  public short dtor_b() {
    DeserializationError d = this;
    if (d instanceof DeserializationError_ExpectingByte) { return ((DeserializationError_ExpectingByte)d)._b; }
    return ((DeserializationError_ExpectingAnyByte)d)._b;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_expected__sq() {
    DeserializationError d = this;
    return ((DeserializationError_ExpectingAnyByte)d)._expected__sq;
  }
  public dafny.DafnySequence<? extends Character> ToString() {
    DeserializationError _source0 = this;
    if (_source0.is_UnterminatedSequence()) {
      return dafny.DafnySequence.asString("Unterminated sequence");
    } else if (_source0.is_UnsupportedEscape()) {
      dafny.DafnySequence<? extends Character> _0___mcc_h0 = ((JSON_mErrors_Compile.DeserializationError_UnsupportedEscape)_source0)._str;
      dafny.DafnySequence<? extends Character> _1_str = _0___mcc_h0;
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Unsupported escape sequence: "), _1_str);
    } else if (_source0.is_EscapeAtEOS()) {
      return dafny.DafnySequence.asString("Escape character at end of string");
    } else if (_source0.is_EmptyNumber()) {
      return dafny.DafnySequence.asString("Number must contain at least one digit");
    } else if (_source0.is_ExpectingEOF()) {
      return dafny.DafnySequence.asString("Expecting EOF");
    } else if (_source0.is_IntOverflow()) {
      return dafny.DafnySequence.asString("Input length does not fit in a 32-bit counter");
    } else if (_source0.is_ReachedEOF()) {
      return dafny.DafnySequence.asString("Reached EOF");
    } else if (_source0.is_ExpectingByte()) {
      byte _2___mcc_h1 = ((JSON_mErrors_Compile.DeserializationError_ExpectingByte)_source0)._expected;
      short _3___mcc_h2 = ((JSON_mErrors_Compile.DeserializationError_ExpectingByte)_source0)._b;
      short _4_b = _3___mcc_h2;
      byte _5_b0 = _2___mcc_h1;
      dafny.DafnySequence<? extends Character> _6_c = ((java.lang.Integer.signum((_4_b)) == 1) ? (dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("'"), dafny.DafnySequence.<Character> of((char)dafny.Helpers.toInt(_4_b))), dafny.DafnySequence.asString("'"))) : (dafny.DafnySequence.asString("EOF")));
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Expecting '"), dafny.DafnySequence.<Character> of((char)java.lang.Byte.toUnsignedInt(_5_b0))), dafny.DafnySequence.asString("', read ")), _6_c);
    } else if (_source0.is_ExpectingAnyByte()) {
      dafny.DafnySequence<? extends java.lang.Byte> _7___mcc_h3 = ((JSON_mErrors_Compile.DeserializationError_ExpectingAnyByte)_source0)._expected__sq;
      short _8___mcc_h4 = ((JSON_mErrors_Compile.DeserializationError_ExpectingAnyByte)_source0)._b;
      short _9_b = _8___mcc_h4;
      dafny.DafnySequence<? extends java.lang.Byte> _10_bs0 = _7___mcc_h3;
      dafny.DafnySequence<? extends Character> _11_c = ((java.lang.Integer.signum((_9_b)) == 1) ? (dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("'"), dafny.DafnySequence.<Character> of((char)dafny.Helpers.toInt(_9_b))), dafny.DafnySequence.asString("'"))) : (dafny.DafnySequence.asString("EOF")));
      dafny.DafnySequence<? extends Character> _12_c0s = dafny.DafnySequence.Create(dafny.TypeDescriptor.CHAR, java.math.BigInteger.valueOf((_10_bs0).length()), ((java.util.function.Function<dafny.DafnySequence<? extends java.lang.Byte>, java.util.function.Function<java.math.BigInteger, Character>>)(_13_bs0) -> ((java.util.function.Function<java.math.BigInteger, Character>)(_14_idx_boxed0) -> {
        java.math.BigInteger _14_idx = ((java.math.BigInteger)(java.lang.Object)(_14_idx_boxed0));
        return (char)java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)((_13_bs0).select(dafny.Helpers.toInt((_14_idx))))));
      })).apply(_10_bs0));
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Expecting one of '"), _12_c0s), dafny.DafnySequence.asString("', read ")), _11_c);
    } else {
      return dafny.DafnySequence.asString("Invalid Unicode sequence");
    }
  }
}
