// Class ItemResponse
// Dafny class ItemResponse compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ItemResponse {
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _Item;
  public ItemResponse (Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item) {
    this._Item = Item;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ItemResponse o = (ItemResponse)other;
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
    s.append("ComAmazonawsDynamodbTypes.ItemResponse.ItemResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Item));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ItemResponse> _TYPE = dafny.TypeDescriptor.<ItemResponse>referenceWithInitializer(ItemResponse.class, () -> ItemResponse.Default());
  public static dafny.TypeDescriptor<ItemResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<ItemResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ItemResponse theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ItemResponse.create(Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor())));
  public static ItemResponse Default() {
    return theDefault;
  }
  public static ItemResponse create(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item) {
    return new ItemResponse(Item);
  }
  public static ItemResponse create_ItemResponse(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Item) {
    return create(Item);
  }
  public boolean is_ItemResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_Item() {
    return this._Item;
  }
}
