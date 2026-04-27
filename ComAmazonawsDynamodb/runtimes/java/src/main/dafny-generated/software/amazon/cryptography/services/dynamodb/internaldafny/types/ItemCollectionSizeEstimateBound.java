// Class ItemCollectionSizeEstimateBound
// Dafny class ItemCollectionSizeEstimateBound compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ItemCollectionSizeEstimateBound {
  public ItemCollectionSizeEstimateBound() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends java.lang.Byte> __source) {
    dafny.DafnySequence<? extends java.lang.Byte> _8_x = __source;
    return __default.IsValid__ItemCollectionSizeEstimateBound(_8_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Byte>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends java.lang.Byte>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Byte>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends java.lang.Byte>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
