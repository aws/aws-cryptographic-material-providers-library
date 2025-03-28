// Class UntagResourceInput
// Dafny class UntagResourceInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class UntagResourceInput {
  public dafny.DafnySequence<? extends Character> _ResourceArn;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _TagKeys;
  public UntagResourceInput (dafny.DafnySequence<? extends Character> ResourceArn, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> TagKeys) {
    this._ResourceArn = ResourceArn;
    this._TagKeys = TagKeys;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UntagResourceInput o = (UntagResourceInput)other;
    return true && java.util.Objects.equals(this._ResourceArn, o._ResourceArn) && java.util.Objects.equals(this._TagKeys, o._TagKeys);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ResourceArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TagKeys);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UntagResourceInput.UntagResourceInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ResourceArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TagKeys));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UntagResourceInput> _TYPE = dafny.TypeDescriptor.<UntagResourceInput>referenceWithInitializer(UntagResourceInput.class, () -> UntagResourceInput.Default());
  public static dafny.TypeDescriptor<UntagResourceInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UntagResourceInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UntagResourceInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.UntagResourceInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(TagKeyString._typeDescriptor()));
  public static UntagResourceInput Default() {
    return theDefault;
  }
  public static UntagResourceInput create(dafny.DafnySequence<? extends Character> ResourceArn, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> TagKeys) {
    return new UntagResourceInput(ResourceArn, TagKeys);
  }
  public static UntagResourceInput create_UntagResourceInput(dafny.DafnySequence<? extends Character> ResourceArn, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> TagKeys) {
    return create(ResourceArn, TagKeys);
  }
  public boolean is_UntagResourceInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_ResourceArn() {
    return this._ResourceArn;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> dtor_TagKeys() {
    return this._TagKeys;
  }
}
