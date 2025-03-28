// Class AttributeValueUpdate
// Dafny class AttributeValueUpdate compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AttributeValueUpdate {
  public Wrappers_Compile.Option<AttributeValue> _Value;
  public Wrappers_Compile.Option<AttributeAction> _Action;
  public AttributeValueUpdate (Wrappers_Compile.Option<AttributeValue> Value, Wrappers_Compile.Option<AttributeAction> Action) {
    this._Value = Value;
    this._Action = Action;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AttributeValueUpdate o = (AttributeValueUpdate)other;
    return true && java.util.Objects.equals(this._Value, o._Value) && java.util.Objects.equals(this._Action, o._Action);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Value);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Action);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.AttributeValueUpdate.AttributeValueUpdate");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Value));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Action));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AttributeValueUpdate> _TYPE = dafny.TypeDescriptor.<AttributeValueUpdate>referenceWithInitializer(AttributeValueUpdate.class, () -> AttributeValueUpdate.Default());
  public static dafny.TypeDescriptor<AttributeValueUpdate> _typeDescriptor() {
    return (dafny.TypeDescriptor<AttributeValueUpdate>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AttributeValueUpdate theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValueUpdate.create(Wrappers_Compile.Option.<AttributeValue>Default(AttributeValue._typeDescriptor()), Wrappers_Compile.Option.<AttributeAction>Default(AttributeAction._typeDescriptor()));
  public static AttributeValueUpdate Default() {
    return theDefault;
  }
  public static AttributeValueUpdate create(Wrappers_Compile.Option<AttributeValue> Value, Wrappers_Compile.Option<AttributeAction> Action) {
    return new AttributeValueUpdate(Value, Action);
  }
  public static AttributeValueUpdate create_AttributeValueUpdate(Wrappers_Compile.Option<AttributeValue> Value, Wrappers_Compile.Option<AttributeAction> Action) {
    return create(Value, Action);
  }
  public boolean is_AttributeValueUpdate() { return true; }
  public Wrappers_Compile.Option<AttributeValue> dtor_Value() {
    return this._Value;
  }
  public Wrappers_Compile.Option<AttributeAction> dtor_Action() {
    return this._Action;
  }
}
