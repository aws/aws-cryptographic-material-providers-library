// Class BatchExecuteStatementInput
// Dafny class BatchExecuteStatementInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BatchExecuteStatementInput {
  public dafny.DafnySequence<? extends BatchStatementRequest> _Statements;
  public Wrappers_Compile.Option<ReturnConsumedCapacity> _ReturnConsumedCapacity;
  public BatchExecuteStatementInput (dafny.DafnySequence<? extends BatchStatementRequest> Statements, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity) {
    this._Statements = Statements;
    this._ReturnConsumedCapacity = ReturnConsumedCapacity;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BatchExecuteStatementInput o = (BatchExecuteStatementInput)other;
    return true && java.util.Objects.equals(this._Statements, o._Statements) && java.util.Objects.equals(this._ReturnConsumedCapacity, o._ReturnConsumedCapacity);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Statements);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnConsumedCapacity);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.BatchExecuteStatementInput.BatchExecuteStatementInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Statements));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnConsumedCapacity));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<BatchExecuteStatementInput> _TYPE = dafny.TypeDescriptor.<BatchExecuteStatementInput>referenceWithInitializer(BatchExecuteStatementInput.class, () -> BatchExecuteStatementInput.Default());
  public static dafny.TypeDescriptor<BatchExecuteStatementInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<BatchExecuteStatementInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BatchExecuteStatementInput theDefault = BatchExecuteStatementInput.create(dafny.DafnySequence.<BatchStatementRequest> empty(BatchStatementRequest._typeDescriptor()), Wrappers_Compile.Option.<ReturnConsumedCapacity>Default(ReturnConsumedCapacity._typeDescriptor()));
  public static BatchExecuteStatementInput Default() {
    return theDefault;
  }
  public static BatchExecuteStatementInput create(dafny.DafnySequence<? extends BatchStatementRequest> Statements, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity) {
    return new BatchExecuteStatementInput(Statements, ReturnConsumedCapacity);
  }
  public static BatchExecuteStatementInput create_BatchExecuteStatementInput(dafny.DafnySequence<? extends BatchStatementRequest> Statements, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity) {
    return create(Statements, ReturnConsumedCapacity);
  }
  public boolean is_BatchExecuteStatementInput() { return true; }
  public dafny.DafnySequence<? extends BatchStatementRequest> dtor_Statements() {
    return this._Statements;
  }
  public Wrappers_Compile.Option<ReturnConsumedCapacity> dtor_ReturnConsumedCapacity() {
    return this._ReturnConsumedCapacity;
  }
}
