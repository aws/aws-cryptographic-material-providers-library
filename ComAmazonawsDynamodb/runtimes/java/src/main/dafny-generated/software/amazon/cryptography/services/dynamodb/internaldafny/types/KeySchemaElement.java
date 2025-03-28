// Class KeySchemaElement
// Dafny class KeySchemaElement compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class KeySchemaElement {
  public dafny.DafnySequence<? extends Character> _AttributeName;
  public KeyType _KeyType;
  public KeySchemaElement (dafny.DafnySequence<? extends Character> AttributeName, KeyType KeyType) {
    this._AttributeName = AttributeName;
    this._KeyType = KeyType;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeySchemaElement o = (KeySchemaElement)other;
    return true && java.util.Objects.equals(this._AttributeName, o._AttributeName) && java.util.Objects.equals(this._KeyType, o._KeyType);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttributeName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyType);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.KeySchemaElement.KeySchemaElement");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AttributeName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyType));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KeySchemaElement> _TYPE = dafny.TypeDescriptor.<KeySchemaElement>referenceWithInitializer(KeySchemaElement.class, () -> KeySchemaElement.Default());
  public static dafny.TypeDescriptor<KeySchemaElement> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeySchemaElement>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeySchemaElement theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.KeySchemaElement.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), KeyType.Default());
  public static KeySchemaElement Default() {
    return theDefault;
  }
  public static KeySchemaElement create(dafny.DafnySequence<? extends Character> AttributeName, KeyType KeyType) {
    return new KeySchemaElement(AttributeName, KeyType);
  }
  public static KeySchemaElement create_KeySchemaElement(dafny.DafnySequence<? extends Character> AttributeName, KeyType KeyType) {
    return create(AttributeName, KeyType);
  }
  public boolean is_KeySchemaElement() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_AttributeName() {
    return this._AttributeName;
  }
  public KeyType dtor_KeyType() {
    return this._KeyType;
  }
}
