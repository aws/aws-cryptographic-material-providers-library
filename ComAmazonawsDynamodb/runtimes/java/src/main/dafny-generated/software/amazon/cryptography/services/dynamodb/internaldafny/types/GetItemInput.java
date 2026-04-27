// Class GetItemInput
// Dafny class GetItemInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetItemInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> _Key;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _AttributesToGet;
  public Wrappers_Compile.Option<Boolean> _ConsistentRead;
  public Wrappers_Compile.Option<ReturnConsumedCapacity> _ReturnConsumedCapacity;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ProjectionExpression;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> _ExpressionAttributeNames;
  public GetItemInput (dafny.DafnySequence<? extends Character> TableName, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Key, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> AttributesToGet, Wrappers_Compile.Option<Boolean> ConsistentRead, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ProjectionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames) {
    this._TableName = TableName;
    this._Key = Key;
    this._AttributesToGet = AttributesToGet;
    this._ConsistentRead = ConsistentRead;
    this._ReturnConsumedCapacity = ReturnConsumedCapacity;
    this._ProjectionExpression = ProjectionExpression;
    this._ExpressionAttributeNames = ExpressionAttributeNames;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetItemInput o = (GetItemInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._Key, o._Key) && java.util.Objects.equals(this._AttributesToGet, o._AttributesToGet) && java.util.Objects.equals(this._ConsistentRead, o._ConsistentRead) && java.util.Objects.equals(this._ReturnConsumedCapacity, o._ReturnConsumedCapacity) && java.util.Objects.equals(this._ProjectionExpression, o._ProjectionExpression) && java.util.Objects.equals(this._ExpressionAttributeNames, o._ExpressionAttributeNames);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Key);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttributesToGet);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConsistentRead);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnConsumedCapacity);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProjectionExpression);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExpressionAttributeNames);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.GetItemInput.GetItemInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Key));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._AttributesToGet));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConsistentRead));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReturnConsumedCapacity));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProjectionExpression));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExpressionAttributeNames));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetItemInput> _TYPE = dafny.TypeDescriptor.<GetItemInput>referenceWithInitializer(GetItemInput.class, () -> GetItemInput.Default());
  public static dafny.TypeDescriptor<GetItemInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetItemInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetItemInput theDefault = GetItemInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,AttributeValue> empty(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(AttributeNameList._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<ReturnConsumedCapacity>Default(ReturnConsumedCapacity._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AttributeName._typeDescriptor())));
  public static GetItemInput Default() {
    return theDefault;
  }
  public static GetItemInput create(dafny.DafnySequence<? extends Character> TableName, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Key, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> AttributesToGet, Wrappers_Compile.Option<Boolean> ConsistentRead, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ProjectionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames) {
    return new GetItemInput(TableName, Key, AttributesToGet, ConsistentRead, ReturnConsumedCapacity, ProjectionExpression, ExpressionAttributeNames);
  }
  public static GetItemInput create_GetItemInput(dafny.DafnySequence<? extends Character> TableName, dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Key, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> AttributesToGet, Wrappers_Compile.Option<Boolean> ConsistentRead, Wrappers_Compile.Option<ReturnConsumedCapacity> ReturnConsumedCapacity, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ProjectionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames) {
    return create(TableName, Key, AttributesToGet, ConsistentRead, ReturnConsumedCapacity, ProjectionExpression, ExpressionAttributeNames);
  }
  public boolean is_GetItemInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> dtor_Key() {
    return this._Key;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_AttributesToGet() {
    return this._AttributesToGet;
  }
  public Wrappers_Compile.Option<Boolean> dtor_ConsistentRead() {
    return this._ConsistentRead;
  }
  public Wrappers_Compile.Option<ReturnConsumedCapacity> dtor_ReturnConsumedCapacity() {
    return this._ReturnConsumedCapacity;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ProjectionExpression() {
    return this._ProjectionExpression;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> dtor_ExpressionAttributeNames() {
    return this._ExpressionAttributeNames;
  }
}
