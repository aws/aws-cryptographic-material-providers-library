// Class BatchWriteItemInput
// Dafny class BatchWriteItemInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BatchWriteItemInput {
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends WriteRequest>> _RequestItems;
  public Wrappers_Compile.Option<ReturnConsumedCapacity> _ReturnConsumedCapacity;
  public Wrappers_Compile.Option<ReturnItemCollectionMetrics> _ReturnItemCollectionMetrics;
  public BatchWriteItemInput (dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends WriteRequest>> RequestItems, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<ReturnItemCollectionMetrics> ReturnItemCollectionMetrics) {
    this._RequestItems = RequestItems;
    this._ReturnConsumedCapacity = ReturnConsumedCapacity;
    this._ReturnItemCollectionMetrics = ReturnItemCollectionMetrics;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchWriteItemInput o = (BatchWriteItemInput)other;
    return true && java.util.Objects.equals(this._RequestItems, o._RequestItems) && java.util.Objects.equals(this._ReturnConsumedCapacity, o._ReturnConsumedCapacity) && java.util.Objects.equals(this._ReturnItemCollectionMetrics, o._ReturnItemCollectionMetrics);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RequestItems);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnConsumedCapacity);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnItemCollectionMetrics);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BatchWriteItemInput.BatchWriteItemInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RequestItems));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnConsumedCapacity));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnItemCollectionMetrics));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<BatchWriteItemInput> _TYPE = dafny.TypeDescriptor.<BatchWriteItemInput>referenceWithInitializer(BatchWriteItemInput.class, () -> BatchWriteItemInput.Default());
  public static dafny.TypeDescriptor<BatchWriteItemInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<BatchWriteItemInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BatchWriteItemInput theDefault = BatchWriteItemInput.create(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,dafny.DafnySequence<? extends WriteRequest>> empty(), Wrappers_Compile.Option.<ReturnConsumedCapacity>Default(ReturnConsumedCapacity._typeDescriptor()), Wrappers_Compile.Option.<ReturnItemCollectionMetrics>Default(ReturnItemCollectionMetrics._typeDescriptor()));
  public static BatchWriteItemInput Default() {
    return theDefault;
  }
  public static BatchWriteItemInput create(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends WriteRequest>> RequestItems, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<ReturnItemCollectionMetrics> ReturnItemCollectionMetrics) {
    return new BatchWriteItemInput(RequestItems, ReturnConsumedCapacity, ReturnItemCollectionMetrics);
  }
  public static BatchWriteItemInput create_BatchWriteItemInput(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends WriteRequest>> RequestItems, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<ReturnItemCollectionMetrics> ReturnItemCollectionMetrics) {
    return create(RequestItems, ReturnConsumedCapacity, ReturnItemCollectionMetrics);
  }
  public boolean is_BatchWriteItemInput() { return true; }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends WriteRequest>> dtor_RequestItems() {
    return this._RequestItems;
  }
  public Wrappers_Compile.Option<ReturnConsumedCapacity> dtor_ReturnConsumedCapacity() {
    return this._ReturnConsumedCapacity;
  }
  public Wrappers_Compile.Option<ReturnItemCollectionMetrics> dtor_ReturnItemCollectionMetrics() {
    return this._ReturnItemCollectionMetrics;
  }
}
