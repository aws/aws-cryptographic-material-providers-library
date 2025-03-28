// Class ValidDecryptionMaterialsTransitionInput
// Dafny class ValidDecryptionMaterialsTransitionInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class ValidDecryptionMaterialsTransitionInput {
  public DecryptionMaterials _start;
  public DecryptionMaterials _stop;
  public ValidDecryptionMaterialsTransitionInput (DecryptionMaterials start, DecryptionMaterials stop) {
    this._start = start;
    this._stop = stop;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ValidDecryptionMaterialsTransitionInput o = (ValidDecryptionMaterialsTransitionInput)other;
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
    s.append("AwsCryptographyMaterialProvidersTypes.ValidDecryptionMaterialsTransitionInput.ValidDecryptionMaterialsTransitionInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._start));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._stop));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ValidDecryptionMaterialsTransitionInput> _TYPE = dafny.TypeDescriptor.<ValidDecryptionMaterialsTransitionInput>referenceWithInitializer(ValidDecryptionMaterialsTransitionInput.class, () -> ValidDecryptionMaterialsTransitionInput.Default());
  public static dafny.TypeDescriptor<ValidDecryptionMaterialsTransitionInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ValidDecryptionMaterialsTransitionInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ValidDecryptionMaterialsTransitionInput theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.ValidDecryptionMaterialsTransitionInput.create(DecryptionMaterials.Default(), DecryptionMaterials.Default());
  public static ValidDecryptionMaterialsTransitionInput Default() {
    return theDefault;
  }
  public static ValidDecryptionMaterialsTransitionInput create(DecryptionMaterials start, DecryptionMaterials stop) {
    return new ValidDecryptionMaterialsTransitionInput(start, stop);
  }
  public static ValidDecryptionMaterialsTransitionInput create_ValidDecryptionMaterialsTransitionInput(DecryptionMaterials start, DecryptionMaterials stop) {
    return create(start, stop);
  }
  public boolean is_ValidDecryptionMaterialsTransitionInput() { return true; }
  public DecryptionMaterials dtor_start() {
    return this._start;
  }
  public DecryptionMaterials dtor_stop() {
    return this._stop;
  }
}
