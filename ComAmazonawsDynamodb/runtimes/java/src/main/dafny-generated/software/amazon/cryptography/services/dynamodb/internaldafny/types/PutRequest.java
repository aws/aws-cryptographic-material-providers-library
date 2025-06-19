// Class PutRequest
// Dafny class PutRequest compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class PutRequest {
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> _Item;
  public PutRequest (dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Item) {
    this._Item = Item;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PutRequest o = (PutRequest)other;
    return true && java.util.Objects.equals(this._Item, o._Item);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Item);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.PutRequest.PutRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Item));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PutRequest> _TYPE = dafny.TypeDescriptor.<PutRequest>referenceWithInitializer(PutRequest.class, () -> PutRequest.Default());
  public static dafny.TypeDescriptor<PutRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<PutRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PutRequest theDefault = PutRequest.create(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,AttributeValue> empty());
  public static PutRequest Default() {
    return theDefault;
  }
  public static PutRequest create(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Item) {
    return new PutRequest(Item);
  }
  public static PutRequest create_PutRequest(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Item) {
    return create(Item);
  }
  public boolean is_PutRequest() { return true; }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> dtor_Item() {
    return this._Item;
  }
}
