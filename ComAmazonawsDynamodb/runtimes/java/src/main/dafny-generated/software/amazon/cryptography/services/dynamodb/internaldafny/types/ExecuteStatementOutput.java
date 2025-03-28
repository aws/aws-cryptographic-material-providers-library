// Class ExecuteStatementOutput
// Dafny class ExecuteStatementOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ExecuteStatementOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>> _Items;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextToken;
  public Wrappers_Compile.Option<ConsumedCapacity> _ConsumedCapacity;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _LastEvaluatedKey;
  public ExecuteStatementOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>> Items, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken, Wrappers_Compile.Option<ConsumedCapacity> ConsumedCapacity, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> LastEvaluatedKey) {
    this._Items = Items;
    this._NextToken = NextToken;
    this._ConsumedCapacity = ConsumedCapacity;
    this._LastEvaluatedKey = LastEvaluatedKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ExecuteStatementOutput o = (ExecuteStatementOutput)other;
    return true && java.util.Objects.equals(this._Items, o._Items) && java.util.Objects.equals(this._NextToken, o._NextToken) && java.util.Objects.equals(this._ConsumedCapacity, o._ConsumedCapacity) && java.util.Objects.equals(this._LastEvaluatedKey, o._LastEvaluatedKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Items);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextToken);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConsumedCapacity);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LastEvaluatedKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ExecuteStatementOutput.ExecuteStatementOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Items));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextToken));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConsumedCapacity));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LastEvaluatedKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ExecuteStatementOutput> _TYPE = dafny.TypeDescriptor.<ExecuteStatementOutput>referenceWithInitializer(ExecuteStatementOutput.class, () -> ExecuteStatementOutput.Default());
  public static dafny.TypeDescriptor<ExecuteStatementOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ExecuteStatementOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ExecuteStatementOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ExecuteStatementOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>>Default(dafny.DafnySequence.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>_typeDescriptor(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor()))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PartiQLNextToken._typeDescriptor()), Wrappers_Compile.Option.<ConsumedCapacity>Default(ConsumedCapacity._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor())));
  public static ExecuteStatementOutput Default() {
    return theDefault;
  }
  public static ExecuteStatementOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>> Items, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken, Wrappers_Compile.Option<ConsumedCapacity> ConsumedCapacity, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> LastEvaluatedKey) {
    return new ExecuteStatementOutput(Items, NextToken, ConsumedCapacity, LastEvaluatedKey);
  }
  public static ExecuteStatementOutput create_ExecuteStatementOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>> Items, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken, Wrappers_Compile.Option<ConsumedCapacity> ConsumedCapacity, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> LastEvaluatedKey) {
    return create(Items, NextToken, ConsumedCapacity, LastEvaluatedKey);
  }
  public boolean is_ExecuteStatementOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>> dtor_Items() {
    return this._Items;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextToken() {
    return this._NextToken;
  }
  public Wrappers_Compile.Option<ConsumedCapacity> dtor_ConsumedCapacity() {
    return this._ConsumedCapacity;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_LastEvaluatedKey() {
    return this._LastEvaluatedKey;
  }
}
