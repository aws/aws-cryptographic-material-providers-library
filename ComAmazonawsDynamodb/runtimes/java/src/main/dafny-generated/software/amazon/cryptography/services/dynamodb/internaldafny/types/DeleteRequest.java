// Class DeleteRequest
// Dafny class DeleteRequest compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteRequest {
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> _Key;
  public DeleteRequest (dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Key) {
    this._Key = Key;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteRequest o = (DeleteRequest)other;
    return true && java.util.Objects.equals(this._Key, o._Key);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Key);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DeleteRequest.DeleteRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Key));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteRequest> _TYPE = dafny.TypeDescriptor.<DeleteRequest>referenceWithInitializer(DeleteRequest.class, () -> DeleteRequest.Default());
  public static dafny.TypeDescriptor<DeleteRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteRequest theDefault = DeleteRequest.create(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,AttributeValue> empty());
  public static DeleteRequest Default() {
    return theDefault;
  }
  public static DeleteRequest create(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Key) {
    return new DeleteRequest(Key);
  }
  public static DeleteRequest create_DeleteRequest(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Key) {
    return create(Key);
  }
  public boolean is_DeleteRequest() { return true; }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> dtor_Key() {
    return this._Key;
  }
}
