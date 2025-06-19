// Class bytes32
// Dafny class bytes32 compiled into Java
package JSON_mSerializer_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class bytes32 {
  public bytes32() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends java.lang.Byte> __source) {
    dafny.DafnySequence<? extends java.lang.Byte> _0_bs = __source;
    return (java.math.BigInteger.valueOf((_0_bs).length())).compareTo(BoundedInts_Compile.__default.TWO__TO__THE__32()) < 0;
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Byte>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends java.lang.Byte>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Byte>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Byte>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
