// Class SerializeKeyDescriptionInput
// Dafny class SerializeKeyDescriptionInput compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class SerializeKeyDescriptionInput {
  public KeyDescription _keyDescription;
  public SerializeKeyDescriptionInput (KeyDescription keyDescription) {
    this._keyDescription = keyDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SerializeKeyDescriptionInput o = (SerializeKeyDescriptionInput)other;
    return true && java.util.Objects.equals(this._keyDescription, o._keyDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.SerializeKeyDescriptionInput.SerializeKeyDescriptionInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<SerializeKeyDescriptionInput> _TYPE = dafny.TypeDescriptor.<SerializeKeyDescriptionInput>referenceWithInitializer(SerializeKeyDescriptionInput.class, () -> SerializeKeyDescriptionInput.Default());
  public static dafny.TypeDescriptor<SerializeKeyDescriptionInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<SerializeKeyDescriptionInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SerializeKeyDescriptionInput theDefault = SerializeKeyDescriptionInput.create(KeyDescription.Default());
  public static SerializeKeyDescriptionInput Default() {
    return theDefault;
  }
  public static SerializeKeyDescriptionInput create(KeyDescription keyDescription) {
    return new SerializeKeyDescriptionInput(keyDescription);
  }
  public static SerializeKeyDescriptionInput create_SerializeKeyDescriptionInput(KeyDescription keyDescription) {
    return create(keyDescription);
  }
  public boolean is_SerializeKeyDescriptionInput() { return true; }
  public KeyDescription dtor_keyDescription() {
    return this._keyDescription;
  }
}
