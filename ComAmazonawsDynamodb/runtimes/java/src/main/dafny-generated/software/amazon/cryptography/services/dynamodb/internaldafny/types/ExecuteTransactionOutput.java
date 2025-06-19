// Class ExecuteTransactionOutput
// Dafny class ExecuteTransactionOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ExecuteTransactionOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ItemResponse>> _Responses;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> _ConsumedCapacity;
  public ExecuteTransactionOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends ItemResponse>> Responses, Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity) {
    this._Responses = Responses;
    this._ConsumedCapacity = ConsumedCapacity;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ExecuteTransactionOutput o = (ExecuteTransactionOutput)other;
    return true && java.util.Objects.equals(this._Responses, o._Responses) && java.util.Objects.equals(this._ConsumedCapacity, o._ConsumedCapacity);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Responses);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConsumedCapacity);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ExecuteTransactionOutput.ExecuteTransactionOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Responses));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConsumedCapacity));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ExecuteTransactionOutput> _TYPE = dafny.TypeDescriptor.<ExecuteTransactionOutput>referenceWithInitializer(ExecuteTransactionOutput.class, () -> ExecuteTransactionOutput.Default());
  public static dafny.TypeDescriptor<ExecuteTransactionOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ExecuteTransactionOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ExecuteTransactionOutput theDefault = ExecuteTransactionOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends ItemResponse>>Default(ItemResponseList._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ConsumedCapacity>>Default(dafny.DafnySequence.<ConsumedCapacity>_typeDescriptor(ConsumedCapacity._typeDescriptor())));
  public static ExecuteTransactionOutput Default() {
    return theDefault;
  }
  public static ExecuteTransactionOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends ItemResponse>> Responses, Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity) {
    return new ExecuteTransactionOutput(Responses, ConsumedCapacity);
  }
  public static ExecuteTransactionOutput create_ExecuteTransactionOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends ItemResponse>> Responses, Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity) {
    return create(Responses, ConsumedCapacity);
  }
  public boolean is_ExecuteTransactionOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ItemResponse>> dtor_Responses() {
    return this._Responses;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> dtor_ConsumedCapacity() {
    return this._ConsumedCapacity;
  }
}
