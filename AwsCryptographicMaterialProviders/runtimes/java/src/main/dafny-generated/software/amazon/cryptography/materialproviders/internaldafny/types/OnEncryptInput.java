// Class OnEncryptInput
// Dafny class OnEncryptInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class OnEncryptInput {
  public EncryptionMaterials _materials;
  public OnEncryptInput (EncryptionMaterials materials) {
    this._materials = materials;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    OnEncryptInput o = (OnEncryptInput)other;
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
    s.append("AwsCryptographyMaterialProvidersTypes.OnEncryptInput.OnEncryptInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._materials));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<OnEncryptInput> _TYPE = dafny.TypeDescriptor.<OnEncryptInput>referenceWithInitializer(OnEncryptInput.class, () -> OnEncryptInput.Default());
  public static dafny.TypeDescriptor<OnEncryptInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<OnEncryptInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final OnEncryptInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput.create(EncryptionMaterials.Default());
  public static OnEncryptInput Default() {
    return theDefault;
  }
  public static OnEncryptInput create(EncryptionMaterials materials) {
    return new OnEncryptInput(materials);
  }
  public static OnEncryptInput create_OnEncryptInput(EncryptionMaterials materials) {
    return create(materials);
  }
  public boolean is_OnEncryptInput() { return true; }
  public EncryptionMaterials dtor_materials() {
    return this._materials;
  }
}
