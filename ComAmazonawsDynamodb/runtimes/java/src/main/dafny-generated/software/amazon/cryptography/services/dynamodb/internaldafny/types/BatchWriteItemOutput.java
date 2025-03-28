// Class BatchWriteItemOutput
// Dafny class BatchWriteItemOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class BatchWriteItemOutput {
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends WriteRequest>>> _UnprocessedItems;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends ItemCollectionMetrics>>> _ItemCollectionMetrics;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> _ConsumedCapacity;
  public BatchWriteItemOutput (Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends WriteRequest>>> UnprocessedItems, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends ItemCollectionMetrics>>> ItemCollectionMetrics, Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity) {
    this._UnprocessedItems = UnprocessedItems;
    this._ItemCollectionMetrics = ItemCollectionMetrics;
    this._ConsumedCapacity = ConsumedCapacity;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchWriteItemOutput o = (BatchWriteItemOutput)other;
    return true && java.util.Objects.equals(this._UnprocessedItems, o._UnprocessedItems) && java.util.Objects.equals(this._ItemCollectionMetrics, o._ItemCollectionMetrics) && java.util.Objects.equals(this._ConsumedCapacity, o._ConsumedCapacity);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._UnprocessedItems);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ItemCollectionMetrics);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConsumedCapacity);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BatchWriteItemOutput.BatchWriteItemOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._UnprocessedItems));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ItemCollectionMetrics));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConsumedCapacity));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<BatchWriteItemOutput> _TYPE = dafny.TypeDescriptor.<BatchWriteItemOutput>referenceWithInitializer(BatchWriteItemOutput.class, () -> BatchWriteItemOutput.Default());
  public static dafny.TypeDescriptor<BatchWriteItemOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<BatchWriteItemOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BatchWriteItemOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.BatchWriteItemOutput.create(Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends WriteRequest>>>Default(BatchWriteItemRequestMap._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends ItemCollectionMetrics>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends ItemCollectionMetrics>>_typeDescriptor(TableArn._typeDescriptor(), dafny.DafnySequence.<ItemCollectionMetrics>_typeDescriptor(ItemCollectionMetrics._typeDescriptor()))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ConsumedCapacity>>Default(dafny.DafnySequence.<ConsumedCapacity>_typeDescriptor(ConsumedCapacity._typeDescriptor())));
  public static BatchWriteItemOutput Default() {
    return theDefault;
  }
  public static BatchWriteItemOutput create(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends WriteRequest>>> UnprocessedItems, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends ItemCollectionMetrics>>> ItemCollectionMetrics, Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity) {
    return new BatchWriteItemOutput(UnprocessedItems, ItemCollectionMetrics, ConsumedCapacity);
  }
  public static BatchWriteItemOutput create_BatchWriteItemOutput(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends WriteRequest>>> UnprocessedItems, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends ItemCollectionMetrics>>> ItemCollectionMetrics, Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity) {
    return create(UnprocessedItems, ItemCollectionMetrics, ConsumedCapacity);
  }
  public boolean is_BatchWriteItemOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends WriteRequest>>> dtor_UnprocessedItems() {
    return this._UnprocessedItems;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends ItemCollectionMetrics>>> dtor_ItemCollectionMetrics() {
    return this._ItemCollectionMetrics;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> dtor_ConsumedCapacity() {
    return this._ConsumedCapacity;
  }
}
