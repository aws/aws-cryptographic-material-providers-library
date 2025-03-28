// Class DeleteItemInput
// Dafny class DeleteItemInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteItemInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> _Key;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends ExpectedAttributeValue>> _Expected;
  public Wrappers_Compile.Option<ConditionalOperator> _ConditionalOperator;
  public Wrappers_Compile.Option<ReturnValue> _ReturnValues;
  public Wrappers_Compile.Option<ReturnConsumedCapacity> _ReturnConsumedCapacity;
  public Wrappers_Compile.Option<ReturnItemCollectionMetrics> _ReturnItemCollectionMetrics;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ConditionExpression;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> _ExpressionAttributeNames;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _ExpressionAttributeValues;
  public Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> _ReturnValuesOnConditionCheckFailure;
  public DeleteItemInput (dafny.DafnySequence<? extends Character> TableName, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Key, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends ExpectedAttributeValue>> Expected, Wrappers_Compile.Option<ConditionalOperator> ConditionalOperator, Wrappers_Compile.Option<ReturnValue> ReturnValues, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<ReturnItemCollectionMetrics> ReturnItemCollectionMetrics, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ConditionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExpressionAttributeValues, Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> ReturnValuesOnConditionCheckFailure) {
    this._TableName = TableName;
    this._Key = Key;
    this._Expected = Expected;
    this._ConditionalOperator = ConditionalOperator;
    this._ReturnValues = ReturnValues;
    this._ReturnConsumedCapacity = ReturnConsumedCapacity;
    this._ReturnItemCollectionMetrics = ReturnItemCollectionMetrics;
    this._ConditionExpression = ConditionExpression;
    this._ExpressionAttributeNames = ExpressionAttributeNames;
    this._ExpressionAttributeValues = ExpressionAttributeValues;
    this._ReturnValuesOnConditionCheckFailure = ReturnValuesOnConditionCheckFailure;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteItemInput o = (DeleteItemInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._Key, o._Key) && java.util.Objects.equals(this._Expected, o._Expected) && java.util.Objects.equals(this._ConditionalOperator, o._ConditionalOperator) && java.util.Objects.equals(this._ReturnValues, o._ReturnValues) && java.util.Objects.equals(this._ReturnConsumedCapacity, o._ReturnConsumedCapacity) && java.util.Objects.equals(this._ReturnItemCollectionMetrics, o._ReturnItemCollectionMetrics) && java.util.Objects.equals(this._ConditionExpression, o._ConditionExpression) && java.util.Objects.equals(this._ExpressionAttributeNames, o._ExpressionAttributeNames) && java.util.Objects.equals(this._ExpressionAttributeValues, o._ExpressionAttributeValues) && java.util.Objects.equals(this._ReturnValuesOnConditionCheckFailure, o._ReturnValuesOnConditionCheckFailure);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Key);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Expected);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConditionalOperator);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnValues);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnConsumedCapacity);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnItemCollectionMetrics);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConditionExpression);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExpressionAttributeNames);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExpressionAttributeValues);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnValuesOnConditionCheckFailure);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DeleteItemInput.DeleteItemInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Key));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Expected));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConditionalOperator));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnValues));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnConsumedCapacity));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnItemCollectionMetrics));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConditionExpression));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExpressionAttributeNames));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExpressionAttributeValues));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnValuesOnConditionCheckFailure));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteItemInput> _TYPE = dafny.TypeDescriptor.<DeleteItemInput>referenceWithInitializer(DeleteItemInput.class, () -> DeleteItemInput.Default());
  public static dafny.TypeDescriptor<DeleteItemInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteItemInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteItemInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteItemInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,AttributeValue> empty(), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends ExpectedAttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, ExpectedAttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), ExpectedAttributeValue._typeDescriptor())), Wrappers_Compile.Option.<ConditionalOperator>Default(ConditionalOperator._typeDescriptor()), Wrappers_Compile.Option.<ReturnValue>Default(ReturnValue._typeDescriptor()), Wrappers_Compile.Option.<ReturnConsumedCapacity>Default(ReturnConsumedCapacity._typeDescriptor()), Wrappers_Compile.Option.<ReturnItemCollectionMetrics>Default(ReturnItemCollectionMetrics._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AttributeName._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AttributeValue._typeDescriptor())), Wrappers_Compile.Option.<ReturnValuesOnConditionCheckFailure>Default(ReturnValuesOnConditionCheckFailure._typeDescriptor()));
  public static DeleteItemInput Default() {
    return theDefault;
  }
  public static DeleteItemInput create(dafny.DafnySequence<? extends Character> TableName, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Key, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends ExpectedAttributeValue>> Expected, Wrappers_Compile.Option<ConditionalOperator> ConditionalOperator, Wrappers_Compile.Option<ReturnValue> ReturnValues, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<ReturnItemCollectionMetrics> ReturnItemCollectionMetrics, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ConditionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExpressionAttributeValues, Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> ReturnValuesOnConditionCheckFailure) {
    return new DeleteItemInput(TableName, Key, Expected, ConditionalOperator, ReturnValues, ReturnConsumedCapacity, ReturnItemCollectionMetrics, ConditionExpression, ExpressionAttributeNames, ExpressionAttributeValues, ReturnValuesOnConditionCheckFailure);
  }
  public static DeleteItemInput create_DeleteItemInput(dafny.DafnySequence<? extends Character> TableName, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Key, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends ExpectedAttributeValue>> Expected, Wrappers_Compile.Option<ConditionalOperator> ConditionalOperator, Wrappers_Compile.Option<ReturnValue> ReturnValues, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<ReturnItemCollectionMetrics> ReturnItemCollectionMetrics, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ConditionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExpressionAttributeValues, Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> ReturnValuesOnConditionCheckFailure) {
    return create(TableName, Key, Expected, ConditionalOperator, ReturnValues, ReturnConsumedCapacity, ReturnItemCollectionMetrics, ConditionExpression, ExpressionAttributeNames, ExpressionAttributeValues, ReturnValuesOnConditionCheckFailure);
  }
  public boolean is_DeleteItemInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> dtor_Key() {
    return this._Key;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends ExpectedAttributeValue>> dtor_Expected() {
    return this._Expected;
  }
  public Wrappers_Compile.Option<ConditionalOperator> dtor_ConditionalOperator() {
    return this._ConditionalOperator;
  }
  public Wrappers_Compile.Option<ReturnValue> dtor_ReturnValues() {
    return this._ReturnValues;
  }
  public Wrappers_Compile.Option<ReturnConsumedCapacity> dtor_ReturnConsumedCapacity() {
    return this._ReturnConsumedCapacity;
  }
  public Wrappers_Compile.Option<ReturnItemCollectionMetrics> dtor_ReturnItemCollectionMetrics() {
    return this._ReturnItemCollectionMetrics;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ConditionExpression() {
    return this._ConditionExpression;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> dtor_ExpressionAttributeNames() {
    return this._ExpressionAttributeNames;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_ExpressionAttributeValues() {
    return this._ExpressionAttributeValues;
  }
  public Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> dtor_ReturnValuesOnConditionCheckFailure() {
    return this._ReturnValuesOnConditionCheckFailure;
  }
}
