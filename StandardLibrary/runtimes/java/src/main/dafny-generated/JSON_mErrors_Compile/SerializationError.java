// Class SerializationError
// Dafny class SerializationError compiled into Java
package JSON_mErrors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class SerializationError {
  public SerializationError() {
  }
  private static final dafny.TypeDescriptor<SerializationError> _TYPE = dafny.TypeDescriptor.<SerializationError>referenceWithInitializer(SerializationError.class, () -> SerializationError.Default());
  public static dafny.TypeDescriptor<SerializationError> _typeDescriptor() {
    return (dafny.TypeDescriptor<SerializationError>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SerializationError theDefault = SerializationError.create_OutOfMemory();
  public static SerializationError Default() {
    return theDefault;
  }
  public static SerializationError create_OutOfMemory() {
    return new SerializationError_OutOfMemory();
  }
  public static SerializationError create_IntTooLarge(java.math.BigInteger i) {
    return new SerializationError_IntTooLarge(i);
  }
  public static SerializationError create_StringTooLong(dafny.DafnySequence<? extends Character> s) {
    return new SerializationError_StringTooLong(s);
  }
  public static SerializationError create_InvalidUnicode() {
    return new SerializationError_InvalidUnicode();
  }
  public boolean is_OutOfMemory() { return this instanceof SerializationError_OutOfMemory; }
  public boolean is_IntTooLarge() { return this instanceof SerializationError_IntTooLarge; }
  public boolean is_StringTooLong() { return this instanceof SerializationError_StringTooLong; }
  public boolean is_InvalidUnicode() { return this instanceof SerializationError_InvalidUnicode; }
  public java.math.BigInteger dtor_i() {
    SerializationError d = this;
    return ((SerializationError_IntTooLarge)d)._i;
  }
  public dafny.DafnySequence<? extends Character> dtor_s() {
    SerializationError d = this;
    return ((SerializationError_StringTooLong)d)._s;
  }
  public dafny.DafnySequence<? extends Character> ToString() {
    SerializationError _source0 = this;
    if (_source0.is_OutOfMemory()) {
      return dafny.DafnySequence.asString("Out of memory");
    } else if (_source0.is_IntTooLarge()) {
      java.math.BigInteger _0___mcc_h0 = ((JSON_mErrors_Compile.SerializationError_IntTooLarge)_source0)._i;
      java.math.BigInteger _1_i = _0___mcc_h0;
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Integer too large: "), JSON_mUtils_mStr_Compile.__default.OfInt(_1_i, java.math.BigInteger.valueOf(10L)));
    } else if (_source0.is_StringTooLong()) {
      dafny.DafnySequence<? extends Character> _2___mcc_h1 = ((JSON_mErrors_Compile.SerializationError_StringTooLong)_source0)._s;
      dafny.DafnySequence<? extends Character> _3_s = _2___mcc_h1;
      return dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("String too long: "), _3_s);
    } else {
      return dafny.DafnySequence.asString("Invalid Unicode sequence");
    }
  }
}
