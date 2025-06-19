// Class ScanInput
// Dafny class ScanInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ScanInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _AttributesToGet;
  public Wrappers_Compile.Option<java.lang.Integer> _Limit;
  public Wrappers_Compile.Option<Select> _Select;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>> _ScanFilter;
  public Wrappers_Compile.Option<ConditionalOperator> _ConditionalOperator;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _ExclusiveStartKey;
  public Wrappers_Compile.Option<ReturnConsumedCapacity> _ReturnConsumedCapacity;
  public Wrappers_Compile.Option<java.lang.Integer> _TotalSegments;
  public Wrappers_Compile.Option<java.lang.Integer> _Segment;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ProjectionExpression;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _FilterExpression;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> _ExpressionAttributeNames;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _ExpressionAttributeValues;
  public Wrappers_Compile.Option<Boolean> _ConsistentRead;
  public ScanInput (dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> AttributesToGet, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<Select> Select, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>> ScanFilter, Wrappers_Compile.Option<ConditionalOperator> ConditionalOperator, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExclusiveStartKey, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<java.lang.Integer> TotalSegments, Wrappers_Compile.Option<java.lang.Integer> Segment, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ProjectionExpression, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FilterExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExpressionAttributeValues, Wrappers_Compile.Option<Boolean> ConsistentRead) {
    this._TableName = TableName;
    this._IndexName = IndexName;
    this._AttributesToGet = AttributesToGet;
    this._Limit = Limit;
    this._Select = Select;
    this._ScanFilter = ScanFilter;
    this._ConditionalOperator = ConditionalOperator;
    this._ExclusiveStartKey = ExclusiveStartKey;
    this._ReturnConsumedCapacity = ReturnConsumedCapacity;
    this._TotalSegments = TotalSegments;
    this._Segment = Segment;
    this._ProjectionExpression = ProjectionExpression;
    this._FilterExpression = FilterExpression;
    this._ExpressionAttributeNames = ExpressionAttributeNames;
    this._ExpressionAttributeValues = ExpressionAttributeValues;
    this._ConsistentRead = ConsistentRead;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ScanInput o = (ScanInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._AttributesToGet, o._AttributesToGet) && java.util.Objects.equals(this._Limit, o._Limit) && java.util.Objects.equals(this._Select, o._Select) && java.util.Objects.equals(this._ScanFilter, o._ScanFilter) && java.util.Objects.equals(this._ConditionalOperator, o._ConditionalOperator) && java.util.Objects.equals(this._ExclusiveStartKey, o._ExclusiveStartKey) && java.util.Objects.equals(this._ReturnConsumedCapacity, o._ReturnConsumedCapacity) && java.util.Objects.equals(this._TotalSegments, o._TotalSegments) && java.util.Objects.equals(this._Segment, o._Segment) && java.util.Objects.equals(this._ProjectionExpression, o._ProjectionExpression) && java.util.Objects.equals(this._FilterExpression, o._FilterExpression) && java.util.Objects.equals(this._ExpressionAttributeNames, o._ExpressionAttributeNames) && java.util.Objects.equals(this._ExpressionAttributeValues, o._ExpressionAttributeValues) && java.util.Objects.equals(this._ConsistentRead, o._ConsistentRead);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttributesToGet);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Limit);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Select);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ScanFilter);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConditionalOperator);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExclusiveStartKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnConsumedCapacity);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TotalSegments);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Segment);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProjectionExpression);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._FilterExpression);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExpressionAttributeNames);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExpressionAttributeValues);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConsistentRead);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ScanInput.ScanInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._AttributesToGet));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Limit));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Select));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ScanFilter));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConditionalOperator));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExclusiveStartKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnConsumedCapacity));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TotalSegments));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Segment));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProjectionExpression));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._FilterExpression));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExpressionAttributeNames));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExpressionAttributeValues));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConsistentRead));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ScanInput> _TYPE = dafny.TypeDescriptor.<ScanInput>referenceWithInitializer(ScanInput.class, () -> ScanInput.Default());
  public static dafny.TypeDescriptor<ScanInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ScanInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ScanInput theDefault = ScanInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(IndexName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(AttributeNameList._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(PositiveIntegerObject._typeDescriptor()), Wrappers_Compile.Option.<Select>Default(Select._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Condition>_typeDescriptor(AttributeName._typeDescriptor(), Condition._typeDescriptor())), Wrappers_Compile.Option.<ConditionalOperator>Default(ConditionalOperator._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor())), Wrappers_Compile.Option.<ReturnConsumedCapacity>Default(ReturnConsumedCapacity._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(ScanTotalSegments._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(ScanSegment._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AttributeName._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AttributeValue._typeDescriptor())), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static ScanInput Default() {
    return theDefault;
  }
  public static ScanInput create(dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> AttributesToGet, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<Select> Select, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>> ScanFilter, Wrappers_Compile.Option<ConditionalOperator> ConditionalOperator, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExclusiveStartKey, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<java.lang.Integer> TotalSegments, Wrappers_Compile.Option<java.lang.Integer> Segment, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ProjectionExpression, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FilterExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExpressionAttributeValues, Wrappers_Compile.Option<Boolean> ConsistentRead) {
    return new ScanInput(TableName, IndexName, AttributesToGet, Limit, Select, ScanFilter, ConditionalOperator, ExclusiveStartKey, ReturnConsumedCapacity, TotalSegments, Segment, ProjectionExpression, FilterExpression, ExpressionAttributeNames, ExpressionAttributeValues, ConsistentRead);
  }
  public static ScanInput create_ScanInput(dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> AttributesToGet, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<Select> Select, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>> ScanFilter, Wrappers_Compile.Option<ConditionalOperator> ConditionalOperator, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExclusiveStartKey, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<java.lang.Integer> TotalSegments, Wrappers_Compile.Option<java.lang.Integer> Segment, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ProjectionExpression, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> FilterExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExpressionAttributeValues, Wrappers_Compile.Option<Boolean> ConsistentRead) {
    return create(TableName, IndexName, AttributesToGet, Limit, Select, ScanFilter, ConditionalOperator, ExclusiveStartKey, ReturnConsumedCapacity, TotalSegments, Segment, ProjectionExpression, FilterExpression, ExpressionAttributeNames, ExpressionAttributeValues, ConsistentRead);
  }
  public boolean is_ScanInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_AttributesToGet() {
    return this._AttributesToGet;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_Limit() {
    return this._Limit;
  }
  public Wrappers_Compile.Option<Select> dtor_Select() {
    return this._Select;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Condition>> dtor_ScanFilter() {
    return this._ScanFilter;
  }
  public Wrappers_Compile.Option<ConditionalOperator> dtor_ConditionalOperator() {
    return this._ConditionalOperator;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_ExclusiveStartKey() {
    return this._ExclusiveStartKey;
  }
  public Wrappers_Compile.Option<ReturnConsumedCapacity> dtor_ReturnConsumedCapacity() {
    return this._ReturnConsumedCapacity;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_TotalSegments() {
    return this._TotalSegments;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_Segment() {
    return this._Segment;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ProjectionExpression() {
    return this._ProjectionExpression;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_FilterExpression() {
    return this._FilterExpression;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> dtor_ExpressionAttributeNames() {
    return this._ExpressionAttributeNames;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_ExpressionAttributeValues() {
    return this._ExpressionAttributeValues;
  }
  public Wrappers_Compile.Option<Boolean> dtor_ConsistentRead() {
    return this._ConsistentRead;
  }
}
