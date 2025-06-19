// Class Get
// Dafny class Get compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class Get {
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> _Key;
  public dafny.DafnySequence<? extends Character> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ProjectionExpression;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> _ExpressionAttributeNames;
  public Get (dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Key, dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ProjectionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames) {
    this._Key = Key;
    this._TableName = TableName;
    this._ProjectionExpression = ProjectionExpression;
    this._ExpressionAttributeNames = ExpressionAttributeNames;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Get o = (Get)other;
    return true && java.util.Objects.equals(this._Key, o._Key) && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._ProjectionExpression, o._ProjectionExpression) && java.util.Objects.equals(this._ExpressionAttributeNames, o._ExpressionAttributeNames);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Key);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProjectionExpression);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExpressionAttributeNames);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.Get.Get");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Key));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProjectionExpression));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExpressionAttributeNames));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Get> _TYPE = dafny.TypeDescriptor.<Get>referenceWithInitializer(Get.class, () -> Get.Default());
  public static dafny.TypeDescriptor<Get> _typeDescriptor() {
    return (dafny.TypeDescriptor<Get>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Get theDefault = Get.create(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,AttributeValue> empty(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AttributeName._typeDescriptor())));
  public static Get Default() {
    return theDefault;
  }
  public static Get create(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Key, dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ProjectionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames) {
    return new Get(Key, TableName, ProjectionExpression, ExpressionAttributeNames);
  }
  public static Get create_Get(dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> Key, dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ProjectionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames) {
    return create(Key, TableName, ProjectionExpression, ExpressionAttributeNames);
  }
  public boolean is_Get() { return true; }
  public dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue> dtor_Key() {
    return this._Key;
  }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ProjectionExpression() {
    return this._ProjectionExpression;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> dtor_ExpressionAttributeNames() {
    return this._ExpressionAttributeNames;
  }
}
