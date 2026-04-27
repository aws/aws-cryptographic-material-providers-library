// Class KeyringInfo
// Dafny class KeyringInfo compiled into Java
package KeyringFromKeyDescription_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyringInfo {
  public software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _description;
  public Wrappers_Compile.Option<KeyMaterial_Compile.KeyMaterial> _material;
  public KeyringInfo (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription description, Wrappers_Compile.Option<KeyMaterial_Compile.KeyMaterial> material) {
    this._description = description;
    this._material = material;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyringInfo o = (KeyringInfo)other;
    return true && java.util.Objects.equals(this._description, o._description) && java.util.Objects.equals(this._material, o._material);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._description);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._material);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("KeyringFromKeyDescription.KeyringInfo.KeyringInfo");
    s.append("(");
    s.append(dafny.Helpers.toString(this._description));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._material));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KeyringInfo> _TYPE = dafny.TypeDescriptor.<KeyringInfo>referenceWithInitializer(KeyringInfo.class, () -> KeyringInfo.Default());
  public static dafny.TypeDescriptor<KeyringInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyringInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeyringInfo theDefault = KeyringInfo.create(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.Default(), Wrappers_Compile.Option.<KeyMaterial_Compile.KeyMaterial>Default(KeyMaterial_Compile.KeyMaterial._typeDescriptor()));
  public static KeyringInfo Default() {
    return theDefault;
  }
  public static KeyringInfo create(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription description, Wrappers_Compile.Option<KeyMaterial_Compile.KeyMaterial> material) {
    return new KeyringInfo(description, material);
  }
  public static KeyringInfo create_KeyringInfo(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription description, Wrappers_Compile.Option<KeyMaterial_Compile.KeyMaterial> material) {
    return create(description, material);
  }
  public boolean is_KeyringInfo() { return true; }
  public software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription dtor_description() {
    return this._description;
  }
  public Wrappers_Compile.Option<KeyMaterial_Compile.KeyMaterial> dtor_material() {
    return this._material;
  }
}
