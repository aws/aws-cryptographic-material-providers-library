// Class ValidUTF8Bytes
// Dafny class ValidUTF8Bytes compiled into Java
package UTF8;

@SuppressWarnings({"unchecked", "deprecation"})
public class ValidUTF8Bytes {
  public ValidUTF8Bytes() {
  }
  public static dafny.DafnySequence Witness = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
  public static dafny.DafnySequence<? extends java.lang.Byte> defaultValue() {
    return Witness;
  }
  public static boolean _Is(dafny.DafnySequence<? extends java.lang.Byte> __source) {
    dafny.DafnySequence<? extends java.lang.Byte> _0_i = __source;
    return __default.ValidUTF8Seq(_0_i);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Byte>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends java.lang.Byte>>referenceWithInitializer(dafny.DafnySequence.class, () -> ValidUTF8Bytes.defaultValue());
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Byte>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Byte>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
