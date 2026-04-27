// Class MinimalWellFormedCodeUnitSeq
// Dafny class MinimalWellFormedCodeUnitSeq compiled into Java
package Utf8EncodingForm_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class MinimalWellFormedCodeUnitSeq {
  public MinimalWellFormedCodeUnitSeq() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends java.lang.Byte> __source) {
    dafny.DafnySequence<? extends java.lang.Byte> _4_s = __source;
    return __default.IsMinimalWellFormedCodeUnitSubsequence(_4_s);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Byte>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends java.lang.Byte>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<java.lang.Byte> empty(dafny.TypeDescriptor.BYTE));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Byte>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Byte>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
