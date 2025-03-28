// Class TransactGetItemsOutput
// Dafny class TransactGetItemsOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class TransactGetItemsOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> _ConsumedCapacity;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ItemResponse>> _Responses;
  public TransactGetItemsOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity, Wrappers_Compile.Option<dafny.DafnySequence<? extends ItemResponse>> Responses) {
    this._ConsumedCapacity = ConsumedCapacity;
    this._Responses = Responses;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TransactGetItemsOutput o = (TransactGetItemsOutput)other;
    return true && java.util.Objects.equals(this._ConsumedCapacity, o._ConsumedCapacity) && java.util.Objects.equals(this._Responses, o._Responses);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConsumedCapacity);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Responses);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TransactGetItemsOutput.TransactGetItemsOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ConsumedCapacity));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Responses));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TransactGetItemsOutput> _TYPE = dafny.TypeDescriptor.<TransactGetItemsOutput>referenceWithInitializer(TransactGetItemsOutput.class, () -> TransactGetItemsOutput.Default());
  public static dafny.TypeDescriptor<TransactGetItemsOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<TransactGetItemsOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TransactGetItemsOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactGetItemsOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends ConsumedCapacity>>Default(dafny.DafnySequence.<ConsumedCapacity>_typeDescriptor(ConsumedCapacity._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ItemResponse>>Default(ItemResponseList._typeDescriptor()));
  public static TransactGetItemsOutput Default() {
    return theDefault;
  }
  public static TransactGetItemsOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity, Wrappers_Compile.Option<dafny.DafnySequence<? extends ItemResponse>> Responses) {
    return new TransactGetItemsOutput(ConsumedCapacity, Responses);
  }
  public static TransactGetItemsOutput create_TransactGetItemsOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity, Wrappers_Compile.Option<dafny.DafnySequence<? extends ItemResponse>> Responses) {
    return create(ConsumedCapacity, Responses);
  }
  public boolean is_TransactGetItemsOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> dtor_ConsumedCapacity() {
    return this._ConsumedCapacity;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ItemResponse>> dtor_Responses() {
    return this._Responses;
  }
}
