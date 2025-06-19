// Class IntermediateKeyWrapping
// Dafny class IntermediateKeyWrapping compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class IntermediateKeyWrapping {
  public DerivationAlgorithm _keyEncryptionKeyKdf;
  public DerivationAlgorithm _macKeyKdf;
  public Encrypt _pdkEncryptAlgorithm;
  public IntermediateKeyWrapping (DerivationAlgorithm keyEncryptionKeyKdf, DerivationAlgorithm macKeyKdf, Encrypt pdkEncryptAlgorithm) {
    this._keyEncryptionKeyKdf = keyEncryptionKeyKdf;
    this._macKeyKdf = macKeyKdf;
    this._pdkEncryptAlgorithm = pdkEncryptAlgorithm;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    IntermediateKeyWrapping o = (IntermediateKeyWrapping)other;
    return true && java.util.Objects.equals(this._keyEncryptionKeyKdf, o._keyEncryptionKeyKdf) && java.util.Objects.equals(this._macKeyKdf, o._macKeyKdf) && java.util.Objects.equals(this._pdkEncryptAlgorithm, o._pdkEncryptAlgorithm);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyEncryptionKeyKdf);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._macKeyKdf);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._pdkEncryptAlgorithm);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.IntermediateKeyWrapping.IntermediateKeyWrapping");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyEncryptionKeyKdf));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._macKeyKdf));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._pdkEncryptAlgorithm));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<IntermediateKeyWrapping> _TYPE = dafny.TypeDescriptor.<IntermediateKeyWrapping>referenceWithInitializer(IntermediateKeyWrapping.class, () -> IntermediateKeyWrapping.Default());
  public static dafny.TypeDescriptor<IntermediateKeyWrapping> _typeDescriptor() {
    return (dafny.TypeDescriptor<IntermediateKeyWrapping>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final IntermediateKeyWrapping theDefault = IntermediateKeyWrapping.create(DerivationAlgorithm.Default(), DerivationAlgorithm.Default(), Encrypt.Default());
  public static IntermediateKeyWrapping Default() {
    return theDefault;
  }
  public static IntermediateKeyWrapping create(DerivationAlgorithm keyEncryptionKeyKdf, DerivationAlgorithm macKeyKdf, Encrypt pdkEncryptAlgorithm) {
    return new IntermediateKeyWrapping(keyEncryptionKeyKdf, macKeyKdf, pdkEncryptAlgorithm);
  }
  public static IntermediateKeyWrapping create_IntermediateKeyWrapping(DerivationAlgorithm keyEncryptionKeyKdf, DerivationAlgorithm macKeyKdf, Encrypt pdkEncryptAlgorithm) {
    return create(keyEncryptionKeyKdf, macKeyKdf, pdkEncryptAlgorithm);
  }
  public boolean is_IntermediateKeyWrapping() { return true; }
  public DerivationAlgorithm dtor_keyEncryptionKeyKdf() {
    return this._keyEncryptionKeyKdf;
  }
  public DerivationAlgorithm dtor_macKeyKdf() {
    return this._macKeyKdf;
  }
  public Encrypt dtor_pdkEncryptAlgorithm() {
    return this._pdkEncryptAlgorithm;
  }
}
