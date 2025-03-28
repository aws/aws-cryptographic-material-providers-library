// Class BatchGetItemInput
// Dafny class BatchGetItemInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class BatchGetItemInput {
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes> _RequestItems;
  public Wrappers_Compile.Option<ReturnConsumedCapacity> _ReturnConsumedCapacity;
  public BatchGetItemInput (dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes> RequestItems, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity) {
    this._RequestItems = RequestItems;
    this._ReturnConsumedCapacity = ReturnConsumedCapacity;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchGetItemInput o = (BatchGetItemInput)other;
    return true && java.util.Objects.equals(this._RequestItems, o._RequestItems) && java.util.Objects.equals(this._ReturnConsumedCapacity, o._ReturnConsumedCapacity);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RequestItems);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnConsumedCapacity);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BatchGetItemInput.BatchGetItemInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RequestItems));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnConsumedCapacity));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<BatchGetItemInput> _TYPE = dafny.TypeDescriptor.<BatchGetItemInput>referenceWithInitializer(BatchGetItemInput.class, () -> BatchGetItemInput.Default());
  public static dafny.TypeDescriptor<BatchGetItemInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<BatchGetItemInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BatchGetItemInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.BatchGetItemInput.create(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,KeysAndAttributes> empty(), Wrappers_Compile.Option.<ReturnConsumedCapacity>Default(ReturnConsumedCapacity._typeDescriptor()));
  public static BatchGetItemInput Default() {
    return theDefault;
  }
  public static BatchGetItemInput create(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes> RequestItems, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity) {
    return new BatchGetItemInput(RequestItems, ReturnConsumedCapacity);
  }
  public static BatchGetItemInput create_BatchGetItemInput(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes> RequestItems, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity) {
    return create(RequestItems, ReturnConsumedCapacity);
  }
  public boolean is_BatchGetItemInput() { return true; }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends KeysAndAttributes> dtor_RequestItems() {
    return this._RequestItems;
  }
  public Wrappers_Compile.Option<ReturnConsumedCapacity> dtor_ReturnConsumedCapacity() {
    return this._ReturnConsumedCapacity;
  }
}
