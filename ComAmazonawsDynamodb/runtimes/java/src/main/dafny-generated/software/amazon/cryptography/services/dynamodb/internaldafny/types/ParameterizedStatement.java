// Class ParameterizedStatement
// Dafny class ParameterizedStatement compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ParameterizedStatement {
  public dafny.DafnySequence<? extends Character> _Statement;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> _Parameters;
  public Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> _ReturnValuesOnConditionCheckFailure;
  public ParameterizedStatement (dafny.DafnySequence<? extends Character> Statement, Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> Parameters, Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> ReturnValuesOnConditionCheckFailure) {
    this._Statement = Statement;
    this._Parameters = Parameters;
    this._ReturnValuesOnConditionCheckFailure = ReturnValuesOnConditionCheckFailure;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ParameterizedStatement o = (ParameterizedStatement)other;
    return true && java.util.Objects.equals(this._Statement, o._Statement) && java.util.Objects.equals(this._Parameters, o._Parameters) && java.util.Objects.equals(this._ReturnValuesOnConditionCheckFailure, o._ReturnValuesOnConditionCheckFailure);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Statement);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Parameters);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnValuesOnConditionCheckFailure);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ParameterizedStatement.ParameterizedStatement");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Statement));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Parameters));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnValuesOnConditionCheckFailure));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ParameterizedStatement> _TYPE = dafny.TypeDescriptor.<ParameterizedStatement>referenceWithInitializer(ParameterizedStatement.class, () -> ParameterizedStatement.Default());
  public static dafny.TypeDescriptor<ParameterizedStatement> _typeDescriptor() {
    return (dafny.TypeDescriptor<ParameterizedStatement>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ParameterizedStatement theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ParameterizedStatement.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends AttributeValue>>Default(PreparedStatementParameters._typeDescriptor()), Wrappers_Compile.Option.<ReturnValuesOnConditionCheckFailure>Default(ReturnValuesOnConditionCheckFailure._typeDescriptor()));
  public static ParameterizedStatement Default() {
    return theDefault;
  }
  public static ParameterizedStatement create(dafny.DafnySequence<? extends Character> Statement, Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> Parameters, Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> ReturnValuesOnConditionCheckFailure) {
    return new ParameterizedStatement(Statement, Parameters, ReturnValuesOnConditionCheckFailure);
  }
  public static ParameterizedStatement create_ParameterizedStatement(dafny.DafnySequence<? extends Character> Statement, Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> Parameters, Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> ReturnValuesOnConditionCheckFailure) {
    return create(Statement, Parameters, ReturnValuesOnConditionCheckFailure);
  }
  public boolean is_ParameterizedStatement() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_Statement() {
    return this._Statement;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeValue>> dtor_Parameters() {
    return this._Parameters;
  }
  public Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> dtor_ReturnValuesOnConditionCheckFailure() {
    return this._ReturnValuesOnConditionCheckFailure;
  }
}
