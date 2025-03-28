// Class GetPublicKeyFromPrivateKeyInput
// Dafny class GetPublicKeyFromPrivateKeyInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GetPublicKeyFromPrivateKeyInput {
  public ECDHCurveSpec _eccCurve;
  public ECCPrivateKey _privateKey;
  public GetPublicKeyFromPrivateKeyInput (ECDHCurveSpec eccCurve, ECCPrivateKey privateKey) {
    this._eccCurve = eccCurve;
    this._privateKey = privateKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetPublicKeyFromPrivateKeyInput o = (GetPublicKeyFromPrivateKeyInput)other;
    return true && java.util.Objects.equals(this._eccCurve, o._eccCurve) && java.util.Objects.equals(this._privateKey, o._privateKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._eccCurve);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._privateKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyInput.GetPublicKeyFromPrivateKeyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._eccCurve));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._privateKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetPublicKeyFromPrivateKeyInput> _TYPE = dafny.TypeDescriptor.<GetPublicKeyFromPrivateKeyInput>referenceWithInitializer(GetPublicKeyFromPrivateKeyInput.class, () -> GetPublicKeyFromPrivateKeyInput.Default());
  public static dafny.TypeDescriptor<GetPublicKeyFromPrivateKeyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetPublicKeyFromPrivateKeyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetPublicKeyFromPrivateKeyInput theDefault = software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyInput.create(ECDHCurveSpec.Default(), ECCPrivateKey.Default());
  public static GetPublicKeyFromPrivateKeyInput Default() {
    return theDefault;
  }
  public static GetPublicKeyFromPrivateKeyInput create(ECDHCurveSpec eccCurve, ECCPrivateKey privateKey) {
    return new GetPublicKeyFromPrivateKeyInput(eccCurve, privateKey);
  }
  public static GetPublicKeyFromPrivateKeyInput create_GetPublicKeyFromPrivateKeyInput(ECDHCurveSpec eccCurve, ECCPrivateKey privateKey) {
    return create(eccCurve, privateKey);
  }
  public boolean is_GetPublicKeyFromPrivateKeyInput() { return true; }
  public ECDHCurveSpec dtor_eccCurve() {
    return this._eccCurve;
  }
  public ECCPrivateKey dtor_privateKey() {
    return this._privateKey;
  }
}
