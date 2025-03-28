// Class TagResourceRequest
// Dafny class TagResourceRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class TagResourceRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public dafny.DafnySequence<? extends Tag> _Tags;
  public TagResourceRequest (dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Tag> Tags) {
    this._KeyId = KeyId;
    this._Tags = Tags;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TagResourceRequest o = (TagResourceRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._Tags, o._Tags);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Tags);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.TagResourceRequest.TagResourceRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Tags));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TagResourceRequest> _TYPE = dafny.TypeDescriptor.<TagResourceRequest>referenceWithInitializer(TagResourceRequest.class, () -> TagResourceRequest.Default());
  public static dafny.TypeDescriptor<TagResourceRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<TagResourceRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TagResourceRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.TagResourceRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Tag> empty(Tag._typeDescriptor()));
  public static TagResourceRequest Default() {
    return theDefault;
  }
  public static TagResourceRequest create(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Tag> Tags) {
    return new TagResourceRequest(KeyId, Tags);
  }
  public static TagResourceRequest create_TagResourceRequest(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Tag> Tags) {
    return create(KeyId, Tags);
  }
  public boolean is_TagResourceRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public dafny.DafnySequence<? extends Tag> dtor_Tags() {
    return this._Tags;
  }
}
