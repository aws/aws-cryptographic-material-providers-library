// Class ExecuteStatementInput
// Dafny class ExecuteStatementInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ExecuteStatementInput {
  public dafny.DafnySequence<? extends Character> _Statement;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> _Parameters;
  public Wrappers_Compile.Option<Boolean> _ConsistentRead;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextToken;
  public Wrappers_Compile.Option<ReturnConsumedCapacity> _ReturnConsumedCapacity;
  public Wrappers_Compile.Option<java.lang.Integer> _Limit;
  public Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> _ReturnValuesOnConditionCheckFailure;
  public ExecuteStatementInput (dafny.DafnySequence<? extends Character> Statement, Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> Parameters, Wrappers_Compile.Option<Boolean> ConsistentRead, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> ReturnValuesOnConditionCheckFailure) {
    this._Statement = Statement;
    this._Parameters = Parameters;
    this._ConsistentRead = ConsistentRead;
    this._NextToken = NextToken;
    this._ReturnConsumedCapacity = ReturnConsumedCapacity;
    this._Limit = Limit;
    this._ReturnValuesOnConditionCheckFailure = ReturnValuesOnConditionCheckFailure;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ExecuteStatementInput o = (ExecuteStatementInput)other;
    return true && java.util.Objects.equals(this._Statement, o._Statement) && java.util.Objects.equals(this._Parameters, o._Parameters) && java.util.Objects.equals(this._ConsistentRead, o._ConsistentRead) && java.util.Objects.equals(this._NextToken, o._NextToken) && java.util.Objects.equals(this._ReturnConsumedCapacity, o._ReturnConsumedCapacity) && java.util.Objects.equals(this._Limit, o._Limit) && java.util.Objects.equals(this._ReturnValuesOnConditionCheckFailure, o._ReturnValuesOnConditionCheckFailure);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Statement);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Parameters);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConsistentRead);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextToken);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnConsumedCapacity);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Limit);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnValuesOnConditionCheckFailure);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ExecuteStatementInput.ExecuteStatementInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Statement));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Parameters));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConsistentRead));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextToken));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnConsumedCapacity));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Limit));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnValuesOnConditionCheckFailure));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ExecuteStatementInput> _TYPE = dafny.TypeDescriptor.<ExecuteStatementInput>referenceWithInitializer(ExecuteStatementInput.class, () -> ExecuteStatementInput.Default());
  public static dafny.TypeDescriptor<ExecuteStatementInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ExecuteStatementInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ExecuteStatementInput theDefault = ExecuteStatementInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends AttributeValue>>Default(PreparedStatementParameters._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PartiQLNextToken._typeDescriptor()), Wrappers_Compile.Option.<ReturnConsumedCapacity>Default(ReturnConsumedCapacity._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(PositiveIntegerObject._typeDescriptor()), Wrappers_Compile.Option.<ReturnValuesOnConditionCheckFailure>Default(ReturnValuesOnConditionCheckFailure._typeDescriptor()));
  public static ExecuteStatementInput Default() {
    return theDefault;
  }
  public static ExecuteStatementInput create(dafny.DafnySequence<? extends Character> Statement, Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> Parameters, Wrappers_Compile.Option<Boolean> ConsistentRead, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> ReturnValuesOnConditionCheckFailure) {
    return new ExecuteStatementInput(Statement, Parameters, ConsistentRead, NextToken, ReturnConsumedCapacity, Limit, ReturnValuesOnConditionCheckFailure);
  }
  public static ExecuteStatementInput create_ExecuteStatementInput(dafny.DafnySequence<? extends Character> Statement, Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> Parameters, Wrappers_Compile.Option<Boolean> ConsistentRead, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> ReturnValuesOnConditionCheckFailure) {
    return create(Statement, Parameters, ConsistentRead, NextToken, ReturnConsumedCapacity, Limit, ReturnValuesOnConditionCheckFailure);
  }
  public boolean is_ExecuteStatementInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_Statement() {
    return this._Statement;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> dtor_Parameters() {
    return this._Parameters;
  }
  public Wrappers_Compile.Option<Boolean> dtor_ConsistentRead() {
    return this._ConsistentRead;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextToken() {
    return this._NextToken;
  }
  public Wrappers_Compile.Option<ReturnConsumedCapacity> dtor_ReturnConsumedCapacity() {
    return this._ReturnConsumedCapacity;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_Limit() {
    return this._Limit;
  }
  public Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> dtor_ReturnValuesOnConditionCheckFailure() {
    return this._ReturnValuesOnConditionCheckFailure;
  }
}
