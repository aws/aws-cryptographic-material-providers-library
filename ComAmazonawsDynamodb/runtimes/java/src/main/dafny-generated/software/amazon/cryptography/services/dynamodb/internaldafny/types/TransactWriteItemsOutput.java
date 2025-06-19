// Class TransactWriteItemsOutput
// Dafny class TransactWriteItemsOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class TransactWriteItemsOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> _ConsumedCapacity;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends ItemCollectionMetrics>>> _ItemCollectionMetrics;
  public TransactWriteItemsOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends ItemCollectionMetrics>>> ItemCollectionMetrics) {
    this._ConsumedCapacity = ConsumedCapacity;
    this._ItemCollectionMetrics = ItemCollectionMetrics;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TransactWriteItemsOutput o = (TransactWriteItemsOutput)other;
    return true && java.util.Objects.equals(this._ConsumedCapacity, o._ConsumedCapacity) && java.util.Objects.equals(this._ItemCollectionMetrics, o._ItemCollectionMetrics);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConsumedCapacity);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ItemCollectionMetrics);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.TransactWriteItemsOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ConsumedCapacity));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ItemCollectionMetrics));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TransactWriteItemsOutput> _TYPE = dafny.TypeDescriptor.<TransactWriteItemsOutput>referenceWithInitializer(TransactWriteItemsOutput.class, () -> TransactWriteItemsOutput.Default());
  public static dafny.TypeDescriptor<TransactWriteItemsOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<TransactWriteItemsOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TransactWriteItemsOutput theDefault = TransactWriteItemsOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends ConsumedCapacity>>Default(dafny.DafnySequence.<ConsumedCapacity>_typeDescriptor(ConsumedCapacity._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends ItemCollectionMetrics>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends ItemCollectionMetrics>>_typeDescriptor(TableArn._typeDescriptor(), dafny.DafnySequence.<ItemCollectionMetrics>_typeDescriptor(ItemCollectionMetrics._typeDescriptor()))));
  public static TransactWriteItemsOutput Default() {
    return theDefault;
  }
  public static TransactWriteItemsOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends ItemCollectionMetrics>>> ItemCollectionMetrics) {
    return new TransactWriteItemsOutput(ConsumedCapacity, ItemCollectionMetrics);
  }
  public static TransactWriteItemsOutput create_TransactWriteItemsOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends ItemCollectionMetrics>>> ItemCollectionMetrics) {
    return create(ConsumedCapacity, ItemCollectionMetrics);
  }
  public boolean is_TransactWriteItemsOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> dtor_ConsumedCapacity() {
    return this._ConsumedCapacity;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends ItemCollectionMetrics>>> dtor_ItemCollectionMetrics() {
    return this._ItemCollectionMetrics;
  }
}
