// Class DeriveSharedSecretInput
// Dafny class DeriveSharedSecretInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeriveSharedSecretInput {
  public ECDHCurveSpec _eccCurve;
  public ECCPrivateKey _privateKey;
  public ECCPublicKey _publicKey;
  public DeriveSharedSecretInput (ECDHCurveSpec eccCurve, ECCPrivateKey privateKey, ECCPublicKey publicKey) {
    this._eccCurve = eccCurve;
    this._privateKey = privateKey;
    this._publicKey = publicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeriveSharedSecretInput o = (DeriveSharedSecretInput)other;
    return true && java.util.Objects.equals(this._eccCurve, o._eccCurve) && java.util.Objects.equals(this._privateKey, o._privateKey) && java.util.Objects.equals(this._publicKey, o._publicKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._eccCurve);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._privateKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._publicKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.DeriveSharedSecretInput.DeriveSharedSecretInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._eccCurve));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._privateKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._publicKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeriveSharedSecretInput> _TYPE = dafny.TypeDescriptor.<DeriveSharedSecretInput>referenceWithInitializer(DeriveSharedSecretInput.class, () -> DeriveSharedSecretInput.Default());
  public static dafny.TypeDescriptor<DeriveSharedSecretInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeriveSharedSecretInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeriveSharedSecretInput theDefault = DeriveSharedSecretInput.create(ECDHCurveSpec.Default(), ECCPrivateKey.Default(), ECCPublicKey.Default());
  public static DeriveSharedSecretInput Default() {
    return theDefault;
  }
  public static DeriveSharedSecretInput create(ECDHCurveSpec eccCurve, ECCPrivateKey privateKey, ECCPublicKey publicKey) {
    return new DeriveSharedSecretInput(eccCurve, privateKey, publicKey);
  }
  public static DeriveSharedSecretInput create_DeriveSharedSecretInput(ECDHCurveSpec eccCurve, ECCPrivateKey privateKey, ECCPublicKey publicKey) {
    return create(eccCurve, privateKey, publicKey);
  }
  public boolean is_DeriveSharedSecretInput() { return true; }
  public ECDHCurveSpec dtor_eccCurve() {
    return this._eccCurve;
  }
  public ECCPrivateKey dtor_privateKey() {
    return this._privateKey;
  }
  public ECCPublicKey dtor_publicKey() {
    return this._publicKey;
  }
}
