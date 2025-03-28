// Class TagResourceInput
// Dafny class TagResourceInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class TagResourceInput {
  public dafny.DafnySequence<? extends Character> _ResourceArn;
  public dafny.DafnySequence<? extends Tag> _Tags;
  public TagResourceInput (dafny.DafnySequence<? extends Character> ResourceArn, dafny.DafnySequence<? extends Tag> Tags) {
    this._ResourceArn = ResourceArn;
    this._Tags = Tags;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TagResourceInput o = (TagResourceInput)other;
    return true && java.util.Objects.equals(this._ResourceArn, o._ResourceArn) && java.util.Objects.equals(this._Tags, o._Tags);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ResourceArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Tags);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TagResourceInput.TagResourceInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ResourceArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Tags));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TagResourceInput> _TYPE = dafny.TypeDescriptor.<TagResourceInput>referenceWithInitializer(TagResourceInput.class, () -> TagResourceInput.Default());
  public static dafny.TypeDescriptor<TagResourceInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<TagResourceInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TagResourceInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.TagResourceInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Tag> empty(Tag._typeDescriptor()));
  public static TagResourceInput Default() {
    return theDefault;
  }
  public static TagResourceInput create(dafny.DafnySequence<? extends Character> ResourceArn, dafny.DafnySequence<? extends Tag> Tags) {
    return new TagResourceInput(ResourceArn, Tags);
  }
  public static TagResourceInput create_TagResourceInput(dafny.DafnySequence<? extends Character> ResourceArn, dafny.DafnySequence<? extends Tag> Tags) {
    return create(ResourceArn, Tags);
  }
  public boolean is_TagResourceInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_ResourceArn() {
    return this._ResourceArn;
  }
  public dafny.DafnySequence<? extends Tag> dtor_Tags() {
    return this._Tags;
  }
}
