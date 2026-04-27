// Class DeleteItemOutput
// Dafny class DeleteItemOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteItemOutput {
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _Attributes;
  public Wrappers_Compile.Option<ConsumedCapacity> _ConsumedCapacity;
  public Wrappers_Compile.Option<ItemCollectionMetrics> _ItemCollectionMetrics;
  public DeleteItemOutput (Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Attributes, Wrappers_Compile.Option<ConsumedCapacity> ConsumedCapacity, Wrappers_Compile.Option<ItemCollectionMetrics> ItemCollectionMetrics) {
    this._Attributes = Attributes;
    this._ConsumedCapacity = ConsumedCapacity;
    this._ItemCollectionMetrics = ItemCollectionMetrics;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteItemOutput o = (DeleteItemOutput)other;
    return true && java.util.Objects.equals(this._Attributes, o._Attributes) && java.util.Objects.equals(this._ConsumedCapacity, o._ConsumedCapacity) && java.util.Objects.equals(this._ItemCollectionMetrics, o._ItemCollectionMetrics);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Attributes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConsumedCapacity);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ItemCollectionMetrics);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DeleteItemOutput.DeleteItemOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Attributes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConsumedCapacity));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ItemCollectionMetrics));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteItemOutput> _TYPE = dafny.TypeDescriptor.<DeleteItemOutput>referenceWithInitializer(DeleteItemOutput.class, () -> DeleteItemOutput.Default());
  public static dafny.TypeDescriptor<DeleteItemOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteItemOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteItemOutput theDefault = DeleteItemOutput.create(Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor())), Wrappers_Compile.Option.<ConsumedCapacity>Default(ConsumedCapacity._typeDescriptor()), Wrappers_Compile.Option.<ItemCollectionMetrics>Default(ItemCollectionMetrics._typeDescriptor()));
  public static DeleteItemOutput Default() {
    return theDefault;
  }
  public static DeleteItemOutput create(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Attributes, Wrappers_Compile.Option<ConsumedCapacity> ConsumedCapacity, Wrappers_Compile.Option<ItemCollectionMetrics> ItemCollectionMetrics) {
    return new DeleteItemOutput(Attributes, ConsumedCapacity, ItemCollectionMetrics);
  }
  public static DeleteItemOutput create_DeleteItemOutput(Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Attributes, Wrappers_Compile.Option<ConsumedCapacity> ConsumedCapacity, Wrappers_Compile.Option<ItemCollectionMetrics> ItemCollectionMetrics) {
    return create(Attributes, ConsumedCapacity, ItemCollectionMetrics);
  }
  public boolean is_DeleteItemOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_Attributes() {
    return this._Attributes;
  }
  public Wrappers_Compile.Option<ConsumedCapacity> dtor_ConsumedCapacity() {
    return this._ConsumedCapacity;
  }
  public Wrappers_Compile.Option<ItemCollectionMetrics> dtor_ItemCollectionMetrics() {
    return this._ItemCollectionMetrics;
  }
}
