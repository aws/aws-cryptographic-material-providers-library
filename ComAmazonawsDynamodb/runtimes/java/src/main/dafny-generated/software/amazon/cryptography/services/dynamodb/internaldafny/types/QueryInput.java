// Class QueryInput
// Dafny class QueryInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class QueryInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexName;
  public Wrappers_Compile.Option<Select> _Select;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _AttributesToGet;
  public Wrappers_Compile.Option<java.lang.Integer> _Limit;
  public Wrappers_Compile.Option<Boolean> _ConsistentRead;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>> _KeyConditions;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>> _QueryFilter;
  public Wrappers_Compile.Option<ConditionalOperator> _ConditionalOperator;
  public Wrappers_Compile.Option<Boolean> _ScanIndexForward;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _ExclusiveStartKey;
  public Wrappers_Compile.Option<ReturnConsumedCapacity> _ReturnConsumedCapacity;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ProjectionExpression;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _FilterExpression;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyConditionExpression;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> _ExpressionAttributeNames;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _ExpressionAttributeValues;
  public QueryInput (dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<Select> Select, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> AttributesToGet, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<Boolean> ConsistentRead, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>> KeyConditions, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>> QueryFilter, Wrappers_Compile.Option<ConditionalOperator> ConditionalOperator, Wrappers_Compile.Option<Boolean> ScanIndexForward, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExclusiveStartKey, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ProjectionExpression, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FilterExpression, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyConditionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExpressionAttributeValues) {
    this._TableName = TableName;
    this._IndexName = IndexName;
    this._Select = Select;
    this._AttributesToGet = AttributesToGet;
    this._Limit = Limit;
    this._ConsistentRead = ConsistentRead;
    this._KeyConditions = KeyConditions;
    this._QueryFilter = QueryFilter;
    this._ConditionalOperator = ConditionalOperator;
    this._ScanIndexForward = ScanIndexForward;
    this._ExclusiveStartKey = ExclusiveStartKey;
    this._ReturnConsumedCapacity = ReturnConsumedCapacity;
    this._ProjectionExpression = ProjectionExpression;
    this._FilterExpression = FilterExpression;
    this._KeyConditionExpression = KeyConditionExpression;
    this._ExpressionAttributeNames = ExpressionAttributeNames;
    this._ExpressionAttributeValues = ExpressionAttributeValues;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    QueryInput o = (QueryInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._Select, o._Select) && java.util.Objects.equals(this._AttributesToGet, o._AttributesToGet) && java.util.Objects.equals(this._Limit, o._Limit) && java.util.Objects.equals(this._ConsistentRead, o._ConsistentRead) && java.util.Objects.equals(this._KeyConditions, o._KeyConditions) && java.util.Objects.equals(this._QueryFilter, o._QueryFilter) && java.util.Objects.equals(this._ConditionalOperator, o._ConditionalOperator) && java.util.Objects.equals(this._ScanIndexForward, o._ScanIndexForward) && java.util.Objects.equals(this._ExclusiveStartKey, o._ExclusiveStartKey) && java.util.Objects.equals(this._ReturnConsumedCapacity, o._ReturnConsumedCapacity) && java.util.Objects.equals(this._ProjectionExpression, o._ProjectionExpression) && java.util.Objects.equals(this._FilterExpression, o._FilterExpression) && java.util.Objects.equals(this._KeyConditionExpression, o._KeyConditionExpression) && java.util.Objects.equals(this._ExpressionAttributeNames, o._ExpressionAttributeNames) && java.util.Objects.equals(this._ExpressionAttributeValues, o._ExpressionAttributeValues);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Select);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttributesToGet);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Limit);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConsistentRead);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyConditions);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._QueryFilter);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConditionalOperator);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ScanIndexForward);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExclusiveStartKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnConsumedCapacity);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProjectionExpression);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._FilterExpression);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyConditionExpression);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExpressionAttributeNames);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExpressionAttributeValues);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.QueryInput.QueryInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Select));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._AttributesToGet));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Limit));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConsistentRead));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyConditions));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._QueryFilter));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConditionalOperator));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ScanIndexForward));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExclusiveStartKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnConsumedCapacity));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProjectionExpression));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._FilterExpression));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyConditionExpression));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExpressionAttributeNames));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExpressionAttributeValues));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<QueryInput> _TYPE = dafny.TypeDescriptor.<QueryInput>referenceWithInitializer(QueryInput.class, () -> QueryInput.Default());
  public static dafny.TypeDescriptor<QueryInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<QueryInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final QueryInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.QueryInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(IndexName._typeDescriptor()), Wrappers_Compile.Option.<Select>Default(Select._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(AttributeNameList._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(PositiveIntegerObject._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Condition>_typeDescriptor(AttributeName._typeDescriptor(), Condition._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Condition>_typeDescriptor(AttributeName._typeDescriptor(), Condition._typeDescriptor())), Wrappers_Compile.Option.<ConditionalOperator>Default(ConditionalOperator._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor())), Wrappers_Compile.Option.<ReturnConsumedCapacity>Default(ReturnConsumedCapacity._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AttributeName._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AttributeValue._typeDescriptor())));
  public static QueryInput Default() {
    return theDefault;
  }
  public static QueryInput create(dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<Select> Select, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> AttributesToGet, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<Boolean> ConsistentRead, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>> KeyConditions, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>> QueryFilter, Wrappers_Compile.Option<ConditionalOperator> ConditionalOperator, Wrappers_Compile.Option<Boolean> ScanIndexForward, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExclusiveStartKey, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ProjectionExpression, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FilterExpression, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyConditionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExpressionAttributeValues) {
    return new QueryInput(TableName, IndexName, Select, AttributesToGet, Limit, ConsistentRead, KeyConditions, QueryFilter, ConditionalOperator, ScanIndexForward, ExclusiveStartKey, ReturnConsumedCapacity, ProjectionExpression, FilterExpression, KeyConditionExpression, ExpressionAttributeNames, ExpressionAttributeValues);
  }
  public static QueryInput create_QueryInput(dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<Select> Select, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> AttributesToGet, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<Boolean> ConsistentRead, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>> KeyConditions, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>> QueryFilter, Wrappers_Compile.Option<ConditionalOperator> ConditionalOperator, Wrappers_Compile.Option<Boolean> ScanIndexForward, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExclusiveStartKey, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ProjectionExpression, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FilterExpression, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyConditionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExpressionAttributeValues) {
    return create(TableName, IndexName, Select, AttributesToGet, Limit, ConsistentRead, KeyConditions, QueryFilter, ConditionalOperator, ScanIndexForward, ExclusiveStartKey, ReturnConsumedCapacity, ProjectionExpression, FilterExpression, KeyConditionExpression, ExpressionAttributeNames, ExpressionAttributeValues);
  }
  public boolean is_QueryInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<Select> dtor_Select() {
    return this._Select;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_AttributesToGet() {
    return this._AttributesToGet;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_Limit() {
    return this._Limit;
  }
  public Wrappers_Compile.Option<Boolean> dtor_ConsistentRead() {
    return this._ConsistentRead;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>> dtor_KeyConditions() {
    return this._KeyConditions;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>> dtor_QueryFilter() {
    return this._QueryFilter;
  }
  public Wrappers_Compile.Option<ConditionalOperator> dtor_ConditionalOperator() {
    return this._ConditionalOperator;
  }
  public Wrappers_Compile.Option<Boolean> dtor_ScanIndexForward() {
    return this._ScanIndexForward;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_ExclusiveStartKey() {
    return this._ExclusiveStartKey;
  }
  public Wrappers_Compile.Option<ReturnConsumedCapacity> dtor_ReturnConsumedCapacity() {
    return this._ReturnConsumedCapacity;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ProjectionExpression() {
    return this._ProjectionExpression;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_FilterExpression() {
    return this._FilterExpression;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyConditionExpression() {
    return this._KeyConditionExpression;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> dtor_ExpressionAttributeNames() {
    return this._ExpressionAttributeNames;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_ExpressionAttributeValues() {
    return this._ExpressionAttributeValues;
  }
}
