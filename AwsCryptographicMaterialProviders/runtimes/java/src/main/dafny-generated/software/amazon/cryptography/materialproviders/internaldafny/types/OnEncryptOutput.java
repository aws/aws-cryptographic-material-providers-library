// Class OnEncryptOutput
// Dafny class OnEncryptOutput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class OnEncryptOutput {
  public EncryptionMaterials _materials;
  public OnEncryptOutput (EncryptionMaterials materials) {
    this._materials = materials;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    OnEncryptOutput o = (OnEncryptOutput)other;
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
    s.append("AwsCryptographyMaterialProvidersTypes.OnEncryptOutput.OnEncryptOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._materials));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<OnEncryptOutput> _TYPE = dafny.TypeDescriptor.<OnEncryptOutput>referenceWithInitializer(OnEncryptOutput.class, () -> OnEncryptOutput.Default());
  public static dafny.TypeDescriptor<OnEncryptOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<OnEncryptOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final OnEncryptOutput theDefault = OnEncryptOutput.create(EncryptionMaterials.Default());
  public static OnEncryptOutput Default() {
    return theDefault;
  }
  public static OnEncryptOutput create(EncryptionMaterials materials) {
    return new OnEncryptOutput(materials);
  }
  public static OnEncryptOutput create_OnEncryptOutput(EncryptionMaterials materials) {
    return create(materials);
  }
  public boolean is_OnEncryptOutput() { return true; }
  public EncryptionMaterials dtor_materials() {
    return this._materials;
  }
}
