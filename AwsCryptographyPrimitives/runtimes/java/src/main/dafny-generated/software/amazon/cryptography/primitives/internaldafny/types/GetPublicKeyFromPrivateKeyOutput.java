// Class GetPublicKeyFromPrivateKeyOutput
// Dafny class GetPublicKeyFromPrivateKeyOutput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GetPublicKeyFromPrivateKeyOutput {
  public ECDHCurveSpec _eccCurve;
  public ECCPrivateKey _privateKey;
  public dafny.DafnySequence<? extends java.lang.Byte> _publicKey;
  public GetPublicKeyFromPrivateKeyOutput (ECDHCurveSpec eccCurve, ECCPrivateKey privateKey, dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    this._eccCurve = eccCurve;
    this._privateKey = privateKey;
    this._publicKey = publicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetPublicKeyFromPrivateKeyOutput o = (GetPublicKeyFromPrivateKeyOutput)other;
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
    s.append("AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyOutput.GetPublicKeyFromPrivateKeyOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._eccCurve));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._privateKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._publicKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetPublicKeyFromPrivateKeyOutput> _TYPE = dafny.TypeDescriptor.<GetPublicKeyFromPrivateKeyOutput>referenceWithInitializer(GetPublicKeyFromPrivateKeyOutput.class, () -> GetPublicKeyFromPrivateKeyOutput.Default());
  public static dafny.TypeDescriptor<GetPublicKeyFromPrivateKeyOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetPublicKeyFromPrivateKeyOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetPublicKeyFromPrivateKeyOutput theDefault = software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput.create(ECDHCurveSpec.Default(), ECCPrivateKey.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static GetPublicKeyFromPrivateKeyOutput Default() {
    return theDefault;
  }
  public static GetPublicKeyFromPrivateKeyOutput create(ECDHCurveSpec eccCurve, ECCPrivateKey privateKey, dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    return new GetPublicKeyFromPrivateKeyOutput(eccCurve, privateKey, publicKey);
  }
  public static GetPublicKeyFromPrivateKeyOutput create_GetPublicKeyFromPrivateKeyOutput(ECDHCurveSpec eccCurve, ECCPrivateKey privateKey, dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    return create(eccCurve, privateKey, publicKey);
  }
  public boolean is_GetPublicKeyFromPrivateKeyOutput() { return true; }
  public ECDHCurveSpec dtor_eccCurve() {
    return this._eccCurve;
  }
  public ECCPrivateKey dtor_privateKey() {
    return this._privateKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_publicKey() {
    return this._publicKey;
  }
}
