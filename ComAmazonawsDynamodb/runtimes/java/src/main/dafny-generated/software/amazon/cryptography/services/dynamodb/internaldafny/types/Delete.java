// Class Delete
// Dafny class Delete compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class Delete {
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> _Key;
  public dafny.DafnySequence<? extends Character> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ConditionExpression;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> _ExpressionAttributeNames;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _ExpressionAttributeValues;
  public Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> _ReturnValuesOnConditionCheckFailure;
  public Delete (dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Key, dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ConditionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExpressionAttributeValues, Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> ReturnValuesOnConditionCheckFailure) {
    this._Key = Key;
    this._TableName = TableName;
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
    Delete o = (Delete)other;
    return true && java.util.Objects.equals(this._Key, o._Key) && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._ConditionExpression, o._ConditionExpression) && java.util.Objects.equals(this._ExpressionAttributeNames, o._ExpressionAttributeNames) && java.util.Objects.equals(this._ExpressionAttributeValues, o._ExpressionAttributeValues) && java.util.Objects.equals(this._ReturnValuesOnConditionCheckFailure, o._ReturnValuesOnConditionCheckFailure);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Key);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConditionExpression);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExpressionAttributeNames);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExpressionAttributeValues);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReturnValuesOnConditionCheckFailure);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.Delete.Delete");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Key));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableName));
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
  private static final dafny.TypeDescriptor<Delete> _TYPE = dafny.TypeDescriptor.<Delete>referenceWithInitializer(Delete.class, () -> Delete.Default());
  public static dafny.TypeDescriptor<Delete> _typeDescriptor() {
    return (dafny.TypeDescriptor<Delete>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Delete theDefault = Delete.create(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,AttributeValue> empty(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AttributeName._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AttributeValue._typeDescriptor())), Wrappers_Compile.Option.<ReturnValuesOnConditionCheckFailure>Default(ReturnValuesOnConditionCheckFailure._typeDescriptor()));
  public static Delete Default() {
    return theDefault;
  }
  public static Delete create(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Key, dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ConditionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExpressionAttributeValues, Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> ReturnValuesOnConditionCheckFailure) {
    return new Delete(Key, TableName, ConditionExpression, ExpressionAttributeNames, ExpressionAttributeValues, ReturnValuesOnConditionCheckFailure);
  }
  public static Delete create_Delete(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Key, dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ConditionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> ExpressionAttributeValues, Wrappers_Compile.Option<ReturnValuesOnConditionCheckFailure> ReturnValuesOnConditionCheckFailure) {
    return create(Key, TableName, ConditionExpression, ExpressionAttributeNames, ExpressionAttributeValues, ReturnValuesOnConditionCheckFailure);
  }
  public boolean is_Delete() { return true; }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> dtor_Key() {
    return this._Key;
  }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
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
