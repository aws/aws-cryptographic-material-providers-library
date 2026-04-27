// Class GetEncryptionMaterialsOutput
// Dafny class GetEncryptionMaterialsOutput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetEncryptionMaterialsOutput {
  public EncryptionMaterials _encryptionMaterials;
  public GetEncryptionMaterialsOutput (EncryptionMaterials encryptionMaterials) {
    this._encryptionMaterials = encryptionMaterials;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetEncryptionMaterialsOutput o = (GetEncryptionMaterialsOutput)other;
    return true && java.util.Objects.equals(this._encryptionMaterials, o._encryptionMaterials);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionMaterials);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsOutput.GetEncryptionMaterialsOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._encryptionMaterials));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetEncryptionMaterialsOutput> _TYPE = dafny.TypeDescriptor.<GetEncryptionMaterialsOutput>referenceWithInitializer(GetEncryptionMaterialsOutput.class, () -> GetEncryptionMaterialsOutput.Default());
  public static dafny.TypeDescriptor<GetEncryptionMaterialsOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetEncryptionMaterialsOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetEncryptionMaterialsOutput theDefault = GetEncryptionMaterialsOutput.create(EncryptionMaterials.Default());
  public static GetEncryptionMaterialsOutput Default() {
    return theDefault;
  }
  public static GetEncryptionMaterialsOutput create(EncryptionMaterials encryptionMaterials) {
    return new GetEncryptionMaterialsOutput(encryptionMaterials);
  }
  public static GetEncryptionMaterialsOutput create_GetEncryptionMaterialsOutput(EncryptionMaterials encryptionMaterials) {
    return create(encryptionMaterials);
  }
  public boolean is_GetEncryptionMaterialsOutput() { return true; }
  public EncryptionMaterials dtor_encryptionMaterials() {
    return this._encryptionMaterials;
  }
}
