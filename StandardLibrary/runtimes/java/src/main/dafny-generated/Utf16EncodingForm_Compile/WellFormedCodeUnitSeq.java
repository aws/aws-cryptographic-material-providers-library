// Class WellFormedCodeUnitSeq
// Dafny class WellFormedCodeUnitSeq compiled into Java
package Utf16EncodingForm_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class WellFormedCodeUnitSeq {
  public WellFormedCodeUnitSeq() {
  }
  public static dafny.DafnySequence Witness = dafny.DafnySequence.<java.lang.Short> empty(dafny.TypeDescriptor.SHORT);
  public static dafny.DafnySequence<? extends java.lang.Short> defaultValue() {
    return Witness;
  }
  public static boolean _Is(dafny.DafnySequence<? extends java.lang.Short> __source) {
    dafny.DafnySequence<? extends java.lang.Short> _3_s = __source;
    return __default.IsWellFormedCodeUnitSequence(_3_s);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Short>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends java.lang.Short>>referenceWithInitializer(dafny.DafnySequence.class, () -> WellFormedCodeUnitSeq.defaultValue());
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Short>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Short>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
