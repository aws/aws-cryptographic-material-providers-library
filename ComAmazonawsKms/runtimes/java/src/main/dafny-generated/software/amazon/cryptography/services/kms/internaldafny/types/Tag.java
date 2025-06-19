// Class Tag
// Dafny class Tag compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class Tag {
  public dafny.DafnySequence<? extends Character> _TagKey;
  public dafny.DafnySequence<? extends Character> _TagValue;
  public Tag (dafny.DafnySequence<? extends Character> TagKey, dafny.DafnySequence<? extends Character> TagValue) {
    this._TagKey = TagKey;
    this._TagValue = TagValue;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Tag o = (Tag)other;
    return true && java.util.Objects.equals(this._TagKey, o._TagKey) && java.util.Objects.equals(this._TagValue, o._TagValue);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TagKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TagValue);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.Tag.Tag");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TagKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TagValue));
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
  public static Tag create(dafny.DafnySequence<? extends Character> TagKey, dafny.DafnySequence<? extends Character> TagValue) {
    return new Tag(TagKey, TagValue);
  }
  public static Tag create_Tag(dafny.DafnySequence<? extends Character> TagKey, dafny.DafnySequence<? extends Character> TagValue) {
    return create(TagKey, TagValue);
  }
  public boolean is_Tag() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TagKey() {
    return this._TagKey;
  }
  public dafny.DafnySequence<? extends Character> dtor_TagValue() {
    return this._TagValue;
  }
}
