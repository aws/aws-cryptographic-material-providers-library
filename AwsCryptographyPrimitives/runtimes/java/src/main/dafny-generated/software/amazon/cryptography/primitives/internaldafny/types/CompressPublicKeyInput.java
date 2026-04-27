// Class CompressPublicKeyInput
// Dafny class CompressPublicKeyInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CompressPublicKeyInput {
  public ECCPublicKey _publicKey;
  public ECDHCurveSpec _eccCurve;
  public CompressPublicKeyInput (ECCPublicKey publicKey, ECDHCurveSpec eccCurve) {
    this._publicKey = publicKey;
    this._eccCurve = eccCurve;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CompressPublicKeyInput o = (CompressPublicKeyInput)other;
    return true && java.util.Objects.equals(this._publicKey, o._publicKey) && java.util.Objects.equals(this._eccCurve, o._eccCurve);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._publicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._eccCurve);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.CompressPublicKeyInput.CompressPublicKeyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._publicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._eccCurve));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CompressPublicKeyInput> _TYPE = dafny.TypeDescriptor.<CompressPublicKeyInput>referenceWithInitializer(CompressPublicKeyInput.class, () -> CompressPublicKeyInput.Default());
  public static dafny.TypeDescriptor<CompressPublicKeyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CompressPublicKeyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CompressPublicKeyInput theDefault = CompressPublicKeyInput.create(ECCPublicKey.Default(), ECDHCurveSpec.Default());
  public static CompressPublicKeyInput Default() {
    return theDefault;
  }
  public static CompressPublicKeyInput create(ECCPublicKey publicKey, ECDHCurveSpec eccCurve) {
    return new CompressPublicKeyInput(publicKey, eccCurve);
  }
  public static CompressPublicKeyInput create_CompressPublicKeyInput(ECCPublicKey publicKey, ECDHCurveSpec eccCurve) {
    return create(publicKey, eccCurve);
  }
  public boolean is_CompressPublicKeyInput() { return true; }
  public ECCPublicKey dtor_publicKey() {
    return this._publicKey;
  }
  public ECDHCurveSpec dtor_eccCurve() {
    return this._eccCurve;
  }
}
