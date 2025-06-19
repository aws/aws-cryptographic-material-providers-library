// Class CreateDefaultCryptographicMaterialsManagerInput
// Dafny class CreateDefaultCryptographicMaterialsManagerInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateDefaultCryptographicMaterialsManagerInput {
  public IKeyring _keyring;
  public CreateDefaultCryptographicMaterialsManagerInput (IKeyring keyring) {
    this._keyring = keyring;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateDefaultCryptographicMaterialsManagerInput o = (CreateDefaultCryptographicMaterialsManagerInput)other;
    return true && this._keyring == o._keyring;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyring);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CreateDefaultCryptographicMaterialsManagerInput.CreateDefaultCryptographicMaterialsManagerInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyring));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateDefaultCryptographicMaterialsManagerInput> _TYPE = dafny.TypeDescriptor.<CreateDefaultCryptographicMaterialsManagerInput>referenceWithInitializer(CreateDefaultCryptographicMaterialsManagerInput.class, () -> CreateDefaultCryptographicMaterialsManagerInput.Default());
  public static dafny.TypeDescriptor<CreateDefaultCryptographicMaterialsManagerInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateDefaultCryptographicMaterialsManagerInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateDefaultCryptographicMaterialsManagerInput theDefault = CreateDefaultCryptographicMaterialsManagerInput.create(null);
  public static CreateDefaultCryptographicMaterialsManagerInput Default() {
    return theDefault;
  }
  public static CreateDefaultCryptographicMaterialsManagerInput create(IKeyring keyring) {
    return new CreateDefaultCryptographicMaterialsManagerInput(keyring);
  }
  public static CreateDefaultCryptographicMaterialsManagerInput create_CreateDefaultCryptographicMaterialsManagerInput(IKeyring keyring) {
    return create(keyring);
  }
  public boolean is_CreateDefaultCryptographicMaterialsManagerInput() { return true; }
  public IKeyring dtor_keyring() {
    return this._keyring;
  }
}
