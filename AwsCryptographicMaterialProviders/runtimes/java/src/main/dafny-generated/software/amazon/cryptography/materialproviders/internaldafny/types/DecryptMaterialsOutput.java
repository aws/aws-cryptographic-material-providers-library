// Class DecryptMaterialsOutput
// Dafny class DecryptMaterialsOutput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DecryptMaterialsOutput {
  public DecryptionMaterials _decryptionMaterials;
  public DecryptMaterialsOutput (DecryptionMaterials decryptionMaterials) {
    this._decryptionMaterials = decryptionMaterials;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DecryptMaterialsOutput o = (DecryptMaterialsOutput)other;
    return true && java.util.Objects.equals(this._decryptionMaterials, o._decryptionMaterials);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._decryptionMaterials);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.DecryptMaterialsOutput.DecryptMaterialsOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._decryptionMaterials));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DecryptMaterialsOutput> _TYPE = dafny.TypeDescriptor.<DecryptMaterialsOutput>referenceWithInitializer(DecryptMaterialsOutput.class, () -> DecryptMaterialsOutput.Default());
  public static dafny.TypeDescriptor<DecryptMaterialsOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DecryptMaterialsOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DecryptMaterialsOutput theDefault = DecryptMaterialsOutput.create(DecryptionMaterials.Default());
  public static DecryptMaterialsOutput Default() {
    return theDefault;
  }
  public static DecryptMaterialsOutput create(DecryptionMaterials decryptionMaterials) {
    return new DecryptMaterialsOutput(decryptionMaterials);
  }
  public static DecryptMaterialsOutput create_DecryptMaterialsOutput(DecryptionMaterials decryptionMaterials) {
    return create(decryptionMaterials);
  }
  public boolean is_DecryptMaterialsOutput() { return true; }
  public DecryptionMaterials dtor_decryptionMaterials() {
    return this._decryptionMaterials;
  }
}
