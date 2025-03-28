// Class DeleteCacheEntryInput
// Dafny class DeleteCacheEntryInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteCacheEntryInput {
  public dafny.DafnySequence<? extends java.lang.Byte> _identifier;
  public DeleteCacheEntryInput (dafny.DafnySequence<? extends java.lang.Byte> identifier) {
    this._identifier = identifier;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteCacheEntryInput o = (DeleteCacheEntryInput)other;
    return true && java.util.Objects.equals(this._identifier, o._identifier);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._identifier);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.DeleteCacheEntryInput.DeleteCacheEntryInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._identifier));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteCacheEntryInput> _TYPE = dafny.TypeDescriptor.<DeleteCacheEntryInput>referenceWithInitializer(DeleteCacheEntryInput.class, () -> DeleteCacheEntryInput.Default());
  public static dafny.TypeDescriptor<DeleteCacheEntryInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteCacheEntryInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteCacheEntryInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static DeleteCacheEntryInput Default() {
    return theDefault;
  }
  public static DeleteCacheEntryInput create(dafny.DafnySequence<? extends java.lang.Byte> identifier) {
    return new DeleteCacheEntryInput(identifier);
  }
  public static DeleteCacheEntryInput create_DeleteCacheEntryInput(dafny.DafnySequence<? extends java.lang.Byte> identifier) {
    return create(identifier);
  }
  public boolean is_DeleteCacheEntryInput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_identifier() {
    return this._identifier;
  }
}
