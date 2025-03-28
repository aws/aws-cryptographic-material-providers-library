// Class TransactWriteItemList
// Dafny class TransactWriteItemList compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class TransactWriteItemList {
  public TransactWriteItemList() {
  }
  public static boolean _Is(dafny.DafnySequence<? extends TransactWriteItem> __source) {
    dafny.DafnySequence<? extends TransactWriteItem> _48_x = __source;
    return __default.IsValid__TransactWriteItemList(_48_x);
  }
  private static final dafny.TypeDescriptor<dafny.DafnySequence<? extends TransactWriteItem>> _TYPE = dafny.TypeDescriptor.<dafny.DafnySequence<? extends TransactWriteItem>>referenceWithInitializer(dafny.DafnySequence.class, () -> dafny.DafnySequence.<TransactWriteItem> empty(TransactWriteItem._typeDescriptor()));
  public static dafny.TypeDescriptor<dafny.DafnySequence<? extends TransactWriteItem>> _typeDescriptor() {
    return (dafny.TypeDescriptor<dafny.DafnySequence<? extends TransactWriteItem>>) (dafny.TypeDescriptor<?>) _TYPE;
  }
}
