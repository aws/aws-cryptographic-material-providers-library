// Class UpdateUsageMetadataInput
// Dafny class UpdateUsageMetadataInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateUsageMetadataInput {
  public dafny.DafnySequence<? extends java.lang.Byte> _identifier;
  public int _bytesUsed;
  public UpdateUsageMetadataInput (dafny.DafnySequence<? extends java.lang.Byte> identifier, int bytesUsed) {
    this._identifier = identifier;
    this._bytesUsed = bytesUsed;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateUsageMetadataInput o = (UpdateUsageMetadataInput)other;
    return true && java.util.Objects.equals(this._identifier, o._identifier) && this._bytesUsed == o._bytesUsed;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._identifier);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._bytesUsed);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.UpdateUsageMetadataInput.UpdateUsageMetadataInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._identifier));
    s.append(", ");
    s.append(this._bytesUsed);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateUsageMetadataInput> _TYPE = dafny.TypeDescriptor.<UpdateUsageMetadataInput>referenceWithInitializer(UpdateUsageMetadataInput.class, () -> UpdateUsageMetadataInput.Default());
  public static dafny.TypeDescriptor<UpdateUsageMetadataInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateUsageMetadataInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateUsageMetadataInput theDefault = UpdateUsageMetadataInput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), 0);
  public static UpdateUsageMetadataInput Default() {
    return theDefault;
  }
  public static UpdateUsageMetadataInput create(dafny.DafnySequence<? extends java.lang.Byte> identifier, int bytesUsed) {
    return new UpdateUsageMetadataInput(identifier, bytesUsed);
  }
  public static UpdateUsageMetadataInput create_UpdateUsageMetadataInput(dafny.DafnySequence<? extends java.lang.Byte> identifier, int bytesUsed) {
    return create(identifier, bytesUsed);
  }
  public boolean is_UpdateUsageMetadataInput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_identifier() {
    return this._identifier;
  }
  public int dtor_bytesUsed() {
    return this._bytesUsed;
  }
}
