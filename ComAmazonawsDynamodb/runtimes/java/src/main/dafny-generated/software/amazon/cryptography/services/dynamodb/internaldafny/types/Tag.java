// Class Tag
// Dafny class Tag compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class Tag {
  public dafny.DafnySequence<? extends Character> _Key;
  public dafny.DafnySequence<? extends Character> _Value;
  public Tag (dafny.DafnySequence<? extends Character> Key, dafny.DafnySequence<? extends Character> Value) {
    this._Key = Key;
    this._Value = Value;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Tag o = (Tag)other;
    return true && java.util.Objects.equals(this._Key, o._Key) && java.util.Objects.equals(this._Value, o._Value);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Key);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Value);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.Tag.Tag");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Key));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Value));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Tag> _TYPE = dafny.TypeDescriptor.<Tag>referenceWithInitializer(Tag.class, () -> Tag.Default());
  public static dafny.TypeDescriptor<Tag> _typeDescriptor() {
    return (dafny.TypeDescriptor<Tag>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Tag theDefault = Tag.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static Tag Default() {
    return theDefault;
  }
  public static Tag create(dafny.DafnySequence<? extends Character> Key, dafny.DafnySequence<? extends Character> Value) {
    return new Tag(Key, Value);
  }
  public static Tag create_Tag(dafny.DafnySequence<? extends Character> Key, dafny.DafnySequence<? extends Character> Value) {
    return create(Key, Value);
  }
  public boolean is_Tag() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_Key() {
    return this._Key;
  }
  public dafny.DafnySequence<? extends Character> dtor_Value() {
    return this._Value;
  }
}
