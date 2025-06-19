// Class KeysAndAttributes
// Dafny class KeysAndAttributes compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeysAndAttributes {
  public dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> _Keys;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _AttributesToGet;
  public Wrappers_Compile.Option<Boolean> _ConsistentRead;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ProjectionExpression;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> _ExpressionAttributeNames;
  public KeysAndAttributes (dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Keys, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> AttributesToGet, Wrappers_Compile.Option<Boolean> ConsistentRead, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ProjectionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames) {
    this._Keys = Keys;
    this._AttributesToGet = AttributesToGet;
    this._ConsistentRead = ConsistentRead;
    this._ProjectionExpression = ProjectionExpression;
    this._ExpressionAttributeNames = ExpressionAttributeNames;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeysAndAttributes o = (KeysAndAttributes)other;
    return true && java.util.Objects.equals(this._Keys, o._Keys) && java.util.Objects.equals(this._AttributesToGet, o._AttributesToGet) && java.util.Objects.equals(this._ConsistentRead, o._ConsistentRead) && java.util.Objects.equals(this._ProjectionExpression, o._ProjectionExpression) && java.util.Objects.equals(this._ExpressionAttributeNames, o._ExpressionAttributeNames);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Keys);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttributesToGet);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ConsistentRead);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProjectionExpression);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExpressionAttributeNames);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.KeysAndAttributes.KeysAndAttributes");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Keys));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._AttributesToGet));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ConsistentRead));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProjectionExpression));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExpressionAttributeNames));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KeysAndAttributes> _TYPE = dafny.TypeDescriptor.<KeysAndAttributes>referenceWithInitializer(KeysAndAttributes.class, () -> KeysAndAttributes.Default());
  public static dafny.TypeDescriptor<KeysAndAttributes> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeysAndAttributes>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeysAndAttributes theDefault = KeysAndAttributes.create(dafny.DafnySequence.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> empty(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, AttributeValue>_typeDescriptor(AttributeName._typeDescriptor(), AttributeValue._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(AttributeNameList._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AttributeName._typeDescriptor())));
  public static KeysAndAttributes Default() {
    return theDefault;
  }
  public static KeysAndAttributes create(dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Keys, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> AttributesToGet, Wrappers_Compile.Option<Boolean> ConsistentRead, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ProjectionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames) {
    return new KeysAndAttributes(Keys, AttributesToGet, ConsistentRead, ProjectionExpression, ExpressionAttributeNames);
  }
  public static KeysAndAttributes create_KeysAndAttributes(dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> Keys, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> AttributesToGet, Wrappers_Compile.Option<Boolean> ConsistentRead, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ProjectionExpression, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> ExpressionAttributeNames) {
    return create(Keys, AttributesToGet, ConsistentRead, ProjectionExpression, ExpressionAttributeNames);
  }
  public boolean is_KeysAndAttributes() { return true; }
  public dafny.DafnySequence<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends AttributeValue>> dtor_Keys() {
    return this._Keys;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_AttributesToGet() {
    return this._AttributesToGet;
  }
  public Wrappers_Compile.Option<Boolean> dtor_ConsistentRead() {
    return this._ConsistentRead;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ProjectionExpression() {
    return this._ProjectionExpression;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>> dtor_ExpressionAttributeNames() {
    return this._ExpressionAttributeNames;
  }
}
