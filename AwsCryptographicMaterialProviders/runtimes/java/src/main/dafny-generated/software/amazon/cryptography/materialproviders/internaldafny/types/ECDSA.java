// Class ECDSA
// Dafny class ECDSA compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ECDSA {
  public software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm _curve;
  public ECDSA (software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm curve) {
    this._curve = curve;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ECDSA o = (ECDSA)other;
    return true && java.util.Objects.equals(this._curve, o._curve);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._curve);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.ECDSA.ECDSA");
    s.append("(");
    s.append(dafny.Helpers.toString(this._curve));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ECDSA> _TYPE = dafny.TypeDescriptor.<ECDSA>referenceWithInitializer(ECDSA.class, () -> ECDSA.Default());
  public static dafny.TypeDescriptor<ECDSA> _typeDescriptor() {
    return (dafny.TypeDescriptor<ECDSA>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ECDSA theDefault = ECDSA.create(software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm.Default());
  public static ECDSA Default() {
    return theDefault;
  }
  public static ECDSA create(software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm curve) {
    return new ECDSA(curve);
  }
  public static ECDSA create_ECDSA(software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm curve) {
    return create(curve);
  }
  public boolean is_ECDSA() { return true; }
  public software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm dtor_curve() {
    return this._curve;
  }
}
