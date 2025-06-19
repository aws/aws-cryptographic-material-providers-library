// Class OnDecryptOutput
// Dafny class OnDecryptOutput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class OnDecryptOutput {
  public DecryptionMaterials _materials;
  public OnDecryptOutput (DecryptionMaterials materials) {
    this._materials = materials;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    OnDecryptOutput o = (OnDecryptOutput)other;
    return true && java.util.Objects.equals(this._materials, o._materials);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._materials);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.OnDecryptOutput.OnDecryptOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._materials));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<OnDecryptOutput> _TYPE = dafny.TypeDescriptor.<OnDecryptOutput>referenceWithInitializer(OnDecryptOutput.class, () -> OnDecryptOutput.Default());
  public static dafny.TypeDescriptor<OnDecryptOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<OnDecryptOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final OnDecryptOutput theDefault = OnDecryptOutput.create(DecryptionMaterials.Default());
  public static OnDecryptOutput Default() {
    return theDefault;
  }
  public static OnDecryptOutput create(DecryptionMaterials materials) {
    return new OnDecryptOutput(materials);
  }
  public static OnDecryptOutput create_OnDecryptOutput(DecryptionMaterials materials) {
    return create(materials);
  }
  public boolean is_OnDecryptOutput() { return true; }
  public DecryptionMaterials dtor_materials() {
    return this._materials;
  }
}
