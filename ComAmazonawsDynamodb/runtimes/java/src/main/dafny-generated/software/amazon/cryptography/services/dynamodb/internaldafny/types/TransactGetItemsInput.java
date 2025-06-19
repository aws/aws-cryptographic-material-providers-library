// Class TransactGetItemsInput
// Dafny class TransactGetItemsInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class TransactGetItemsInput {
  public dafny.DafnySequence<? extends TransactGetItem> _TransactItems;
  public Wrappers_Compile.Option<ReturnConsumedCapacity> _ReturnConsumedCapacity;
  public TransactGetItemsInput (dafny.DafnySequence<? extends TransactGetItem> TransactItems, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity) {
    this._TransactItems = TransactItems;
    this._ReturnConsumedCapacity = ReturnConsumedCapacity;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TransactGetItemsInput o = (TransactGetItemsInput)other;
    return true && java.util.Objects.equals(this._TransactItems, o._TransactItems) && java.util.Objects.equals(this._ReturnConsumedCapacity, o._ReturnConsumedCapacity);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TransactItems);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnConsumedCapacity);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TransactGetItemsInput.TransactGetItemsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TransactItems));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnConsumedCapacity));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TransactGetItemsInput> _TYPE = dafny.TypeDescriptor.<TransactGetItemsInput>referenceWithInitializer(TransactGetItemsInput.class, () -> TransactGetItemsInput.Default());
  public static dafny.TypeDescriptor<TransactGetItemsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<TransactGetItemsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TransactGetItemsInput theDefault = TransactGetItemsInput.create(dafny.DafnySequence.<TransactGetItem> empty(TransactGetItem._typeDescriptor()), Wrappers_Compile.Option.<ReturnConsumedCapacity>Default(ReturnConsumedCapacity._typeDescriptor()));
  public static TransactGetItemsInput Default() {
    return theDefault;
  }
  public static TransactGetItemsInput create(dafny.DafnySequence<? extends TransactGetItem> TransactItems, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity) {
    return new TransactGetItemsInput(TransactItems, ReturnConsumedCapacity);
  }
  public static TransactGetItemsInput create_TransactGetItemsInput(dafny.DafnySequence<? extends TransactGetItem> TransactItems, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity) {
    return create(TransactItems, ReturnConsumedCapacity);
  }
  public boolean is_TransactGetItemsInput() { return true; }
  public dafny.DafnySequence<? extends TransactGetItem> dtor_TransactItems() {
    return this._TransactItems;
  }
  public Wrappers_Compile.Option<ReturnConsumedCapacity> dtor_ReturnConsumedCapacity() {
    return this._ReturnConsumedCapacity;
  }
}
