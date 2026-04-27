// Class ECDHCurveSpec_ECC__NIST__P521
// Dafny class ECDHCurveSpec_ECC__NIST__P521 compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ECDHCurveSpec_ECC__NIST__P521 extends ECDHCurveSpec {
  public ECDHCurveSpec_ECC__NIST__P521 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ECDHCurveSpec_ECC__NIST__P521 o = (ECDHCurveSpec_ECC__NIST__P521)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.ECDHCurveSpec.ECC_NIST_P521");
    return s.toString();
  }
}
