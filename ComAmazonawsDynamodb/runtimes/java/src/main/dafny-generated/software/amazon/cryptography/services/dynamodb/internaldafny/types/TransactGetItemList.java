// Class TransactGetItemList
// Dafny class TransactGetItemList compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class TransactGetItemList {
  public TransactGetItemList() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends TransactGetItem> __source) {
    dafny.DafnySequence<? extends TransactGetItem> _47_x = __source;
    return __default.IsValid__TransactGetItemList(_47_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends TransactGetItem>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends TransactGetItem>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<TransactGetItem> empty(TransactGetItem._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends TransactGetItem>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends TransactGetItem>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
