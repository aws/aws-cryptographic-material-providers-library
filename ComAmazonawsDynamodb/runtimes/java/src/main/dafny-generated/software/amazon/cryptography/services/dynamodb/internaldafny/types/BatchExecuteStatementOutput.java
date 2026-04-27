// Class BatchExecuteStatementOutput
// Dafny class BatchExecuteStatementOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BatchExecuteStatementOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends BatchStatementResponse>> _Responses;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> _ConsumedCapacity;
  public BatchExecuteStatementOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends BatchStatementResponse>> Responses, Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity) {
    this._Responses = Responses;
    this._ConsumedCapacity = ConsumedCapacity;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchExecuteStatementOutput o = (BatchExecuteStatementOutput)other;
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
    s.append("ComAmazonawsDynamodbTypes.BatchExecuteStatementOutput.BatchExecuteStatementOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Responses));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConsumedCapacity));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<BatchExecuteStatementOutput> _TYPE = dafny.TypeDescriptor.<BatchExecuteStatementOutput>referenceWithInitializer(BatchExecuteStatementOutput.class, () -> BatchExecuteStatementOutput.Default());
  public static dafny.TypeDescriptor<BatchExecuteStatementOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<BatchExecuteStatementOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BatchExecuteStatementOutput theDefault = BatchExecuteStatementOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends BatchStatementResponse>>Default(dafny.DafnySequence.<BatchStatementResponse>_typeDescriptor(BatchStatementResponse._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ConsumedCapacity>>Default(dafny.DafnySequence.<ConsumedCapacity>_typeDescriptor(ConsumedCapacity._typeDescriptor())));
  public static BatchExecuteStatementOutput Default() {
    return theDefault;
  }
  public static BatchExecuteStatementOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends BatchStatementResponse>> Responses, Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity) {
    return new BatchExecuteStatementOutput(Responses, ConsumedCapacity);
  }
  public static BatchExecuteStatementOutput create_BatchExecuteStatementOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends BatchStatementResponse>> Responses, Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> ConsumedCapacity) {
    return create(Responses, ConsumedCapacity);
  }
  public boolean is_BatchExecuteStatementOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends BatchStatementResponse>> dtor_Responses() {
    return this._Responses;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ConsumedCapacity>> dtor_ConsumedCapacity() {
    return this._ConsumedCapacity;
  }
}
