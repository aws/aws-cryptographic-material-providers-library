// Class ExecuteTransactionInput
// Dafny class ExecuteTransactionInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ExecuteTransactionInput {
  public dafny.DafnySequence<? extends ParameterizedStatement> _TransactStatements;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ClientRequestToken;
  public Wrappers_Compile.Option<ReturnConsumedCapacity> _ReturnConsumedCapacity;
  public ExecuteTransactionInput (dafny.DafnySequence<? extends ParameterizedStatement> TransactStatements, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientRequestToken, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity) {
    this._TransactStatements = TransactStatements;
    this._ClientRequestToken = ClientRequestToken;
    this._ReturnConsumedCapacity = ReturnConsumedCapacity;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ExecuteTransactionInput o = (ExecuteTransactionInput)other;
    return true && java.util.Objects.equals(this._TransactStatements, o._TransactStatements) && java.util.Objects.equals(this._ClientRequestToken, o._ClientRequestToken) && java.util.Objects.equals(this._ReturnConsumedCapacity, o._ReturnConsumedCapacity);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TransactStatements);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ClientRequestToken);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnConsumedCapacity);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ExecuteTransactionInput.ExecuteTransactionInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TransactStatements));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ClientRequestToken));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnConsumedCapacity));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ExecuteTransactionInput> _TYPE = dafny.TypeDescriptor.<ExecuteTransactionInput>referenceWithInitializer(ExecuteTransactionInput.class, () -> ExecuteTransactionInput.Default());
  public static dafny.TypeDescriptor<ExecuteTransactionInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ExecuteTransactionInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ExecuteTransactionInput theDefault = ExecuteTransactionInput.create(dafny.DafnySequence.<ParameterizedStatement> empty(ParameterizedStatement._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(ClientRequestToken._typeDescriptor()), Wrappers_Compile.Option.<ReturnConsumedCapacity>Default(ReturnConsumedCapacity._typeDescriptor()));
  public static ExecuteTransactionInput Default() {
    return theDefault;
  }
  public static ExecuteTransactionInput create(dafny.DafnySequence<? extends ParameterizedStatement> TransactStatements, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientRequestToken, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity) {
    return new ExecuteTransactionInput(TransactStatements, ClientRequestToken, ReturnConsumedCapacity);
  }
  public static ExecuteTransactionInput create_ExecuteTransactionInput(dafny.DafnySequence<? extends ParameterizedStatement> TransactStatements, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ClientRequestToken, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity) {
    return create(TransactStatements, ClientRequestToken, ReturnConsumedCapacity);
  }
  public boolean is_ExecuteTransactionInput() { return true; }
  public dafny.DafnySequence<? extends ParameterizedStatement> dtor_TransactStatements() {
    return this._TransactStatements;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ClientRequestToken() {
    return this._ClientRequestToken;
  }
  public Wrappers_Compile.Option<ReturnConsumedCapacity> dtor_ReturnConsumedCapacity() {
    return this._ReturnConsumedCapacity;
  }
}
