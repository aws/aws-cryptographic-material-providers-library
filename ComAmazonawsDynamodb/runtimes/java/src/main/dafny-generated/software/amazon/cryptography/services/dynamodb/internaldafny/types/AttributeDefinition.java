// Class AttributeDefinition
// Dafny class AttributeDefinition compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AttributeDefinition {
  public dafny.DafnySequence<? extends Character> _AttributeName;
  public ScalarAttributeType _AttributeType;
  public AttributeDefinition (dafny.DafnySequence<? extends Character> AttributeName, ScalarAttributeType AttributeType) {
    this._AttributeName = AttributeName;
    this._AttributeType = AttributeType;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AttributeDefinition o = (AttributeDefinition)other;
    return true && java.util.Objects.equals(this._AttributeName, o._AttributeName) && java.util.Objects.equals(this._AttributeType, o._AttributeType);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttributeName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttributeType);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.AttributeDefinition.AttributeDefinition");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AttributeName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._AttributeType));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AttributeDefinition> _TYPE = dafny.TypeDescriptor.<AttributeDefinition>referenceWithInitializer(AttributeDefinition.class, () -> AttributeDefinition.Default());
  public static dafny.TypeDescriptor<AttributeDefinition> _typeDescriptor() {
    return (dafny.TypeDescriptor<AttributeDefinition>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AttributeDefinition theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeDefinition.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), ScalarAttributeType.Default());
  public static AttributeDefinition Default() {
    return theDefault;
  }
  public static AttributeDefinition create(dafny.DafnySequence<? extends Character> AttributeName, ScalarAttributeType AttributeType) {
    return new AttributeDefinition(AttributeName, AttributeType);
  }
  public static AttributeDefinition create_AttributeDefinition(dafny.DafnySequence<? extends Character> AttributeName, ScalarAttributeType AttributeType) {
    return create(AttributeName, AttributeType);
  }
  public boolean is_AttributeDefinition() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_AttributeName() {
    return this._AttributeName;
  }
  public ScalarAttributeType dtor_AttributeType() {
    return this._AttributeType;
  }
}
