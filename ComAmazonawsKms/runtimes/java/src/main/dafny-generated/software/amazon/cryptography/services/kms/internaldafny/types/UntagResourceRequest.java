// Class UntagResourceRequest
// Dafny class UntagResourceRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class UntagResourceRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _TagKeys;
  public UntagResourceRequest (dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> TagKeys) {
    this._KeyId = KeyId;
    this._TagKeys = TagKeys;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UntagResourceRequest o = (UntagResourceRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._TagKeys, o._TagKeys);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TagKeys);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.UntagResourceRequest.UntagResourceRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TagKeys));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UntagResourceRequest> _TYPE = dafny.TypeDescriptor.<UntagResourceRequest>referenceWithInitializer(UntagResourceRequest.class, () -> UntagResourceRequest.Default());
  public static dafny.TypeDescriptor<UntagResourceRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<UntagResourceRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UntagResourceRequest theDefault = UntagResourceRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(TagKeyType._typeDescriptor()));
  public static UntagResourceRequest Default() {
    return theDefault;
  }
  public static UntagResourceRequest create(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> TagKeys) {
    return new UntagResourceRequest(KeyId, TagKeys);
  }
  public static UntagResourceRequest create_UntagResourceRequest(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> TagKeys) {
    return create(KeyId, TagKeys);
  }
  public boolean is_UntagResourceRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> dtor_TagKeys() {
    return this._TagKeys;
  }
}
