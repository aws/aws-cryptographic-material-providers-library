// Class TransactWriteItemsInput
// Dafny class TransactWriteItemsInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class TransactWriteItemsInput {
  public dafny.DafnySequence<? extends TransactWriteItem> _TransactItems;
  public Wrappers_Compile.Option<ReturnConsumedCapacity> _ReturnConsumedCapacity;
  public Wrappers_Compile.Option<ReturnItemCollectionMetrics> _ReturnItemCollectionMetrics;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ClientRequestToken;
  public TransactWriteItemsInput (dafny.DafnySequence<? extends TransactWriteItem> TransactItems, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<ReturnItemCollectionMetrics> ReturnItemCollectionMetrics, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientRequestToken) {
    this._TransactItems = TransactItems;
    this._ReturnConsumedCapacity = ReturnConsumedCapacity;
    this._ReturnItemCollectionMetrics = ReturnItemCollectionMetrics;
    this._ClientRequestToken = ClientRequestToken;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TransactWriteItemsInput o = (TransactWriteItemsInput)other;
    return true && java.util.Objects.equals(this._TransactItems, o._TransactItems) && java.util.Objects.equals(this._ReturnConsumedCapacity, o._ReturnConsumedCapacity) && java.util.Objects.equals(this._ReturnItemCollectionMetrics, o._ReturnItemCollectionMetrics) && java.util.Objects.equals(this._ClientRequestToken, o._ClientRequestToken);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TransactItems);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnConsumedCapacity);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnItemCollectionMetrics);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ClientRequestToken);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TransactWriteItemsInput.TransactWriteItemsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TransactItems));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnConsumedCapacity));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnItemCollectionMetrics));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ClientRequestToken));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TransactWriteItemsInput> _TYPE = dafny.TypeDescriptor.<TransactWriteItemsInput>referenceWithInitializer(TransactWriteItemsInput.class, () -> TransactWriteItemsInput.Default());
  public static dafny.TypeDescriptor<TransactWriteItemsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<TransactWriteItemsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TransactWriteItemsInput theDefault = TransactWriteItemsInput.create(dafny.DafnySequence.<TransactWriteItem> empty(TransactWriteItem._typeDescriptor()), Wrappers_Compile.Option.<ReturnConsumedCapacity>Default(ReturnConsumedCapacity._typeDescriptor()), Wrappers_Compile.Option.<ReturnItemCollectionMetrics>Default(ReturnItemCollectionMetrics._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(ClientRequestToken._typeDescriptor()));
  public static TransactWriteItemsInput Default() {
    return theDefault;
  }
  public static TransactWriteItemsInput create(dafny.DafnySequence<? extends TransactWriteItem> TransactItems, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<ReturnItemCollectionMetrics> ReturnItemCollectionMetrics, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientRequestToken) {
    return new TransactWriteItemsInput(TransactItems, ReturnConsumedCapacity, ReturnItemCollectionMetrics, ClientRequestToken);
  }
  public static TransactWriteItemsInput create_TransactWriteItemsInput(dafny.DafnySequence<? extends TransactWriteItem> TransactItems, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<ReturnItemCollectionMetrics> ReturnItemCollectionMetrics, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientRequestToken) {
    return create(TransactItems, ReturnConsumedCapacity, ReturnItemCollectionMetrics, ClientRequestToken);
  }
  public boolean is_TransactWriteItemsInput() { return true; }
  public dafny.DafnySequence<? extends TransactWriteItem> dtor_TransactItems() {
    return this._TransactItems;
  }
  public Wrappers_Compile.Option<ReturnConsumedCapacity> dtor_ReturnConsumedCapacity() {
    return this._ReturnConsumedCapacity;
  }
  public Wrappers_Compile.Option<ReturnItemCollectionMetrics> dtor_ReturnItemCollectionMetrics() {
    return this._ReturnItemCollectionMetrics;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ClientRequestToken() {
    return this._ClientRequestToken;
  }
}
