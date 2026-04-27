// Class WellFormedCodeUnitSeq
// Dafny class WellFormedCodeUnitSeq compiled into Java
package Utf8EncodingForm_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class WellFormedCodeUnitSeq {
  public WellFormedCodeUnitSeq() {
  }
  public static dafny.DafnySequence Witness = dafny.DafnySequence.<java.lang.Byte> empty(dafny.TypeDescriptor.BYTE);
  public static dafny.DafnySequence<? extends java.lang.Byte> defaultValue() {
    return Witness;
  }
  public static boolean _Is(dafny.DafnySequence<? extends java.lang.Byte> __source) {
    dafny.DafnySequence<? extends java.lang.Byte> _3_s = __source;
    return __default.IsWellFormedCodeUnitSequence(_3_s);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Byte>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends java.lang.Byte>>referenceWithInitializer(dafny.DafnySequence.class, () -> WellFormedCodeUnitSeq.defaultValue());
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Byte>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Byte>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
