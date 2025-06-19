// Class ItemResponseList
// Dafny class ItemResponseList compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ItemResponseList {
  public ItemResponseList() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends ItemResponse> __source) {
    dafny.DafnySequence<? extends ItemResponse> _10_x = __source;
    return __default.IsValid__ItemResponseList(_10_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends ItemResponse>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends ItemResponse>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<ItemResponse> empty(ItemResponse._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends ItemResponse>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends ItemResponse>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
