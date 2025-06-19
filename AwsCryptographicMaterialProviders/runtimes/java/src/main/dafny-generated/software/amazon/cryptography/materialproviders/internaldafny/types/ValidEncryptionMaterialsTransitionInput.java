// Class ValidEncryptionMaterialsTransitionInput
// Dafny class ValidEncryptionMaterialsTransitionInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ValidEncryptionMaterialsTransitionInput {
  public EncryptionMaterials _start;
  public EncryptionMaterials _stop;
  public ValidEncryptionMaterialsTransitionInput (EncryptionMaterials start, EncryptionMaterials stop) {
    this._start = start;
    this._stop = stop;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ValidEncryptionMaterialsTransitionInput o = (ValidEncryptionMaterialsTransitionInput)other;
    return true && java.util.Objects.equals(this._start, o._start) && java.util.Objects.equals(this._stop, o._stop);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._start);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._stop);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.ValidEncryptionMaterialsTransitionInput.ValidEncryptionMaterialsTransitionInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._start));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._stop));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ValidEncryptionMaterialsTransitionInput> _TYPE = dafny.TypeDescriptor.<ValidEncryptionMaterialsTransitionInput>referenceWithInitializer(ValidEncryptionMaterialsTransitionInput.class, () -> ValidEncryptionMaterialsTransitionInput.Default());
  public static dafny.TypeDescriptor<ValidEncryptionMaterialsTransitionInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ValidEncryptionMaterialsTransitionInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ValidEncryptionMaterialsTransitionInput theDefault = ValidEncryptionMaterialsTransitionInput.create(EncryptionMaterials.Default(), EncryptionMaterials.Default());
  public static ValidEncryptionMaterialsTransitionInput Default() {
    return theDefault;
  }
  public static ValidEncryptionMaterialsTransitionInput create(EncryptionMaterials start, EncryptionMaterials stop) {
    return new ValidEncryptionMaterialsTransitionInput(start, stop);
  }
  public static ValidEncryptionMaterialsTransitionInput create_ValidEncryptionMaterialsTransitionInput(EncryptionMaterials start, EncryptionMaterials stop) {
    return create(start, stop);
  }
  public boolean is_ValidEncryptionMaterialsTransitionInput() { return true; }
  public EncryptionMaterials dtor_start() {
    return this._start;
  }
  public EncryptionMaterials dtor_stop() {
    return this._stop;
  }
}
