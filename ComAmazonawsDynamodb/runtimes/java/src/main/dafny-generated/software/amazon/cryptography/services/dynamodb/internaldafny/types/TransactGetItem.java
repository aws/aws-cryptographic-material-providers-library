// Class TransactGetItem
// Dafny class TransactGetItem compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class TransactGetItem {
  public Get _Get;
  public TransactGetItem (Get Get) {
    this._Get = Get;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TransactGetItem o = (TransactGetItem)other;
    return true && java.util.Objects.equals(this._Get, o._Get);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Get);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TransactGetItem.TransactGetItem");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Get));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TransactGetItem> _TYPE = dafny.TypeDescriptor.<TransactGetItem>referenceWithInitializer(TransactGetItem.class, () -> TransactGetItem.Default());
  public static dafny.TypeDescriptor<TransactGetItem> _typeDescriptor() {
    return (dafny.TypeDescriptor<TransactGetItem>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TransactGetItem theDefault = TransactGetItem.create(Get.Default());
  public static TransactGetItem Default() {
    return theDefault;
  }
  public static TransactGetItem create(Get Get) {
    return new TransactGetItem(Get);
  }
  public static TransactGetItem create_TransactGetItem(Get Get) {
    return create(Get);
  }
  public boolean is_TransactGetItem() { return true; }
  public Get dtor_Get() {
    return this._Get;
  }
}
